# 2026-10-23 LLM 服务系统每日文献简报

> 检索窗口：2026-10-22 至 2026-10-23（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 以语言模型和视觉特征为例的房价:来自北克房地产列表的证据

> 英文原标题：Hedonic House Pricing with Language-Model and Vision Features: Evidence from Quebec Real-Estate Listings

- **作者：** Simon-Pierre Boucher
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-22；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7651058) · [DOI](https://doi.org/10.2139/ssrn.7651058)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、pricing。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

分析师可以测量的特征限制了希多尼的房价模型,但房子价值的大部分都仅记录在其清单的自由文本描述和照片中. 我们将通用人工智能模型视为一种功能工程技术:一个大型语言模型将每个描述转化为结构性属性规格,而一个视觉语言模型将面议照片转化为视觉属性, 使用19123个北克房地产列表,两层人工智能将已经丰富的日志直线性性规格的R^2从0.717提高到0.755,从面议照片中获得的3.8个点中的3.0,并将每个估计器的R^2从OLS提高到梯度增强和神经网络 (最佳组合:R^2为0.779,平均绝对错误14.0%). 视觉层比从OLS转向随机森林更为增强了线性模型. 提取的属性具有经济合理的隐含价格2.3%每个门点,34%用于或石头面议存活于市政集群推断,集群启动,邮政代码固定效果,以及对描述语言的控制,这本身为英语列表带来了7%的条件溢价. 我们还记录了销售按所有者描述的嵌入要求价格,所以文本层的收益仅在经纪平台上是可信的,

### 英文原摘要

Hedonic house-price models are bounded by the characteristics an analyst can measure, yet much of a home's value is recorded only in the free-text description and photographs of its listing. We treat general-purpose AI models as a feature-engineering technology for hedonic analysis: a large language model converts each description into structured property specifications, and a vision–language model converts the façade photograph into visual attributes, both under strict JSON schemas that make the outputs auditable econometric variables. Using 19,123 Quebec house listings, the two AI layers raise the R^2 of an already rich log-linear hedonic specification with municipality fixed effects from 0.717 to 0.755, 3.0 of the 3.8 points coming from the façade photograph, and they raise the out-of-sample R^2 of every estimator from OLS to gradient boosting and neural networks (best ensemble: R^2 of 0.779, median absolute error 14.0%). The vision layer adds more to the linear model than switching from OLS to a random forest does. The extracted attributes carry economically sensible implicit prices—2.3% per point of curb appeal, 3–4% for brick or stone façades—that survive municipality-clustered inference, a cluster bootstrap, postal-code fixed effects, and a control for the language of the description, which itself carries a 7% conditional premium for English listings. We also document that for-sale-by-owner descriptions embed the asking price, so that the text layer's gain is credible only on the brokered platform, and that spatially grouped cross-validation lowers all accuracy levels by three to five points while preserving the AI increments.

## 2. 推理深度作为生成人工智能中可变的决定

> 英文原标题：Reasoning Depth As A Decision Variable in Generative AI

- **作者：** Rosario Milelli
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-22；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7657598) · [DOI](https://doi.org/10.2139/ssrn.7657598)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 generative ai、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在2026年NFLPick'em研究中出现了一个意想不到的方法问题:在ChatGPT中选择的推理水平可能会显著改变人工智能生成决策的结构,即使基本的建议基本保持不变.一项7周的侧实验比较了使用高,中和即时推理的三个独立的ChatGPT运行. 每个比赛都是在其他比赛的几秒钟内进行的,基本上使用相同的简单指令:在第7周的NFL选项中进行选项,并根据信心排名球队.结果令人惊叹.这三个配置在14场比赛中的13场比赛中同意了赢家,这表明了第一级选项的实质性稳定.然而,他们的信心排名明显不同. 堪萨斯城分别排名为12,1和2;达拉斯1,11和10;克利夫兰11,4和1;休斯顿分别排名为7,12和14在高,中等和瞬间.该模式反映了独立的AI指数股票选择实验中的早期观察,其中推理深度显著改变了投资组合权重.在这种比较中,30个道斯组件中19个重量不同. 在这两个领域中,出现了相同的结构问题:推理深度可能会比选择更强烈地影响分配.这还没有证明推理深度本身是导致差异的原因.自然使用实验还允许推理配置在搜索宽度,信息选择,证据权重和 Stochastic 路径上有所不同. 它确立的是,即使标题选择基本保持稳定,用户面向的配置变化也可能与信任或分配的重大变化相吻合.临时跨域假设 AI 推理深度可能对分配决策 - - 信任,资本,优先级或风险权重产生更大的影响,而不是对分类选择本身.

### 英文原摘要

An unexpected methodological issue emerged during the 2026 NFL Pick'em study: the reasoning level selected in ChatGPT may materially alter the structure of an AI-generated decision even when the basic recommendation remains largely unchanged. A Week 7 side experiment compared three independent ChatGPT runs using High, Medium, and Instant reasoning. Each run was conducted in a fresh chat, within seconds of the others, using essentially the same simple instruction: make the Week 7 NFL Pick'em selections and rank the teams by confidence. The result was striking. The three configurations agreed on the winner in 13 of 14 games, suggesting substantial stability in first-order selection. Yet their confidence rankings differed dramatically. Kansas City was ranked 12, 1, and 2; Dallas 1, 11, and 10; Cleveland 11, 4, and 1; and Houston 7, 12, and 14 across High, Medium, and Instant respectively. The pattern mirrors an earlier observation in the separate AI Index stock-selection experiment, where reasoning depth materially changed portfolio weighting. In that comparison, 19 of the 30 Dow Jones component weights differed. Across the two domains, the same structural question appears: reasoning depth may affect allocation more strongly than selection. This does not yet establish that reasoning depth alone caused the differences. The natural-use experiment also allowed the reasoning configurations to differ in search breadth, information selection, evidence weighting, and stochastic path. What it does establish is that a user-facing configuration change can coincide with large changes in confidence or allocation even when headline choices remain mostly stable. Provisional cross-domain hypothesis AI reasoning depth may have a larger effect on allocation decisions-confidence, capital, priority, or risk weighting-than on categorical selections themselves.

## 3. 法学院测试时间计算的Pareto Frontier:在代币预算下进行适应性推广和投票

> 英文原标题：Pareto Frontier of LLM Test-Time Compute: Adaptive Rollouts and Voting under Token Budgets

- **作者：** Zhenyu Wang、Xiaozhi Zhu、Yifan Hu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-22；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7650878) · [DOI](https://doi.org/10.2139/ssrn.7650878)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、budget constraint。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型通过生成多个推出和汇总这些答案来提高测试时间精度.随着生成额外的推出消耗更多的代币,测试时间计算面临基本的成本精度交易,自然会提出问题:鉴于固定的代币预算,如何分配预算以最大限度地提高精度? 现有的方法通常适应每个查询的推广数量,同时保持了投票规则的固定性,即将生成的推广集成到最终答案的规则. 由于不同的投票规则可以有利于不同的查询,并引发不同的精度上限,我们表明投票规则本身也应该适应各种查询. 特别是常用的固定的投票规则,如自相一致性和最好的n,是统一的博尔茨曼权重投票家族的特殊案例, 参数为尺度 τ ≥ 0. 因此, 在代币预算限制下,我们制定了一个适应性查询依赖于联合推广数量和投票规则的选择. 我们表明,在各预算中没有固定投票规则是均的最佳的,而适应性推广和投票产生的成本准确性Pareto边界,它占据了每个固定投票规则的边界. 基于这些结构性结果,我们提出PRICE (Priced Rollouts and Inference-time voting-rule Choice under a token budgetEt),是一个实用算法,该算法在代币预算下实现了适应性,查询级的联合决策.在 MATH-500 上,PRICE在所有评估预算中始终超过了六个测试时间计算基线,并通过使用2.8-3.5×更少的代币实现了相对准确性.

### 英文原摘要

Large language models improve test-time accuracy by generating multiple rollouts and aggregating these answers. As generating additional rollouts consumes more tokens, test-time compute faces a fundamental cost accuracy trade-off, naturally raising the question: given a fixed token budget, how to allocate the budget to maximize accuracy? Existing approaches typically adapt the number of rollouts for each query while keeping the voting rule fixed, i.e., the rule used to aggregate the generated rollouts into a final answer. As different voting rules can favor different queries and induce different accuracy ceilings, we show that the voting rule itself should also adapt across queries. In particular, commonly used fixed voting rules such as self-consistency and best-of-n are special cases of a unified Boltzmann-weighted vote family, parameterized by a scalar τ ≥ 0. We therefore formulate an adaptive query dependent choice of jointly the number of rollouts and the voting rule under a token-budget constraint. We show that no fixed voting rule is uniformly optimal across budgets, whereas adaptive rollout and voting yields a cost-accuracy Pareto frontier that dominates every fixed voting rule's frontier. We further characterize the large-budget asymptotics of this Pareto frontier, identifying both its attainable accuracy ceiling with an unlimited budget, and the convergence rate to the ceiling as the token budget grows. Building on these structural results, we propose PRICE (Priced Rollouts and Inference-time voting-rule Choice under a token budgEt), a practical algorithm that implements the adaptive, query-level joint decisions under a token budget. On MATH-500, PRICE consistently outperforms six test-time compute baselines across all evaluated budgets and achieves comparable accuracy using 2.8-3.5× fewer tokens.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
