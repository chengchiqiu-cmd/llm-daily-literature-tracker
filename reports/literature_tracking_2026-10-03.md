# 2026-10-03 LLM 服务系统每日文献简报

> 检索窗口：2026-10-02 至 2026-10-03（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 数字双集成人工智能建模和适应性PI收益优化在滚动到滚动制造中的回旋压力控制

> 英文原标题：Digital Twin–Integrated AI Modeling and Adaptive PI Gain Optimization for Rewinder Tension Control in Roll-to-Roll Manufacturing

- **作者：** Muhammad Irfan、Uzair Ali、Qasim Shahzad、Yunseon Byun、Seung-Hyun Lee、Inyoung Kim、Taik-Min Lee
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-02；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7552652) · [DOI](https://doi.org/10.2139/ssrn.7552652)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、scheduling、optimization。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

由于滚动直径和惯性不断变化的动态,在滚动到滚动 (R2R) 转系统中实现稳定和一致的电压控制仍然具有挑战性.本文介绍了一个适应性整体 (PI) 收益规划框架,其中控制器收益与转直径进行动调整,以保持系统性能一致. 数据驱动的替代模型用于在不同操作条件中生成最佳的PI获益轨迹.为了支持实时实现,拟议的方法是集成在数字双胞胎 (DT) 环境中,该方法可以通过基于共享内存的数据交换机制实现现场步骤响应功能提取,包括超越和升级时间 (t90). 此外,采用轻量级大型语言模型 (LLM) 辅助验证模块来评估当前控制性能是否符合预定义标准或需要进一步调整.在R2R平台上的实验验验证表明,拟议的适应策略显著提高了广泛的网络速度和反向直径的控制性能. 与传统的固定收益PI控制相比,该框架实现了0.4%的平均超越,相当于大约96%的超越降低,同时保持稳定的过渡反应行为. 该方法还实现了0.53秒的平均上升时间 (t90). 这些结果表明,与实时功能监测和智能验证相结合,基于直径的适应性PI增长规划为R2R回系统的电压控制提供了有效和实用的解决方案.

### 英文原摘要

Achieving stable and consistent tension control in roll-to-roll (R2R) rewinding systems remains challenging due to time-varying dynamics caused by continuously changing roll diameter and inertia. This paper presents an adaptive proportional–integral (PI) gain scheduling framework, where controller gains are dynamically adjusted with respect to rewinder diameter to maintain consistent system performance. A data-driven surrogate model is used to generate optimal PI gain trajectories across varying operating conditions. To support real-time implementation, the proposed approach is integrated within a digital twin (DT) environment that enables live step-response feature extraction, including overshoot and rise time (t90), using a shared-memory-based data exchange mechanism. In addition, a lightweight large language model (LLM)-assisted validation module is incorporated to assess whether the current control performance satisfies predefined criteria or requires further tuning. Experimental validation on R2R platform demonstrates that the proposed adaptive strategy significantly improves control performance across a wide range of web speeds and rewinder diameters. Compared with conventional fixed-gain PI control, which exhibited a median overshoot of 9.8%, the proposed framework achieved a median overshoot of 0.4%, corresponding to an approximate 96% reduction in overshoot while maintaining stable transient response behavior. The proposed method also achieved a median rise time (t90) of 0.53 s. These results demonstrate that diameter-dependent adaptive PI gain scheduling, combined with real-time feature monitoring and smart validation, provides an effective and practical solution for tension control in R2R rewinding systems.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
