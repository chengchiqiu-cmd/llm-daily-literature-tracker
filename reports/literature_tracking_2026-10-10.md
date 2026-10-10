# 2026-10-10 LLM 服务系统每日文献简报

> 检索窗口：2026-10-09 至 2026-10-10（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. GARF:在能源,碳和延迟限制下的可持续人工智能的恢复第一框架

> 英文原标题：GARF: A Reclamation-First Framework for Sustainable AI Under Energy, Carbon, and Latency Constraints

- **作者：** Dipul Poudel
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-09；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7589164) · [DOI](https://doi.org/10.2139/ssrn.7589164)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 llm、llm serving、priority。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

现代人工智能系统在电力,碳预算,硬件成本和响应延迟方面越来越严格运行,但常见的做法仍然将扩展视为提高性能的默认杆. 在固定资源限制下,在添加新的计算之前,应尝试恢复可避免的计算损失 (无效加速器时间,冗余的计算,过度参数化的模型). 我们将这一优先事项正式化为绿色人工智能回收框架 (GARF),一个可伪造的决策规则基于最近独立发表的测量研究的综合性:量化微调,保持任务准确性,同时大幅减少训练硬件需求, 电气电机的大部分能量都在名义上置. 据证实,采用回收技术增加了端到端的能源使用,而不是宣称普遍效益的理由是GARF明确的边界条件. 我们报告了该协议的第一次实验测试:在一个固定语言建模任务上,试点比较了与4位量化低级适应 (QLoRA) 的完整细调,

### 英文原摘要

Modern AI systems increasingly operate under hard limits on power, carbon budget, hardware cost, and response latency, yet common practice still treats scaling as the default lever for improving performance. This paper argues for a different default: under a fixed resource constraint, recovering avoidable compute losses (idle accelerator time, redundant computation, over-parameterized models) should be attempted before adding new compute. We formalize this priority as the Green AI Reclamation Framework (GARF), a falsifiable decision rule grounded in a synthesis of recent, independently published measurement studies: quantized fine-tuning that preserves task accuracy while sharply reducing training hardware needs, memory-management techniques that raise LLM serving throughput several-fold on unchanged hardware, and cluster-telemetry studies showing accelerators spend a large share of energy nominally idle. A documented counter-example, in which a reclamation technique increased end-to-end energy use, motivates GARF's explicit boundary conditions rather than a claim of universal benefit. We report a first empirical test of the protocol: a pilot comparing full fine-tuning against 4-bit quantized low-rank adaptation (QLoRA) on a fixed language-modeling task, where reclamation-first cut measured GPU energy by 54.9% and wall-clock time by 53.5% (paired t-test, N = 3, p

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
