# 2026-07-31 LLM 服务系统每日文献简报

> 检索窗口：2026-07-30 至 2026-07-31（北京时间 / Asia/Shanghai）；本期确认 6 篇，其中直接 LLM 服务研究 6 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. Back from the Future: Key-Value Cache Management by Counter-Causal Surprise

> 英文原标题：Back from the Future: Key-Value Cache Management by Counter-Causal Surprise

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Stephen Gould、Anton van den Hengel
- **来源/日期：** arXiv；2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.27600v1) · [PDF](https://arxiv.org/pdf/2607.27600v1)

<details><summary>英文原摘要（补充）</summary>

Key-value (KV) cache management through compression and eviction strategies has emerged as an important research direction in recent years. Computational demands of large language models (LLMs) and their multi-modal variants during output generation can be partially alleviated by caching previous key and value calculations needed by subsequent scaled dot-product attention operations. However, this leads to another problem: the size of the resulting KV cache grows linearly with context length and quickly consumes all available GPU memory when either the prompt or the generated output are long. KV cache management periodically prunes entries from the cache thereby reducing its memory footprint while attempting to retain sufficient information for accurate generation. A by-product is faster inference speed. We propose a simple yet effective KV eviction scheme motivated by the insight that past tokens which can be well-predicted from more recent tokens are redundant and their associated keys and values can be removed from the cache. To score entries for eviction we run the model on the tokens in their original order, reusing the key and value representations already stored in the KV cache, and applying a counter-causal attention mask so that each position attends only to its future context. This is in-distribution, tied directly to the actual cache contents, and requires no additional training. To further reduce cost, we additionally propose a fast single-layer approximation that restricts the counter-causal pass to the last transformer layer, achieving a significant speedup per refresh cycle at marginal accuracy cost. We evaluate our strategy on various open-source LLMs and benchmark datasets showing competitive or improved performance over other state-of-the-art methods. Reference code is available at https://github.com/metacognitionai/counter_causal.

</details>

## 2. Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling

> 英文原标题：Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Yuan Tian、Yi Mei、Mengjie Zhang
- **来源/日期：** arXiv；2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.27698v1) · [PDF](https://arxiv.org/pdf/2607.27698v1)

<details><summary>英文原摘要（补充）</summary>

In dynamic multi-mode project scheduling, activities have alternative execution modes and uncertain durations, while precedence relations and limited resources constrain their execution. Heuristic priority rules support fast online decisions, but their design requires substantial domain expertise. Genetic programming (GP) hyper-heuristics can automatically evolve such rules. Large language models (LLMs), meanwhile, provide a flexible interface for interpreting scheduling information and explaining decisions. However, zero-shot LLM decisions may lack domain knowledge, consume many tokens, and vary across repeated queries. GP-evolved rules therefore provide a potential source of scheduling knowledge for guiding LLM decisions. Unlike existing LLM--GP hybrids that use LLMs to support heuristic evolution, we transfer knowledge in the reverse direction, using knowledge extracted from high-quality GP rules to guide an online LLM decision maker. We extract knowledge from high-quality GP rules and inject it through Feature Selection, Feature Hint, Rule Reference, and Rule Follow. These mechanisms are evaluated in terms of scheduling performance, token consumption, decision stability, and the feature focus expressed in generated rationales. GP-derived guidance generally improves the unguided LLM, but its representation matters. Simplifying the decision context or supplying explicit decision logic is more effective than highlighting important features. Feature Selection offers the best token efficiency, whereas Rule Follow achieves strong performance at greater token cost. Guidance also improves decision stability and changes the features expressed in generated rationales.

</details>

## 3. S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring

> 英文原标题：S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Glenn Anta Bucagu、Thorir Mar Ingolfsson、Yawei Li、Luca Benini
- **来源/日期：** arXiv；2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.27913v1) · [PDF](https://arxiv.org/pdf/2607.27913v1)

<details><summary>英文原摘要（补充）</summary>

Foundation models offer a promising paradigm for Electroencephalography (EEG) analysis, leveraging generalizable representations from vast unlabeled datasets. Yet, Transformer-based architectures face a critical bottleneck: global attention mechanisms couple the attention memory state to the signal duration, causing memory overflow during continuous monitoring. To address this, we introduce S-CEReBrO (Streaming CEReBrO), an evolution of the CEReBrO architecture designed for continuous monitoring. Our novel Windowed Alternating Attention mechanism factorizes attention computation into fixed-size spatiotemporal windows, guaranteeing constant KV cache memory as only the active window requires resident attention maps. Empirical scaling analysis confirms that windowed alternating attention can process signals 100X longer than full self-attention and 3X longer than low-rank linear attention. Compared to low-rank linear attention on long contexts, windowed alternating attention requires 55% of the memory while increasing inference throughput by 2.1X. Pre-trained on >25,000 hours of recordings from >12,000 subjects, S-CEReBrO achieves state-of-the-art performance on 7 of 11 downstream tasks, with up to 60% fewer parameters. This work represents a significant step toward the realization of efficient, generalizable, and continuous EEG monitoring. An accompanying code repository is available.

</details>

## 4. SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer

> 英文原标题：SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Xuchuan Luo、Jiacheng Shen、Xin Wang、Yangfan Zhou
- **来源/日期：** arXiv；2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.28150v1) · [PDF](https://arxiv.org/pdf/2607.28150v1)

<details><summary>英文原摘要（补充）</summary>

Disaggregating the prefill and decoding stages of large language model (LLM) inference into two separate sets of nodes is widely adopted in today's LLM serving systems. However, such an architecture poses significant challenges for self-hosted LLM deployments on rented cloud instances, since transferring enormous key-value (KV) caches between disaggregated nodes can easily saturate the limited inter-node network bandwidth. In this paper, we propose to mitigate the network bottleneck by selectively transferring essential KV cache entries across the two stages. There are two challenges to achieve selective KV cache transfer, i.e., accurate KV selection during the prefill stage, and efficient KV fetching during the decoding stage. To address these challenges, we design SmartGen, a KV cache transfer engine that allows seamless disaggregated LLM inference with three data transfer paths. Specifically, we leverage 1) a profile-based proactive transfer path to identify and push essential KV cache entries to the decoding node during the prefill stage, 2) a parallel on-demand transfer path to simultaneously fetch remote and local KV cache entries during the decoding stage, and 3) a speculative transfer path to finally deliver all KV caches to the decoding node. Experimental results show that SmartGen reduces time-to-second-token by up to 4.3x compared with the typical full KV cache transfer approach while offering comparable subsequent decoding performance and accuracy.

</details>

## 5. RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing

> 英文原标题：RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing

- **研究问题：** 这篇论文讨论与“Token 定价、订阅与额度套餐”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注按 token/请求计费、订阅与额度套餐、价格歧视及用户异质性。
- **作者：** Liexin Cheng、Xue Cheng、Shuaiqiang Liu、Cornelis W. Oosterlee
- **来源/日期：** arXiv；首次发布 2026-07-28；最近更新 2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.25199v2) · [PDF](https://arxiv.org/pdf/2607.25199v2)

<details><summary>英文原摘要（补充）</summary>

Automated code generation is becoming an important tool in quantitative finance, where large language models can generate option pricing implementations directly from mathematical model specifications. Validating such implementations, however, requires considerably more than conventional software testing: numerical pricing methods must remain mathematically consistent, numerically stable, and reliable across a wide range of model parameters. We introduce RIDGE, an autonomous validation framework in which generated pricing implementations are subjected to structured no-arbitrage tests, stress tests, benchmark comparisons, and consistency checks. Validation evidence is interpreted diagnostically, while the resulting knowledge is accumulated in a repository and reused across models and successive validation iterations. This enables systematic refinement of both the pricing implementation and the validation methodology. The framework is applied to five stochastic volatility models. Across these studies, all detected implementation defects are removed and, in two cases, the validation process reveals methodological limitations and motivates the development of alternative numerical methods. The supplementary material is available in the GitHub repository: https://github.com/ShQiangLiu/ridge.

</details>

## 6. A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding

> 英文原标题：A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Yuesong Liu、Yuan Zeng、Min Lyu、Ruilin Liu、Yu Guo、Yinlong Xu
- **来源/日期：** arXiv；2026-07-30；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.27735v1) · [PDF](https://arxiv.org/pdf/2607.27735v1)

<details><summary>英文原摘要（补充）</summary>

Speculative decoding alleviates the memory-bandwidth bottleneck in large language model inference, but its acceleration is jointly constrained by drafting overhead, token acceptance, and speculation length. We present a unified efficiency analysis showing that extending the speculation horizon can reduce rather than improve speedup when the marginal acceptance probability falls below the relative drafting cost. Guided by this analysis, we introduce SparseSpec-L, a training-free self-speculative decoding framework for long-context inference. SparseSpec-L generates lightweight drafts directly from the target model using a dynamically sparsified and recallable KV cache. It recycles per-head attention statistics produced during full-context verification as a no-extra-forward importance signal, allowing critical historical tokens to be recalled without permanently discarding the dense KV cache. An online entropy-based controller further selects the speculation length according to expected step-wise efficiency. Experiments across multiple long-context tasks and model scales show consistent end-to-end acceleration, with up to speedup over autoregressive decoding while preserving the target model's output distribution.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
