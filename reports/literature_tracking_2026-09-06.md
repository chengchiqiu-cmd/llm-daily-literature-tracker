# 2026-09-06 LLM 服务系统每日文献简报

> 检索窗口：2026-09-05 至 2026-09-06（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 买更大的模型，还是使用更长提示：面向准确率的LLM推理能耗前沿

> 英文原标题：Buy Bigger or Prompt Longer: Accuracy-Targeted Energy Frontiers for LLM Inference

- **作者：** Dhairya Sarin、Gokul Prabhu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-05；SSRN/Crossref
- **分类：** 数据中心能源、碳与跨时段转移；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7393439) · [DOI](https://doi.org/10.2139/ssrn.7393439)

### 一两句话看懂

论文研究在提升大语言模型（LLM）准确率时，使用更大模型与采用更复杂提示策略，哪种方式更节能。作者测量了9个开源LLM在5项基准测试上的GPU推理能耗，发现许多模型—策略组合同时存在更便宜且更准确的替代方案，而且模型家族的选择有时比提示策略对能效影响更大。

### 中文摘要（翻译）

随着部署中的大语言模型（LLM）系统处理的查询量不断增加，推理能耗成为人工智能总能耗中的一个重要组成部分。实践者经常面临这样的决策：是通过扩展到更大的模型来提高准确率，还是采用思维链（chain-of-thought，CoT）推理或少样本示例（few-shot exemplars）等提示策略。两种选择都会增加计算成本，但它们在能耗与准确率之间的权衡尚未得到充分刻画。在本文中，我们测量了9个开源LLM的GPU推理能耗。这些模型来自5个模型家族，参数量范围为0.5B至14.7B，并覆盖5项标准化基准测试；我们比较了直接（0-shot）推理与增强提示策略的表现（数学推理任务使用8-shot CoT，其他任务使用少样本示例）。利用NVIDIA A100 GPU的实际功耗遥测数据，我们为每项基准测试构建了准确率—能耗Pareto前沿，并观察到，在所测试的模型—策略组合中，有56%—72%处于能耗劣势（energy-dominated），这意味着存在严格意义上成本更低且准确率更高的替代方案。当增强提示出现在Pareto前沿上时，它主要出现在准确率范围的高端；在这一范围内，所评估模型中的直接提示无法达到同样的准确率。在5项基准测试中的两项（MMLU和HellaSwag）上，完全没有增强提示配置进入前沿。此外，我们还观察到，模型家族的选择对能效的影响可能大于提示策略：在某些情况下，一个模型家族中的较小模型在准确率和能耗两方面都优于另一个模型家族中的较大模型。这些结果表明，与默认采用增强提示相比，考虑能耗的模型选择通常可以降低推理能耗。本分析仅限于单一GPU平台上、参数量不超过14.7B的开放权重模型，未来应在更大规模以及生产环境的服务基础设施上进行验证。

### 英文原摘要

As deployed LLM systems serve increasing query volumes, inference energy becomes an important component of total AI energy consumption. Practitioners face a recurring decision: improve accuracy by scaling to a larger model, or by applying prompting strategies such as chain-of-thought (CoT) reasoning or few-shot exemplars. Both options increase computational cost, but their energy-accuracy trade-offs are poorly characterized. In this paper, GPU inference energy for 9 open-source LLMs spanning 5 model families (0.5B-14.7B parameters) across 5 standardised benchmarks was measured, comparing direct (0-shot) inference against enhanced prompting strategies (8-shot CoT for mathematical reasoning; few-shot exemplars for other tasks). Using real power telemetry from an NVIDIA A100 GPU, accuracy-energy Pareto frontiers for each benchmark were constructed, and it was observed that 56-72% of tested model-strategy configurations are energy-dominated, meaning a strictly cheaper and more accurate alternative exists. When enhanced prompting appears on the Pareto frontier, it does so primarily at the upper end of the accuracy range, where direct prompting among the evaluated models does not reach the same accuracy. On two of five benchmarks (MMLU and HellaSwag), no enhanced prompting configuration reaches the frontier at all. Further, it was observed that model family selection can have a larger effect on energy efficiency than prompting strategy: in some cases, a smaller model from one family dominates a larger model from another on both accuracy and energy. These results suggest that energy-aware model selection can often reduce inference energy relative to applying enhanced prompting by default. This analysis is limited to open-weight models up to 14.7B parameters on a single GPU platform and should be validated at larger scales and on production serving infrastructure.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
