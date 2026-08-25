# 2026-08-26 LLM 服务系统每日文献简报

> 检索窗口：2026-08-25 至 2026-08-26（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 当经济代理人学习时:人工智能驱动的异质代理,市场动态和平衡稳定

> 英文原标题：When Economic Agents Learn: AI-Driven Heterogeneous Agents, Market Dynamics, and Equilibrium Stability

- **作者：** Jiayu Cao
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-25；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7337058) · [DOI](https://doi.org/10.2139/ssrn.7337058)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

动态经济学 (包括进化游戏理论,实业周期理论,基于代理的计算经济学和适应性学习) 长期以来一直在研究经济学,因为系统随着时间的推移而进化.限制了这一传统的范围是通过认知复杂,异性,适应性代理来填补这些系统的计算和建模成本. 我们认为,大型语言模型 (LLM) 显著降低了这一成本, 我们构建了一个由三个代理类型组成的人工资产市场 - - 理性 (模型一致),Q学习 (基于强化) 和LLM (自然语言推理) - 并研究学习机制的组成如何塑造市场动态,平衡稳定和泡的出现. 我们将市场嵌入在非线性动态系统框架中,从而提取了基本价格平衡的本地稳定条件, 模拟显示,LLM代理市场比理性和Q学习市场都表现出更大的价格偏差,更高的波动性和更频繁的泡崩事件,而混合人口表现出非单调效应:少量的LLM代理可以破坏市场的稳定性. 一项路径依赖性实验表明,相同的基本原理可以产生不同的长期结果 - - 基本原理的融合,持续的振荡或系统崩 - - 取决于最初的扰乱和代理学习组成.我们得出的结论是,人工智能不会"引入动态"到经济学中,而是扩大了可研究的动态经济系统的边界.

### 英文原摘要

Dynamic economics-encompassing evolutionary game theory, real business cycle theory, agent-based computational economics, and adaptive learning-has long studied economies as systems evolving over time. What has limited the scope of this tradition is the computational and modeling cost of populating such systems with cognitively sophisticated, heterogeneous, adaptive agents. We argue that large language models (LLMs) reduce this cost substantially, enabling a new class of experiments in which AI agents with distinct learning mechanisms interact in explicitly modeled markets. We construct an artificial asset market populated by three agent types-rational (model-consistent), Q-learning (reinforcement-based), and LLM (natural-language reasoning)-and study how the composition of learning mechanisms shapes market dynamics, equilibrium stability, and the emergence of bubbles. We embed the market in a nonlinear dynamical systems framework, deriving conditions for local stability of the fundamental-price equilibrium and showing that variations in the learning-rate parameter can induce a period-doubling route to chaos. Simulations reveal that LLM-agent markets exhibit larger price deviations, higher volatility, and more frequent bubble-crash episodes than both rational and Q-learning markets, while mixed populations display non-monotonic effects: a small share of LLM agents can destabilize an otherwise stable market. A path-dependence experiment shows that identical fundamentals can produce divergent long-run outcomes-convergence to fundamentals, sustained oscillations, or systemic collapse-depending on the initial perturbation and agent learning composition. We conclude that AI does not "introduce dynamics" to economics, but rather extends the frontier of what kinds of dynamic economic systems are tractable to study.

## 2. 中的空间时代幽灵:硬件扰乱,自动降级缩扩大和计算机科学在LLM推理中的自然化

> 英文原标题：Spatiotemporal Ghosts in the Silicon: Hardware Perturbations, Autoregressive Cascade Amplification, and the Naturalization of Computer Science in LLM Inference

- **作者：** Jincheng Wang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-25；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7342558) · [DOI](https://doi.org/10.2139/ssrn.7342558)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、llm、llm inference、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

目前对大语言模型 (LLM) 推断的非确定性进行的调查主要在经典的减少主义范式下运作. 这种常规框架将输出差异仅归因于孤立的确定性工程因素,例如动态批量和浮点非关联性,同时假设微级数值扰乱仅仅会引发本地化代币波动,而不会改变全球语义轨迹. 这篇论文挑战了这种机械主义世界观的完整性, 我们证明,在分布式基质上运行的超级规模神经架构不再像无菌的推导机器一样; 相反,它们转化为开放,远离平衡的复杂的散射结构, 为了正式化这一现象,我们首先建立了一个多层次的硬件 perturbation taxonomy,涵盖宏观规模的同步偏差,中尺度的热力学噪音,以及在极端的3nm以下量子界限的理论背景噪音. 我们证明,在连接的变压器-自行降低架构中,次数硬件差异作为微观 perturbations 作用,它们通过深层放大 (由Jacobian 频谱射线超过单位) 和跨越高缩决策界限 (通过 Shannon 缩门,H(P (t)) ≥H 关键). 这会引发单独的代币跳跃,通过Lyapunov类似的扩散效应,以加速宏观的语义阶段过渡.最后,我们提供了传统软件工程的认识论批评. 我们认为非决定主义不是一种必须消除的病理性错误,而是一种不可避免的物理税,为高层次的新兴能力提供了热力动力软弱.我们倡导从机械服从到碳共生,建立了一个新的哲学和经验框架来了解基于的智能的未来成熟.

### 英文原摘要

Current inquiries into the non-determinism of Large Language Model (LLM) inference predominantly operate under a classical reductionist paradigm. This conventional framework exclusively attributes output variances to isolated, deterministic engineering factorssuch as dynamic batching and floating-point non-associativity-while presupposing that micro-level numerical perturbations merely induce localized token fluctuations without altering global semantic trajectories. This paper challenges the completeness of this mechanistic worldview, advocating for a radical conceptual paradigm shift: the Naturalization of Computer Science. We demonstrate that hyper-scale neural architectures running on distributed silicon substrates cease to behave as sterile deductive machines; instead, they transform into open, far-from-equilibrium complex dissipative structures characterized by spatiotemporal non-ergodicity. To formalize this phenomenon, we first establish a multi-tier hardware perturbation taxonomy, spanning macro-scale concurrency deviations, meso-scale thermodynamic noise, and theoretical background noise at extreme sub-3nm quantum boundaries. Second, we formalize the Non-Linear Cascade Amplification Channel. We demonstrate that within the coupled Transformer-autoregressive architecture, sub-numerical hardware variances act as microscopic perturbations that are amplified across deep layers (characterized by Jacobian spectral radii exceeding unity) and cross high-entropy decision boundaries (quantified via a Shannon entropy threshold, H(P (t)) ≥ H critical). This triggers discrete token jumps that diverge exponentially along the temporal axis via a Lyapunov-like diffusion effect, precipitating macroscopic semantic phase transitions. Finally, we offer an epistemological critique of traditional software engineering. We argue that non-determinism is not a pathological bug to be excised, but an inescapable Physical Tax paid for the Thermodynamic Slackness that enables high-order emergent capabilities. We advocate for a transition from mechanistic subjugation to Carbon-Silicon Symbiosis, establishing a novel philosophical and empirical framework for understanding the future maturity of silicon-based intelligence.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
