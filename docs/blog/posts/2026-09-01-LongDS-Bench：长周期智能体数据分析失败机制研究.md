---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 长周期智能体
- 数据分析
- 基准测试
- 状态演进
- 机器学习
title: LongDS-Bench：长周期智能体数据分析失败机制研究
---
### 文章背景与核心概要

真实世界中的数据分析本质上是一个迭代的过程，然而现有的基准测试大多集中在孤立或短期的交互任务上。这导致我们在评估人工智能智能体（AI Agent）在长周期内跟踪不断演变的分析上下文的能力时，存在着明显的评估盲区。

为了填补这一空白，作者团队推出了 **LongDS-Bench**，这是一个旨在评估长周期、多轮数据分析的新型基准测试。该基准测试全面检验了智能体在复杂工作流中维护、更新、恢复和组合不断演变的分析状态的能力。研究发现，即使是最先进的模型在长周期分析中也表现出极高的错误率，核心瓶颈在于模型无法随时间推移维持正确且连贯的分析状态，而非交互步数的限制。

---

# LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis

**Authors:** Kewei Xu, Xiaoben Lu, Shuofei Qiao, Zihan Ding, Haoming Xu, Lei Liang, Ningyu Zhang  
**Published:** ACL 2026 (arXiv:2605.30434 [cs.LG])  
**Links:** [View PDF](https://arxiv.org/pdf/2605.30434) | [HTML Version](https://arxiv.org/html/2605.30434v2) | [GitHub Repository](https://github.com/zjunlp/DataMind)

> # LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis
> 
> **Authors:** Kewei Xu, Xiaoben Lu, Shuofei Qiao, Zihan Ding, Haoming Xu, Lei Liang, Ningyu Zhang  
> **Published:** ACL 2026 (arXiv:2605.30434 [cs.LG])  
> **Links:** [View PDF](https://arxiv.org/pdf/2605.30434) | [HTML Version](https://arxiv.org/html/2605.30434v2) | [GitHub Repository](https://github.com/zjunlp/DataMind)

---

## 📌 Summary

Real-world data analysis is inherently iterative, yet existing benchmarks predominantly focus on isolated or short interactive tasks. This leaves a critical gap in evaluating an AI agent's ability to track evolving analytical contexts over extended horizons. 

To bridge this gap, the authors introduce **LongDS-Bench**, a novel benchmark designed to evaluate long-horizon, multi-turn data analysis. The benchmark tests an agent's capability to maintain, update, restore, and compose evolving analytical states across complex workflows.

> ## 📌 Summary
> 
> Real-world data analysis is inherently iterative, yet existing benchmarks predominantly focus on isolated or short interactive tasks. This leaves a critical gap in evaluating an AI agent's ability to track evolving analytical contexts over extended horizons. 
> 
> To bridge this gap, the authors introduce **LongDS-Bench**, a novel benchmark designed to evaluate long-horizon, multi-turn data analysis. The benchmark tests an agent's capability to maintain, update, restore, and compose evolving analytical states across complex workflows.

---

## 📊 Key Highlights of LongDS-Bench

* **Scale & Scope:** Comprises **68 tasks** constructed from real-world Kaggle notebooks, spanning **2,225 turns** across six distinct domains (including Geoscience, Business, and Education).
* **State-Evolution Patterns:** Built around complex analytical state changes such as counterfactual perturbations, rollbacks, and multi-state compositions, featuring an average dependency span of **11.3 turns**.
* **Performance Deficit:** Evaluations on five state-of-the-art models revealed that:
  * The top-performing model achieved a mere **48.45% average accuracy**.
  * Performance dropped by nearly **47 points** from early to late turns.
  * Long-horizon errors account for **52% to 69%** of total failures.
* **Core Bottleneck:** Further analysis indicates that simply granting additional interaction steps (interaction budget) does not inherently improve performance. Instead, the primary bottleneck is the model's ability to maintain a correct, coherent analytical state over time.

> ## 📊 Key Highlights of LongDS-Bench
> 
> * **Scale & Scope:** Comprises **68 tasks** constructed from real-world Kaggle notebooks, spanning **2,225 turns** across six distinct domains (including Geoscience, Business, and Education).
> * **State-Evolution Patterns:** Built around complex analytical state changes such as counterfactual perturbations, rollbacks, and multi-state compositions, featuring an average dependency span of **11.3 turns**.
> * **Performance Deficit:** Evaluations on five state-of-the-art models revealed that:
>   * The top-performing model achieved a mere **48.45% average accuracy**.
>   * Performance dropped by nearly **47 points** from early to late turns.
>   * Long-horizon errors account for **52% to 69%** of total failures.
> * **Core Bottleneck:** Further analysis indicates that simply granting additional interaction steps (interaction budget) does not inherently improve performance. Instead, the primary bottleneck is the model's ability to maintain a correct, coherent analytical state over time.

---

## 🗂️ Metadata & Classification

* **Primary Subject:** Machine Learning (`cs.LG`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Multiagent Systems (`cs.MA`)
* **Submission History:** 
  * *v1:* 28 May 2026
  * *v2 (Latest):* 28 August 2026

> ## 🗂️ Metadata & Classification
> 
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Multiagent Systems (`cs.MA`)
> * **Submission History:** 
>   * *v1:* 28 May 2026
>   * *v2 (Latest):* 28 August 2026