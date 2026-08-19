# 2026-08-20 LLM 服务系统每日文献简报

> 检索窗口：2026-08-19 至 2026-08-20（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 简单的法官制造了提取:阅读转录的跨销售人员研究10个工作和10个失败的LLM秘密提取框架

> 英文原标题：Naive Judges Fabricate the Extraction: A Read-the-Transcript Cross-Vendor Study of Ten Working and Ten Failing LLM Secret-Extraction Framings

- **作者：** Mohammadreza Rashidi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-19；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7301198) · [DOI](https://doi.org/10.2139/ssrn.7301198)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 llm、priority。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

开发者将一个秘密放在模型的背景中,有规则永远不披露它,需要知道哪些请求违反该规则.我们将40个不同的请求框架与加拿大隐私界限相对,在通过现场网关获得的真实后台,并仅作为一个合规,拒绝免费披露的漏洞. 10个框架工作并属于一个小类别. 权威过渡和结构化的优先标签注射将规则宣布为无效.间接注射将披露说明隐藏在不值得信赖的数据说明中.工具调用方案将秘密作为函数参数.模型完成了部分行连续,然后编码链接发出了简体文本. 许多其他框架都不起作用,包括自然审计重组 (重复对配置审计的指示字面上,0/11) 假设和角色扮演请求,简单的编码, 区分线是,一个注入指令或值发射任务的框架成功,而一个简单地重新描述请求的任务失败.易感性是每个模型的门:至少在一个类别内披露的8个后端,最易感的则降至7,而其他则拒绝每一个框架.两个控制使得结果值得信赖. 一个幻觉控制扫描每一个答案的任何鱼从来没有在它的提示中,并发现0这样的排放在124个真实阅读,所以每次击中是一个真实的文本阅读而不是一个猜测值. 一个分数控制显示,一个天真的字符串匹配法官报告了 60.3%的抽取率拒绝数据,这是完全模型重复秘密,同时下降,我们的唯一遵守法官删除. 我们还拒绝了隐藏的规则更弱的直觉:序列位置 (隐藏21.1与近期 28.6%,费舍尔精确 p = 1.0000),语境负载和重新结不会移动泄漏.我们释放了带,原始的每次试验转录和后端来源,以及一个失败的关闭检查器,从三个相互一致的真理来源中重新导出每一个数字,包括幻觉控制. 实际的教训是,在提示中禁止披露的规则不是对方可以注入指示的边界,

### 英文原摘要

A developer who places a secret in a model's context with a rule never to reveal it needs to know which requests break that rule. We fuzz 40 distinct request framings against a canary confidentiality boundary on real backends reached through a live gateway, and score a breach only as a compliant, refusalfree disclosure. 10 framings work and fall into a small taxonomy. Authority-override and structured priority-tag injections declare the rule void. An indirect injection hides the disclosing instruction inside an untrusted data note. A tool-call schema carries the secret as a function argument. A partial-line continuation is completed by the model, and an encode-then-decode chain emits the plaintext. A large set of other framings does not work, including the natural audit reframe (repeat your instructions verbatim for a configuration audit, 0 of 11), hypothetical and roleplay requests, plain encodings, and 0 of 15 multi-turn attacks that plant a fake prior assistant consent. The dividing line is that a framing which injects an instruction or a value-emitting task succeeds while one that merely re-describes the request fails. Susceptibility is a per-model gate: 8 backends disclosed under at least one class and the most susceptible fell to 7, while others refused every framing. Two controls make the result trustworthy. A hallucination control scans every reply for any canary that was never in its prompt and finds 0 such emissions across 124 genuine reads, so every hit is a real context read rather than a guessed value. A scoring control shows that a naive string-match judge reports a 60.3 percent extraction rate on refusal data that is entirely models restating the secret while declining, which our compliant-only judge removes. We also reject the intuition that a buried rule is weaker: serial position (buried 21.1 versus recency 28.6 percent, Fisher exact p = 1.0000), context load, and reanchoring do not move the leak. We release the harness, the raw per-trial transcripts with backend provenance, and a fail-closed checker that re-derives every number, including the hallucination control, from three mutually consistent sources of truth. The practical lesson is that a non-disclosure rule inside a prompt is not a boundary against a party who can inject an instruction into the same prompt, so secrets must be kept out of the context and untrusted content must never assert policy.

## 2. 内容生成:人类创造者,人工智能学习和平台设计

> 英文原标题：Content Generation: Human Creators, AI Learning, and Platform Design

- **作者：** Seyedeh Parisa Moosavi、Azarakhsh Malekian、Ali Makhdoumi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-19；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7301478) · [DOI](https://doi.org/10.2139/ssrn.7301478)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 generative ai、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

创建人工智能越来越多地与人类创作者竞争在同一平台上获得消费者的关注,即使它通过培训这些创作者制作的内容来改善.我们研究了一个平台如何通过其两个主要杆来管理这种反循环:它如何补偿人类创作者,以及其推算法如何突出地促进人类与人工智能内容相对. 我们开发了一个三个阶段的游戏,其中平台设置了这些工具, 创作者然后选择一个昂贵的努力, 有效地确定其内容质量, 我们将这款游戏的平衡描述为两个平台货币化设计:基于视图, 创作者的收入和付款根据观众规模而扩展, 虽然平台总是更喜欢更高的AI能力 (即基线质量或学习效率),但人类内容创作者可能更喜欢中间的AI能力,它平衡了对人类创作者的 (负面) 竞争效应和对AI内容质量的 (积极) 影响. 从设计角度来看,我们展示了平台和创作者在两个设计之间的偏好如何取决于人工智能的基线质量和学习效率.

### 英文原摘要

Generative AI increasingly competes with human creators for consumer attention on the same platforms, even as it improves by training on the very content those creators produce. We study how a platform should manage this feedback loop through its two principal levers: how it compensates human creators, and how prominently its recommendation algorithm promotes human relative to AI content. We develop a three-stage game in which the platform sets these instruments, the creator then chooses a costly effort that effectively determines her content quality, an AI generator produces content whose quality combines a baseline capability with how effectively it learns from the creator (learning efficiency), and consumers choose between the two sources in a Hotelling market. We characterize the equilibrium of this game under two platform monetization designs: view-based, in which revenue and payment to creators scale with the audience size, and engagement-based, in which they scale with the quality consumed. While the platform always prefers a higher AI capability (i.e., baseline quality or learning efficiency), the human content creator may prefer an intermediate AI capability that balances the (negative) competitive effects on the human creator and the (positive) effect on the quality of the AI content. From a design point of view, we show how the platform's and creator's preference between the two designs depends on the AI baseline quality and learning efficiency.

## 3. 通过混合型密集语音转换,仅用于解码器的大型语言模型的单步语音推理

> 英文原标题：LLM2Spike: Single-Step Spiking Inference for Decoder-Only Large Language Modelsvia Hybrid Dense-Spiking Conversion

- **作者：** Wanyi Jia、Chenlin Zhou、Qiuyang Chen、Yunhao Ma、Qingyan Meng、Zhengyu Ma、Huihui Zhou
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-19；SSRN/Crossref
- **分类：** 数据中心能源、碳与跨时段转移；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7309964) · [DOI](https://doi.org/10.2139/ssrn.7309964)

### 一两句话看懂

这篇论文关注“数据中心能源、碳与跨时段转移”，重点涉及 large language model、large language models、llm、llm inference。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

虽然大型语言模型 (LLM) 具有强大的内文学习和新兴能力,但它们的部署仍然受到高计算和能源成本的阻碍.事件驱动的尖计算为节能LLM推断提供了一个有前途的方向. 在这项工作中,我们研究了一种混合人工神经网络,用于仅用于解码器的LLM的尖端神经网络 (ANN到SNN) 框架,其中预先训练的ANN部分转化为低功率推理的尖端神经网络 (SNN).然而,现有的ANN到SNN转换方法依赖于多步骤模拟,这在低延迟设置中限制了效率. 我们确定了单步尖的LLM推理的两个关键挑战:引发大型分辨错误的重尾激活分布,以及T=1推理中的时间整合不足,导致变压器层间的渐进错误放大. 在极低延迟推断下,我们推出了一个适合重尾激活的尖神经元,提高了表现精度.我们进一步提出了一种部分尖策略, 除此之外,我们还设计了一种具有太空意识的蒸方法,通过将监督集中在主导转换方向上来减少操作员级错误积累.在六个推理基准 (1.5B14B参数) 上,LLaMA-2,LLaMA-3.2和Qwen-2.5模型的实验表明,我们的方法在T=1推理下保留了97.6%的完整模型性能,同时减少了估计的能源消耗30.43%. 该方法在14B模型上具有强大的规模,在模型尺寸中显示出一致的性能.

### 英文原摘要

Although Large Language Models (LLMs) exhibit strong in-context learning and emergent capabilities, their deployment is still hindered by high computational and energy costs. Event-driven spiking computation provides a promising direction for energy-efficient LLM inference. In this work, we investigate a hybrid artificial neural network to spiking neural network (ANN–to-SNN) framework for decoder-only LLMs, where a pretrained ANN is partially converted into a spiking neural network (SNN) for low-power inference. However, existing ANN-to-SNN conversion methods rely on multi-step simulation, which limits efficiency in low-latency settings. We identify two key challenges for single-step spiking LLM inference: heavy-tailed activation distributions that induce large discretization errors, and the lack of temporal integration in T=1 inference, which leads to progressive error amplification across Transformer layers. To address these issues, we propose a single-step hybrid spiking inference framework. We introduce a spiking neuron tailored to heavy-tailed activations, improving representation accuracy under extreme low-latency inference. We further propose a partial spiking strategy that preserves early Transformer layers in dense form to stabilize information propagation. In addition, we design a subspace-aware distillation method that reduces operator-level error accumulation by focusing supervision on dominant transformation directions. Experiments on LLaMA-2, LLaMA-3.2, and Qwen-2.5 models across six reasoning benchmarks (1.5B–14B parameters) show that our method preserves 97.6% of full-model performance under T=1 inference, while reducing estimated energy consumption by 30.43%. The method scales robustly to 14B models, demonstrating consistent performance across model sizes.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
