# 2026-09-07 LLM 服务系统每日文献简报

> 检索窗口：2026-09-06 至 2026-09-07（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 建筑运营中的维护优先级分类自然语言处理：基于词典、BERT 与大语言模型方法的比较研究

> 英文原标题：Natural language processing for maintenance priority classification in building operation: a comparative study of lexicon-based, BERT, and large language model approaches

- **作者：** Marco D'Orazio、Elisa Di Giuseppe、Gabriele Bernardini
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-06；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7422586) · [DOI](https://doi.org/10.2139/ssrn.7422586)

### 一两句话看懂

论文比较了三类自然语言处理方法如何根据建筑维护请求的文本内容，将请求分为高、中、低三种优先级。基于两个大学校园、超过4万条请求的测试显示，基于Transformer的模型表现最好，准确率超过0.95；词典方法整体表现较好但难以识别中等紧急程度，大语言模型则需要进行领域适配才能可靠使用。

### 中文摘要（翻译）

计算机化维护管理系统（Computerized Maintenance Management Systems，CMMS）包含大量自由文本请求，这些请求通常被用于组织建筑维护工作。人工智能驱动的技术可以利用CMMS数据提高维护人员的工作效率，并增强建筑运营的连续性。其中，自动分配优先级是一个极其重要的主题，有助于实现更快速且更一致的分诊。在这一总体背景下，本研究比较了三种用于将请求分类为高、中、低优先级的自然语言处理（Natural Language Processing，NLP）方案：基于词典的方法、监督式基于Transformer的分类器，以及大语言模型（Large Language Model）。所有方法均在来自两个大学校园的超过40,000条请求上进行了测试。研究首先采用共同的初步文本规范化处理，随后进行各模型特定的预处理和分词；同时，使用相同的类别级指标和总体指标评估性能。结果显示，基于Transformer的模型优于其他方法，准确率超过0.95，并且在各优先级类别之间实现了均衡分类。基于词典的建模在总体表现上较好，但无法有效识别中等紧急程度；大语言模型则需要进行领域适配，才能可靠部署。因此，这项比较为三种部署情境提供了证据，而不是证明某一种架构具有内在优越性。研究结果支持：当存在带标签数据时，应采用针对具体任务的情境建模；词典可以作为透明的辅助组件；并且，在没有进行领域适配、类别级验证和人工监督的情况下，所考察的大语言模型配置不应被用于运营决策。尽管研究没有量化能源和舒适度影响，但该工作流程构成了一个支持性运营层，可用于确定那些会影响建筑性能的系统的干预优先级。

### 英文原摘要

Computerized Maintenance Management Systems (CMMSs) contain large volumes of free-text requests that are routinely used to organize building maintenance. Artificial Intelligent-driven technologies can use CMMS data to improve maintenance workforce productivity and strengthen the continuity of building operation. Above all, automating priority assignment represents one paramount topic, supporting faster and more consistent triage. In this overall context, this study compares three Natural Language Processing (NLP) scenarios for classifying requests as high, medium and low priority: a lexicon-based approach, a supervised transformer-based classifier, and a Large Language Model. All approaches were tested on over 40000 requests from two university campuses. A common preliminary text normalisation is followed by model-specific preprocessing and tokenisation, while performance is assessed using the same class-level and aggregate metrics. Results show that the transformer-based model outperforms the alternatives, with over 0.95 accuracy and balanced classification across priority classes. Lexicon-based modelling performs well globally but fails on intermediate urgency detection, while the Large Language Model requires domain adaptation for reliable deployment. The comparison therefore provides evidence on three deployment scenarios rather than the intrinsic superiority of one architecture. The results support task-specific contextual modelling when labelled data are available, position lexicons as transparent supporting components, and show that the examined LLM configuration should not be used for operational decisions without domain adaptation, class-level validation, and human oversight. Although energy and comfort effects are not quantified, the workflow constitutes an enabling operational layer for prioritizing interventions on systems that influence building performance.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
