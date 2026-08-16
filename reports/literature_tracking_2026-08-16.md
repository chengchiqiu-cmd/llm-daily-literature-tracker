# 2026-08-16 LLM 服务系统每日文献简报

> 检索窗口：2026-08-15 至 2026-08-16（北京时间 / Asia/Shanghai）；本期确认 7 篇，其中直接 LLM 服务研究 7 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 在HPC环境中支持OpenAI API兼容的AI推理服务

> 英文原标题：OpenAI API compatible AI Inference Service support in HPC environment

- **作者：** Adam Matuš、Tomáš Martinovič、Arif Görkem Özer、Jakub Konvička、Firat Cekinel、Pinar Karagoz、Ismail Hakki Toroslu、Jakub Krejčí 等
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 12
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7287387) · [DOI](https://doi.org/10.2139/ssrn.7287387)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、ai inference service、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

由于人工智能 (AI) 和大型语言模型 (LLM) 的兴起,高密度GPU资源的需求大幅增加.高性能计算 (HPC) 中心拥有必要的硬件,但它们的传统基础设施和软件生态系统使得用户友好的人工智能服务的托管非常复杂. 本文介绍了专门为HPC环境设计的创新推理服务.通过集成批量安排,战略项目预分配和高端应用环境 (HEAppE) 中文软件,该服务揭示了LLM的无,类似云的应用程序编程界面 (API),也可以扩展到更广泛的AI推理任务,包括代理AI. 为了支持常见的生成性使用情况,如文本到文本或图像到文本任务,该服务旨在完全兼容行业标准的OpenAI API.我们通过使用标准化基准来评估该解决方案的性能,以证明其最小的调整总费用.该服务是在欧洲视野项目EXA4MIND的范围内开发的.

### 英文原摘要

Driven by the rise of Artificial Intelligence (AI) and Large Language Models (LLMs), the demand for high-density GPU resources has escalated significantly. High-Performance Computing (HPC) centers possess the necessary hardware, yet their conventional infrastructure and software ecosystems make hosting user-friendly AI services highly complex. This paper presents an innovative inference service designed specifically for HPC environments. By integrating batch scheduling, strategic project pre-allocations, and the High-End Application Environment (HEAppE) middleware, the service exposes a seamless, cloud-like Application Programming Interface (API) for LLMs, which can also be extended for broader AI inference tasks including agentic AI. To support common generative use-cases, such as text-to-text or image-to-text tasks, the service is designed to be fully compatible with the industry-standard OpenAI API. We evaluate the performance of this solution using standardized benchmarks against a bare-metal baseline to demonstrate its minimal orchestration overhead. This service has been developed within the scope of the Horizon Europe project EXA4MIND.

## 2. 打破记忆墙:对高效的大语言模型 (LLM) 输入的关键值 (KV) 缓存压缩的调查

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

## 3. JaccardServe:通过MINHash-LSH代币屏幕服务在LLM服务中跨请求预填加快

> 英文原标题：JaccardServe: Cross-Request Prefill Acceleration in LLM Serving via MinHash-LSH Token Shingling

- **作者：** Anmol Sureshkumar Panchal
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7290195) · [DOI](https://doi.org/10.2139/ssrn.7290195)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在请求中重复使用计算关键值 (KV) 缓存是服务大型语言模型 (LLM) 的高效优化,但该领域分为三个主要方法:精确的区块级预写缓存 (vLLM APC),精确的代币级预写缓存 (SGLang RadixAttention) 和对代币嵌入式 (SemShareKV) 进行近似的共数类似性缓存. 每种方法都捕获了不同类型的交叉请求冗余性,同时缺失了其他类型.精确的预写缓存无法处理使用者特定的替换的模板提示;SemShareKV需要对对比和GPU级嵌入计算才能匹配. 没有一个具体解决了许多同时请求共享大型,几乎相同的代币序列的场景,只有微小的词汇变化而不同. 模板聊天,检索增强生成 (RAG) 与通过重新排序和多代理框架中的共同模式. 这篇论文介绍了JaccardServe,一个交叉要求预填加速度层, 匹配过程在任何模型推断之前在标准CPU上运行在API门口,基于BroderCharikar MinHash频段技术,通过闭式S曲线公式P(碰撞;s,b,r) =1 − (1 − s^r)^b提供可调节的精确回忆交易. 这种方法扩大了作者之前的MinHashLSH频段实现,用于近重复检测文档 [Panchal, 2018]到在线推断,具有代币级别的细节. 在500个即时模板聊天基准中,精确的区块级预写缓存实现了5.2%的交叉请求匹配率,而JaccardServe在平衡的设置 (b=20,r=4, τ=0.5) 达到97.4%的匹配率,每次请求仅为0.28ms. 在 320 个即时多文档总结基准上,VLLM APC 的击中率为 19.7%,SemShareKV 模拟器 5.9% 和JaccardServe 的平衡率为 70.9%.与 Oracle 地点真相相比,JaccardServe 在高回忆模式中达到 0.905 的精度,回忆率为 0.806 (F1 = 0.853),超过vLLM APC 0.324 和 SemShareKV 0.120. 该论文遵循作者之前的审查和扩展框架[Panchal, 2018],调查了三个现有的交叉请求重复使用技术,概述了它们的局限性,并将JaccardServe作为补充解决方案.所有相关代码,基准和数字都可在一个可复制的CPU存储库中使用. 关键词:AI,LLM,模型压缩,代币减倍,LLM推理,KV缓存,前缓存,MinHash,本地敏感的哈希,Jaccard相似性和服务系统.

### 英文原摘要

Reusing computed key-value (KV) caches across requests is a highly effective optimization in serving large language models (LLMs), but the field has split into three main approaches: exact block-level prefix caching (vLLM APC), exact token-level prefix caching (SGLang RadixAttention), and approximate cosine-similarity caching on token embeddings (SemShareKV). Each method captures different types of cross-request redundancy while missing others. Exact prefix caches fail to handle templated prompts with user-specific substitutions; SemShareKV requires pairwise comparisons and GPU-level embedding computations before matching. None specifically address scenarios where many simultaneous requests share large, nearly identical token sequences differing only by minor lexical changes—a common pattern in templated chat, retrieval-augmented generation (RAG) with passage reordering, and multi-agent frameworks. This paper introduces JaccardServe, a cross-request prefill acceleration layer that uses MinHash-LSH near-duplicate detection on token shingles. The matching process operates at the API gateway on standard CPUs before any model inference, based on the Broder–Charikar MinHash banding technique, which provides a tunable precision-recall trade-off via the closed-form S-curve formula 𝑃(collision; 𝑠, 𝑏, 𝑟) = 1 − (1 − 𝑠^𝑟)^𝑏. This approach extends the author's previous MinHash–LSH banding implementation for document near-duplicate detection [Panchal, 2018] to online inference with token-level detail. In a 500-prompt templated-chat benchmark, exact block-level prefix caching achieves a 5.2% cross-request match rate, while JaccardServe at a balanced setting (b=20, r=4, 𝜏=0.5) reaches a 97.4% match rate with only 0.28 ms overhead per request at the gateway—an 18.7-fold improvement. On a 320-prompt multi-document summarization benchmark, hit rates are 19.7% for vLLM APC, 5.9% for a SemShareKV simulator, and 70.9% for JaccardServe balanced. Compared to an oracle ground truth, JaccardServe in high-recall mode achieves precision of 0.905 and recall of 0.806 (F1 = 0.853), outperforming vLLM APC’s 0.324 and SemShareKV’s 0.120. The paper follows the author’s previous review-and-extend framework [Panchal, 2018], surveying three existing cross-request reuse techniques, outlining their limitations, and presenting JaccardServe as a complementary solution. All related code, benchmarks, and figures are available in a single CPU-reproducible repository. Keywords: AI, LLM, Model Compression, Token Deduplication, LLM inference, KV cache, prefix caching, MinHash, locality-sensitive hashing, Jaccard similarity, and serving systems.​

## 4. 通过基于大型语言模型的设备规划来适应天气的家庭能源管理

> 英文原标题：Adaptive Weather-Aware Home Energy Management through Large Language Model-Based Appliance Scheduling

- **作者：** sokipriala jonah、Queen Moses、Abiola Babatunde、Michael Ajao-Olarinoye、Daniel Bammeke
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7289632) · [DOI](https://doi.org/10.2139/ssrn.7289632)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、tariff。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

住宅灵活性可以降低电力成本,增加当地光伏 (PV) 利用率,支持需求侧操作,但传统的家庭能源管理系统通常要求用户将日常偏好转化为技术约束. 本文介绍了一个适应性,有意识到天气的能源管理代理,将自然语言要求转化为多个灵活家庭负载的协调日程. 据我们所知,这是第一个基于LLM的自主HEMS,通过使用动态零售价格,天气衍生的光伏预测,家庭需求,自消费,出口收入,日历截止日期和家庭电力限制,在统一的净成本目标内共同优化设备时间表. 预测不确定性,约束冲突,以及7天的滚动部署. 结果显示,在动态关税下可靠的多设备协调和近乎最佳的运营成本. 压力冲突测试显示,在截止日期,电力限制,不规则的时间表和不可行的请求中,模型的故障表明,单独的经济表现不足以评估自主能源控制器. 意识到天气的规划,通过协调灵活的需求与预测生成,提供了依赖于政权的成本和光伏自消费的好处. 在7天的评估中,代理商在非峰值计时器和优化预言器之间获得了96.798.0%的节省,同时超过了即时启动和贪的政策.这些发现证明了基于LLM的住宅能源控制的潜力,同时强调在物理启动之前需要一个独立的确定性可行性层.

### 英文原摘要

Residential flexibility can reduce electricity costs, increase local photovoltaic (PV) utilisation, and support demand-side operation, but conventional Home Energy Management Systems often require users to translate everyday preferences into technical constraints. This paper presents an adaptive, weather-aware energy-management agent that converts natural-language requirements into coordinated schedules for multiple flexible household loads. To our knowledge, it is the first autonomous LLM-based HEMS to jointly optimise appliance schedules using dynamic retail prices, weather-derived PV forecasts, household demand, self-consumption, export revenue, calendar deadlines, and household power limits within a unified net-cost objective.Five language-model controllers are evaluated against an extended mixed-integer linear programming oracle across tariff-volatility and weather regimes, forecast uncertainty, constraint conflicts, and a seven-day rolling deployment. Results show reliable multi-appliance coordination and near-optimal operating cost under dynamic tariffs. Constraint-conflict testing reveals model-specific failures under deadlines, power caps, irregular schedules, and infeasible requests, demonstrating that economic performance alone is insufficient for evaluating autonomous energy controllers.Weather-aware scheduling provides regime-dependent cost and PV self-consumption benefits by coordinating flexible demand with forecast generation. Across the seven-day evaluation, the agents capture 96.7–98.0% of the savings available between an off-peak timer and the optimisation oracle, while outperforming immediate-start and greedy policies. The findings demonstrate the potential of LLM-based residential energy control while highlighting the need for an independent deterministic feasibility layer before physical actuation.

## 5. 大型语言模型推理树 具有阶段过渡保证的控制分支过程框架

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

## 6. 预测不是预测:在LLM时代的预测驱动GPU规划的集群尺寸扫描和交叉追踪启动

> 英文原标题：Backfilling, Not Prediction: A Cluster-Size Sweep and Cross-Trace Bootstrap of Forecast-Driven GPU Scheduling in the LLM Era

- **作者：** Don Harl C. Malabanan
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7291636) · [DOI](https://doi.org/10.2139/ssrn.7291636)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 llm、scheduling、gpu cluster。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

之前的工作声称,预测工作持续时间和按该预测安排减少了生产GPU集群中平均完成工作时间 (JCT) (Hu et al., 2021; Luo et al., 2025),这一声称仅在2022年之前的轨迹或私人测试床上得到验证,尽管它已经塑造了LLM时代GPU集群的规划设计. 这篇论文测试了它尚未获得的统计严格性:一个19点的集群大小扫描,一个300次的工作级别启动带, 使用阿里巴巴的2023年GPU集群发布和四个Helios追踪集群,我们通过追踪驱动的离散事件模拟来比较了六个规划政策,严格的FIFO,FIFO与后填充,两个预测的最短剩余时间变化,一个希尔伯特曲线定位基线和拟议的PredSched-LLM. 结果逆转了它试验设定的前提:在两条线上,FIFO的严格平均JCT在争议中崩,在阿里巴巴和更进一步的海利奥斯上甚至是9倍更糟, 两条线条不同意预测信息的订单在后填补上增加了什么:阿里巴巴没有明显的优势,但在黑利斯上有一个真正的方向信号 (90-100%的启动链复制品赞成它).拟议的碎片化意识定位限制不会在任何一个线条上清除后填补的条. 后填充是最大的效果,并且在每个测试的集群中复制;预测的价值是真正依赖于痕迹的,而不仅仅是不存在的.

### 英文原摘要

Prior work claims that predicting job duration and scheduling on that prediction reduces average job completion time (JCT) on production GPU clusters (Hu et al., 2021; Luo et al., 2025), a claim that has shaped scheduler design for LLM-era GPU clusters despite being validated only on pre-2022 traces or private testbeds. This paper tests that claim with the statistical rigor it has not yet received: a 19-point cluster-size sweep, a 300-replicate job-level bootstrap, and a separate cross-trace bootstrap on a second, independent trace. Using Alibaba's 2023 GPU cluster release and all four clusters of the Helios trace, we compare six scheduling policies, strict FIFO, FIFO-with-backfilling, two predicted-shortest-remaining-time variants, a Hilbert-curve placement baseline, and the proposed PredSched-LLM, via trace-driven discrete-event simulation. The result inverts the premise it set out to test: on both traces, strict FIFO's average JCT collapses under contention, up to ninefold worse on Alibaba and further still on Helios, but the mechanism responsible is backfilling, not prediction, and that finding replicates cleanly across all five clusters tested (95 percent CI excludes zero everywhere). The two traces disagree on what prediction-informed ordering adds on top of backfilling: no distinguishable advantage on Alibaba, but a real directional signal on Helios (90-100 percent of bootstrap replicates favor it). The proposed fragmentation-aware placement constraint does not clear backfilling's bar on either trace. Backfilling is the one effect that is large and reproduces across every cluster tested; prediction's value is genuinely trace-dependent, not simply absent.

## 7. 在生产LLM管道中的经济完整性:测量尝试扩大,丢弃推理和反试成本

> 英文原标题：Economic Integrity in Production LLM Pipelines: Measuring Attempt Amplification, Discarded Reasoning, and Retry Cost

- **作者：** Sean Halverson
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7270819) · [DOI](https://doi.org/10.2139/ssrn.7270819)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 llm、pricing、provider。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

模型定价页面引用每个代币的成本.生产管道每次付费.当一个管道重新尝试空答案时,当其验证层重新要求失败的角色时,当推理模型为他们从未发出的输出计算代币时,发票将脱离分数板. 在一个伴侣可靠性研究中,我们报告了这种分离为仪器差距:尝试没有仪器,所以尝试命名器无法使用,饥饿只能从运行日志中计算. 我们在生产分析管道的HTTP边界添加每次尝试的经济账本,每次实体模型调用一个记录,包括推理和快速缓存分区,预算,杆状态,层,结果和延迟, 我们在本书上定义了两个指标: 推理增强因素 (IAF), 每个逻辑工作的物理尝试, 所有四个细胞都相当于分数板,48次检查中的答案密钥平均值为46.8至47.4次,以及10次执行清洁或恢复清洁重复中9至10次;下面,试验机器差异高达1.7倍. 预防措施:在127个代理层工作中,第一次尝试失去了饥饿,再试被禁用,所以没有恢复可以隐藏它,在任何恢复圈都没有放大 (IAF=1000通过直接计算). 在对抗验证层中,基于复试的恢复达到相当的分数板,IAF高达1.70和ECI高达1.96:在最糟糕的细胞中,该层的48.9%的支出购买了被丢弃的尝试,而在研究中丢弃的228.890个输出代币中,有228.889个是推理代币, 拯救效率也非稳定:同一个预算的重复要求在同一配置下一晚恢复了大约19个20个饥饿失业的就业机会,并在两个晚上恢复了5个16个就业机会,因此基于重复试验的成本预测继承了基于预防的成本预测的波动性.在整个研究中,9.6%的账本计算支出购买了废弃的尝试.重复试验修复了答案.它不会删除第一个账单.

### 英文原摘要

Model pricing pages quote cost per token. Production pipelines pay per attempt. When a pipeline retries empty replies, when its validation layers re-ask failed roles, and when reasoning models bill thinking tokens for outputs they never emit, the invoice decouples from the scoreboard. In a companion reliability study we reported this decoupling as an instrumentation gap: attempts were not instrumented, so attempt denominators were unavailable and starvation could only be counted from run logs. This paper closes that gap. We add a per-attempt economic ledger at the HTTP boundary of a production analysis pipeline, one record per physical model call, carrying token counts including reasoning and prompt-cache splits, budgets, lever state, layer, outcome, and latency, and re-run a four-cell budget/retry ablation (n=10 repetitions per cell, one provider, one night) with the ledger armed. We define two metrics over the ledger: the Inference Amplification Factor (IAF), physical attempts per logical job, and the Economic Contamination Index (ECI), total spend over spend on attempts whose output was actually used. All four cells were scoreboard-equivalent, with answer-key means of 46.8 to 47.4 of 48 checks and 9 to 10 of 10 execution-clean or recovered-clean repetitions; underneath, the attempt machinery differed by up to a factor of 1.7. Proactive budget headroom measures as prevention: one starved first attempt in 127 agent-layer jobs, and, with the retry disabled so no recovery could hide it, no amplification at either recovery ring (IAF = 1.000 by direct enumeration). Retry-based recovery reaches an equivalent scoreboard with IAF up to 1.70 and ECI up to 1.96 in the adversarial validation layer: in the worst cell, 48.9% of that layer's spend bought attempts whose output was discarded, and 228,889 of 228,890 discarded output tokens in the study were reasoning tokens, the spend category no scoreboard sees. Rescue effectiveness was also non-stationary: a same-budget re-ask recovered roughly 19 of 20 starved jobs one night and 5 of 16 two nights later under an identical configuration, so retry-based cost forecasts inherit a volatility that prevention-based forecasts do not. Across the study, 9.6% of ledger-computed spend bought discarded attempts. A retry repairs the answer. It does not erase the first invoice.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
