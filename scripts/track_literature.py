#!/usr/bin/env python3
"""Daily LLM service-operations literature tracker.

Uses only the Python standard library. It queries arXiv and OpenAlex, applies a
configurable relevance/quality filter, deduplicates results, and writes both a
Markdown report and a small static HTML site.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import html
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "llm_service_ops.json"
INDEX_TEMPLATE = ROOT / "templates" / "index.html"
ANALYSIS_CACHE = ROOT / "data" / "paper_analysis_zh.json"
CONFIRMED_PAPERS = ROOT / "data" / "confirmed_papers.json"
USER_AGENT = "llm-service-ops-literature-tracker/1.0"


@dataclasses.dataclass
class Paper:
    title: str
    authors: list[str]
    abstract: str
    published: str
    updated: str
    venue: str
    url: str
    pdf_url: str = ""
    doi: str = ""
    source: str = ""
    external_id: str = ""
    category_id: str = ""
    category_name: str = ""
    track: str = ""
    relevance_score: int = 0
    matched_terms: list[str] = dataclasses.field(default_factory=list)


def compact_space(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", compact_space(value).lower())


def contains_phrase(text: str, phrase: str) -> bool:
    text = text.lower()
    phrase = phrase.lower().strip()
    if not phrase:
        return False
    if re.fullmatch(r"[a-z0-9]+", phrase):
        return re.search(rf"(?<![a-z0-9]){re.escape(phrase)}(?![a-z0-9])", text) is not None
    return phrase in text


def matched_phrases(text: str, phrases: Iterable[str]) -> list[str]:
    return [phrase for phrase in phrases if contains_phrase(text, phrase)]


def request_bytes(url: str, *, attempts: int = 3) -> bytes:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, application/atom+xml, text/xml;q=0.9, */*;q=0.8",
    }
    email = os.environ.get("OPENALEX_EMAIL", "").strip()
    if email:
        headers["From"] = email
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=35) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(2**attempt)
    raise RuntimeError(f"Request failed after {attempts} attempts: {url}\n{last_error}")


def parse_iso_date(value: str) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return dt.date.fromisoformat(value[:10])
        except ValueError:
            return None


def fetch_arxiv(query: str, start_date: dt.date, end_date: dt.date, max_results: int) -> list[Paper]:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "lastUpdatedDate",
            "sortOrder": "descending",
        }
    )
    raw = request_bytes(f"https://export.arxiv.org/api/query?{params}")
    root = ET.fromstring(raw)
    atom = "{http://www.w3.org/2005/Atom}"
    papers: list[Paper] = []
    for entry in root.findall(f"{atom}entry"):
        published = compact_space(entry.findtext(f"{atom}published", ""))
        updated = compact_space(entry.findtext(f"{atom}updated", ""))
        activity_dates = [d for d in (parse_iso_date(published), parse_iso_date(updated)) if d]
        if not activity_dates or max(activity_dates) < start_date or max(activity_dates) > end_date:
            continue
        entry_url = compact_space(entry.findtext(f"{atom}id", ""))
        pdf_url = ""
        for link in entry.findall(f"{atom}link"):
            if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                pdf_url = link.attrib.get("href", "")
                break
        papers.append(
            Paper(
                title=compact_space(entry.findtext(f"{atom}title", "")),
                authors=[compact_space(a.findtext(f"{atom}name", "")) for a in entry.findall(f"{atom}author")],
                abstract=compact_space(entry.findtext(f"{atom}summary", "")),
                published=published[:10],
                updated=updated[:10],
                venue="arXiv",
                url=entry_url,
                pdf_url=pdf_url,
                source="arXiv",
                external_id=entry_url.rsplit("/", 1)[-1],
            )
        )
    return papers


def abstract_from_inverted_index(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, word_positions in index.items():
        positions.extend((position, word) for position in word_positions)
    return compact_space(" ".join(word for _, word in sorted(positions)))


def fetch_openalex(query: str, start_date: dt.date, end_date: dt.date, max_results: int) -> list[Paper]:
    filters = f"from_publication_date:{start_date.isoformat()},to_publication_date:{end_date.isoformat()}"
    params = {
        "search": query,
        "filter": filters,
        "sort": "publication_date:desc",
        "per-page": min(max_results, 100),
        "select": "id,doi,title,publication_date,authorships,abstract_inverted_index,primary_location,best_oa_location",
    }
    email = os.environ.get("OPENALEX_EMAIL", "").strip()
    if email:
        params["mailto"] = email
    raw = request_bytes("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
    results = json.loads(raw.decode("utf-8")).get("results", [])
    papers: list[Paper] = []
    for work in results:
        primary = work.get("primary_location") or {}
        best_oa = work.get("best_oa_location") or {}
        source_info = primary.get("source") or {}
        doi = (work.get("doi") or "").replace("https://doi.org/", "")
        landing = primary.get("landing_page_url") or best_oa.get("landing_page_url") or work.get("id", "")
        pdf_url = best_oa.get("pdf_url") or primary.get("pdf_url") or ""
        authors = [
            compact_space((authorship.get("author") or {}).get("display_name", ""))
            for authorship in work.get("authorships", [])
        ]
        papers.append(
            Paper(
                title=compact_space(work.get("title", "")),
                authors=[author for author in authors if author],
                abstract=abstract_from_inverted_index(work.get("abstract_inverted_index")),
                published=work.get("publication_date") or "",
                updated=work.get("publication_date") or "",
                venue=compact_space(source_info.get("display_name", "")) or "OpenAlex indexed work",
                url=landing,
                pdf_url=pdf_url,
                doi=doi,
                source="OpenAlex",
                external_id=(work.get("id") or "").rsplit("/", 1)[-1],
            )
        )
    return papers


def venue_is_quality(venue: str, config: dict[str, Any]) -> bool:
    venue_key = compact_space(venue).casefold()
    return bool(venue_key) and any(
        venue_key == compact_space(name).casefold() for name in config["quality_venues"]
    )


def score_paper(paper: Paper, config: dict[str, Any], *, analog_query: bool = False) -> Paper | None:
    text = compact_space(f"{paper.title} {paper.abstract}").lower()
    context_hits = matched_phrases(text, config["direct_llm_terms"])
    method_hits = matched_phrases(text, config["method_terms"])
    operational_hits = matched_phrases(text, config.get("service_operational_terms", []))
    exclusion_hits = matched_phrases(text, config["exclusion_terms"])
    category_rankings: list[tuple[int, int, dict[str, Any], list[str], list[str]]] = []
    for index, category in enumerate(config["categories"]):
        strong_hits = matched_phrases(text, category["terms"])
        weak_hits = matched_phrases(text, category.get("weak_terms", []))
        category_score = len(strong_hits) * int(category.get("weight", 1)) + len(weak_hits)
        category_rankings.append((category_score, -index, category, strong_hits, weak_hits))
    category_score, _, category, strong_category_hits, weak_category_hits = max(
        category_rankings, key=lambda item: (item[0], item[1])
    )
    category_hits = strong_category_hits + weak_category_hits
    if not category_hits:
        return None

    quality = venue_is_quality(paper.venue, config)
    if context_hits:
        if not strong_category_hits and len(operational_hits) < 2:
            return None
        track = "直接 LLM 服务研究"
        score = min(6, 3 + 2 * len(context_hits)) + category_score + min(2, len(method_hits))
    else:
        if not config.get("include_service_analogs") or not analog_query or not quality:
            return None
        if len(category_hits) < 2 and not method_hits:
            return None
        track = "高质量服务运营机制桥接"
        score = category_score + min(3, len(method_hits)) + 3

    score += 2 if quality else 0
    score -= 3 * len(exclusion_hits)
    if score < int(config["min_relevance_score"]):
        return None

    paper.category_id = category["id"]
    paper.category_name = category["name"]
    paper.track = track
    paper.relevance_score = score
    paper.matched_terms = list(dict.fromkeys(context_hits + category_hits + method_hits + operational_hits))[:10]
    return paper


def merge_papers(papers: Iterable[Paper]) -> list[Paper]:
    merged: dict[str, Paper] = {}
    title_aliases: dict[str, str] = {}
    for paper in papers:
        doi_key = f"doi:{paper.doi.lower()}" if paper.doi else ""
        title_key = f"title:{normalized_title(paper.title)}"
        key = doi_key or title_aliases.get(title_key) or title_key
        if key not in merged:
            merged[key] = paper
            title_aliases[title_key] = key
            continue
        existing = merged[key]
        if len(paper.abstract) > len(existing.abstract):
            existing.abstract = paper.abstract
        if paper.doi and not existing.doi:
            existing.doi = paper.doi
        if paper.pdf_url and not existing.pdf_url:
            existing.pdf_url = paper.pdf_url
        if paper.url and (not existing.url or existing.source == "OpenAlex"):
            existing.url = paper.url
        existing.authors = existing.authors or paper.authors
        existing.venue = existing.venue if existing.venue != "arXiv" else paper.venue
        existing.source = "+".join(sorted(set(existing.source.split("+") + paper.source.split("+"))))
        if paper.relevance_score > existing.relevance_score:
            existing.category_id = paper.category_id
            existing.category_name = paper.category_name
            existing.track = paper.track
            existing.relevance_score = paper.relevance_score
        existing.matched_terms = list(dict.fromkeys(existing.matched_terms + paper.matched_terms))[:10]
    return sorted(merged.values(), key=lambda p: (-p.relevance_score, p.category_name, p.title.lower()))


def category_reason(category_id: str, config: dict[str, Any]) -> str:
    for category in config["categories"]:
        if category["id"] == category_id:
            return category["reason"]
    return ""


def paper_links_markdown(paper: Paper) -> str:
    links = [f"[论文页]({paper.url})"] if paper.url else []
    if paper.pdf_url:
        links.append(f"[PDF]({paper.pdf_url})")
    if paper.doi:
        links.append(f"[DOI](https://doi.org/{paper.doi})")
    return " · ".join(links)


def display_dates(paper: Paper) -> str:
    if paper.published and paper.updated and paper.published != paper.updated:
        return f"首次发布 {paper.published}；最近更新 {paper.updated}"
    return paper.published or paper.updated or "日期未提供"


def stable_anchor(paper: Paper) -> str:
    return "paper-" + hashlib.sha1(normalized_title(paper.title).encode("utf-8")).hexdigest()[:10]


def load_analysis_cache(path: Path = ANALYSIS_CACHE) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return loaded if isinstance(loaded, dict) else {}


def load_confirmed_papers(
    report_date: dt.date,
    path: Path = CONFIRMED_PAPERS,
) -> list[Paper]:
    """Load manually confirmed papers so a temporary source outage cannot erase a published daily report."""
    if not path.exists():
        return []
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    records = loaded.get(report_date.isoformat(), []) if isinstance(loaded, dict) else []
    field_names = {field.name for field in dataclasses.fields(Paper)}
    papers = []
    for record in records:
        if not isinstance(record, dict):
            continue
        values = {key: value for key, value in record.items() if key in field_names}
        if values.get("title"):
            papers.append(Paper(**values))
    return papers


def fallback_analysis(paper: Paper, config: dict[str, Any]) -> dict[str, Any]:
    relation = category_reason(paper.category_id, config)
    return {
        "title_zh": paper.title,
        "analysis_type": "待全文核验",
        "research_question": f"这篇论文讨论与“{paper.category_name}”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？",
        "method": "当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。",
        "research_insight": relation or "需要阅读全文后判断它与我们的定价、排队、优先权和容量研究有何关系。",
        "one_line": relation or "该论文命中 LLM 服务运营主题，但中文深度分析尚待全文核验。",
        "chinese_abstract": "中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。",
        "model_summary": "模型设定尚待全文核验。",
        "participants": ["尚待全文核验"],
        "decisions": ["尚待全文核验"],
        "primitives": ["尚待全文核验"],
        "sequence": ["获取全文", "核验模型设定与公式", "生成中文研究解读"],
        "equations": [],
        "solution": "尚待全文核验。",
        "findings": ["尚待全文核验"],
        "limitations": ["当前仅凭题录或摘要，不能可靠复原模型。"],
        "verification": "未完成全文核验；英文原摘要仅作为补充材料展示。",
    }


def analysis_for(
    paper: Paper,
    config: dict[str, Any],
    analyses: dict[str, dict[str, Any]] | None,
) -> dict[str, Any]:
    return (analyses or {}).get(stable_anchor(paper)) or fallback_analysis(paper, config)


def extract_pdf_text(paper: Paper, max_chars: int = 60000) -> str:
    """Download and extract a paper when pypdf is available; fail closed to the abstract."""
    if not paper.pdf_url:
        return ""
    try:
        import pypdf  # type: ignore
    except ImportError:
        return ""
    urls = [paper.pdf_url]
    if "arxiv.org/pdf/" in paper.pdf_url:
        urls.append(paper.pdf_url.replace("https://arxiv.org/pdf/", "https://export.arxiv.org/pdf/"))
    raw = b""
    for url in dict.fromkeys(urls):
        try:
            candidate = request_bytes(url, attempts=2)
            if candidate.startswith(b"%PDF-"):
                raw = candidate
                break
        except RuntimeError:
            continue
    if not raw:
        return ""
    try:
        reader = pypdf.PdfReader(io.BytesIO(raw))
        text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:
        return ""
    return compact_space(text)[:max_chars]


def analysis_json_schema() -> dict[str, Any]:
    text_array = {"type": "array", "items": {"type": "string"}}
    equation = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "label": {"type": "string"},
            "latex": {"type": "string"},
            "explanation": {"type": "string"},
        },
        "required": ["label", "latex", "explanation"],
    }
    properties: dict[str, Any] = {
        "title_zh": {"type": "string"},
        "analysis_type": {"type": "string"},
        "research_question": {"type": "string"},
        "method": {"type": "string"},
        "research_insight": {"type": "string"},
        "one_line": {"type": "string"},
        "chinese_abstract": {"type": "string"},
        "model_summary": {"type": "string"},
        "participants": text_array,
        "decisions": text_array,
        "primitives": text_array,
        "sequence": text_array,
        "equations": {"type": "array", "items": equation},
        "solution": {"type": "string"},
        "findings": text_array,
        "limitations": text_array,
        "verification": {"type": "string"},
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": properties,
        "required": list(properties),
    }


def generate_chinese_analysis(paper: Paper, config: dict[str, Any], api_key: str) -> dict[str, Any]:
    full_text = extract_pdf_text(paper)
    evidence = full_text or paper.abstract
    evidence_label = "论文全文提取文本" if full_text else "数据源摘要（不得据此虚构未出现的公式）"
    prompt = f"""请用中文分析下面的学术论文，服务于 LLM 服务运营、Token/API 定价、排队调度、优先权/SLO、GPU 容量与平台机制研究。
必须遵守：假设读者刚接触这个方向，不熟悉经济学、运筹学或计算机系统术语；先用日常语言讲清楚，再在括号中补充必要的专业名词。避免连续堆砌术语，每出现一个不可避免的专业词，都要立即解释它在这篇论文里是什么意思。研究问题只写一句话；“文章怎么做”必须说明作者先做什么、再做什么、最后得到什么；重点复原参与者、决策、参数、时序、目标函数/约束、求解方法和主要结论；公式说明必须逐个解释符号以及公式想表达的直观意思；只写证据支持的公式；明确它与我们研究的关系和核验边界。英文仅可作为专有名词补充。

标题：{paper.title}
作者：{', '.join(paper.authors)}
来源：{paper.venue} / {paper.source}
分类提示：{paper.category_name}；{category_reason(paper.category_id, config)}
证据口径：{evidence_label}
证据文本：
{evidence}
"""
    model = os.environ.get("OPENAI_ANALYSIS_MODEL", "gpt-5.6-luna").strip() or "gpt-5.6-luna"
    payload = {
        "model": model,
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": "你是擅长给初学者讲论文的运营管理与服务系统分析员。用普通读者能看懂的中文表达，先讲直观含义，再补专业术语；所有主要内容必须使用中文，绝不补写证据未支持的模型细节。"}]},
            {"role": "user", "content": [{"type": "input_text", "text": prompt}]},
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "chinese_paper_analysis",
                "strict": True,
                "schema": analysis_json_schema(),
            }
        },
        "max_output_tokens": 7000,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        result = json.loads(response.read().decode("utf-8"))
    output_text = result.get("output_text", "")
    if not output_text:
        for item in result.get("output", []):
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    output_text += content.get("text", "")
    parsed = json.loads(output_text)
    if not isinstance(parsed, dict):
        raise ValueError("OpenAI analysis response was not a JSON object")
    return parsed


def ensure_chinese_analyses(
    papers: list[Paper],
    config: dict[str, Any],
    cache_path: Path = ANALYSIS_CACHE,
) -> dict[str, dict[str, Any]]:
    analyses = load_analysis_cache(cache_path)
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    changed = False
    if api_key:
        for paper in papers:
            key = stable_anchor(paper)
            if key in analyses:
                continue
            try:
                analyses[key] = generate_chinese_analysis(paper, config, api_key)
                changed = True
            except Exception as exc:
                print(f"WARNING: Chinese analysis failed for {paper.title}: {exc}", file=sys.stderr)
    if changed:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(analyses, ensure_ascii=False, indent=2), encoding="utf-8")
    return analyses


def _legacy_build_markdown(
    papers: list[Paper],
    config: dict[str, Any],
    report_date: dt.date,
    start_date: dt.date,
    analyses: dict[str, dict[str, Any]] | None = None,
) -> str:
    direct = sum(p.track.startswith("直接") for p in papers)
    analog = len(papers) - direct
    source_counts = Counter(p.source for p in papers)
    lines = [
        f"# {report_date.isoformat()} LLM 服务系统每日文献简报",
        "",
        f"> 检索窗口：{start_date.isoformat()} 至 {report_date.isoformat()}（{config['timezone']}）；"
        f"共保留 {len(papers)} 篇，其中直接 LLM 服务研究 {direct} 篇、服务运营机制桥接 {analog} 篇。",
        "",
        "## 今日概览",
        "",
        f"- 来源：{', '.join(f'{name} {count}' for name, count in sorted(source_counts.items())) or '无命中'}",
        f"- 筛选门槛：相关性评分 ≥ {config['min_relevance_score']}；机制桥接条目必须来自质量期刊白名单。",
        "- 研究主线：Token 定价；推理排队与调度；优先权/SLO；容量与云资源；能源约束；平台机制。",
        "",
    ]
    grouped: dict[str, list[Paper]] = defaultdict(list)
    for paper in papers:
        grouped[paper.category_name].append(paper)
    if not papers:
        lines += ["本检索窗口没有达到门槛的新论文。", ""]
    for category in config["categories"]:
        category_papers = grouped.get(category["name"], [])
        if not category_papers:
            continue
        lines += [f"## {category['name']}（{len(category_papers)}）", ""]
        for index, paper in enumerate(category_papers, 1):
            authors = ", ".join(paper.authors[:8]) or "作者信息未提供"
            if len(paper.authors) > 8:
                authors += " et al."
            abstract = paper.abstract or "来源未提供摘要；建议打开论文页人工核验。"
            lines += [
                f"### {index}. {paper.title}",
                "",
                f"- **作者：** {authors}",
                f"- **来源/日期：** {paper.venue}；{display_dates(paper)}；{paper.source}",
                f"- **追踪线：** {paper.track}；相关性评分 {paper.relevance_score}",
                f"- **命中词：** {', '.join(paper.matched_terms)}",
                f"- **与项目的关系：** {category_reason(paper.category_id, config)}",
                f"- **摘要：** {abstract}",
                f"- **链接：** {paper_links_markdown(paper)}",
                "",
            ]
    lines += [
        "## 核验说明",
        "",
        "- 本报告的题录与摘要来自 arXiv/OpenAlex；相关性解释由规则生成，不替代全文阅读。",
        "- 同题名、同 DOI 的预印本与期刊版本会合并；发布日期口径取数据源公开字段。",
        "- “机制桥接”不是直接研究 LLM，而是来自质量期刊、可迁移到 LLM 服务系统的模型论文。",
        "",
    ]
    return "\n".join(lines)


def stable_anchor(paper: Paper) -> str:
    return "paper-" + hashlib.sha1(normalized_title(paper.title).encode("utf-8")).hexdigest()[:10]


def _legacy_build_html(papers: list[Paper], config: dict[str, Any], report_date: dt.date, start_date: dt.date) -> str:
    grouped: dict[str, list[Paper]] = defaultdict(list)
    for paper in papers:
        grouped[paper.category_name].append(paper)
    direct = sum(p.track.startswith("直接") for p in papers)
    analog = len(papers) - direct
    source_counts = Counter(part for paper in papers for part in paper.source.split("+") if part)
    quick_cards: list[str] = []
    paper_articles: list[str] = []
    for paper in papers:
        authors = " / ".join(paper.authors[:8]) or "作者信息未提供"
        if len(paper.authors) > 8:
            authors += " et al."
        links = []
        if paper.url:
            links.append(f'<a href="{html.escape(paper.url, quote=True)}">论文页</a>')
        if paper.pdf_url:
            links.append(f'<a href="{html.escape(paper.pdf_url, quote=True)}">PDF</a>')
        if paper.doi:
            links.append(f'<a href="https://doi.org/{html.escape(paper.doi, quote=True)}">DOI</a>')
        abstract = paper.abstract or "来源未提供摘要；建议打开论文页人工核验。"
        abstract_preview = abstract if len(abstract) <= 430 else abstract[:427].rstrip() + "…"
        terms = "".join(f'<span class="tag">{html.escape(term)}</span>' for term in paper.matched_terms)
        quick_class = "quick-card top" if paper.track.startswith("直接") else "quick-card bridge-top"
        quick_cards.append(
            f'<div class="{quick_class}"><h3>{html.escape(paper.title)}</h3>'
            f'<p class="authors">{html.escape(authors)}</p><div class="quick-facts">'
            f'<span class="tag">{html.escape(paper.venue)}</span><span class="tag model">{html.escape(paper.category_name)}</span>'
            f'<span class="tag">相关性 {paper.relevance_score}</span></div>'
            f'<p class="one-line">{html.escape(category_reason(paper.category_id, config))}</p></div>'
        )
        paper_articles.append(
            f'<article class="paper" id="{stable_anchor(paper)}"><div class="paper-head">'
            f'<span class="tag model">{html.escape(paper.track)}</span><span class="tag">{html.escape(paper.source)}</span>'
            f'<span class="tag">相关性 {paper.relevance_score}</span></div>'
            f'<h2 class="paper-title">{html.escape(paper.title)}</h2>'
            f'<p class="paper-meta">{html.escape(authors)} · {html.escape(paper.venue)} · {html.escape(display_dates(paper))}</p>'
            f'<div class="guide"><div><b>背景问题</b>{html.escape(category_reason(paper.category_id, config))}</div>'
            f'<div><b>文章怎么做</b>{html.escape(abstract_preview)}</div>'
            f'<div><b>读前提示</b>该论文通过主题、服务运营机制和来源规则筛选；具体模型、识别策略与结论仍需阅读全文核验。</div></div>'
            f'<div class="matched"><b>命中主题</b><div class="quick-facts">{terms}</div></div>'
            f'<details open><summary>摘要、来源与核验边界</summary><div class="detail-body">'
            f'<p>{html.escape(abstract)}</p><div class="callout"><b>自动追踪边界：</b>本页保留数据源原始摘要，不自动补写摘要未支持的公式、结论或因果解释。</div>'
            f'<p>{" · ".join(links)}</p></div></details></article>'
        )
    if not quick_cards:
        quick_cards.append('<div class="quick-card"><h3>本窗口无新增</h3><p class="one-line">没有论文达到当前相关性和质量门槛。</p></div>')
    source_summary = "、".join(f"{name} {count} 篇" for name, count in sorted(source_counts.items())) or "无命中"
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="tracker" content="{html.escape(config['tracker_slug'])}"><title>{report_date.isoformat()} LLM 服务系统文献简报</title>
<style>
:root{{--ink:#172126;--muted:#5f6b72;--line:#d9e0e2;--paper:#fff;--wash:#f4f7f6;--green:#17685f;--green-soft:#e8f3f0;--coral:#a64b3b;--blue:#315c78;--gold:#8a681f;--gold-soft:#fff7df}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--wash);color:var(--ink);font:16px/1.72 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}}
a{{color:var(--blue);text-underline-offset:3px}}.page{{width:min(1180px,calc(100% - 32px));margin:30px auto 72px}}header,section,article{{background:var(--paper);border:1px solid var(--line);border-radius:8px}}
header{{padding:42px 48px 38px;border-top:5px solid var(--green)}}.eyebrow{{color:var(--green);font-weight:700;font-size:13px;text-transform:uppercase}}h1{{margin:8px 0 10px;font-size:clamp(30px,4vw,48px);line-height:1.16}}h2{{margin:0 0 16px;font-size:25px;line-height:1.3}}h3{{margin:0 0 8px;font-size:18px;line-height:1.36}}p{{margin:0 0 12px}}.scope{{max-width:920px;color:var(--muted);font-size:17px}}
.meta-row,.paper-head,.quick-facts{{display:flex;flex-wrap:wrap;gap:8px}}.meta-row{{margin-top:22px}}.tag{{display:inline-flex;align-items:center;min-height:28px;padding:4px 9px;border:1px solid var(--line);border-radius:6px;background:#fff;color:var(--muted);font-size:13px}}.tag.model{{background:var(--green-soft);color:var(--green);border-color:#c8e3dc}}
section{{margin-top:20px;padding:34px 38px}}.summary-list{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}}.summary-item{{padding:17px 18px;background:var(--wash);border-left:4px solid var(--green);border-radius:5px}}.summary-item strong{{display:block;margin-bottom:3px}}.summary-item span{{color:var(--muted);font-size:14px}}
.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:20px}}.metric{{min-height:94px;padding:15px;background:#fff;border:1px solid var(--line);border-radius:6px}}.metric b{{display:block;font-size:27px;line-height:1.1;color:var(--coral)}}.metric span{{display:block;margin-top:8px;color:var(--muted);font-size:13px}}
.quick-grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.quick-card{{padding:19px 20px;border:1px solid var(--line);border-radius:7px;background:#fff}}.quick-card.top{{border-top:4px solid var(--green)}}.quick-card.bridge-top{{border-top:4px solid var(--blue)}}.authors{{color:var(--muted);font-size:13px;line-height:1.55;margin:7px 0 10px}}.one-line{{margin-top:9px;font-size:14px}}
.paper{{margin-top:22px;padding:34px 38px;scroll-margin-top:24px}}.paper:target{{outline:3px solid #d79565;outline-offset:8px}}.paper-head{{margin-bottom:12px}}.paper-title{{max-width:900px}}.paper-meta{{color:var(--muted);font-size:14px}}.guide{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:22px 0 18px}}.guide>div{{min-height:150px;padding:17px 18px;border-radius:6px;background:var(--wash)}}.guide b{{display:block;margin-bottom:6px;color:var(--green)}}
.matched{{margin:0;padding:14px 18px;background:var(--green-soft);border-radius:6px}}details{{margin-top:18px;border-top:1px solid var(--line);padding-top:15px}}summary{{cursor:pointer;font-weight:700;color:var(--blue)}}.detail-body{{padding-top:15px}}.callout{{margin:18px 0;padding:17px 18px;border-left:4px solid var(--gold);background:var(--gold-soft);border-radius:5px}}.back{{display:inline-block;margin-bottom:12px}}
@media(max-width:780px){{header,section,.paper{{padding:26px 22px}}.summary-list,.quick-grid,.guide,.metrics{{grid-template-columns:1fr}}}}
</style></head><body><main class="page"><a class="back" href="index.html">← 返回研究归档首页</a><header>
<div class="eyebrow">LLM service operations · daily research brief</div><h1>{report_date.isoformat()} 每日学术文献简报</h1>
<p class="scope">检索窗口：{start_date.isoformat()} 至 {report_date.isoformat()}（{html.escape(config['timezone'])}）。本期确认 {len(papers)} 篇，优先展示 Token 定价、推理排队与调度、优先权/SLO、容量和平台机制。</p>
<div class="meta-row"><span class="tag model">服务运营机制优先</span><span class="tag">直接 LLM {direct} 篇</span><span class="tag">机制桥接 {analog} 篇</span><span class="tag">去重与质量门槛已执行</span></div></header>
<section><h2>Executive Summary</h2><div class="summary-list"><div class="summary-item"><strong>今日共确认 {len(papers)} 篇</strong><span>经过主题相关性、来源和重复版本筛选。</span></div><div class="summary-item"><strong>来源分布</strong><span>{html.escape(source_summary)}</span></div><div class="summary-item"><strong>阅读口径</strong><span>自动报告保留原始摘要，具体公式和结论以全文为准。</span></div></div>
<div class="metrics"><div class="metric"><b>{len(papers)}</b><span>确认新增 / 更新</span></div><div class="metric"><b>{direct}</b><span>直接 LLM 服务研究</span></div><div class="metric"><b>{analog}</b><span>高质量机制桥接</span></div><div class="metric"><b>{len(grouped)}</b><span>研究主题</span></div></div></section>
<section><h2>今日速览</h2><div class="quick-grid">{''.join(quick_cards)}</div></section>
{''.join(paper_articles)}
<section><h2>最终审核清单</h2><ul><li>同 DOI 或同题名版本已合并。</li><li>泛 benchmark、提示工程和非服务运营应用已降权或排除。</li><li>旧论文当天更新时，首次发布日期与最近更新日期分开显示。</li><li>未从摘要核验的公式和结论不自动补写。</li></ul></section>
</main></body></html>"""


def markdown_list(values: Iterable[str]) -> list[str]:
    return [f"- {value}" for value in values]


def html_list(values: Iterable[str], *, ordered: bool = False) -> str:
    tag = "ol" if ordered else "ul"
    items = "".join(f"<li>{html.escape(str(value))}</li>" for value in values)
    return f"<{tag}>{items}</{tag}>"


def bar_group_html(title: str, counts: Counter[str] | dict[str, int], color: str) -> str:
    entries = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    maximum = max((value for _, value in entries), default=1)
    rows = []
    for label, value in entries:
        width = max(4, round(value / maximum * 100))
        rows.append(
            f'<div class="bar-row"><span>{html.escape(label)}</span><div class="bar-track">'
            f'<i class="{color}" style="width:{width}%"></i></div><b>{value}</b></div>'
        )
    return f'<div class="bar-group"><h3>{html.escape(title)}</h3>{"".join(rows) or "<p>本期无数据</p>"}</div>'


def build_markdown(
    papers: list[Paper],
    config: dict[str, Any],
    report_date: dt.date,
    start_date: dt.date,
    analyses: dict[str, dict[str, Any]] | None = None,
) -> str:
    direct = sum(p.track.startswith("直接") for p in papers)
    analog = len(papers) - direct
    lines = [
        f"# {report_date.isoformat()} LLM 服务系统每日文献简报",
        "",
        f"> 检索窗口：{start_date.isoformat()} 至 {report_date.isoformat()}（北京时间 / {config['timezone']}）；"
        f"本期确认 {len(papers)} 篇，其中直接 LLM 服务研究 {direct} 篇、机制桥接 {analog} 篇。",
        "",
        "## Executive Summary",
        "",
        "本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。",
        "",
    ]
    if not papers:
        lines += ["本检索窗口没有达到门槛的新论文。", ""]
    for index, paper in enumerate(papers, 1):
        item = analysis_for(paper, config, analyses)
        authors = "、".join(paper.authors[:8]) or "作者信息未提供"
        if len(paper.authors) > 8:
            authors += " 等"
        lines += [
            f"## {index}. {item['title_zh']}",
            "",
            f"> 英文原标题：{paper.title}",
            "",
            f"- **研究问题：** {item['research_question']}",
            f"- **文章怎么做：** {item['method']}",
            f"- **研究启示：** {item['research_insight']}",
            f"- **作者：** {authors}",
            f"- **来源/日期：** {paper.venue}；{display_dates(paper)}；{paper.source}",
            f"- **研究类型：** {item['analysis_type']}；{paper.track}；相关性评分 {paper.relevance_score}",
            "",
            "### 中文内容总结",
            "",
            item["chinese_abstract"],
            "",
            "### 模型设定",
            "",
            f"**模型主线：** {item['model_summary']}",
            "",
            "**参与者 / 系统组件**",
            "",
            *markdown_list(item["participants"]),
            "",
            "**决策变量**",
            "",
            *markdown_list(item["decisions"]),
            "",
            "**关键参数与状态**",
            "",
            *markdown_list(item["primitives"]),
            "",
            "**研究时序**",
            "",
            *[f"{number}. {value}" for number, value in enumerate(item["sequence"], 1)],
            "",
            "### 公式与求解",
            "",
        ]
        if item["equations"]:
            for equation in item["equations"]:
                lines += [
                    f"- **{equation['label']}：** `{equation['latex']}`",
                    f"  - {equation['explanation']}",
                ]
        else:
            lines.append("- 现有证据不足以可靠复原公式。")
        lines += [
            "",
            f"**如何求解：** {item['solution']}",
            "",
            "### 主要结果",
            "",
            *markdown_list(item["findings"]),
            "",
            "### 局限与核验边界",
            "",
            *markdown_list(item["limitations"]),
            f"- **核验说明：** {item['verification']}",
            f"- **链接：** {paper_links_markdown(paper)}",
            "",
            "<details><summary>英文原摘要（补充）</summary>",
            "",
            paper.abstract or "数据源未提供摘要。",
            "",
            "</details>",
            "",
        ]
    lines += [
        "## 最终审核说明",
        "",
        "- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。",
        "- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。",
        "- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。",
        "",
    ]
    return "\n".join(lines)


def build_html(
    papers: list[Paper],
    config: dict[str, Any],
    report_date: dt.date,
    start_date: dt.date,
    analyses: dict[str, dict[str, Any]] | None = None,
) -> str:
    direct = sum(p.track.startswith("直接") for p in papers)
    analog = len(papers) - direct
    source_counts: Counter[str] = Counter(
        part for paper in papers for part in paper.source.split("+") if part
    )
    type_counts: Counter[str] = Counter(
        analysis_for(paper, config, analyses)["analysis_type"] for paper in papers
    )
    deep_count = sum(stable_anchor(paper) in (analyses or {}) for paper in papers)
    themes = []
    quick_cards = []
    paper_articles = []
    for paper in papers:
        item = analysis_for(paper, config, analyses)
        authors = " / ".join(paper.authors[:8]) or "作者信息未提供"
        if len(paper.authors) > 8:
            authors += " 等"
        title_zh = html.escape(item["title_zh"])
        title_en = html.escape(paper.title)
        themes.append(
            f'<div class="summary-item"><strong>{title_zh}</strong><span>{html.escape(item["one_line"])}</span></div>'
        )
        quick_class = "quick-card top" if paper.track.startswith("直接") else "quick-card bridge-top"
        quick_cards.append(
            f'<a class="{quick_class}" href="#{stable_anchor(paper)}"><h3>{title_zh}</h3>'
            f'<p class="english-title">{title_en}</p><p class="authors">{html.escape(authors)}</p>'
            f'<div class="quick-facts"><span class="tag model">{html.escape(item["analysis_type"])}</span>'
            f'<span class="tag">{html.escape(paper.venue)}</span><span class="tag">相关性 {paper.relevance_score}</span></div>'
            f'<p class="one-line">{html.escape(item["one_line"])}</p></a>'
        )
        links = []
        if paper.url:
            links.append(f'<a href="{html.escape(paper.url, quote=True)}">论文页面</a>')
        if paper.pdf_url:
            links.append(f'<a href="{html.escape(paper.pdf_url, quote=True)}">论文 PDF</a>')
        if paper.doi:
            links.append(f'<a href="https://doi.org/{html.escape(paper.doi, quote=True)}">DOI</a>')
        terms = "".join(f'<span class="tag">{html.escape(term)}</span>' for term in paper.matched_terms)
        equations = []
        for equation in item["equations"]:
            equations.append(
                f'<div class="formula"><b>{html.escape(equation["label"])}</b>'
                f'<div class="math">\\({html.escape(equation["latex"])}\\)</div>'
                f'<p>{html.escape(equation["explanation"])}</p></div>'
            )
        equation_block = "".join(equations) or '<p class="muted">现有证据不足以可靠复原公式。</p>'
        paper_articles.append(
            f'<article class="paper" id="{stable_anchor(paper)}">'
            f'<div class="paper-head"><span class="tag model">{html.escape(paper.track)}</span>'
            f'<span class="tag">{html.escape(paper.source)}</span><span class="tag">{html.escape(item["analysis_type"])}</span>'
            f'<span class="tag">相关性 {paper.relevance_score}</span></div>'
            f'<h2 class="paper-title">{title_zh}</h2><p class="original-title">英文原标题：{title_en}</p>'
            f'<p class="paper-meta">{html.escape(authors)} · {html.escape(paper.venue)} · {html.escape(display_dates(paper))}</p>'
            f'<div class="guide"><div><b>研究问题</b><p>{html.escape(item["research_question"])}</p></div>'
            f'<div><b>文章怎么做</b><p>{html.escape(item["method"])}</p></div>'
            f'<div><b>研究启示</b><p>{html.escape(item["research_insight"])}</p></div></div>'
            f'<div class="matched"><b>命中主题</b><div class="quick-facts">{terms}</div></div>'
            f'<details open><summary>中文内容总结与模型主线</summary><div class="detail-body">'
            f'<p>{html.escape(item["chinese_abstract"])}</p><div class="model-lead"><b>模型主线</b><p>{html.escape(item["model_summary"])}</p></div>'
            f'<div class="model-grid"><div><h3>参与者 / 系统组件</h3>{html_list(item["participants"])}</div>'
            f'<div><h3>决策变量</h3>{html_list(item["decisions"])}</div>'
            f'<div><h3>关键参数与状态</h3>{html_list(item["primitives"])}</div></div></div></details>'
            f'<details open><summary>研究时序、公式与求解</summary><div class="detail-body">'
            f'<h3>研究时序</h3>{html_list(item["sequence"], ordered=True)}<h3>核心公式</h3>'
            f'<div class="formula-grid">{equation_block}</div><div class="solution"><b>如何求解</b><p>{html.escape(item["solution"])}</p></div>'
            f'</div></details><details open><summary>主要结果、局限与核验边界</summary><div class="detail-body split">'
            f'<div><h3>主要结果</h3>{html_list(item["findings"])}</div><div><h3>局限与可扩展方向</h3>{html_list(item["limitations"])}</div>'
            f'</div><div class="callout"><b>核验说明：</b>{html.escape(item["verification"])}</div></details>'
            f'<details><summary>英文原摘要与来源链接（补充）</summary><div class="detail-body">'
            f'<p class="english-abstract">{html.escape(paper.abstract or "数据源未提供摘要。")}</p><p>{" · ".join(links)}</p></div></details>'
            f'</article>'
        )
    if not themes:
        themes.append('<div class="summary-item"><strong>本窗口无新增</strong><span>没有论文达到当前相关性和质量门槛。</span></div>')
        quick_cards.append('<div class="quick-card"><h3>本窗口无新增</h3><p>没有论文达到当前相关性和质量门槛。</p></div>')
    charts = bar_group_html("来源", source_counts, "green") + bar_group_html("研究类型", type_counts, "coral")
    template = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="tracker" content="__SLUG__"><title>__DATE__ LLM 服务系统每日文献简报</title>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
:root{--ink:#172126;--muted:#5f6b72;--line:#d9e0e2;--paper:#fff;--wash:#f4f7f6;--green:#17685f;--green-soft:#e8f3f0;--coral:#b24b38;--blue:#315c78;--gold:#8a681f;--gold-soft:#fff7df}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--wash);color:var(--ink);font:16px/1.72 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}a{color:var(--blue);text-underline-offset:3px}.page{width:min(1120px,calc(100% - 32px));margin:28px auto 72px}.back{display:inline-block;margin-bottom:11px}header,section,article{background:var(--paper);border:1px solid var(--line);border-radius:8px}header{padding:40px 46px 36px;border-top:5px solid var(--green)}.eyebrow{color:var(--green);font-weight:750;font-size:13px}h1{margin:7px 0 10px;font-size:clamp(31px,4.3vw,47px);line-height:1.15}h2{margin:0 0 15px;font-size:25px;line-height:1.32}h3{margin:0 0 8px;font-size:17px;line-height:1.4}p{margin:0 0 12px}.scope{max-width:920px;color:var(--muted);font-size:16px}.meta-row,.paper-head,.quick-facts{display:flex;flex-wrap:wrap;gap:8px}.meta-row{margin-top:21px}.tag{display:inline-flex;align-items:center;min-height:28px;padding:4px 9px;border:1px solid var(--line);border-radius:6px;background:#fff;color:var(--muted);font-size:13px}.tag.model{background:var(--green-soft);color:var(--green);border-color:#c8e3dc}section{margin-top:20px;padding:33px 36px}.summary-list{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}.summary-item{padding:17px 18px;background:var(--wash);border-left:4px solid var(--green);border-radius:5px}.summary-item strong{display:block;margin-bottom:5px}.summary-item span{color:var(--muted);font-size:14px}.metrics{display:grid;grid-template-columns:repeat(5,1fr);gap:9px;margin-top:18px}.metric{min-height:88px;padding:14px;border:1px solid var(--line);border-radius:6px}.metric b{display:block;color:var(--coral);font-size:25px;line-height:1.1}.metric span{display:block;margin-top:7px;color:var(--muted);font-size:12px}.charts{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:23px}.bar-group h3{font-size:18px}.bar-row{display:grid;grid-template-columns:88px 1fr 24px;gap:9px;align-items:center;margin:9px 0;font-size:13px}.bar-track{height:8px;background:#e2e7e8;border-radius:5px;overflow:hidden}.bar-track i{display:block;height:100%;border-radius:5px}.bar-track .green{background:var(--green)}.bar-track .coral{background:var(--coral)}.status-note{margin-top:24px;padding:16px 18px;border-left:4px solid var(--gold);background:var(--gold-soft);border-radius:5px}.quick-grid{display:grid;grid-template-columns:1fr 1fr;gap:13px}.quick-card{display:block;padding:18px 19px;border:1px solid var(--line);border-radius:7px;background:#fff;color:inherit;text-decoration:none}.quick-card.top{border-top:4px solid var(--green)}.quick-card.bridge-top{border-top:4px solid var(--blue)}.quick-card:hover h3{color:var(--coral)}.english-title,.original-title{color:var(--muted);font-size:13px}.authors,.paper-meta{color:var(--muted);font-size:13px}.one-line{margin-top:9px;font-size:14px}.paper{margin-top:22px;padding:33px 36px;scroll-margin-top:22px}.paper:target{outline:3px solid #d79565;outline-offset:7px}.paper-head{margin-bottom:12px}.paper-title{max-width:900px}.guide{display:grid;grid-template-columns:repeat(3,1fr);gap:11px;margin:22px 0 18px}.guide>div{min-height:190px;padding:17px 18px;border-radius:6px;background:var(--wash)}.guide b{display:block;margin-bottom:7px;color:var(--green)}.guide p{font-size:14px}.matched{padding:14px 18px;background:var(--green-soft);border-radius:6px}.matched>b{display:block;margin-bottom:7px}details{margin-top:18px;border-top:1px solid var(--line);padding-top:15px}summary{cursor:pointer;font-weight:750;color:var(--blue)}.detail-body{padding-top:15px}.model-lead,.solution{margin:17px 0;padding:16px 18px;border-left:4px solid var(--green);background:var(--green-soft);border-radius:5px}.model-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin-top:18px}.model-grid>div{padding:17px;background:var(--wash);border-radius:6px}.model-grid ul,.split ul{padding-left:20px;margin:8px 0}.model-grid li,.split li{margin:5px 0}.formula-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.formula{padding:16px 17px;border:1px solid var(--line);border-radius:6px}.formula b{color:var(--green)}.math{margin:9px 0;padding:10px 12px;background:#f1f4f4;border-radius:5px;font-family:Cambria Math,"Times New Roman",serif;font-size:16px;overflow:auto}.formula p{font-size:14px;color:var(--muted)}.split{display:grid;grid-template-columns:1fr 1fr;gap:24px}.callout{margin:16px 0;padding:16px 18px;border-left:4px solid var(--gold);background:var(--gold-soft);border-radius:5px}.english-abstract{color:#3e494f}.muted{color:var(--muted)}
@media(max-width:780px){header,section,.paper{padding:25px 21px}.summary-list,.metrics,.charts,.quick-grid,.guide,.model-grid,.formula-grid,.split{grid-template-columns:1fr}.guide>div{min-height:0}.bar-row{grid-template-columns:80px 1fr 24px}}
</style></head><body><main class="page"><a class="back" href="index.html">← 返回研究归档首页</a>
<header><div class="eyebrow">每日文献追踪 · 北京时间</div><h1>__DATE__ 每日学术文献简报</h1><p class="scope">检索窗口：__START__ 至 __DATE__（北京时间 / __TIMEZONE__）。本期确认 __TOTAL__ 篇，中文优先解读研究问题、模型设定、求解方法和研究启示。</p><div class="meta-row"><span class="tag model">模型与机制优先</span><span class="tag">直接 LLM __DIRECT__ 篇</span><span class="tag">机制桥接 __ANALOG__ 篇</span><span class="tag">全文核验与版本边界</span></div></header>
<section><h2>Executive Summary</h2><div class="summary-list">__THEMES__</div><div class="metrics"><div class="metric"><b>__TOTAL__</b><span>确认新增 / 更新</span></div><div class="metric"><b>__DIRECT__</b><span>直接 LLM 服务研究</span></div><div class="metric"><b>__ANALOG__</b><span>高质量机制桥接</span></div><div class="metric"><b>__MODEL_COUNT__</b><span>模型 / 机制条目</span></div><div class="metric"><b>__DEEP__</b><span>中文深度分析</span></div></div><div class="charts">__CHARTS__</div><div class="status-note"><b>检索状态：</b>题录经主题、来源、日期与重复版本筛选；正文以中文分析为主，英文原标题和原摘要仅作为补充。公式只在全文或可靠原文证据支持时写入。</div></section>
<section><h2>今日速览</h2><div class="quick-grid">__QUICK__</div></section>
__ARTICLES__
<section><h2>最终审核清单</h2><ul><li>同 DOI 或同题名版本已合并。</li><li>泛 benchmark、提示工程和非服务运营应用已降权或排除。</li><li>首次发布日期与最近更新日期分开显示。</li><li>每篇论文均按“研究问题—文章怎么做—研究启示”呈现，模型条目另列参与者、决策、参数、公式、求解、结果和边界。</li><li>无法从全文核验的内容会明确标为待核验，不自动补写。</li></ul></section>
</main></body></html>"""
    replacements = {
        "__SLUG__": html.escape(config["tracker_slug"]),
        "__DATE__": report_date.isoformat(),
        "__START__": start_date.isoformat(),
        "__TIMEZONE__": html.escape(config["timezone"]),
        "__TOTAL__": str(len(papers)),
        "__DIRECT__": str(direct),
        "__ANALOG__": str(analog),
        "__MODEL_COUNT__": str(sum(value for value in type_counts.values() if value)),
        "__DEEP__": str(deep_count),
        "__THEMES__": "".join(themes[:3]),
        "__CHARTS__": charts,
        "__QUICK__": "".join(quick_cards),
        "__ARTICLES__": "".join(paper_articles),
    }
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    return template


def report_archive_record(
    papers: list[Paper],
    config: dict[str, Any],
    report_date: dt.date,
    start_date: dt.date,
    analyses: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    sources: Counter[str] = Counter()
    for paper in papers:
        sources.update(part for part in paper.source.split("+") if part)
    paper_records = []
    for paper in papers:
        analysis = analysis_for(paper, config, analyses)
        paper_records.append(
            {
                "date": report_date.isoformat(),
                "file": f"literature_tracking_{report_date.isoformat()}.html",
                "id": stable_anchor(paper),
                "title": analysis["title_zh"],
                "original_title": paper.title,
                "authors": " / ".join(paper.authors) or "作者信息未提供",
            }
        )
    return {
        "date": report_date.isoformat(),
        "window": f"{start_date.isoformat()} 至 {report_date.isoformat()}（{config['timezone']}）",
        "file": f"literature_tracking_{report_date.isoformat()}.html",
        "total": len(papers),
        "sources": dict(sorted(sources.items())),
        "types": dict(Counter(paper.category_name for paper in papers)),
        "statuses": dict(Counter(paper.track for paper in papers)),
        "papers": paper_records,
    }


def update_archive(
    archive_path: Path,
    record: dict[str, Any],
) -> dict[str, Any]:
    archive: dict[str, Any] = {"reports": []}
    if archive_path.exists():
        try:
            loaded = json.loads(archive_path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict) and isinstance(loaded.get("reports"), list):
                archive = loaded
        except (json.JSONDecodeError, OSError):
            pass
    reports = [item for item in archive["reports"] if item.get("date") != record["date"]]
    reports.append(record)
    archive["reports"] = sorted(reports, key=lambda item: item["date"], reverse=True)
    return archive


def safe_json_for_script(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def build_index(config: dict[str, Any], archive: dict[str, Any]) -> str:
    reports = archive.get("reports", [])
    public_reports = [
        {key: report[key] for key in ("date", "window", "file", "total", "sources", "types", "statuses")}
        for report in reports
    ]
    paper_index = [paper for report in reports for paper in report.get("papers", [])]
    dates = [report["date"] for report in reports]
    latest_date = max(dates) if dates else "—"
    archive_start = min(dates) if dates else "—"
    template = INDEX_TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "__REPORT_COUNT__": str(len(reports)),
        "__PAPER_COUNT__": str(sum(int(report.get("total", 0)) for report in reports)),
        "__LATEST_DATE__": latest_date,
        "__ARCHIVE_START_DATE__": archive_start,
        "__REPORTS_JSON__": safe_json_for_script(public_reports),
        "__PAPER_INDEX_JSON__": safe_json_for_script(paper_index),
    }
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    return template


def collect(
    config: dict[str, Any],
    start_date: dt.date,
    end_date: dt.date,
    source: str,
    max_results: int,
) -> list[Paper]:
    candidates: list[Paper] = []
    errors: list[str] = []
    query_count = 0
    if source in {"all", "arxiv"}:
        arxiv_queries = config["source_queries"]["arxiv"]
        query_count += len(arxiv_queries)
        for index, query in enumerate(arxiv_queries):
            try:
                for paper in fetch_arxiv(query, start_date, end_date, max_results):
                    scored = score_paper(paper, config)
                    if scored is not None:
                        candidates.append(scored)
            except Exception as exc:  # keep the other source usable during an outage
                errors.append(f"arXiv query {index + 1}: {exc}")
            if index + 1 < len(arxiv_queries):
                time.sleep(3)
    if source in {"all", "openalex"}:
        direct_queries = config["source_queries"]["openalex"]
        query_count += len(direct_queries)
        for query in direct_queries:
            try:
                for paper in fetch_openalex(query, start_date, end_date, max_results):
                    scored = score_paper(paper, config)
                    if scored is not None:
                        candidates.append(scored)
            except Exception as exc:
                errors.append(f"OpenAlex direct query '{query}': {exc}")
        if config.get("include_service_analogs"):
            analog_queries = config["source_queries"].get("service_analog_openalex", [])
            query_count += len(analog_queries)
            for query in analog_queries:
                try:
                    for paper in fetch_openalex(query, start_date, end_date, max_results):
                        scored = score_paper(paper, config, analog_query=True)
                        if scored is not None:
                            candidates.append(scored)
                except Exception as exc:
                    errors.append(f"OpenAlex analog query '{query}': {exc}")
    if errors:
        print("\n".join(f"WARNING: {error}" for error in errors), file=sys.stderr)
    if not candidates and query_count and len(errors) >= query_count:
        raise RuntimeError("All configured source queries failed; no report was written.")
    return merge_papers(candidates)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--date", help="Report date in YYYY-MM-DD; defaults to today in the configured timezone")
    parser.add_argument("--lookback-days", type=int, help="Override the configured lookback window")
    parser.add_argument("--source", choices=("all", "arxiv", "openalex"), default="all")
    parser.add_argument("--max-per-query", type=int, help="Override max results fetched per source query")
    parser.add_argument("--reports-dir", type=Path, default=ROOT / "reports")
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    timezone = ZoneInfo(config["timezone"])
    report_date = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(timezone).date()
    lookback_days = args.lookback_days or int(config["default_lookback_days"])
    if lookback_days < 1:
        raise ValueError("--lookback-days must be at least 1")
    start_date = report_date - dt.timedelta(days=lookback_days - 1)
    max_results = args.max_per_query or int(config["max_results_per_query"])
    papers = collect(config, start_date, report_date, args.source, max_results)
    papers = merge_papers([*papers, *load_confirmed_papers(report_date)])
    analyses = ensure_chinese_analyses(papers, config)

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    args.site_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = args.reports_dir / f"literature_tracking_{report_date.isoformat()}.md"
    html_path = args.site_dir / f"literature_tracking_{report_date.isoformat()}.html"
    archive_path = args.site_dir / "archive.json"
    markdown_path.write_text(build_markdown(papers, config, report_date, start_date, analyses), encoding="utf-8")
    html_path.write_text(build_html(papers, config, report_date, start_date, analyses), encoding="utf-8")
    archive = update_archive(
        archive_path,
        report_archive_record(papers, config, report_date, start_date, analyses),
    )
    archive_path.write_text(json.dumps(archive, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.site_dir / "index.html").write_text(build_index(config, archive), encoding="utf-8")
    print(f"Wrote {markdown_path}")
    print(f"Wrote {html_path}")
    print(f"Kept {len(papers)} papers after relevance filtering and deduplication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
