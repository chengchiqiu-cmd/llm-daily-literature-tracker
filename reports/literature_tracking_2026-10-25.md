# 2026-10-25 LLM 服务系统每日文献简报

> 检索窗口：2026-10-24 至 2026-10-25（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. HiKnow-LAS:云端GPU集群的层次知识驱动的LLM增强计划架构

> 英文原标题：HiKnow-LAS: Hierarchical Knowledge-Driven LLM-Augmented Scheduling Architecture for Cloud-Edge GPU Cluster

- **作者：** Chao Liang、Xingwei Wang、Qiang He、Bo Peng、Zhijiang Wang、Min Huang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-24；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7665885) · [DOI](https://doi.org/10.2139/ssrn.7665885)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 llm、scheduling、latency、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

云端协作GPU集群对于延迟敏感的深度学习推断至关重要;然而,动态工作负载,异质资源和GPU共享所产生的干扰挑战了高效的规划.我们建议为云端GPU集群提供HiKnow-LAS,一个\emph{hierarchical Knowledge-Driven LLM-Augmented Scheduling Architecture}. 该架构将规划过程分解成三个协调层次:一个执行基于历史知识的语义意识政策演变的战略优化层次,具有工作负载级别干扰建模方案,以确保为动态到达任务提供明确干扰模型;通过反驱动的在线参数来管理参数调整的适应性调整层次 调整和政策导向的稳定机制;以及通过结合排队意识的节点选择和干扰意识的GPU分配策略来做出决策的快速安排层. 通过关闭循环知识更新和运行时间反,HiKnow-LAS实现了自我进化. 广泛的追踪实验表明,与最具性能的基线相比,HiKnow-LAS将平均任务延迟降低10.0%和每任务的能源消耗降低7.2%;此外,缩研究独立验证了每个层和LLM本身的贡献.

### 英文原摘要

Cloud-edge collaborative GPU clusters are critical for latency-sensitive deep learning inference; however, efficient scheduling is challenged by dynamic workloads, heterogeneous resources, and interference arising from GPU sharing. We propose HiKnow-LAS, a \emph{Hierarchical Knowledge-Driven LLM-Augmented Scheduling Architecture} for cloud-edge GPU clusters. This architecture decomposes the scheduling process into three coordinated layers: a strategic optimization layer that performs semantic-aware policy evolution based on historical knowledge, with a workload-class-level interference modeling scheme to ensure well-defined interference models for dynamically arriving tasks; an adaptive adjustment layer that manages parameter tuning through feedback-driven online parameter adaptation and policy-guided stabilization mechanisms; and a fast scheduling layer that makes decisions by combining queue-aware node selection with interference-aware GPU allocation strategies. HiKnow-LAS achieves self-evolution through closed-loop knowledge updates and runtime feedback. Extensive trace-driven experiments demonstrate that, compared to the best-performing baseline, HiKnow-LAS reduces average task latency by 10.0\% and energy consumption per task by 7.2\%; furthermore, ablation studies independently validate the contributions of each layer and the LLM itself.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
