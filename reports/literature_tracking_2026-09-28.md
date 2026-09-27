# 2026-09-28 LLM 服务系统每日文献简报

> 检索窗口：2026-09-27 至 2026-09-28（北京时间 / Asia/Shanghai）；本期确认 1 篇，其中直接 LLM 服务研究 1 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. ACAT-TP:在验证的微仿真沙箱中,监控运输信号优先级和动态公交车道的警卫机械环境意识控制

> 英文原标题：ACAT-TP: Guarded agentic context-aware control of transit signal priority and dynamic bus lanes in a validated microsimulation sandbox

- **作者：** Md. Shadman Sakib Chowdhury、Md. Mizanur Rahman
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-09-27；SSRN/Crossref
- **分类：** 优先权、SLO 与差异化服务；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7533335) · [DOI](https://doi.org/10.2139/ssrn.7533335)

### 一两句话看懂

这篇论文关注“优先权、SLO 与差异化服务”，重点涉及 large language model、llm、priority。从摘要看，作者通过实验、仿真或系统测试进行评估；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

交通信号优先 (TSP) 和动态公交车道 (DBL) 可以通过拥挤的走廊移动更多的人, 本研究介绍了Agentic Context-Aware Traffic Controller (ACAT),一个大型语言模型 (LLM) 激活预先编码的控制操作,但从未编写信号时间,并评估其运输优先级实例ACAT-TP. 每10秒钟,LLM阅读一个结构化的文本快照,并切换了十二条路线旗 (TSP和DBL为六条公共汽车路线);一个故障关闭的警卫,路线锁和确定性控制器门绑定每个行动.ACAT-TP运行在两个交叉城市走廊的专用,基于标的微模拟器中,根据HCM,ITE,TCQSM和FHWA实践进行验证,并与SUMO的行为合同进行交叉检查. 8个工作的LLM,使用零射击 (六个当地模型38亿参数,两个云模型),与协调的韦伯斯特控制,一个条件规则和乘客压力测试在0.85的度下进行了比较. 每个LLM在所有15个对联运行中减少了乘客延迟,每乘客4.513.6%;公交车乘客延迟下降了1454%,车乘客没有显著变化.基于规则的比较器增加了8.7%的延迟,压力测量也减少了2.5%.最好的手臂是本地8亿参数模型,因此不需要细节调整. 缓慢推理模型获得了最少的收益,而每次通话都失败的云模型都完全复制了基线:保卫的失败降低到基线,从来没有低于基线.

### 英文原摘要

Transit signal priority (TSP) and dynamic bus lanes (DBL) can move more people through a congested corridor, but deciding when to activate them is a passenger-weighted trade-off that fixed rules handle poorly. This study introduces the Agentic Context-Aware Traffic Controller (ACAT), a framework in which a large language model (LLM) activates pre-coded control actions but never writes signal timings, and evaluates its transit-priority instance, ACAT-TP. Every 10 s the LLM reads a structured text snapshot and switches twelve route flags (TSP and DBL for six bus routes); a fail-closed guard, a route lock and deterministic controller gates bound every action. ACAT-TP runs in a purpose-built, tick-based microsimulator of a two-intersection urban corridor, verified against HCM, ITE, TCQSM and FHWA practice and cross-checked against SUMO's behavioural contracts. Eight working LLMs, used zero-shot (six local models of 3–8 billion parameters, two cloud models), were compared with coordinated Webster control, a conditional rule and a passenger-pressure heuristic under common random numbers at a degree of saturation of 0.85. Every LLM reduced in-network passenger delay in all 15 paired runs, by 4.5–13.6% per passenger; bus-passenger delay fell 14–54% with no significant change for car occupants. The rule-based comparator increased delay by 8.7% and the pressure heuristic reduced it by 2.5%, neither significantly. The best arm was a local 8-billion-parameter model, so fine-tuning was not required. Slow reasoning models gained least, and a cloud model that failed on every call reproduced the baseline exactly: guarded failures degrade to the baseline, never below it.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
