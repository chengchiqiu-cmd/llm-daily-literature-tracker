# 日期选择与全站论文搜索 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将首页日期控件拆成年、月、日三级联动，并提供覆盖全部已生效报告的标题/作者搜索和文章锚点定位。

**Architecture:** Python 静态生成器继续作为唯一数据入口，从每份日报的 `article.paper` 提取精简搜索索引，并将报告元数据与索引嵌入首页。浏览器端只负责三级日期联动、分布弹窗和本地索引匹配；GitHub Pages 发布阶段向报告页注入 `:target` 高亮样式。

**Tech Stack:** Python 3 标准库 `html.parser`、原生 HTML/CSS/JavaScript、`unittest`、Playwright、GitHub Pages Actions。

## Global Constraints

- 网站保持纯静态，无后端、数据库或外部前端依赖。
- 搜索覆盖全部 `2026-07-14` 起的已生效报告，不受当前日期选择影响。
- 日期控件默认最新可用报告日期，仅提供实际存在的年月日组合。
- 不改变报告正文、文章排序、Fasheng Xu 聊天通知、期刊白名单与隐藏标签规则。
- 搜索结果点击后必须以 `报告文件#文章ID` 定位，并提供克制的 `:target` 高亮。

---

### Task 1: 提取稳定的论文搜索索引

**Files:**
- Modify: `scripts/build_literature_portal.py`
- Test: `tests/test_build_literature_portal.py`

**Interfaces:**
- Consumes: 报告 HTML 中的 `article.paper[id]`、`h2.paper-title`、`p.paper-meta` 与报告元数据。
- Produces: `extract_papers(document: str, report: Dict) -> List[Dict]` 和 `load_search_index(outputs_dir: Path, reports: List[Dict]) -> List[Dict]`。

- [x] **Step 1: 写索引提取失败测试**

```python
def test_extract_papers_builds_title_author_and_anchor_index(self):
    report = metadata_for("2026-07-14")
    document = report_html(report, papers=[
        ("paper-one", "Platform Pricing", "Alice Chen / Bob Xu"),
    ])

    self.assertEqual(extract_papers(document, report), [{
        "date": "2026-07-14",
        "file": "literature_tracking_2026-07-14.html",
        "id": "paper-one",
        "title": "Platform Pricing",
        "authors": "Alice Chen / Bob Xu",
    }])
```

- [x] **Step 2: 运行测试并确认因缺少接口失败**

Run: `python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests.test_extract_papers_builds_title_author_and_anchor_index -v`

Expected: `ImportError` 或 `AttributeError` 指向 `extract_papers` 尚不存在。

- [x] **Step 3: 实现最小 HTMLParser**

```python
class PaperIndexParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.current = None
        self.capture = None
        self.parts = []
        self.papers = []

    def handle_starttag(self, tag, attrs) -> None:
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())
        if tag == "article" and "paper" in classes:
            self.current = {"id": attributes.get("id", ""), "title": "", "authors": ""}
        elif self.current is not None and tag == "h2" and "paper-title" in classes:
            self.capture, self.parts = "title", []
        elif self.current is not None and tag == "p" and "paper-meta" in classes:
            self.capture, self.parts = "authors", []

    def handle_data(self, data) -> None:
        if self.capture:
            self.parts.append(data)

    def handle_endtag(self, tag) -> None:
        if self.current is not None and self.capture and tag in {"h2", "p"}:
            self.current[self.capture] = " ".join("".join(self.parts).split())
            self.capture, self.parts = None, []
        if tag == "article" and self.current is not None:
            if self.current["id"] and self.current["title"]:
                self.papers.append(self.current)
            self.current = None

def extract_papers(document: str, report: Dict) -> List[Dict]:
    parser = PaperIndexParser()
    parser.feed(document)
    return [
        {"date": report["date"], "file": report["file"], **paper}
        for paper in parser.papers
    ]
```

- [x] **Step 4: 增加缺失 ID/标题时跳过并告警的测试与实现**

```python
document_without_article_id = report_html(
    report,
    papers=[("", "Platform Pricing", "Alice Chen")],
)
with self.assertLogs("literature_portal", level="WARNING"):
    papers = extract_papers(document_without_article_id, report)
self.assertEqual(papers, [])
```

- [x] **Step 5: 运行生成器单元测试**

Run: `python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests -v`

Expected: 所有 `PortalGeneratorTests` 通过。

### Task 2: 生成三级日期控件与全站搜索界面

**Files:**
- Modify: `scripts/build_literature_portal.py`
- Test: `tests/test_build_literature_portal.py`

**Interfaces:**
- Consumes: `reports: List[Dict]` 和 Task 1 的 `search_index: List[Dict]`。
- Produces: `render_portal(reports: List[Dict], search_index: Optional[List[Dict]] = None) -> str`。

- [x] **Step 1: 写首页结构失败测试**

```python
def test_render_portal_has_split_date_controls_and_search_index(self):
    search_index = [{
        "date": "2026-07-14", "file": "literature_tracking_2026-07-14.html",
        "id": "paper-one", "title": "Platform Pricing", "authors": "Alice Chen",
    }]
    document = render_portal([metadata_for("2026-07-14")], search_index)
    for control in ('id="report-year"', 'id="report-month"', 'id="report-day"'):
        self.assertIn(control, document)
    self.assertIn('id="paper-search"', document)
    self.assertIn('id="search-results"', document)
    self.assertIn('"id":"paper-one"', document)
    self.assertNotIn('id="report-date"', document)
```

- [x] **Step 2: 运行测试并确认旧单日期控件导致失败**

Run: `python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests.test_render_portal_has_split_date_controls_and_search_index -v`

Expected: FAIL，缺少 `report-year`、`report-month`、`report-day` 或 `paper-search`。

- [x] **Step 3: 实现日期控件与默认最新日期**

```javascript
const latestDate = reports.length ? reports[0].date : '';
const reportDates = new Set(reports.map(item => item.date));

function replaceOptions(select, values) {
  select.replaceChildren(...values.map(value => {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = value;
    return option;
  }));
}

function setSelectedDate(value) {
  const [year, month, day] = value.split('-');
  replaceOptions(reportYear, [...new Set(reports.map(item => item.date.slice(0, 4)))]);
  reportYear.value = year;
  replaceOptions(reportMonth, [...new Set(reports
    .filter(item => item.date.startsWith(`${year}-`))
    .map(item => item.date.slice(5, 7)))]);
  reportMonth.value = month;
  replaceOptions(reportDay, reports
    .filter(item => item.date.startsWith(`${year}-${month}-`))
    .map(item => item.date.slice(8, 10)));
  reportDay.value = day;
}

function selectedDate() {
  const value = `${reportYear.value}-${reportMonth.value}-${reportDay.value}`;
  return reportDates.has(value) ? value : '';
}
setSelectedDate(latestDate);
```

- [x] **Step 4: 实现全站标题/作者搜索**

```javascript
function normalize(value) { return value.trim().toLocaleLowerCase(); }
function searchPapers(query) {
  const needle = normalize(query);
  return needle
    ? paperIndex.filter(item => normalize(`${item.title} ${item.authors}`).includes(needle))
    : [];
}
```

结果链接必须使用：

```javascript
link.href = `${item.file}#${encodeURIComponent(item.id)}`;
```

- [x] **Step 5: 让 build_portal 自动加载索引并运行测试**

```python
reports = load_reports(outputs_dir, minimum_date)
search_index = load_search_index(outputs_dir, reports)
output_path.write_text(render_portal(reports, search_index), encoding="utf-8")
```

Run: `python3 -m unittest discover -s tests -v`

Expected: 全部 Python 测试通过。

### Task 3: 注入目标文章高亮并验证发布同步

**Files:**
- Modify: `scripts/build_literature_portal.py`
- Test: `tests/test_build_literature_portal.py`

**Interfaces:**
- Consumes: `sync_github_pages` 发布的合格报告 HTML。
- Produces: `_inject_report_target_style(document: str) -> str`，且不重复注入。

- [x] **Step 1: 写发布报告高亮失败测试**

```python
published = (public_dir / current_report.name).read_text(encoding="utf-8")
self.assertIn("article.paper:target", published)
self.assertEqual(published.count("portal-target-style"), 1)
```

- [x] **Step 2: 运行测试并确认缺少样式失败**

Run: `python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests.test_sync_github_pages_publishes_only_index_and_eligible_reports -v`

Expected: FAIL，找不到 `article.paper:target`。

- [x] **Step 3: 实现幂等样式注入**

```python
TARGET_STYLE = (
    '<style id="portal-target-style">'
    'article.paper{scroll-margin-top:24px}'
    'article.paper:target{outline:3px solid #d79565;outline-offset:8px;'
    'animation:portal-target-fade 2.8s ease-out}'
    '@keyframes portal-target-fade{0%,45%{background:#fff3cf}100%{background:transparent}}'
    '</style>'
)

def _inject_report_target_style(document: str) -> str:
    if 'id="portal-target-style"' in document:
        return document
    head_match = re.search(r"<head\b[^>]*>", document, re.IGNORECASE)
    if head_match:
        return document[:head_match.end()] + TARGET_STYLE + document[head_match.end():]
    return f"<head>{TARGET_STYLE}</head>{document}"
```

- [x] **Step 4: 运行全部 Python 测试**

Run: `python3 -m unittest discover -s tests -v`

Expected: 全部测试通过且无异常输出。

### Task 4: 浏览器验证与 GitHub Pages 发布

**Files:**
- Modify: `tests/browser_qa.cjs`
- Generate: `outputs/index.html`
- Generate: `literature-portal-pages/site/index.html`
- Generate: `literature-portal-pages/site/literature_tracking_2026-07-14.html`

**Interfaces:**
- Consumes: 生成后的本地静态站点与公开 GitHub Pages URL。
- Produces: 桌面/移动自动化验收证据与公开部署。

- [x] **Step 1: 更新浏览器测试并先观察旧页面失败**

断言包括：

```javascript
assert.equal(await page.inputValue("#report-year"), "2026");
assert.equal(await page.inputValue("#report-month"), "07");
assert.equal(await page.inputValue("#report-day"), "14");
await page.fill("#paper-search", "Dominik Gutt");
assert.equal(await page.locator(".search-result").count(), 1);
assert.match(await page.locator(".search-result").getAttribute("href"), /#hit-gas$/);
```

Run: `node tests/browser_qa.cjs`

Expected: FAIL，旧页面找不到三级日期控件或搜索框。

- [x] **Step 2: 重新生成 Pages 目录**

Run:

```bash
python3 scripts/build_literature_portal.py \
  --outputs outputs \
  --output outputs/index.html \
  --minimum-date 2026-07-14 \
  --github-pages-dir literature-portal-pages
```

Expected: `Built outputs/index.html with 1 report(s).`

- [x] **Step 3: 执行完整本地验收**

Run:

```bash
python3 -m unittest discover -s tests -v
node tests/browser_qa.cjs
```

Expected: Python 测试全部通过；Playwright 桌面与移动断言通过，无页面或控制台错误。

- [x] **Step 4: 检查发布差异并提交**

Run:

```bash
git -C literature-portal-pages status -sb
git -C literature-portal-pages diff --check
git -C literature-portal-pages diff -- site/index.html site/literature_tracking_2026-07-14.html tests 2>/dev/null || true
```

仅提交本功能相关的规格、计划与 `site/` 文件。

- [x] **Step 5: 推送并等待 Pages 部署**

Run:

```bash
git -C literature-portal-pages push origin main
tools/gh_2.94.0_macOS_arm64/bin/gh run watch --repo RuiyangRyanxu/analytical-models-ai-research-tracker --exit-status
```

Expected: 最新 `pages build and deployment` 工作流结论为 `success`。

- [x] **Step 6: 对公开 URL 复跑浏览器测试**

Run:

```bash
PORTAL_URL=https://ruiyangryanxu.github.io/analytical-models-ai-research-tracker/ node tests/browser_qa.cjs
```

Expected: 公开页面日期默认值、作者搜索、标题搜索、锚点 URL、弹窗与移动布局全部通过。
