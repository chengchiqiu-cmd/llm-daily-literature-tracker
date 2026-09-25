# 2026-09-26 LLM 服务系统每日文献简报

> 检索窗口：2026-09-25 至 2026-09-26（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 关闭形式成本,延迟和流量限制在实时流处理中的LLM电话

> 英文原标题：Gating Beats Batching: Closed-form Cost, Latency, and Concurrency Bounds for LLM Calls in Real-Time Stream Processing

- **作者：** Sagar Vishnubhai Sheta
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-25；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7508098) · [DOI](https://doi.org/10.2139/ssrn.7508098)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、large language models、llm、slo。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

流处理系统越来越多地调用大型语言模型 (LLM) 来分类,丰富或解释事件,但每次调用都会增加代币成本和延迟的秒到数毫秒内构建的管道. 这项研究在三个调用策略下对实时管道中的LLM调用成本,延迟和同步性产生了封闭形式的限制. 每次事件调用每次事件一次调用LLM,微批发每次调用发送b事件,并且门接调用LLM只在廉价上游过器选择的事件的小部分 f上.该模型结合了一个基于代币的成本方程,线性生成时间延迟模型和利特尔的定律,并产生最大的批量大小,满足延迟服务水平目标 (SLO). 在每百万输入和输出代币的中端价格为1美元和5美元,每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每次电话每 关闭1%的事件削减成本是100倍,加上关闭与SLO限制的批量降低了每日成本到389美元.结果给管道设计师一个操作顺序:关闭第一,批次,选择模型层次第三.这项研究是分析性的,生产管道的测量仍然是未来的工作.

### 英文原摘要

Stream processing systems increasingly call large language models (LLMs) to classify, enrich, or explain events, yet each call adds token cost and seconds of latency to a pipeline built for milliseconds. This study derives closed-form bounds on the cost, latency, and concurrency of LLM calls in a realtime pipeline under three invocation strategies. Per-event invocation calls the LLM once per event, micro-batching sends b events per call, and gating calls the LLM only on a fraction f of events that a cheap upstream filter selects. The model combines a token-based cost equation, a linear generationtime latency model, and Little's law, and it yields the largest batch size that meets a latency servicelevel objective (SLO). At illustrative mid-range prices of $1 and $5 per million input and output tokens, per-event calls at 1,000 events per second cost $90,720 per day and keep 750 requests in flight. A $1,000 daily budget covers only 11 events per second. Batching amortizes only the shared prompt, so its savings cap at 4.2 times, and a 2-second SLO limits batches to 5 events and savings to 2.56 times. Gating 1% of events cuts cost 100 times, and gating combined with SLO-bounded batching lowers the daily cost to $389. The results give pipeline designers an order of operations: gate first, batch second, and choose the model tier third. The study is analytical, and measurement on production pipelines remains future work.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
