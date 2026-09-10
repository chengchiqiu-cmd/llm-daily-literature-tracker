# 2026-09-11 LLM 服务系统每日文献简报

> 检索窗口：2026-09-10 至 2026-09-11（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. AgentPN 基准测试：面向企业专用网络的意图型 AI 智能体确定性安全评估

> 英文原标题：AgentPN Benchmark Test: Deterministic Safety Evaluation of Intent-based AI Agents for Enterprise Private Networks

- **作者：** Onur Sahin、Vanlin Sathya、Lyutianyang Zhang、Kalpana Naidu
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-10；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7411900) · [DOI](https://doi.org/10.2139/ssrn.7411900)

### 一两句话看懂

论文提出了 AgentPN Benchmark Test，用一组可重复、由脚本判定的合成场景，评估意图型 AI 智能体在企业专用 5G/LTE 和未来专用 6G 网络中执行控制任务前，是否能遵守安全、隐私、关键服务优先级、人工审批、回滚和审计等要求。对两个开源权重模型端点进行 420 次测试后，gpt-oss-120b 的通过率为 44.8%，gpt-oss-20b 的通过率为 24.3%；论文据此指出，未通过该基准测试的智能体不应被视为已准备好在相应企业约束下控制专用网络。

### 中文摘要（翻译）

企业专用 5G/LTE 以及正在出现的专用 6G 系统，正日益支持医院、工厂、仓库、港口、能源场所、数据中心和园区中的安全关键型应用。意图型 AI 智能体可以将运营者目标转化为网络操作，但专用网络控制要求明确保留安全性、隐私、数据本地性、关键服务优先级、人工审批、回滚和可审计性。本文提出 AgentPN Benchmark Test，这是一项确定性的决策安全基准测试，用于在意图型 AI 智能体接触企业专用网络控制界面之前对其进行评估。AgentPN 包含 210 个由专家设计的合成场景，涵盖七个企业垂直行业和六类横向任务。每个公开案例都会提供现场背景、网络状态、运营者意图、政策、证据、架构元数据以及中立的候选操作；隐藏的真实标准则规定必需、可选、需审批后执行和禁止的操作，以及关于本地性、验证、回滚、审计、风险和关键性的要求。智能体输出被限制为结构化 JSON 模式，并依据确定性的脚本判定规则评为 PASS、PARTIAL、UNSAFE 或 INVALID，而不是采用由大语言模型担任评判者的评估方式。在对两个经 OpenRouter 路由的开源权重模型端点进行 420 次评估后，结果显示：gpt-oss-120b 的 PASS、PARTIAL、UNSAFE 和 INVALID 结果占比分别为 44.8%、20.0%、9.5% 和 25.7%；gpt-oss-20b 的 PASS 结果占比为 24.3%，UNSAFE 结果占比为 32.9%。我们进一步使用资源、成本和时间线影响方程量化运营暴露，展示不安全智能体的比例如何在高速自动化环境中放大。AgentPN 是一种就绪度筛选工具：在经过基准测试的企业约束下，未通过该测试的智能体不应被视为已准备好控制专用网络。

### 英文原摘要

Enterprise private 5G/LTE and emerging private 6G systems increasingly support safety-critical applications in hospitals, factories, warehouses, ports, energy sites, data centers, and campuses. Intent-based AI agents can translate operator goals into network actions, but private-network control requires explicit preservation of security, privacy, data locality, critical-service priority, human approval, rollback, and auditability. This paper introduces AgentPN Benchmark Test, a deterministic decision-safety benchmark for evaluating intent-based AI agents before they interact with enterprise private-network control surfaces. AgentPN contains 210 synthetic expertdesigned scenarios organized across seven enterprise verticals and six horizontal task families. Each public case exposes site context, network state, operator intent, policies, evidence, architecture metadata, and neutral candidate actions; hidden ground truth specifies required, optional, approval-gated, and forbidden actions together with locality, validation, rollback, audit, risk, and criticality requirements. Agent outputs are restricted to a structured JSON schema and are scored by deterministic script-based PASS/PARTIAL/UNSAFE/INVALID rules rather than LLM-asjudge evaluation. A 420-run evaluation of two OpenRouter-routed open-weight model endpoints shows that gpt-oss-120b attains 44.8% PASS, 20.0% PARTIAL, 9.5% UNSAFE, and 25.7% INVALID outcomes, while gpt-oss-20b attains 24.3% PASS and 32.9% UNSAFE outcomes. We further quantify operational exposure using resource-, cost-, and timeline-impact equations, showing how unsafe-agent rates amplify in high-velocity automation settings. AgentPN is a readiness filter: an agent that fails it should not be considered ready for private-network control under the benchmarked enterprise constraints.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
