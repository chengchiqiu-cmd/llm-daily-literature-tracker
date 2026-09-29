# 2026-09-29 LLM 服务系统每日文献简报

> 检索窗口：2026-09-28 至 2026-09-29（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 卢西姆:城市规划的LLM驱动空间平衡模拟器

> 英文原标题：LUSIM: An LLM-Driven Spatial-Equilibrium Simulator for Urban Planning

- **作者：** Mengzhong Ma、Jingwei Zhou、Te Bao、Lin William Cong、Yonggang Wen
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-28；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7530560) · [DOI](https://doi.org/10.2139/ssrn.7530560)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在城市政策前面的量化评估历史上依赖于封闭形式的空间平衡和低维度的离散选择模型,这些模型将分析限制在均的代理和固定形式的参数公用品上,从而在校准的基线周围平衡比例的响应. 将大型语言模型集成到多代理模拟中缓解了这些限制,但现有的LLM驱动平台缺乏量化政策评估所需的市场清算机制和外部校准参数. 我们介绍了LUSim (LLM驱动的城市模拟器),这是一个多代理模拟器,多种家庭通过一个大语言模型和一个在外部校准的一般平衡城市内清晰的住房和劳动市场来选择居住和工作场所, 我们在Ahlfeldt et al. (2015) 校准的96区柏林实例上模拟了一个新的快速过渡线. 结构发动机只能按比例重量化校准的城市,将其响应集中在新站点上,而在LLM驱动的家庭中,搬迁人数大约是8倍,收益转移到边缘地区. 为了测试哪个发动机能预测真正的城市变化, 我们启动了1986年分化的柏林的每一个发动机, 让它预测重新统一的城市, 与LLM驱动家庭的模拟比任何结构基线都更好地预测这些变化, 地区名称也被保留以免依赖记忆历史, 而对比存在于第二条铁路走廊,扩大地板空间的区块化政策和第二个模型家庭中. 我们将这些结果解释为证据, 基于LLM的决策规则, 在校准环境中通过市场清算进行纪律, 预测城市变化超出结构模型的范围.

### 英文原摘要

Quantitative ex-ante urban-policy evaluation has historically relied on closedform spatial-equilibrium and low-dimensional discrete-choice models that constrain analysis to homogeneous agents and fixed-form parametric utilities, and thereby to smooth proportional responses around the calibrated baseline. Integrating large language models into multi-agent simulation alleviates these constraints, but existing LLM-driven platforms lack the market-clearing mechanism and externally calibrated parameters that quantitative policy evaluation requires. We present LUSim (LLM-driven Urban Simulator), a multi-agent simulator in which heterogeneous households choose residence and workplace through a large language model and clear housing and labour markets inside an externally calibrated general-equilibrium city, with structural decision rules as baselines under identical conditions. We simulate a new rapid-transit line on a 96-zone Berlin instance calibrated from Ahlfeldt et al. (2015). The structural engines, which can only reweight the calibrated city in proportion, concentrate their response at the new stations, whereas with LLM-driven households approximately eight times as many relocate and the gains shift to peripheral districts. To test which engine predicts real urban change, we initialise every engine on the divided Berlin of 1986, let it predict the reunified city, and score, by criteria fixed in advance, its prediction of which districts gain or lose residents, jobs, prices, and wages against the changes observed by 2006. The simulation with LLM-driven households predicts these changes better than every structural baseline, also with district names withheld so that it cannot rely on memorised history, and the contrast persists across a second rail corridor, a zoning policy that expands floor space, and a second model family. We interpret these results as evidence that LLM-driven decision rules, disciplined by market clearing in a calibrated environment, predict urban change beyond the reach of structural models.

## 2. 自主网络运营的演变:自动利用生成智能框架 (AEG) 的审查

> 英文原标题：The Evolution of Autonomous Cyber Operations: A Review of Intelligent Frameworks for Automated Exploit Generation (AEG)

- **作者：** Rilwan Ali Zira、Kabiru Sunusi Alaramma、Maryam Abdullahi Musa
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-28；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7536849) · [DOI](https://doi.org/10.2139/ssrn.7536849)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 llm、resource allocation。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

网络威胁的快速升级,其特征是多阶段的攻击向量和复杂的防御缓解措施,使得传统的手动透测试对现代软件生态系统不够. 这项审查探讨了"代理安全"的技术轨迹, 专注于集成一个智能框架, 合成,符号执行和强化学习 (RL) 来自动化漏洞研究的生命周期. 这一演变的核心是从概率化"黑盒"模糊到深度Q学习指导的发现的过渡,这优化了路径覆盖和资源配置.我们分析了符号执行如何为自动利用生成 (AEG) 提供必要的数学严格性,允许系统解决复杂的路径限制并绕过ASLR和DEP等现代操作系统级保护. 此外,我们评估了强化学习作为战略调整器的作用,利用马科夫决策流程链接漏洞到自主攻击路径.该审查突出了2025年2026年的关键范式转变:基于LLM的象征分解出现可扩展分析和O-SAFE等正式验证框架以确保运营道德. 通过评估这些融合技术,本论文确定了统一可解释框架中的研究缺口,这些框架平衡了模糊的高速探索与正式解决器的确定性证明,最终为下一代自主防御安全服务提供了蓝图.

### 英文原摘要

The rapid escalation of cyber threats, characterized by multi-stage attack vectors and sophisticated defensive mitigations, has rendered traditional, manual penetration testing insufficient for modern software ecosystems. This review examines the technological trajectory toward "Agentic Security," focusing on the integration of an Intelligent Framework that synthesizes Fuzzing, Symbolic Execution, and Reinforcement Learning (RL) to automate the lifecycle of vulnerability research. Central to this evolution is the transition from probabilistic "black-box" fuzzing to Deep Q-Learning guided discovery, which optimizes path coverage and resource allocation. We analyze how Symbolic Execution provides the mathematical rigor necessary for Automated Exploit Generation (AEG), allowing systems to solve complex path constraints and bypass modern OS-level protections like ASLR and DEP. Furthermore, we evaluate the role of Reinforcement Learning as a strategic orchestrator, utilizing Markov Decision Processes to chain vulnerabilities into autonomous attack paths. The review highlights a critical paradigm shift in 2025–2026: the emergence of LLM-based symbolic decomposition for scalable analysis and formal verification frameworks like O-SAFE to ensure operational ethics. By evaluating these converged technologies, this paper identifies a research gap in unified, explainable frameworks that balance the high-speed exploration of fuzzing with the deterministic proofs of formal solvers, ultimately providing a blueprint for the next generation of autonomous defensive security services.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
