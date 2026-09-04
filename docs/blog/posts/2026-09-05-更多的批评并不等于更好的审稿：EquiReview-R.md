---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- AI审稿
- 大语言模型
- 同行评审
- 证据引导
- EquiReview-R
title: 更多的批评并不等于更好的审稿：EquiReview-R
---
### 文章背景与核心概要
当前的AI审稿人能够生成大量具体的批评意见，但数量并不等同于质量。AI辅助审稿往往面临两种截然相反的失效模式：**遗漏**（未能指出重大的实质性弱点）和**过度批评**（保留了缺乏支持的指责）。传统的生成式系统和聚合指标无法有效区分或纠正这两种截然相反的问题。

为了解决这一痛点，本文作者将AI辅助同行评审重新定义为“结构化关注点的证据引导式精炼”（evidence-guided refinement of a structured concern set），并将遗漏与过度批评视为两类不同的风险。他们推出了 **EquiReview-R** 系统，该系统能够：1. 针对局部证据对现有关注点进行检验；2. 从独立和受审稿条件约束的双重视角搜寻遗漏的问题；3. 动态返回**停止（stop）**、**继续（continue）**或**推迟（defer）**的决策。实验表明，该系统在减少过度批评的同时有效控制了遗漏率，为未来的审稿修正研究奠定了重要基础。

---

# More Criticism Does Not Make a Better Review: EquiReview-R

**arXiv:** [arXiv:2609.03943 [cs.AI]](https://arxiv.org/abs/2609.03943)  
**Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
**Submitted:** September 3, 2026  
**Authors:** Zexing Zhang, Jichao Li, Tianyang Lei, Yude Fu, Yang Kewei  

> **arXiv:** [arXiv:2609.03943 [cs.AI]](https://arxiv.org/abs/2609.03943)  
> **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
> **Submitted:** September 3, 2026  
> **Authors:** Zexing Zhang, Jichao Li, Tianyang Lei, Yude Fu, Yang Kewei  

---

## 📋 Summary

Current AI reviewers are capable of generating numerous specific criticisms, but quantity does not equate to quality. AI-assisted reviews often suffer from two contrasting failures: **omissions** (missing consequential weaknesses) and **overcritiques** (retaining unsupported allegations). Traditional generation-oriented systems and aggregate metrics fail to distinguish or properly correct these opposing issues. 

To address this, the authors recast AI-assisted peer review as **evidence-guided refinement of a structured concern set**, treating omission and overcritique as distinct risks. They introduce **EquiReview-R**, a system that:
1. Resolves existing concerns against localized evidence.
2. Searches for missing issues from both independent and review-conditioned perspectives.
3. Dynamically returns a decision of **stop**, **continue**, or **defer**.

### Key Results
* **Reduced Overcritique:** Successfully reduced major overcritiques from 15.5% down to 8.1% on a frozen cohort of previously unseen papers.
* **Controlled Omission:** Satisfied the prespecified non-inferiority criterion for major omissions, attaining a one-sided omission upper bound of 9.9% while prematurely stopping on 52.4% of papers.
* **Core Insight:** Controlled comparisons and ablations demonstrate that performance gains originate from *systematic revision* rather than extra inference steps or simply shorter outputs.
* **ReviewTrace:** The authors release an evidence-linked trajectory corpus called *ReviewTrace* to facilitate future research on review revision, disagreement, and provenance.

> ## 📋 Summary
> 
> Current AI reviewers are capable of generating numerous specific criticisms, but quantity does not equate to quality. AI-assisted reviews often suffer from two contrasting failures: **omissions** (missing consequential weaknesses) and **overcritiques** (retaining unsupported allegations). Traditional generation-oriented systems and aggregate metrics fail to distinguish or properly correct these opposing issues. 
> 
> To address this, the authors recast AI-assisted peer review as **evidence-guided refinement of a structured concern set**, treating omission and overcritique as distinct risks. They introduce **EquiReview-R**, a system that:
> 1. Resolves existing concerns against localized evidence.
> 2. Searches for missing issues from both independent and review-conditioned perspectives.
> 3. Dynamically returns a decision of **stop**, **continue**, or **defer**.
> 
> ### Key Results
> * **Reduced Overcritique:** Successfully reduced major overcritiques from 15.5% down to 8.1% on a frozen cohort of previously unseen papers.
> * **Controlled Omission:** Satisfied the prespecified non-inferiority criterion for major omissions, attaining a one-sided omission upper bound of 9.9% while prematurely stopping on 52.4% of papers.
> * **Core Insight:** Controlled comparisons and ablations demonstrate that performance gains originate from *systematic revision* rather than extra inference steps or simply shorter outputs.
> * **ReviewTrace:** The authors release an evidence-linked trajectory corpus called *ReviewTrace* to facilitate future research on review revision, disagreement, and provenance.

---

## 🔗 Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.03943) | [HTML (Experimental)](https://arxiv.org/html/2609.03943v1) | [TeX Source](https://arxiv.org/src/2609.03943)
* **DOI:** [10.48550/arXiv.2609.03943](https://doi.org/10.48550/arXiv.2609.03943)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="height: 1em; vertical-align: middle; display: inline-block; margin-left: 4px;" />

> ## 🔗 Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.03943) | [HTML (Experimental)](https://arxiv.org/html/2609.03943v1) | [TeX Source](https://arxiv.org/src/2609.03943)
> * **DOI:** [10.48550/arXiv.2609.03943](https://doi.org/10.48550/arXiv.2609.03943)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="height: 1em; vertical-align: middle; display: inline-block; margin-left: 4px;" />