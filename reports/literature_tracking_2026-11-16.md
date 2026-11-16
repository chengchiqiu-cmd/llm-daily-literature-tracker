# 2026-11-16 LLM 服务系统每日文献简报

> 检索窗口：2026-11-15 至 2026-11-16（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. RPS-Service: "岩石,石头和沙子:多模式LLM推理的规范性意识规划" (SIGOPS ATC '26) 的艺术品

> 英文原标题：RPS-Serve: Artifact for "Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal LLM Inference" (SIGOPS ATC '26)

- **作者：** Konstantinos Papaioannou、Thaleia Dimitra Doudali
- **来源/日期：** Zenodo (CERN European Organization for Nuclear Research)；2026-11-15；OpenAlex
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 12
- **链接：** [论文页](https://doi.org/10.5281/zenodo.23134684) · [DOI](https://doi.org/10.5281/zenodo.23134684)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、llm、llm inference、scheduling。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

这个文物伴随着Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference. 它包装了RPS-Serve,一个基于vLLM (v0.21.1) 的多模式LLM (MLLM) 服务的modality-aware request scheduling framework,以及修补的基线,工作负载生成器和用于制作论文结果的图案脚本. 该文物包括:RPS-Serve本身 (影响估计器,请求分类器,队列管理器和优先级监管器),用于部署基线系统的补丁vLLM (vLLM,ModServe和ModServe与RPS),用于工作负载生成和重播的GuideLLM和LLMPerf的补丁版本,用于评估的模型以及从原料实验输出中再生纸张数据的脚本. 审查人员可以使用这个文物安装软件堆,生成纸张的混合模式工作负载,在单个GPU上运行最小的端到端示例,并在可用的硬件尺度上复制纸张的实验和数字.

### 英文原摘要

This artifact accompanies Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference. It packages RPS-Serve, a modality-aware request scheduling framework for multimodal LLM (MLLM) serving built on top of vLLM (v0.21.1), together with the patched baselines, workload generators, and plotting scripts used to produce the paper's results. The artifact includes: RPS-Serve itself (Impact Estimator, Request Classifier, Queue Manager, and Priority Regulator), a patched vLLM used to deploy the baseline systems (vLLM, ModServe, and ModServe with RPS), patched versions of GuideLLM and LLMPerf for workload generation and replay, the models used for evaluation, and scripts to regenerate the paper's figures from raw experiment output. Reviewers can use this artifact to install the software stack, generate the paper's mixed-modality workloads, run a minimal end-to-end example on a single GPU, and reproduce the paper's experiments and figures at the hardware scale available to them.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
