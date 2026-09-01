# 2026-09-02 LLM 服务系统每日文献简报

> 检索窗口：2026-09-01 至 2026-09-02（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. PRISM:通过智能场景和优先管理进行LLM指导的持续跟踪

> 英文原标题：PRISM: LLM-Guided Persistent Tracking with Intelligent Scene and Priority Management

- **作者：** Chandrakanth Vipparla
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-01；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7387392) · [DOI](https://doi.org/10.2139/ssrn.7387392)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 llm、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

视觉对象跟踪仍然是计算机视觉的核心挑战,单个对象跟踪SOT) 和多对象跟踪 (MOT) 方法主要侧重于在场景内的目标跟踪.然而,这些传统方法在动态的现实环境中有限,目标指定和优先级必须根据不断变化的要求实时适应. 通过克服这些限制,我们推出了一个基于LLM的持续自然语言跟踪网络,称为PRISM,该网络将自然语言处理与视觉跟踪结合起来,以促进动态目标指定和优先级. 拟议的系统利用LLM模型来解释实时自然语言指令,使用中断驱动的机制来处理新的输入,而不妨碍持续的跟踪,并整合了 ದೃಶ್ಯ和语言特征,以实现强和适应的目标定位.这种架构使系统能够指定和启动新物体进入视野时的跟踪. 该算法在多个开源数据集上进行评估,以分析需要实时优先级更改的场景中的动态目标指定和跟踪性能. 基于中断驱动的设计确保了实时用户输入的无整合,允许响应性重定优先,而没有显著的性能损失,从而提高了视觉跟踪系统的灵活性和互动性,并解决了传统跟踪算法的关键局限性.

### 英文原摘要

Visual object tracking remains a core challenge in computer vision, with single object tracking SOT) and multi- object tracking (MOT) methods primarily focusing on tracking targets within a scene. However, these conventional approaches are limited in dynamic, real-world settings where target designation and prioritization must adapt in real time based on evolving requirements. overcome these constraints, we introduce a LLM based persistent natural language tracking network termed ’PRISM’, which fuses natural language processing with visual tracking to facilitate dynamic target designation and prioritization. The proposed system leverages an LLM model to interpret real-time natural language instructions, employs an interrupt- driven mechanism to process new inputs without disrupting ongoing tracking, and integrates visual and linguistic features for robust and adaptive target localization. This architecture enables the system to designate and initiate tracking of new objects as they enter the ﬁeld of view. The algorithm is evaluated on multiple open-source datasets to analyze dynamic target designation and tracking performance in scenarios requiring real-time priority changes. The interrupt-driven design ensures seamless integration of real-time user inputs, allowing responsive re-prioritization without signiﬁcant performance loss, thereby advancing the ﬂexibility and interactivity of visual tracking systems and addressing key limitations of traditional tracking algorithms.

## 2. 人工智能在网上评论中的作用

> 英文原标题：The Role of AI in Online Reviews

- **作者：** Valeria Lerman、Oren Rigbi、Yaniv Dover
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-01；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7374658) · [DOI](https://doi.org/10.2139/ssrn.7374658)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、generative ai。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

快速采用大型语言模型 (LLM) 创造了在线平台上战略内容生成的新机会,包括潜在的有害形式的操纵,可能会破坏平台的有效性和重塑平台动态. 我们引入了一个实验方法,利用不同的LLM供应冲击 - - 模型价格和能力的突然变化,并与未经验证的评论进行对比,以确定与生成人工智能供应改进相关的平台活动的变化. 一个强有力的发现是,在LLLM供应冲击之后,未经验证的评论转向更大的负面性:更多的1星,更少的5星和更低的评级,主要由新型号发布驱动的影响,并集中在具有最低和最高评价量的公司中,这表明战略人工智能使用可能重塑平台竞争动态. 我们进一步发现,LLM的供应冲击会引发短暂,集中的审查活动.

### 英文原摘要

The rapid adoption of large language models (LLMs) creates new opportunities for strategic content generation on online platforms, including potentially harmful forms of manipulation that may undermine platform effectiveness and reshape platform dynamics. However, measuring such activity is difficult because AI-generated content is rarely directly observable. We introduce an empirical approach that leverages discrete LLM supply shocks-abrupt changes in model prices and capabilities, and contrasts verified with non-verified reviews to identify changes in platform activity associated with generative AI supply improvements. We apply this approach to more than 13 million reviews from Trustpilot, one of the leading online platforms for business reviews. A robust finding is that following LLM supply shocks, unverified reviews shift toward greater negativity: more 1-stars, fewer 5-stars, and lower ratings, with effects driven primarily by new model releases and concentrated among firms with the lowest and highest review volumes, suggesting that strategic AI use may reshape platform competition dynamics. We further find that LLM supply shocks trigger short, concentrated bursts of review activity. Together, these findings suggest that generative AI is already reshaping how reputation and competition operate on online platforms.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
