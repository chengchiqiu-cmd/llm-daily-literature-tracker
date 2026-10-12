# 2026-10-12 LLM 服务系统每日文献简报

> 检索窗口：2026-10-11 至 2026-10-12（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 超越光束:穿越内皮层语音解码与声学候选扩展和自信门式语言模型恢复

> 英文原标题：Beyond the Beam: Cross-Fitted Intracortical Speech Decoding with Phonetic Candidate Expansion and Confidence-Gated Language-Model Rescoring

- **作者：** Anik Biswas、Md. Shohanur Rahman
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-11；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7589721) · [DOI](https://doi.org/10.2139/ssrn.7589721)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、llm、deadline。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

内皮层语音神经合成通过链接一个神经模型到音符模型,一个词典限制光束搜索和,越来越多,一个大型语言模型 (LLM) 来解码试图的语音.两种数量很少被报告为公众基准:由于正确的句子从未达到最终得分者,所以发生了多少错误,以及在试验中是否调节了解码器重量. 我们构建了一个测量这两种方法的解码器.标签的验证试验在记录区内交叉安装,因此每个解码器重量都安装在外折输出上,五分之一的试验都保留用于验证.来自多种语言模型重量的光束搜索候选人被聚合起来,用单声语字替代扩大,并用精确的连接定时分类 (CTC) 概率恢复. 采用QLoRA适应的Llama-3.1-8B评分一个短名单,而一个信任门降低了对不可思议的言论的语言模型权重. 通过使用两个16GB的GPU训练的30.2M参数声学模型,该系统在私人Brain-to-Text '25延迟 (4.30%公开;截止日期后得分) 和 Brain-to-Text '24延迟 (8.54%),而在组织者基线的6.67%和9.76%之间达到5.16%的字体错误率 (WER).在验证折叠中,WER从5.75%降至2.85%和12.98%降至8.59%相对于光束搜索1-最佳. 由于光束搜索从未发出了"做"这个词,因此部分收益修复了第一次通过缺陷;在没有它的发言中,外折 WER仍然从4.54%下降到3.34%和从12.08%下降到10.34%.在LLM得分短暂列表中缺席的引用会导致37%和60%的剩余错误.

### 英文原摘要

Intracortical speech neuroprostheses decode attempted speech by chaining a neural-to-phoneme model, a lexicon-constrained beam search and, increasingly, a large language model (LLM). Two quantities are seldom reported for the public benchmarks: how many errors occur because the correct sentence never reached the final scorer, and whether decoder weights were tuned on trials the acoustic model had seen. We build a decoder that measures both. Labelled validation trials are cross-fitted inside recording blocks, so every decoder weight is fitted on out-of-fold outputs and one fifth of the trials is kept for verification. Beam-search candidates from several language-model weights are pooled, enlarged with one-phoneme word substitutions, and rescored with exact connectionist temporal classification (CTC) likelihoods. A QLoRA-adapted Llama-3.1-8B scores a shortlist, and a confidence gate reduces the language-model weights for implausible utterances. With a 30.2M-parameter acoustic model trained on two 16 GB GPUs, the system reached a word error rate (WER) of 5.16% on the private Brain-to-Text '25 hold-out (4.30% public; scored after the deadline) and 8.54% on the Brain-to-Text '24 hold-out, against 6.67% and 9.76% for the organisers' baselines. On the verification fold, WER fell from 5.75% to 2.85% and from 12.98% to 8.59% relative to the beam-search 1-best. Part of this gain repairs a first-pass defect, since the beam search never emitted the word do; on utterances without it, out-of-fold WER still fell from 4.54% to 3.34% and from 12.08% to 10.34%. References absent from the LLM-scored shortlist that would have won if scored cause 37% and 60% of remaining errors.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
