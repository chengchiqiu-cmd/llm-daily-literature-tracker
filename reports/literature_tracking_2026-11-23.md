# 2026-11-23 LLM 服务系统每日文献简报

> 检索窗口：2026-11-22 至 2026-11-23（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 服务连锁结构的工作,具有较大的内存足迹,应用到较大的基础模型服务

> 英文原标题：Serving Chain-structured Jobs with Large Memory Footprints with Application to Large Foundation Model Serving

- **作者：** Tingyang Sun、Ting He、I-Hong Hou
- **来源/日期：** ACM International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing (MobiHoc)；2026-11-22；OpenAlex
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.1145/3842721.3849638) · [DOI](https://doi.org/10.1145/3842721.3849638)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 large language model、llm、foundation model、load balancing。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

作为人工智能 (AI) 的当前趋势,大型基础模型越来越被使用为人工智能服务的核心. 然而,即使在训练后,由于它们的重资源足迹,特别是GPU内存方面,在规模上提供此类模型仍然是一个具有挑战性的任务. 虽然最近的研究揭示了服务基础模型的系统的独特特征,使它们与传统分布式计算系统区别起来,但仍然缺乏对潜在的系统管理问题的基本理解. 这项工作旨在通过区块配置和缓存配置来解决这一差距,通过通过提供大型内存足迹的链结构性工作来提取服务器链链构成的新问题,这通过管道平行性来模拟服务大型基础模型的根本问题. 在显示最佳解决方案的NP硬度后,重点转向在最先进的负载平衡下开发可扩展的算法,以保证性能. 该解决方案应用于分布式大型语言模型 (LLM) 服务系统,与最先进的解决方案相比,反应时间显著减少.

### 英文原摘要

As a current trend in Artificial Intelligence (AI), large foundation models are increasingly employed as the core of AI services. However, even after training, serving such models at scale remains a challenging task due to their heavy resource footprints, particularly in terms of GPU memory. While recent works revealed unique characteristics of systems serving foundation models that distinguish them from traditional distributed computing systems, there is still a lack of fundamental understanding of the underlying system management problems. This work aims at addressing this gap by extracting a novel problem of “server chain composition” via block placement and cache allocation for serving chain-structured jobs with large memory footprints, which models a fundamental problem in serving large foundation models through pipeline parallelism. After showing the NP-hardness of the optimal solution, the focus is turned to developing scalable algorithms with guaranteed performance under state-of-the-art load balancing. Application of the proposed solution to a distributed large language model (LLM) serving system shows significant reduction of response times compared to state-of-the-art solutions.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
