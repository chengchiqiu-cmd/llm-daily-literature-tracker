# 2026-10-07 LLM 服务系统每日文献简报

> 检索窗口：2026-10-06 至 2026-10-07（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 对于LLM请求路由的政策约束,知情的部署保证

> 英文原标题：Policy-Bounded, Provenance-Aware Deployment Assurance for LLM Request Routing

- **作者：** Yihua Xu、Jiani He、Ishita Chirag Talati、Yitian Qian、Youting Wang、Zhenyu Xu、Dingyan Shang
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-10-06；SSRN/Crossref
- **分类：** 容量、云资源与服务运营；直接 LLM 服务研究；相关性评分 8
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7554440) · [DOI](https://doi.org/10.2139/ssrn.7554440)

### 一两句话看懂

这篇论文关注“容量、云资源与服务运营”，重点涉及 llm、capacity planning、capacity、provider。从摘要看，作者围绕摘要中的研究对象展开分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

一个LLM路由器可以平均准确,但可以向不同的工作流派发送同等请求,或者在潜在需求发生变化时无法重新路由.由于路由决定了下一步哪个工作流程,模型或人类过程行动,因此这些边界故障会产生操作后果. 我们将版本的路由器包,即实际部署的模型和路由配置,视为政策限制部署保证的单元.保证在这里意味着符合预先规定的行为关系,证据身份和声明的部署政策的资格.它不证实生产安全性,也不估计生产普遍性或下游利益. 认证对同样的需求要求保持正确的路线,在需求发生变化时转向新目标,同时保持错误的替代方案,持久性,人类审查和显而易见的范围之外的操作.在固定,可复制的BANKING77和CLINC150队伍中,有害的正确到错误的交叉路由是稀有的,但不是零. 严格的OOS评分进一步表明,更少的强制错误路径可以反映审查升级,而不是明确的OOS识别.盲目的三注释器比较支持采样路由关系.三个预先指定的信息等级提示,保留任务内容,同时改变指令措辞和顺序,产生持久和实现依赖的行为. 使用新型供应商调用的更新重复使用1770个未受影响的决定,拒绝过时证据,重复590个受影响的决定,重建完整的血统,检测退化;多细胞重播证实了同时改变的包装中确切的重建.结果的证据支持监测,审查能力规划,范围之外的保障措施和包装版本中的部署决策.

### 英文原摘要

An LLM router can be accurate on average yet send equivalent requests to different workflows or fail to reroute when the underlying need changes. Because routing determines which workflow, model, or human process acts next, these boundary failures have operational consequences. We treat the versioned router package, meaning the model and routing configuration actually deployed, as the unit of policy-bounded deployment assurance. Assurance here means qualification against prespecified behavioral relations, evidence identity, and declared deployment policies. It does not certify production safety or estimate production prevalence or downstream benefit. Qualification couples preservation of the correct route for same-need requests with movement to a new target when the need changes, while keeping wrong alternatives, persistence, human review, and explicit out-of-scope handling visible. Across fixed, reproducible BANKING77 and CLINC150 cohorts, harmful correct-to-wrong crossings are sparse but nonzero. Strict OOS scoring further shows that fewer forced misroutes can reflect review escalation rather than explicit OOS recognition. A blinded three-annotator comparison supports the sampled routing relations. Three prespecified information-equivalent prompts, which preserve task content while varying instruction wording and order, produce both persistent and realization-dependent behavior. An update using fresh provider calls reuses 1,770 unaffected decisions, rejects stale evidence, reruns 590 affected decisions, reconstructs complete lineage, and detects degradation; a multi-cell replay confirms exact reconstruction across concurrent package changes. The resulting evidence supports monitoring, review-capacity planning, out-of-scope safeguards, and rollout decisions across package versions.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
