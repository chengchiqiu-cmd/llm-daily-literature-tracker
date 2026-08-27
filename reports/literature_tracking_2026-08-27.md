# 2026-08-27 LLM 服务系统每日文献简报

> 检索窗口：2026-08-26 至 2026-08-27（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 超越连接:对长文本LLM培训的序列包装调查

> 英文原标题：Beyond Concatenation: A Survey of Sequence Packing for Long-Context LLM Training

- **作者：** Yue Min、Ruining Chen、Yuan Cheng、Tianze Xu、Jianghao Yang、Bowei He、Meng Ding、Tian Zhang 等
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-26；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7343278) · [DOI](https://doi.org/10.2139/ssrn.7343278)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、scheduling。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

扩展大型语言模型 (LLM) 的文本窗口不仅需要建筑修改或扩展定位表示,还取决于训练数据是如何组织和包装成扩展序列的. 虽然天真连锁最大限度地利用代币,但它可以破坏文档界限,混合无关的文本,重量化示例,并无法提供有意义的长距离监督. 根据我们所知,本文介绍了首个针对长文本LLM培训序列包装的调查,涵盖预训练,持续预训练,监督细节调整和邻近偏好优化.我们组织了围绕四个角色的包装干预:序列分配和完整性,文本构建,工作负载安排和共享结构重复使用. 通过比较代表性框架,我们分析包装单元,成员选择和顺序,边界和监督政策,元数据要求,执行和评估目标. 最后,我们为可审核的长文本培训管道推出了实用原则,强调了边界保护,关系意识过,目标和损失正常化,清除污染和框架层次的元数据集成.调查显示了数据组织如何塑造长文本利用和执行工作负载,并为未来的培训食谱提供了实用基础.

### 英文原摘要

Scaling the context window of large language models (LLMs) requires more than architectural modifications or extended positional representations. It also depends on how training data are organized and packed into extended sequences. While naive concatenation maximizes token utilization, it can disrupt document boundaries, mix unrelated contexts, reweight examples, and fail to provide meaningful long-range supervision. To the best of our knowledge, this paper presents the first survey dedicated to sequence packing for long-context LLM training, spanning pretraining, continued pretraining, supervised finetuning, and adjacent preference optimization. We organize packing interventions around four roles: Sequence Allocation and Integrity, Context Construction, Workload Scheduling, and Shared-Structure Reuse. We further examine relationaware data selection and organization strategies that seek useful long-range supervision beyond simple length heuristics. By comparing representative frameworks, we analyze packing units, member selection and order, boundary and supervision policies, metadata requirements, execution, and evaluation targets. Finally, we derive practical principles for robust, auditable long-context training pipelines, emphasizing boundary preservation, relation-aware filtering, target and loss normalization, decontamination, and framework-level metadata integration. The survey shows how data organization shapes both long-context utilization and executed workload, and provides a practical foundation for future training recipes.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
