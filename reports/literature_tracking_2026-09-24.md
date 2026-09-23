# 2026-09-24 LLM 服务系统每日文献简报

> 检索窗口：2026-09-23 至 2026-09-24（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 大型语言模型作为对行为参数的校准测量仪器

> 英文原标题：Large Language Models as Calibrated Measurement Instruments for Behavioral Parameters

- **作者：** Brandon Yee
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-23；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7505498) · [DOI](https://doi.org/10.2139/ssrn.7505498)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

行为参数,如损失厌恶性,牧养和外分,是资产定价模型的核心,但它们仍然很难测量,没有噪音,选择效应或联合识别问题.本文开发了一个框架,将大型语言模型作为这些参数的校准测量工具,而不是作为人类对象的替代品来判断现实主义. 在四种模型和19200个完全合成的金融环境中的代理场景试验中,基线 (理性配置文件) 行为显然比研究的八个偏见中的大多数的人类基准更合理,损失厌恶,牧养和处置效应都与其定理性的人类价值观相比减弱. 然而,在提示中嵌入行为配置文件将基本参数移动到一个大规模和统计上可靠的数量:对于损失厌恶,牧养,外分和定,诱导值达到或超过相应的人类基准值,同时保持在重复抽取中稳定,并在实验环境中保持一致. 一项进一步的测试询问,校准抽象参数是否将其超越测量实践本身的任何经济内容,并将其,未经修改,转化为基于代理的最小资产定价模型;这样做将重现了Jegadeesh和Titman (1993) 记录的短视野动力和长视野逆转模式,这种模式从未出现当交易者默认合理时. 该论文的贡献是方法性的:对校准有效性的定义,三个验证级别,以及该方法在哪里有效和哪里不有效的明确地图,作为使用语言模型作为行为金融测量工具的实际指导.

### 英文原摘要

Behavioral parameters such as loss aversion, herding, and extrapolation sit at the center of asset pricing models, yet they remain difficult to measure without noise, selection effects, or jointidentification problems. This paper develops a framework that treats large language models as calibrated measurement instruments for these parameters, rather than as stand-ins for human subjects to be judged on realism. Across four models and 19,200 agent-scenario trials on fully synthetic financial environments, baseline (rational-profile) behavior turns out to be systematically more rational than the human benchmarks on most of the eight biases studied, with loss aversion, herding, and disposition effects all attenuated relative to their canonical human values. Embedding a behavioral profile in the prompt, however, moves the underlying parameter by a large and statistically reliable amount: for loss aversion, herding, extrapolation, and anchoring, the induced value reaches or exceeds the corresponding human benchmark while remaining stable across repeated draws and coherent across experimental contexts. A further test asks whether the calibrated extrapolation parameter carries any economic content beyond the measurement exercise itself, by feeding it, unmodified, into a minimal agent-based asset pricing model; doing so reproduces the short-horizon momentum and long-horizon reversal pattern documented by Jegadeesh and Titman (1993), a pattern that never appears when traders are rational by default. The paper's contribution is methodological: a definition of calibration validity, three validation tiers, and an explicit map of where the approach works and where it does not, offered as practical guidance for using language models as measurement instruments in behavioral finance.

## 2. 大语言模型理论概述:第一部分:语义理想气体的概念基础

> 英文原标题：Outline of a Theory of Large Language Models:Part 1. Conceptual Foundations of a Semantic Ideal Gas

- **作者：** Venkat Venkatasubramanian
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-23；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7511763) · [DOI](https://doi.org/10.2139/ssrn.7511763)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 large language model、large language models、llm、equilibrium。从摘要看，作者建立理论或分析模型；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

什么类型的数学对象是大型语言模型 (LLM)?这是我们试图在这篇三部分论文中回答的问题.训练有素的LLM被模型为一个{emph{emergent semantic field $\psi^*$}与一个{emph{context-indexed}的概率状态在模型衍生的语义空间. 正如理想气体给了统计力学一个基线,从而生长了更丰富的物质理论,第1部分从一个故意最小的意义式理想气体开始. 使用统计式电动力学,意义上的替代品被建模为具有有效效益的适应性剂群体. arbitrage平衡产生了指数占用法,在连续中,$\psi^*(x)\propto e^{u(x)-v(x)}$. 这只是当使用性差异$u-v$独立于测量训练的场所$\widehat{\psi}^{\,*}$时的预测,所以$\widehat{\psi}^{\,*}\stackrel{?}{\approx}\psi^*$是一个真正的理论测试. 预测字段定义了一个理论基础景观 $\Vth$,而测量字段定义 $\Vhat$;它们的协议是相同的训练侧测试的第二个表示.为了推断,一个依赖环境的偏差 $B_\eta(x;c) $必须独立于它用于预测的保持状态进行校准或指定. 结果的有效景观产生了吉布斯状态 $\rho^G_{c,T}$,从重复代代的运行状态 $\widehat{\rho}_{c,T}$而测试.可观察到的基本生成度是 $Y_{\mathrm{sem}}=\sum_\alpha p_\alpha^2$,其反向计算了一个文本选择的有效语义替代方案. 部分~2和~3增加了 mesoscopic 动态,有限容量相互作用,非本地内核,响应理论和更高复制结构诊断.

### 英文原摘要

What kind of mathematical object is a large language model (LLM)? This is the question we attempt to answer in this three-part paper. A trained LLM is modeled as an \emph{emergent semantic field $\psi^*$} together with a \emph{context-indexed} family of probability states on a model-derived semantic space. Just as the ideal gas gave statistical mechanics a baseline from which richer theories of matter grew, Part~1 starts with a deliberately minimal \emph{semantic ideal gas}. Using \emph{statistical teleodynamics}, semantic alternatives are modeled as adaptive agent populations with effective utility $h_k=u_k-v_k-\ln N_k$. Arbitrage equilibrium yields an exponential occupancy law and, in the continuum, $\psi^*(x)\propto e^{u(x)-v(x)}$. This is a prediction only when the utility difference $u-v$ is specified independently of the measured trained field $\widehat{\psi}^{\,*}$, so that $\widehat{\psi}^{\,*}\stackrel{?}{\approx}\psi^*$ is a genuine theory--measurement test. The predicted field defines a theoretical base landscape $\Vth$, while the measured field defines $\Vhat$; their agreement is a second representation of the same training-side test. For inference, a context-dependent bias $B_\eta(x;c)$ must be calibrated or specified independently of the held-out state it is used to predict. The resulting effective landscape generates a Gibbs state $\rho^G_{c,T}$, tested against the operational state $\widehat{\rho}_{c,T}$ from repeated generations. The elementary generative concentration observable is $Y_{\mathrm{sem}}=\sum_\alpha p_\alpha^2$, whose inverse counts the effective semantic alternatives selected by a context. Parts~2 and~3 add mesoscopic dynamics, finite-capacity interactions, nonlocal kernels, response theory, and higher-copy structural diagnostics.

## 3. 一个在果上运行的多语言地底检测器:训练有素的代币分类与LLM法官和仅使用英语的检测器在31种语言中

> 英文原标题：A Multilingual Groundedness Detector that Runs on a Raspberry Pi: Trained Token Classification against LLM Judges and English-only Detectors in 31 Languages

- **作者：** Aghasalim Mustafazada、Teymur Eyvazov
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-23；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7497398) · [DOI](https://doi.org/10.2139/ssrn.7497398)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 llm、quota。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

检索增强助理最常通过表示文件不支持的价格,时间,地址或电话号码来失败用户.为此故障的开放权重探测器 Vectara HHEM-2.1-Open,LettuceDetect 以英语训练. 我们将我们的植入错误基准扩展到31种语言,在九种脚本中 (434个答案,372个一个植入错误,62个植入控制,每个语言都有相同的错误) 并添加第三种检测器:我们自己的多语言代币分类器,从XLM-RoBERTa基础上调整到6,647个答案 2,844个合成商业答案在30种语言中 RAGTruth 根据保留的数据选择的决策门. 它在62个基于地面的答案中捕获了352个插入的372个错误 (95%),在32个基于地面的答案中捕获了32个虚假警报,在笔记本电脑CPU上的每个答案时间为34ms,并在Raspberry Pi 5上提供了 grounded.siba.az的公众演示. 在相同的案例中,HHEM-2.1-Open达到71%的回忆率,其中22个有基因的答案被标记:其分数与英语的脚本距离崩 在6种语言中,它标记了每个有基因的答案 ,因此其回忆量度量了脚本,而不是索赔. LettuceDetect捕获了51%. 开放的LLM法官仍然保持了准确度上限 openai/gpt-oss-120b捕获了163/163的假警报,其每日配额允许的14种语言,为0.70秒每次网络通话, ~21x探测器的延迟和每代币价格.

### 英文原摘要

Retrieval-augmented assistants fail their users most often by stating a price, hour, address or phone number that their documents do not support. The open-weights detectors for this failure — Vectara HHEM-2.1-Open, LettuceDetect — are trained on English. We extend our planted-error benchmark to 31 languages across nine scripts (434 answers, 372 with one planted error, 62 grounded controls; identical errors in every language) and add a third kind of detector: a multilingual token classifier of our own, fine-tuned from XLM-RoBERTa-base on 6,647 answers — 2,844 synthetic business answers in 30 languages whose unsupported spans were planted and marked by open LLMs, plus RAGTruth — with the decision threshold chosen on held-out data. It catches 352 of 372 planted errors (95 %) with 32 false alarms in 62 grounded answers, in 34 ms per answer on a laptop CPU, and it serves the public demo at grounded.siba.az from a Raspberry Pi 5. On the same cases HHEM-2.1-Open reaches 71 % recall with 22 of 62 grounded answers flagged: its score collapses with script distance from English — in 6 languages it flags every grounded answer — so its recall there measures the script, not the claim. LettuceDetect catches 51 %. The open LLM judges remain the accuracy ceiling — openai/gpt-oss-120b catches 163/163 with 0 false alarms on the 14 languages its daily quota allowed, at 0.70 s per network call, ~21× the detector's latency and a per-token price. Weights (MIT, huggingface.co/aghasalim/grounded-multilingual-base), data, training and evaluation code and every raw output: github.com/aghasalim/groundedness.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
