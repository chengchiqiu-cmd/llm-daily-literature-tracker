# 2026-11-19 LLM 服务系统每日文献简报

> 检索窗口：2026-11-18 至 2026-11-19（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 经过LLM指导的运输中心能力规划与文本业务输入

> 英文原标题：LLM-guided Transportation Hub Capacity Planning with Textual Business Inputs

- **作者：** Xiaoyue Liu、Zheng Dong
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-18；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7699780) · [DOI](https://doi.org/10.2139/ssrn.7699780)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、llm、capacity planning、capacity。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

虽然传统的枢纽能力规划模型对量化输入进行有效优化,但它们往往无法消化质量业务背景. 我们提出了一个新的框架,其中一个大型语言模型 (LLM) 代理通过自然语言的业务环境描述来反复提出枢纽能力决策. 主要机制是思想链推理协议:LLM构建了一个结构化的决策表,根据变化的暗示方向和大小将每个文本项目映射到特定的容量调整.新容量决策随后通过一个反循环进行验证,采用优化模型,该循环提供基于路由的性能指标来指导代理人的选择. 在美国东南部的现实13枢纽货运网络上,我们的框架实现了与隐藏的地面真相相相比2.8%的优化差距,这是传统优化模型没有文本业务输入产生的11.0%的差距相比的显著改善.这表明LLM可以作为一个文本桥梁,将质量业务见解集成到运营研究工作流程中.

### 英文原摘要

While traditional hub capacity planning models optimize effectively for quantitative inputs, they often fail to digest qualitative business context. We propose a novel framework where a large language model (LLM) agent iteratively proposes hub capacity decisions guided by natural-language business context descriptions. The key mechanism is a chain-of-thought reasoning protocol: the LLM constructs a structured decision table that maps each contextual item to specific capacity adjustments based on the implied direction and magnitude of changes. The new capacity decision is then validated through a feedback loop with an optimization model, which provides routing-based performance metrics to guide the agent's selection. On a real-world 13-hub freight network in the southeastern US, our framework achieves a 2.8% optimality gap relative to the hidden ground-truth, a significant improvement over the 11.0% gap produced by the traditional optimization model without textual business inputs. This demonstrates that LLMs can serve as a contextual bridge, integrating qualitative business insights into Operations Research workflows.

## 2. 规范基于LLM的升级估计的治疗泄漏

> 英文原标题：Regularizing Treatment Leakage for LLM-based Uplift Estimation

- **作者：** Bojing Feng、Jinqiu Deng、Zihan Hong、Yuan Xue、Wenqi Xiang、Shuhan Wang、Feng Xiao、Shiwei Wang 等
- **来源/日期：** arXiv；首次发布 2026-11-16；最近更新 2026-11-18；arXiv
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2611.20794v3) · [PDF](https://arxiv.org/pdf/2611.20794v3)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、llm、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 为升级估计提供语义特性,但治疗揭示文本可以导致预测快捷径,而不会转移到部署.我们建议基于LLM的升级泄漏规范化 (LULR) 来应对这种风险. 随着LLM编码器被结,LULR处罚了因果标题的可训练共享表示和治疗之间的依赖,同时保留了单独的结果标题.该处罚使用了对相互信息的对比日志比上限 (CLUB) 的变化近似,针对治疗依赖而不是通用参数缩小. 控制代理实验提供了对没有规范化和测试的减重设置的注射治疗信息下改善排名分数的探索性证据.仅结构性基准显示出适度,依赖数据集的效果.在工业定价随机控制试验中,离线升高@0.3为LULR的0.258,而相同的脊柱基线为0.106. 一个单独的一周在线A/B测试显示了完整的部署定价政策的销售量高达5.45%和商品总价值高达1.91%比控制部门.这些短期政策水平的收益并没有隔离调节者的效果.

### 英文原摘要

Large language models (LLMs) provide semantic features for uplift estimation, but treatment-revealing text can induce prediction shortcuts that do not transfer to deployment. We propose LLM-based Uplift Leakage Regularization (LULR) to address this risk. With the LLM encoder frozen, LULR penalizes dependence between the causal head's trainable shared representation and treatment while retaining separate outcome heads. The penalty uses a variational approximation to the contrastive log-ratio upper bound (CLUB) of mutual information, targeting treatment dependence rather than generic parameter shrinkage. Controlled proxy experiments provide exploratory evidence of improved ranking scores under injected treatment information relative to no regularization and the tested weight-decay setting. Structured-only benchmarks show modest, dataset-dependent effects. On an industrial pricing randomized controlled trial, mean offline lift@0.3 is 0.258 for LULR, compared with 0.106 for the same-backbone baseline. A separate one-week online A/B test of the complete deployed pricing policy records 5.45% higher sales volume and 1.91% higher gross merchandise value than the control arm. These short-term policy-level gains do not isolate the regularizer's effect.

## 3. 算法的丰富性:全球动态CGE模型中的生成人工智能,就业和不平等

> 英文原标题：The Wealth of Algorithms: Generative AI, Jobs and Inequality in a Global Dynamic CGE Model

- **作者：** David Radi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-18；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7696925) · [DOI](https://doi.org/10.2139/ssrn.7696925)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 generative ai、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

这篇论文模拟了人工智能如何影响全球经济的就业,工资和不平等.很少有人怀疑它将改变经济,但目前还没有人知道是如何.工人,企业和政府想知道谁的就业和工资将改变,谁将捕获收益和哪些国家将走向前面,在证据能够告诉他们之前. 这篇论文没有试图预测那个未来.它的贡献是理解人工智能的经济影响,它们依赖于什么以及政策的后果的量化框架.我们将人工智能添加到一个全球动态可计算的总平衡 (CGE) 模型中,该模型每年追踪生产,贸易,投资和就业到2040年,在23个地区. 人工智能在每个职业中完成一些任务,使工人在其他职业中更具生产力.当人工智能完成任务时,我们从其劳动力成本的27%节省开始,平均的Acemoglu (2025) 从两个工作场所实验中获取.我们运行了一个中心场景和68种替代方案,这些替代方案不同于人工智能是多快,多广泛采用,成本有多大,它取代了工人,而不是帮助工人,以及劳动力市场如何调整. 人工智能如何变得便宜和有能力,以及企业如何广泛采用它,决定了收益的规模:到2040年,世界GDP将在我们主要场景中 (中央情况下约为7%),在没有人工智能的道路上达到1%至15%.在极端情况下,人工智能变得每年30%更高效 (如果人工智能持续改善但随着时间的推移更缓慢),它将达到35%. 在几乎每一个场景中,大部分收益都归于资本所有者.谁在资本中分享,取决于谁拥有资本,以及人工智能在何种程度上取代而不是帮助工人. 在中央经济体中,资本的世界收入份额增加了4个点左右,公务员的实际工资在大型经济体中大约13至22%低于无人工智能路径,而在富裕经济体中,家庭收入的吉尼系数增加了2到3.5个点左右.如果就业损失持续下去,2040年与无人工智能基线相比的世界增长率将为5.4%而不是6.8%,劳动力收入将在各个地方进一步下降. 根据这些结果,我们然后测试了几种说明性人工智能政策,看看它们如何改变结果及其分布效果. 每个都做着不同的工作:支持改变工作主要保护工人的工资,保持人工智能便宜主要保护产量,仅仅分享人工智能的资本收入显著缩小了不平等. 这些政策是说明性的,并且在模型中很大程度上没有资金,因此他们的收益可能会膨胀.

### 英文原摘要

This paper models how generative artificial intelligence (AI) affects jobs, wages and inequality across the world economy. Few doubt that it will change the economy; what nobody yet knows is how. Workers, firms and governments want to know whose jobs and pay will change, who will capture the gains and which countries will come out ahead, well before the evidence can tell them. This paper does not try to forecast that future. Its contribution is a quantitative framework for understanding what drives AI's economic effects, what they depend on, and what follows for policy. We add AI to a global dynamic computable general equilibrium (CGE) model that tracks production, trade, investment and employment year by year to 2040 in 23 regions. AI does some tasks inside each occupation and makes workers more productive in others. When AI does a task, we start from a 27% saving on its labour cost, the average Acemoglu (2025) draws from two workplace experiments. We run a central scenario and 68 alternatives that vary how fast and how widely AI is adopted, what it costs, how far it replaces rather than helps workers and how labour markets adjust. How cheap and capable AI becomes, and how widely firms adopt it, decide the size of the gain: by 2040 world GDP ends about 1% to 15% above a path without AI in our main scenarios (about 7% in the central case). It reaches about 35% in an extreme case where AI becomes 30% a year more efficient (15 to 25% if AI keeps improving but more slowly over time). Most of the gain goes to owners of capital in almost every scenario. Who shares in it depends on who owns capital and on the extent to which AI replaces rather than helps workers. In the central case capital's share of world income rises by about 4 points, clerks' real pay ends roughly 13 to 22% below the no-AI path in the large economies, and within rich economies the Gini coefficient of household income rises by about 2 to 3.5 points. If job losses last, the world gain against the no-AI baseline in 2040 is 5.4% against 6.8%, and labour income falls further everywhere. Based on these results, we then test several illustrative AI policies to see how they change the outcomes and their distributional effects. Each does a different job: support for changing jobs mainly protects workers' pay, keeping AI cheap mainly protects output, and only sharing AI's capital income narrows inequality noticeably. The policies are illustrative and largely unfunded in the model, so their gains are likely inflated.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
