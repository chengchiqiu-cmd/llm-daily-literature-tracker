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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

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

中文摘要翻译暂未生成，请参考下方英文原摘要。

### 英文原摘要

Model pricing pages quote cost per token. Production pipelines pay per attempt. When a pipeline retries empty replies, when its validation layers re-ask failed roles, and when reasoning models bill thinking tokens for outputs they never emit, the invoice decouples from the scoreboard. In a companion reliability study we reported this decoupling as an instrumentation gap: attempts were not instrumented, so attempt denominators were unavailable and starvation could only be counted from run logs. This paper closes that gap. We add a per-attempt economic ledger at the HTTP boundary of a production analysis pipeline, one record per physical model call, carrying token counts including reasoning and prompt-cache splits, budgets, lever state, layer, outcome, and latency, and re-run a four-cell budget/retry ablation (n=10 repetitions per cell, one provider, one night) with the ledger armed. We define two metrics over the ledger: the Inference Amplification Factor (IAF), physical attempts per logical job, and the Economic Contamination Index (ECI), total spend over spend on attempts whose output was actually used. All four cells were scoreboard-equivalent, with answer-key means of 46.8 to 47.4 of 48 checks and 9 to 10 of 10 execution-clean or recovered-clean repetitions; underneath, the attempt machinery differed by up to a factor of 1.7. Proactive budget headroom measures as prevention: one starved first attempt in 127 agent-layer jobs, and, with the retry disabled so no recovery could hide it, no amplification at either recovery ring (IAF = 1.000 by direct enumeration). Retry-based recovery reaches an equivalent scoreboard with IAF up to 1.70 and ECI up to 1.96 in the adversarial validation layer: in the worst cell, 48.9% of that layer's spend bought attempts whose output was discarded, and 228,889 of 228,890 discarded output tokens in the study were reasoning tokens, the spend category no scoreboard sees. Rescue effectiveness was also non-stationary: a same-budget re-ask recovered roughly 19 of 20 starved jobs one night and 5 of 16 two nights later under an identical configuration, so retry-based cost forecasts inherit a volatility that prevention-based forecasts do not. Across the study, 9.6% of ledger-computed spend bought discarded attempts. A retry repairs the answer. It does not erase the first invoice.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
