# 2026-10-11 LLM 服务系统每日文献简报

> 检索窗口：2026-10-10 至 2026-10-11（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 在移动人工智能工具中部署大型语言模型 (LLM) 的模型蒸技术

> 英文原标题：Model Distillation Techniques for Deploying Large Language Models (LLMs) in Mobile AI Tools

- **作者：** Jeffery Podolski
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-10；SSRN/Crossref
- **分类：** 数据中心能源、碳与跨时段转移；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7590859) · [DOI](https://doi.org/10.2139/ssrn.7590859)

### 一两句话看懂

这篇论文关注“数据中心能源、碳与跨时段转移”，重点涉及 large language model、large language models、llm、energy consumption。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型 (LLM) 在移动和边缘设备上部署仍然基本上受到模型能力和硬件可行性之间的紧张局限. 虽然数十亿参数模型在自然语言任务中实现了显著的性能,但它们的内存足迹,推断延迟和能源消耗远远超过智能手机和嵌入式系统的持续性. 知识蒸 (KD) 已成为将LLM压缩到适合设备部署的紧学生模型的主要技术,但在转移推理能力,保持安全配合和优化异性移动硬件方面仍然存在重大挑战. 本文介绍了针对移动人工智能工具部署LLM的模型蒸技术的系统性审查和分析. 我们研究了白盒方法 (基于logit的蒸,反向KL分离,层次的暗示转移) 和黑盒技术 (思想链蒸,指令后转移,文本蒸),以及包括量化和剪裁在内的补充压缩策略. 通过分析最近的基准标准的实验结果,我们确定了模型压缩,响应质量和延迟之间的三方面的交易, 我们的发现表明,结合知识传输与激活意识的量化的混合蒸管道使10亿次参数模型能够在CPU平台上实现500ms以下的响应延迟,同时在特定领域任务上保持大约85-90%的教师模型准确性. 我们进一步分析开放的挑战,包括跨架构蒸中的词汇不匹配,自动降低的学生模型中的错误复合,积极压缩下的安全保护以及移动LLM部署的标准化评估框架的缺乏. 该审查为研究人员和实践者提供了一个结构性参考,他们希望在模型能力和移动部署限制之间的设计空间中进行导航.

### 英文原摘要

The deployment of large language models (LLMs) on mobile and edge devices remains fundamentally constrained by the tension between model capability and hardware feasibility. While multi-billion-parameter models achieve remarkable performance across natural language tasks, their memory footprint, inference latency, and energy consumption far exceed what smartphones and embedded systems can sustain. Knowledge distillation (KD) has emerged as a primary technique for compressing LLMs into compact student models suitable for on-device deployment, yet significant challenges persist in transferring reasoning capabilities, preserving safety alignment, and optimizing for heterogeneous mobile hardware. This paper presents a systematic review and analysis of model distillation techniques specifically for deploying LLMs in mobile AI tools. We examine the methodological landscape across white-box approaches (logit-based distillation, reverse KL divergence, layer-wise hint transfer) and black-box techniques (chain-of-thought distillation, instruction-following transfer, context distillation), alongside complementary compression strategies including quantization and pruning. Through analysis of empirical results from recent benchmarks, we identify a three-way trade-off between model compression, response quality, and latency that governs deployment feasibility on mobile-class hardware. Our findings indicate that hybrid distillation pipelines combining knowledge transfer with activation-aware quantization enable sub-billion-parameter models to achieve sub-500ms response latency on CPU platforms, while preserving approximately 85-90% of teacher model accuracy on domain-specific tasks. We further analyze open challenges including vocabulary mismatch in cross-architecture distillation, error compounding in autoregressive student models, safety preservation under aggressive compression, and the lack of standardized evaluation frameworks for mobile LLM deployment. This review provides a structured reference for researchers and practitioners seeking to navigate the design space between model capability and mobile deployment constraints.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
