# 2026-10-02 LLM 服务系统每日文献简报

> 检索窗口：2026-10-01 至 2026-10-02（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 使用经济数据和基础模型的中期多分辨率电荷预测

> 英文原标题：Medium-Term Multi-Resolution Electric Load Forecasting using Economic Data and Foundation Model

- **作者：** Eloi Lindas、Yannig Goude、Philippe Ciais
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-01；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7548372) · [DOI](https://doi.org/10.2139/ssrn.7548372)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 foundation model、scheduling。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

准确的中期,从几个月到几年,电力负载预测对于制定电站维护时间表,运输负载和价格结算的知情决策至关重要. 由于长期负载预测 (LTLF),主要采用经济和设备发展场景,以及基于天气和日历模式的短期负载预测 (STLF),中期负载预测 (MTLF) 需要抽象能力和可变性建模. 然而,目前尚不清楚MTLF是否可以从经济指标中获益,特别是预测的视野和分辨率. 为了应对这些挑战,一个数据集涵盖了20年的观察到的电力负载,天气和经济变量,如消费者价格和生产指数,电动汽车数量或就业,并与一个表格基础模型 (FM) 结合,以以每月和每天分辨率为法国提供一个月至48个月的预测. 一项新的特征选择管道,包括多种特征子集,旨在删除噪音数据,并证明选定的经济变量在2015-2025年期间提高了20%的预测能力. 解释性,通过特征和文本重要性进行调查,显示了FM的有限的文本使用,表明了潜在的计算节省,而文本减少,而经济预测因素的特征重要性随着预测视野增长. 这表明,将经济数据纳入MTLF可以弥合与LTLF的差距,同时也适合使用气候数据和社会经济叙述的需求预测.

### 英文原摘要

Accurate medium-term, from a few months to a few years, electricity load forecasts are crucial for informed decision-making in power plant maintenance scheduling, load dispatch and price settlement. Being comprised between Long-Term Load Forecasting (LTLF) which uses mostly economic and appliances development scenarios, and Short-Term Load Forecasting (STLF) driven by weather and calendar patterns, Medium-Term Load Forecasting (MTLF) requires both extrapolation capabilities and variability modeling. Yet, it remains unclear if MTLF can benefit from economic indicators, and especially at which forecast horizon and resolution. To address these challenges, a dataset covering 20 years of observed electricity load, weather and economic variables such as consumer price and production indices, electric vehicle counts or employment is combined with a tabular Foundation Model (FM) to issue predictions ranging from 1 month to 48 months in advance for France at monthly and daily resolution. A new feature selection pipeline, ensembling diverse feature subsets, is designed to remove noisy data and demonstrate that selected economic covariates improve forecast skill by 20 % over 2015-2025. This enhancement limits the Mean Absolute Percentage Error to 4 % for monthly granularity and 5 % for daily granularity. Explainability, investigated through feature and context importance, showed the limited context usage of the FM indicating potential computational savings with context reduction, while feature importance of economic predictors grows with the forecast horizon. This suggests that including economic data in MTLF could bridge the gap with LTLF while also being suitable for demand projections using climate data and socioeconomic narratives.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
