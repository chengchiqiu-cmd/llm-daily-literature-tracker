#!/usr/bin/env python3
"""Rebuild legacy pending-verification reports as abstract-first briefs."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("track_literature", ROOT / "scripts" / "track_literature.py")
tracker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = tracker
SPEC.loader.exec_module(tracker)


def field(section: str, label: str) -> str:
    match = re.search(rf"^- \*\*{re.escape(label)}：\*\* (.+)$", section, re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_dates(value: str) -> tuple[str, str]:
    first = re.search(r"首次发布 ([0-9-]+)", value)
    latest = re.search(r"最近更新 ([0-9-]+)", value)
    if first or latest:
        published = first.group(1) if first else ""
        updated = latest.group(1) if latest else published
        return published, updated
    date = re.search(r"\d{4}(?:-\d{2})?(?:-\d{2})?", value)
    return (date.group(0), date.group(0)) if date else ("", "")


def link(section: str, label: str) -> str:
    match = re.search(rf"\[{re.escape(label)}\]\(([^)]+)\)", section)
    return match.group(1).strip() if match else ""


def parse_legacy_report(path: Path, config: dict) -> tuple[object, object, list]:
    text = path.read_text(encoding="utf-8")
    report_match = re.search(r"^# (\d{4}-\d{2}-\d{2}) ", text, re.MULTILINE)
    window_match = re.search(r"^> 检索窗口：(\d{4}-\d{2}-\d{2}) 至 (\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    if not report_match or not window_match:
        raise ValueError(f"Cannot parse report dates from {path}")
    report_date = tracker.dt.date.fromisoformat(report_match.group(1))
    start_date = tracker.dt.date.fromisoformat(window_match.group(1))
    sections = re.split(r"(?=^## \d+\. )", text, flags=re.MULTILINE)[1:]
    papers = []
    for section in sections:
        title_match = re.search(r"^## \d+\. (.+)$", section, re.MULTILINE)
        original_match = re.search(r"^> 英文原标题：(.+)$", section, re.MULTILINE)
        abstract_match = re.search(
            r"<details><summary>英文原摘要（补充）</summary>\s*(.*?)\s*</details>",
            section,
            re.DOTALL,
        )
        if not title_match:
            continue
        title = (original_match or title_match).group(1).strip()
        source_value = field(section, "来源/日期")
        source_parts = [part.strip() for part in source_value.split("；")]
        venue = source_parts[0] if source_parts else ""
        source = source_parts[-1] if len(source_parts) > 1 else venue
        published, updated = parse_dates(source_value)
        type_value = field(section, "研究类型")
        track_match = re.search(r"(直接 LLM 服务研究|高质量服务运营机制桥接)", type_value)
        score_match = re.search(r"相关性评分 (\d+)", type_value)
        category_match = re.search(r"与“([^”]+)”相关", section)
        category_name = category_match.group(1) if category_match else "未分类"
        category = next((item for item in config["categories"] if item["name"] == category_name), None)
        authors_value = field(section, "作者")
        authors = [part.strip() for part in authors_value.removesuffix(" 等").split("、") if part.strip()]
        doi_url = link(section, "DOI")
        doi = doi_url.removeprefix("https://doi.org/") if doi_url else ""
        paper = tracker.Paper(
            title=tracker.clean_abstract(title),
            authors=authors,
            abstract=tracker.clean_abstract(abstract_match.group(1) if abstract_match else ""),
            published=published,
            updated=updated,
            venue=venue,
            url=link(section, "论文页") or doi_url,
            pdf_url=link(section, "PDF"),
            doi=doi,
            source=source,
            category_id=category["id"] if category else "",
            category_name=category_name,
            track=track_match.group(1) if track_match else "直接 LLM 服务研究",
            relevance_score=int(score_match.group(1)) if score_match else 0,
        )
        scored = tracker.score_paper(paper, config, analog_query=paper.track.startswith("高质量"))
        if scored is None:
            paper.matched_terms = tracker.matched_phrases(
                f"{paper.title} {paper.abstract}",
                config["direct_llm_terms"] + (category or {}).get("terms", []),
            )[:10]
        papers.append(paper)
    return report_date, start_date, tracker.merge_papers(papers)


def main() -> int:
    config = json.loads((ROOT / "config" / "llm_service_ops.json").read_text(encoding="utf-8"))
    analyses = tracker.load_analysis_cache()
    archive_path = ROOT / "site" / "archive.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8")) if archive_path.exists() else {"reports": []}
    changed = 0
    for markdown_path in sorted((ROOT / "reports").glob("literature_tracking_*.md")):
        text = markdown_path.read_text(encoding="utf-8")
        if "待全文核验" not in text:
            continue
        report_date, start_date, papers = parse_legacy_report(markdown_path, config)
        markdown_path.write_text(
            tracker.build_markdown(papers, config, report_date, start_date, analyses),
            encoding="utf-8",
        )
        (ROOT / "site" / f"literature_tracking_{report_date.isoformat()}.html").write_text(
            tracker.build_html(papers, config, report_date, start_date, analyses),
            encoding="utf-8",
        )
        archive = tracker.update_archive(
            archive_path,
            tracker.report_archive_record(papers, config, report_date, start_date, analyses),
        )
        archive_path.write_text(json.dumps(archive, ensure_ascii=False, indent=2), encoding="utf-8")
        changed += 1
    (ROOT / "site" / "index.html").write_text(tracker.build_index(config, archive), encoding="utf-8")
    print(f"Rebuilt {changed} legacy reports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
