# 2026-07-23 LLM 服务系统每日文献简报

> 检索窗口：2026-07-22 至 2026-07-23（北京时间 / Asia/Shanghai）；本期确认 7 篇，其中直接 LLM 服务研究 7 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models

> 英文原标题：Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Chen Li、Jiexiong Liu、Yixuan Chen、Yi Li
- **来源/日期：** arXiv；首次发布 2026-07-14；最近更新 2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.13093v3) · [PDF](https://arxiv.org/pdf/2607.13093v3)

<details><summary>英文原摘要（补充）</summary>

On-device LLM inference faces a trilemma of response latency, limited hardware resources and user privacy. Full cloud inference delivers strong computing power but exposes user prompts and dialogue data, while standalone on-device inference is unfeasible for most consumer and embedded edge devices. This paper presents a privacy-centric edge-cloud collaborative LLM inference framework built on endpoint-authenticated KV cache. Local endpoints handle input preprocessing, embedding computation, adaptive feature optimization, KV cache authentication, speculative decoding and low-dimensional model head calculation, while the cloud conducts authenticated decoder inference, KV cache management, token verification and high-dimensional vocabulary projection. Endpoints fuse partial outputs, apply language-adaptive masking and sample target tokens. All transmitted data and truncated logits are quantized and AES-GCM encrypted for privacy, with core lightweight modules, draft parameters and cache access policies kept local to avoid leakage. The framework supports heterogeneous devices including CPU-only, GPU-equipped and embedded devices via optimized streaming, batching and quantized ONNX deployment. Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.

</details>

## 2. HijackKV: New Threat in Position-Independent KV Cache Reuse

> 英文原标题：HijackKV: New Threat in Position-Independent KV Cache Reuse

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Yichi Zhang、Zhiqi Wang、Huan Zhang、Yuchen Yang
- **来源/日期：** arXiv；2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.19957v1) · [PDF](https://arxiv.org/pdf/2607.19957v1)

<details><summary>英文原摘要（补充）</summary>

Key-Value (KV) cache reduces inference latency in large language models (LLMs). Traditional prefix-based reuse has low cache hit rates across inference requests because it requires exact token and position matches. To improve efficiency, recent system optimizations introduce position-independent KV reuse, allowing KV cache to be reused whenever identical text chunks appear, regardless of their position in the sequence. We show this design introduces a new threat, KV Cache Hijacking. Since KV caches are retrieved by token match but encode the context in which they were originally computed, the KV tied to a benign-looking token chunk may encode an attacker-controlled prefix. When later reused in a victim query, this contaminated KV silently hijacks the model's behavior, even if no attacker-controlled text appears in the input. We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality. HIJACKKV optimizes an attacker-controlled prefix, so that the KV computed for a subsequent common benign text encodes the attacker's goal, while the text remains unchanged for future cache hits. HIJACKKV achieves an average 94% success rate in a single attempt, remains effective under realistic constraints including low hit rates (10%) and frequent recomputation (50%), persists over multi-turn interactions, and transfers across models in black-box settings. We further provide design insights for building secure KV reuse systems.

</details>

## 3. Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs

> 英文原标题：Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Pengcheng Wang、Zhiquan Wang、Jayoung Lee、Zhuoyan Xu、Ran Xu、Saurabh Bagchi、Yin Li、Somali Chaterji
- **来源/日期：** arXiv；2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.20357v1) · [PDF](https://arxiv.org/pdf/2607.20357v1)

<details><summary>英文原摘要（补充）</summary>

Multimodal Large Language Models (MLLMs) have recently demonstrated strong performance across vision-language tasks. However, their high inference cost, arising from both the large number of input visual tokens and the heavy computation of the large language model (LLM), remains a key barrier to practical deployment. Recent work attempts to reduce the cost by adaptively optimizing individual dimensions, e.g., pruning redundant visual tokens or skipping LLM layers and heads. Nonetheless, prior approaches typically treat these dimensions independently and overlook a fundamental coupling: the available compute resources must be dynamically allocated across all dimensions based on the input content. To bridge the gap, we propose SmartVL, a unified adaptive inference framework that jointly controls vision token number and model compute capability in response to varying input contents and compute budgets. SmartVL introduces a vision-side token controller that dynamically selects informative visual tokens and an LLM-side compute controller that adaptively adjusts LLM computation. Importantly, these controllers are trained to coordinate with each other so that the overall inference cost satisfies a target budget. To allow this joint scheduling, we connect the controllers using a shared budget encoding and leverage a differentiable latency estimator for end-to-end training. This design enables SmartVL to learn cross-stage allocation strategies that adapt to both input complexity and runtime compute constraints. Experiments across multiple MLLM benchmarks demonstrate that, with joint scheduling, SmartVL consistently outperforms prior adaptive methods and achieves superior accuracy-efficiency Pareto frontiers. Project page: https://www.schaterji.io/publications/2026/jointtokencompute.

</details>

## 4. WARA: A Closed-Loop Multi-Agent Framework for Wireless Optimization Autoresearch

> 英文原标题：WARA: A Closed-Loop Multi-Agent Framework for Wireless Optimization Autoresearch

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Yuan Guo、Yilong Chen、Chao Hu、Xianghao Yu、Liang Hong、Jie Xu
- **来源/日期：** arXiv；2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.19822v1) · [PDF](https://arxiv.org/pdf/2607.19822v1)

<details><summary>英文原摘要（补充）</summary>

Large language model (LLM) agents have shown growing capabilities in tool use, code execution, artifact inspection, and iterative revision, creating new opportunities for automating scientific research. To the best of our knowledge, this paper presents the first end-to-end autoresearch framework for the wireless domain, with a particular focus on wireless resource allocation optimization, an essential area for characterizing the fundamental performance limits of wireless systems and enhancing their practical performance under dynamic channel and network conditions. Specifically, we propose the Wireless AutoResearch Agent (WARA), a closed-loop multi-agent system that transforms an initial research topic into a complete research package. WARA organizes the research workflow into three phases: 1) research gap identification and problem proposal, 2) optimization modeling, algorithm design, and experimentation, and 3) research deliverable construction. Each phase follows an artifact-mediated process, in which structured upstream artifacts are consumed to generate downstream outputs. Controller-managed gates validate these artifacts and maintain consistency among problem formulations, algorithms, experiments, and research claims. When validation fails, WARA repairs only the affected artifact instead of restarting the entire workflow. We further design an LLM-based ScoringAgent to evaluate manuscript-level research validity. Comparative results show that WARA substantially outperforms one-shot LLM generation and approaches the quality profile of recently accepted peer-reviewed papers. These results demonstrate the potential of closed-loop artifact control for end-to-end LLM-assisted wireless optimization research. The source code is available at https://github.com/guoyuan-dotcom/WARA_CUHKSZ

</details>

## 5. Harmonia: Algorithm-Hardware Co-Design for Memory- and Compute-Efficient BFP-based LLM Inference

> 英文原标题：Harmonia: Algorithm-Hardware Co-Design for Memory- and Compute-Efficient BFP-based LLM Inference

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Xinyu Wang、Jieyu Li、Yanan Sun、Weifeng He
- **来源/日期：** arXiv；首次发布 2026-02-04；最近更新 2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2602.04595v3) · [PDF](https://arxiv.org/pdf/2602.04595v3)

<details><summary>英文原摘要（补充）</summary>

Large Language Models (LLMs) incur substantial memory and computation costs. Prior works reduce FP-INT arithmetic overhead by converting linear-layer activations to block floating point (BFP), but retain FP activations in attention layers due to accuracy concerns. We propose Harmonia, an algorithm-hardware co-design framework that enables BFP representation and computation across both linear and attention layers. Harmonia first explores BFP configurations to balance model accuracy and activation compression. It then combines asymmetric bit allocation with hybrid offline-online outlier smoothing to compress the KV cache from FP16 to 4-bit-mantissa BFP with less than 1% average accuracy loss on LongBench. To efficiently support all-layer BFP computation, Harmonia incorporates a reconfigurable PE unit for mixed data formats and precisions, a real-time FP16-to-BFP converter, and a flexible tiling-aware dataflow that reduces external memory traffic. Evaluations across eight widely used LLMs show that Harmonia achieves 3.84x higher area efficiency, 2.03x better energy efficiency, and 3.08x speedup on average, with maximum improvements of 5.05x, 3.90x, and 4.62x, respectively.

</details>

## 6. Generative Augmented Inference of LLM-generated Data for Market Research: Theory and Empirical Evidence

> 英文原标题：Generative Augmented Inference of LLM-generated Data for Market Research: Theory and Empirical Evidence

- **研究问题：** 这篇论文讨论与“Token 定价、订阅与额度套餐”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注按 token/请求计费、订阅与额度套餐、价格歧视及用户异质性。
- **作者：** Cheng Lu、Mengxin Wang、Dennis J. Zhang、Heng Zhang
- **来源/日期：** arXiv；首次发布 2026-04-16；最近更新 2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2604.14575v3) · [PDF](https://arxiv.org/pdf/2604.14575v3)

<details><summary>英文原摘要（补充）</summary>

Marketing research often relies on parameters estimated from costly human-generated data, such as conjoint survey responses, purchase decisions, and field experiment outcomes. Recent advances in large language models (LLMs) and other AI systems offer inexpensive auxiliary data, but introduce a new challenge: AI outputs are not direct observations of the target outcomes, but could involve high-dimensional representations with complex and unknown relationships to human labels. Conventional methods leverage AI predictions as direct proxies for true labels, which can be inefficient or unreliable when this relationship is weak or misspecified. We propose Generative Augmented Inference (GAI), a general framework that incorporates AI-generated outputs as informative features for estimating models of human-labeled outcomes. GAI uses an orthogonal moment construction that enables consistent estimation and valid inference with a flexible, nonparametric relationship between LLM-generated outputs and human labels. We establish asymptotic normality and a key dominance result: under random labeling, GAI is optimal within a unified class of debiased estimators-including human-data-only estimators and state-of-the-art debiasing methods-and delivers strict improvements under a mild informativeness condition. Even when the labeled sample is not representative of the target population, an extended variant of GAI still dominates the weighted human-data-only estimator. Empirically, GAI outperforms benchmarks across diverse marketing research settings. In a conjoint analysis, it halves estimation error and reduces human labeling requirements by over 75%. In a pricing study, it consistently outperforms alternative estimators when all methods receive identical auxiliary inputs. In a health insurance study, it saves over 90% of labels while preserving decision accuracy.

</details>

## 7. When Shippers Become Algorithms: Candidate Exposure, Information Design, and the Concentration of LLM-Mediated Freight Markets

> 英文原标题：When Shippers Become Algorithms: Candidate Exposure, Information Design, and the Concentration of LLM-Mediated Freight Markets

- **研究问题：** 这篇论文讨论与“平台经济、市场设计与竞争”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注模型供应商、平台和用户之间的定价、竞争、筛选与激励相容。
- **作者：** Takahiro Ezaki、Naoto Imura、Katsuhiro Nishinari
- **来源/日期：** arXiv；2026-07-22；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.19967v1) · [PDF](https://arxiv.org/pdf/2607.19967v1)

<details><summary>英文原摘要（补充）</summary>

Shippers are beginning to delegate carrier selection to large language model (LLM) agents. We ask what such delegation does to a freight matching market, and which platform design choices contain it. We carried out agent-based simulations in which fifty shipper agents, built on commercial LLMs from OpenAI (GPT), Anthropic (Claude), and Google (Gemini), procure truckload capacity for thirty days. The market implements the rules of digital freight matching: each load is offered down the shipper's ranked list of carriers (waterfall tendering), carriers have daily capacity limits, spot prices respond to congestion, and carrier ratings accumulate with transactions. We found three risks and one remedy that works. Agents converged at once: for a fixed sampled carrier population, the same carrier was the modal first choice of every model on day one, attracting up to 76% of requests. Because each agent picks from its own randomly drawn list of displayed candidates, the platform controls how many options each shipper sees; concentration rose steeply once lists exceeded about ten carriers, with the onset differing across models. Which carriers ended up dominant varied widely from one sampled market to another, and displaying true quality instead of estimated ratings changed neither the level nor this variability (by design, quality affects only what agents see, never delivery outcomes). Against these risks, disclosing each carrier's remaining daily capacity cut concentration by a third and doubled shipper surplus, while vendor diversification, list-order randomization, and popularity display showed no clearly detectable effect. Platform information design, ahead of model choice or model regulation, is the lever that works.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
