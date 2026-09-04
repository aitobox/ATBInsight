---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 数字孪生
- 智能体决策
- 决策图
- 可解释性
- 图神经网络
title: DNative-Twin：用于可重建智能体决策的决策图与数字孪生
---
### 文章背景与核心概要
随着AI智能体在收集证据、调用工具、应用约束以及产生决策等关键角色中扮演越来越重要的仅依赖最终输出已无法满足问责制的需求。通常很难弄清楚到底是哪些证据、工具状态、规则、授权或决策路径导致了最终结果。

为了解决这一痛点，本文引入了 **DNative-Twin**，这是一个图原生的数字孪生框架，旨在将已提交的智能体决策记录为类型化轨迹，并在声明的条件下重新执行决策机制。通过同步观察到的状态、执行路径和治理权限，该系统能够在受控修改下进行隔离重演和对比分析。

---

## 📋 Summary

随着AI智能体承担起关键角色——收集证据、调用工具、应用约束并产生决策，仅依赖最终输出已不足以保证问责制。通常很难弄清楚究竟是哪些证据、工具状态、规则、授权或决策路径导致了该结果。

> As AI agents take on critical roles—gathering evidence, invoking tools, applying constraints, and producing decisions—relying solely on a final output is insufficient for accountability. It is often unclear which evidence, tool state, rule, authorization, or decision path led to the outcome. 

本文介绍了 **DNative-Twin**，这是一个图原生的数字孪生框架，旨在将已提交的智能体决策记录为类型化轨迹，并在声明的条件下重新执行决策机制。通过同步观察到的状态、执行路径和治理权限，该系统能够在受控修改下进行隔离重演和对比分析。

> This paper introduces **DNative-Twin**, a graph-native digital twin framework designed to record committed agentic decisions as typed trajectories and re-execute decision mechanisms under declared conditions. By synchronizing observed states, execution paths, and governance authorities, the system enables isolated replays and comparative analysis under controlled modifications.

### 关键发现与方法论：
* **图结构的局限性：** 尽管图结构成功地局部化了所表示的变更，但实验表明，它们无法确定未观测工具状态的下游后果。
* **受控实验结果：** 在300个注入实例（使用公共企业流程日志）上进行测试，未解决分歧的召回率：
  * 当加入重演契约状态时，从 **0 增加到 0.667**。
  * 当同时纳入验证结果时，增加到 **1.0**。
* **性能影响：** 在500到5,000个 BPI 2020 案例中，端到端处理的中位时间从 **0.794秒增加到 8.889秒**。

> ### Key Findings & Methodology:
> * **The Limitation of Graph Structure:** While graph structures successfully localize represented changes, experiments reveal they cannot determine the downstream consequences of unobserved tool states.
> * **Controlled Experiment Results:** Tested across 300 injected instances (using public enterprise process logs), the recall for unresolved divergences:
>   * Increased from **0 to 0.667** when replay-contract state was added.
>   * Increased to **1.0** when verification results were also incorporated.
> * **Performance Impact:** Across 500 to 5,000 BPI 2020 cases, the median end-to-end processing time increased from **0.794 to 8.889 seconds**.

---

## 🔗 Links & Resources

* **全文访问：**
  * [查看 PDF](https://arxiv.org/pdf/2609.03787)
  * [HTML 版本（实验性）](https://arxiv.org/html/2609.03787v1)
  * [TeX 源码](https://arxiv.org/src/2609.03787)
* **引用与指标：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03787)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03787)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03787)
  * [DOI](https://doi.org/10.48550/arXiv.2609.03787)

> ## 🔗 Links & Resources
> 
> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2609.03787)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2609.03787v1)
>   * [TeX Source](https://arxiv.org/src/2609.03787)
> * **Citations & Metrics:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03787)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03787)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03787)
>   * [DOI](https://doi.org/10.48550/arXiv.2609.03787)