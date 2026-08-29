---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 模型上下文协议
- 事实核查
- 智能体安全
- 溯源验证
- 医疗AI
title: ProvenanceGuard：基于模型上下文协议（MCP）的大模型智能体源感知事实核查机制
---
### 文章背景与核心概要

随着使用工具的大语言模型（LLM）智能体日益依赖**模型上下文协议（MCP）**来从异构证据源（如搜索引擎、API、数据库、临床记录和处方集工具）中收集信息，一个关键的漏洞浮出水面：**跨源混淆（cross-source conflation）**。传统的事实核查方法通常只检查LLM的回答是否总体上得到汇总证据的支持，从而漏掉了某些陈述在数据集中虽然事实正确、但**归错了数据来源**的情况。

为了解决这一问题，本文作者推出了 **ProvenanceGuard**，这是一种专为MCP基础上的回答而设计的源感知核查器。通过解析捕获的MCP轨迹、将回答分解为原子级声明（atomic claims）、将这些声明路由至特定源，并对比明确的归因与经验证的原始出处，ProvenanceGuard能够提供可靠的每条声明判定（per-claim verdicts）以及回答级别的准入/拦截决策。

---

**arXiv:** [arXiv:2606.18037](https://arxiv.org/abs/2606.18037) [cs.AI]  
**Authors:** Ander Alvarez, Santhiya Rajan, Alessandro Genuardi, Oliver Wirjadi, Samuel Mugel, Román Orús  
**Submission History:** Submitted on 16 Jun 2026; last revised 27 Aug 2026 (v3).  

> **arXiv:** [arXiv:2606.18037](https://arxiv.org/abs/2606.18037) [cs.AI]  
> **Authors:** Ander Alvarez, Santhiya Rajan, Alessandro Genuardi, Oliver Wirjadi, Samuel Mugel, Román Orús  
> **Submission History:** Submitted on 16 Jun 2026; last revised 27 Aug 2026 (v3).

---

## Executive Summary

As tool-using Large Language Model (LLM) agents increasingly rely on the **Model Context Protocol (MCP)** to gather information from heterogeneous evidence sources (such as search engines, APIs, databases, clinical records, and formulary tools), a critical vulnerability emerges: **cross-source conflation**. 

Standard factuality verification methods typically check whether an LLM's answer is supported by the pooled evidence overall, missing cases where a claim is factually correct somewhere in the dataset but **attributed to the wrong source**. 

To combat this, the authors introduce **ProvenanceGuard**, a source-aware verifier designed specifically for MCP-grounded answers. By parsing captured MCP traces, decomposing answers into atomic claims, routing those claims to specific sources, and comparing stated attributions against verified origins, ProvenanceGuard provides robust per-claim verdicts and answer-level allow/block decisions.

> ## Executive Summary
> 
> As tool-using Large Language Model (LLM) agents increasingly rely on the **Model Context Protocol (MCP)** to gather information from heterogeneous evidence sources (such as search engines, APIs, databases, clinical records, and formulary tools), a critical vulnerability emerges: **cross-source conflation**. 
> 
> Standard factuality verification methods typically check whether an LLM's answer is supported by the pooled evidence overall, missing cases where a claim is factually correct somewhere in the dataset but **attributed to the wrong source**. 
> 
> To combat this, the authors introduce **ProvenanceGuard**, a source-aware verifier designed specifically for MCP-grounded answers. By parsing captured MCP traces, decomposing answers into atomic claims, routing those claims to specific sources, and comparing stated attributions against verified origins, ProvenanceGuard provides robust per-claim verdicts and answer-level allow/block decisions.

---

## Key Concepts & Methodology

* **The Problem (Cross-Source Conflation):** A failure mode where an LLM agent generates a claim supported by the broader evidence pool, but incorrectly maps it to an improper source, compromising auditability and safety (especially in high-stakes domains like healthcare).
* **ProvenanceGuard Workflow:**
  1. **Trace Ingestion:** Consumes captured MCP traces containing stable tool IDs, source IDs, and raw outputs.
  2. **Claim Decomposition:** Breaks down the generated answer into atomic, verifiable claims.
  3. **Evidence Routing:** Directs individual claims to their corresponding source-specific evidence.
  4. **Support Checking:** Evaluates factual support utilizing Natural Language Inference (NLI) and a token-alignment proxy.
  5. **Attribution Verification:** Compares the agent's stated source attribution against the actually routed source.
  6. **Action & Repair:** Emits per-claim verdicts alongside an answer-level allow/block decision. Blocked answers trigger a retrieval-augmented answer revision and re-verification loop.

> ## Key Concepts & Methodology
> 
> * **The Problem (Cross-Source Conflation):** A failure mode where an LLM agent generates a claim supported by the broader evidence pool, but incorrectly maps it to an improper source, compromising auditability and safety (especially in high-stakes domains like healthcare).
> * **ProvenanceGuard Workflow:**
>   1. **Trace Ingestion:** Consumes captured MCP traces containing stable tool IDs, source IDs, and raw outputs.
>   2. **Claim Decomposition:** Breaks down the generated answer into atomic, verifiable claims.
>   3. **Evidence Routing:** Directs individual claims to their corresponding source-specific evidence.
>   4. **Support Checking:** Evaluates factual support utilizing Natural Language Inference (NLI) and a token-alignment proxy.
>   5. **Attribution Verification:** Compares the agent's stated source attribution against the actually routed source.
>   6. **Action & Repair:** Emits per-claim verdicts alongside an answer-level allow/block decision. Blocked answers trigger a retrieval-augmented answer revision and re-verification loop.

---

## Evaluation & Results

The paper evaluates ProvenanceGuard across rigorous medical-domain benchmarks:

* **Medical Trace Dataset:** Evaluated on 281 medical-domain MCP-agent traces (featuring a 266-trace adjudicated subset yielding 2,325 LLM-assisted claim labels and 361 human-verified held-out labels).
* **Performance on Held-Out Split (40 traces / 260 source-eligible claims):** 
  * **Block F1 Score:** 0.802
  * **Source Accuracy:** 0.858  
  *(Outperforming source-blind baselines that lack claim-to-source ID tracking).*
* **Multi-Source Benchmark:** On a more complex multi-source benchmark, the block F1 reaches **0.846**, though source-plus-relation accuracy drops to **0.229**, demonstrating that exact source ownership remains challenging when dealing with semantically overlapping or close sources.
* **Repair-and-Reverify:** Successfully resolves all blocked answers in the full trace set, frequently relying on conservative fallback mechanisms.
* **Controlled Conflation Probes:** Across 50 targeted clinical conflation tests, ProvenanceGuard successfully detected **100% of injected attribution swaps**, leaving zero retained incorrect attributions.

> ## Evaluation & Results
> 
> The paper evaluates ProvenanceGuard across rigorous medical-domain benchmarks:
> 
> * **Medical Trace Dataset:** Evaluated on 281 medical-domain MCP-agent traces (featuring a 266-trace adjudicated subset yielding 2,325 LLM-assisted claim labels and 361 human-verified held-out labels).
> * **Performance on Held-Out Split (40 traces / 260 source-eligible claims):** 
>   * **Block F1 Score:** 0.802
>   * **Source Accuracy:** 0.858  
>   *(Outperforming source-blind baselines that lack claim-to-source ID tracking).*
> * **Multi-Source Benchmark:** On a more complex multi-source benchmark, the block F1 reaches **0.846**, though source-plus-relation accuracy drops to **0.229**, demonstrating that exact source ownership remains challenging when dealing with semantically overlapping or close sources.
> * **Repair-and-Reverify:** Successfully resolves all blocked answers in the full trace set, frequently relying on conservative fallback mechanisms.
> * **Controlled Conflation Probes:** Across 50 targeted clinical conflation tests, ProvenanceGuard successfully detected **100% of injected attribution swaps**, leaving zero retained incorrect attributions.

---

## Conclusion

The findings demonstrate that **source attribution is an independent and vital axis for factuality verification** in MCP-based agentic workflows. ProvenanceGuard establishes a viable paradigm for auditing, blocking, and repairing source-conflated AI generations in critical decision-making environments.

> ## Conclusion
> 
> The findings demonstrate that **source attribution is an independent and vital axis for factuality verification** in MCP-based agentic workflows. ProvenanceGuard establishes a viable paradigm for auditing, blocking, and repairing source-conflated AI generations in critical decision-making environments.

---

## Additional Resources & Links

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2606.18037) | [HTML Version](https://arxiv.org/html/2606.18037v3) | [TeX Source](https://arxiv.org/src/2606.18037)
* **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
  <a class="has_license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" title="Rights to this article">
  <img alt="license icon" role="presentation" src="./images/079cd8198ba3.png" width="80" />
  </a>
* **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.18037) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.18037) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.18037)

> ## Additional Resources & Links
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2606.18037) | [HTML Version](https://arxiv.org/html/2606.18037v3) | [TeX Source](https://arxiv.org/src/2606.18037)
> * **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
>   <a class="has_license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" title="Rights to this article">
>   <img alt="license icon" role="presentation" src="./images/079cd8198ba3.png" width="80" />
>   </a>
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.18037) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.18037) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.18037)