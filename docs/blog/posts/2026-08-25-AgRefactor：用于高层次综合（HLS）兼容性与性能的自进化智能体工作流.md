---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- HLS
- 高层次综合
- 大语言模型
- 多智能体
- 硬件加速
title: AgRefactor：用于高层次综合（HLS）兼容性与性能的自进化智能体工作流
---
### 文章背景与核心概要
高层次综合（HLS）技术能够加速从概念软件到功能硅片的转化。然而，将标准软件编程实践桥接到硬件设计中，同时克服语言支持的限制，依然是硬件加速领域的一大痛点。现有的自动化和基于大语言模型的重构方法往往缺乏灵活性、难以扩展且计算成本高昂。

本文介绍了 **AgRefactor**，这是一个全自动、开源的基于大语言模型的多智能体框架，旨在将复杂软件无缝重构为符合 HLS 规范的程序。该框架的核心创新包括一个能够在不同任务间动态积累和检索知识的**自进化记忆系统**，以及一个结合了自动化重构工具与大语言模型驱动重写的**混合重构策略**。在更长、更复杂的真实世界基准测试中，AgRefactor 展现出了卓越的性能和普适性。

---

# AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance

**Authors:** Yang Zou, Zijian Ding, Yizhou Sun, Jason Cong  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**Secondary Subject:** Hardware Architecture (`cs.AR`)  
**arXiv Identifier:** [arXiv:2606.30949 [cs.AI]](https://arxiv.org/abs/2606.30949)  
**Dates:** Submitted on June 29, 2026; Last revised August 20, 2026 (v2)  

> **Authors:** Yang Zou, Zijian Ding, Yizhou Sun, Jason Cong  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **Secondary Subject:** Hardware Architecture (`cs.AR`)  
> **arXiv Identifier:** [arXiv:2606.30949 [cs.AI]](https://arxiv.org/abs/2606.30949)  
> **Dates:** Submitted on June 29, 2026; Last revised August 20, 2026 (v2)  

---

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>

> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>

## Summary
High-Level Synthesis (HLS) accelerates the transition from conceptual software to functional silicon. However, bridging the gap between standard software and hardware programming practices—while navigating restrictive language support—remains a major hurdle. 

**AgRefactor** is a fully-automated, open-source multi-agent LLM framework designed to seamlessly refactor complex software into HLS-compatible programs. Key innovations include:
* **Self-Evolving Memory System:** Dynamically accumulates and retrieves both factual and strategic knowledge across disparate tasks to boost efficiency and robustness on unseen programs.
* **Hybrid Refactoring Strategy:** Combines automated refactoring tools with LLM-driven rewrites to scale effectively while reducing computational costs.
* **Superior Performance:** Outperforms or matches state-of-the-art automated refactoring tools and LLM baselines on 9 out of 11 challenging real-world benchmarks (which are 5–10× longer than prior work's most complex cases). Furthermore, agentic pragma tuning delivers a **6.51× geometric mean speedup** over existing SoTA tools and a **1.20× speedup** over optimized open-source designs using less than 20% extra resources.

> 高层次综合（HLS）加速了从概念软件向功能硅片的过渡。然而，在克服严格的语言支持限制的同时，弥合标准软件与硬件编程实践之间的鸿沟仍然是一大障碍。
> 
> **AgRefactor** 是一个全自动、开源的多智能体大语言模型（LLM）框架，旨在将复杂软件无缝重构为与 HLS 兼容的程序。其核心创新包括：
> * **自进化记忆系统（Self-Evolving Memory System）：** 在不同任务之间动态积累和检索事实性与策略性知识，从而提高对未见程序的处理效率和鲁棒性。
> * **混合重构策略（Hybrid Refactoring Strategy）：** 将自动化重构工具与 LLM 驱动的代码重写相结合，在有效降低计算成本的同时实现可扩展性。
> * **卓越的性能（Superior Performance）：** 在 11 个具有挑战性的现实世界基准测试中的 9 个上，其性能超越或匹配了最先进（SoTA）的自动化重构工具以及 LLM 基线（这些基准测试比以往工作的最复杂案例长 5-10 倍）。此外，智能体化编译制导指令（pragma）调优与现有 SoTA 工具相比，实现了 **6.51 倍的几何平均加速比**，与优化后的开源设计相比实现了 **1.20 倍的加速比**，且额外资源消耗不到 20%。

---

## Abstract
> High-Level Synthesis (HLS) provides a fast path from concepts to silicon, but converting real-world software into synthesizable HLS code remains challenging due to restrictive language support and the gap between software and hardware programming practices. Existing automated and LLM-based refactoring approaches partially address this problem, yet they often lack flexibility, struggle to scale, and incur high computational costs. We introduce AgRefactor, an LLM-based multi-agent workflow for refactoring software into HLS-compatible programs. AgRefactor incorporates a self-evolving memory system that accumulates and retrieves factual and strategic knowledge across tasks, improving robustness and efficiency on unseen programs. To reduce cost and enhance scalability, it integrates automated refactoring tools, enabling agents to balance LLM-driven rewrites with efficient tool-based transformations. On 9 out of 11 challenging real-world benchmarks, which are 5-10x longer than the most complex cases studied in prior work, AgRefactor outperforms or matches the state-of-the-art automated refactoring tool and a strong LLM-based baseline built on the same framework backbone. Further agentic performance optimization yields a 6.51x geometric mean speedup over the SoTA pragma tuning tool and a 1.20x speedup over optimized open-source designs with less than 20% extra resources. AgRefactor is fully-automated and open-sourced.

> 高层次综合（HLS）为从概念到硅片提供了一条快速通道，但由于语言支持受限以及软件与硬件编程实践之间的差距，将真实世界的软件转换为可综合的 HLS 代码依然充满挑战。现有的自动化和基于 LLM 的重构方法部分解决了这个问题，但它们往往缺乏灵活性、难以扩展且产生高昂的计算成本。我们引入了 AgRefactor，这是一个基于 LLM 的多智能体工作流，用于将软件重构为兼容 HLS 的程序。AgRefactor 包含一个自进化记忆系统，能够在任务间积累和检索事实与策略知识，从而提高对未见程序的鲁棒性和效率。为了降低成本并增强可扩展性，它集成了自动化重构工具，使智能体能够平衡 LLM 驱动的代码重写与高效的基于工具的变换。在 11 个具有挑战性的现实世界基准测试（比以往工作研究的最复杂案例长 5-10 倍）中的 9 个上，AgRefactor 的表现超越或追平了最先进的自动化重构工具以及构建于相同框架骨干之上的强大 LLM 基线。进一步的智能体性能优化在消耗不到 20% 额外资源的情况下，比 SoTA pragma 调优工具取得了 6.51 倍的几何平均加速比，并比优化的开源设计取得了 1.20 倍的加速比。AgRefactor 是全自动且开源的。

---

## Submission History
* **[v1]** Mon, 29 Jun 2026, 22:02:34 UTC (774 KB)
* **[v2]** Thu, 20 Aug 2026, 22:38:09 UTC (774 KB) — *This version*

> * **[v1]** Mon, 29 Jun 2026, 22:02:34 UTC (774 KB)
> * **[v2]** Thu, 20 Aug 2026, 22:38:09 UTC (774 KB) — *This version*

---

## Access & Resources
* **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2606.30949) | [HTML (Experimental)](https://arxiv.org/html/2606.30949v2) | [TeX Source](https://arxiv.org/src/2606.30949)
* **External Indices:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.30949) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.30949) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.30949)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2606.30949) | [HTML (Experimental)](https://arxiv.org/html/2606.30949v2) | [TeX Source](https://arxiv.org/src/2606.30949)
> * **External Indices:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.30949) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.30949) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.30949)