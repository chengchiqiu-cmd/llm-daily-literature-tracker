# 2026-07-16 LLM 服务系统每日文献简报

> 检索窗口：2026-07-15 至 2026-07-16（北京时间 / Asia/Shanghai）；本期确认 5 篇，其中直接 LLM 服务研究 5 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. NSNQuant: A Double Normalization Approach for Calibration-Free Low-Bit Vector Quantization of KV Cache

> 英文原标题：NSNQuant: A Double Normalization Approach for Calibration-Free Low-Bit Vector Quantization of KV Cache

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Donghyun Son、Euntae Choi、Sungjoo Yoo
- **来源/日期：** arXiv；首次发布 2025-05-23；最近更新 2026-07-15；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2505.18231v3) · [PDF](https://arxiv.org/pdf/2505.18231v3)

<details><summary>英文原摘要（补充）</summary>

Large Language Model (LLM) inference is typically memory-intensive, especially when processing large batch sizes and long sequences, due to the large size of key-value (KV) cache. Vector Quantization (VQ) is recently adopted to alleviate this issue, but we find that the existing approach is susceptible to distribution shift due to its reliance on calibration datasets. To address this limitation, we introduce NSNQuant, a calibration-free Vector Quantization (VQ) technique designed for low-bit compression of the KV cache. By applying a three-step transformation-1) a token-wise normalization (Normalize), 2) a channel-wise centering (Shift), and 3) a second token-wise normalization (Normalize)-with Hadamard transform, NSNQuant effectively aligns the token distribution with the standard normal distribution. This alignment enables robust, calibration-free vector quantization using a single reusable codebook. Extensive experiments show that NSNQuant consistently outperforms prior methods in both 1-bit and 2-bit settings, offering strong generalization and up to 3$\times$ throughput gain over full-precision baselines. Code is available at https://github.com/DHdroid/NSNQuant.

</details>

## 2. JW-ASTClaw: A Generalizable Multi-Agent Framework for Autonomous Solar Telescope and Its Implementation within Chinese Meridian Project

> 英文原标题：JW-ASTClaw: A Generalizable Multi-Agent Framework for Autonomous Solar Telescope and Its Implementation within Chinese Meridian Project

- **研究问题：** 这篇论文讨论与“LLM 推理排队与调度”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注请求到达、prefill/decode、批处理、KV cache 与时延—吞吐权衡。
- **作者：** Li-Yue Tong、Jia-Ben Lin、Yuan-Yong Deng、Ying-Zi Sun、Ming-Fu Shao、Hui Wang、Chen Yang
- **来源/日期：** arXiv；2026-07-15；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.13549v1) · [PDF](https://arxiv.org/pdf/2607.13549v1)

<details><summary>英文原摘要（补充）</summary>

We present the first deployment of an end-to-end autonomous control system driven by a large language model (LLM) on an operational solar telescope-the Solar Full-disk Multi-layer Magnetograph (SFMM), named JW-ASTClaw. This system employs a multi-agent framework adopting a decoupled three-layer architecture (perception-decision-execution) interconnected through the Model Context Protocol (MCP), which addresses real-time adaptive scheduling under complex environmental conditions while achieving high portability: the perception and decision logic are reused unchanged across instruments, requiring only telescope-specific command interfaces to be adapted. Three perception agents-data-quality-agent, cloud-analyzer-agent, and flare-detector-agent-encode senior observer expertise, including wind jitter detection via limb-ring standard deviation, projected-circle zonal cloud analysis, and multi-band active region identification, as LLM-callable rules, while a central reasoning engine performs multi-source fusion and conflict resolution. The system supports graceful degradation from cloud LLM to local inference and finally to rule-based fallback, designed for remote field stations with unstable connectivity. Cross-season validation on archival data demonstrates 100% cloud detection with zero false positives across 10 distinct observation dates, with active-region counts and positions closely matching the NOAA Solar Region Summary (SRS) reports (102 vs. 100 across 10 separate validation dates). These capabilities significantly improve scientific-intent-driven observation accessibility, enable rapid flare response for space weather monitoring, enhance data usability under adverse conditions, and increase observability during partially cloudy periods.

</details>

## 3. Foundation Models for Credit Risk Prediction: A Game Changer?

> 英文原标题：Foundation Models for Credit Risk Prediction: A Game Changer?

- **研究问题：** 这篇论文讨论与“优先权、SLO 与差异化服务”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注付费优先、SLO/截止期、抢占规则和不同等待成本用户的服务分层。
- **作者：** Bart Baesens、Andreas Goethals、Stefan Lessmann、Simon De Vos、Cristián Bravo、David Martens、Victor Medina-Olivares、Christophe Mues 等
- **来源/日期：** arXiv；首次发布 2026-05-18；最近更新 2026-07-15；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2605.18147v2) · [PDF](https://arxiv.org/pdf/2605.18147v2)

<details><summary>英文原摘要（补充）</summary>

Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.

</details>

## 4. Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana

> 英文原标题：Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana

- **研究问题：** 这篇论文讨论与“容量、云资源与服务运营”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注 GPU/云容量配置、资源池化、扩缩容、拥堵和服务能力投资。
- **作者：** Shunbao Li、Zhipeng Yuan、Amoako Ofori、Benedicta Y. Fosu-Mensah、Yang Li、Manu Kenchappa Junjanna、Qing Xue、Po Yang
- **来源/日期：** arXiv；2026-07-15；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.13934v1) · [PDF](https://arxiv.org/pdf/2607.13934v1)

<details><summary>英文原摘要（补充）</summary>

Large language models are increasingly deployed in agricultural decision-support settings, yet high-stakes crop protection in smallholder agriculture requires more than output-quality benchmarks. Over a two-year design and evaluation programme, we formalise policy-constrained large language model assessment as an adaptive compute allocation problem that jointly captures safety compliance, helpfulness, operational latency, and expert supervision workload. We introduce P-EVAL (Policy-grounded Expert-calibrated VALidation protocol), a unified evaluation framework for policy-grounded decision support, evaluating the architecture on a simulated field query database consisting of 1,240 cases. The protocol is instantiated on the Pezego advisory architecture (Pezego-HITL) and evaluated in Ghana. Following offline judge calibration against gold-standard human expert decisions ($κ= 0.77$), we evaluate the architectural performance under simulated query workloads. Under P-EVAL, our memory-routed architecture improves the Policy Alignment Rate (PAR) to 0.94 and the Agronomic Utility Rate (AUR) to 0.95, while reducing P95 latency by 55% (from 28.6s to 12.9s) through a 59.6% cache reuse ratio. We also demonstrate generalisability using the open-source \texttt{Qwen3.5-9B-DeepSeek-V4-Flash} model, achieving a PAR of 0.86 and a 54.5% latency reduction (to 10.2s). To evaluate practical utility and socio-technical integration, we administer detailed questionnaires to Ghanaian Extension Services Officers ($N=30$) and smallholder farmers ($N=36$). Taken together, this work demonstrates how policy-grounded structured retrieval-augmented generation with validated-memory routing makes safety-utility-latency trade-offs explicit, offering a scalable template for trustworthy AI-driven extension in smallholder farming systems.

</details>

## 5. NNStar: An end-to-end AI agent for nuclear matter and neutron star physics

> 英文原标题：NNStar: An end-to-end AI agent for nuclear matter and neutron star physics

- **研究问题：** 这篇论文讨论与“平台经济、市场设计与竞争”相关的什么问题，以及它如何影响 LLM 服务系统的运营表现？
- **文章怎么做：** 当前数据源仅提供英文题录或摘要，尚未生成可靠的中文全文模型解读；自动报告不会据此虚构模型、公式或结论。
- **研究启示：** 关注模型供应商、平台和用户之间的定价、竞争、筛选与激励相容。
- **作者：** Yao Ma、Yong-Liang Ma、Jia-Ying Xiong
- **来源/日期：** arXiv；2026-07-15；arXiv
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
- **链接：** [论文页](http://arxiv.org/abs/2607.13930v1) · [PDF](https://arxiv.org/pdf/2607.13930v1)

<details><summary>英文原摘要（补充）</summary>

Constraining the equation of state of dense matter requires confronting effective models with massive data that spans many orders of magnitude in scale, from sub-saturation nuclear matter properties to the masses, radii, and tidal deformabilities of neutron stars. Exploring the high-dimensional coupling space of such a model and fine tuning it against all of these constraints is a labor- and time-intensive task. We present \textsc{NNStar}, an end-to-end artificial-intelligence agent that automates this workflow. Rather than a bespoke application, \textsc{NNStar} is delivered as a portable \emph{skill} for an open large-language-model (LLM) agent platform -- a self-describing module that pairs worked usage conventions with symbolic and numerical physics engines that (i) build a relativistic mean-field model directly from a Lagrangian, (ii) solve the mean-field equations of motion and evaluate the saturation properties, (iii) construct the $β$-equilibrium equation of state, splice it to a crust, and integrate the Tolman--Oppenheimer--Volkoff equations, and (iv) score the resulting predictions through a Bayesian joint analysis against nuclear matter and astrophysical observations. The agent can read a model, fit its parameters, and report the full set of nuclear matter and neutron star observables without human intervention. \textsc{NNStar} therefore provides a new, AI-driven framework for analyzing nuclear matter and neutron-star observations.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
