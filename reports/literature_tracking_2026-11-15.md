# 2026-11-15 LLM 服务系统每日文献简报

> 检索窗口：2026-11-14 至 2026-11-15（北京时间 / Asia/Shanghai）；本期确认 4 篇，其中直接 LLM 服务研究 4 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. RPS-Service: "岩石,石头和沙子:多模式LLM推理的规范性意识规划" (SIGOPS ATC '26) 的艺术品

> 英文原标题：RPS-Serve: Artifact for "Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal LLM Inference" (SIGOPS ATC '26)

- **作者：** Konstantinos Papaioannou、Thaleia Dimitra Doudali
- **来源/日期：** Zenodo (CERN European Organization for Nuclear Research)；2026-11-15；OpenAlex
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 12
- **链接：** [论文页](https://doi.org/10.5281/zenodo.23134684) · [DOI](https://doi.org/10.5281/zenodo.23134684)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、llm inference、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

这个文物伴随着Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference. 它包装了RPS-Serve,一个基于vLLM (v0.21.1) 的多模式LLM (MLLM) 服务的modality-aware request scheduling framework,以及修补的基线,工作负载生成器和用于制作论文结果的图案脚本. 该文物包括:RPS-Serve本身 (影响估计器,请求分类器,队列管理器和优先级监管器),用于部署基线系统的补丁vLLM (vLLM,ModServe和ModServe与RPS),用于工作负载生成和重播的GuideLLM和LLMPerf的补丁版本,用于评估的模型以及从原料实验输出中再生纸张数据的脚本. 审查人员可以使用这个文物安装软件堆,生成纸张的混合模式工作负载,在单个GPU上运行最小的端到端示例,并在可用的硬件尺度上复制纸张的实验和数字.

### 英文原摘要

This artifact accompanies Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference. It packages RPS-Serve, a modality-aware request scheduling framework for multimodal LLM (MLLM) serving built on top of vLLM (v0.21.1), together with the patched baselines, workload generators, and plotting scripts used to produce the paper's results. The artifact includes: RPS-Serve itself (Impact Estimator, Request Classifier, Queue Manager, and Priority Regulator), a patched vLLM used to deploy the baseline systems (vLLM, ModServe, and ModServe with RPS), patched versions of GuideLLM and LLMPerf for workload generation and replay, the models used for evaluation, and scripts to regenerate the paper's figures from raw experiment output. Reviewers can use this artifact to install the software stack, generate the paper's mixed-modality workloads, run a minimal end-to-end example on a single GPU, and reproduce the paper's experiments and figures at the hardware scale available to them.

## 2. 在复杂计算环境中可解释的人工智能,适应性学习和自主决策智能基础人工智能模型

> 英文原标题：Foundation AI Models for Explainable Artificial Intelligence, Adaptive Learning and Autonomous Decision Intelligence in Complex Computing Environments

- **作者：** Shubh Prabhat
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-14；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7690003) · [DOI](https://doi.org/10.2139/ssrn.7690003)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 foundation model、scheduling、resource allocation。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

复杂的计算环境的复杂性质,以及可解释性,适应性学习和可靠的决策方面的挑战, 通过提出决策知识片段 (DKF) 作为一个以文本意识的方式进行结构化和基于证据的知识传输的方法,本文引入了一个名为FUSE-AI (基础人工智能结构理解合成和进化) 的新框架. 它结合了验证包裹验证,基于矛盾的知识调整,解释重建和选择性知识调整,以便在不需要重新训练完整的基础模型的情况下实现自主决策智能化.它与四个基线模型进行了比较:传统的基础模型,检索增强的生成,转移学习和基于知识图的决策模型. 实验设计包括六个指标:决策正确性,解释正确性,传输有效性,适应时间,计算过载和限制违规率.数量评估的方法是在三个计算环境中开发的,即云资源配置编排和边缘计算中的动态任务规划. 三个计算环境:云资源配置,边缘调整和动态任务规划,旨在在在不断变化的运营场景下提供可靠性的量化评估.拟议的方法旨在提高知识传输的可靠性,保持决策的可追溯性,消除适应错误的环境. 与目前可解释和适应的基础人工智能模型的验证方法相比,

### 英文原摘要

The intricate nature of complex computing environments, coupled with the challenges in explainability, adaptive learning and reliable decision-making, makes Foundation AI models a formidable obstacle. By proposing Decision Knowledge Fragments (DKFs) as an approach for structured and evidence-based knowledge transfer in a context-aware manner, this paper introduces a novel framework called FUSE-AI (Fractured-Understanding Synthesis and Evolution for Foundation AI). It combines Validate Envelope Verification, Contradiction-driven knowledge reconciliation, Explanation reconstruction and Selective knowledge adaptation to enable autonomous decision intelligence without the need to retrain the full foundation model. It is compared with four baseline models: Conventional Foundation models, Retrieval-augmented generation, Transfer learning and Knowledge-graph-based decision models. The experimental design involves six metrics: Decision Correctness, Explanation Correctness, Transfer Validity, Adaptation Time, Computational Overload and Constraint-violation rate. Methods for quantitative evaluation are developed in three computing environments, namely, cloud resource allocation orchestration and dynamic task scheduling in edge computing. Three computing environments: cloud resource allocation, edge orchestration and dynamic task scheduling, are designed to provide quantitative evaluation of robustness under changing operation scenarios. The aim of the proposed approach is to increase the reliability of knowledge transfer, to maintain traceability of the decisions and to eliminate adaptation to a false context. The outcome will answer the question of whether fragment-level validation can offer tangible benefits when compared to current validation approaches for explainable and adaptive foundation AI models.

## 3. 从神经网络到代理网络:桌面系统设计用于企业级多模型规划

> 英文原标题：From Neural Networks to Agent Networks: Desktop System Design for Enterprise-grade Multi-model Scheduling

- **作者：** Zimeng Wang、Haowen Yan、Yuxin Luo、Mengzhe Wang、Hongkun Zhu、Tianming Wu、Hongxuan Liu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-14；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7689958) · [DOI](https://doi.org/10.2139/ssrn.7689958)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、quota。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 代理人正在从单个实例转变为群体,但企业采用面临三个实际的限制:模型配额分散在异性客户端和道之间,模型能力的任务要求不均,组织需要可观察性和问责. 该论文报告了基于企业的多代理规划的桌面系统的设计和部署状态.该系统没有自己的模型.它将本地机器和企业中的每个可用代理都视为"神经元",并在运行时进行探测,网络,规划,执行和会计.报告了四种机制. (1) 连接器适应层:四种必需方法的接口均地允许官方无头CLI和官方运行时间库,桌面应用程序调试协议桥梁和ACP漏洞,以及绕过连接器的HTTP终端点供应. (2) 快速驱动的机组人员规划:一个规划模型提供了个人资料功能;基于后填和冷却的源切换提供了故障耐受性,并且在任务级别内建立了两个协商模式 (辩论和审查),但未经验证. (3) 四个许可级别与跨协议投影:计划/构建/完整级别在列出的参数组合下设置的能力中是严格单调的,而确认级别的人类评判的语义是明确被破坏的,供应商对供应商,在无头的CLI领域. (4) 组织层面的问责链:一千秒分辨率事件流由账本编译器编译成五个字段,并将集成数据逐步报告到企业层次结构上.该系统作为电子客户端和零依赖服务器实施;试点公司配置已经实施. 我们介绍了开发机器上19天的部署事件流,机制的分析分析,界面和方案层面的文物披露,场次数据流库,授权层级分类和符合的子集的质量分析.控制实验和试点操作数据仍然是未来的工作.

### 英文原摘要

Large language model (LLM) agents are moving from single instances to swarms, yet enterprise adoption faces three practical constraints: model quota is fragmented across heterogeneous clients and channels, task demands on model capability are uneven, and organizations require observability and accountability. This paper reports the design and deployment status of a desktop system for enterprise-oriented multi-agent scheduling. The system trains no model of its own. It treats every usable agent on the local machine and in the enterprise as a "neuron" and performs probing, networking, scheduling, execution, and bookkeeping at run time. Four mechanisms are reported. (1) A connector adaptation layer: a four-required-method interface uniformly admits official headless CLIs and official runtime libraries, desktop-application debug-protocol bridges, and ACP loopbacks, together with HTTP endpoint supplies that bypass connectors. (2) Prompt-driven crew scheduling: profile features are supplied to a scheduling model; backfill and cooldown-based source switching provide failure tolerance, and two consultation modes (debate and review) are built in at the task level, implemented but unverified. (3) Four permission tiers with cross-protocol projection: the plan/build/full tiers are strictly monotone in capability set under the listed parameter combinations, while the confirm tier's human-adjudication semantics are explicitly compromised, vendor by vendor, in the headless CLI domain. (4) An organization-level accountability chain: a millisecond-resolution event stream is compiled by a ledger compiler into five-field tuples, and aggregates are reported incrementally up the corporate hierarchy. The system is implemented as an Electron client and a zero-dependency server; pilot-company provisioning is in place. We present a desensitized aggregate measurement of a 19-day deployment event stream on the development machine, analytical analysis of mechanisms, interface-and schema-level artifact disclosure, a field-by-field data-flow inventory, authorizationtier classification, and a qualitative analysis of the compliant subset. Controlled experiments and pilot operational data remain future work.

## 4. 人工智能基础设施债务量化压力测试:非平衡阶段过渡方法

> 英文原标题：Quantitative Stress Testing for AI Infrastructure Debt: A Non-Equilibrium Phase Transition Approach

- **作者：** Manoj Bhatkar、Prashant Yawalkar
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-14；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7687244) · [DOI](https://doi.org/10.2139/ssrn.7687244)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 generative ai、equilibrium。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

由于资本支出和企业收入之间的差距越来越大,生成人工智能的增长受到高基础设施成本和债务的增加所限制.根据2026年底的经验数据,包括11月的美国 与国际货币基金组织,Gartner和S&P全球的报告一起,这项研究调查了技术部门的宏观经济风险模拟. 通过结合增强的7个因素宏观经济压力模型和新型混合量子储量计算 (nHQRC) 架构,建立了多因素的系统风险和阶段过渡框架. 通过模拟循环供应商融资,信用违约 swap 扩散,银行滞后,电网限制,硬件过时和私人信用压力,该模型模拟了36个月的系统风险和多万亿美元资产损失 (约为3.5万亿至4.0万亿美元). 评估三种渐进式配置,从传统的3因素基线到增强的7因素确定性模型和nHQRC阶段过渡引擎,证明了传统线性模型为什么失败,以及量子增强方法如何在2029年前确定关键的宏观经济转折点.

### 英文原摘要

The growth of generative AI is constrained by high infrastructure costs and rising debt, driven by a widening gap between capital spending and enterprise revenue. Grounded in late-2026 empirical data, including the November U.S. tech rout, semiconductor investigations, and international equity drops like the STAR 50 crash, along with reports from the International Monetary Fund, Gartner, and S&P Global, this study investigates macroeconomic risk simulation for the technology sector. A multi-factor systemic risk and phase transition framework is established by combining an enhanced 7-factor macroeconomic stress model with a novel Hybrid Quantum Reservoir Computing (nHQRC) architecture. By modeling circular vendor financing, credit default swap spreads, bank backlogs, power grid limits, hardware obsolescence, and private credit strain, the model simulates a 36-month timeline of systemic risk and multi-trillion-dollar asset impairments ($3.5 trillion to $4.0 trillion USD exposure). Evaluating three progressive configurations, ranging from a legacy 3-factor baseline to an enhanced 7-factor deterministic model and the nHQRC phase transition engine, demonstrates why traditional linear models fail and how quantum-enhanced methods identify critical macroeconomic tipping points before 2029.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
