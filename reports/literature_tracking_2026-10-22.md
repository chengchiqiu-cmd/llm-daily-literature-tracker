# 2026-10-22 LLM 服务系统每日文献简报

> 检索窗口：2026-10-21 至 2026-10-22（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 谁支付人工智能?工作,家庭预算和订阅需求

> 英文原标题：Who Pays for Generative AI? Work, Household Budgets, and Subscription Demand

- **作者：** Fuli Yang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-21；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7643078) · [DOI](https://doi.org/10.2139/ssrn.7643078)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 generative ai、subscription。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

个人对生成人工智能的需求将工作场所的采用与家庭预算联系起来.我们在韩国11个每周的消费者观察调查中研究了这种联系,其中包括8,800份记录和4440个主要职业样本. 在调整人口统计,职业,企业规模,工作场所政策和使用频率之后,混合用途差异在九波中以11.3个百分点与无工作用途相比和8.5个百分点与无个人用途相比复制. 货币排名也在整体职业样本中保持在变量调整和每次可接受的不完整数额完成后:在KRW10,000,后波混合用途差异在下面有4.2和2.6分的界限.确认订阅支出记录集中在工作用户中,他们占这些记录的92.2%而比较的核心样本的73.8%. 一个净价值框架解释了各个目的之间的好处如何进入个人预算与自由和组织替代方案相比.这些发现确定了目的宽度作为人工智能融资需求的实质性维度,并将家庭预算决策与组织的采用放在一起,解释了付费市场的形成.

### 英文原摘要

Personal demand for generative AI connects workplace adoption to household budgets. We study this connection in eleven weekly ConsumerInsight surveys from South Korea, comprising 8,800 records and a main occupational sample of 4,440. Joint work and personal use is associated with substantially more widespread willingness to allocate a monthly AI budget. After adjustment for demographics, occupation, firm size, workplace policy and use frequency, the mixed-use differences reproduce in nine later waves at 11.3 percentage points relative to no work use and 8.5 points relative to work without personal use. A seven-configuration decomposition shows a further 4.6-point difference when study joins work and personal uses. The monetary ranking also holds in the full occupational sample after covariate adjustment and every admissible completion of incomplete amounts: at KRW 10,000, the later-wave mixed-use differences are bounded below by 4.2 and 2.6 points. Affirmative subscription-expenditure records are concentrated among work users, who account for 92.2% of these records against 73.8% of the comparable core sample. A net-value framework explains how benefits across purposes enter personal budgets relative to free and organizational alternatives. The findings establish purpose breadth as a substantial dimension of AI financing demand and place household budget decisions alongside organizational adoption in explaining the formation of a paying market.

## 2. 在经典经济游戏中,异性跨家庭LLM代理.

> 英文原标题：When Do Language Models Reach Nash? Heterogeneous Cross-Family LLM Agents in Classic Economic Games.

- **作者：** Alexandra Bernadotte、Ivan Menshikov
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-21；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7637178) · [DOI](https://doi.org/10.2139/ssrn.7637178)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 llm、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工代理是否达到经济游戏的纳什平衡已成为算法市场和多代理人工智能的一个负担性的问题.现有的文献建立了一个强有力的对一种行为是肯定的,默默的勾结在竞争基准上,同时绘制了一个混合的图像. 我们认为,更有用的问题不是是否,而是什么时候语言模型能到达纳什, 通过使用一种异质,跨机器的测试床,其中来自三个不同的模型家族 (Qwen 3.6, Gemma 4, Nemotron 3) 的代理人在两个物理服务器上互动,我们运行了三个经典的游戏, 我们发现一个一致的模式:当决策缩小到选择给定的收益数组中最低的选择时,代理人只能复制准确的纳什平衡 (Bress游戏带有明确的选项成本,其中悖论平衡被恢复到单元),而每项任务都需要真正的战略推理, 实际上,这种方法是从成本公式中得到的,而是通过记忆或社会论来得到的,这种论从平衡中偏离,有时是灾难性的. 一个简单的污染探测器,扭转了美丽竞赛参数,使平衡从0转到100, 重要的是,异质的跨家庭互动表现出在自动游戏中看不见的战略不对称性:Gemma 4执行了教科书终端游戏叛逃,并在囚犯困境中利用一个信任的Qwen,而Qwen在拥堵游戏中排除了Gemma和Nemotron. 我们将正常化可利用性 ( ε - Nash) 作为主要的指标,并确定了四种未被探索的测量仪器,替代 (非互动) 控制,作为平衡标志的输出空间融合,真正的跨家庭异质性和人类+AI神经共同测量, 所有的结果都是试点规模的,旨在作为概念证明和方法架,而不是最终的基准.

### 英文原摘要

Whether artificial agents reach the Nash equilibrium of an economic game has become a load-bearing question for algorithmic markets and multi-agent AI. The existing literature establishes a robust yes for one behaviour, tacit collusion above the competitive benchmark, while painting a mixed picture for equilibrium play in general. We argue the more useful question is not whether but when language models reach Nash, and what instrument detects it. Using a heterogeneous, cross-machine testbed in which agents drawn from three distinct model families (Qwen 3.6, Gemma 4, Nemotron 3) interact across two physical servers, we run three classic games with analytically known equilibria: the p -beauty contest, the iterated Prisoner’s Dilemma, and a Braess-paradox routing game. We find a consistent pattern: agents reproduce the exact Nash equilibrium only when the decision reduces to selecting the lowest of a set of given payoffs (the Braess game with explicit option costs, where the paradoxical equilibrium is recovered to the unit), whereas every task demanding genuine strategic reasoning, level- k depth in the beauty contest, backward induction in the Prisoner’s Dilemma, or computing congestion from cost formulas, is met instead with a memorized or social heuristic that diverges from equilibrium, sometimes catastrophically. A simple contamination probe , inverting the beauty-contest parameter so the equilibrium moves from 0 to 100 , exposes the apparent equilibrium “success” of the standard game as template recall: agents move in the wrong direction. Crucially, heterogeneous cross-family interaction surfaces strategic asymmetries that are invisible under self-play: Gemma 4 performs textbook end-game defection and exploits a trusting Qwen in the Prisoner’s Dilemma, while Qwen out-routes Gemma and Nemotron in the congestion game. We adopt normalized exploitability ( ε -Nash) as the primary metric, and we identify four under-explored measurement instruments, surrogate (non-interacting) controls, output-space convergence as an equilibrium signature, true cross-family heterogeneity, and human+AI neural co-measurement, as the open ground this testbed is built to claim. All results are pilot-scale and intended as a proof of concept and a methodological scaffold rather than a definitive benchmark.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
