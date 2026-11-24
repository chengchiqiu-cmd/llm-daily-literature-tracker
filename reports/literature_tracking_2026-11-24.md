# 2026-11-24 LLM 服务系统每日文献简报

> 检索窗口：2026-11-23 至 2026-11-24（北京时间 / Asia/Shanghai）；本期确认 5 篇，其中直接 LLM 服务研究 5 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 实现协议效应的明确性:超级基板互连探索的LLM-to-packet模拟

> 英文原标题：Making Protocol Effects Explicit: LLM-to-Packet Simulation for Superpod Interconnect Exploration

- **作者：** Yu Zhu、Xinhao Yang、Zhaoshi Li、Baodong Wu、Boxun Li、Wenxue Li、Guohao Dai、Hongyang Jia 等
- **来源/日期：** arXiv；2026-11-23；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 11
- **链接：** [论文页](http://arxiv.org/abs/2611.30191v1) · [PDF](https://arxiv.org/pdf/2611.30191v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、queueing。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 已成为现代人工智能服务的基础.LLM尺寸和背景长度的快速增长已经超过了单个GPU或NPU的内存容量,需要在设备之间进行模型分区.然而,在设备之间进行模型分区引入了昂贵的通信费用,从而推动了大规模,高带宽,低延迟扩展布料的超级Pod的需求. 探索超级 Pod 设计需要精确的互联网模拟,因为通信延迟由链接技术,拓学和扩展协议-堆选择共同决定.延迟带宽模型使用启动术语和信息大小和有效带宽衍生的传输术语估计通信延迟.但它们无法捕捉争端和协议效应. 包级模拟器如ns-3模型路由,排队和包时间,但需要协议特定的LLM-to-packet实现.本文介绍了ProtoBridge,一个基于ns-3的LLM-to-packet模拟器用于超底互联探索. 为了使协议效果明确,ProtoBridge在ns-3上引入了两个抽象层: (1) 捕捉协议特定的包交换和依赖性的操作到包 (OTP) 层, (2) 应用共享的包级机制到ns-3事件系统的包执行层 (PEX).ProtoBridge在H200 NVLink4上实现平均延迟错误17.8%和C500 MetaXLink上实现平均延迟错误10.3%. 为了实现更快的超基基评估,我们推出了一个替代模型,该模型将OTP参数与PEX机制的分析模型结合起来.替代模型将评估时间从2.38$\sim$75.70s减少到每次操作的20.5us. 我们使用ProtoBridge来分析两个新兴的超级Pod设计,扩展内存池和共包装光学 (CPO) 互联, 揭示未来LLM超级Pod架构的设计见解.

### 英文原摘要

Large language models (LLMs) have become the foundation of modern AI services. The rapid growth of LLM sizes and context lengths has exceeded the memory capacity of a single GPU or NPU, requiring model partitioning across devices. However, partitioning models across devices introduces costly communication overhead, driving the need for superpods with large-scale, high-bandwidth, low-latency scale-up fabrics. Exploring superpod designs requires accurate interconnect simulation, as communication latency is jointly determined by link technologies, topologies, and scale-up protocol-stack choices. Latency-bandwidth models estimate communication latency using a startup term and a transfer term derived from message size and effective bandwidth. But they fail to capture contention and protocol effects. Packet-level simulators like ns-3 model routing, queueing, and packet timing, but require protocol-specific LLM-to-packet implementations. This paper presents ProtoBridge, an ns-3-based LLM-to-packet simulator for superpod interconnect exploration. To make protocol effects explicit, ProtoBridge introduces two abstraction layers over ns-3: (1) an operation-to-packet (OTP) layer that captures protocol-specific packet exchanges and dependencies, and (2) a packet-execution (PEX) layer that applies shared packet-level mechanisms to the ns-3 event system. ProtoBridge achieves average latency error of 17.8\% on H200 NVLink4 and 10.3\% on C500 MetaXLink. To enable faster superpod evaluation for further interconnect exploration, we derive a surrogate model that combines OTP parameters with analytical models of PEX mechanisms. The surrogate reduces evaluation time from 2.38$\sim$75.70s to 20.5us per operation. We use ProtoBridge to analyze two emerging superpod designs, scale-up memory pool and co-packaged optics (CPO) interconnects, revealing design insights for future LLM superpod architectures.

## 2. 自动SECO:自动化技能演变与一般目的LLM代理人进行跨问题结合优化

> 英文原标题：AutoSECO: Automated Skill Evolution for Cross-Problem Combinatorial Optimization with General-Purpose LLM Agents

- **作者：** Zirui Zhu、Cong Zhang、Ni Zhang、Kuan Xu、Zhiguang Cao
- **来源/日期：** arXiv；2026-11-23；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.30139v1) · [PDF](https://arxiv.org/pdf/2611.30139v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

一般用途的大语言模型 (LLM) 代理可以为组合优化问题开发完整的解决方案.然而,它们的专业化往往依赖于针对单个问题的工程工作流程,从而限制了开发专业知识的重复使用.我们建议AutoSECO,这是一个自动化技能进化方法,从经验中学习可重复使用的解决方案开发指导. 挑战在于,外部评估测量已完成的解决方案,而技能在开发过程中指导决策.AutoSECO通过通过解决方案代码和记录的开发决策来追踪性能缺陷,将这种反与指导缺陷联系起来. 修改表达为一般指令,并且只保留在修改技能下开发的新型解决器达到较低的平均评估差距时. 仅仅基于旅行销售人员问题 (TSP) 发展的技能,在开发有能力的车辆路由,工作店安排和三维垃圾箱包装的解决器方面指导新型代理人,而没有进一步的技能演变. 在TSP上,最终的平均基准差距为0.52\%,而技能进化基线SkillOpt的0.98\%.在四个问题中,进化的技能比没有技能指导,初始技能和SkillOpt获得更好的综合结果.同样的结技能也支持在替代模型-架配置下解决方案开发. 这些发现表明,解决方案开发经验可以作为一般目的LLM代理人可重复使用的专业知识保留.

### 英文原摘要

General-purpose large language model (LLM) agents can develop complete solvers for combinatorial optimization problems. Their specialization, however, often relies on workflows engineered for individual problems, limiting the reuse of development expertise. We propose AutoSECO, an automated skill evolution method that learns reusable solver-development guidance from experience. The challenge is that external evaluation measures the completed solver, while the skill guides decisions during development. AutoSECO connects this feedback to guidance deficiencies by tracing performance shortfalls through solver code and recorded development decisions. Revisions are expressed as general instructions and retained only if a fresh solver developed under the revised skill achieves a lower mean evaluation gap. Evolved solely on the traveling salesperson problem (TSP), the skill guides fresh agents in developing solvers for capacitated vehicle routing, job-shop scheduling, and three-dimensional bin packing without further skill evolution. On TSP, the final mean benchmark gap is 0.52\%, compared with 0.98\% for the skill-evolution baseline SkillOpt. Across all four problems, the evolved skill achieves better aggregate results than no skill guidance, the initial skill, and SkillOpt. The same frozen skill also supports solver development under alternative model--harness configurations. These findings suggest that solver-development experience can be retained as reusable expertise for general-purpose LLM agents.

## 3. 在国内芯片和框架上推进边界代理模式

> 英文原标题：TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- **作者：** Xingchen AGI Lab、:、Baotian Hu、Bingkai Yang、Boyang Wang、Changzai Pan、Chao Lyu、Chao Wang 等
- **来源/日期：** arXiv；首次发布 2026-11-17；最近更新 2026-11-23；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.22115v2) · [PDF](https://arxiv.org/pdf/2611.22115v2)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、scheduling、optimization。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

我们介绍了Xing 4,一系列大型语言模型,通过Ascend模型架构和培训基础设施的协调进步,扩大了TeleChat流程.本报告描述了该系列背后的设计原则和系统工程,涵盖了建筑选择,大规模预训,推理和代理后训练. 我们研究如何稀疏的激活,注意力设计,模型深度和宽度以及推测式解码平衡模型容量与计算,内存访问和执行总额.我们的预训基础设施基于MindSpore HyperParallel,结合了对拓知识的混合碎片化,高效的分布式优化器执行和长序列工作负载和激活内存的协调管理. 这些机制支持在8,192 Ascend 910C卡上进行285B参数模型的预训练,为建筑和系统研究提供了具体的设置.为后培训,我们推出了TeleGym,一个统一的代理执行平台,将执行,评估和轨迹构建与政策优化联系起来. 分散的异步执行,有限的过量样本处理和部分部署都适应异质任务持续时间,同时保持政策更新中的轨迹连续性.这些进步共同建立了一个以升级为导向的培训基础,以继续发展Xing4在模型尺度和越来越苛刻的推理和代理工作负载上.

### 英文原摘要

We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model depth and width, and speculative decoding balance model capacity with computation, memory access, and execution overhead. Our pretraining infrastructure builds on MindSpore HyperParallel, combining topology-aware hybrid sharding, efficient distributed optimizer execution, and coordinated management of long-sequence workloads and activation memory. CPU affinity and core isolation further reduce host scheduling interference. Together, these mechanisms support the pretraining of a 285B-parameter model on 8,192 Ascend 910C cards, providing a concrete setting for the architectural and systems studies. For post-training, we introduce TeleGym, a unified agent execution platform that connects execution, evaluation, and trajectory construction to policy optimization. Disaggregated asynchronous execution, bounded oversampling, and partial rollout accommodate heterogeneous task durations while preserving trajectory continuity across policy updates. Together, these advances establish an Ascend-oriented training foundation for the continued development of Xing 4 across model scales and increasingly demanding reasoning and agent workloads.

## 4. MemT-1.0:向记忆原生进化

> 英文原标题：MemT-1.0: Towards Memory-Native Evolution

- **作者：** Zhiyu Li、Zeyu Zhang、Linyun Liu、Yiwei Bu、Chenyang Xi、Xichong Zhang、Yi Yu、Yu Yu 等
- **来源/日期：** arXiv；首次发布 2026-10-19；最近更新 2026-11-23；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](http://arxiv.org/abs/2610.26825v5) · [PDF](https://arxiv.org/pdf/2610.26825v5)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 foundation model、kv cache。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

记忆原生进化需要使记忆成为基础模型的内在能力,使它们能够不断积累和利用信息.为了此,我们引入了MemT-1.0,一种新的内存基础模型架构,将记忆作为模型计算的一部分内存化.基于Metis,MemT-1.0采用Gated DeltaNet-2,在每个转换中具有稳定的代币级内存更新机制. 此外,我们还推出了混合存储器,以扩大原生记忆容量. 经过故意的培训后,我们开发了一套由持续的预训和后训组成的两阶段的培训管道,由34B培训数据代币和高效的培训和推断基础设施支持. 我们发布了包括Memt-1.0-Nano,Memt-1.0-Flash和Memt-1.0-Pro在内的模型家族,并对内存和一般功能进行了全面评估.结果显示,它们平均优于参数内存基线,并且与检索增强方法保持竞争力,同时大大保留了一般功能. 在 128K 代币的历史长度下,MemT-1.0-Nano 实现了大约 1.86 美元的端到端推理速度和与全文KV缓存相比持续存储的66 倍的减少.通过内部化检索的程序体验,MemT-1.0 改善了代理任务的任务成功,为内存原生进化提供了实际的步骤.

### 英文原摘要

Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We further introduce Mixture-of-Storage to scale native memory capacity. Following a deliberate backbone preparation, we develop a two-stage training pipeline consisting of continued pre-training and post-training, supported by 34B tokens of training data and efficient training and inference infrastructure. We release a model family comprising MemT-1.0-Nano, MemT-1.0-Flash, and MemT-1.0-Pro, and conduct a comprehensive evaluation of memory and general capabilities. The results show that they outperform the parametric memory baselines on average and remain competitive with retrieval-augmented methods, while largely preserving general capabilities. At a history length of 128K tokens, MemT-1.0-Nano achieves approximately $1.86\times$ end-to-end inference speedup and a $66\times$ reduction in persistent storage relative to full context KV cache. By internalizing retrieved procedural experience, MemT-1.0 improves task success on agentic tasks, providing a practical step toward memory-native evolution.

## 5. 人工智能媒介科学宪法规则:扩大理性选择 科学知识新制度主义理论

> 英文原标题：Constitutional Rules for AI-Mediated Science: Extending the Rational Choice Neo-Institutionalist Theory of Scientific Knowledge

- **作者：** Yanfei Shi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-23；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7719982) · [DOI](https://doi.org/10.2139/ssrn.7719982)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 foundation model、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

理性选择新制度主义解释了科学如何通过宪法,分配和集体规则将个人研究人员的自私行为转化为可靠的公共知识 (Shi, 2001). 自主人工智能代理和专有基础模型的兴起使该机构平衡不稳定. 这篇论文将新制度主义科学理论扩展到人工智能介导的研究,通过重新构想宪法规则作为三层次的治理层次: (1) 一个认识和技术宪法,其中认知范式与人工智能系统架构结合 ("代码作为法律"); (2) 一个机构宪法,分配权力,残余控制权和对三方主代理的责任 结构包括科学企业家,人工智能系统所有者和授权的人工代理;以及 (3) 人工循环任务,审计标准和技术防护的运营制度. 这篇论文分析了智能市场中的零成本人工智能输出和黑盒信息不对称性如何引发同行评价拥堵,不利选择和认识单元文化,该论文概述了资助机构,大学和期刊的具体宪法改革,以重新调整激励措施并保护自动发现中的进化选择.

### 英文原摘要

Rational choice neo-institutionalism explains how science transforms the self-interested actions of individual researchers into reliable public knowledge through constitutional, distributive, and aggregative rules (Shi, 2001). However, this framework assumed exclusively human cognitive agency and a clear separation between non-market academic credit and commercial property regimes. The rise of autonomous AI agents and proprietary foundation models destabilises that institutional equilibrium. This paper extends the neo-institutionalist theory of science to AImediated research by reconceptualising constitutional rules as a three-tier governance hierarchy: (1) an epistemic and technical constitution, where cognitive paradigms merge with AI system architectures ("code as law"); (2) an institutional constitution, allocating authority, residual control rights, and liability across a tripartite principal–agent structure comprising the scientific entrepreneur, the AI system owner, and the delegated artificial agent; and (3) an operational regime of Human-in-the-Loop mandates, audit standards, and technical guardrails. Analysing how zeromarginal-cost AI outputs and black-box information asymmetry induce peer-review congestion, adverse selection, and epistemic monoculture in the intellectual market, the paper outlines concrete constitutional reforms for funding agencies, universities, and journals to realign incentives and safeguard evolutionary selection in automated discovery.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
