# Compact Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the visible daily-report archive rows from the public homepage while preserving date-based distribution access and title/author search across all eligible reports.

**Architecture:** Keep the existing report metadata and paper index embedded in the static homepage. Remove only the archive-row rendering path, dedicated styles, and row click handlers; the split date controls continue to resolve report metadata and open the existing distribution dialog.

**Tech Stack:** Python 3 static HTML generator, inline CSS and JavaScript, `unittest`, Playwright browser QA, GitHub Pages.

## Global Constraints

- Keep separate year, month, and day selectors, defaulted to the newest eligible report.
- Keep the distribution dialog, complete-report link, and title/author search.
- Do not delete report metadata or archived report HTML files.
- Do not change report content, inclusion rules, sorting, or daily publishing behavior.
- The homepage must not render an archive list, archive rows, or `data-report-date` elements.
- Desktop and mobile layouts must have no horizontal overflow.

---

### Task 1: Lock The Compact Homepage Contract

**Files:**
- Modify: `tests/test_build_literature_portal.py`
- Modify: `tests/browser_qa.cjs`

**Interfaces:**
- Consumes: `render_portal(reports, search_index)` and the generated static homepage.
- Produces: regression assertions for absent archive-row markup and retained date/search behavior.

- [ ] **Step 1: Write the failing unit assertion**

Add the following assertions to `test_render_portal_has_split_date_controls_and_search_index`:

```python
self.assertNotIn('class="archive-list"', document)
self.assertNotIn('class="archive-row"', document)
self.assertNotIn('data-report-date', document)
```

- [ ] **Step 2: Run the focused unit test and verify RED**

Run:

```bash
python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests.test_render_portal_has_split_date_controls_and_search_index -v
```

Expected: FAIL because the current generated homepage contains `class="archive-list"`.

- [ ] **Step 3: Update browser expectations**

Change the browser assertion from two report rows to zero while retaining all checks for the default date, modal totals/link, search results, report target highlighting, and desktop/mobile overflow:

```javascript
assert.equal(desktop.reportRows, 0);
```

### Task 2: Remove Archive-Row Rendering

**Files:**
- Modify: `scripts/build_literature_portal.py`

**Interfaces:**
- Consumes: the existing `reports` and `search_index` payloads.
- Produces: `render_portal()` output without visible report rows, with unchanged date selector and search APIs.

- [ ] **Step 1: Remove the row-rendering helper**

Delete `_archive_rows(reports)` because no visible archive list remains.

- [ ] **Step 2: Remove dedicated markup and styling**

Delete the following generated homepage elements:

```html
<div class="archive-list" id="archive-list">...</div>
```

Delete `.archive-list`, `.archive-row`, `.archive-date`, `.archive-summary`, `.archive-action`, and now-unused `.empty-state` CSS, including mobile overrides. Keep `.search-area` as the visual divider directly following the date controls.

- [ ] **Step 3: Remove obsolete row click handlers**

Delete the `document.querySelectorAll('[data-report-date]')` listener block. Keep date selector and `#open-distribution` handlers unchanged.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run:

```bash
python3 -m unittest tests.test_build_literature_portal.PortalGeneratorTests.test_render_portal_has_split_date_controls_and_search_index -v
```

Expected: PASS.

### Task 3: Rebuild And Validate The Public Artifact

**Files:**
- Regenerate: `outputs/index.html`
- Regenerate: `literature-portal-pages/site/index.html`

**Interfaces:**
- Consumes: eligible report metadata and HTML files dated 2026-07-14 or later.
- Produces: the compact local and GitHub Pages homepages.

- [ ] **Step 1: Rebuild the portal**

Run:

```bash
python3 scripts/build_literature_portal.py --outputs outputs --output outputs/index.html --minimum-date 2026-07-14 --github-pages-dir literature-portal-pages
```

Expected: homepage and Pages site are regenerated with the current eligible reports.

- [ ] **Step 2: Run the full unit suite**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 3: Run browser QA**

Run:

```bash
/Users/ryan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node tests/browser_qa.cjs
```

Expected: zero report rows; latest date `2026-07-15`; working distribution dialog and title/author search; no desktop or mobile overflow; no internal labels.

- [ ] **Step 4: Inspect the desktop and mobile screenshots**

Verify that the search section follows the date controls without report rows and that spacing remains restrained on both viewports.

### Task 4: Publish GitHub Pages

**Files:**
- Commit: `literature-portal-pages/site/index.html`
- Preserve: all archived report HTML files.

**Interfaces:**
- Consumes: verified generated homepage.
- Produces: the public GitHub Pages homepage.

- [ ] **Step 1: Review repository status and diff**

Confirm that only the implementation plan and generated homepage are newly changed, in addition to the already committed design specification.

- [ ] **Step 2: Commit the homepage change**

```bash
git add docs/superpowers/plans/2026-07-15-compact-homepage.md site/index.html
git commit -m "Simplify homepage report navigation"
```

- [ ] **Step 3: Push `main` and watch deployment**

Push to `origin/main`, then watch the latest `Deploy GitHub Pages` workflow until it reports `success`.

- [ ] **Step 4: Verify the deployed page**

Confirm the public HTML has no archive-list, archive-row, or `data-report-date` markup, while the date controls and paper search remain present.
