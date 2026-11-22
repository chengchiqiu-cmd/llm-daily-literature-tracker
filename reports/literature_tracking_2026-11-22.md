# 2026-11-22 LLM 服务系统每日文献简报

> 检索窗口：2026-11-21 至 2026-11-22（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 在云和无服务器平台中进行阶段分类的LLM推理的碳意识计划:审查和模拟

> 英文原标题：Carbon-Aware Scheduling for Phase-Disaggregated LLM Inference in Cloud and Serverless Platforms: Review and Simulation

- **作者：** Umar Iqbal
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-21；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7715978) · [DOI](https://doi.org/10.2139/ssrn.7715978)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、llm inference、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

互动大语言模型 (LLM) 推断分为多区域云集群和无服务器GPU池的计算预填和内存带宽解码阶段. 一项以PRISMA-2020为指导的65项工作的审查表明,虽然最近的系统单独处理子集 (包括单集群分类的GreenLLM和多数据中心碳路由器),但没有一个系统联合集成预填/解码分类,广域关键值 (KV) 转移关口,主机和GPU体现的碳抵消,以及无服务器检查点保持活力, 制造业的排放量. 为了评估这个设计空间,我将一个ISO/IEC 21031:2024软件碳强度 (SCI) 控制架构正式化成一个基于追踪的SimPy 4.1.2分化事件模拟器,根据发布的服务基准和持久扩展趋势进行验证. 通过Azure LLM跟踪,英国NESO和日本TSO网络远程测量驱动的10种配对种子,混合路由在交谈流量上降低了高达60.8%的运营SCI和高达54.9%的总SCI0.81%-0.82%的SLO违规,即使在400Gbps链接上也削减了跨地区KV管道低于0.31%,并且降低了85.2%-86.0%的破裂代码SLO违规,低于无条件的地理分类. 在风电清洁电网上,折扣硬件达到总SCI的93.0%-97.6%,导致四个备用清洁节点在名额负载下将生命周期排放量提高27.7%-32.6%然后在需求超过1.6x-1.7x的破解平衡门时将碳减少 (-30.6%到3.0x36.5%).

### 英文原摘要

Interactive large language model (LLM) inference separates into compute-bound prefill and memory-bandwidthbound decode stages across multi-region cloud clusters and bursty serverless GPU pools. A PRISMA-2020-guided review of 65 works shows that while recent systems address subsets in isolation (including single-cluster disaggregated GreenLLM and colocated multi-datacenter carbon routers), no implemented system jointly integrates prefill/decode disaggregation, wide-area key-value (KV) transfer gating, host and GPU embodied carbon amortization, and serverless checkpoint keep-alive, and 76.9% of reviewed studies omit manufacturing emissions. To evaluate this design space, I formalize an ISO/IEC 21031:2024 Software Carbon Intensity (SCI) control architecture in a trace-driven SimPy 4.1.2 discreteevent simulator validated against published serving benchmarks and held-out scaling trends. Over 10 paired seeds driven by Azure LLM traces, UK NESO, and Japan TSO grid telemetry, hybrid routing lowers operational SCI by up to 60.8% and total SCI by up to 54.9% on conversational traffic at 0.81%-0.82% SLO violations, prunes cross-region KV pipelining below 0.31% even on 400 Gbps links, and reduces bursty-code SLO violations by 85.2%-86.0% below unconditional geographic disaggregation. On wind-clean grids, amortized hardware reaches 93.0%-97.6% of total SCI, causing four spare clean nodes to raise lifecycle emissions by 27.7%-32.6% at nominal load before turning carbon-reducing (-30.6% to-36.5% at 3.0x) once demand crosses a 1.6x-1.7x break-even threshold.

## 2. 从试点到生产:制造业管理人工智能以决策为中心的框架

> 英文原标题：From Pilot to Production: A Decision-Centred Framework for Governed AI in Manufacturing Operations

- **作者：** Farhood Salami Araghi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-21；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7715961) · [DOI](https://doi.org/10.2139/ssrn.7715961)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、scheduling。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工智能 (AI) 现在在制造业中被广泛试点化,但许多试点并没有成为可靠的生产系统.这篇论文认为,主要的障碍不是算法能力,而是缺乏以决策为中心的设计纪律,将数据,模型,人员和治理联系在一起. 基于作者"人工智能驱动生产管理" (2026) 的书,它提出了一个框架,其中每个人工智能应用都从一个命名的运营决定,其所有者和测量的基线开始,并由明确的权威限制,人力控制和监控局限.该框架应用于四个核心领域:质量控制,生产规划,供应链管理和预测维护. 它扩展到数字双胞胎,代理人工智能和大型语言模型.一个假设英国液压设备制造商的组件准备预测可复制的合成案例研究说明了评估纪律.一个梯度增强分类器达到0.669对0.587的ROC-AUC,而透明规则则则保持更高的回忆 (0.768对0.652). 该论文还列出了杀死标准的阶段门,NPV敏感性表明40%的利息实现短缺可能会使阳性病例变成负面,以及2026年10月英国和欧盟的监管立场.

### 英文原摘要

Artificial intelligence (AI) is now widely piloted in manufacturing, yet many pilots do not become dependable production systems. This paper argues that the main obstacle is not algorithmic capability but the absence of a decision-centred design discipline that links data, models, people and governance. Drawing on the author's book AI-Driven Production Management (2026), it proposes a framework in which every AI application starts from a named operational decision, its owner and a measured baseline, and is bounded by explicit authority limits, human override and monitoring. The framework is applied across four core domains: quality control, production scheduling, supply-chain management and predictive maintenance. It is extended to digital twins, agentic AI and large language models. A reproducible synthetic case study on component-readiness prediction for a hypothetical UK hydraulic-equipment manufacturer illustrates the evaluation discipline. A gradient boosting classifier reached a ROC-AUC of 0.669 against 0.587 for a transparent rule, while the rule kept higher recall (0.768 against 0.652). The paper also sets out stage gates with kill criteria, an NPV sensitivity showing that a 40% shortfall in benefit realisation can turn a positive case negative, and the UK and EU regulatory position as of October 2026. Implications for practice and research are discussed.

## 3. 服务连锁结构的工作,具有较大的内存足迹,应用到较大的基础模型服务

> 英文原标题：Serving Chain-structured Jobs with Large Memory Footprints with Application to Large Foundation Model Serving

- **作者：** Tingyang Sun、Ting He、I-Hong Hou
- **来源/日期：** ACM International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing (MobiHoc)；2026-11-22；OpenAlex
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.1145/3842721.3849638) · [DOI](https://doi.org/10.1145/3842721.3849638)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、llm、foundation model、load balancing。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

作为人工智能 (AI) 的当前趋势,大型基础模型越来越被使用为人工智能服务的核心. 然而,即使在训练后,由于它们的重资源足迹,特别是GPU内存方面,在规模上提供此类模型仍然是一个具有挑战性的任务. 虽然最近的研究揭示了服务基础模型的系统的独特特征,使它们与传统分布式计算系统区别起来,但仍然缺乏对潜在的系统管理问题的基本理解. 这项工作旨在通过区块配置和缓存配置来解决这一差距,通过通过提供大型内存足迹的链结构性工作来提取服务器链链构成的新问题,这通过管道平行性来模拟服务大型基础模型的根本问题. 在显示最佳解决方案的NP硬度后,重点转向在最先进的负载平衡下开发可扩展的算法,以保证性能. 该解决方案应用于分布式大型语言模型 (LLM) 服务系统,与最先进的解决方案相比,反应时间显著减少.

### 英文原摘要

As a current trend in Artificial Intelligence (AI), large foundation models are increasingly employed as the core of AI services. However, even after training, serving such models at scale remains a challenging task due to their heavy resource footprints, particularly in terms of GPU memory. While recent works revealed unique characteristics of systems serving foundation models that distinguish them from traditional distributed computing systems, there is still a lack of fundamental understanding of the underlying system management problems. This work aims at addressing this gap by extracting a novel problem of “server chain composition” via block placement and cache allocation for serving chain-structured jobs with large memory footprints, which models a fundamental problem in serving large foundation models through pipeline parallelism. After showing the NP-hardness of the optimal solution, the focus is turned to developing scalable algorithms with guaranteed performance under state-of-the-art load balancing. Application of the proposed solution to a distributed large language model (LLM) serving system shows significant reduction of response times compared to state-of-the-art solutions.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
