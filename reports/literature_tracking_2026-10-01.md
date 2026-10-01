# 2026-10-01 LLM 服务系统每日文献简报

> 检索窗口：2026-09-30 至 2026-10-01（北京时间 / Asia/Shanghai）；本期确认 4 篇，其中直接 LLM 服务研究 4 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 神经检查器:基于非同步学习的关键-值缓存预集管道,以实现高效的大型语言模型推理

> 英文原标题：Neuro-Fetcher: An Asynchronous Learning-Based Key-Value Cache Pre-fetching Pipeline for Efficient Large Language Model Inference

- **作者：** Shenyu Liu、Fengxun Qi、Yu Chen、Caifeng Shan
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-30；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 14
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7545713) · [DOI](https://doi.org/10.2139/ssrn.7545713)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、scheduling、kv cache。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 中的关键值 (KV) 缓存的巨大规模使得自动降低推理成为了显著的内存带宽瓶. 最近的KV缓存压缩方法主要使用手工或休斯主义规则预先获取重要的KV缓存输入并发出不必要的缓存. 这些基于规则的方法无法捕捉不同模型和数据分布中固有的复杂动态关注模式,导致下游任务的降低. 在本文中,我们提出了一种基于学习的KV缓存管理方法,称为Neuro-Fetcher,这是一个轻量级的神经网络,通过输入代币和中间注意模式之间的关系准确预测重要的KV缓存输入.这种基于学习的预测策略可以提高KV缓存预测的准确性和下游任务的性能. 我们的工作克服了基于学习的预测者两个关键挑战:我们提出了"浅预测"战略,以应对多层预测的高度复杂性, 实验表明,我们的方法可以显著提高推断吞吐量, 此外,我们对模型的通用化能力进行了分析,并证明我们的Neuro-Fetcher可以表现出强大的零射击家庭内可转移性 (例如,OPT-13B到OPT-6.7B),

### 英文原摘要

The immense size of the Key-Value (KV) cache in Large Language Models (LLMs) has made autoregressive inference a significant memory-bandwidth bottleneck. Recent KV cache compression methods mainly utilize handcraft or heuristic rules to pre-fetch the important KV cache entries and emit unnecessary caches. These rule-based methods fail to capture the complex dynamic attention patterns inherent in different models and data distributions, leading to degradation of downstream tasks. In this paper, we propose a novel learning-based KV cache management approach named Neuro-Fetcher, which is a lightweight neural network trained to accurately predict important KV cache entries by the relationship between input tokens and intermediate attention patterns. This learning-based pre-fetching strategy can improve the accuracy of KV cache prediction and the performance of downstream tasks. Our work overcomes two critical challenges for learning-based pre-fetchers: we propose the "Shallow Pre-fetching" strategy to tackle the high complexity of multi-layer prediction, and design a "Ping-Pong Scheduling" mechanism to effectively hide the inference latency of the predictor itself. The experiments demonstrate that our approach significantly improves inference throughput over strong heuristic baselines without compromising model perplexity. Furthermore, we conduct an analysis of the model generalization capabilities and demonstrate that our Neuro-Fetcher could exhibit strong zero-shot intra-family transferability (e.g., OPT-13B to OPT-6.7B), unlocking a 'train-once, deploy-anywhere within the family' paradigm that drastically reduces deployment costs.

## 2. 大学招生中的人工智能政策:对机构景观及其经济利益的调查

> 英文原标题：AI Policy In College Admissions: A Survey Of The Institutional Landscape And Its Economic Stakes

- **作者：** Mani Deepika Adusumilli、Tianming Liu、Triparna Ganguly、Zhengliang Liu、David B. Mustard
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-30；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7545281) · [DOI](https://doi.org/10.2139/ssrn.7545281)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 generative ai、price discrimination。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工智能从两个方向进入大学,几乎完全分开.机构越来越多地使用人工智能来评分论文,预测收益率和优化财务援助;申请人越来越多地使用它来写那些系统阅读的论文.这篇论文调查了他们共享的经济基层和他们现在运营的法律环境. 我们审查了招生管理的经济学,学费价格歧视,以及人类资本与信号的辩论,描述了长期以来被要求认证的招生;在本科,研究生,医学和法律招生中,人工智能的文档化机构部署; 认证机构和国际响应;以及提供大多数机构招生AI的集中供应商市场. 作为一个原始的实验贡献,我们介绍了75个美国和英国机构关于申请人在招生试卷中使用生成人工智能的公布的政策的手工编译数据集, 三分之二的样本允许人工智能提供帮助和编辑,同时禁止生成文本,并且特定程序的禁令集中在艺术,设计和创意写作录取中,其中提交的作品本身是被评估的文物. 第三个结论涉及证据本身:在18项政策总结列出执行机制的条款中,所有18项均来自第三方聚合物,而在样本中没有一个机构以其自己的发表词来说明执行机制. 我们直接报告数据集的限制:75项录取中的35项基于抛词而不是经验证的报价,24项来自一个聚合物而不是机构本身的网站. 我们认为这种分断反映了政治和法律选择而不是技术不可避免性,

### 英文原摘要

Artificial intelligence has entered college admissions from two directions that are governed almost entirely separately. Institutions increasingly use AI to score essays, forecast yield, and optimize financial aid; applicants increasingly use it to write the essays those systems read. This paper surveys both, together with the economic substrate they share and the legal environment they now operate in. We review the economics of enrollment management, tuition price discrimination, and the human-capital-versus-signaling debate that describes what admission has long been asked to certify; the documented institutional deployment of AI across undergraduate, graduate, medical, and law admissions; the post-SFFA legal landscape and the 2025 federal retreat from disparateimpact enforcement, set against a fragmented state, accreditor, and international response; and the concentrated vendor market that supplies most institutional admissions AI. As an original empirical contribution, we present a hand-compiled dataset of 75 U.S. and UK institutions' published policies on applicant use of generative AI in admissions essays, coded into five tiers. Two-thirds of the sample permits AI for assistance and editing while forbidding generated text, and program-specific prohibitions concentrate sharply in art, design, and creative-writing admissions, where the submitted work is itself the evaluated artifact. A third finding concerns the evidence itself: of the 18 entries whose policy summary names an enforcement mechanism, all 18 come from a third-party aggregator, and no institution in the sample states an enforcement mechanism in its own published words. We report the dataset's limits directly: 35 of 75 entries rest on paraphrase rather than verified quotation, and 24 derive from an aggregator rather than the institution's own site. Read together, the applicant-facing and institution-facing sides of admissions AI are proceeding on separate tracks with separate rules. We argue that this disarticulation reflects a political and legal choice rather than a technical inevitability, and that narrowing it is the central unresolved question at the intersection of AI and college admissions.

## 3. 运营GPU能源和开放权重LLM推理的估计碳排放跨模型尺度和背景长度

> 英文原标题：Operational GPU Energy and Estimated Carbon Emissions ofOpen-Weight LLM Inference Across Model Scale and ContextLength

- **作者：** Anupam Dhakal、Keshav Raj Sharma、Saimon Neupane
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-30；SSRN/Crossref
- **分类：** 数据中心能源、碳与跨时段转移；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7545974) · [DOI](https://doi.org/10.2139/ssrn.7545974)

### 一两句话看懂

这篇论文关注“数据中心能源、碳与跨时段转移”，重点涉及 large language model、llm、llm inference、carbon emissions。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 推断越来越多地部署在规模上,使运营能源使用和相关的碳排放成为重要可持续发展问题.我们为九个Qwen3,Ministral3和Llama3.1家庭的开放权重LLM进行了经过控制的实验研究. 所有4,050次最终推断测量均采用相同的NVIDIA RTX PRO6000黑服务器版GPU采用非量化BF16精度,批量一,确定性贪解码和基于Zeus的GPU能量测量.技术重复在模型问题级别上总结,产生990次初始观测. 平均GPU能量随着每个模型的工作负载长度而大幅增加:长工作负载需要大约9.115.2次,而短工作负载的平均能量.在全球平均电力强度假设为445g CO2/kWh下,对于长工作负载的Qwen3-32B来说,最大的平均值为1.737.66J/推断,相当于214.795g CO2/1000推断. 在相匹配的架构比较中,Qwen3-32B Dense分别比Qwen3-30B-A3BMoE在短,中和长工作负载上消耗了202.70%,255.46%和355.99%更多的能量.响应质量结果没有显示模型规模的单调改善.这些发现表明,文本长度和架构可以显著改变LLM推断的运营可持续性,并且应在整个过程中报告.

### 英文原摘要

Large language model (LLM) inference is increasingly deployed atscale, making operational energy use and associated carbon emissions important sustainability concerns. We present a controlledempirical study of nine open-weight LLMs from the Qwen3, Ministral 3, and Llama 3.1 families across frozen short-, medium-, andlong-context question-answering workloads. All 4,050 final inference measurements were collected on the same NVIDIA RTX PRO6000 Blackwell Server Edition GPU using unquantized BF16 precision, batch size one, deterministic greedy decoding, and Zeus-basedGPU energy measurement. Technical repeats were aggregated atthe model–question level, yielding 990 primary observations. MeanGPU energy increased substantially with workload length for every model: Long workloads required approximately 9.1–15.2 timesthe mean energy of Short workloads. The largest observed meanwas 1,737.66 J per inference for Qwen3-32B on the Long workload,corresponding to 214.795 g CO2 per 1,000 inferences under a globalaverage electricity-intensity assumption of 445 g CO2/kWh. In thematched architecture comparison, Qwen3-32B Dense consumed202.70%, 255.46%, and 355.99% more energy than Qwen3-30B-A3BMoE on Short, Medium, and Long workloads, respectively. Answerquality results did not show a monotonic improvement with modelscale. These findings show that context length and architecture canmaterially change the operational sustainability of LLM inferenceand should be reported alongsi

## 4. 人类人工智能操作中集中或委托生成人工智能?决策权威,责任和工作分配

> 英文原标题：Centralize or Delegate Generative AI in Human--AI Operations? Decision Authority, Responsibility, and Work Allocation

- **作者：** Lingchen Huang、Kun Wang、Xiangfeng Chen
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-30；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7545846) · [DOI](https://doi.org/10.2139/ssrn.7545846)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 generative ai、information design、workload。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

创建人工智能越来越多地执行运营任务,但不能承担其错误的责任.因此,企业必须决定谁控制人工智能工作负载,如何分配损失,以及哪些激励措施控制人工智能生产. 我们开发了一种主要的代理模式, 集中和委托管理, 多元化的员工, 人类和GenAI工作的错误损失,以及私下观察到的AI协调能力. 委托治理允许工人适应人工智能依赖能力,但引入了不利的选择和信息租金;它仅在特定类型的刀上实现了第一个最佳. 因此,选扭曲,信息租金和汇集可以创造一个中间组合集中化间隔. 责任分享区分权威与损失负担,共同转让基准提高了集中合同,同时保持了标准化,可审计的人工智能使用支持了边际收费或补贴,在能力可观测时实现了第一个最佳.能力评估只有当其包括治理的收益超过其成本时才有价值. 这项分析将决策权力,财务责任,边际责任和信息设计确定为不同的运营杆,并为组织人为人工智能工作流程提供可实施的指导.

### 英文原摘要

Generative artificial intelligence increasingly performs operational tasks but cannot bear responsibility for its errors. Firms must therefore decide who controls AI workload, how losses are allocated, and which incentives govern human--AI production. We develop a principal--agent model of centralized and delegated governance with heterogeneous workers, error losses from both human and GenAI work, and privately observed AI-coordination capability. Centralized governance lets the firm determine AI reliance but ignores worker heterogeneity and generally fails to achieve the first best. Delegated governance allows workers to adapt AI reliance to capability but introduces adverse selection and information rents; it implements the first best only at a type-specific knife edge. With private capability, optimized delegated value is convex rather than affine in workforce composition. Screening distortions, information rents, and pooling can therefore create an intermediate-composition centralization interval. We then separate mechanisms bundled in the baseline. Responsibility shares distinguish authority from loss bearing, a common-transfer benchmark improves centralized contracting while preserving standardization, and auditable AI use supports a marginal charge or subsidy that implements the first best when capability is observable. Capability assessment is valuable only when its governance-inclusive gain exceeds its cost. The analysis identifies decision authority, financial responsibility, marginal accountability, and information design as distinct operating levers and provides implementable guidance for organizing human--AI workflows.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
