# 2026-10-15 LLM 服务系统每日文献简报

> 检索窗口：2026-10-14 至 2026-10-15（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 机器学习在资产定价

> 英文原标题：Machine Learning in Asset Pricing

- **作者：** David Rapach、Guofu Zhou
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-14；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7611982) · [DOI](https://doi.org/10.2139/ssrn.7611982)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

这项调查将对资产定价中选定的机器学习方法进行两部分的审查.第一部分侧重于汇总股市超额回报的时间序列可预测性,涵盖了最近的进展,如复杂性优势,噪音优势和预测因素的单一最佳因素. 我们还讨论了其他新方法和新型预测因素,包括收益分解,预测不可知的投资组合,基于选项的限制,宏观金融趋势和基于大语言模型 (LLM) 的文本信号.第二部分探讨了跨部门的股票收益预测性和高效的投资组合估算. 从Fama-MacBeth框架和关键绩效措施开始,我们调查了最近的发展,如LASSO规范化,预测组合和包括,异质回报响应模型,限制深度学习,遗传编程, 总体而言,证据强烈支持回报可预测性,机器学习方法与传统基准相比带来了显著的收益.

### 英文原摘要

This survey reviews selected machine learning methods in asset pricing in two parts. The first part focuses on time-series predictability of the aggregate stock market excess return, covering recent advances such as the “virtue of complexity,” the “virtue of noise,” and the single optimal factor of predictors. We also discuss other new methods and novel predictors, including return decomposition, forecast-agnostic portfolios, option-based bounds, macro-financial trends, and large language model (LLM)-based textual signals. The second part examines cross-sectional stock return predictability and efficient portfolio estimation. Starting from the Fama-MacBeth framework and key performance measures, we survey recent developments such as LASSO regularization, forecast combination and encompassing, heterogeneous return response models, constrained deep learning, genetic programming, feasible stochastic discount factor estimation under portfolio constraints, and LLM applications to numerical financial data. Overall, the evidence strongly supports return predictability, with machine learning methods delivering substantial gains vis-à-vis conventional benchmarks.

## 2. 自动登记:基于域的大型语言模型代理,用于物理约束的好日志解释工作流程

> 英文原标题：Auto-Logging: domain-grounded large language model agents for physics-constrained well-log interpretation workflows

- **作者：** RongBo Shao、Guangzhi Liao、Xingcai Zhang、Jun Zhou、Juan Zhang、Xianzhi Song、LiZhi Xiao
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-14；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7610813) · [DOI](https://doi.org/10.2139/ssrn.7610813)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工智能的工程应用不仅需要在预测上准确的系统,还需要在完整的工程工作流程中部署,可审核和强的系统.本文介绍了自动登记,这是一个基于域名的大型语言模型代理框架,用于物理限制的好日志解释. 人工智能贡献是一个规划者-执行者代理架构,将工作流程推理与数值预测分开:规划者通过检索石化物理程序和物理规则将用户请求转化为依赖性意识的解释计划,而执行者则通过标准化界面和返回结构调用注册的预处理工具和具体任务模型 (d) 状态,指标和警报. 工程应用是从端到端的地底井记录解释,包括曲线质量控制,预处理,缺陷曲线计算,学分类,水库参数预测,流体判断和报告生成. 在预期模拟数据集和公开井记录预测基准上,自动登录完成单井解释时间为10.2~25.3分钟,而专家辅助的传统解释时间为约14小时,同时将手动干预量降至约1分钟,保持竞争性预测性能. 废除研究表明,采集增强的域定位,动态代理规划和结构化反都提高了工作流的可靠性. 这些结果证明了工程工作流自动化的实用人工智能系统,其中语言模型在明确的物理约束下协调验证的数值组件,而不是取代域模型或专家审查.

### 英文原摘要

Engineering applications of artificial intelligence require systems that are not only accurate in prediction, but also deployable, auditable and robust across complete engineering workflows. This paper presents Auto-Logging, a domain-grounded large language model agent framework for physics-constrained well-log interpretation. The artificial intelligence contribution is a Planner-Executor agent architecture that separates workflow reasoning from numerical prediction: the Planner converts a user request into a dependency-aware interpretation plan by retrieving petrophysical procedures and physical rules, whereas the Executor invokes registered preprocessing tools and task-specific models through standardized interfaces and returns structured status, metrics and alarms. The engineering application is end-to-end subsurface well-log interpretation, including curve quality control, preprocessing, missing-curve imputation, lithology classification, reservoir-parameter prediction, fluid judgment and report generation. On a forward-simulated data set and a public well-log prediction benchmark, Auto-Logging completes single-well interpretation in 10.2--25.3 min, compared with approximately 14 h for expert-assisted conventional interpretation, while reducing manual intervention to about 1 min and maintaining competitive prediction performance. Ablation studies show that retrieval-augmented domain grounding, dynamic agent scheduling and structured feedback each improve workflow reliability. These results demonstrate a practical artificial intelligence system for engineering workflow automation, in which language models coordinate validated numerical components under explicit physical constraints rather than replacing domain models or expert review.

## 3. 风险负载平衡:在人工智能软件工作流程中推进有效的保证

> 英文原标题：Risk-Load Balancing: Carrying Forward Valid Assurance in Human–AI Software Workflows

- **作者：** Jiasheng Yang、Shengfeng Wang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-14；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7609701) · [DOI](https://doi.org/10.2139/ssrn.7609701)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 generative ai、load balancing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

人工智能软件工作流程可以在交付后重复有效的检查或应用其结果超出它们所设定的范围.我们提出了风险负载平衡 (RLB),一种工作流程控制理论,该理论提供了有效的支持,识别了未解决的情况,并将进一步的保证工作转向影响的责任. 我们在48个工程运行中评估了来自6个公共存储库的8项任务,与强大的本地模型 (N) 和完整的公共工作流程 (P) 相比. 在完成两次P重复的六项任务中,RLB的平均记录交付时间低于P的23.9963.10%,平均减少了50.75%.与N相同任务相比,P的记录时间平均高于182.4%,而RLB则高于35.8%.P的更大的负担并不持续提供更强的保证,而RLB的较低负担并不持续牺牲它们. 在使用边界模型的四项研究写作任务 (C1C4) 中,RLB 显示了比两个基线更少的防御过程扩展,同时保留了源支持的结论和必要的限制.结果还揭示了对理论进行具体决策的映射的差距.我们在没有改变核心数学的情况下完善了这一映射. 随后的已知任务验证显示了更好的责任连续性和更少的审查扩展,但当模型未能确定具体决策所需的责任关系时,错误仍然存在. 在研究中使用生成人工智能:OpenAI ChatGPT和Codex协助了先前材料和文献审查,数学正式化,实验和协议设计,研究实施和分析,以及英语语言的完善.生成人工智能代理也是评估的实验系统的一部分. 报告的实验测量来源于保留的执行记录,产品水平的发现是从结的文物中评估的.生成人工智能并没有用于改变,制造或取代经过运行后记录的实验结果.

### 英文原摘要

Human–AI software workflows may repeat valid checks after handoffs or apply their results beyond the scope they establish. We present Risk-Load Balancing (RLB), a workflow control theory that carries forward valid support, identifies what remains unresolved, and directs further assurance work to the affected responsibilities. The theory establishes sound carryover, exact logical residuals, and conditional preservation under abstraction and local updates. We evaluate RLB in 48 engineering runs across eight tasks from six public repositories against a strong native model (N) and a complete public workflow (P). In the six tasks where both P repeats completed, RLB's taskwise mean recorded delivery time was 23.99–63.10% lower than P's, with a median reduction of 50.75%. Relative to N on the same tasks, P's recorded times were 182.4% higher on average, compared with 35.8% for RLB. P's much larger burden did not consistently yield stronger guarantees, while RLB's lower burden did not consistently sacrifice them. In four research-writing tasks (C1–C4) using a frontier model, RLB showed less defensive process expansion than both baselines while preserving source-supported conclusions and necessary limitations. The results also exposed gaps in mapping the theory to concrete decisions. We refined this mapping without changing the core mathematics. Subsequent known-task validation showed better responsibility continuity and less review expansion, but errors remained when the model failed to identify the responsibility relations needed for concrete decisions. Use of generative AI in the research: OpenAI ChatGPT and Codex assisted with prior-material and literature review, mathematical formalization, experiment and protocol design, research implementation and analysis, and English-language refinement. Generative-AI agents were also part of the experimental systems evaluated. Reported experimental measurements were derived from retained execution records, and product-level findings were assessed from frozen artifacts. Generative AI was not used to alter, fabricate, or replace recorded experimental outcomes after the runs.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
