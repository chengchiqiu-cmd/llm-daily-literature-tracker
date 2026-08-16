# 2026-08-16 LLM 服务系统每日文献简报

> 检索窗口：2026-08-15 至 2026-08-16（北京时间 / Asia/Shanghai）；本期确认 7 篇，其中直接 LLM 服务研究 7 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. OpenAI API compatible AI Inference Service support in HPC environment

> 英文原标题：OpenAI API compatible AI Inference Service support in HPC environment

- **作者：** Adam Matuš、Tomáš Martinovič、Arif Görkem Özer、Jakub Konvička、Firat Cekinel、Pinar Karagoz、Ismail Hakki Toroslu、Jakub Krejčí 等
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 12
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7287387) · [DOI](https://doi.org/10.2139/ssrn.7287387)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、ai inference service、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在人工智能(AI)和大语言模型(LLMs)崛起的推动下,对高密度GPU资源的需求大幅上升。 高性能计算机(HPC)中心拥有必要的硬件,但它们的传统基础设施和软件生态系统使得托管方便用户的AI服务高度复杂。 本文介绍了专门为高电荷环境设计的创新性推论服务。 通过整合批量排期、战略项目预分配和高端应用环境(HEAppE)中间软件,该服务为LLMS展示了无缝的、云状的应用编程界面(API),该界面也可以用于更广泛的AI推论任务,包括代理AI。 为了支持普通的基因化使用案例,如文本到文字或图像到文字的任务,这项服务的设计完全符合行业标准OpenAI API。我们使用标准基准来评估这一解决方案的性能,以证明其最小的管弦管理。这项服务是在欧洲地平线项目EXA4MIND的范围内开发的。

### 英文原摘要

Driven by the rise of Artificial Intelligence (AI) and Large Language Models (LLMs), the demand for high-density GPU resources has escalated significantly. High-Performance Computing (HPC) centers possess the necessary hardware, yet their conventional infrastructure and software ecosystems make hosting user-friendly AI services highly complex. This paper presents an innovative inference service designed specifically for HPC environments. By integrating batch scheduling, strategic project pre-allocations, and the High-End Application Environment (HEAppE) middleware, the service exposes a seamless, cloud-like Application Programming Interface (API) for LLMs, which can also be extended for broader AI inference tasks including agentic AI. To support common generative use-cases, such as text-to-text or image-to-text tasks, the service is designed to be fully compatible with the industry-standard OpenAI API. We evaluate the performance of this solution using standardized benchmarks against a bare-metal baseline to demonstrate its minimal orchestration overhead. This service has been developed within the scope of the Horizon Europe project EXA4MIND.

## 2. Breaking the Memory Wall: A Survey of Key-Value (KV) Cache Compression for Efficient Large Language Model (LLM) Inference

> 英文原标题：Breaking the Memory Wall: A Survey of Key-Value (KV) Cache Compression for Efficient Large Language Model (LLM) Inference

- **作者：** Manpreet Singh、Yash Jajoo、Rohith Reddy Bellibatlu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-16；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 11
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7273098) · [DOI](https://doi.org/10.2139/ssrn.7273098)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、kv cache。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型(LLMs)在长的上下文长度上的部署越来越受内存的限制,而不是计算。 在自动递减解码过程中,键值缓存存储了经过处理的符号的键和值激活,随着序列长度和批量大小的线性增长,并且常常必须流出每个生成的符号。 在长通和高通量的设置中,这可以解码内存带宽和暴露内存墙。 本次调查提供了一种统一的硬件意识处理方法,可以减轻这种瓶颈。 我们通过屋顶线模型和VRAM脚印分析将其正规化,将计算中的预填与内存解码区分开来,然后将文献组织成四个互补的层次:算法压缩(量化、驱逐和垃圾化,以及象征性、低级别或学习合并);建筑重新设计(多查询和分组清理关注,低级别潜伏关注,以及经常性或混合性) (c) 硬件加速(解码内核、聚变和模拟处理)。 对于每一个国家,我们给出了管理机制、可实现的内存减少和准确度利差权衡。 与以往的调查不同,我们(a) 将四个层次统一到共同设计框架和Pareto前沿框架之下,(b) 合并关于多租户KV缓存安全和侧道渗漏的证据,(c) 分析长方位介质循环中的缓存降解。 为使这一差距可以操作,我们建议采用匹配预算评估(MBE),即轻量级报告程序,并同时在固定内存预算中对KV缓冲结果进行描述。我们把MBE作为一种标准化建议,而不是一个完全有效的基准。它针对的是将KV缓存优化结合起来的研究人员和工程师。

### 英文原摘要

The deployment of large language models (LLMs) at long context lengths is increasingly limited by memory rather than compute. During autoregressive decoding, the key-value (KV) cache stores the key and value activations of processed tokens, grows linearly with sequence length and batch size, and must often be streamed for each generated token. In long-context and high-throughput settings, this makes decoding memory-bandwidthbound and exposes the memory wall. This survey gives a unified, hardware-aware treatment of techniques that mitigate this bottleneck. We formalise it through the roofline model and a VRAM-footprint analysis separating compute-bound prefill from memorybound decoding, then organise the literature into four complementary layers: algorithmic compression (quantization, eviction and sparsification, and token, low-rank, or learned merging); architectural redesign (multi-query and grouped-query attention, low-rank latent attention, and recurrent or hybrid state-space models); system-level management (paged memory, prefix sharing, cross-request transport, and tiered offloading); and hardware acceleration (decoding kernels, fusion, and processing-in-memory). For each we give the governing mechanism, achievable memory reduction, and accuracy-latency trade-offs. Distinct from prior surveys, we (a) unify the four layers under a co-design and Pareto-frontier framework, (b) consolidate the evidence on multi-tenant KV cache security and side-channel leakage, and (c) analyse cache degradation in long-horizon agentic loops. To make this gap actionable, we propose Matched-Budget Evaluation (MBE), a lightweight reporting protocol and accompanying pilot harness for describing KV-cache results at fixed memory budgets. We present MBE as a standardization proposal, not a fully validated benchmark. It targets researchers and engineers combining KV cache optimisations under deployment constraints.

## 3. JaccardServe: Cross-Request Prefill Acceleration in LLM Serving via MinHash-LSH Token Shingling

> 英文原标题：JaccardServe: Cross-Request Prefill Acceleration in LLM Serving via MinHash-LSH Token Shingling

- **作者：** Anmol Sureshkumar Panchal
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7290195) · [DOI](https://doi.org/10.2139/ssrn.7290195)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在请求中重用计算出的关键值缓存是服务大型语言模型(LLMs)的一个非常有效的优化,但字段分为三个主要方法:准确的区块级前缀缓存(VLLM APC)、精确的符号级前缀缓存(SGLang RadixAttention)和符号嵌入(SemShareKV)上大致相似的余弦缓存。 每种方法都捕捉不同类型的交叉请求冗余, 却缺少其它方法 。 精确的前缀缓存无法用用户专用的替换处理模板提示 ; SemShareKV 在匹配前需要配对比较和 GPU 级嵌入计算 。 没有具体述及许多同时提出的请求都具有大、几乎相同的象征性序列的情况,仅因细小的词汇变化而不同——在模板式聊天中的一种常见模式,检索和增强的生成(RAG)与通过重排顺序和多试剂框架。 本文介绍JacardServe, 这是一个交叉请求的预填加速层, 使用 MinHash-LSH 近乎重复的检测符号闪烁。 根据Broder-Charikar MinHash带宽技术,在标准CPU的API网关上操作匹配程序,该方法通过封闭式S曲线公式P(collision;s,b,r)=1(1-sr)b提供可加金枪鱼精确召回的交换。 这种办法将提交人先前的MinHash-LSH带宽用于近似重复的检测文件[Panchal, 2018年]的范围扩大至在线推断,并附有象征性的细节。 在500个即时模板-聊天基准中,准确的区块级前缀缓冲达到5.2%的交叉请求匹配率,而平衡环境下的JacardServe(b=20,r=4,0.5)达到97.4%的匹配率,在网关上,每个请求只有0.28米的管理费,改进了18.7倍。 根据320-即时多文档汇总基准,VLLM APC的点击率为19.7%,SemShareKV模拟器为5.9%,JaccardServe平衡为70.9%。 与甲骨文地面真理相比,高调JaccarServe的精确度为0.905,回溯0.806(F1=0.853),优于VLLM APC的0.324和SemShareKV的0.120。 该文件遵循了作者先前的审查和扩展框架[2018年,Panchal],调查了三种现有的交叉请求再利用技术,概述了其局限性,并将JaccardServe作为补充解决方案。 所有相关代码、基准和数字都可以在一个可复制的CPU存储库中找到。 关键词:AI、LLM、模型压缩、Token Deduction、LLM推理、KV缓存、前缀缓存、MinHash、对地点敏感的散列、积分相似性以及服务系统。

### 英文原摘要

Reusing computed key-value (KV) caches across requests is a highly effective optimization in serving large language models (LLMs), but the field has split into three main approaches: exact block-level prefix caching (vLLM APC), exact token-level prefix caching (SGLang RadixAttention), and approximate cosine-similarity caching on token embeddings (SemShareKV). Each method captures different types of cross-request redundancy while missing others. Exact prefix caches fail to handle templated prompts with user-specific substitutions; SemShareKV requires pairwise comparisons and GPU-level embedding computations before matching. None specifically address scenarios where many simultaneous requests share large, nearly identical token sequences differing only by minor lexical changes—a common pattern in templated chat, retrieval-augmented generation (RAG) with passage reordering, and multi-agent frameworks. This paper introduces JaccardServe, a cross-request prefill acceleration layer that uses MinHash-LSH near-duplicate detection on token shingles. The matching process operates at the API gateway on standard CPUs before any model inference, based on the Broder–Charikar MinHash banding technique, which provides a tunable precision-recall trade-off via the closed-form S-curve formula 𝑃(collision; 𝑠, 𝑏, 𝑟) = 1 − (1 − 𝑠^𝑟)^𝑏. This approach extends the author's previous MinHash–LSH banding implementation for document near-duplicate detection [Panchal, 2018] to online inference with token-level detail. In a 500-prompt templated-chat benchmark, exact block-level prefix caching achieves a 5.2% cross-request match rate, while JaccardServe at a balanced setting (b=20, r=4, 𝜏=0.5) reaches a 97.4% match rate with only 0.28 ms overhead per request at the gateway—an 18.7-fold improvement. On a 320-prompt multi-document summarization benchmark, hit rates are 19.7% for vLLM APC, 5.9% for a SemShareKV simulator, and 70.9% for JaccardServe balanced. Compared to an oracle ground truth, JaccardServe in high-recall mode achieves precision of 0.905 and recall of 0.806 (F1 = 0.853), outperforming vLLM APC’s 0.324 and SemShareKV’s 0.120. The paper follows the author’s previous review-and-extend framework [Panchal, 2018], surveying three existing cross-request reuse techniques, outlining their limitations, and presenting JaccardServe as a complementary solution. All related code, benchmarks, and figures are available in a single CPU-reproducible repository. Keywords: AI, LLM, Model Compression, Token Deduplication, LLM inference, KV cache, prefix caching, MinHash, locality-sensitive hashing, Jaccard similarity, and serving systems.​

## 4. Adaptive Weather-Aware Home Energy Management through Large Language Model-Based Appliance Scheduling

> 英文原标题：Adaptive Weather-Aware Home Energy Management through Large Language Model-Based Appliance Scheduling

- **作者：** sokipriala jonah、Queen Moses、Abiola Babatunde、Michael Ajao-Olarinoye、Daniel Bammeke
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7289632) · [DOI](https://doi.org/10.2139/ssrn.7289632)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、tariff。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

住宅的灵活性可以降低电力成本,增加当地光电的利用,并支持需求方的运作,但传统的家庭能源管理系统往往要求用户将日常偏好转化为技术限制。 本文介绍了一个适应性强的、对天气有了解的能源管理代理机构,该代理机构将自然语言要求转化为多种灵活家庭负担的协调时间表。 据我们所知,这是第一个在统一的净成本目标范围内,利用动态零售价格、天气产生的光电池预报、家庭需求、自消费、出口收入、日历期限和家庭权力限度,联合优化基于LLM的软件计划。 孤独和天气制度、预测不确定性、制约冲突和七天滚动部署。 结果表明,在动态费率下,有可靠的多功能协调以及接近最佳的运营成本。 严格的冲突测试显示,在最后期限、电力上限、不规则时间表和不可行的要求下,模型出现故障,这表明仅靠经济表现不足以评价自主能源控制者。 天气意识列表通过协调灵活需求与预测的生成,提供了依赖制度的成本和光电池自消费的好处。 在整个七天的评估中,代理商获取了超峰定时器和优化预告器之间可用储蓄的96.7-98.0%,同时超过了即时启动和贪婪的政策。 研究结果显示了基于LLM的住宅能源控制的潜力,同时强调了在物理激活之前需要有一个独立的确定性可行性层。

### 英文原摘要

Residential flexibility can reduce electricity costs, increase local photovoltaic (PV) utilisation, and support demand-side operation, but conventional Home Energy Management Systems often require users to translate everyday preferences into technical constraints. This paper presents an adaptive, weather-aware energy-management agent that converts natural-language requirements into coordinated schedules for multiple flexible household loads. To our knowledge, it is the first autonomous LLM-based HEMS to jointly optimise appliance schedules using dynamic retail prices, weather-derived PV forecasts, household demand, self-consumption, export revenue, calendar deadlines, and household power limits within a unified net-cost objective.Five language-model controllers are evaluated against an extended mixed-integer linear programming oracle across tariff-volatility and weather regimes, forecast uncertainty, constraint conflicts, and a seven-day rolling deployment. Results show reliable multi-appliance coordination and near-optimal operating cost under dynamic tariffs. Constraint-conflict testing reveals model-specific failures under deadlines, power caps, irregular schedules, and infeasible requests, demonstrating that economic performance alone is insufficient for evaluating autonomous energy controllers.Weather-aware scheduling provides regime-dependent cost and PV self-consumption benefits by coordinating flexible demand with forecast generation. Across the seven-day evaluation, the agents capture 96.7–98.0% of the savings available between an off-peak timer and the optimisation oracle, while outperforming immediate-start and greedy policies. The findings demonstrate the potential of LLM-based residential energy control while highlighting the need for an independent deterministic feasibility layer before physical actuation.

## 5. OQTOPUS: Optimal Query-Time Optimization for Probabilistic Utility Search inLarge Language Model Reasoning Trees — A Controlled Branching ProcessFramework with Phase-Transition Guarantees

> 英文原标题：OQTOPUS: Optimal Query-Time Optimization for Probabilistic Utility Search inLarge Language Model Reasoning Trees — A Controlled Branching ProcessFramework with Phase-Transition Guarantees

- **作者：** Soumyapriya Goswami、Raj Ganesh Jayaraman、Partha Sarathi Banerjee、Amruutha Chandrasekar Rao
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-16；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7292749) · [DOI](https://doi.org/10.2139/ssrn.7292749)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、large language models、compute allocation、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大语言模型(LLMs)的推理过程越来越多地通过基于树的模拟推理轨迹探索来进行。 现有的推理框架通常决定分支因素、搜索深度、梁宽度以及通过经验调整来阻止政策,缺乏计算分配的原则性理论基础。 本文介绍 " 概率实用性搜索最佳查询-时间优化 " ,这是一个由操作-研究驱动的框架,它将推论-时间推理作为有限焦距马尔科夫的决策过程(MDP)。 与吸收奖励国(CBPARS)的拟议控制分流处理模型,每种推理都使用搜索深度、分流宽度、信任度、核实可靠性和剩余计算预算进行说明。 通过将Galton-Watson分流过程嵌入决定框架,我们得出了一个以有效推理指数=bpv为特征的尖锐的阶段过渡,其中b表示分流系数,p是 产生有用的推理继续的可能性,v 代表核实准确性。 分析确定了达到预期成功概率所需的最低计算预算的封闭式界限,并严格界定了低于关键计算阈值的收益递减的特点。 此外,我们得出了适应性的分支政策以及最佳停止战略,在最小化计算支出的同时,共同最大限度地发挥预期的推理效用。 广泛的模拟研究超过1万个推理轨迹证实了理论分析,表明理论与实证业绩之间极佳的一致。 结果进一步表明,一些最先进的推理系统分配的推理数量比理论最佳性所要求的要多,表明有原则地计算有效推理的机会很大。

### 英文原摘要

Inference-time reasoning in Large Language Models (LLMs) is increasingly implemented through tree-based exploration of in-termediate reasoning trajectories. Existing reasoning frameworks typically determine branching factor, search depth, beam width,and stopping policies through empirical tuning, lacking a principled theoretical foundation for compute allocation. This paper intro-duces OQTOPUS (Optimal Query-Time Optimization for Probabilistic Utility Search), an operations-research-inspired frameworkthat formulates inference-time reasoning as a finite-horizon Markov Decision Process (MDP). The proposed Controlled BranchingProcess with Absorbing Reward States (CBPARS) models each reasoning state using search depth, branching width, confidencescore, verifier reliability, and remaining computational budget.By embedding a Galton–Watson branching process into the decision framework, we derive a sharp phase-transition characterizedby the effective reasoning indexR= bpv,where b denotes branching factor, p is the probability of generating a useful reasoning continuation, and v represents verifieraccuracy. The analysis establishes closed-form bounds on the minimum computational budget required to attain a desired reasoningsuccess probability and rigorously characterizes diminishing returns beyond the critical compute threshold. Furthermore, we derivean adaptive branching policy together with an optimal stopping strategy that jointly maximize expected reasoning utility whileminimizing computational expenditure.Extensive simulation studies over 10,000 reasoning trajectories validate the theoretical analysis, demonstrating excellent agree-ment between theory and empirical performance. The results further indicate that several state-of-the-art reasoning systems allocatesubstantially more inference compute than required by the theoretical optimum, suggesting significant opportunities for principledcompute-efficient reasoning.

## 6. Backfilling, Not Prediction: A Cluster-Size Sweep and Cross-Trace Bootstrap of Forecast-Driven GPU Scheduling in the LLM Era

> 英文原标题：Backfilling, Not Prediction: A Cluster-Size Sweep and Cross-Trace Bootstrap of Forecast-Driven GPU Scheduling in the LLM Era

- **作者：** Don Harl C. Malabanan
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7291636) · [DOI](https://doi.org/10.2139/ssrn.7291636)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 llm、scheduling、gpu cluster。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

先前的工作索赔要求预测工作期限和预测的时间安排会减少生产GPU集群的平均工作完成时间(Hu等人,2021年;Luo等人,2025年),这项索赔要求尽管只对2022年之前的痕量或私人测试台进行了验证,但还是形成了LLM-era GPU集群的排程设计。 本文用它尚未收到的统计严谨度来检验这一说法:一个19点的集束尺寸的扫瞄、一个300个重复工作级的靴子和另一个独立追踪的跨轨靴子。 我们使用Alibaba的2023 GPU集发布和所有四个太阳系追踪组,通过追踪驱动的离散活动模拟,比较了六种排期政策、严格的FIFO、FIFO与回填、两个预测的最短时间变体、Hilbert-曲线定位基线和拟议的Predshed-LLM。 其结果是颠倒了它用来测试的前提:在两种痕迹上,FIFO的平均JCT在争议中崩溃,在Alibaba甚至仍然在Helitos上更严重达9倍,但负责的机制是回填,而不是预测,而且发现在所测试的所有5个组群中都完全复制(95%的CI在所有部分中排除零)。 这两种痕迹对预测知情的订单在回填上增加了哪些内容有分歧:阿里巴巴没有明显的优势,但在赫利奥斯上有一个真正的定向信号(90%-100%的靴子都复制了它 ) 。 拟议的碎片识别定位限制并不能清除回填的痕迹。 后填是一个大效果,在所测试的每个组群中复制;预测的价值真正取决于追踪,而不是完全不存在。

### 英文原摘要

Prior work claims that predicting job duration and scheduling on that prediction reduces average job completion time (JCT) on production GPU clusters (Hu et al., 2021; Luo et al., 2025), a claim that has shaped scheduler design for LLM-era GPU clusters despite being validated only on pre-2022 traces or private testbeds. This paper tests that claim with the statistical rigor it has not yet received: a 19-point cluster-size sweep, a 300-replicate job-level bootstrap, and a separate cross-trace bootstrap on a second, independent trace. Using Alibaba's 2023 GPU cluster release and all four clusters of the Helios trace, we compare six scheduling policies, strict FIFO, FIFO-with-backfilling, two predicted-shortest-remaining-time variants, a Hilbert-curve placement baseline, and the proposed PredSched-LLM, via trace-driven discrete-event simulation. The result inverts the premise it set out to test: on both traces, strict FIFO's average JCT collapses under contention, up to ninefold worse on Alibaba and further still on Helios, but the mechanism responsible is backfilling, not prediction, and that finding replicates cleanly across all five clusters tested (95 percent CI excludes zero everywhere). The two traces disagree on what prediction-informed ordering adds on top of backfilling: no distinguishable advantage on Alibaba, but a real directional signal on Helios (90-100 percent of bootstrap replicates favor it). The proposed fragmentation-aware placement constraint does not clear backfilling's bar on either trace. Backfilling is the one effect that is large and reproduces across every cluster tested; prediction's value is genuinely trace-dependent, not simply absent.

## 7. Economic Integrity in Production LLM Pipelines: Measuring Attempt Amplification, Discarded Reasoning, and Retry Cost

> 英文原标题：Economic Integrity in Production LLM Pipelines: Measuring Attempt Amplification, Discarded Reasoning, and Retry Cost

- **作者：** Sean Halverson
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-15；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7270819) · [DOI](https://doi.org/10.2139/ssrn.7270819)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 llm、pricing、provider。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

模型定价页每面标注成本。 生产管道每面都支付一次。 当管道重试时,当其验证层重新质疑失败的角色时,当推理模型认为它们从未发放产出的标牌时,发票就会与记分牌脱钩。 在一项配套的可靠性研究中,我们将这一脱钩报告为仪器空白:尝试没有仪器,因此尝试的分母是不存在的,饥饿只能从运行的原木中计算出来。本文缩小了这一空白。 在HTTP边界,我们增加一个生产分析管道的人均经济分类账,每个实物模型呼叫记录一份记录,携带标语计数,包括推理和即时剖析、预算、杠杆状态、层、结果和潜伏,并用分类账重新处理一个四个细胞的预算/复制(每细胞10个重复,一个供应商,一个晚上)。 我们在分类账上定义了两个衡量标准:推论放大系数(IAF),每个逻辑工作的实际尝试,以及经济污染指数(ECI),总开支用于实际使用产出的尝试。 所有四个细胞都相当于计分板,回答键为46.8至47.4,48次检查,10次执行-清洁或回收-清洁重复,9至10次;下面,尝试机器相差高达1.7倍。 预防性预算总措施:在127个代理工作方面,第一次尝试绝食,如果重新尝试残疾,无法隐藏,则在两个康复圈子(IAF=1 000,通过直接查点)都没有放大作用。 重试回收达到与IAF的等值记分牌,最高为1.70,在对抗性验证层达到ECI的等值记分板:在最差的细胞中,48.9%的该层支出购买了产出被丢弃的尝试,在研究中228 890个废弃产出标牌中,228 889个是推理符号,没有记分板看到的支出类别。 救援效果也是非固定性的:在20个饥饿工作岗位中,有19个预算重现了一夜,有5个16个晚上恢复了同样的配置,因此,基于再尝试的成本预测继承了不稳定性,而基于预防的预测却并非如此。在整个研究中,9.6%的分类账计算支出了被抛弃的尝试。重修答案。它并没有抹去第一张发票。

### 英文原摘要

Model pricing pages quote cost per token. Production pipelines pay per attempt. When a pipeline retries empty replies, when its validation layers re-ask failed roles, and when reasoning models bill thinking tokens for outputs they never emit, the invoice decouples from the scoreboard. In a companion reliability study we reported this decoupling as an instrumentation gap: attempts were not instrumented, so attempt denominators were unavailable and starvation could only be counted from run logs. This paper closes that gap. We add a per-attempt economic ledger at the HTTP boundary of a production analysis pipeline, one record per physical model call, carrying token counts including reasoning and prompt-cache splits, budgets, lever state, layer, outcome, and latency, and re-run a four-cell budget/retry ablation (n=10 repetitions per cell, one provider, one night) with the ledger armed. We define two metrics over the ledger: the Inference Amplification Factor (IAF), physical attempts per logical job, and the Economic Contamination Index (ECI), total spend over spend on attempts whose output was actually used. All four cells were scoreboard-equivalent, with answer-key means of 46.8 to 47.4 of 48 checks and 9 to 10 of 10 execution-clean or recovered-clean repetitions; underneath, the attempt machinery differed by up to a factor of 1.7. Proactive budget headroom measures as prevention: one starved first attempt in 127 agent-layer jobs, and, with the retry disabled so no recovery could hide it, no amplification at either recovery ring (IAF = 1.000 by direct enumeration). Retry-based recovery reaches an equivalent scoreboard with IAF up to 1.70 and ECI up to 1.96 in the adversarial validation layer: in the worst cell, 48.9% of that layer's spend bought attempts whose output was discarded, and 228,889 of 228,890 discarded output tokens in the study were reasoning tokens, the spend category no scoreboard sees. Rescue effectiveness was also non-stationary: a same-budget re-ask recovered roughly 19 of 20 starved jobs one night and 5 of 16 two nights later under an identical configuration, so retry-based cost forecasts inherit a volatility that prevention-based forecasts do not. Across the study, 9.6% of ledger-computed spend bought discarded attempts. A retry repairs the answer. It does not erase the first invoice.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
