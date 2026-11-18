# 2026-11-18 LLM 服务系统每日文献简报

> 检索窗口：2026-11-17 至 2026-11-18（北京时间 / Asia/Shanghai）；本期确认 6 篇，其中直接 LLM 服务研究 6 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 在延迟目标下的GPU效率:对批量,KV-缓存配置和LLM推理的阶段意识规划的模拟研究

> 英文原标题：GPU Efficiency Under Latency Objectives: A Simulation Study of Batching, KV-Cache Allocation, and Phase-Aware Scheduling for LLM Inference

- **作者：** Bhavin Kotak
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-17；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 14
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7697758) · [DOI](https://doi.org/10.2139/ssrn.7697758)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

该预印 1.0 版本报告了大型语言模型 (LLM) 推理技术的吞吐量和成本增长,没有数据支持它们.本版本将它们撤回并报告一个服务节点的单独事件模拟,每一个假设都被写下来.模拟器在A100级加速器上运行了7B级解码器. 它的屋顶线成本模型通过阅读权重和关键值 (KV) 缓存来进行预填计算绑定和解码绑定.我们比较静态批量,动态请求级批量,连续批量与连接或页面的KV分配,碎片预填,以及8KV存储,该模型将其视为容量变化. 所有政策都有无效输入,内存耗尽,预期和排队时间的书面规则.主要的指标是SLO容量,最大的Poisson到达率,其中90%的提交请求达到1秒的时间到第一代令和0.1秒的输出代令目标. 我们预先注册了这个假设,即页面分配至少对连续保留最大序列长度相对的容量增加了一倍.在五种配对种子上,模拟容量比为3.77 (95%的信任间隔3.36至4.17),因此预先注册的判决得到了支持.在每个成本模型常数的两次变化下,平均比在2.63至6.45之间. 当连续预订仅覆盖提示加上1024代币时,它降至1.57.长提示时,降至1.77.碎片预填补增加了1.22.请求级批量甚至错过了每秒0.125请求的目标.所有结果都是模拟输出,而不是硬件测量.人工智能披露:生成人工智能用于准备此修订. 大型语言模型 (GitHub Copilot with Anthropic Claude) 批评了该方法,生成了实验代码,并起草并编辑了文本.在最后的通过中,同样的模型也编辑了论文的措辞和其Zenodo描述.每个报告的数字,表格和数字都是通过记录的实验结果编写的代码生成的;没有一个语言模型编写的.

### 英文原摘要

Version 1.0 of this preprint reported throughput and cost gains for large language model (LLM) inference techniques, and no data supported them. This version withdraws them and reports a discrete-event simulation of one serving node, with every assumption written down. The simulator runs a 7B-class decoder on an A100-class accelerator. Its roofline cost model makes prefill compute-bound and decode bound by reading the weights and the key-value (KV) cache. We compare static batching, dynamic request-level batching, continuous batching with contiguous or paged KV allocation, chunked prefill, and int8 KV storage, which the model treats as a capacity change. All policies share written rules for invalid inputs, memory exhaustion, preemption, and queue timeouts. The primary metric is SLO capacity, the largest Poisson arrival rate at which 90% of submitted requests meet a 1 s time-to-first-token and a 0.1 s time-per-output-token objective. We pre-registered the hypothesis that paged allocation at least doubles this capacity relative to contiguous reservation of the maximum sequence length. Over five paired seeds the simulated capacity ratio was 3.77 (95% confidence interval 3.36 to 4.17), so the pre-registered verdict is SUPPORTED. Under twofold changes of each cost-model constant the mean ratio ranged from 2.63 to 6.45. It fell to 1.57 when contiguous reservation covered only the prompt plus 1024 tokens, and to 1.77 for long prompts. Chunked prefill added a factor of 1.22. Request-level batching missed the target even at 0.125 requests per second. All results are simulation outputs, not hardware measurements. AI disclosure: Generative AI was used to prepare this revision. Large language models (GitHub Copilot with Anthropic Claude) critiqued the methodology, generated experiment code, and drafted and edited the text. In a final pass the same model also edited the wording of the paper and of its Zenodo description. Every reported number, table, and figure was produced by code from logged experiment results; none was written by a language model.

## 2. XAccel:限制指导的跨加速器输入优化,延迟,成本和能源效率

> 英文原标题：XAccel: Constraint-Guided Cross-Accelerator Inference Optimization for Latency, Cost, and Energy Efficiency

- **作者：** Wenyu Zhao、Boyuan Wang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-17；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 12
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7691850) · [DOI](https://doi.org/10.2139/ssrn.7691850)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 llm、slo、service-level objective、optimization。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

同样的机器学习模型可以由GPU和人工智能加速器提供,它们在吞吐量,价格,内存容量和功率上有多大差异,但最佳执行配置取决于模型,其尾延服务水平目标 (SLO),其内存足迹和必须承受的负载. 这篇论文介绍了XAccel,这是一个受限制指导的框架,在延迟,成本和能源预算下选择和调整异性加速器中的推理配置. XAccel (i) 从2,173次审核的MLPerf推理运行 (v4.0-v6.0) 中构建一个统一的,SLO知情的性能描述器,涵盖28种加速器类型和34个工作负载场景对,包括p95/p99延迟,时间至第一代标和时间至输出代标的百分比,以及88次重建的墙功率; (ii) 通过解决SLO-,内存和预算限制的成本-能量程序来选择配置 (iii) 将性能转移到未测量的加速器和模型,通过数据表以基层杆校准的弹性模型;以及 (iv) 在Azure LLM服务的一周生产轨迹下重新选择机队. 在30个工作负载-SLO设置中,选择最快,最便宜的每小时加速器或现有的H100加速器平均将每次推断成本提高56-152%与XAccel相比. 零射传输预测SLO有限的吞吐量,平均绝对百分比错误为28%,保留了94%的选择决定在1.6%的平均成本后悔,并且在4.5的测量之后发现了新模型的成本最佳加速器. 在实际生产负载下,XAccel将每周的成本降低69-82%和能源降低69-80%与LLC服务的H100车队相比,最高为0.51%的SLO风险分钟.

### 英文原摘要

The same machine learning model can be served by GPUs and AI accelerators that differ by more than an order of magnitude in throughput, price, memory capacity, and power, yet the best execution configuration depends jointly on the model, its tail-latency service-level objective (SLO), its memory footprint, and the load it must sustain. This paper presents XAccel, a constraint-guided framework that selects and adapts inference configurations across heterogeneous accelerators under latency, cost, and energy budgets. XAccel (i) builds a unified, SLO-aware performance descriptor from 2,173 audited MLPerf Inference runs (v4.0-v6.0) covering 28 accelerator types and 34 workloadscenario pairs, including p95/p99 latency, time-to-first-token and time-per-output-token percentiles, and wall power reconstructed for 88 runs; (ii) selects configurations by solving an SLO-, memory-, and budget-constrained cost-energy program over measured operating points; (iii) transfers performance to unmeasured accelerators and models through a datasheetinformed elasticity model with hierarchical anchor calibration; and (iv) re-selects fleets under week-long production traces of Azure LLM services. Across 30 workload-SLO settings, choosing the fastest, the cheapest-per-hour, or the incumbent H100 accelerator raises the cost per inference by 56-152% on average relative to XAccel. Zero-shot transfer predicts SLO-bounded throughput with 28% mean absolute percentage error and preserves 94% of selection decisions at 1.6% mean cost regret, and the cost-optimal accelerator for a new model is found after 2.2 measurements instead of 4.5. Under real production load, XAccel lowers weekly cost by 69-82% and energy by 69-80% relative to a peak-provisioned H100 fleet for LLM services, with at most 0.51% SLO-risk minutes.

## 3. HyCoInfer:对异性GPU-FPGA架构的大型语言模型的云端协作推理

> 英文原标题：HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures

- **作者：** Zewen Huang、Xiangwen Zhuge、Yingkun Hu、Zheng Yang、Qiang Ma
- **来源/日期：** arXiv；2026-11-17；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.22086v1) · [PDF](https://arxiv.org/pdf/2611.22086v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、kv cache。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大语言模型 (LLM) 服务主要依赖于云GPU,但自动降级解码是内存绑定的,并且经常使其算术单元未充分利用.边缘FPGAs提供了有吸引力的解码效率,但不适合单独维持高竞争性服务工作负载. 本文介绍了HyCoInfer,一个多元化的云端服务系统,将预填分配到云GPU,并在云GPU和边缘FPGA中分发解码.该设计解决了实际卸载的三个障碍:多元化加速器的容量平衡,大KV缓存跨越一个有限的宽区域链接,以及多元化执行增加的延迟. HyCoInfer将FPGA解码能力纳入GPU预填/解码角色分区,并根据队列负载,提示长度和网络状态进行请求.它进一步结合了层次管道传输,解码器侧预计算和基于残余向量量化的带宽适应性KV缓存压缩. 我们使用两台NVIDIA V100 GPU和AMD Xilinx Alveo U280实现HyCoInfer,并对其进行100-1000Mbps链接的评估. 在不同网络条件和工作负载中,该系统提高了总体服务能力,最大的收益是通信密集任务,并减少了每次请求的能量.

### 英文原摘要

Large language model (LLM) serving relies predominantly on cloud GPUs, yet autoregressive decoding is memory-bound and often leaves their arithmetic units underutilized. Edge FPGAs offer attractive decoding efficiency, but are ill suited to sustaining a high-concurrency serving workload alone. This paper presents HyCoInfer, a heterogeneous cloud-edge serving system that assigns prefill to cloud GPUs and distributes decoding across cloud GPUs and edge FPGAs. The design addresses three barriers to practical offloading: capacity balancing across heterogeneous accelerators, the large KV cache crossing a constrained wide-area link, and the latency added by heterogeneous execution. HyCoInfer incorporates FPGA decode capacity into GPU prefill/decode role partitioning and places requests according to queue load, prompt length, and network state. It further combines layer-wise pipelined transfer, decoder-side precomputation, and bandwidth-adaptive KV cache compression based on residual vector quantization. We implement HyCoInfer using two NVIDIA V100 GPUs and an AMD Xilinx Alveo U280 and evaluate it over 100-1000 Mbps links. At 500 Mbps, HyCoInfer delivers up to 4.11 times the request goodput of cloud-only vLLM and reduces mean end-to-end latency by up to 61.1%. Across different network conditions and workloads, the system improves overall serving capacity, with the largest gains on communication-intensive tasks, and reduces per-request energy.

## 4. 在国内芯片和框架上推进边界代理模式

> 英文原标题：TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- **作者：** Xingchen AGI Lab、:、Baotian Hu、Bingkai Yang、Boyang Wang、Changzai Pan、Chao Lyu、Chao Wang 等
- **来源/日期：** arXiv；2026-11-17；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.22115v1) · [PDF](https://arxiv.org/pdf/2611.22115v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、scheduling、optimization。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

我们介绍了Xing 4,一系列大型语言模型,通过Ascend模型架构和培训基础设施的协调进步,扩大了TeleChat流程.本报告描述了该系列背后的设计原则和系统工程,涵盖了建筑选择,大规模预训,推理和代理后训练. 我们研究如何稀疏的激活,注意力设计,模型深度和宽度以及推测式解码平衡模型容量与计算,内存访问和执行总额.我们的预训基础设施基于MindSpore HyperParallel,结合了对拓知识的混合碎片化,高效的分布式优化器执行和长序列工作负载和激活内存的协调管理. 这些机制支持在8,192 Ascend 910C卡上进行285B参数模型的预训练,为建筑和系统研究提供了具体的设置.为后培训,我们推出了TeleGym,一个统一的代理执行平台,将执行,评估和轨迹构建与政策优化联系起来. 分散的异步执行,有限的过量样本处理和部分部署都适应异质任务持续时间,同时保持政策更新中的轨迹连续性.这些进步共同建立了一个以升级为导向的培训基础,以继续发展Xing4在模型尺度和越来越苛刻的推理和代理工作负载上.

### 英文原摘要

We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model depth and width, and speculative decoding balance model capacity with computation, memory access, and execution overhead. Our pretraining infrastructure builds on MindSpore HyperParallel, combining topology-aware hybrid sharding, efficient distributed optimizer execution, and coordinated management of long-sequence workloads and activation memory. CPU affinity and core isolation further reduce host scheduling interference. Together, these mechanisms support the pretraining of a 285B-parameter model on 8,192 Ascend 910C cards, providing a concrete setting for the architectural and systems studies. For post-training, we introduce TeleGym, a unified agent execution platform that connects execution, evaluation, and trajectory construction to policy optimization. Disaggregated asynchronous execution, bounded oversampling, and partial rollout accommodate heterogeneous task durations while preserving trajectory continuity across policy updates. Together, these advances establish an Ascend-oriented training foundation for the continued development of Xing 4 across model scales and increasingly demanding reasoning and agent workloads.

## 5. 在超高分辨率远程传感中获得无需培训的有效证据的统一空间概率

> 英文原标题：GeoJeV: Unified Spatial Probability for Training-Free Efficient Evidence Acquisition in Ultra-High-Resolution Remote Sensing

- **作者：** Xinyi Niu、Lingfeng Chen、Jiehua Zhang、Panhe Hu、Li Liu、Zhen Liu、Yongxiang Liu
- **来源/日期：** arXiv；首次发布 2026-11-06；最近更新 2026-11-17；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2611.08879v2) · [PDF](https://arxiv.org/pdf/2611.08879v2)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、large language models、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

超高分辨率 (UHR) 远程传感图像提供丰富的空间细节,但对准确和高效的多模式理解构成挑战.现有的证据采集方法选择性地探索相关的图像区域,但主要依赖于生成多模式的大语言模型 (MLLM) 进行中间搜索控制. 然而,从人类反中增强学习 (RLHF) 主要将这些模型与人类首选的响应结合起来,而不是明确优化区域级相关性判断,而重复自动降低解码引入了额外的计算费用. 为了解决这些局限性,我们提出了GeoJeV,这是一个无培训的方法,该方法将证据采集作为基于空间概率的决策. 在每个评估区域中,一个结的JeV模型产生了候选地区的概率分布. 具体来说,区域排名优先考虑候选地区,Sparse Branch通过稀有概率支持可适应地确定分支宽度,而Deepth Gate则根据分支稀度和分布度控制精炼深度. 通过通过通过共享分布协调搜索优先级,分支宽度和精炼深度,GeoJeV减少了对RLHF一致生成的依赖,并消除了中间解码.LRS-GRO,MME-RealWorld-RS和LRS-VQA的实验分别达到60.59%,52.79%和34.32%. 在三个基准中,GeoJeV提高了Qwen3-VL-8B的平均准确性为 +5.32pp,每次问题只增加1.12秒,同时实现了7.8倍的推断速度.

### 英文原摘要

Ultra-high-resolution (UHR) remote sensing imagery provides rich spatial details but poses challenges for accurate and efficient multimodal understanding. Existing evidence acquisition methods selectively explore relevant image regions, yet largely rely on generative multimodal large language models (MLLMs) for intermediate search control. However, reinforcement learning from human feedback (RLHF) primarily aligns these models with human-preferred responses rather than explicitly optimizing region-level relevance judgments, while repeated autoregressive decoding introduces additional computational overhead. To address these limitations, we propose GeoJeV, a training-free method that formulates evidence acquisition as spatial probability-driven decision making. At each evaluated region, a frozen JeV model produces a probability distribution over candidate regions. Specifically, Region Rank prioritizes candidate regions, Sparse Branch adaptively determines branching width through sparse probability support, and Depth Gate controls refinement depth based on branch sparsity and distribution concentration. By coordinating search priority, branching width, and refinement depth through a shared distribution, GeoJeV reduces reliance on RLHF-aligned generation and eliminates intermediate decoding. Experiments on LRS-GRO, MME-RealWorld-RS, and LRS-VQA achieve accuracies of 60.59%, 52.79%, and 34.32%, respectively. Across the three benchmarks, GeoJeV improves the average accuracy of Qwen3-VL-8B by +5.32pp with only 1.12 additional seconds per question, while achieving a 7.8-fold inference speedup over the recent method.

## 6. 有趣搜索和结构化的SAT搜索弱的Schur分区

> 英文原标题：FunSearch and Structured SAT Search for Weak Schur Partitions

- **作者：** Rebecca Vicenzi、Pablo Christofferson、Caleb Hartman、Jingxuan Feng、Suleman Khan、Omar M. Elshinawy、Eric Ramos
- **来源/日期：** arXiv；2026-11-17；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](http://arxiv.org/abs/2611.22032v1) · [PDF](https://arxiv.org/pdf/2611.22032v1)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、priority。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

舒尔的弱问题问,连续整数间隔有多大可以分为一个固定数量的类,没有类包含一个单色的解决方案 $a+b=c$与 $a\neq b$. 我们调查FunSearch,一个由大型语言模型指导的进化程序搜索方法,是否可以发现有效的构建策略来解决这个经典的结合式问题. 在我们的适应中,FunSearch开发了一个固定贪解决器使用的优先函数,而单独的有效性检查强制执行虚弱的无数条件.这种方法与两个,三个和四个类的已知精确值相匹配,达到 $WS ((5) \geq195 $.然后我们探索了基于SAT的补充方法. 根据Fred Rowley (Rowley,2026) 提供的207个元素结构信息,我们的SAT搜索产生并验证了 $\{1,\ldots,207\}$的有效五级分区. 这两种方法的对比也揭示了我们FunSearch公式的局限性:它的贪解决器做出了本地,不可逆转的决定,而SAT可以在整个分区中执行全球结构.

### 英文原摘要

The weak Schur problem asks how large an interval of consecutive integers can be partitioned into a fixed number of classes with no class containing a monochromatic solution to $a+b=c$ with $a\neq b$. We investigate whether FunSearch, an evolutionary program-search method guided by a large language model, can discover effective construction strategies for this classical combinatorial problem. In our adaptation, FunSearch evolves a priority function used by a fixed greedy solver, while a separate validity check enforces the weakly sum-free condition. This approach matches the known exact values for two, three, and four classes and reaches $WS(5)\geq195$. We then explore a complementary SAT-based approach. Guided by structural information from a 207-element construction communicated by Fred Rowley (Rowley, 2026), our SAT search produces and verifies a distinct valid five-class partition of $\{1,\ldots,207\}$. Thus the strongest construction obtained in this project reaches $WS(5)\geq207$, eleven integers beyond the best published lower bound of 196. The contrast between the two approaches also exposes a limitation of our FunSearch formulation: its greedy solver makes local, irreversible decisions, whereas SAT can enforce global structure across the whole partition.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
