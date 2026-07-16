# LLM 服务运营研究追踪器

面向 LLM-as-a-Service 研究的每日文献追踪器，重点不是泛 AI 技术，而是：

- Token/API 定价、订阅、额度套餐和价格歧视；
- LLM 推理排队、调度、batching、prefill/decode 与 KV cache；
- 付费优先、SLO、deadline 和差异化服务；
- GPU/云容量、资源配置、扩缩容和拥堵；
- 数据中心电力、碳、水约束与跨时段负载转移；
- 平台定价、竞争、机制设计和战略用户。

## 这次改造补了什么

下载到的公开仓库只包含 `site/` 静态网页和 GitHub Pages 部署流程，README 中提到的私有日报生成器不在仓库中。因此，本项目新增了一套独立、可运行的替代实现：

- `config/llm_service_ops.json`：研究主题、关键词、排除词、期刊白名单和检索式；
- `scripts/track_literature.py`：查询 arXiv/OpenAlex、筛选、评分、去重、分类并生成报告；
- `data/paper_analysis_zh.json`：已核验论文的中文深度分析缓存，包含研究问题、方法、模型、公式、求解、结果和研究启示；
- `data/confirmed_papers.json`：已经人工确认的当日论文集合；来源接口临时漏报时，同一天的已发布论文不会被自动删掉；
- `tests/test_tracker.py`：防止泛 LLM benchmark 或低质量类比论文混入；
- `.github/workflows/daily-literature.yml`：北京时间每天 08:00 自动运行并提交日报；
- `reports/`：Markdown 日报；
- `site/`：可由 GitHub Pages 直接发布的 HTML 日报和索引。

检索与网页生成使用 Python 标准库；若要自动读取 PDF 全文，需要 `pypdf`。已收录论文可直接使用中文分析缓存；若希望每天对新论文自动生成同样完整的中文解读，需要配置 OpenAI API key。

## 筛选逻辑

系统保留两条研究线：

1. **直接 LLM 服务研究**：论文必须同时命中 LLM/GenAI 语境和至少一个服务运营主题。
2. **高质量服务运营机制桥接**：可以不直接讨论 LLM，但必须来自配置中的质量期刊，并高度命中排队、优先权、容量或定价机制。

提示工程、越狱、医学诊断、通用 benchmark 等主题会被排除或降分。同 DOI 或同题名的 arXiv/期刊版本会合并。

## 本地运行

在项目根目录运行：

```powershell
# 用于 PDF 全文提取
python -m pip install pypdf

python scripts/track_literature.py
```

如果系统没有全局 `python`，可在 Codex 中使用工作区附带的 Python 运行时。常用参数：

```powershell
# 指定报告日期与回看窗口
python scripts/track_literature.py --date 2026-07-15 --lookback-days 3

# 只测试 OpenAlex，减少调试时的请求量
python scripts/track_literature.py --source openalex --max-per-query 20

# 运行单元测试
python -m unittest discover -s tests -v
```

建议设置 `OPENALEX_EMAIL` 环境变量，进入 OpenAlex polite pool；不设置也能运行：

```powershell
$env:OPENALEX_EMAIL="your_email@example.com"
python scripts/track_literature.py
```

## 中文深度分析

日报主体全部以中文输出，英文原标题和英文原摘要只放在补充位置。每篇论文固定包含：

1. **研究问题**：用一句话说明论文真正要回答的问题；
2. **文章怎么做**：说明使用什么方法、模型或实验，并具体做了什么；
3. **研究启示**：说明它与 Token 定价、排队调度、优先权/SLO、容量和平台机制研究的关系；
4. **模型设定**：参与者、决策变量、关键参数、研究时序、核心公式、求解方法、主要结果与局限。

表达面向刚接触该领域的读者：先用日常语言解释，再在必要时补充专业名词；公式使用 MathJax 排版，并在公式下面逐个解释符号和直观含义。

对新论文自动生成中文分析时，设置：

```powershell
$env:OPENAI_API_KEY="你的 API key"
$env:OPENAI_ANALYSIS_MODEL="gpt-5.6-luna"  # 可替换为账号可用的兼容模型
python scripts/track_literature.py
```

没有 API key 时，检索和网页仍会运行；但新论文会明确显示“待全文核验”，不会把英文摘要冒充中文模型分析。

## 调整关键词

只需编辑 `config/llm_service_ops.json`：

- `direct_llm_terms`：什么算直接 LLM 语境；
- `categories[].terms`：六条研究主线各自的关键词；
- `exclusion_terms`：需要降分的泛 AI 主题；
- `quality_venues`：机制桥接条目的期刊白名单；
- `source_queries`：真正发送给 arXiv/OpenAlex 的检索式；
- `min_relevance_score`：越高越精确，越低召回越多。

## GitHub 自动运行

1. 把本目录作为一个 GitHub 仓库推送；
2. 在仓库 Settings → Actions → General 中允许 Actions 写入仓库；
3. 添加 `OPENAI_API_KEY` repository secret，使新论文自动生成中文深度分析；`OPENALEX_EMAIL` 为可选 secret；
4. 可选：添加 `OPENAI_ANALYSIS_MODEL` repository variable；默认使用工作流内配置的成本敏感型模型；
5. 在 Actions 页面手动运行一次 **Daily LLM literature tracker**；
6. 在 Settings → Pages 中选择 **GitHub Actions** 作为发布源。

每日工作流会生成日报、提交 `reports/`、`data/` 和 `site/`，并在同一次运行中发布 GitHub Pages。独立的 `Deploy GitHub Pages` 工作流继续负责人工推送到 `main` 时的网页发布；由 `GITHUB_TOKEN` 产生的自动提交不会重复触发它。

## 数据与核验边界

日报中的题录和摘要来自 arXiv/OpenAlex。模型解读会优先提取可访问 PDF 全文；无法取得全文时必须在核验说明中标记证据边界，不允许从摘要虚构公式。中文“研究启示”是面向本项目的机制迁移判断，不是论文作者的原始结论，也不能替代全文阅读。预印本作者质量目前不做自动猜测。
