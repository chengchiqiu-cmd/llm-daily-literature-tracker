# 2026-10-31 LLM 服务系统每日文献简报

> 检索窗口：2026-10-30 至 2026-10-31（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 没有共同标志的错误:金融管道中量子和LLM组件的认证评估

> 英文原标题：Errors With No Common Sign: Certified Evaluation of Quantum and LLM Components in Financial Pipelines

- **作者：** Chevin Jeon、Byungkwon Jeon、Michelle Jeon
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-30；SSRN/Crossref
- **分类：** 平台经济、市场设计与竞争；直接 LLM 服务研究；相关性评分 7
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7666979) · [DOI](https://doi.org/10.2139/ssrn.7666979)

### 一两句话看懂

这篇论文关注“平台经济、市场设计与竞争”，重点涉及 llm、budget constraint。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

我们研究了一个具体的决策问题:在预算限制下选择二进制投资组合配置,其中风险期限是根据生成的联合信用分布压力场景估计的. 我们构建了一个模块化管道,SynQubi,有两个量子组件在孤立,可交换的角色:一个量子电路诞生机 (QCBM) 在种子中,在非退化情况下,QAOA与解决方案质量的经典参考相匹配,但在满足约束方面明显更差,将预算可行的分配返回大约一半的样本与零模型的全部相比. 我们的主要发现是方法性:认证推翻了我们普通检查经过的五项结果,错误指向不同的方向 (两个赞美了量子组件,三个没有). 一个基于LLM生成的交易策略代码的小试点显示了LLM设置中的相同模式:一系列机械有效性检查发现,每个失败都是缺失的进口,而不是对策略的误解.我们没有建立量子优势.CCS概念 •计算方法 →智能代理; •应用计算 →经济学.

### 英文原摘要

Hybrid quantum-classical machine learning is increasingly tested in financial settings, yet evaluations rarely make it possible to attribute observed behavior to the quantum components themselves. We study one concrete decision problem: choosing a binary portfolio allocation under a budget constraint, where the risk term is estimated from generated joint credit-spread stress scenarios. We build a modular pipeline, SynQubi, with two quantum components in isolated, swappable roles: a Quantum Circuit Born Machine (QCBM) that generates tail scenarios, benchmarked against empirical, Gaussian, and Student-𝑡 copulas, and a QAOA optimizer, whose proposals are certified against exact classical solvers. Across seeds, on non-degenerate instances QAOA matches classical references on solution quality but is markedly worse on constraint satisfaction, returning budget-feasible allocations in roughly half of samples against the null model's all. Our main finding is methodological: certification overturned five of our own results that ordinary inspection had passed, and the errors pointed in different directions (two flattered the quantum components, three did not). Such errors cannot be fixed by discounting favorable results, only by a mechanical classical reference. A small pilot on LLM-generated trading-strategy code shows the same pattern in an LLM setting: a harness of mechanical validity checks found that every failure was a missing import, not a misunderstanding of the strategy. We establish no quantum advantage. CCS Concepts • Computing methodologies → Intelligent agents; • Applied computing → Economics.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
