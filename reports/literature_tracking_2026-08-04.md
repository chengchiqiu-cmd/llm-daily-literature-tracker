# 2026-08-04 LLM 服务系统每日文献简报

> 检索窗口：2026-08-03 至 2026-08-04（北京时间 / Asia/Shanghai）；本期确认 9 篇，其中直接 LLM 服务研究 9 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving

> 英文原标题：HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Yuning Zhang、Dong Yuan
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 13

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.01785v1) · [PDF](https://arxiv.org/pdf/2608.01785v1)

<details><summary>英文原摘要（补充）</summary>

Omni models unify text, speech, image, and multimodal reasoning in a single serving backend, but this unified deployment exposes a new scheduling problem. Requests with different output modalities may share an initial multimodal backbone and then diverge into downstream generation stages, creating heterogeneous first-response metrics and service-level objective (SLO) targets on the same GPU. Existing large language model (LLM) and multimodal serving systems mainly optimize token progress or input-side processing, and they do not jointly control temporal sharing in the shared stage and spatial sharing among co-running stages. This paper presents HorizonServe, a single-GPU omni-model serving system that coordinates request admission and GPU allocation under heterogeneous SLOs. HorizonServe profiles per-class first-response latency, protects requests with limited slack, rotates shared-stage opportunities across execution paths, and throttles the shared-stage streaming multiprocessor (SM) allocation when downstream stages are active. Across three omni-model workloads and two GPU platforms, HorizonServe improves SLO attainment by up to 4.9$\times$ in arrival-rate sweeps and 7.0$\times$ under downstream-heavy traffic, and reduces per-class first-response latency by 38.4--63.7\%.

</details>

## 2. AIC-VDS: Attention-Based In-Context Learning for Joint Velocity Control and Data Collection Scheduling in Multi-UAV-Assisted Pipeline Monitoring

> 英文原标题：AIC-VDS: Attention-Based In-Context Learning for Joint Velocity Control and Data Collection Scheduling in Multi-UAV-Assisted Pipeline Monitoring

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Yousef Emami、Miguel Gutierrez Gaitan、Atefeh Hajijamali Arani、Jingjing Zheng、Hao Zhou
- **来源/日期：** arXiv；首次发布 2025-10-07；最近更新 2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 11

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2510.05698v2) · [PDF](https://arxiv.org/pdf/2510.05698v2)

<details><summary>英文原摘要（补充）</summary>

Uncrewed aerial vehicles (UAVs) are increasingly deployed for autonomous inspection and sensor data collection in large-scale infrastructure monitoring applications, such as pipeline monitoring, where timely anomaly detection is critical. Jointly optimizing data-collection schedules and flight velocities is a critical challenge, as inefficiencies can increase packet loss and inspection latency. While online deep reinforcement learning (DRL) is a widely investigated approach, it suffers from low sample efficiency, substantial training requirements, and simulation-to-reality gaps in time-sensitive scenarios. Large language models (LLMs) offer a promising alternative through in-context learning (ICL); however, their substantial input requirements can introduce considerable computational and communication overhead. To address this, we propose Attention-Based In-Context Learning for Velocity Control and Data Collection Scheduling (AIC-VDS), a joint optimization framework designed to minimize packet loss under partial and potentially outdated local network-state information. AIC-VDS utilizes an attention module to process real-time network-state data, including sensor battery levels, sensor queue lengths, communication channel conditions, UAV locations, time since the previous sensor visit, and sensor urgency scores. This module extracts task-relevant features to reduce input overhead before querying the LLM. The LLM leverages these compressed natural-language prompts to generate adaptive data-collection schedules and velocity-control decisions for UAV execution. Simulation results show that the attention-based representation reduces the average prompt length by 50\%, while AIC-VDS rapidly stabilizes packet loss in the considered scenario.

</details>

## 3. Bole: Efficient Tree Speculation for Hybrid-Attention Language Models

> 英文原标题：Bole: Efficient Tree Speculation for Hybrid-Attention Language Models

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Li Wang、Yi Su、Xiabao Wu、Chiran You、Yongchao Liu、Zhan Qiu、Juelu Zhang、Jiajun Zheng 等
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 11

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.01651v1) · [PDF](https://arxiv.org/pdf/2608.01651v1)

<details><summary>英文原摘要（补充）</summary>

Hybrid-attention large language models combine full attention with recurrent linear attention to reduce long-context inference costs, yet their autoregressive decoding remains memory-bound. Tree speculative decoding offers an attractive acceleration path, but existing tree-speculation systems are designed around the key--value caches of full-attention models. On hybrid models, they traverse recurrent layers branch by branch and materialize a full state for every proposal node, causing verification latency and transient memory to scale poorly with tree and batch sizes. We present Bole, a kernel--runtime co-design that enables efficient tree speculation for hybrid-attention LLMs. Bole transforms the linear-attention recurrence into a tree-structured closed form and realizes it with a resource-efficient GPU kernel, verifying all proposal nodes in parallel and accelerating linear-attention tree verification by 3.4--7.7$\times$. It losslessly encodes speculative state updates as token-level factors and reconstructs only the state selected after sampling, reducing transient state memory by 82--99$\times$ and freeing GPU capacity for KV caches. Its integration into SGLang, a widely deployed production LLM serving engine, couples efficient state management with a batch-wide verification budget calibrated to the complete hybrid forward. Across four models, two GPU platforms, and diverse datasets, Bole delivers up to $4.72\times$ the offline decode throughput of autoregressive decoding and up to $2.03\times$ that of the strongest tree-speculative baseline. Under online agent workloads, it reduces TTFT and TPOT by up to $67.6%$ and $49.9%$, respectively, over the strongest tree-speculative baseline.

</details>

## 4. Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling

> 英文原标题：Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Dayi Yao、Zijie Zhou
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 11

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.02244v1) · [PDF](https://arxiv.org/pdf/2608.02244v1)

<details><summary>英文原摘要（补充）</summary>

This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache footprint, a short request co-batched with a long request can experience latency and GPU-resource consumption disproportionate to its own token workload. We formalize this phenomenon as a resource-fair scheduling problem. We develop a mathematical scheduling model that connects within-batch resource fairness to system throughput. The proposed fairness constraint bounds the disparity in decode progress, equivalently KV-cache footprint, among co-batched requests. Based on this model, we design the Insert-Short-Jobs-with-Limit (ISJL) algorithm, a parameterized hybrid batching policy. We prove that ISJL achieves a global competitive-ratio lower bound of $3/4$. We further examine the profit implications of resource-fair scheduling under the token-metered pricing convention used by commercial LLM APIs. Numerical experiments show that ISJL occupies a favorable middle ground between FCFS, which has large batching externalities, and LJF, which is cost-aligned but sacrifices batching flexibility. Thus, ISJL provides a bi-criterion scheduling policy: it maintains high throughput while aligning max-driven batch cost with token-metered revenue.

</details>

## 5. Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling

> 英文原标题：Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling

- **研究问题：** 这篇论文讨论与“优先权、SLO 与差异化服务”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注付费优先、SLO/截止期、抢占规则和不同等待成本用户的服务分层。
- **作者：** Cunchen Hu、Liangliang Xu、Tian Liu、Min Lyu、Yongkun Li、Sa Wang、Shuo Quan、Yanan Yang 等
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 10

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.01891v1) · [PDF](https://arxiv.org/pdf/2608.01891v1)

<details><summary>英文原摘要（补充）</summary>

Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption. Existing energy-management approaches adapt GPU frequencies only at the request or inference-phase level, overlooking operator-level differences in frequency sensitivity between Attention and feed-forward networks (FFNs). We find that the energy-optimal frequencies of Attention and FFN (A/F) differ and vary with the inference phase, workload, and system configurations. However, runtime variability and independent A/F frequency control create a large search space and high communication overhead. To address these challenges, we present AFlex, a framework that jointly optimizes resource provisioning and GPU frequency scaling for disaggregated A/F serving. AFlex introduces a global scheduler and a local operator-level dynamic voltage and frequency scaling (DVFS) controller to determine A/F resource allocations and frequencies. It further introduces an interleaved A/F pipeline with dynamic microbatch depth and adaptive request batching to reduce pipeline bubbles. We implement AFlex in SGLang and evaluate it on NVIDIA A800 GPUs using Qwen3-32B and Mixtral-8$\times$7B under production Conversation and Coding traces. \AFlex reduces energy per token by up to 49\% over state-of-the-art disaggregated serving and 48\% over frequency-scaling systems while satisfying TTFT and TPOT SLOs.

</details>

## 6. Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO

> 英文原标题：Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO

- **研究问题：** 这篇论文讨论与“优先权、SLO 与差异化服务”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注付费优先、SLO/截止期、抢占规则和不同等待成本用户的服务分层。
- **作者：** Ngoc Hung Nguyen、Bjorn Landfeldt
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 10

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.02031v1) · [PDF](https://arxiv.org/pdf/2608.02031v1)

<details><summary>英文原摘要（补充）</summary>

This paper investigates collaborative mobile edge computing (MEC) servers for large language model (LLM) inference under soft deadline constraints. In this system, to improve the quality of service, computations are expected to be completed within their deadlines. However, due to dependencies among tasks or subtasks, any missed deadline can lead to catastrophic consequences for the entire request. In this context, this work proposes an extended deadline mechanism with constrained flexibility. The main challenges lie in handling large-scale computations under strict latency constraints while limiting the number of allowable deadline extensions, especially in the presence of task dependencies within each request. To tackle these challenges, we develop a transformer-enhanced proximal policy optimization (PPO) framework that enables efficient collaboration among MEC servers. The proposed approach aims to maximize the number of tasks completed within their deadlines while minimizing the use of deadline extensions. By capturing temporal dependencies and cross-server interactions, the transformer improves decision-making for task migration. Simulation results demonstrate that the proposed method significantly outperforms conventional PPO and heuristic-based approaches in terms of task completion rate and overall system efficiency.

</details>

## 7. EdgeCoInfer: Hierarchical Collaborative Inference for On-Device Multimodal Large Models

> 英文原标题：EdgeCoInfer: Hierarchical Collaborative Inference for On-Device Multimodal Large Models

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Lin Tan、Songtao Guo、Mingyan Li、David K. Y. Yau
- **来源/日期：** arXiv；首次发布 2026-07-19；最近更新 2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 9

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2607.17143v2) · [PDF](https://arxiv.org/pdf/2607.17143v2)

<details><summary>英文原摘要（补充）</summary>

To deliver ubiquitous intelligence, modern mobile applications increasingly execute concurrent Multimodal Large Language Models (MLLMs) on edge devices, presenting severe challenges under multi-task concurrency and tight resource constraints. To address this, we propose EdgeCoInfer, a hierarchical collaborative inference framework enabling efficient on-device MLLM inference through coarse-to-fine orchestration. Coarsely, EdgeCoInfer decomposes MLLMs into functional modules for inter-task sharing, avoiding redundant model loading. Finely, it partitions models at the neural network layer level and distributes segments across devices and servers. We jointly optimize layer partitioning, module sharing, and resource allocation under tight constraints. To tackle the non-differentiable combinatorial explosion, we propose a Hybrid Evolutionary Hierarchical Reinforcement Learning (HE-HRL) framework. HE-HRL synchronizes a gradient-free genetic algorithm for discrete partitioning and sharing decisions with a gradient-based soft actor-critic agent for continuous resource refinement. We further embed a constructive cut-step decoder with pre-act pruning and a two-phase curriculum to improve feasibility and accelerate convergence. Experimental results show that EdgeCoInfer breaks the edge memory wall and prevents catastrophic out-of-memory and task failures under high concurrency, reducing memory demand by 53.53\% and system cost by 59.86\% compared to existing methods.

</details>

## 8. What is the Role of Small Models in the LLM Era: A Survey

> 英文原标题：What is the Role of Small Models in the LLM Era: A Survey

- **研究问题：** 这篇论文讨论与“数据中心能源、碳与跨时段转移”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 LLM 负载的电力、碳、水约束，以及跨地点/跨时段需求响应。
- **作者：** Lihu Chen、Gaël Varoquaux
- **来源/日期：** arXiv；首次发布 2024-09-10；最近更新 2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 8

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2409.06857v8) · [PDF](https://arxiv.org/pdf/2409.06857v8)

<details><summary>英文原摘要（补充）</summary>

Large Language Models (LLMs) have made significant progress in advancing artificial general intelligence (AGI), leading to the development of increasingly large models such as GPT-4 and LLaMA-405B. However, scaling up model sizes results in exponentially higher computational costs and energy consumption, making these models impractical for academic researchers and businesses with limited resources. At the same time, Small Models (SMs) are frequently used in practical settings, although their significance is currently underestimated. This raises important questions about the role of small models in the era of LLMs, a topic that has received limited attention in prior research. In this work, we systematically examine the relationship between LLMs and SMs from two key perspectives: Collaboration and Competition. We hope this survey provides valuable insights for practitioners, fostering a deeper understanding of the contribution of small models and promoting more efficient use of computational resources. The code is available at https://github.com/tigerchen52/role_of_small_models

</details>

## 9. TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference

> 英文原标题：TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Ruilin Xu、Junyi Li、Pengfei Chen、Zongxuan Xie
- **来源/日期：** arXiv；2026-08-03；arXiv
- **研究类型：** 待全文核验；直接 LLM 服务研究；相关性评分 7

### 中文内容总结

中文深度摘要尚未生成。请配置自动分析 API，或在阅读全文后补充研究问题、模型设定、求解方法和主要结论。

### 模型设定

**模型主线：** 模型设定尚待全文核验。

**参与者 / 系统组件**

- 尚待全文核验

**决策变量**

- 尚待全文核验

**关键参数与状态**

- 尚待全文核验

**研究时序**

1. 获取全文
2. 核验模型设定与公式
3. 生成中文研究解读

### 公式与求解

- 现有证据不足以可靠复原公式。

**如何求解：** 尚待全文核验。

### 主要结果

- 尚待全文核验

### 局限与核验边界

- 当前仅凭题录或摘要，不能可靠复原模型。
- **核验说明：** 未完成全文核验；英文原摘要仅作为补充材料展示。
- **链接：** [论文页](http://arxiv.org/abs/2608.01975v1) · [PDF](https://arxiv.org/pdf/2608.01975v1)

<details><summary>英文原摘要（补充）</summary>

Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication. Existing profilers expose raw timelines, while log-based diagnosis often misses cross-layer execution semantics and request-level structure. We present TELLER, a non-intrusive Trace- and Log-aware LLM inference Root-cause analysis framework. TELLER first collects NVTX/CUPTI traces and service logs without modifying model binaries, then reconstructs per-request call-chain trees and aligns log lines with the corresponding execution steps. We introduce a dependency-aware causal-context slice that preserves parent-child structure, temporal order, and communication relations, and a Trace Pair Encoding (TPE) tokenizer that compresses such slices into compact structural token sequences with parent, depth, and duration attributes. On top of these representations, TELLER combines numeric candidate localization with a multimodal root-cause model that jointly predicts abnormal steps, localizes suspicious operators, and generates natural-language explanations. Experiments on multi-node GPU inference workloads show a clear compression-accuracy trade-off: a moderate TPE vocabulary reduces per-step trace length by more than 80% while achieving the best overall performance on both horizontal (cross-node communication) and vertical (within-node execution stack) views, whereas more aggressive compression substantially degrades diagnosis quality. Further analyses under low-fault priors, strengthened baselines, modality ablations, explanation-quality checks, and tracing overhead show that TELLER provides a practical triage and evidence-localization substrate for LLM inference RCA.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
