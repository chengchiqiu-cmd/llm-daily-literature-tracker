# 2026-07-15 LLM 服务系统每日文献简报

> 检索窗口：2026-07-14 至 2026-07-15（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用中文说明论文研究什么、怎样建模、如何求解，以及它能怎样进入我们的 LLM 服务运营研究；英文内容仅作为原文补充。

## 1. 编排式 AI 智能体系统的一般均衡理论

> 英文原标题：A General Equilibrium Theory of Orchestrated AI Agent Systems

- **研究问题：** 一个平台同时调度多个 LLM 智能体时，怎样给不同智能体分配任务，才能兼顾回答质量、等待时间和运行成本，并让整个系统稳定下来？
- **文章怎么做：** 作者把系统想象成一个小型市场：每个 LLM 智能体负责提供服务，平台负责把用户任务分给它们。平台先给质量、速度和成本设置一组内部评分，再根据“哪个智能体太忙、哪个还有空余”不断调整评分和任务分配，最后证明这种调整在一定条件下会停在一个稳定状态。论文把这个稳定状态称为“一般均衡”。
- **研究启示：** 这篇论文提供了一种理解平台调度的方法：平台可以同时考虑质量、等待时间和成本，而不是只选择最快的模型。对我们的研究来说，可以在此基础上继续加入用户实际支付的 Token 价格、不同用户对等待的敏感程度以及服务器拥堵。
- **作者：** Jean-Philippe Garnier
- **来源/日期：** arXiv；首次发布 2026-02-23；最近更新 2026-07-13；arXiv
- **研究类型：** 理论模型；直接 LLM 服务研究；相关性评分 17

### 中文内容总结

这篇论文研究一个平台怎样同时管理多个 LLM 智能体。不同智能体的回答质量、速度和成本不同，平台需要决定每个任务交给谁。作者把这一过程类比成市场：智能体提供服务，平台购买和分配这些服务，质量、时间和成本都有一个内部价格。当某个智能体需求过多时，它对应的内部价格会上升，平台就会把一部分任务转给其他智能体。作者证明，在若干规则成立时，这套调整过程能找到一个稳定方案，而且这个方案不会浪费系统资源。

### 模型设定

**模型主线：** 直观地说，平台给“回答质量高”“响应快”“成本低”分别设置内部评分，再根据各智能体是否过载调整这些评分和任务流向。这里的“价格”只是平台内部衡量资源稀缺程度的分数，并不是用户真正支付的钱。

**参与者 / 系统组件**

- 多个已经训练好的 LLM 智能体：它们不再学习新参数，只负责处理分配到的任务
- 中央平台：决定一个任务要经过哪些智能体，以及每个智能体分到多少任务
- 用户任务：需要消耗智能体的计算时间，同时产生回答质量、等待时间和运行成本

**决策变量**

- 每个智能体决定自己能够提供多少服务，以及能达到怎样的质量和速度
- 平台决定任务分给谁，以及一个任务是否需要依次调用多个智能体
- 系统不断调整内部评分和任务分配，直到没有智能体持续过载或闲置

**关键参数与状态**

- H：记录一个智能体在一段时间内的质量、速度、成本等表现；论文用函数空间表示这类连续变化的数据
- Yᵃ：智能体 a 实际能够做到的各种服务组合，例如更高质量通常可能需要更多时间或成本
- pᵃ(t)：平台在时刻 t 给智能体 a 的各项资源设置的内部稀缺分数，也叫影子价格
- dᵃ(α)：在当前任务分配方案下，平台希望智能体 a 承担的工作量
- W(α)：平台对整个方案的综合评价，包含回答质量、等待时间和运行成本

**研究时序**

1. 平台先根据当前任务量，查看每个智能体能提供多少服务。
2. 如果某个智能体收到的任务超过它能处理的数量，就提高它的内部稀缺分数；反之则降低。
3. 平台重新比较不同调用路径，把更多任务分给综合表现更合适的路径。
4. 重复以上过程；如果每次调整幅度不过大，系统最终会稳定在同一个分配方案。

### 公式与求解

- **智能体利润与供给：** `\pi_a(p)=\sup_{y\in Y^a}\langle p^a,y\rangle,\qquad \eta_a(p)=\underset{y\in Y^a}{\arg\max}\,\langle p^a,y\rangle`
  - πₐ 表示智能体 a 的内部收益，Yᵃ 表示它能提供的服务组合，pᵃ 是平台设置的内部评分。公式的意思是：智能体从自己能做到的方案中，选择内部评分最高的一个。
- **编排器预算约束：** `\sum_a \langle p^a,d^a(\alpha)\rangle \le \sum_a \pi_a(p)`
  - 左边是平台分配任务后需要占用的资源总分值，右边是所有智能体能够提供的资源总分值。平台不能安排超过系统承受能力的工作。
- **均衡出清：** `d^a(\alpha^*)=y^{a*},\qquad \forall a`
  - dᵃ 是平台想交给智能体 a 的任务量，yᵃ 是它能提供的服务量。稳定时，两者必须相等，也就是既不过载，也没有无故闲置。
- **价格与路由更新：** `p^+=\operatorname{Proj}_{\Delta}([p+\eta(d-y)]_+),\qquad \alpha^+=\operatorname{softmax}_{\beta}(V\cdot s(p,y))`
  - 第一部分表示：需求大于能力时提高内部评分，需求较少时降低；第二部分表示：平台更倾向选择综合表现好的调用路径，但不会一次把全部任务突然切过去。

**如何求解：** 原模型允许质量、时延和成本随时间连续变化，因此直接计算很困难。作者先把这些连续曲线近似成有限个数字，在简化后的模型中证明一定能找到稳定方案，再说明当近似越来越精细时，结果仍适用于原来的连续模型。如果每轮调整不会反应过度，那么算法会越来越接近同一个稳定方案。

### 主要结果

- 只要每个智能体可提供的方案不会过于跳跃，平台的综合评价也保持连续，系统就能找到一个稳定的任务分配方案。
- 在这个稳定方案下，想让某个用户或任务变得更好，通常会让其他部分变差，因此资源没有被明显浪费。
- 如果平台每次只做适度调整，而不是看到拥堵就大幅切换任务，迭代会逐步收敛。
- 平台可以调高或调低对时延、质量目标的重视程度，类似用控制旋钮把系统拉回目标状态。

### 局限与核验边界

- 论文假设服务能力可以比较平滑地调整，但现实中的模型选择、批处理和路由往往只能整块切换。
- 文中的价格是平台内部衡量资源紧张程度的分数，不是用户实际支付的 Token/API 价格。
- 论文暂时没有加入用户请求随机到达、真实排队、不同用户选择和多个平台竞争。
- **核验说明：** 模型、公式与结论依据可访问的 arXiv 全文核验；这里保留论文的理论结构，但未逐条复现全部技术假设和证明。
- **链接：** [论文页](https://arxiv.org/abs/2602.21255v2) · [PDF](https://arxiv.org/pdf/2602.21255v2)

<details><summary>英文原摘要（补充）</summary>

We establish a general equilibrium theory for systems of large language model (LLM) agents operating under centralized orchestration. The framework is a production economy in the sense of Arrow-Debreu (1954), extended to infinite-dimensional commodity spaces following Bewley (1972). Each LLM agent is modeled as a firm whose production set represents the feasible metric trajectories determined by its frozen model weights. The orchestrator is the consumer, choosing a routing policy over the agent DAG to maximize system welfare subject to a budget constraint evaluated at functional prices. We prove via Brouwer's theorem applied to a finite-dimensional approximation that every such economy admits at least one general equilibrium. A functional Walras' law holds, and we further establish welfare theorems, uniqueness and geometric convergence under a contraction condition. The framework admits a DSGE interpretation with SLO parameters as policy rates.

</details>

## 2. 稀疏 MoE LLM 的即插即用复制–量化负载均衡策略

> 英文原标题：A Replicate-and-Quantize Strategy for Plug-and-Play Load Balancing of Sparse Mixture-of-Experts LLMs

- **研究问题：** 当 MoE 大模型中的少数“专家模块”忙不过来、其他模块却很空闲时，怎样在不增加显存的情况下把工作分得更均匀？
- **文章怎么做：** 作者先统计每个专家模块实际收到多少 Token，找出最忙的专家；再暂时移除各个专家，观察模型准确率下降多少，从而找出对结果影响最小的专家。系统复制最忙的专家来分担工作，同时降低最不重要专家的存储精度，腾出复制所需的显存。
- **研究启示：** 这篇论文说明“最忙”不等于“最重要”。平台扩充服务能力时，既要看哪里排队最严重，也要看降低哪部分质量的代价最小。我们可以把专家模块看成服务器，进一步研究容量、服务质量、优先级和价格怎样一起决定。
- **作者：** Zijie Liu、Jie Peng、Jinhao Duan、Zirui Liu、Kaixiong Zhou、Mingfu Liang、Luke Simon、Xi Liu 等
- **来源/日期：** arXiv；2026-02-23；arXiv
- **研究类型：** 算法与实验；直接 LLM 服务研究；相关性评分 12

### 中文内容总结

MoE 大模型由多个分工不同的“专家模块”组成，每个 Token 只会被送到其中几个专家。现实中，一些专家经常非常拥堵，另一些却很空闲。作者发现，收到任务最多的专家不一定对回答质量最重要，于是提出 R&Q：复制最忙的专家来分担任务，同时压缩对结果影响较小的专家，腾出同样大小的显存。这个方法不需要重新训练模型，可以直接加到已经部署的系统上。

### 模型设定

**模型主线：** 显存总量不变：一边复制最忙的专家，增加处理能力；另一边压缩对结果影响较小的专家，省出空间。它主要是一种系统配置办法，不是用户和平台之间的定价博弈。

**参与者 / 系统组件**

- 包含 p 个 MoE 模块、每个模块有 m 个专家的稀疏 MoE 模型
- 任务分配器：每个 Token 会被送到 k 个专家模块处理
- R&Q 配置器：识别重载专家和低重要性专家，并重新分配显存

**决策变量**

- 选择每个 MoE 层中需要复制的重载专家
- 选择可以压缩存储精度、同时尽量不影响回答质量的专家
- 静态使用校准数据，或在动态场景中按历史窗口更新复制与量化配置

**关键参数与状态**

- nᵢⱼ：第 i 个 MoE 模块中被路由到专家 j 的 Token 数
- n：数据集中的 Token 总数；k：每个 Token 激活的专家数；m：专家总数
- lᵢ：模块 i 的负载不均衡分数，衡量最大专家负载相对理想平均负载的倍数
- 专家重要性：移除该专家后模型准确率或任务性能的下降
- 量化位数与专家副本数：共同决定显存使用、质量损失和并行容量

**研究时序**

1. 先用一小批样例运行模型，记录每个专家收到多少 Token。
2. 找出最忙的专家；再逐个暂时移除专家，观察准确率下降多少，以判断谁最不重要。
3. 复制最忙的专家，并压缩低重要性专家，以抵消新增副本占用的显存。
4. 部署时把原本集中到重载专家的 Token 分配给原专家及其副本并行执行。

### 公式与求解

- **负载不均衡分数：** `l_i=\frac{m\max_j n_{i,j}}{nk}`
  - nᵢⱼ 是第 i 层的专家 j 收到的 Token 数。这个分数比较“最忙专家的实际任务量”和“如果平均分配时每个专家应有的任务量”；等于 1 表示完全均匀，越大表示越拥堵。
- **固定显存替换逻辑：** `\text{新增重载专家副本占用的空间}\;\approx\;\text{量化低重要性专家释放的空间}`
  - 论文通过“复制—量化”成对操作，使总内存预算基本保持不变。

**如何求解：** 这篇论文没有求一个复杂的数学最优解，而是使用一套清楚的选择规则：按 Token 数找最忙的专家，按暂时移除后的准确率损失找最不重要的专家，然后执行复制和压缩。动态版本会定期查看最近一段时间的数据，再更新选择。

### 主要结果

- 更新版论文摘要报告，R&Q 可将专家负载不均衡最多改善约 1.4 倍。
- 在测试模型和数据集上，模型准确率变化控制在约 ±0.6% 范围内。
- 重载程度与专家重要性并不等价，因此可以用低重要性专家的存储让渡支持重载专家扩容。
- 方法训练后即可使用，对已有稀疏 MoE 部署的侵入性较低。

### 局限与核验边界

- Token 路由由预训练模型给定，没有研究用户需求、价格或战略行为。
- 复制与量化是一种系统启发式，未给出全局最优容量配置保证。
- 质量损失取决于模型、任务和校准数据；历史窗口也可能无法及时跟踪分布突变。
- **核验说明：** 模型公式与机制依据可访问的 OpenReview 全文核验，最新性能数字依据更新后的 arXiv 摘要；不同版本之间的实验表述可能存在变化。
- **链接：** [论文页](https://arxiv.org/abs/2602.19938v1) · [PDF](https://arxiv.org/pdf/2602.19938v1)

<details><summary>英文原摘要（补充）</summary>

Sparse Mixture-of-Experts architectures are increasingly used to scale large language models efficiently, but often suffer from severe load imbalance across experts. We present a systematic analysis of expert routing during inference and identify that load imbalance persists and worsens with larger batch sizes, selection frequency does not reliably reflect expert importance, and workload and importance can be estimated using a small calibration set. We propose Replicate-and-Quantize, a training-free and near-lossless framework for dynamic workload rebalancing. In each layer, heavy-hitter experts are replicated to increase parallel capacity, while less critical experts and replicas are quantized to remain within the original memory budget. We also introduce a Load-Imbalance Score to compare heavy-hitter load with an equal allocation baseline. Experiments show up to 1.4x reduction in imbalance with accuracy maintained within +/-0.6%.

</details>

## 3. 面向消费级设备混合 CPU–GPU LLM 推理的自动张量调度

> 英文原标题：Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices

- **研究问题：** 个人电脑的 GPU 放不下整个大模型时，哪些数据应该留在 GPU、哪些放在 CPU，才能让回答生成得更快？
- **文章怎么做：** 作者先测量模型中每一块数据在 CPU 和 GPU 上分别要运行多久、占多少空间、搬运一次要花多少时间；然后用动态规划逐步比较各种放置方案，在有限显存内选出总耗时最短的一种。运行过程中，如果电脑负载明显变化，系统会重新计算是否值得临时把某些数据搬到 GPU。
- **研究启示：** 这篇论文说明，计算资源分配不能只看 GPU 是否更快，还要把数据搬运和频繁切换的时间算进去。对我们的研究来说，可以把 GPU 看成有限服务容量，再加入用户到达、等待时间要求和价格，研究平台怎样分配不同等级的服务。
- **作者：** Yangyijian Liu、Hongyi Ye、Mingyang Li、Wu-jun Li
- **来源/日期：** arXiv；首次发布 2026-07-11；最近更新 2026-07-14；arXiv
- **研究类型：** 系统优化模型；直接 LLM 服务研究；相关性评分 10

### 中文内容总结

ATSInfer 解决的是个人电脑显存不足的问题。大模型由许多数据块组成，论文把这些数据块称为“张量”。系统先测量每个数据块在 CPU 和 GPU 上运行需要多久、占多少显存以及搬运需要多久，再决定哪些数据长期放在 GPU。真正运行时，系统还会查看电脑当前是否繁忙，判断临时搬动某些数据能否节省时间。作者把系统接入 llama.cpp，并在普通消费级设备上测试，结果显示输入处理和逐字生成速度都有提升。

### 模型设定

**模型主线：** 模型分两步：先决定平时哪些数据长期留在 GPU；再根据电脑当时的忙闲程度，决定是否临时搬动数据。它既计算 GPU 带来的加速，也扣除搬运数据和来回切换的时间。

**参与者 / 系统组件**

- 消费级 GPU：速度快但显存容量 M 有限
- CPU 与主存：容量较大但计算更慢
- 按顺序执行的 n 个模型数据块；论文把这种数据块称为张量
- ATSInfer 调度器：离线分析放置，在线响应硬件负载

**决策变量**

- 长期放置选择 bᵢ：数据块 i 平时留在 CPU 还是 GPU
- 本轮运行选择 rbᵢ：这一次生成回答时，数据块 i 实际在哪个设备上计算
- 是否在负载变化超过阈值后触发重新分析与迁移

**关键参数与状态**

- sᵢ：张量 i 的显存占用；M：可用 GPU 显存预算
- tᶜᵢ、tᵍᵢ：张量 i 在 CPU 和 GPU 上的执行时间
- rᵢ = tᶜᵢ − tᵍᵢ：把张量放到 GPU 带来的计算收益
- cᵢ：相邻张量执行后端变化时的激活传输成本
- wᵢ：权重传输时间；seg(j,i)：可用于掩盖传输的计算重叠窗口

**研究时序**

1. 正式运行前先做测量：记录每个数据块的大小、CPU/GPU 运行时间和搬运速度。
2. 逐步比较不同组合：在显存限制内挑选长期放在 GPU 的数据，同时避免频繁来回切换。
3. 每轮推理前读取当前负载，估计张量临时迁移后的净时延。
4. 在线动态规划决定运行后端；只有负载偏离超过阈值且间隔足够长时才重调度。

### 公式与求解

- **静态张量放置：** `\max \sum_i r_i\mathbf{1}\{b_i=\mathrm{GPU}\}-\sum_{i\ge 2}c_i\mathbf{1}\{b_i\ne b_{i-1}\}`
  - rᵢ 是数据块 i 放到 GPU 后节省的时间，cᵢ 是相邻数据块在不同设备运行时的搬运时间。公式就是“总加速时间减去来回搬运造成的损失”。
- **显存约束：** `\sum_i s_i\mathbf{1}\{b_i=\mathrm{GPU}\}\le M`
  - sᵢ 是数据块 i 占用的显存，M 是 GPU 总共能用的显存；选中的所有数据块加起来不能超过 M。
- **无法隐藏的传输时间：** `\delta_i=\max\{w_i-\operatorname{seg}(j,i),0\}`
  - wᵢ 是搬运时间，seg(j,i) 是搬运时可以同时进行其他计算、从而被遮住的时间；剩下无法遮住的部分才会真正让用户多等。
- **运行时总时延：** `T(rb)=\sum_i t_i(rb_i)+\sum_i c_i\mathbf{1}\{rb_i\ne rb_{i-1}\}+\sum_i\delta_i`
  - 一次回答的总等待时间，包括实际计算、CPU/GPU 之间切换，以及没有被其他计算遮住的数据搬运时间。

**如何求解：** 作者使用动态规划，也就是从第一个数据块开始，逐步记录“用了多少显存、当前在哪个设备、累计耗时多少”，只保留更好的选择，最后回头找出整条最省时的方案。长期放置需要比较数据块数量 n 和显存预算 M；运行时调整主要比较数据块之间的先后关系。

### 主要结果

- 在相同 GPU 显存预算下，相比 llama.cpp 基线，论文报告 prefill 吞吐最高提升约 1.94 倍、decode 最高提升约 3.29 倍。
- 静态放置避免只按单个张量收益选择而造成大量 CPU/GPU 边界切换。
- 在线负载感知迁移在硬件状态变化时使用空闲 GPU，同时用阈值避免频繁重配置。
- 方法同时覆盖稠密模型与 MoE 模型，并在 llama.cpp 上进行了系统实现。

### 局限与核验边界

- 研究场景主要是消费级设备和低并发请求，目标是单请求响应性，不是云端高并发队列。
- 目标函数主要最小化系统时延，没有平台收入、用户等待成本或价格决策。
- profiling 与调度依赖硬件和模型结构，部署环境改变时需要重新测量。
- **核验说明：** 模型设定、动态规划、复杂度和实验结果依据可访问的 arXiv 全文核验；性能数字是论文实验环境中的最好结果，不代表所有设备。
- **链接：** [论文页](http://arxiv.org/abs/2607.10183v2) · [PDF](https://arxiv.org/pdf/2607.10183v2)

<details><summary>英文原摘要（补充）</summary>

Running large language models on consumer devices such as laptops and desktops is challenging because model weights often exceed GPU memory capacity, making offloading inference necessary to extend effective model capacity with CPU memory. Existing offloading systems, however, typically rely on coarse layer-level or expert-level scheduling, which overlooks substantial heterogeneity among tensors within the same layer and adapts poorly to changing hardware load conditions on such devices. This paper presents ATSInfer, a hybrid CPU-GPU inference system for consumer devices that performs offloading at tensor granularity. ATSInfer combines static tensor placement with load-aware dynamic transfer, and introduces asynchronous CPU-GPU coordination to efficiently schedule hardware storage, data movement, and computation across heterogeneous backends. We implement ATSInfer and evaluate it on representative consumer platforms using both dense and MoE models. Compared with existing systems, ATSInfer improves prefill throughput by up to 1.94$\times$ and decode throughput by up to 3.29$\times$, while also increasing GPU utilization and making more effective use of PCIe bandwidth. These results show that ATSInfer can substantially improve the user experience of local LLM deployment on personal consumer devices.

</details>

## 最终审核说明

- 中文研究问题、方法、模型与结论优先依据可访问全文生成；未取得全文时会明确标注，不从摘要猜公式。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
