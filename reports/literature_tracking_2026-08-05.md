# 2026-08-05 LLM 服务系统每日文献简报

> 检索窗口：2026-08-04 至 2026-08-05（北京时间 / Asia/Shanghai）；本期确认 7 篇，其中直接 LLM 服务研究 7 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems

> 英文原标题：The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Ankur Sharma、Deep Shah
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.03214v1) · [PDF](https://arxiv.org/pdf/2608.03214v1)

<details><summary>英文原摘要（补充）</summary>

Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a stable, implementation-independent operating architecture for governing intent, selecting capabilities, preserving authority across delegation, controlling uncertainty, coordinating runtime behavior, and reconstructing why consequential actions occurred. This paper proposes the Agent Operating System (AOS), a vendor-neutral reference operating architecture for distributed agentic systems. AOS contains two internal planes: a Control & Governance Plane responsible for intent, policy, trust, authority, confidence, auditability, observability, and human oversight; and a Runtime & Coordination Plane responsible for agent lifecycle, workflow coordination, model and tool routing, context and memory coordination, scheduling, traffic management, and runtime assurance. Platform services, Linux or Windows, container runtimes, and physical infrastructure remain outside the AOS boundary and are integrated through explicit interfaces. The paper specifies AOS concepts, invariants, interface objects, optimization objectives, deployment profiles, and reliability responsibilities. It also identifies tradeoffs and unresolved research questions. AOS is not presented as a replacement for existing frameworks or infrastructure; it is proposed as the operating architecture through which heterogeneous components can be composed into governable, reliable, observable, and interoperable agentic systems.

</details>

## 2. Separating quantum circuits from classical LLMs

> 英文原标题：Separating quantum circuits from classical LLMs

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Srinivasan Arunachalam、Arkopal Dutt、Hari Krovi、Rik Sengupta
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.03962v1) · [PDF](https://arxiv.org/pdf/2608.03962v1)

<details><summary>英文原摘要（补充）</summary>

Modern large language models - transformers and diffusion language models - are built around two canonical algorithmic tasks: prediction and generation. We prove unconditional separations between low-depth quantum computation and the corresponding bounded-resource classical language-model architectures in both regimes. Concretely, we exhibit the following: 1. Distributional separation. We give a distribution that is sampleable by $\textsf{QNC}^0$ circuits (i.e., a family of constant-depth quantum circuits consisting of bounded fan-in gates) that no constant-round diffusion language model ($\textsf{DLM}$) with shallow scheduling and denoising can sample within constant distance, even when allowed sublinear chain-of-thought and output-token revision/remasking events, the very features modern $\textsf{DLM}$s rely on. 2. Functional separation. We exhibit a function computable in $\land \circ \textsf{QNC}^0[\log\log n]$ (i.e., a family of O$(\log\log n)$-depth $\textsf{QNC}^0$ circuits, where $n$ is the input length, followed by a single classical $\mathsf{AND}$ gate) such that any constant-depth decoder-only transformer computing the function must be large: it would have to have width $n^{Ω(1)}$. Together, our work initiates the study of quantum advantage in the era of large language models.

</details>

## 3. TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning

> 英文原标题：TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Wonpyo Park、Seung-won Hwang
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.03276v1) · [PDF](https://arxiv.org/pdf/2608.03276v1)

<details><summary>英文原摘要（补充）</summary>

Long-context inference with large language models is constrained by the linear growth of the key-value cache to sequence length. While pruning offers mitigation, prevailing methods determine query-specific token importance that cannot be reused across unseen queries. In contrast, we introduce TaskPress, a framework for task-guided, query-agnostic KV cache eviction. Instead of optimizing the cache for a single query, TaskPress constructs a reusable memory representation conditioned on a high-level task guide. The guide functions as a meta-query during prefill to filter irrelevant tokens before downstream queries are issued. In addition, TaskPress leverages quantization scale factors as a zero-cost signal for detecting influential representation outliers, providing an efficient proxy for token importance. Experiments on conducted on various tasks with long context input demonstrate that TaskPress efficiently creates a compact, reusable cache across diverse queries.

</details>

## 4. MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations

> 英文原标题：MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations

- **研究问题：** 这篇论文讨论与“Token 定价、订阅与额度套餐”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注按 token/请求计费、订阅与额度套餐、价格歧视及用户异质性。
- **作者：** Qiming Shi、Yulong Tao、Linbo Jin、Zhaolu Kang、Yibo Dou、Jiawen Zhu、Tianjun Pan、Shaokang Fu 等
- **来源/日期：** arXiv；首次发布 2026-07-31；最近更新 2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.28956v2) · [PDF](https://arxiv.org/pdf/2607.28956v2)

<details><summary>英文原摘要（补充）</summary>

Large language model agents are increasingly evaluated as autonomous tool users, yet most benchmarks focus on bounded tasks with immediate success criteria. Real-world deployments often require Long-Term Coherence, the capacity to preserve purposeful behavior across extended horizons while adapting decisions to accumulated evidence. Evaluating this capacity requires a persistent environment in which actions constrain future choices, feedback arrives at heterogeneous delays, and incoherent behavior produces measurable cumulative effects. Seller-side e-commerce provides a suitable setting for this evaluation through recurrent and interdependent decisions over Product Sourcing, Listing and Pricing Control, Cash-Flow Management, and Mixed-Latency Feedback Adaptation. We introduce MerchantBench, a 365-day order-level simulation grounded in 98,843 real e-commerce product records and equipped with 26 tools for agent interaction. MerchantBench couples promptly observable Upstream Supplier Events with delayed Downstream Order Outcomes, requiring agents to follow individual order lifecycles and revisit earlier decisions. We evaluate eight LLMs under two agent frameworks in 48 runs, each spanning 365 simulated days. Our results reveal a substantial gap between even the latest LLMs and human participants, with the best LLM configuration attaining only 27.3\% of the mean final net assets achieved by human participants.

</details>

## 5. Shorter Reasoning, Earlier Answers? An Evaluation of Reasoning Interfaces

> 英文原标题：Shorter Reasoning, Earlier Answers? An Evaluation of Reasoning Interfaces

- **研究问题：** 这篇论文讨论与“优先权、SLO 与差异化服务”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注付费优先、SLO/截止期、抢占规则和不同等待成本用户的服务分层。
- **作者：** Francesca Carlon、Vincent Ginis、Andres Algaba
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.03401v1) · [PDF](https://arxiv.org/pdf/2608.03401v1)

<details><summary>英文原摘要（补充）</summary>

Large language models often reason at length before answering, increasing cost and latency. Prompts and trained settings can shorten this reasoning, but a shorter trace may only show that the model stopped sooner. Here, we evaluate paired runs of the same question at matched reasoning horizons across 198 GPQA Diamond and 500 MMLU-Pro questions. We test a numeric/concision prompt that announces a token limit for Qwen3-14B and the trained effort settings of gpt-oss-20b and -120b. The Qwen prompt shortens reasoning traces by 12-17%, while accuracy changes at matched token limits are small and mixed. A concise/early-answer instruction raises MMLU-Pro accuracy by 3.8 percentage points at 512 tokens, including +2.7 points when both runs are unfinished. Its gain at 2,048 tokens is uncertain. For gpt-oss, candidate-logit answers from completed low- and medium-effort reasoning are 14.5-26.3 points more accurate than matched-horizon high-effort answers. Most of the 512-token advantage comes from lower effort finishing earlier, while differences among unfinished runs are smaller and mixed. Wrong early answers often concentrate probability on the chosen option, so earlier stopping does not uniformly improve probability quality. In these tests, a tight deadline can favor lower effort or a concise instruction, whereas allowing high effort to finish can recover higher final accuracy. Evaluations should report correct completion before a deadline, the answer obtained when a run is stopped, differences among unfinished runs, and probability assigned to the correct answer separately.

</details>

## 6. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

> 英文原标题：ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Yang Yang、Qinyu Zhao、Mouxiang Chen、Xiaohui Li、Lixin Gu、Wenhai Wang、Hongjie Zhang、Wenwei Zhang
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.04010v1) · [PDF](https://arxiv.org/pdf/2608.04010v1)

<details><summary>英文原摘要（补充）</summary>

Existing scaling strategies for Multimodal Large Language Models (MLLMs) typically expand either model parameters or sequential inference computation, incurring substantial memory or latency overhead. More importantly, most existing methods fail to alter the rigid, fixed computation allocation between the Vision Transformer and the Large Language Model components, limiting task-specific optimization. To address this, we introduce the Parallel Vision-Language (ParVL) scaling framework for MLLMs, which scales parallel computation by reusing the existing ViT and LLM backbone parameters across multiple vision and language branches. This framework raises a central question: given a fixed backbone parameter budget, how should additional shared-backbone computation be allocated between the vision and language modalities? We instantiate each parallel computational stream with branch-specific prefix parameters over a shared backbone, and train the entire model end-to-end via full-parameter supervised fine-tuning on roughly 13B tokens. We systematically study the computation-allocation trade-off between the ViT encoder and LLM decoder. ParVL improves overall multimodal performance over same-recipe single-branch baselines, and the best evaluated vision--language allocation varies across tasks. Code is available at https://github.com/YangYangGirl/ParVL.

</details>

## 7. Test-Time Scalable AI-RAN: Inference Time Allocation for Cell-Free MIMO

> 英文原标题：Test-Time Scalable AI-RAN: Inference Time Allocation for Cell-Free MIMO

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Seonghoon Yoo、Sangwoo Park、Seok-Hwan Park、Joonhyuk Kang
- **来源/日期：** arXiv；2026-08-04；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2608.03614v1) · [PDF](https://arxiv.org/pdf/2608.03614v1)

<details><summary>英文原摘要（补充）</summary>

Artificial intelligence-enabled radio access networks (AI-RANs) are envisioned to consist of multiple AI-based modules, potentially developed independently by different vendors. In this work, we study AI-RAN-enabled cell-free MIMO systems, with a particular focus on the system implications of modern AI models. Specifically, we focus on the phenomenon of test-time scalability popularized by large language models (LLMs), under which model performance improves as additional computational resources are allocated at testing time. By noting that the optimal amount of additional computational resources for each AI module should in general depend on its interaction with the other modules as well as with the underlying wireless channels, we propose a generic framework that enables optimal resource allocation for each test-time scalable module in cell-free MIMO systems. Experimental results demonstrate the effectiveness of the proposed framework in fully exploiting the potential of test-time scalable AI-RANs in cell-free MIMO systems.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
