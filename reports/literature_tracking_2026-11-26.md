# 2026-11-26 LLM 服务系统每日文献简报

> 检索窗口：2026-11-25 至 2026-11-26（北京时间 / Asia/Shanghai）；本期确认 4 篇，其中直接 LLM 服务研究 4 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 大型语言模型中的信息辨识

> 英文原标题：Information Discernment in Large Language Models

- **作者：** Joshua Ashkinaze、Laura Kurek、Alina Faisal、Tongyuan Miao、Mariam Joseph、Ceren Budak、Eric Gilbert
- **来源/日期：** arXiv；首次发布 2026-05-22；最近更新 2026-11-25；arXiv
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2607.19355v2) · [PDF](https://arxiv.org/pdf/2607.19355v2)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、llm、quota。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

法律法学 (LLM) 越来越多地与互联网等外部知识来源使用.它们是否适当地权衡信息 - - 更新更多的可靠来源 (来源辨别) 和更多的说法将事先更接近真相 (真相辨别)? 为了确定外部有效性,一项预注册,配额匹配的用户研究 (n=299) 证实了真正的LLM用户支持所有三个 axiom,并报告违反行为减少了他们的信任和使用意图. 在13种模型和近670万次试验中,我们发现了两种维度的一致失败:模型在源和真相辨别上几乎是偶然的, 模型在数据集上最有效地集成外部知识,其中其先例已经是最准确的.新型和更大的模型改善了真理辨识,但不是源辨识,这是模型复杂性不解决的盲点.我们确定了简单的推断时间干预,改善了两种形式的辨识. 我们将我们的数据集和调查作为一个核心对齐性质的试验床, 随着LLM取代传统搜索,

### 英文原摘要

LLMs are increasingly used with external knowledge sources like the internet. Do they weigh information appropriately -- updating more for reliable sources (source discernment) and more when claims bring priors closer to the truth (truth discernment)? We formalize this as information discernment and introduce Learn2Discern (L2D), an experimental framework and benchmark grounded in three normative axioms with interpretable metrics. To establish external validity, a pre-registered, quota-matched user study (n=299) confirms that real LLM users endorse all three axioms and report that violations reduce their trust and usage intent. Across 13 models and nearly 670K trials, we find consistent failures across both dimensions: models perform near chance on source and truth discernment, rely on source popularity twice as much as source reliability, and update roughly equally whether a claim improves or worsens their position relative to the ground truth. Models integrate external knowledge most effectively on datasets where their priors are already the most accurate. Newer and larger models improve truth discernment but not source discernment, a blind spot that model complexity does not address. We identify simple inference-time interventions that improve both forms of discernment. We release our dataset and survey as a testbed for a core alignment property that scales in importance as LLMs replace traditional search.

## 2. AiFlow:修改版LLM服务的建筑到退休标准

> 英文原标题：AiFlow: Construction-to-Retirement Conformance for Versioned LLM Services

- **作者：** Qunhui Zhang
- **来源/日期：** arXiv；首次发布 2026-08-01；最近更新 2026-11-25；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2608.00558v2) · [PDF](https://arxiv.org/pdf/2608.00558v2)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、llm、deadline、queue。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

现场更新可以保存大型语言模型 (LLM) 工作流程的拓和输出,同时绕过过过器的队列和同步限制. 背景任务可以在调用者返回后使用旧版本. AiFlow 通过可执行合同连接构建,调用和退休. 每个被允许的请求都捕捉到与检查的运营商相关的行动. 该服务证实呼叫的终端结果和其注册工作的发布.一旦新的呼叫不再能够捕获版本,所有者在退休之前检查这些证书和剩余的本地资源.严格的出版物暂停录取,而旧呼叫耗尽.推迟的出版物可以在其前任退休之前接受继任者的呼叫. 我们在一个Java虚拟机中评估了两个无状态线性工作流程.在严格的发布下,我们每次检查配置重复了三次注入的故障场景.如果没有未监督执行或过早更换,观察会被计算为包含的.仅仅在构建或完成检查时,九项故障观察中的六项满足了这一标准.在两项检查中,九项都实现了. 一个单独实施的协调员在所有24个测试对的生命周期结果,服务呼叫数量和回收决策上匹配了AiFlow.每400ms的更新,推迟发布会在两个负载中更频繁地达到500ms的截止日期.我们测量了所有满足截止日期的提供请求的份额. 严格的发布率为80个请求/秒,推迟的发布率为20个请求/秒.

### 英文原摘要

A live update can preserve the topology and output of a large language model (LLM) workflow while bypassing a filter's queue and concurrency limits. A background task can use the old version after its caller returns. AiFlow links construction, invocation and retirement through an executable contract. Each admitted request captures an action bound to the checked operators. The service certifies the call's terminal outcome and the release of its registered work. Once new calls can no longer capture the version, the owner checks these certificates and remaining local resources before retirement. Strict publication pauses admission while old calls drain. Deferred publication can admit calls to the successor before its predecessor retires. We evaluated two stateless linear workflows in one Java virtual machine. Under strict publication, we repeated three injected fault scenarios three times per check configuration. An observation counted as contained if neither unguarded execution nor premature replacement occurred. With construction or completion checking alone, six of nine fault observations met this criterion. With both checks, all nine did. A separately implemented coordinator matched AiFlow on the lifecycle outcome, service call count and reclamation decision in all 24 tested pairs. With updates every 400 ms, deferred publication met the 500 ms deadline more often at both loads. We measured the share of all offered requests that met the deadline on the latest scheduled version due at return. Strict publication led at 80 requests/s and deferred publication at 20 requests/s. Both policies use the same local evidence for retirement.

## 3. 在精细调整之前的试验:可行性关键选择和监测对固定物理平台实体基础模型的适应

> 英文原标题：Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform

- **作者：** Zilin Huang、Zhengyang Wan、Zihao Sheng、Boyue Wang、Ruolin Yang、Yuhao Luo、Sikai Chen
- **来源/日期：** arXiv；2026-11-25；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](http://arxiv.org/abs/2611.33772v1) · [PDF](https://arxiv.org/pdf/2611.33772v1)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 foundation model、deadline。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

实体基础模型越来越多地通过选择部署:一个实践者根据基准排名选择一个公共检查点,并根据本地数据进行细节调整.在选择模型之前,平台是固定的,几乎没有本地数据.我们问这样的检查点在固定平台上损失了什么,以及本地数据的损失可以回购的部分.我们将差距分为什么可以修复它. 传感器无法捕获的信息,不能用其数据关闭的传感器差距; 延迟差距,输出后控制循环需要它,属于循环,而不是重量;只有分布差距是细调的修复. 试验将其转化为五个阶段的可行性选择和监控适应:传感器合约的门和任何分数都无法取消的端到端延迟,在10分钟的本地日志上进行探测,在通过的候选人中根据目标相关分数进行排名,以及在发布前在闭环中监控和检查的细节调整. 在驾驶基准上,一个领先的闭环模型的延迟时间低于80至90%的路线,视野损失将计划移动2.2到5.7倍,而不是在相同的像素下丢失分辨率.本地框架缩小了75%的稳定差距,但在小预算中提高了扰动敏感性,并且根据分数选择违反了四个部署配置文件中的两个门. 在一辆全尺寸车辆上,工厂摄像头失败了传感门,并增加了一台摄像头修复了它.延迟门删除了两个最高得分的候选人,没有一个完成了闭环的旅行.选定的模型在5个闭环的旅行中通过了4次接受,而闭环检查保留了一个精细调节的模型,该模型在线上改进. 试验使那些无法从头开始训练基础模型的组织能够了解公共检查点是否可以在他们拥有的机器人或车辆上运行,

### 英文原摘要

Embodied foundation models are increasingly deployed by selection: a practitioner picks a public checkpoint by benchmark rank and fine-tunes it on local data. The platform is fixed before the model is chosen, with little or no local data. We ask what such a checkpoint loses on a fixed platform and which part of the loss local data can buy back. We split the gap by what can repair it. A sensing gap, information the sensors do not capture, cannot be closed with their data; a latency gap, output arriving after the control loop needs it, belongs to the loop, not the weights; only a distribution gap is fine-tuning's to repair. TRIAGE turns this into feasibility-gated selection and monitored adaptation in five stages: gates on the sensor contract and on end-to-end latency that no score can override, probes on ten minutes of local logs, a ranking by target-relevant score among the candidates that pass, and fine-tuning that is monitored and checked in closed loop before release. On driving benchmarks, a deadline below a leading closed-loop model's latency makes it collide on 80 to 90% of routes, and losing field of view moves plans 2.2 to 5.7 times more than losing resolution at equal pixels. Local frames close 75% of a stability gap but raise perturbation sensitivity at small budgets, and picking by score violates a gate in two of four deployment profiles. On a full-scale vehicle, the factory camera failed the sensing gate and an added camera repaired it. The latency gate removed the two highest-scoring candidates, neither of which completed a closed-loop trip. The selected model passed acceptance in 4 of 5 closed-loop trips, and the closed-loop check withheld a fine-tuned model that had improved offline. TRIAGE lets organizations that cannot train foundation models from scratch find out whether a public checkpoint can run on the robot or vehicle they own, and what to fix if not.

## 4. 不是每一个输入都需要一切:统一专家关门,模范布和代理管弦乐

> 英文原标题：Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration

- **作者：** Dat Tat Mai、Hung Tran Quy、Thai Viet Pham、James Jin Kang
- **来源/日期：** arXiv；2026-11-25；arXiv
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](http://arxiv.org/abs/2611.34112v1) · [PDF](https://arxiv.org/pdf/2611.34112v1)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 foundation model、load balancing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

执行单一神经重量,边界基础模型或整个多代理工作流程在每个输入上均地带来了大量的计算,延迟和货币总费用. 条件计算通过动态决定哪些内部专家,模型终端点或专业代理需要根据要求调用来缓解这些成本. 然而,在稀缺的神经架构中的代币层面关闭,查询层面模型台和任务层面的多代理协调在分离的研究小组中很大程度上取得了进展,从而掩盖了反复出现的系统故障和可转移的修复. 在这个系统性审查中,我们在2017年至2026年9月期间发表的2,289项研究 (从13,884个独特记录中选择) 在20个方法学家庭中,在统一的两步检查然后分配框架下合成. 微妙硬选分别占比70%,83%和91%的代币,查询和任务尺度文献,计算总费用在每个层面都表现为顶级的运营瓶. 工程保障仍然非常不对称:内部盖特优先考虑负载平衡,但很少采用不确定性估计,而模型选择和代理调整则依赖于信任门和预算规则,同时面临错误校准和级错误. 与此同时,在代理任务委托方面,出版量最快加速,路由机制在实验上最少被孤立,方法偏见风险最高.

### 英文原摘要

Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts, model endpoints, or specialized agents to invoke per request. Yet token-level gating in sparse neural architectures, query-level model cascades, and task-level multi-agent coordination have largely progressed in disconnected research silos, obscuring recurring system failures and transferable fixes. In this systematic review, we synthesize 2,289 studies published between 2017 and September 2026 (selected from 13,884 unique records) across 20 methodological families under a unified two-step inspect-then-allocate framework. Discrete hard selection accounts for 70%, 83%, and 91% of token-, query-, and task-scale literature respectively, and computational overhead appears as a top operational bottleneck across every layer. Engineering safeguards remain sharply asymmetric: intra-layer gating prioritizes load balancing while rarely incorporating uncertainty estimation, whereas model selection and agent orchestration rely on confidence thresholds and budget rules while confronting miscalibration and cascading errors. At the same time, publication volume is accelerating fastest in agentic task delegation, where routing mechanisms are least often isolated experimentally and methodological bias risk is highest.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
