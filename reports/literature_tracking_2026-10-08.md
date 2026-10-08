# 2026-10-08 LLM 服务系统每日文献简报

> 检索窗口：2026-10-07 至 2026-10-08（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 代理商提出,代码决定:建立股权阿尔法模型的自主研究循环框架

> 英文原标题：Agents Propose, Code Decides: An Autonomous Research Loop Framework to Build an Equity Alpha Model

- **作者：** Erfan Sadeghi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-07；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7568638) · [DOI](https://doi.org/10.2139/ssrn.7568638)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

这篇论文提出了一个自主研究循环,其中大型语言模型 (LLM) 代理商从开始到结束构建一个多因素的股权阿尔法模型,而一个固定的,基于规则的带使每一步都可进行审计.代理商决定要测试什么,代码决定如何测量它. 一个运行模型 (Claude Opus) 从一个常设指令文件中执行搜索,一个顾问模型 (Claude Fable) 审查了阶段界限和接受,以及有限制工具的五个子代理商在冷的Sharadar数据集上收集,验证,翻译,审计和评估陈和齐默曼 (2022) 开源资产定价目录中的每个预测器. 在任何候选人被选之前,已经设定了接受条款,这是一个长短的行业排名,并通过前期测试对市场进行了对冲,以及57个月的样本外期, 循环列出了陈和齐默曼 (2022) 中的所有212个目录预测器,选了107个数据可以构建的数据,并承认了14个信息已经超过了所有已持有的信息,将Fama-French (2015) 加时基线的平均级别IC从0.0145升至0.0389在1999年至2021年. 在样本中,IC保持在0.0300,而对冲的长短收益大约是预期的Sharpe (0.523对0.996),其中大部分来自对冲期. 贡献是框架而不是模型:一个自行运行的研究过程,追踪每个数字到生成的数据和代码,并报告出与它之前写下的预期相比的混合结果.

### 英文原摘要

This paper proposes an autonomous research loop in which large language model (LLM) agents build a multi-factor equity alpha model from start to finish, while a fixed, rule-based harness keeps every step auditable. Agents decide what to test, and code decides how it is measured. A runner model (Claude Opus) executes the search from a standing instruction file, an advisor model (Claude Fable) reviews phase boundaries and acceptances, and five sub-agents with restricted tools fetch, verify, translate, audit and evaluate each predictor in Chen and Zimmermann's (2022) Open Source Asset Pricing catalogue on a frozen Sharadar dataset. The acceptance bars, a long-short ranked within sector and hedged to the market by an ex-ante beta, and a 57-month out-of-sample period were fixed before any candidate was screened, and the human answers a closed list of seven questions rather than directing the search. The loop inventoried all 212 catalogue predictors in Chen and Zimmermann (2022), screened the 107 the data could construct, and admitted 14 whose information was significant beyond every leg already held, raising a Fama-French (2015) plus-momentum baseline's mean rank IC from 0.0145 to 0.0389 over 1999 to 2021. Out of sample the IC held at 0.0300, while the hedged long-short earned about half its expected Sharpe (0.523 against 0.996), most of it from the hedge term. The contribution is the framework rather than the model: a research process that runs itself, traces every number to the data and code that produced it, and reports a mixed result against expectations it wrote down before it looked.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
