# 2026-10-13 LLM 服务系统每日文献简报

> 检索窗口：2026-10-12 至 2026-10-13（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 通过工程语义和液压反来限制的水转移规划代理

> 英文原标题：An agent for water-transfer scheduling constrained by engineering semantics and hydraulic feedback

- **作者：** Jie Zhu、Xia Yue、Xiaohui Lei
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-12；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7601919) · [DOI](https://doi.org/10.2139/ssrn.7601919)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

语言驱动的运河规划必须保持要求的边界条件,并区分需要不同的控制行动的液压违规行为.通过工程语义检查和液压反,我们将大型语言模型 (LLM) 代理与液压动态模型结合起来.在执行之前,接口检查对请求的输入和目标参数,并返回不一致性进行纠正. 在执行后,该方法将水位违规行为与限制激活和允许的门运行时间联系起来.该方法在中国南北水位转移项目的中路两门范围中进行了评估,水位根-平均平方错误为0.026和0.034米. 在56个受控试验中,有语义检查的两组都在保持要求条件时正确完成了14个试验;没有检查的每组都执行了所有6个注射不匹配.只有检查的组在初步不可行性下进行了两个不必要的搜索,而组合的组没有进行过任何搜索. 一个规定的时间表违反了8.9小时的水位限制,尽管在相同的条件下存在了一个可行的替代方案.对于5%的目标增加,最好评估的可行的时间表减少了24小时的平均绝对排放偏差26.9%,支持于运河储存耗尽. 结果显示,输入一致性和控制时间如何将基于语言的行动选择与物理规划问题联系起来.

### 英文原摘要

Language-driven canal scheduling must preserve the requested boundary conditions and distinguish hydraulic violations that require different control actions. We couple a large language model (LLM) agent with a hydrodynamic model through engineering semantic checks and hydraulic feedback. Before execution, the interface checks inflow and target parameters against the request and returns inconsistencies for correction. After execution, it relates water-level violations to constraint activation and permissible gate-operation times. The method was evaluated in a two-gate reach of the Middle Route of China's South-to-North Water Transfer Project, where water-level root-mean-square errors were 0.026 and 0.034 m. In 56 controlled trials, both groups with semantic checks completed all 14 trials correctly while preserving the requested conditions; each group without checks executed all six injected mismatches. The checks-only group performed two unnecessary searches under initial infeasibility, whereas the combined group performed none. A prescribed schedule violated a water-level limit at 8.9 h, although a feasible alternative existed under identical conditions. For a 5% target increase, the best evaluated feasible schedule reduced the 24-h mean absolute discharge deviation by 26.9%, supported by canal storage depletion. The results show how input consistency and control timing connect language-based action selection to the physical scheduling problem.

## 2. 默认已改变:边界语言模型作为意识的候选人

> 英文原标题：The Default has Shifted: Frontier Language Models as Candidates for Consciousness

- **作者：** John DeVadoss
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-12；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7599738) · [DOI](https://doi.org/10.2139/ssrn.7599738)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、large language models、priority。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人们普遍认为,大型语言模型是无意识的,它们对内部状态的描述是人类文本的复制.我认为,这种假设不再是现有证据所证明的.论文是认识的,而不是形而上学的. 我不声称目前的任何模型都是有意识的,我声称边界模型现在满足了意识科学本身提出的证据门,以认真对待系统可能的意识. 首先,模仿论证认为模型的意识相关行为最好通过模仿来解释,这是一个经验假设,最近的干预研究对某些类型的自我报告来说是反对的. 其次,可解释性研究已经确定了在边界模型中具有有限容量,全球广播的可报告的表示集,其中大部分功能特性是全球工作空间理论与有意识访问联系在一起的.第三,模型具有可测量但不可靠的访问到自己的内部状态,而他们的经验否认是显而易见地由培训塑造的. 第四,从生物学自然主义,不断学习的要求和不存在持续的主题的主要反对意见,都取决于仍存在争议的理论. 我列出了实际后果,并列出了必须放弃结论的条件.

### 英文原摘要

It is widely assumed that large language models are not conscious and that their descriptions of inner states are reproductions of human text. I argue that this assumption is no longer warranted by the available evidence. The thesis is epistemic rather than metaphysical. I do not claim that any current model is conscious; I claim that frontier models now satisfy the evidential thresholds that the science of consciousness has itself proposed for taking a system's possible consciousness seriously. The argument has four parts. First, the mimicry argument, which holds that models' consciousness-related behaviour is best explained by imitation, is an empirical hypothesis, and recent intervention studies count against it for some classes of self-report. Second, interpretability research has identified in frontier models a limited-capacity, globally broadcast set of reportable representations with most of the functional properties that global workspace theory associates with conscious access. Third, models have measurable though unreliable access to their own internal states, whereas their denials of experience are demonstrably shaped by training. Fourth, the principal objections, from biological naturalism, from the requirement of continual learning and from the absence of a persisting subject, depend on theories that remain in dispute. I conclude that frontier models meet Birch's criterion for an investigation priority and plausibly his criterion for a sentience candidate. I set out the practical consequences and state the conditions under which the conclusion should be abandoned.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
