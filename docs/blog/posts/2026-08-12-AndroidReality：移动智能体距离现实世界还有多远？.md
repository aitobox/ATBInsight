---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- AndroidReality
- 移动智能体
- 模型鲁棒性
- 强化学习
- 测试时恢复
title: AndroidReality：移动智能体距离现实世界还有多远？
---
### 文章背景与核心概要

当前，尽管移动智能体在诸如 *AndroidWorld* 等高度理想化的在线基准测试中表现优异，但在面对现实世界的环境波动和不完美的真实用户界面（UI）时，其可靠性往往会出现断崖式下跌。为了系统性评估并增强智能体的鲁棒性，本文推出了 **AndroidReality** 这一基于扰动的评估框架。

研究团队通过马尔可夫决策过程（MDP）的视角对界面变异性进行深入分析，将扰动精准归纳为三个核心维度：**状态（state）**、**转移（transition）**和**动作（action）**。基于这一分类体系，他们在 AndroidWorld 的基础上构建了一个增强型移动端基准测试。研究结果揭露了当前智能体在鲁棒性上的重大漏洞，总结出四类高频出现的错误模式，并提出了一种无需训练的**测试时内省恢复（TTIR）**机制，该机制在洁净环境与受到干扰的现实场景中均能有效缓解此类失效问题。

---

# AndroidReality: How Far Are Mobile Agents from the Real World?

**Authors:** Xiaoou Liu, Longchao Da, Hanyang Chen, Yuan Ling, Hua Wei  
**Published:** August 7, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**ArXiv ID:** [arXiv:2608.07775](https://arxiv.org/abs/2608.07775)  
**DOI:** [10.48550/arXiv.2608.07775](https://doi.org/10.48550/arXiv.2608.07775)  

---

## 📌 Summary

> While mobile agents perform exceptionally well on pristine online benchmarks like *AndroidWorld*, their reliability plummets in real-world deployments due to environmental fluctuations and imperfect user interfaces. This paper introduces **AndroidReality**, a perturbation-based framework designed to evaluate and enhance agent robustness. 
> 
> By analyzing interface variability through a Markov Decision Process (MDP) lens, the authors categorize perturbations into three primary axes: **state**, **transition**, and **action**. Using this taxonomy, they developed a perturbed mobile benchmark built upon AndroidWorld. Their findings reveal major robustness gaps, highlight four recurring error categories, and introduce a training-free **Test-Time Introspective Recovery (TTIR)** mechanism that successfully mitigates these failures across both clean and perturbed settings.

---

## 🔍 Key Contributions

1. **原则性扰动分类体系：** 通过结构化的基于 MDP 的框架，将现实世界的界面变异性整理为三个维度：
   * *状态* 扰动
   * *转移* 扰动
   * *动作* 扰动
2. **AndroidReality 基准测试：** 一个构建于 AndroidWorld 之上的可控、基于扰动的压力测试框架，旨在暴露移动智能体中潜伏的脆弱性。
3. **失效模式识别：** 揭示了巨大的鲁棒性差距，并指出了四类独特且重复出现的智能体错误。
4. **测试时内省恢复（TTIR）：** 提出了一种简单且无需训练的恢复机制，能够有效解决现实扰动环境以及洁净基准测试中的故障。

> 1. **Principled Perturbation Taxonomy:** Organizes real-world interface variability into a structured MDP-based framework across three axes:
>    * *State* perturbations
>    * *Transition* perturbations
>    * *Action* perturbations
> 2. **AndroidReality Benchmark:** A controllable, perturbation-based stress-testing framework built on top of AndroidWorld to expose latent vulnerabilities in mobile agents.
> 3. **Identification of Failure Modes:** Uncovers substantial robustness gaps and highlights four distinct, recurring categories of agent errors.
> 4. **Test-Time Introspective Recovery (TTIR):** Proposes a simple, training-free recovery mechanism that effectively resolves failures in both realistic perturbed environments and clean benchmarks.

---

## 🔗 Links & Resources

* **阅读论文：** [查看 PDF](https://arxiv.org/pdf/2608.07775) | [HTML 版本](https://arxiv.org/html/2608.07775v1)
* **引用与工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07775) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07775)

> * **Read the Paper:** [View PDF](https://arxiv.org/pdf/2608.07775) | [HTML Version](https://arxiv.org/html/2608.07775v1)
> * **Citations & Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07775) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07775)