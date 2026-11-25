# 2026-11-25 LLM 服务系统每日文献简报

> 检索窗口：2026-11-24 至 2026-11-25（北京时间 / Asia/Shanghai）；本期确认 11 篇，其中直接 LLM 服务研究 11 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 诺恩:环境长度知情优化重量和KV缓存配置用于卸载LLM推理

> 英文原标题：Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference

- **作者：** Naoto Sugiura、Hiroki Matsutani
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 11
- **链接：** [论文页](http://arxiv.org/abs/2611.32295v1) · [PDF](https://arxiv.org/pdf/2611.32295v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

卸载模型重量和关键值 (KV) 缓存用于托管内存使大型语言模型 (LLM) 在单个内存限制的GPU上运行.随着解码过程中KV缓存增长,GPU内存需求以及KV缓存转移和注意计算的成本发生变化. 然而,现有的卸载方法通常使用静态计算分配和模型权重和KV缓存的配置,防止它们适应这些变化并降低推理性能. 我们建议Norn,一个意识到环境长度的卸载LLM推理方法. 基于线下配置文件,诺恩在子层级上进行计算任务和配置,预先计算多个执行计划及其交换点.在解码过程中,诺恩随着语境长度的增加而切换计划,在不提前知道输出长度的情况下重叠计算和数据传输. 对于预填,诺恩采用主要运营商的碎片预填,以避免重量重复转移,并自动选择碎片大小.在两个单GPU系统上使用Qwen3-14B和Qwen3-32B的实验显示,在 Pipelined Sharding 上的端到端延迟增速为16.8$\times$和已知输入和输出长度的Oracle 变量增速为4.2$\times$.

### 英文原摘要

Offloading model weights and the key-value (KV) cache to host memory enables large language models (LLMs) to run on a single memory-constrained GPU. As the KV cache grows during decoding, GPU memory requirements and the costs of KV cache transfers and attention computation change. However, existing offloading methods generally use static computation assignments and placements of model weights and the KV cache, preventing them from adapting to these changes and degrading inference performance. We propose Norn, a context-length-aware offloaded LLM inference method. Based on offline profiling, Norn co-optimizes computation assignments and placements at the sublayer level, precomputing multiple execution plans and their switching points. During decoding, Norn switches plans as context length increases, overlapping computation and data transfers without knowing the output length in advance. For prefill, Norn employs operator-major chunked prefill to avoid repeated weight transfers and automatically selects the chunk size. Experiments with Qwen3-14B and Qwen3-32B on two single-GPU systems show up to a 16.8$\times$ speedup in end-to-end latency over Pipelined Sharding and a 4.2$\times$ speedup over its oracle variant with known input and output lengths.

## 2. LoomKV:从GPU内存到SSD进行无损KV缓存压缩,用于LLM服务

> 英文原标题：LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving

- **作者：** Wentao Zhu、Ziao Sheng、Peng Deng、Huiqi Hu、Xuan Zhou、Xing Wei、Zhuang Wang
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.32954v1) · [PDF](https://arxiv.org/pdf/2611.32954v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、llm serving、kv cache。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 服务引擎将关键/值 (KV) 缓存从GPU内存中卸载,以托管DRAM和SSD,以便多转和代理请求可以重复使用即时前置.容量然后将服务限制在两个层次上:外部层次在驱逐之前控制了前置重复使用,而GPUKV池限制了同时长期请求,损失压缩改变了KV值和输出. 在未修改的引擎上,LoomKV将无损的KV压缩带到外部层 (层模式) 和GPU池 (池模式) 上.使用BF16高字节 (标志和上方七个指标比特) 的每头两级3位代码,LoomKV将BF16KV存储在九个模型中0.71的原始尺寸和FP8KV0.85-0.87. 在层次模式下,TileStream 写出精确长度的记录,随着载荷路径的长度回复,保持层次存储,排放和预收的长度不变,并将带来的记录直接压缩到分散的GPU页面中.在积分模式下,FragPack 将变量长度的记录包装到更小的共享预算GPU页面中,由一个合并的解码注意内核在BF16上的FlashAttention-3更快地读取. 通过LMCache和vLLM构建,LoomKV使压缩层在 AgentX 上表现为1.4倍大的原始层次:在LMCache的LRU悬崖上,层次模式提供2.7-3.6倍的原始的好输出和1.9-3.1倍的低平均时间到第一代币 (TTFT),在其他模拟替换政策下,相同地移动悬崖,并通过SSD到DRAM推广削减重复提示的TTFT到1.7倍. 当层次保持工作集时,积分模式适用于1.31-1.34x的GPU代币,允许12个长时间的请求,大致是原始的队列和 goodput 在 8. 在AI IDE 轨迹上,在两个层次和 GPU 池被限制,层次和积分模式提高 goodput 的1.24x和1.59x. 在原装容量足够的情况下,压缩成本最高为2.2%的吞吐量;级别模式与原装级别的比特精确,而池组模式与FlashAttention-3的数值准确性相匹配.

### 英文原摘要

Large language model (LLM) serving engines offload the key/value (KV) cache from GPU memory to host DRAM and SSD so multi-turn and agent requests can reuse prompt prefixes. Capacity then limits service at two levels: external tiers govern prefix reuse before eviction, while the GPU KV pool bounds concurrent long requests, and lossy compression alters KV values and outputs. LoomKV brings lossless KV compression to both external tiers (tier mode) and the GPU pool (pool mode) on an unmodified engine. Using a calibrated per-head two-level 3-bit code over BF16 high bytes (sign and upper seven exponent bits), LoomKV stores BF16 KV at 0.71 of its raw size across nine models and FP8 KV at 0.85-0.87. In tier mode, TileStream writes exact-length records with length readback off the load path, leaving tier storage, eviction, and prefetch unchanged, and decompresses fetched records straight into scattered GPU pages. In pool mode, FragPack packs variable-length records into smaller shared-budget GPU pages read in place by a fused decode-attention kernel faster than FlashAttention-3 on BF16. Built with LMCache and vLLM, LoomKV makes compressed tiers act as 1.4x larger raw tiers on AgentX: across LMCache's LRU cliff, tier mode delivers 2.7-3.6x raw's goodput and 1.9-3.1x lower mean time-to-first-token (TTFT), shifts the cliff identically under other simulated replacement policies, and cuts repeated-prompt TTFT up to 1.7x via SSD-to-DRAM promotion. When tiers hold the working set, pool mode fits 1.31-1.34x as many GPU tokens, admitting 12 long requests with roughly raw's queue and goodput at 8. On an AI IDE trace where both tiers and the GPU pool are constrained, tier and pool modes raise goodput by 1.24x and 1.59x. Where raw capacity suffices, compression costs at most 2.2% throughput; tier mode is bit-exact with raw tiers, and pool mode matches FlashAttention-3's numerical accuracy.

## 3. 复制:服务的LLM代理人联合请求和代表安排

> 英文原标题：RePrism: Joint Request and Representation Scheduling for LLM Agent Serving

- **作者：** Xijiang Shen、Aoli Zhu、Yanbo Tan、Xiyuan Hu、Huailiang Tan
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.32545v1) · [PDF](https://arxiv.org/pdf/2611.32545v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、scheduling。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

代理工作流经常多次调用大型语言模型.当服务系统看到依赖性时,它可以使用它们来安排请求和缓存可重复使用的内容,提高工作流的执行效率.以前的工作主要集中在订单请求或在固定缓存方案下管理共享资源上. 然而,指定模型行为的可重复使用提示可能具有多个表示.我们介绍了RePrism,一个服务系统,共同选择准备服务的请求和使用提示的符合条件的表示.它的目标是提高吞吐量和缩短会议完成时间 (SCT). 编程器通过结合每个对的即时值和基于可见工作流程的未来值的估计来排列请求和表示的对.资源经理将GPU内存分配给LoRA适配器和缓存关键值状态.随着内存压力变化,它还协调它们的录取和驱逐. 我们将RePrism与S-LoRA进行动态工作负载比较,其到达速度为每秒1.8次,达到1.37倍的请求吞吐量,并将P95SCT减少4.10倍.在控制负载下,RePrism将与S-LoRA相比的平均时间减少5.26倍. 在控制的工作负载上,RePrism的联合评分达到2.7%更高的请求吞吐量和12.3%较低的平均SCT,

### 英文原摘要

Agentic workflows often invoke large language models multiple times. When the dependencies are visible to the serving system, it can use them to schedule requests and cache reusable content, improving workflow execution efficiency. Prior work has largely focused on ordering requests or managing shared resources under a fixed caching scheme. A reusable prompt that specifies model behavior, however, can have multiple representations. We present RePrism, a serving system that jointly selects which ready request to serve and which eligible representation of its prompt to use. Its goal is to improve throughput and shorten session completion time (SCT). The scheduler ranks pairs of requests and representations by combining each pair's immediate value with an estimate of its future value based on the visible workflow. The resource manager allocates GPU memory to both LoRA adapters and cached key-value states. It also coordinates their admission and eviction as memory pressure changes. We compare RePrism with S-LoRA on a dynamic workload with an arrival rate of 1.8 sessions per second, and it achieves 1.37 times the request throughput and reduces P95 SCT by a factor of 4.10. Under controlled load, RePrism reduces mean time to first token by a factor of 5.26 relative to S-LoRA. On a controlled workload, RePrism's joint scoring achieves 2.7% higher request throughput and 12.3% lower mean SCT than a policy that ranks requests before selecting their representations.

## 4. 无线OptSG:无线资源分配的多代理优化框架

> 英文原标题：Wireless-OptSG: A Versatile Multi-Agent Optimization Framework for Wireless Resource Allocation

- **作者：** Wenhe Zhang、Xin Li、Hanzhi Chen、Chau Yuen
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](http://arxiv.org/abs/2611.32105v1) · [PDF](https://arxiv.org/pdf/2611.32105v1)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、large language models、resource allocation、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

预计6G无线网络将适应不同部署场景的异质服务需求,从而导致物理层资源分配问题,具体目标和局限性取决于场景.大型语言模型 (LLM) 和代理系统的最新进展可以解释无线域规格,并将执行反纳入优化. 然而,将语言级推理转化为可行的,高质量的资源分配仍然是一个挑战,因为候选人需要在反复搜索过程中满足精确的数学约束.这项工作提出了无线优化解决方案生成器 (Wireless-OptSG),用于物理层资源分配的多元代理框架. 无线OptSG组织优化作为一个反驱动的候选人搜索,由静态的地标提示和不断发展的优化历史指导. 在嵌入式的外部内部循环中,并行代理人探索解决方案轨迹并定期交换高质量的记录来指导候选人生成. 可行的初始化使用可执行的优化原始化,而一个层次的维修管道恢复可行性,解决方案依赖的环境改善保留记录的信息性. 在完美和不完美的道状态信息下进行四项代表性任务的实验表明,无线OptSG实现了与场景特定的最先进解决方案 (SOTA) 的性能相比,在某些设置中超越SOTA,并且始终优于通用基线,证明其作为未来无线网络的可转移优化框架的潜力.

### 英文原摘要

6G wireless networks are expected to accommodate heterogeneous service requirements across diverse deployment scenarios, giving rise to physical-layer resource allocation problems with scenario-dependent objectives and constraints. Recent advances in large language models (LLMs) and agent systems can interpret wireless-domain specifications and incorporate execution feedback into optimization. However, translating language-level reasoning into feasible, high-quality resource allocations remains challenging, since candidates need to satisfy precise mathematical constraints throughout iterative search. This work proposes the Wireless Optimization Solution Generator (Wireless-OptSG), a versatile multi-agent framework for physical-layer resource allocation. Wireless-OptSG organizes optimization as a feedback-driven candidate search guided by a static meta-prompt and an evolving optimization history. In a nested outer-inner loop, parallel agents explore solution trajectories and periodically exchange high-quality records to guide candidate generation. Feasible initialization uses executable optimization primitives, while a tiered repair pipeline restores feasibility and solution-dependent context improves retained-record informativeness. Experiments on four representative tasks under perfect and imperfect channel state information show that Wireless-OptSG achieves performance comparable to scenario-specific state-of-the-art (SOTA) solvers, exceeds SOTA in some settings, and consistently outperforms generic baselines, demonstrating its potential as a transferable optimization framework for future wireless networks.

## 5. 无阻延期:通过JAMN机器人支持学生,这是一个基于RAG的移动政策助理

> 英文原标题：Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded Policy Assistant

- **作者：** Mark Farinas、Alesandra Garcia、Maria Reyes、Jethro Nueva、Nawaf Qureshi、Mahmoud Elsaadany、Shokry Shamseldin
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2611.32266v1) · [PDF](https://arxiv.org/pdf/2611.32266v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

在一些教育机构中,考试推迟过程的工作流程可能会缓慢,不方便和不一致,从而需要实施新的数字系统.本文介绍了Schedulater,一个用于管理大学考试推迟的移动应用程序. JAMN Bot 是一个集成到 Schedulater 的大型语言模型 (LLM) 驱动的聊天机器人,它提供了对文本意识的支持,以帮助用户了解推迟过程.该系统采用 Ollama (Llama 3.2 3B) 的检索增强代 (RAG) 管道来自主进行推断,这使得没有牺牲隐私的情况下能够基于政策的响应. 我们使用43项基准标准评估系统,包括考试推迟,隐私,规划,跨政策和对抗性和范围之外的问题, 随后,我们使用了GPT-5.4的LLM-as-a-judge方法,显示了与我们的评级器的轻微到中等的调整,从而改善了答案质量,并对 Gemini 3.5 Flash和Qwen3.5 397B等组进行了排名检查.我们的研究结果显示了开放权重和边界模型之间的交易,以及LLM-人评估与答案质量的调整. 时间表证明了将轻量级的LLM纳入大学行政工作流程的可行性.

### 英文原摘要

In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsistent, which creates the need to implement novel digital systems. This paper presents Schedulater, a mobile app for managing university exam deferrals. JAMN Bot is a Large Language Model (LLM)-powered chatbot integrated into Schedulater that provides context-aware support to help users understand the deferral process. The system features a Retrieval-Augmented Generation (RAG) pipeline using Ollama (Llama 3.2 3B) for self-hosted inference which enables policy-grounded responses without sacrificing privacy. We evaluate the system using a 43-item benchmark spanning Exam Deferral, Privacy, Scheduling, Cross-Policy, and Adversarial & Out-of-Scope questions, and report inter-rater agreement among our human evaluators alongside retrieval hit-rate metrics. Subsequently, we utilize an LLM-as-a-judge approach with GPT-5.4, revealing slight-to-moderate alignment with our raters that improves with answer quality, and check the ranking against a panel including Gemini 3.5 Flash and Qwen3.5 397B. The results of our study display trade-offs between open-weight and frontier models, as well as LLM-human evaluation alignment with answer quality. Schedulater demonstrates the feasibility of integrating lightweight LLMs into university administrative workflows with structured retrieval.

## 6. 我的代币去哪里?可验证的代币账单

> 英文原标题：Where Did My Tokens Go? Verifiable Token Billing for LLM Services

- **作者：** Jiayuan Du、Yebo Feng、Lin Zhang、Konglin Zhu
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2611.31806v1) · [PDF](https://arxiv.org/pdf/2611.31806v1)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、pricing、provider。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大语言模型 (LLM) 服务的用户收到代币账单,有有限的证据表明他们的通话承担了他们的费用.在经纪人介导的代理工作流程中,通话发生在授权后,并且账单证据跨越服务域.一个账单可以两次计算一个真实收据并省略另一个.有效的计量证据也可以归因于错误的执行. 我们介绍 \textsc{TokenProv},它使用验证的供应商接受来确定结算覆盖和验证代币费用.一个验证的因果历史将运行时间尝试与签署的政策联系起来,并联合签署的交付将意图,发送和接受绑定到同一通话.独立于账单提交的交付可以揭示被遗漏的通话. 审计师需要对可观察的接受和结算的收据进行一个对一个匹配.对于每个接受,一个共同的供应商关系将测量使用绑定到使用注册模型和服务规则的接受输入的缓存依赖执行,并根据定价规则检查收费. 为了限制服务途径的通用费用,提供商可以在可信的执行环境中使用认证的状态过渡,或者通过在结算前向证人提交收据,将证据生成推迟到审计.审计师从验证的费用中重新计算账单.我们证明审计的实质性与验证证的证据相比. 在五种模型中,通过签署的供应商收据实现了94.4--107.4%的基线吞吐量,每次请求可通过54-66ms的在线非LLM处理.在单独的八次重播中,推迟范围证明将前台协议时间从1.20\,s缩短到8.65\,ms (99.28\%).审计师拒绝所有1,600个有效签署的攻击查询在100个适应节目中.

### 英文原摘要

Users of large language model (LLM) services receive token bills with limited evidence of which calls incurred their charges. In broker-mediated agent workflows, calls arise after authorization and billing evidence spans service domains. A bill can count one genuine receipt twice and omit another. Valid metering evidence can also be attributed to the wrong execution. We present \textsc{TokenProv}, which uses authenticated provider acceptances to establish settlement coverage and verify token charges. An authenticated causal history links runtime attempts to the signed policy, and jointly signed handoffs bind intent, dispatch, and acceptance to the same call. Handoffs submitted independently of the bill can reveal omitted calls. The auditor requires a one-to-one match between observable acceptances and settled receipts. For each acceptance, a common provider relation binds metered usage to the cache-dependent execution of the accepted input using the registered model and serving rules, and checks the charge under the pricing rule. To limit serving-path overhead, providers can use attested state transitions in trusted execution environments or defer proof generation until audit by committing to witnesses in receipts before settlement. The auditor recomputes the bill from the verified charges. We prove audit soundness relative to authenticated evidence. Across five models, \textsc{TokenProv} with signed provider receipts achieves 94.4--107.4\% of baseline throughput with 54--66\,ms of online non-LLM processing per request. In a separate eight-call replay, deferring scoped proofs reduces foreground protocol time from 1.20\,s to 8.65\,ms (99.28\%). The auditor rejects all 1,600 validly signed attack queries across 100 adaptive episodes.

## 7. 透露但被忽略:人工智能调整风险评估中的披露率

> 英文原标题：Disclosed but Overlooked: Disclosure Prevalence in AI-Mediated Risk Review

- **作者：** Kun Li、Lin Hu、Xueyan Yin、Pei-Yu Chen
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-24；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7728239) · [DOI](https://doi.org/10.2139/ssrn.7728239)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、large language models、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

组织越来越依赖大型语言模型来识别需要进一步审查的风险. 然而,人工智能介导的选择可能反映出组织明确声明的优先事项之外的突出模式,潜在地将注意力转向常见而不是本地重要的事情. 这对依赖人工智能的组织产生了关注:一个可信的短名单可能仍然会留下其最重要的风险未经审查.通过将正式模型与受控实验结合起来,我们会检查人工智能调整的审查何时偏离组织的声明审查优先事项. 无论被要求选择高优先级的风险还是删除低优先级的风险,人工智能读者倾向于支持通常披露的风险进行进一步考虑,即使公司特定的证据表明不一样.当分配高优先级时,更有可能忽略更少的风险,而当分配低优先级时,更有可能保持共同的风险. 这些偏差发生在每个符合条件的风险都符合所需的选择数量时.仅仅改变公司行业描述也改变了选择,尽管风险段和优先事项相同.该研究通过展示授权选择如何重塑由披露的信息构成的议程,推进了基于注意力的AI中介审查. 它将组织优先事项的保护视为审查可靠性的重要方面.

### 英文原摘要

Organizations increasingly rely on large language models to identify risks requiring further review. However, AI-mediated selection may reflect patterns of salience beyond the organization's explicitly stated priorities, potentially directing attention toward what is common rather than what is locally important. This creates a concern for organizations relying on AI to direct attention: a plausible shortlist may still leave their most important risks unexamined. Combining a formal model with controlled experiments, we examine when AI-mediated review departs from an organization's stated review priorities. Whether asked to select high-priority risks or remove low-priority risks, AI readers tend to favor commonly disclosed risks for further consideration, even when company-specific evidence indicates otherwise. Less common risks are more likely to be omitted when assigned high priority, whereas common risks are more likely to remain when assigned low priority. These departures occur even when every qualifying risk fits within the requested number of choices. Changing only the company's industry description also alters selection despite identical risk passages and stated priorities. The study advances an attention-based account of AImediated review by showing how delegated selection can reshape the agenda formed from disclosed information. It identifies preservation of organizational priorities as an important dimension of review reliability.

## 8. 沉默的仲裁:大型语言模型如何解决与权力相冲突的指示

> 英文原标题：Silent Arbitration: How Large Language Models Resolve Co-Authoritative Conflicting Instructions

- **作者：** Sihyeon Lee、Jiwoo Kum、Jihun Song、Kyojun Choo、Chanwoo Kim、Chanjun Park
- **来源/日期：** arXiv；首次发布 2026-11-20；最近更新 2026-11-24；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](http://arxiv.org/abs/2611.27444v2) · [PDF](https://arxiv.org/pdf/2611.27444v2)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、large language models、priority。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型越来越多地收到有关角色,价值观,兴趣和沟通风格的高层指令.即使一个提示赋予他们同等权威,并且没有优先规则,这种指令也可能发生冲突.我们研究了共同权威的人格冲突,其中一个提示共同分配两个对立的人物. 在8种冲突类型中,基于发表的源材料和5个LLM,我们测量冲突承认,解决策略和方向立场.模型在72%的直接检查中承认不兼容性,但在仅22%的任务响应中明确表现出不兼容性,从而揭示了沉默的仲裁. 占占主导地位的比例为45%的双人响应,35%的妥协标签的响应保持了方向性倾斜.快速框架进一步改变了可见的仲裁形式,远远超过普通的表达式变化.这些发现表明,评估下列指令应该评估模型是否披露冲突,如何解决它们,以及它们的响应有利于哪个角色.

### 英文原摘要

Large language models increasingly receive high-level instructions about roles, values, interests, and communication style. Such instructions can conflict even when a prompt assigns them equal authority and provides no priority rule. We study co-authoritative persona conflict, in which a single prompt jointly assigns two opposing personas. Across eight conflict types grounded in published source material and five LLMs, we measure conflict acknowledgment, resolution strategy, and directional stance. Models acknowledge incompatibility in 72% of direct checks but explicitly surface it in only 22% of task responses, revealing silent arbitration. Dominance accounts for 45% of dual-persona responses, and 35% of compromise-labeled responses retain directional lean. Prompt framing further changes the visible form of arbitration substantially more than ordinary paraphrase variation. These findings show that evaluating instruction following should assess whether models disclose conflicts, how they resolve them, and which persona their responses favor.

## 9. 视觉思维:无需培训的活跃感知,用于计算和定位难以找到的物体

> 英文原标题：Visual Thinking: Training-Free Active Perception for Counting and Localizing Hard-to-Find Objects

- **作者：** Emil Kielar、Pratik Chaudhari
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](http://arxiv.org/abs/2611.31973v1) · [PDF](https://arxiv.org/pdf/2611.31973v1)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 foundation model、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

视觉基础模型可以仅基于文本提示,精确划分对象.然而,它们难以恢复小,隐蔽或原始文本描述不充分捕捉到外观的对象.视觉语言模型可以检查图像及其背景,它们可以提出更丰富的对象描述. 但是这些模型与精确的细分和本地化斗争.我们引入了视觉思维,这是一个无训练的框架,它通过循环反复的活跃感知循环结合了视觉语言模型和细分任何模型3 (SAM 3).在每次反复中,VLM提出使用图像,候选作物和过去的反复的历史的短名词短语. 一个控制器使用嵌入原始提示和提案之间的相似性,基于 entropy的验证优先级和提示的新奇性来排列这些短语.接下来,SAM 3使用提示来检测图像中的物体. 我们将检测进行连接,并使用SAM 3中获得的分数的权重平均值来更新每个对象的可信度分数.使用较窄的提示来检测的重量更大.我们为SAM 3提供可信的检测,作为正面的视觉示例,并将图像嵌在一起,以恢复混乱图像中的小物体. 与SAM3相比,视觉思维将计算平均绝对错误 (MAE) 降低约18在FSC-147和约8在CARPK上.它提高了FSCD-147和CARPK的平均精度 (AP) 超过12. 视觉思维 (Visual Thinking) 有固定或没有板的性能与Claude Opus 5.5相等于超高的推理力度,同时在单台桌面GPU上运行每张图像约为5.91秒,而通过其API为Claude每张图像约为46.53秒.

### 英文原摘要

Vision foundation models can precisely segment objects based solely on a text prompt. However, they struggle to recover objects that are small, occluded or whose appearance is poorly captured by the original textual description. Vision language models can examine the image and its context, they can propose richer descriptions of the objects to be detected. But these models struggle with precise segmentation and localization. We introduce Visual Thinking, a training-free framework that combines a vision-language model with Segment Anything Model 3 (SAM 3) through an iterative active perception loop. At each iteration, the VLM proposes short noun phrases using the image, candidate crops and history from past iterations. A controller ranks these phrases using embedding similarity between the original prompt and the proposal, an entropy-based verification priority and the novelty of the prompt. Next, SAM 3 uses prompts to detect objects in the image. We associate detections across iterations and update each object's confidence score using a weighted mean of scores obtained from SAM 3 with a larger weight for detections using narrower prompts. We supply confident detections as positive visual exemplars for SAM 3, and incorporate image tiling to recover small objects in cluttered images. We evaluate counting and localization on CARPK, FSCD-147, PixMo-Count, and OmniCount (Fruits). Compared with SAM 3, Visual Thinking reduces the counting mean absolute error (MAE) by about 18 on FSC-147 and about 8 on CARPK. It improves box average precision (AP) by more than 12 on FSCD-147 and CARPK. Visual Thinking, with fixed or no tiling, performs on par with Claude Opus 5.5 at extra-high reasoning effort, while running on single desktop GPU in about 5.91 seconds per image, compared to about 46.53 seconds per image for Claude through its API.

## 10. 在SAP S/4HANA中,人工智能驱动的金融分析:改善决策和金融转型

> 英文原标题：AI-Driven Financial Analytics in SAP S/4HANA: Improving Decision-Making and Finance Transformation

- **作者：** Nandini Nandipati
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-24；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7727505) · [DOI](https://doi.org/10.2139/ssrn.7727505)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 generative ai、resource allocation。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

企业金融团队越来越需要超越回顾性报告,向有关流动性,利能力,预测,控制和资源分配的及时,可解释的决定迈进. SAP S/4HANA提供了集成的交易基础,而SAP Analytics Cloud (SAC),SAP商业技术平台 (BTP),预测模型和生成人工智能可以扩大资金领导者可用的分析和决策支持能力. 然而,技术的可用性本身并不能建立业务价值:结果取决于数据质量,流程设计,集成,模型治理,用户信任以及衡量利益的学科.本文为SAP S/4HANA财务开发了一个人工智能驱动金融转型框架 (AIDFTF) 和一个人工智能驱动金融转型成熟模型 (AIFTMM). 该研究旨在作为一个概念性,集成性审查和框架开发论文. 它汇总了提供的六份研究指导文件,确定了反复存在的缺陷,将这些缺陷转化为可测试的假设,并提出混合方法验证协议. 该框架将金融数据基础,人工智能和分析能力,见解质量,决策效率,过程结果和业务价值实现联系在一起.七个假设涉及决策效率,预测准确性,过程效率,嵌入式分析成熟度,数据质量,生成人工智能决策支持以及见解质量的调解作用. 该论文指明了候选措施,阶段性验证计划,治理控制,使用案例优先事项以及说明性而非经验性商业案例模型. 该框架旨在指导未来实验工作和执行评估,而不是声称拟议的效应已经被证明.

### 英文原摘要

Enterprise finance teams increasingly need to move beyond retrospective reporting toward timely, explainable decisions about liquidity, profitability, forecasting, control, and resource allocation. SAP S/4HANA provides an integrated transactional foundation, while SAP Analytics Cloud (SAC), SAP Business Technology Platform (BTP), predictive models, and generative AI may extend the analytical and decision-support capabilities available to finance leaders. Yet technology availability alone does not establish business value: outcomes depend on data quality, process design, integration, model governance, user trust, and the discipline with which benefits are measured. This paper develops an AI-Driven Finance Transformation Framework (AIDFTF) and an AI-Driven Finance Transformation Maturity Model (AIFTMM) for SAP S/4HANA finance. The study is designed as a conceptual, integrative review and framework-development paper. It synthesizes the six supplied research guidance documents, identifies recurring gaps, translates those gaps into testable hypotheses, and proposes a mixed-methods validation protocol. The framework links financial data foundations, AI and analytics capabilities, insight quality, decision effectiveness, process outcomes, and business-value realization. Seven hypotheses address decision effectiveness, forecast accuracy, process efficiency, embedded analytics maturity, data quality, generative-AI decision support, and the mediating role of insight quality. The paper specifies candidate measures, a staged validation plan, governance controls, use-case priorities, and an illustrative-not empirical-business-case model. No primary data were collected, and the proposed relationships are not presented as tested findings. The principal contribution is an integrated, SAP-finance-oriented model that connects technical capability to measurable decision and transformation outcomes while making validation requirements explicit. The framework is intended to guide future empirical work and executive evaluation, rather than to claim that the proposed effects have already been demonstrated.

## 11. GreenDynaMix:热敏动态混合精密MoE LLM推理系统

> 英文原标题：GreenDynaMix: Thermal-Aware Dynamic Mixed-Precision MoE LLM Inference Systems

- **作者：** Han-Yi Lin、Kieran Griperay、Qiang Zhou、Xiangyu Zhou、Nate Bonacci、Zinachidi Achikeh、Li He、Shaofei Qi 等
- **来源/日期：** arXiv；2026-11-24；arXiv
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](http://arxiv.org/abs/2611.31737v1) · [PDF](https://arxiv.org/pdf/2611.31737v1)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、llm inference、throughput。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

由于GPU温度随着工作负载强度和环境条件不断波动,保持它在安全范围内需要实时频率扩展,这必然是通过吞吐量或精度的成本. 为了应对这项紧密相结合的挑战,我们提出了GreenDynaMix,这是首个基于DVFS的热管理器和动态精度调节吞吐量补偿器的运行时间系统.一个意识到敏感性的分配器利用来自专家混合路由器 (MoE) 的内在重要信号来分配更高的精度给关键专家,保持准确性. 在服务器,桌面和嵌入式平台上的实验表明,GreenDynaMix在LLM推断期间将温度诱导的GPU老龄化率降低25-33%.没有离线配置或模型重训,它以8位/4位混合精度0.9-1.6%的困难性成本恢复吞吐量,升至9.4%的4位/2-位内存强迫.

### 英文原摘要

Sustained Large Language Model (LLM) inference generates significant heat that exacerbates silicon aging and reduces GPU reliability. Because GPU temperature fluctuates continuously with workload intensity and ambient conditions, keeping it in a safe range requires real-time frequency scaling, which inevitably comes at the cost of either throughput or accuracy. To address this tightly coupled challenge, we propose GreenDynaMix, the first runtime system to jointly integrate a DVFS-based thermal manager with a dynamic precision-tuning throughput compensator. A sensitivity-aware allocator leverages intrinsic importance signals from the Mixture-of-Experts (MoE) router to assign higher precision to critical experts, preserving accuracy. Experiments on server, desktop, and embedded platforms demonstrate that GreenDynaMix reduces the temperature-induced aging rate of GPUs during LLM inference by 25-33%. Without offline profiling or model retraining, it recovers throughput at a perplexity cost of 0.9-1.6% with 8-bit/4-bit mixed precision, rising to 9.4% where memory forces 4-bit/2-bit.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
