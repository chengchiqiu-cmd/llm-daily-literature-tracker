import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("track_literature", ROOT / "scripts" / "track_literature.py")
tracker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = tracker
SPEC.loader.exec_module(tracker)
CONFIG = json.loads((ROOT / "config" / "llm_service_ops.json").read_text(encoding="utf-8"))


def paper(title, abstract, venue="arXiv", doi="", source="arXiv"):
    return tracker.Paper(
        title=title,
        authors=["Test Author"],
        abstract=abstract,
        published="2026-07-15",
        updated="2026-07-15",
        venue=venue,
        url="https://example.org/paper",
        doi=doi,
        source=source,
    )


class ScoringTests(unittest.TestCase):
    def test_direct_llm_queueing_paper_is_kept(self):
        candidate = paper(
            "Queueing-Aware Scheduling for Large Language Model Inference",
            "We optimize request scheduling, admission control and the latency throughput tradeoff in LLM serving.",
        )
        scored = tracker.score_paper(candidate, CONFIG)
        self.assertIsNotNone(scored)
        self.assertEqual(scored.category_id, "queue_scheduling")
        self.assertEqual(scored.track, "直接 LLM 服务研究")

    def test_generic_llm_benchmark_is_rejected(self):
        candidate = paper(
            "A Vision-Language Benchmark for Large Language Models",
            "We introduce a question answering benchmark and report accuracy.",
        )
        self.assertIsNone(tracker.score_paper(candidate, CONFIG))

    def test_generic_latency_mention_is_not_a_service_operations_paper(self):
        candidate = paper(
            "Materials Discovery with Large Language Models",
            "The method improves accuracy and reports lower latency on a chemistry benchmark.",
        )
        self.assertIsNone(tracker.score_paper(candidate, CONFIG))

    def test_quality_journal_service_analog_is_kept_only_in_analog_lane(self):
        candidate = paper(
            "Priority Pricing in Queueing Systems with Strategic Customers",
            "An analytical model studies a priority queue, service differentiation, and equilibrium admission control.",
            venue="Management Science",
            source="OpenAlex",
        )
        self.assertIsNone(tracker.score_paper(candidate, CONFIG, analog_query=False))
        self.assertIsNotNone(tracker.score_paper(candidate, CONFIG, analog_query=True))

    def test_preprint_service_analog_without_llm_context_is_rejected(self):
        candidate = paper(
            "Priority Pricing in Queueing Systems",
            "A queueing model studies service differentiation and admission control.",
        )
        self.assertIsNone(tracker.score_paper(candidate, CONFIG, analog_query=True))

    def test_partial_journal_name_does_not_pass_quality_gate(self):
        candidate = paper(
            "Priority Pricing in Queueing Systems",
            "A queueing model studies priority pricing, strategic customers, and admission control.",
            venue="Science",
            source="OpenAlex",
        )
        self.assertIsNone(tracker.score_paper(candidate, CONFIG, analog_query=True))


class DeduplicationTests(unittest.TestCase):
    def test_same_title_is_merged(self):
        first = paper("LLM Serving at Scale", "Short abstract", source="arXiv")
        second = paper("LLM Serving at Scale", "A much longer abstract about inference scheduling.", source="OpenAlex")
        first.relevance_score = 8
        second.relevance_score = 10
        merged = tracker.merge_papers([first, second])
        self.assertEqual(len(merged), 1)
        self.assertIn("much longer", merged[0].abstract)
        self.assertEqual(merged[0].relevance_score, 10)

    def test_arxiv_update_date_is_displayed_separately(self):
        candidate = paper("Updated paper", "Abstract")
        candidate.published = "2026-02-23"
        candidate.updated = "2026-07-15"
        self.assertEqual(
            tracker.display_dates(candidate),
            "首次发布 2026-02-23；最近更新 2026-07-15",
        )


class HomepageTests(unittest.TestCase):
    def test_original_archive_interactions_are_preserved(self):
        candidate = paper(
            "Queueing-Aware Scheduling for Large Language Model Inference",
            "We optimize request scheduling and admission control.",
        )
        tracker.score_paper(candidate, CONFIG)
        record = tracker.report_archive_record(
            [candidate],
            CONFIG,
            tracker.dt.date(2026, 7, 15),
            tracker.dt.date(2026, 7, 13),
        )
        page = tracker.build_index(CONFIG, {"reports": [record]})
        self.assertIn('id="report-year"', page)
        self.assertIn('id="paper-search"', page)
        self.assertIn('id="distribution-dialog"', page)
        self.assertIn(candidate.title, page)
        self.assertNotIn("__REPORTS_JSON__", page)

        report_page = tracker.build_html(
            [candidate],
            CONFIG,
            tracker.dt.date(2026, 7, 15),
            tracker.dt.date(2026, 7, 13),
        )
        self.assertIn("Executive Summary", report_page)
        self.assertNotIn("<h2>执行摘要", report_page)
        self.assertIn("今日速览", report_page)
        self.assertIn("最终审核清单", report_page)
        self.assertIn("研究问题", report_page)
        self.assertIn("文章怎么做", report_page)
        self.assertIn("研究启示", report_page)
        self.assertIn("英文原摘要与来源链接（补充）", report_page)

    def test_confirmed_daily_papers_survive_source_fluctuation(self):
        confirmed = tracker.load_confirmed_papers(tracker.dt.date(2026, 7, 15))
        self.assertEqual(len(confirmed), 3)
        self.assertTrue(all(paper.track == "直接 LLM 服务研究" for paper in confirmed))

    def test_cached_chinese_analysis_drives_report(self):
        confirmed = tracker.load_confirmed_papers(tracker.dt.date(2026, 7, 15))
        analyses = tracker.load_analysis_cache()
        report_page = tracker.build_html(
            confirmed,
            CONFIG,
            tracker.dt.date(2026, 7, 15),
            tracker.dt.date(2026, 7, 13),
            analyses,
        )
        self.assertIn("编排式 AI 智能体系统的一般均衡理论", report_page)
        self.assertIn("核心公式", report_page)
        self.assertIn("中文深度分析", report_page)
        self.assertIn("tex-mml-chtml.js", report_page)
        self.assertIn(r"\(\pi_a(p)=\sup", report_page)
        self.assertNotIn("<b>背景问题</b>", report_page)
        self.assertNotIn("<b>读前提示</b>", report_page)


if __name__ == "__main__":
    unittest.main()
