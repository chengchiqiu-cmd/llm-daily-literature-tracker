# 2026-08-28 LLM 服务系统每日文献简报

> 检索窗口：2026-08-27 至 2026-08-28（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 法律法师可以设计接近最佳的OR算法

> 英文原标题：LLMs Can Design Near-Optimal OR Algorithms

- **作者：** Jackie Baek
- **来源/日期：** arXiv；2026-08-27；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2608.27296v1) · [PDF](https://arxiv.org/pdf/2608.27296v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、queueing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

我们询问大型语言模型 (LLM) 是否能够为精确的操作研究 (OR) 问题设计有效的算法. 我们研究库存控制,排队网络控制和各种优化. 我们评估了两个级别的LLM使用:在1级,模型接收了一个问题实例,并返回该实例的解决方案;在2级,它只接收问题类描述和广泛的参数范围,并返回一个算法,将实例参数映射到解决方案. 人类输入是最小的:我们给了一个未调整的提示来描述问题,模型可以访问一个有固定计算预算的Python沙箱工具.我们测试的最强的模型,gpt-5.6-sol,几乎在所有评估实例上都匹配或优于现有的最佳方法.即使在2级,返回的算法在看到评估实例之前都固定. 在不到八个月间隔发布的模型中,性能也大幅提高,这表明这种能力正在迅速发展.因此,对于我们研究的精确操作问题,单个未调整的LLM查询已经可以产生与专业方法竞争的算法. 这些结果表明,边界LLM可以成为精确的OR问题中的算法设计的严实验基线.

### 英文原摘要

We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment optimization. We evaluate two levels of LLM use: at level 1, the model receives one problem instance and returns a solution for that instance; at level 2, it receives only the problem class description and broad parameter ranges, and returns an algorithm that maps instance parameters to solutions. Human input is minimal: we give one untuned prompt that describes the problem, and the model has access to a Python sandbox tool with a fixed compute budget. The strongest model we test, gpt-5.6-sol, matches or outperforms the best existing method on almost all evaluated instances. This holds even at level 2, where the returned algorithm is fixed before seeing the evaluation instances. Performance also improves sharply across models released less than eight months apart, suggesting that this capability is moving quickly. Thus, for the well-specified operations problems we study, a single untuned LLM query can already produce algorithms competitive with specialized methods. These results suggest that frontier LLMs can be a serious empirical baseline for algorithm design in well-specified OR problems.

## 2. 全球南方的算法公平感知:孟加拉国关于骑车共享,美容过器和大型车辆的证据

> 英文原标题：Algorithmic Fairness Perceptions in the Global South: Evidence from Bangladesh on Ride-Sharing, Beauty Filters, and Large

- **作者：** Ahmed Abdal Shafi Rasel、Ahmed Mustafa Amlan、Tasmim Shajahan Mim
- **来源/日期：** arXiv；首次发布 2025-08-07；最近更新 2026-08-27；arXiv
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2508.05281v2) · [PDF](https://arxiv.org/pdf/2508.05281v2)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、llm、pricing。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

算法公平性研究几乎完全来自北美和西欧,所以我们对人们在其他地方如何评判他们已经每天依赖的算法所知甚少. 我们直接询问孟加拉人:一项双语 (孟加拉语和英语) 的调查对199名参与者进行了三种日常情景中的公平评价 - - 乘坐共享的价格随着环境而变化,人工智能的美容过器重塑外观, 环境改变了判决,即使结果没有:在医疗紧急情况下,价格上20%似乎不太公平,而在休旅行中同样上 (2.00vs2.17在5点尺度上,威尔科森p=0.006),在收入群体中 (中等收入参与者中最大).人们已经看到了上价格的批评;环境加剧了判断,而不是创造它. 要求透明度,同意和真正的用户控制几乎是普遍的:85.7%到90.3%的参与者想要这些保护, 美容过器的伤害轨迹与自我形象比社会压力更容易命名;个人影响的感觉预测减少了自信 (R^2 = .30,p < .001),尽管尺度的方向是从文本中推断而不是通过标记的标保证. 在那些注意到LLM文化偏见的参与者中,许多人无法解释为什么被要求详细阐述 - - 识别偏见和能够阐述它是不同的技能.

### 英文原摘要

Algorithmic fairness research comes almost entirely out of North America and Western Europe, so we know little about how people elsewhere judge the algorithms they already rely on every day. We asked people in Bangladesh directly: a bilingual (Bangla and English) survey of 199 participants rated fairness across three everyday scenarios -- ride-sharing prices that shift with context, AI beauty filters that reshape appearance, and large language models that handle cultural values differently than a human would. Four patterns stood out. Context changes the verdict even when the outcome doesn't: a 20% price surge during a medical emergency feels less fair than the identical surge on a casual trip (2.00 vs. 2.17 on a 5-point scale, Wilcoxon p = .006), a small effect uneven across income groups (largest among middle-income participants). People already view surge pricing critically in general; context sharpens the judgment rather than creating it. Demand for transparency, consent, and real user control is close to universal: 85.7% to 90.3% of participants want these protections regardless of gender, income, or prior awareness of algorithmic bias. Beauty-filter harm tracks with self-image more than with social pressure people can easily name; feeling personally affected predicts reduced self-confidence tightly (R^2 = .30, p < .001), though the scale's direction is inferred from context rather than guaranteed by labeled anchors. And among participants who noticed specific instances of LLM cultural bias, many could not say why when asked to elaborate -- recognizing bias and being able to articulate it are different skills. Outcome-only fairness metrics would miss every one of these patterns.

## 3. 驾驶人工智能基础设施繁荣:政策支持韩国电力设备出口第二次增长

> 英文原标题：Riding the AI Infrastructure Boom: Policy Support for a Second Surge in Korea's Power Equipment Exports

- **作者：** Sungjin Kim
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-27；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7353539) · [DOI](https://doi.org/10.2139/ssrn.7353539)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、tariff。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工智能 (AI) 的快速扩散导致了超级规模数据中心投资的激增,这种激增与美国老龄化电网的需要相结合.它们一起推动了电力设备的需求:变压器,电缆,开关设备和分销板. 据预测,全球电力设备市场将从2025年的780亿美元扩大到2031年的1.23万亿美元,每年平均增长约7.9%.随着欧洲领先的制造商的供应瓶持续存在,韩国企业正在成为交付时间强度的关键参与者. 韩国电力设备行业由大型专业制造商领导,其中包括HDHyundai Electric,LS ELECTRIC和Hyosung Heavy Industries,该行业的主要产品出口从2022年到2025年以23.7%的复合年率增长. 在美国进口市场上,韩国在高压电缆和超高压变压器中排名第一,这证明了上游电力基础设施设备的强竞争力.韩国在电力分配板 (PDU) 中排名第七,这是一个具有高附加价值的产品,这使得在价值链上进行多样化成为一个突出任务. 转换该行业目前的势头为可持续的竞争力将需要集中在三个结构性弱点上的政策支持:通过扩大美国国内生产基地来管理关税风险,进一步推动高附加价值的分销板和PDU市场,以及对关键原材料的供应链的多元化. 这篇论文是用克劳德·奥普斯5大语言模型从原始韩语中翻译的.

### 英文原摘要

The rapid spread of generative artificial intelligence (AI) has driven a surge in hyperscale data center investment, and that surge has converged with the need to replace an aging power grid in the United States. Together they are pushing up demand for power equipment: transformers, power cables, switchgear, and distribution boards. The global power equipment market is projected to expand from about USD 780 billion in 2025 to USD 1.23 trillion by 2031, growing at an average of roughly 7.9 percent a year. With supply bottlenecks at Europe's leading manufacturers persisting, Korean firms are emerging as key players on the strength of their delivery times. Korea's power equipment industry is led by large specialist manufacturers, among them HD Hyundai Electric, LS ELECTRIC, and Hyosung Heavy Industries, and exports of the industry's main products grew at a compound annual rate of 23.7 percent from 2022 to 2025. In the US import market, Korea ranks first in high-voltage power cables and second in extra-high-voltage transformers, evidence of strong competitiveness in upstream power infrastructure equipment. Korea ranks only seventh, however, in power distribution boards (PDUs), a high-value-added product, which leaves diversification along the value chain as an outstanding task. Converting the industry's current momentum into durable competitiveness will require policy support concentrated on three structural weaknesses: managing tariff risks by expanding production bases inside the United States, pushing further into the high-value-added distribution board and PDU market, and diversifying supply chains for critical raw materials. This paper was translated from the original Korean using the Claude Opus 5 large language model. It was reviewed by an editor and the author prior to publication.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
