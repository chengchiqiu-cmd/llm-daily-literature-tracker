# 2026-08-14 LLM 服务系统每日文献简报

> 检索窗口：2026-08-13 至 2026-08-14（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文附数据源原始摘要，并用一两句话概括研究内容。模型、公式和完整结论留到后续精读。

## 1. Right-Sized Distillation of an Edge Large Language Model for Live Multi-Protocol IoT Traffic Classification

> 英文原标题：Right-Sized Distillation of an Edge Large Language Model for Live Multi-Protocol IoT Traffic Classification

- **作者：** Dimitris Koutras、Vangelis Paklatzis、Panayiotis Kotzanikolaou
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-13；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7276712) · [DOI](https://doi.org/10.2139/ssrn.7276712)

### 一两句话看懂

这篇论文关注“LLM 推理排队与调度”，重点涉及 large language model、large language models、llm、queuing。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 原始摘要

Low-power IoT deployments rely extensively on lightweight protocols such as the Constrained Application Protocol (CoAP) and Message Queuing Telemetry Transport (MQTT). While engineered for low overhead, this minimalism inherently strips away strong authentication and rate-limiting mechanisms, exposing a broad attack surface that includes CoAP amplification, MQTT Denial-of-Service (DoS), and TCP-based exploits. Existing intrusion detection systems largely depend on classical machine-learning classifiers; although accurate, these models only output opaque class indices. Conversely, Large Language Models (LLMs) can provide human-readable rationales and actionable mitigation strategies, yet their large memory footprint, high inference latency, and lack of protocol-specific awareness conventionally preclude their deployment on resource-constrained edge appliances. To overcome these limitations, this paper proposes a novel closed-loop pipeline for multi-protocol edge inference. Our methodology applies a right-sized teacher-distillation approach, combined with parameter-efficient Quantized Low-Rank Adaptation (QLoRA) fine-tuning, to adapt a compact 2B effective-parameter student model from a moderately sized 4B teacher. We evaluate the proposed edge-deployable model against three large 27–31B reference models within a live, deterministic flow-window stream. Experimental results demonstrate that our approach achieves an optimal operational trade-off, attaining 95% recall on CoAP amplification with only a 1.2% False-Alarm Rate (FAR). Furthermore, it achieves 100% recall for MQTT DoS, 82% for malformed MQTT, 100% for TCP scanning, and 86% for Telnet brute-force attacks. The results show that right-sized distillation produces an edge-feasible LLM that remains competitive with classical Machine Learning (ML), while additionally providing explanations and attack-specific mitigation guidance.

## 2. Asterism: A Hebbian-Weighted Knowledge Graph as a Priority Index over Long-Term LLM Memory

> 英文原标题：Asterism: A Hebbian-Weighted Knowledge Graph as a Priority Index over Long-Term LLM Memory

- **作者：** Bidit Das
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-13；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7257118) · [DOI](https://doi.org/10.2139/ssrn.7257118)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、llm、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 原始摘要

Large language model (LLM) assistants increasingly persist user information across sessions as unstructured "memory" summaries. Such summaries behave like an unindexed heap: every stored fact carries equal retrieval priority, and nothing signals which facts currently matter most to the user. We present Asterism, a local-first system that builds a weighted, decaying knowledge graph from conversation history and injects a ranked subset of it into the model's context at inference time. The central design claim is architectural: the graph functions as a priority index over flat memory, in the same sense that a B-tree indexes an ordered file, with node weight acting as a salience signal analogous to an index key. We evaluate the mechanism on a seeded personal graph across three retrieval conditions (weighted graph, unweighted flat list, and no memory) and report a specific, bounded finding: the graph's advantage over a flat list is not recall but decisiveness under ambiguity. On a set of priority-ranking queries scored with a pre-registered, held-out-validated commit/hedge metric, the graph-conditioned model commits to a weight-justified answer on 7 of 12 queries, versus 4 of 12 for a flat list of the same facts and 0 of 12 with no memory; the flat list, seeing identical facts but lacking a salience signal, more often defers the ranking back to the user. In short: the weighting helps the model decide, not merely remember. We further characterize two engineering components required to make the graph trustworthy as an index: an entity-resolution layer whose accuracy ceiling we measure empirically, and a supersession mechanism that demotes contradicted facts from default retrieval. Local retrieval latency scales approximately linearly, remaining near 34 ms at 10,000 nodes. We release the full system, benchmarks, and negative results.

## 3. Vertical Integration and Pricing in the AI Industry:Evidence from Foundation Model Markets

> 英文原标题：Vertical Integration and Pricing in the AI Industry:Evidence from Foundation Model Markets

- **作者：** Nuwan Indika、Adeel Faheem
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-08-13；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7276625) · [DOI](https://doi.org/10.2139/ssrn.7276625)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 foundation model、pricing。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 原始摘要

This paper analyzes vertical integration in artificial-intelligence markets in which foundation-model providers supply inference capacity to downstream application developers while also offering their own downstream applications. Extending Salinger (1988, 1991) and Luco and Marshall (2020), we show that integration creates asymmetric price effects through a portfolio mechanism: eliminating double marginalization lowers the price of the integrated application, while the induced change in relative margins can raise the prices of unintegrated substitutes. We document three recent integration cases--OpenAI's ChatGPT, Anthropic's Claude.ai, and Google's Gemini applications--where foundation-model providers increasingly compete downstream while continuing to supply rivals. The corrected framework uses logit demand, linear wholesale pricing, and multiproduct downstream pricing. In the baseline calibration, integration reduces the integrated application's price by 12.9 percent and increases the unintegrated application's price by 6.5 percent. Consumer surplus rises by 13.3 percent, producer surplus is essentially unchanged, and total welfare rises by 4.9 percent. The portfolio effect reduces the consumer-surplus gain by 22.7 percent relative to a no-portfolio counterfactual. Diversion ratios provide a practical antitrust diagnostic: unintegrated-product price increases exceed five percent when diversion from the integrated product is below about D=0.36. The framework offers an implementable screening tool for AI vertical integration when detailed cost and contract data are unavailable.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 原始摘要完整保留；如果数据源没有摘要，会明确显示“数据源未提供摘要”。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
