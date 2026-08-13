---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- GUI代理
- 测试时自适应
- 视觉语言模型
- 强化学习
- 移动应用
title: CoAdapt-GUI：针对未见GUI应用的联合工作流上下文与策略自适应
---
### 文章背景与核心概要
移动GUI（图形用户界面）智能体在部署到未在源训练数据中出现过的全新应用程序时，往往表现脆弱。为了解决这一泛化难题，本文提出了 **CoAdapt-GUI**，这是一个新颖的测试时自适应（TTA）框架。该框架在目标交互预算有限且无需目标示范数据的情况下，实现了对未见应用的有效泛化。

CoAdapt-GUI 通过两大核心机制运作：首先是**结构化工作流上下文自适应**，它保留可迁移的程序、失效模式和验证规则，同时剔除与源应用强绑定的细节，从而将可重用的工作流知识与源界面状态分离开来；其次是**策略自适应**，采用任务上下文匹配的群组相对优化方法，来更新构建于冻结视觉语言模型之上的 LoRA 适配器。实验结果表明，该方法在 AndroidWorld-Generalization 和 AndroidWorld Plus 评估中均取得了显著的性能提升。

---

# CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications

**arXiv ID:** [arXiv:2608.11588](https://arxiv.org/abs/2608.11588) [cs.AI]  
**Submitted:** August 12, 2026  
**Authors:** Linqiang Guo, Li Gu, Zihuan Jiang, Zhixiang Chi, Siobhan Reid, Ziqiang Wang, Yuanhao Yu, Wei Liu, Yang Wang, Tse-Hsun (Peter) Chen  

> **arXiv ID:** [arXiv:2608.11588](https://arxiv.org/abs/2608.11588) [cs.AI]  
> **Submitted:** August 12, 2026  
> **Authors:** Linqiang Guo, Li Gu, Zihuan Jiang, Zhixiang Chi, Siobhan Reid, Ziqiang Wang, Yuanhao Yu, Wei Liu, Yang Wang, Tse-Hsun (Peter) Chen  

---

## Summary

移动GUI智能体在部署到源训练中未曾出现的应用程序时经常失效。本文介绍了 **CoAdapt-GUI**，这是一种新颖的测试时自适应（TTA）框架，旨在解决在有限的目标交互预算下且不需要目标示范的泛化挑战。

CoAdapt-GUI 通过两个关键机制运行：
1. **结构化工作流上下文自适应：** 保留可迁移的程序、失败模式和验证规则，同时排除与应用绑定的源细节。这把可重用的工作流知识与源界面状态隔离开来。
2. **策略自适应：** 采用任务上下文匹配的群组相对优化，来更新构建在冻结的视觉语言模型之上的 LoRA 适配器。

### 核心结果
* **AndroidWorld-Generalization：** 成功率达到 **45.0%**（相比之下，基线“纯策略TTA”为 37.5%）。
* **AndroidWorld Plus：** 性能从 **38.6%** 提升至 **52.9%**。

> ## Summary
> 
> Mobile GUI agents often fail when deployed to unseen applications (applications absent from their source training data). This paper introduces **CoAdapt-GUI**, a novel test-time adaptation (TTA) framework designed to tackle this generalization challenge under a limited target interaction budget and without requiring target demonstrations. 
> 
> CoAdapt-GUI operates through two key mechanisms:
> 1. **Structured Workflow Context Adaptation:** Retains transferable procedures, failure modes, and verification rules while excluding app-bound source details. This separates reusable workflow knowledge from source-interface states.
> 2. **Policy Adaptation:** Employs task-context-matched group-relative optimization to update a LoRA adapter built on a frozen vision-language model.
> 
> ### Key Results
> * **AndroidWorld-Generalization:** Reaches **45.0%** success rate (compared to 37.5% for the baseline Policy-Only TTA).
> * **AndroidWorld Plus:** Raises performance from **38.6% to 52.9%**.

---

## Abstract

移动GUI智能体在部署到源训练中缺失的应用程序时，依然显得不够稳健。我们研究了在有限的目标交互预算下且无目标示范的情况下的全新应用泛化。我们推出了 CoAdapt-GUI，这是一个测试时自适应（TTA）框架，它从智能体自身的目标应用运行轨迹（rollouts）和奖励中联合自适应结构化工作流上下文和策略。工作流上下文保留了可迁移的程序、失败模式和验证规则，同时排除了应用绑定的源细节。这种分离使得可重用的工作流知识能够在不转移源界面状态的情况下指导自适应。对于策略自适应，任务上下文匹配的群组相对优化更新了冻结视觉语言模型上的 LoRA 适配器。在两个未见应用的评估中，CoAdapt-GUI 在 AndroidWorld-Generalization 上达到了 45.0%，而报告的纯策略 TTA 基线为 37.5%，并将 AndroidWorld Plus 的性能从 38.6% 提高到 52.9%。这些结果表明，转移受限的工作流上下文提供了显著的增益，并且联合策略自适应进一步提高了留出性能（held-out performance）。

> ## Abstract
> 
> Mobile GUI agents remain brittle when deployed to applications absent from source training. We study novel-app generalization under a limited target interaction budget and without target demonstrations. We introduce CoAdapt-GUI, a test-time adaptation (TTA) framework that jointly adapts structured workflow context and policy from the agent's own target-app rollouts and rewards. The workflow context retains transferable procedures, failure modes, and verification rules while excluding app-bound source details. This separation allows reusable workflow knowledge to guide adaptation without transferring source-interface state. For policy adaptation, task-context-matched group-relative optimization updates a LoRA adapter on a frozen vision-language model. Across two unseen-app evaluations, CoAdapt-GUI reaches 45.0% on AndroidWorld-Generalization, compared with 37.5% for the reported Policy-Only TTA baseline, and raises AndroidWorld Plus performance from 38.6% to 52.9%. These results show that transfer-constrained workflow context provides substantial gains and that joint policy adaptation further improves held-out performance.

---

## Paper Metadata & Links

* **学科领域：** 人工智能 (`cs.AI`)
* **DOI：** [10.48550/arXiv.2608.11588](https://doi.org/10.48550/arXiv.2608.11588)
* **全文资源：**
  * [查看 PDF](https://arxiv.org/pdf/2608.11588)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.11588v1)
  * [TeX 源码](https://arxiv.org/src/2608.11588)
  * 许可协议：[知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) ![license icon](images/345c7ad61f1b.png)
* **外部引用与工具：**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11588)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11588)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11588)

> ## Paper Metadata & Links
> 
> * **Subject:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2608.11588](https://doi.org/10.48550/arXiv.2608.11588)
> * **Full-Text Resources:**
>   * [View PDF](https://arxiv.org/pdf/2608.11588)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.11588v1)
>   * [TeX Source](https://arxiv.org/src/2608.11588)
>   * License: [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](images/345c7ad61f1b.png)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11588)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11588)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11588)