# 2026-09-12 LLM 服务系统每日文献简报

> 检索窗口：2026-09-11 至 2026-09-12（北京时间 / Asia/Shanghai）；本期确认 2 篇，其中直接 LLM 服务研究 2 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 面向推理工作负载的基于指标驱动、支持动态 MPS GPU 共享的 Kubernetes Operator

> 英文原标题：A Metric-Driven Kubernetes Operator for Dynamic MPS-Based GPU Sharing in Inference Workloads

- **作者：** Papon Choonhaklai、Kohei Ichikawa、Kundjanasith Thonglek、Hajimu Iida
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-11；SSRN/Crossref
- **分类：** LLM 推理排队与调度；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7446799) · [DOI](https://doi.org/10.2139/ssrn.7446799)

### 一两句话看懂

论文研究如何在不支持 MIG 的消费级 GPU 上，让 Kubernetes 更充分地共享 GPU，以提升大语言模型推理任务的资源利用率。作者提出了一个基于运行时硬件指标进行调度的 Kubernetes Operator；真实 LLM 推理工作负载的评估显示，该方法达到 89% 的 GPU 利用率、60% 的显存使用率、34,183 毫秒的最低平均响应时间，并保持零错误率。

### 中文摘要（翻译）

随着深度学习模型在 Kubernetes 集群中的部署不断增加，高效的 GPU 共享机制变得十分必要，尤其是对于不支持多实例 GPU（Multi-Instance GPU，MIG）的消费级 GPU。这类 GPU 广泛存在于学术界、初创企业和边缘计算环境中；在这些场景下，成本限制使得使用高端数据中心硬件并不可行。一个关键挑战是，Kubernetes 原生地将 GPU 视为不可分割的整体资源，这会导致资源被大量闲置，尤其是在无法完全占满 GPU 的推理工作负载中。为了解决这一低效问题，我们提出了一种基于指标驱动的 Kubernetes Operator，通过 NVIDIA 多进程服务（Multi-Process Service，MPS）实现进程级 GPU 共享。我们的系统利用 Nebuly OS（NOS）在各节点上激活 MPS 守护进程，并采用运行时硬件遥测数据——例如 GPU 利用率、显存使用量和错误代码——来指导调度决策。不同于依赖自定义资源定义（Custom Resource Definitions，CRDs）的既有方法，我们的 Operator 只使用一个简单的 Pod 标签，从而简化了在 Kubernetes 上的部署。使用真实世界的 LLM 推理工作负载进行的实证评估证明了该方法的有效性。该方法实现了 89% 的 GPU 利用率和 60% 的显存使用率，同时实现了最低的平均响应时间（34,183 毫秒），并保持零错误率。与 NVIDIA time-slicing 和独立运行的 NOS 相比，我们的方法能够有效支持高吞吐量和弹性的推理工作负载。

### 英文原摘要

The increasing deployment of deep learning models in Kubernetes clusters demands efficient GPU sharing mechanisms, especially for consumer-grade GPUs that lack Multi-Instance GPU (MIG) support. Such GPUs are prevalent in academia, startups, and edge computing environments, where cost constraints prevent the use of high-end datacenter hardware. A key challenge is that Kubernetes natively treats GPUs as monolithic resources, leading to significant underutilization, especially for inference workloads that do not fully saturate a GPU. To address this inefficiency, we propose a metric-driven Kubernetes operator that enables process-level GPU sharing through the NVIDIA Multi-Process Service (MPS). Our system leverages Nebuly OS (NOS) to activate MPS daemons across nodes and employs runtime hardware telemetry—such as GPU utilization, memory usage, and error codes—toguide scheduling decisions. Unlike prior methods that rely on custom resource definitions (CRDs), our operator uses only a simple pod label, simplifying deployment on Kubernetes. Empirical evaluations using a real-world LLM inference workload demonstrate the efficacy of our approach. It achieved 89% GPU utilization and 60% memory usage while delivering the lowest average response time (34,183 ms) and maintaining a zero-error rate. Compared to NVIDIA time-slicing and standalone NOS, our approach effectively supports high-throughput and elastic inference workloads.

## 2. 将大型语言模型智能体与强化学习进行基准比较：用于建筑需求响应

> 英文原标题：Benchmarking Large Language Model Agents against Reinforcement Learning for Building Demand Response

- **作者：** Rui Wang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-11；SSRN/Crossref
- **分类：** 数据中心能源、碳与跨时段转移；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7447344) · [DOI](https://doi.org/10.2139/ssrn.7447344)

### 一两句话看懂

论文研究大型语言模型（LLM）智能体能否像强化学习控制器一样，有效协调建筑中的灵活用电设备，以降低成本、控制用电峰值并避免配电馈线过载。作者建立统一评测框架进行比较，结果显示，在合成数据中，PPO、SAC和残差强化学习总体优于在线LLM智能体；LLM决策速度也比已学习的策略慢1,000—10,000倍。

### 中文摘要（翻译）

灵活的建筑负荷可以降低成本并缓解电力网络压力，但车队控制必须协调异质设备，同时避免产生需求峰值、舒适度违规或馈线过载。大型语言模型（large language model，LLM）智能体有望实现适应性强、零样本的控制，但由于与经过训练的数值控制器进行比较时，很少使用匹配的轨迹，也没有始终如一地考虑不确定性和推理成本，因此其运行价值仍不明确。我们通过DRBENCH这一通用评测框架弥补这一空白。该框架涵盖基于规则的控制、模型预测控制（model predictive control，MPC）、强化学习（reinforcement learning，RL）、协调式强化学习与残差强化学习，以及三种LLM智能体设计。该框架通过共享馈线耦合建筑和设备动态，在相同回合上使用配对统计评估各种方法，测量推理开销，并考察向CityLearn数据的迁移。研究结果表明，仅凭灵活的语言推理并不能产生有效的实时调度。在合成评估中，PPO和SAC在成本和峰值控制方面优于所有接受评估的在线LLM智能体，并且避免了所观察到的馈线过载。相较于PPO，直接使用LLM控制会使每周电费增加309美元，而在线LLM决策的速度比已学习策略的推理慢1,000—10,000倍。残差强化学习取得了最强的平均表现，说明学习过程可以从改进结构化控制先验中获益。CityLearn提供了一项重要限定：直接智能体和ReAct智能体的表现优于固定的分时电价规则，但没有优于MPC；在该设置下未评估RL。总体而言，证据支持使用数值控制器进行运行调度，并更有说服力地将LLM定位为用于规范说明、奖励设计和控制器配置的离线辅助工具。

### 英文原摘要

Flexible building loads can reduce costs and relieve power networks, but fleet control must coordinate heterogeneous devices without creating demand peaks, comfort violations, or feeder overload. Large language model (LLM) agents promise adaptable, zero-shot control, but their operational value remains unclear because comparisons with trained numerical controllers rarely use matched trajectories or consistently account for uncertainty and inference cost. We address this gap with DRBENCH, a commonevaluation frameworkfor rule-based control, model predictive control (MPC), reinforcement learning (RL), coordinated and residual RL, and three LLM-agent designs. The framework couples building and device dynamics through a shared feeder, evaluates methods on identical episodes with paired statistics, measures inference overhead, and examines transfer to CityLearn data. The findingsshow that flexible language reasoning alone does not produce effective real-time dispatch. In the synthetic evaluation, PPO and SAC outperform all evaluated online LLM agents on cost and peak control and avoid the observed feeder overloads. Direct LLM control increases the weekly bill by $309 relative to PPO, while online LLM decisions are 1,000–10,000 times slower than learned-policy inference. Residual RL gives the strongest mean performance, indicating that learning benefits from refining a structured control prior. CityLearn provides an important qualification: direct and ReAct agents improve on a fixed time-of-use rule but not on MPC, and RL is not evaluated in that setting. Overall, the evidence supports numerical controllers for operational dispatch and positions LLMs more credibly as offline aids for specification, reward design, and controller configuration.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
