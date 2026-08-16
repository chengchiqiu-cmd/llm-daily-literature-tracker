# 2026-08-17 LLM 服务系统每日文献简报

> 检索窗口：2026-08-16 至 2026-08-17（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 打破记忆墙:对高效的大语言模型 (LLM) 输入的关键值 (KV) 缓存压缩的调查

> 英文原标题：Breaking the Memory Wall: A Survey of Key-Value (KV) Cache Compression for Efficient Large Language Model (LLM) Inference

- **作者：** Manpreet Singh、Yash Jajoo、Rohith Reddy Bellibatlu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-16；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 11
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7273098) · [DOI](https://doi.org/10.2139/ssrn.7273098)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、kv cache。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大语言模型 (LLM) 在长文本长度的部署越来越受到记忆而不是计算的限制.在自动降级解码过程中,密钥值 (KV) 缓存存储处理代币的密钥和值激活,随着序列长度和批量大小而线性增长,并且必须经常为每个生成的代币流. 在长文本和高吞吐量设置中,这使得解码将存储器绑定到带宽,并暴露了存储器墙. 这项调查提供了一个统一的,硬件意识的处理,减轻这种瓶的技术. 我们通过屋顶线模型和VRAM足迹分析将计算式预填写与内存式解码分开,然后将文献组织成四个互补层:算法压缩 (量化,排放和稀释,以及代币,低级或学习合并);建筑重新设计 (多级查询和集成查询关注,低级隐藏关注,以及反复或混合 国家空间模型);系统级管理 (页面内存,前置共享,交叉请求运输和层次卸载);以及硬件加速 (解码内核,融合和内存处理). 与之前的调查不同,我们 (a) 将四层层统一在共同设计和Pareto边界框架下, (b) 巩固了多租户KV缓存安全性和侧通道泄漏的证据, (c) 在长视野代理循环中分析缓存退化. 为了使这一差距可行化,我们提出了匹配预算评估 (MBE),一个轻量级的报告协议和附带的试点工具来描述KV缓存结果在固定的内存预算下.我们提出了MBE作为一个标准化提案,而不是一个完全验证的基准标准.它针对研究人员和工程师在部署限制下结合KV缓存优化.

### 英文原摘要

The deployment of large language models (LLMs) at long context lengths is increasingly limited by memory rather than compute. During autoregressive decoding, the key-value (KV) cache stores the key and value activations of processed tokens, grows linearly with sequence length and batch size, and must often be streamed for each generated token. In long-context and high-throughput settings, this makes decoding memory-bandwidthbound and exposes the memory wall. This survey gives a unified, hardware-aware treatment of techniques that mitigate this bottleneck. We formalise it through the roofline model and a VRAM-footprint analysis separating compute-bound prefill from memorybound decoding, then organise the literature into four complementary layers: algorithmic compression (quantization, eviction and sparsification, and token, low-rank, or learned merging); architectural redesign (multi-query and grouped-query attention, low-rank latent attention, and recurrent or hybrid state-space models); system-level management (paged memory, prefix sharing, cross-request transport, and tiered offloading); and hardware acceleration (decoding kernels, fusion, and processing-in-memory). For each we give the governing mechanism, achievable memory reduction, and accuracy-latency trade-offs. Distinct from prior surveys, we (a) unify the four layers under a co-design and Pareto-frontier framework, (b) consolidate the evidence on multi-tenant KV cache security and side-channel leakage, and (c) analyse cache degradation in long-horizon agentic loops. To make this gap actionable, we propose Matched-Budget Evaluation (MBE), a lightweight reporting protocol and accompanying pilot harness for describing KV-cache results at fixed memory budgets. We present MBE as a standardization proposal, not a fully validated benchmark. It targets researchers and engineers combining KV cache optimisations under deployment constraints.

## 2. 大型语言模型推理树 具有阶段过渡保证的控制分支过程框架

> 英文原标题：OQTOPUS: Optimal Query-Time Optimization for Probabilistic Utility Search inLarge Language Model Reasoning Trees — A Controlled Branching ProcessFramework with Phase-Transition Guarantees

- **作者：** Soumyapriya Goswami、Raj Ganesh Jayaraman、Partha Sarathi Banerjee、Amruutha Chandrasekar Rao
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-16；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7292749) · [DOI](https://doi.org/10.2139/ssrn.7292749)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、large language models、compute allocation、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在大型语言模型 (LLM) 中,引进时间推理越来越多地通过基于树的探索中途推理轨迹实施.现有的推理框架通常通过经验调整来确定分支因子,搜索深度,光束宽度和停止政策,缺乏计算分配的原则性理论基础. 这篇论文介绍了OQTOPUS (Optimal Query-Time Optimization for Probabilistic Utility Search),一个基于操作研究的框架, 通过将GaltonWatson分支流程嵌入决策框架中,我们得出一个明显的阶段过渡,其特征是有效分支指数R= bpv,其中b表示分支因子,p是 产生有用推理延续的可能性,v表示验证准确性. 这项分析确定了达到预期的推理成功概率所需的最低计算预算的封闭形式限制,并严格地描述了超越关键计算门的降低回报率. 此外,我们还推出了适应性分支政策,以及一个最佳的停止策略,共同最大限度地提高预期的推理效益,同时最大限度地降低计算支出.超过10,000条推理轨迹的广泛模拟研究验证了理论分析,证明了理论和实验性性能之间的良好一致性. 结果进一步表明,多种最先进的推理系统分配了比理论最佳要求要多的推断计算,这表明了基于原则的计算效率推理的重要机会.

### 英文原摘要

Inference-time reasoning in Large Language Models (LLMs) is increasingly implemented through tree-based exploration of in-termediate reasoning trajectories. Existing reasoning frameworks typically determine branching factor, search depth, beam width,and stopping policies through empirical tuning, lacking a principled theoretical foundation for compute allocation. This paper intro-duces OQTOPUS (Optimal Query-Time Optimization for Probabilistic Utility Search), an operations-research-inspired frameworkthat formulates inference-time reasoning as a finite-horizon Markov Decision Process (MDP). The proposed Controlled BranchingProcess with Absorbing Reward States (CBPARS) models each reasoning state using search depth, branching width, confidencescore, verifier reliability, and remaining computational budget.By embedding a Galton–Watson branching process into the decision framework, we derive a sharp phase-transition characterizedby the effective reasoning indexR= bpv,where b denotes branching factor, p is the probability of generating a useful reasoning continuation, and v represents verifieraccuracy. The analysis establishes closed-form bounds on the minimum computational budget required to attain a desired reasoningsuccess probability and rigorously characterizes diminishing returns beyond the critical compute threshold. Furthermore, we derivean adaptive branching policy together with an optimal stopping strategy that jointly maximize expected reasoning utility whileminimizing computational expenditure.Extensive simulation studies over 10,000 reasoning trajectories validate the theoretical analysis, demonstrating excellent agree-ment between theory and empirical performance. The results further indicate that several state-of-the-art reasoning systems allocatesubstantially more inference compute than required by the theoretical optimum, suggesting significant opportunities for principledcompute-efficient reasoning.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
