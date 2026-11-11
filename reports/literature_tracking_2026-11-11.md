# 2026-11-11 LLM 服务系统每日文献简报

> 检索窗口：2026-11-10 至 2026-11-11（北京时间 / Asia/Shanghai）；本期确认 3 篇，其中直接 LLM 服务研究 3 篇、机制桥接 0 篇。

## Executive Summary

本报告用于快速筛选：每篇论文先用一两句话概括研究内容，再附完整中文摘要翻译和英文原摘要。模型、公式和完整结论留到后续精读。

## 1. 法学士竞争和集成经济

> 英文原标题：LLM Competition and the Aggregator Economy

- **作者：** Fupeng Sun、Zhe Liu、Wolfram Wiesemann
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-10；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 15
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7683780) · [DOI](https://doi.org/10.2139/ssrn.7683780)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、llm、pricing、subscription。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大语言模型 (LLM) 聚合器,如Poe和ChatHub,销售单个订阅,允许用户访问竞争性供应商的模型,利用供应商在任务之间水平差异化和垂直差异化性能. 对于OpenAI和Anthropic等LLM提供商来说,集成器同时是补充和竞争对手:它产生批发API收入,但它食用直接零售订阅. 我们开发了一个游戏理论框架,其中两个LLM提供商,每一个在两个特征中更强大, 服务于具有异质特征偏好的用户, 我们表明,集成器以平衡的偏好为用户提供服务,其对供应商的影响取决于市场覆盖率:在不飽和市场上,它主要扩大覆盖率,但仍然可以通过订阅食减少供应商收入,而在飽和市场上,它只会重新分配现有订户,并且只会使供应商受益,如果其API价格足够高. 聚合器也改变了创新激励措施:提高供应商强大特征可能会从竞争对手那里夺走市场份额,但扩大聚合器的用户群,并且可以增加供应商的收入而不增加直接订阅者,同时改善其弱特征可以让用户从聚合器中回来,同时保持竞争对手的市场份额不变. 最后,当用户使用强度不同时,基于使用的聚合器级别使一次性直接订阅对重量用户相对更有吸引力,反映了实践中观察到的级别定价和使用上限.

### 英文原摘要

Large Language Model (LLM) aggregators, such as Poe and ChatHub, sell a single subscription that gives users access to the models of competing providers, exploiting the providers' horizontal differentiation across tasks and vertical differentiation in performance. For LLM providers such as OpenAI and Anthropic, an aggregator is simultaneously a complement and a competitor: it generates wholesale API revenue, but it cannibalizes direct retail subscriptions. We develop a game-theoretic framework in which two LLM providers, each stronger in one of two features, serve users with heterogeneous feature preferences who choose between subscribing directly, subscribing to the aggregator, or opting out. We show that the aggregator serves users with balanced preferences, and that its impact on providers depends on market coverage: in unsaturated markets it primarily expands coverage but can still reduce provider revenues through subscription cannibalization, whereas in saturated markets it only reallocates existing subscribers and benefits a provider only if its API price is sufficiently high. The aggregator also changes innovation incentives: improving a provider's strong feature may steal market share from its rival but enlarges the aggregator's user base, and it can raise the provider's revenue without adding direct subscribers, while improving its weak feature can win users back from the aggregator while keeping the rival's market share unchanged. Finally, when users differ in usage intensity, usage-based aggregator tiers make flat-fee direct subscriptions relatively more attractive to heavy users, reflecting the tiered pricing and usage caps observed in practice.

## 2. 大型语言模型服务的最佳缓存时间和价格

> 英文原标题：Optimal Cache Duration and Pricing for Large Language Model Serving

- **作者：** Zhuyu Liu、Meichun Lin、Woonghee Tim Huh
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-10；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 10
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7682318) · [DOI](https://doi.org/10.2139/ssrn.7682318)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、language model serving、pricing、optimization。从摘要看，作者提出并评估一种新方法或系统；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

大型语言模型系统在请求到来之间保留对话的关键值缓存,以避免重新计算对话历史.选择缓存时间需要与使用稀缺的GPU内存的重新计算成本平衡.我们开发了一种 stochastic优化框架,将缓存时间视为操作控制和定价服务属性. 我们首先以闭式形式推出一个单次对话的独特成本最小化持续时间.对于多次对话共享内存,我们描述了基于操作成本的稳定状态缓存使用情况,并显示成本最小化持续时间仍然是独特的. 由于最佳持续时间取决于完整的稳定状态分布,因此我们开发了一个基于平均的替代方案,并证明,随着对话到达率和内存容量比例上升,它是不符号的最佳的.我们还研究了付费的持续时间延长,而不仅仅是免费默认. 在单次交谈模式和多次交谈替代模式中,我们确定了可以根据价格优化付费时间的条件.我们进一步表明,最大化利的默认时间从来不超过相应的成本最小化时间,从而显示了限制免费服务的激励,以增加用户对延期付费的意愿.

### 英文原摘要

Large language model systems retain a conversation's key-value cache between request arrivals to avoid recomputing the conversation history. Choosing the cache duration requires balancing recomputation costs against the use of scarce GPU memory. We develop a stochastic optimization framework that treats cache duration as both an operational control and a priced service attribute. We first derive the unique cost-minimizing duration in closed form for a single conversation. For multiple conversations sharing memory, we characterize the steady-state cache usage underlying the operating cost and show that the cost-minimizing duration remains unique. Since the optimal duration depends on the full steady-state distribution, we develop a mean-based surrogate with a closed-form solution and prove that it is asymptotically optimal as the conversation arrival rate and memory capacity scale up proportionally. We also study paid duration extensions beyond a free default. In the single-conversation model and the multiple-conversation surrogate, we identify conditions under which the paid duration can be optimized independently of the price. We further show that the profit-maximizing default duration never exceeds the corresponding cost-minimizing duration, revealing an incentive to limit free service to increase users' willingness to pay for the extension.

## 3. 资产价格的大型语言模型:文献评论

> 英文原标题：Large Language Models in Asset Pricing: A Literature Review

- **作者：** Mohammad Gheidi
- **来源/日期：** SSRN working paper；首次发布 2026；最近更新 2026-11-10；SSRN/Crossref
- **分类：** Token 定价、订阅与额度套餐；直接 LLM 服务研究；相关性评分 9
- **链接：** [论文页](https://doi.org/10.2139/ssrn.7683739) · [DOI](https://doi.org/10.2139/ssrn.7683739)

### 一两句话看懂

这篇论文关注“Token 定价、订阅与额度套餐”，重点涉及 large language model、large language models、llm、pricing。从摘要看，作者使用数据开展实证分析；下方附有数据源提供的完整原始摘要，可直接核对研究内容。

### 中文摘要（翻译）

该文献审查审查了资产定价中的大语言模型 (LLM) 的使用.主要重点是基于文本的应用,其中LLM将资产文本,如新闻,收益调用,企业披露,基金报告,宏观经济通信和气候相关的叙述转化为与回报,风险,基础和投资者信仰相关的定量信号. 这项审查首先将LLM放在金融方面的文本分析的更长历史和实验性资产定价领域人工智能和机器学习的更广泛发展中. 然后审查资产定价的主要LLM应用,包括基于新闻的回报预测,收益调用和披露,企业政策,ESG和气候风险,基金经理的信念,债券,期权,外汇和新兴的LLM代理系统. 该审查还讨论了前景偏见,培训数据泄露,快速敏感性,模型不稳定性,有限的可解释性,交易成本以及实际的样本外评估的必要性等局限性.

### 英文原摘要

This literature review examines the use of large language models (LLMs) in asset pricing. The main focus is on text-based applications, where LLMs transform financial text such as news, earnings calls, corporate disclosures, fund reports, macroeconomic communication, and climate-related narratives into quantitative signals related to returns, risk, fundamentals, and investor beliefs. The review first places LLMs within the longer history of text analysis in finance and the broader development of artificial intelligence and machine learning in empirical asset pricing. It then reviews the main LLM applications in asset pricing, including news-based return prediction, earnings calls and disclosures, corporate policies, ESG and climate risk, fund-manager beliefs, bonds, options, foreign exchange, and emerging LLM-agent systems. The review also discusses limitations such as look-ahead bias, training-data leakage, prompt sensitivity, model instability, limited interpretability, transaction costs, and the need for realistic out-of-sample evaluation. Finally, the review discusses research gaps and future directions for using LLMs in asset pricing.

## 阅读说明

- 中文概括仅依据数据源摘要，用于快速判断是否值得精读，不代表完成全文核验。
- 每篇先展示忠实的中文摘要翻译，再完整保留英文原摘要；如果数据源没有摘要，会明确说明。
- 同题名、同 DOI 的预印本与期刊版本会合并；首次发布日期与最近更新日期分开显示。
- 机制桥接条目不是直接研究 LLM，而是可迁移到 LLM 服务系统的高质量模型论文。
