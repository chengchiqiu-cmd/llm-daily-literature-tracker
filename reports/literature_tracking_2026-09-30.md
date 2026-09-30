# 2026-09-30 LLM 服务系统每日文献简报

> 检索窗口：2026-09-29 至 2026-09-30（北京时间 / Asia/Shanghai）；本期确认 5 篇，其中直接 LLM 服务研究 5 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. CertiGATE:设施管理中基于大型语言模型的工作顺序安排的监护基准和质量证书协议

> 英文原标题：CertiGATE: A Guard Benchmark and Quality-Certificate Protocol for Large Language Model-Based Work-Order Scheduling in Facility Management

- **作者：** Ziheng Zhang、Tzu Pei Ku Chia、Xiaofei Yang、Xiangyu Chang、Shuyi Wang、Jichuan Tang、Wei Zhang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-29；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7529119) · [DOI](https://doi.org/10.2139/ssrn.7529119)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

设施管理安排越来越多地使用大型语言模型 (LLM) 将监督员的指示转化为时间表变化.确定性保护者决定每个变化是否可以执行,但大多数只检查语法和可行性,因此可执行但糟糕的时间表通过. 我们推出了CertiGATE,这是一个开放的基准和质量证书协议:2000个标记的说明,从公共工作订单数据中可播放的发送环境,以及八个LLM提议.该套件是识别一个警卫可以和不能捕获的LLM故障模式的可复制工具. 对于每次接受,质量门计算出一个无溶剂的下限,在变更后达到最好的优先权重延迟.在正宗提案上,证书拒绝了91.4%的构建质量违规行为,并错误地拒绝了2.6%的合法指示,每项提案的可用性成本保证. 终端认证将旗舰模型的平均时间表损害从+36.96重量工作小时每次指令,仅在可行性监控下降至0.55,靠近没有AI的基线.手写的恶化规则与认证的检测相匹配或超过了相匹配的假块成本,但只有与一个参考相比,它本身可能很差. 证书限制了每个接受的距离与最佳可实现的时间表,并将这两项结合保持了两种特性.在匹配的代币预算下,一个相同模型的多代理管道对单个代理没有任何优势,尽管只有很大的差异可以检测到. 证书不确定指令是否捕获用户意图,因此模糊性和快速注射需要语义,安全或人类批准的控制.

### 英文原摘要

Facility-management scheduling increasingly uses large language models (LLMs) to turn supervisors' instructions into schedule changes. Deterministic guards decide whether each change may be executed, yet most check only syntax and feasibility, so executable but poor schedules pass. We introduce CertiGATE, an open benchmark and quality-certificate protocol for this guard layer: 2,000 labelled instructions, a replayable dispatch environment from public work-order data, and eight LLM proposers. The suite is a reproducible instrument for identifying LLM failure modes that a guard can and cannot catch. For every acceptance, the quality gate computes a solver-free lower bound on the best achievable priority-weighted tardiness after the change. On canonical proposals, the certificate rejects 91.4% of constructed quality violations and falsely rejects 2.6% of legitimate instructions, the usability cost of per-proposal assurance. End-toend certification reduces the flagship model's mean schedule damage from +36.96 weighted business hours per instruction under feasibility-only guarding to-0.55, near the no-AI baseline. A handwritten deterioration rule matches or exceeds the certificate's detection at matched falseblock cost, but only against a reference that may itself be poor. The certificate bounds every acceptance's distance from the best achievable schedule, and combining the two retains both properties. At matched token budgets, a same-model multi-agent pipeline shows no advantage over a single agent, though only large differences were detectable. The findings characterise guard behaviour under controlled stress, not field failure rates. The certificate does not establish whether an instruction captures user intent, so ambiguity and prompt injection require semantic, security, or human-approval controls.

## 2. 在梯子类型碳交易下,集成能源系统规划的LLM驱动奖励进化

> 英文原标题：LLM-Driven Reward Evolution for Integrated Energy System Scheduling under Ladder-Type Carbon Trading

- **作者：** Xinquan Shao、Kai Zhao、Qianwen Xu、Xin Yu、shuai Liu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-29；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7540426) · [DOI](https://doi.org/10.2139/ssrn.7540426)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在梯子类型的碳交易下,集成能源系统 (IES) 规划涉及水平水平的碳结算,这使得加强学习的有效步骤奖励设计复杂.本论文提出了基于大语言模型 (LLM) 的适应性奖励进化 (LLM-ADRE),这是对奖励政策候选人从工程运营结果中反复调整的培训框架. 后期工程评估人员在完整的时间表事件中测量运营成本,会计排放,热服务偏差和终端电源状态偏差,为独立于奖励特定回报的候选人进行比较提供了共同的基础. 奖励重新标记,基于质量的推广分配和条件参数转移再利用收藏的过渡和奖励修改后学习的政策信息.在28天的测试集中,LLM-ADRE在同一环境互动预算下提高了平均剧集质量5.6%. 它还减少了2.14%和37.96%的平均计量排放和加热服务偏差,运营成本和终端SOC偏差相似.

### 英文原摘要

Integrated energy system (IES) scheduling under ladder-type carbon trading involves horizon-level carbon settlement, which complicates the design of effective stepwise rewards for reinforcement learning. This paper proposes large language model (LLM)-driven Adaptive Reward Evolution (LLM-ADRE), a training framework for iteratively adapting reward–policy candidates from engineering operating outcomes. A posterior engineering evaluator measures operating cost, accounted emissions, thermal-service deviations, and terminal state-of-charge (SOC) deviation over complete scheduling episodes, providing a common basis for candidate comparison independent of reward-specific returns. Reward relabeling, quality-based rollout allocation, and conditional parameter transfer reuse collected transitions and learned policy information after reward revisions. Across three seeds on a 28-day held-out test set, LLM-ADRE improves mean episode quality by 5.6% over Manual-Reward under the same environment-interaction budget. It also reduces mean accounted emissions and combined thermal-service deviation by 2.14% and 37.96%, respectively, with similar operating cost and terminal SOC deviation. It achieves comparable observed scheduling quality to Eureka while using one-third of Eureka’s nominal environment-interaction budget.

## 3. 异质共享:在边缘计算上进行LLM推理培训的职能部门工作架构

> 英文原标题：Heterogeneous Co-Serving: A Functional Division-of-Labor Architecture for LLM Inference-Training on Edge Computing

- **作者：** Zhicheng Guo、Wei Gao、Xiaoze Jiang、Chenglei Fan
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-29；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7540536) · [DOI](https://doi.org/10.2139/ssrn.7540536)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 llm、llm inference、latency、throughput。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

现有共服务系统为推断和训练而设置均的GPU资源,这不适合高内存,低VRAM的异质边缘设置. 本文提出了功能分工系统设计模式:GPU处理注意力,路由和解码以低延迟推断,而CPU同时执行MoE专家FFN计算和LoRA细节调整,通过mmap页面缓存共享INT4专家重量. 引入了三种一般机制: (1) 基于功能模块的GPUCPU分工架构; (2) 单副本共享专家重量存储与一个物理页面缓存副本在推断和训练之间共享; (3) 预折叠在线重量迁移机制,允许免于图表捕获的热更新,零运行时间绕行费用. 这些机制与不断适应的防守深度安全链 (数据质量选,持久评估门,控制部署,异常滚动) 结合,构成了有限风险服务学习系统. 在 16 GB VRAM 工作站上,具有 35 B 参数 MoE 模型,原型实现 9.0 tok/s 度吞吐量,推理侧 RSS 为 13.95 GB (全系统工作组 ∼ 65.6 GB);预折热更新比重启更新 131.5 × 快 (∼ 180 ms vs 23.78 s) 在轻到中等负载下无飞行请求损失;在联合训练下推理保留达到 0.90 ×. 核心机制通过三个设备类和三个模型架构进行验证,为边缘服务学习系统提供了设计模式.

### 英文原摘要

Existing co-serving systems assume homogeneous GPU resources for inference and training, which poorly fits the “high-memory, low-VRAM” heterogeneous edge setting. This paper proposes a functional division-of-labor system design pattern: GPU handles attention, routing, and decoding for low-latency inference, while CPU concurrently executes MoE expert FFN computation and LoRA fine-tuning, sharing INT4 expert weights via mmap page cache. Three general mechanisms are introduced: (1) a GPU–CPU division-of-labor architecture partitioned by functional module; (2) single-copy shared expert-weight storage with one physical page-cache copy shared between inference and training; (3) a prefolding online weight migration mechanism enabling graph-recapture-free hot updates with zero runtime bypass overhead. Together with a defense-in-depth safety chain for continual adaptation (data quality screening, holdout evaluation gate, controlled rollout, anomaly rollback), these mechanisms form a bounded-risk serve-while-learning system. On a 16 GB VRAM workstation with a 35B-parameter MoE model, the prototype achieves 9.0 tok/s saturation throughput with an inference-side RSS of 13.95 GB (full-system working set ∼65.6 GB); prefolding hot update is 131.5× faster than restart-based update (∼180 ms vs. 23.78 s) with zero in-flight request loss under light-to-medium load; inference retention under co-training reaches 0.90×. Core mechanisms are validated across three device classes and three model architectures, providing a design pattern for edge “serve-while-learning” systems.

## 4. 提供生成人工智能:均的价格,不平等的负担和人工智能传播的两个边缘

> 英文原标题：Affording Generative AI: Uniform Prices, Unequal Burdens, and the Two Margins of AI Diffusion

- **作者：** TaeHwan Oh
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-29；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7535900) · [DOI](https://doi.org/10.2139/ssrn.7535900)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 generative ai、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

我记录了这个阶梯的成本与201个经济体的收入相比,审计了包括税收在内的170个商店的ChatGPT,Claude和Gemini的本地应用商店价格,并将负担与两个独立的扩散措施相关. 当地美元价格几乎没有回应收入:20美元计划的弹性为0.030.04美元,而OpenAI的入门级别ChatGPT Go的弹性为0.14美元,而购买力指数价格为0.23美元. 因此,20美元计划在高收入中等经济体每年占人均收入的0.65%和低收入中等经济体的29%,而在覆盖经济体工作年龄人口的60%生活在宽带负担率比率超过2%的地区. 任何生成人工智能使用的收入弹性为0.37,其中大约一半反映了互联网使用的收入梯度,而人工智能用户与互联网用户的比例在中等和低收入群体中均.每人对边境助理 (Claude;免费和付费账户合并) 的使用量增加了收入的两倍 (0.71),并且其测量梯度在2025年8月至2026年2月之间加剧. 两层次的采用模式,其中免费层次放宽了人们是否使用人工智能而不是使用多少边界能力的预算限制,与这种对比一致,尽管跨国数据无法确定价格影响.

### 英文原摘要

Consumer generative AI is sold on a price ladder (roughly $8, $20, $100 and $200 a month) that is nearly identical across countries. I document what this ladder costs relative to income in 201 economies, audit tax-inclusive local App Store prices for ChatGPT, Claude and Gemini in 170 storefronts, and relate burdens to two independent measures of diffusion. Local dollar prices barely respond to income: the elasticity is 0.03–0.04 for $20 plans and 0.14 for ChatGPT Go, OpenAI's entry tier, compared with 0.23 under purchasing-power-indexed pricing. A $20 plan therefore costs 0.65% of per-capita income a year in the median high-income economy and 29% in the median low-income economy, and 60% of the covered economies' working-age population lives where it exceeds the 2% affordability benchmark for broadband. The income elasticity of any generative-AI use is 0.37, about half of which mirrors the income gradient in internet use, and the ratio of AI users to internet users is flat across middle- and low-income groups. Per-capita use of a frontier assistant (Claude; free and paid accounts pooled) rises twice as steeply with income (0.71), and its measured gradient steepened between August 2025 and February 2026. A two-tier adoption model, in which free tiers relax the budget constraint on whether people use AI but not on how much frontier capability they use, is consistent with this contrast, although cross-country data cannot identify price effects. Because exposure and access are both income-graded, larger conditional gains for less-skilled users need not produce cross-country convergence.

## 5. 什么时候LLM管弦演唱会支付?GEAR:根据推理预算的适应性路由的图表控制执行

> 英文原标题：When Does LLM Orchestration Pay? GEAR: Graph-Controlled Execution with Adaptive Routing under Inference Budgets

- **作者：** Cheng Zhu、Bai Jiangyao、Zhaoyun Ding、Yijia Fu、Lailong luo
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-29；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7541005) · [DOI](https://doi.org/10.2139/ssrn.7541005)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、llm serving。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 越来越多地作为基于知识的系统的推理引擎,但在预算限制下部署它们伴随着两个关键的决定:模型层的选择和执行拓学.现有路由器只分配模型用于平面的单次调用调用,而固定的多代理框架在每个接入查询上承担大量的编排总费用. 这篇论文提出了GEAR (Graph-Controlled Execution with Adaptive Routing),一个基于原则的框架,利用任务结构知识,在推断预算下动态管理执行拓学,推理深度和模型层次分配.GEAR与闭环拉格兰基预算节奏和不确定性引导的外部升级机制协调了等级级级路由. 综合实验评估和部署重复显示,任务结构的限制在不损害推理准确性的情况下大幅减少了与静态调整相比的代币消费. 此外,选择性外部升级通过仅限于可恢复推理缺陷诊断的查询来保留多步骤图表构造,始终优于静态执行政策. 因此,GEAR将多代理配套设置为针对性的计算干预,而不是为可持续复合LLM服务提供无条件违约.

### 英文原摘要

Large language models (LLMs) increasingly serve as reasoning engines in knowledge-based systems, yet deploying them under budget constraints couples two critical decisions: model tier selection and execution topology. Existing routers allocate models only for flat single-call invocations, whereas fixed multi-agent frameworks incur substantial orchestration overhead on every incoming query. This paper proposes GEAR (Graph-Controlled Execution with Adaptive Routing), a principled framework that leverages task-structure knowledge to dynamically govern execution topology, reasoning depth, and model tier allocation under an inference budget. GEAR coordinates hierarchical step-level routing with closed-loop Lagrangian budget pacing and an uncertainty-guided outer escalation mechanism. Comprehensive empirical evaluations and deployment replays demonstrate that task-structure constraints substantially curtail token consumption relative to static orchestration without compromising reasoning accuracy. Furthermore, selective outer escalation consistently outperforms static execution policies by reserving multi-step graph construction exclusively for queries diagnosed with recoverable reasoning lapses. Consequently, GEAR establishes multi-agent orchestration as a targeted computational intervention rather than an unconditional default for sustainable compound LLM serving.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
