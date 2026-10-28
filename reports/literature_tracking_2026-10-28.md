# 2026-10-28 LLM 服务系统每日文献简报

> 检索窗口：2026-10-27 至 2026-10-28（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 限制式大型语言模型辅助任务解析和多模式合作控制用于航空发动机高度测试

> 英文原标题：Constrained Large Language Model-Assisted Task Parsing and Multimodal Cooperative Control for Aero-Engine Altitude Tests

- **作者：** bo feng、Hehong Zhang、Chun-Yang Zhang、Chao Zhai、Baiyi Zhang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-27；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7674281) · [DOI](https://doi.org/10.2139/ssrn.7674281)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

自动执行空中发动机高度测试需要将未结构化的测试卡转换为可执行任务,同时保留任务生成,事件安排和物理执行的限制.现有方法通常将任务解析,离散安排和连续控制作为部分分离的阶段. 因此,本论文提出了一个受限制的大语言模型辅助任务分析和多模式合作控制框架.语言模型生成结构化候选任务,而确定性检查和审查保留任务释放权.一个有限状态机器根据执行状态,运行时间监护和安全间隔授权候选活动. 连续控制层使用压力额定需求作为一个共同的接口,根据测试状态安排多种控制模式,并在正常过渡期间应用Smoothstep混合. 紧迫合作分配然后将结果的需求映射到可接受的门命令,并在多模式交换下确定了降低序控制错误的条件限制结果. 采用实体测试卡,数字和半物理控制测试以及物理双门实验.结果显示可靠的限制任务释放,有效的多模压力调节和模式过渡,以及与评估场景合作的执行器操作.因此,该框架为航空发动机高度测试提供了可追踪的任务到门执行路径.

### 英文原摘要

Automated execution of aero-engine altitude tests requires unstructured test cards to be converted into executable tasks whilepreserving constraints across task generation, event scheduling, and physical execution. Existing approaches typically address task parsing, discrete scheduling,and continuous control as partially separated stages. This paper therefore proposes a constrained largelanguage model-assisted task parsing and multimodal cooperative control framework. The language model generates structuredcandidate tasks, while deterministic checks and review retain task release authority. A finite-state machine authorizes candidate events according to theexecution state, runtime guards, and safety interlocks. The continuous control layer uses pressure ratedemand as a common interface, schedules multiple control modes according to the test state, and applies Smoothstep blending duringnormal transitions. Constrained cooperative allocation then maps the resulting demand to admissible valve commands, and aconditional boundedness result is established for the reduced-order control error under multimodal switching. Layered evaluationuses real test cards, digital and semi-physical control tests, and a physical dual-valve experiment. The results demonstrate reliableconstrained task release, effective multimodal pressure regulation and mode transition, and cooperative actuator operation withinthe evaluated scenarios. The framework thus provides a traceable task-to-valve execution path for aero-engine altitude tests.

## 2. 当人工智能误认为不可见性是无关紧要的时:在生成人工智能营销中的反复市场排除理论

> 英文原标题：When AI Mistakes Invisibility for Irrelevance: A Theory of Recursive Market Exclusion in Generative-AI Marketing

- **作者：** Ihsaan Basharat Want
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-27；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7665601) · [DOI](https://doi.org/10.2139/ssrn.7665601)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 generative ai、resource allocation。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

随着生成人工智能 (GenAI) 越来越嵌入战略营销中,企业依赖于消费者细分市场的算法表示,以信息市场研究,合成人格生成,创意开发和广告决策. 然而,许多消费者仍然在商业跟踪基础设施中受代表不足,从而创造了数据沙漠,其特征是稀缺,碎片化或未观察到的数字痕迹. 当GenAI工作流程遇到这些信息漏洞,而没有适当的领域特定的实验基础或不确定性校准,它们可能会产生流动的,心理详细的消费者表示,从而掩盖了部分特定证据的缺失. 我们将这种现象概念化为产生性伪确定性,并理论化它如何促进可见性需求混:管理层错误地将竞选活动表现错误归因于市场需求不足,而不是错误预测的营销干预. 通过整合行为学习理论,性能反理论和热炉效应的逻辑, 该框架建议,如果基于非校准生成表现的营销干预效果不佳,管理人员可以撤回战略投资,减少付费的曝光和可观测的行为信号,以便随后学习. 由于没有独立的探索性调查,这种过程可能加强了最初的算法隐形性,并维持了潜在的可行消费者细分的排除. 我们指定了一个理论上的可行性条件来区分递归排斥与理性市场退出:在最佳干预下预期的增长利保持积极时,排斥是病理性的 (Pi* > 0),但错误校准的生成属性有助于实现较差的结果. 我们推出了六项理论命题,确定相关的边界条件,将检索引发的代表性替代作为潜在的机制进行研究,并解释市场内外感知能力如何打断拟议的反循环. 通过将生成人工智能中的代表性限制与管理属性,组织学习和战略资源配置联系起来,本文推进了人工智能调整的营销决策如何复制市场排斥的概念性解释,并为未来的实验调查奠定了基础.

### 英文原摘要

As generative artificial intelligence (GenAI) becomes increasingly embedded in strategic marketing, firms are relying on algorithmic representations of consumer segments to inform market research, synthetic persona generation, creative development, and advertising decisions. Yet, many consumer populations remain underrepresented in commercial tracking infrastructures, creating “data deserts” characterised by sparse, fragmented, or unobserved digital traces. When GenAI workflows encounter these information gaps without adequate domain-specific empirical grounding or uncertainty calibration, they may generate fluent, psychologically detailed consumer representations that obscure the absence of segment-specific evidence. We conceptualise this phenomenon as generative pseudocertainty and theorise how it can contribute to visibility–demand conflation : the managerial misattribution of poor campaign performance to insufficient market demand rather than to a miscalibrated marketing intervention. Integrating behavioural learning theory, performance feedback theory, and the logic of the “hot stove effect”, we develop a conceptual framework of recursive market exclusion . The framework proposes that, when marketing interventions based on uncalibrated generative representations underperform, managers may withdraw strategic investment, reducing paid exposure and the observable behavioural signals available for subsequent learning. In the absence of independent exploratory inquiry, this process may reinforce initial algorithmic invisibility and sustain the exclusion of potentially viable consumer segments. We specify a theoretical viability condition distinguishing recursive exclusion from rational market exit: exclusion is pathological when expected incremental profit under an optimal intervention remains positive (Pi* > 0), but miscalibrated generative attributes contribute to inferior realised outcomes. We derive six theoretical propositions, identify relevant boundary conditions, examine retrieval-induced representational substitution as a potential mechanism, and explain how outside-in market sensing capabilities may interrupt the proposed feedback loop. By connecting representational limitations in generative AI with managerial attribution, organisational learning, and strategic resource allocation, this paper advances a conceptual account of how AI-mediated marketing decisions may reproduce market exclusion and establishes a foundation for future empirical investigation.

## 3. 有限缓冲式批发服务队列,有限的排列长度依赖的假期和国家依赖的批次抵达:适用于LLM推断批次

> 英文原标题：A finite-buffer bulk-service queue with bounded queue-length-dependent vacations and state-dependent batch arrivals: application to LLM inference batching

- **作者：** Gopal Gupta
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-27；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7675463) · [DOI](https://doi.org/10.2139/ssrn.7675463)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 的推理服务器在批量中执行请求,其尺寸由免费的关键值缓存限制,并且它们经常以背景工作填补静静的时期.由这种做法激励,我们研究一个单个服务器排队,有有限的等待室和批量波森抵达,其速度取决于服务器状态. 服务仅在至少一个客户等待时启动,并移除了排队长和随机容量Y的较小部分;其持续时间取决于批量大小和留下的客户数量. 当客户数量少于一个客户等待时,服务器最多采取M假期,其长度取决于他们的订单和开始时的排队长度,然后保持休眠,直到达到门. 我们用零件确定性马科夫过程来描述系统,编写其扩展生成器,并推导了科尔摩戈尔夫差异方程.在服务和假期完成时,嵌入式马科夫链,结合补充变量技术,给出了排队长和服务器状态在任意,出发和到达时代的联合分布. 边际分布,阻断概率和平均绩效测量以封闭形式或明确的有限数量进行. 经典的有限和无限队列作为特殊情况被恢复. 收取延迟,拒绝,能量和开关,并借助背景工作的成本函数,在门,假期数量,假期长度和等待室的大小上最小化.

### 英文原摘要

Inference servers for large language models (LLMs) execute requests in batches whose size is limited by the free key–value cache, and they often fill quiet periods with background jobs. Motivated by this practice, we study a single-server queue with a finite waiting room and batch Poisson arrivals whose rate depends on the server state. A service starts only when at least a customers wait and removes the smaller of the queue length and a random capacity Y ; its duration depends on the batch size and on the number of customers left behind. When fewer than a customers wait, the server takes at most M vacations whose lengths depend on their order and on the queue length at their start, and then stays dormant until the threshold is reached. We describe the system by a piecewise-deterministic Markov process, write its extended generator and derive the Kolmogorov differential–difference equations. An embedded Markov chain at service and vacation completions, combined with the supplementary variable technique, gives the joint distribution of the queue length and the server state at arbitrary, departure and arrival epochs. Marginal distributions, blocking probabilities and mean performance measures follow in closed form or as explicit finite sums. Classical finite and infinite queues are recovered as special cases. A cost function that charges latency, rejection, energy and switching, and credits background work, is minimised over the threshold, the number of vacations, the vacation length and the size of the waiting room.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
