# 2026-09-03 LLM 服务系统每日文献简报

> 检索窗口：2026-09-02 至 2026-09-03（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 一个层次的制造智能平台,整合 Ontologies,知识图,预测分析和智能工厂运营的自主代理

> 英文原标题：A Layered Manufacturing Intelligence Platform Integrating Ontologies, Knowledge Graphs, Predictive Analytics, and Autonomous Agents for Intelligent Factory Operations

- **作者：** Khemais Jannadi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-02；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7385658) · [DOI](https://doi.org/10.2139/ssrn.7385658)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling、latency。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

越来越复杂的离散和连续的制造业需要超越传统监督控制系统的智能信息架构. 本文介绍了一个为七层制造智能平台 (MIP) 的综合概念框架,集成基于ontology的语义建模,知识图实体关系表示,基于规则的推理,图形理论预测分析,大语言模型 (LLM) 自然语言生成,人工智能辅助决策支持和自主代理驱动的操作干预. 基于ISA-95 (IEC 62264) 标准,拟议的架构为制造数据文本化提供了正式的语义基础,使设备风险状态的自动推断,多跳谱经历和实时异常分类成为可能. 图形变压器组件学习不同制造变量之间的关系模式,产生对整体设备效率 (OEE) 的概率预测,设备故障风险和预期停机时间的概率预测准确性. LLM层将分析输出转化为可验证的,文本化的自然语言叙述,而AI助理层则在没有自主干预的情况下响应复杂的操作员查询. 顶级人工智能代理级别自主执行封闭循环纠正工作流程,包括根源分析,工作订单创建,监督通知,干预计划和行动后绩效监测. 通过在塑料注塑成型生产环境中进行结构化架构分析和插图实例化,本文展示了MIP架构降低运营风险,加快纠正响应延迟,并实现可扩展,数据驱动的制造智能的机制水平途径. 未来的研究方向包括对光学限制的图形神经网络培训,多代理冲突解决,跨企业语义联合和纵向投资回报基准测量.

### 英文原摘要

The increasing complexity of discrete and continuous manufacturing operations demands intelligent information architectures that transcend conventional supervisory control systems. This paper presents a comprehensive conceptual framework for a seven-layer Manufacturing Intelligence Platform (MIP), integrating ontology-based semantic modelling, knowledge graph entity-relationship representation, rule-based reasoning, graph-theoretic predictive analytics, large language model (LLM) natural language generation, AI-assisted decision support, and autonomous agent-driven operational intervention. Grounded in the ISA-95 (IEC 62264) standard, the proposed architecture provides a formal semantic foundation for manufacturing data contextualization, enabling automated inference of equipment risk states, multi-hop genealogy traversal, and real-time anomaly classification. A graph transformer component learns relational patterns across heterogeneous manufacturing variables, producing probabilistic forecasts for Overall Equipment Effectiveness (OEE), equipment failure risk, and expected downtime with demonstrated predictive accuracy. The LLM layer translates analytical outputs into verifiable, contextualized natural language narratives, while the AI assistant tier responds to complex operator queries without autonomous intervention. The apex AI agent tier executes closed-loop corrective workflows autonomously, encompassing root cause analysis, work order creation, supervisory notification, intervention scheduling, and post- action performance monitoring. Through structured architectural analysis and illustrative instantiation within a plastic injection molding production environment, this paper demonstrates the mechanism-level pathways by which the MIP architecture reduces operational risk, accelerates corrective response latency, and enables scalable, data-driven manufacturing intelligence. Future research directions include ontology-constrained graph neural network training, multi-agent conflict resolution, cross-enterprise semantic federation, and longitudinal return-on-investment benchmarking.

## 2. memLLM-net:用于在设备上提供LLM语境的Wi-Fi,共享内存和RDMA运输的经验比较

> 英文原标题：memLLM-net: An Empirical Comparison of Wi-Fi, Shared-memory, and RDMA Transports for On-device LLM Context Delivery

- **作者：** Hari Prasad Sampatirao
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-02；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7385639) · [DOI](https://doi.org/10.2139/ssrn.7385639)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 llm、llm inference、kv cache。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

除了单个机器之外,MemLLM的[1]核心论点停止存在:它认为零拷贝共享内存消除了主导在设备上LLM推断的序列化上层费用,这是通过构建来向一个机器进行的索赔. memLLM-net测试在该范围边缘发生的事情. 我们在现实硬件上构建和验证: (i) 在应用程序和推断服务器不配合位置的情况下,在合成损失上进行 eRPC 式可靠的运输,然后在两个物理设备之间建立真正的家庭 Wi-Fi 连接; (ii) Linux memfd_create/eventfd共享内存路 MemLLM 总是描述但从未测量,完成了自己的声明的评估缺口; 软RoCE,不需要专门的硬件. 在Wi-Fi运输的构建中出现了五个真正的缺陷,其中包括重试风暴故障模式, 真正的共享内存比Wi-Ficapable运输大约4x,真正的RDMA动词比我们自己的Python共享内存实现大约36x在同一台机器上. 我们还认为KV缓存几乎永远不应该跨越网络:仅仅跟踪变化的客户端,而不是缓存本身,

### 英文原摘要

Beyond a single machine is where MemLLM's [1] central argument stops holding: it argued that zero-copy shared memory eliminates the serialization overhead dominating on-device LLM inference, a claim scoped, by construction, to one machine. memLLM-net tests what happens at that scope's edges. We build and validate, on real hardware: (i) an eRPC-style reliable transport for the case where the application and inference server are not co-located, exercised over synthetic loss and then a real home Wi-Fi link between two physical devices; (ii) the Linux memfd_create/eventfd shared-memory path MemLLM always described but never measured, completing its own stated evaluation gap; and (iii) a real RDMA transport via Soft-RoCE, requiring no specialized hardware. Five genuine defects surfaced and were fixed in building the Wi-Fi transport, including a retry-storm failure mode that reproduces, and complicates, the standard claim that RoCE livelocks on lossy links. Real shared memory beats the Wi-Ficapable transport by roughly 4× and real RDMA verbs beat our own Python shared-memory implementation by roughly 36× on the same machine-a measured ceiling this line of work falls well short of. We further argue, against an earlier framing of our own, that the KV cache should almost never cross the network at all: a thin client tracking only what changed, not the cache itself, is sufficient for the common architecture, which reframes what "KV-cache-over-Wi-Fi" should actually mean.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
