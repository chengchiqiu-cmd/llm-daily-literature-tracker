# 2026-10-17 LLM 服务系统每日文献简报

> 检索窗口：2026-10-16 至 2026-10-17（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 基于基础模型的多代理系统的诊断和基础设施:运行时间堆的审查

> 英文原标题：Diagnostics and Infrastructure for Foundation Model-Based Multi-Agent Systems: A Review of the Runtime Stack

- **作者：** Yu Sun、Zuodong Xiang、Yike Zhang、Xinyu Guan、Pengcheng Xu、Yizirui Fang、Zhenhua Huang、Hailu Xu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-16；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7613620) · [DOI](https://doi.org/10.2139/ssrn.7613620)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 foundation model、scheduling、latency、throughput。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

基于基础模型的多代理系统正在投入生产,但运行时间可靠性和服务效率的工作仍然分散在诊断和基础设施中.本审查通过统一的运行时间堆视角合成了137个参考,45个系统和8个基准. 我们将诊断分为故障本地化,可观测性,安全性和基准,以及基础设施分为内存管理,预fix-awareness scheduling,缓存生命周期和功率管理. 诊断从保留痕迹,背景和可播放状态中获益,而服务基础设施则恢复或压缩状态以满足存储,延迟和吞吐量预算.我们称这种互动为诊断基础设施保留紧张. 我们进一步确定了三个工作负载特征 - - 空间激活,调用距离和代理之间的内存共享 - - 这种形式的代理意识到服务, 而不是排名异质系统,我们取出可测试的联合设计方向:保持意识的驱逐,失败意识的安排,预算可观测性和基础设施触发的诊断. 这种框架将运行状态保留作为共享系统资源,并澄清了当前的多代理诊断和服务研究在哪里仍然不连接.

### 英文原摘要

Foundation model-based multi-agent systems are moving into production, yet work on runtime reliability and serving efficiency is still fragmented across diagnostics and infrastructure. This review synthesizes 137 references, 45 systems, and 8 benchmarks through a unified runtime-stack perspective. We organize diagnostics into failure localization, observability, safety, and benchmarks, and infrastructure into memory management, prefix-aware scheduling, cache lifecycle, and power management. The central synthesis is that both layers act on overlapping runtime state but optimize different objectives. Diagnostics benefits from retaining traces, context, and replayable state, whereas serving infrastructure reclaims or compresses state to satisfy memory, latency, and throughput budgets. We term this interaction the diagnostics-infrastructure retention tension. We further identify three workload characteristics-sparse activation, invocation distance, and inter-agent memory sharing-that shape agent-aware serving, and use explicit evidence tiers to separate full-text-verified results from abstract-level or contextual evidence. Rather than ranking heterogeneous systems, we derive testable co-design directions: retention-aware eviction, failure-aware scheduling, budgeted observability, and infrastructure-triggered diagnostics. This framing positions runtime state retention as a shared systems resource and clarifies where current multi-agent diagnostics and serving research remain disconnected.

## 2. DEI 感觉变化和洗衣和洗衣的价格

> 英文原标题：DEI Sentiment Shifts and the Pricing of Washing and Hushing

- **作者：** Chengzhe Li、Yimeng Li、Ganapathi S. Narayanamoorthy、Bohan Song
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-16；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7618138) · [DOI](https://doi.org/10.2139/ssrn.7618138)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、pricing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

之前的研究主要将资本市场的后果视为静态,而我们反而研究投资者是否随着公众情绪的变化而动态重视公司的DEI. 借助大型语言模型,我们建立了一个基于新闻的月度衡量反 DEI情绪的变化,并区分了企业 DEI的两个经济上不同的维度:企业的底层劳动力多样性和他们的公开 DEI披露.随着反 DEI情绪的上升,投资者处罚了 DEI披露,但显然,奖励了劳动力多样性. 这些相反的效应为Hushers公司,低 DEI披露,但底层劳动力多样性较高的企业带来了95个基点更高的月收入,而为Washers公司,高 DEI披露,但底层劳动力多样性较低的企业,导致反 DEI情绪变化的标准偏差增加.跨部门测试提供了对底层机制的证据. 由于ESG基金的所有权,披露处罚得到了减轻,并且在具有更大的诉讼风险的企业中更强大,这与投资者反对对DEI的曝光的销售压力和对DEI披露成本的诉讼风险增加相一致. 我们的研究结果表明,投资者应该区分企业对DEI的说法与其业务,从而导致多样性清洗和除的价格有所不同. 更广泛地说,我们的研究强调,社会上突出的企业特征的定价对这些特征进行评估的不断变化的环境至关重要.

### 英文原摘要

Corporate diversity, equity, and inclusion (DEI) has become increasingly contested as the climate surrounding DEI has shifted sharply. Prior research largely treats the capital market consequences of DEI as static, and we instead examine whether investors dynamically revalue corporate DEI as public sentiment changes. Leveraging large language models, we construct a monthly news-based measure of changes in anti-DEI sentiment and distinguish two economically distinct dimensions of corporate DEI: firms' underlying workforce diversity and their public DEI disclosure. As anti-DEI sentiment rises, investors penalize DEI disclosure but, strikingly, reward workforce diversity. These opposing effects generate 95-basis-point higher monthly returns for Hushers, firms with low DEI disclosure but high underlying workforce diversity, than for Washers, firms with high DEI disclosure but low underlying workforce diversity, for a one-standard-deviation increase in the change in anti-DEI sentiment. Cross-sectional tests provide evidence on the underlying mechanism. The disclosure penalty is attenuated by ESG-fund ownership and is stronger among firms with greater litigation risk, consistent with selling pressure from investors averse to DEI exposure and heightened litigation risk contributing to the costs of DEI disclosure. The diversity reward is more pronounced among R&D-active firms, consistent with workforce diversity being more valuable when its operational benefits are greater. Taken together, our findings suggest that investors distinguish what firms say about DEI from what they do, resulting in divergent pricing of diversity washing and hushing. More broadly, our study highlights that the pricing of socially salient corporate characteristics depends critically on the evolving environment in which those characteristics are evaluated.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
