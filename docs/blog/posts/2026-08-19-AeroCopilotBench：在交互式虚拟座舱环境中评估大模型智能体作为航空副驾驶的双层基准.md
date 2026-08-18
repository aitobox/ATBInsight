---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 大模型智能体
- 航空航天
- 基准测试
- 虚拟座舱
- 具身智能
title: AeroCopilotBench：在交互式虚拟座舱环境中评估大模型智能体作为航空副驾驶的双层基准
---
### 文章背景与核心概要

随着大语言模型（LLM）智能体越来越多地被考虑用于协助机组人员进行复杂决策，当前完全依赖静态知识的评估方法已无法满足测试实时程序执行和安全合规性的要求。为了弥补这一空白，研究人员推出了AeroCopilotOperational Environment（ACOE）——一个可复现的交互式虚拟座舱测试环境，能将自然语言程序转换为可执行的状态转换、最终状态目标条件以及严格的安全约束。

此外，本文还提出了AeroCopilotBench，这是一个严苛的双层航空智能体评估基准。该基准包含评估基础航空知识的Tier-1（1200道多项选择题），以及在ACOE中评估来自制造商《飞行员操作手册》（POH）的73个紧急和异常任务实际执行情况的Tier-2。实验结果显示，在测试的12个模型中，Tier-2的最高成功率仅为72.6%，这凸显出强大的静态知识并不能可靠地转化为成功的程序执行。

---

# AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment

> **arXiv:** [2608.16349](https://arxiv.org/abs/2608.16349) [cs.AI]  
> **Submitted:** August 17, 2026  
> **Authors:** Yuchen Yuan, Zhenghuang Wu, Yuangan Li, Liang Ma, Ke Li  

---

## 📌 Summary

> As Large Language Model (LLM) agents are increasingly considered for assisting flight crews with complex decisions, current evaluation methods relying purely on static knowledge fall short of testing real-time procedural execution and safety compliance. 

> To bridge this gap, the researchers introduce:
> 1. **AeroCopilot Operational Environment (ACOE):** A reproducible, interactive virtual-cockpit test environment that converts natural-language procedures into executable state transitions, final-state goal conditions, and strict safety constraints.
> 2. **AeroCopilotBench:** A rigorous two-tier aviation agent evaluation benchmark comprising:
>    - **Tier-1:** Evaluates foundational aviation knowledge using 1,200 multiple-choice questions.
>    - **Tier-2:** Evaluates practical execution across 73 emergency and abnormal tasks sourced from manufacturers' Pilot's Operating Handbooks (POHs) within ACOE.

> ### Key Findings
> * Across 12 tested models, the highest Tier-2 success rate achieved was **72.6%**, highlighting that strong static knowledge does not reliably translate into successful procedural execution.
> * An analysis of 451 failed episodes across 3 representative models revealed recurring issues in procedural completeness, state feedback utilization, and long-horizon execution management.
> * The findings advocate for state-aware agent orchestration, separate assessments of task completion and trajectory safety, and rigorous iterative regression testing.

---

## 📋 Document Metadata

> | Metadata Field | Detail |
> | :--- | :--- |
> | **Primary Subject** | Artificial Intelligence (`cs.AI`) |
> | **Cite As** | `arXiv:2608.16349 [cs.AI]` |
> | **Document Specs** | 38 pages, 7 figures, 6 tables |
> | **DOI** | [10.48550/arXiv.2608.16349](https://doi.org/10.48550/arXiv.2608.16349) |

---

## 🔗 Full-Text & Resource Links

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.16349)
> * **HTML Version:** [HTML (experimental)](https://arxiv.org/html/2608.16349v1)
> * **TeX Source:** [Source Archive](https://arxiv.org/src/2608.16349)
> * **License:** [Non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)