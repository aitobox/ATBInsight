---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- POMDP
- 机器人学
- 在线规划
- Rao-Blackwellized
- 不确定性处理
title: 高维POMDP的可扩展Rao-Blackwellized在线规划
---
### 文章背景与核心概要
在具有高维状态空间的部分可观测环境中运行的机器人系统，在面对不确定性时进行在线规划极具挑战性。虽然基于采样的POMDP求解器允许在大规模或连续域中进行近似决策，但由于蒙特卡洛估计的高方差，其性能会随着信念空间维度的增加而下降。

本文扩展了 Rao-Blackwellized 在线 POMDP（RB-POMDP）框架，通过混合的连续-高维离散信念表示，提高了其在高维环境中的可扩展性和通用性。通过在基于树的规划过程中解析地传播边缘化状态分量的方差，该方法降低了价值估计中由采样引起的方差。将其与 FastSLAM 2.0 相结合并在机器人搜救任务中进行测试，所提出的规划器以显著少于纯采样方法的粒子数和模拟次数，实现了更高的累积奖励。

---

# Scalable Rao-Blackwellized Online Planning for High-Dimensional POMDPs

## Summary
Online planning under uncertainty is exceptionally challenging for robotic systems operating in partially observable environments with high-dimensional state spaces. While sampling-based POMDP solvers allow for approximate decision-making in large or continuous domains, their performance degrades as belief dimensionality increases due to the high variance of Monte Carlo estimation. 

This paper extends the **Rao-Blackwellized online POMDP (RB-POMDP)** framework to improve scalability and generalizability in high-dimensional settings using hybrid continuous-discrete belief representations. By analytically propagating the uncertainty of marginalized state components during tree-based planning, the approach reduces sampling-induced variance in value estimation. Integrated with FastSLAM 2.0 and tested on a robotic search-and-rescue task, the proposed planner achieves higher cumulative rewards with significantly fewer particles and simulations than purely sampling-based methods.

> 在具有高维状态空间的部分可观测环境中运行的机器人系统，在面对不确定性时进行在线规划极具挑战性。虽然基于采样的POMDP求解器允许在大规模或连续域中进行近似决策，但由于蒙特卡洛估计的高方差，其性能会随着信念维度的高企而下降。
> 
> 本文扩展了 **Rao-Blackwellized 在线 POMDP (RB-POMDP)** 框架，利用混合的连续-离散信念表示来提升高维设置下的可扩展性与泛化能力。通过在基于树的规划过程中解析地传播边缘化状态分量的不确定性，该方法降低了价值估计中因采样引起的方差。通过将其与 FastSLAM 2.0 相集成并在机器人搜救任务中进行测试，所提出的规划器相比纯基于采样的方法，仅需显著更少的粒子和模拟次数即可获得更高的累积奖励。

---

## Document Metadata

| Metadata Field | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2609.01351](https://arxiv.org/abs/2609.01351) [cs.RO] |
| **Primary Subject** | Robotics (`cs.RO`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **Submission Date** | September 1, 2026 |
| **Authors** | Jiho Lee, Nisar Ahmed, Kyle Hollins Wray, Zachary Sunberg |
| **DOI** | [10.48550/arXiv.2609.01351](https://doi.org/10.48550/arXiv.2609.01351) |

> | 元数据字段 | 详情 |
> | :--- | :--- |
> | **arXiv ID** | [arXiv:2609.01351](https://arxiv.org/abs/2609.01351) [cs.RO] |
> | **主要学科** | 机器人学 (`cs.RO`) |
> | **次要学科** | 人工智能 (`cs.AI`) |
> | **提交日期** | 2026年9月1日 |
> | **作者** | Jiho Lee, Nisar Ahmed, Kyle Hollins Wray, Zachary Sunberg |
> | **DOI** | [10.48550/arXiv.2609.01351](https://doi.org/10.48550/arXiv.2609.01351) |

---

## Abstract
Online planning under uncertainty remains a fundamental challenge for robotic systems operating in partially observable environments with high-dimensional state spaces. While sampling-based POMDP solvers enable approximate decision-making in large or continuous domains, their performance degrades as belief dimensionality increases due to the high variance inherent in Monte Carlo-based estimation. 

In this work, we extend the Rao-Blackwellized online POMDP (RB-POMDP) framework to improve its generalizability in high-dimensional settings through hybrid continuous-discrete belief representations. By analytically propagating uncertainty associated with marginalized state components during tree-based planning, the proposed approach reduces sampling-induced variance in value estimation. We demonstrate the effectiveness of this framework in a robotic search-and-rescue task by integrating it with FastSLAM 2.0. Experimental results show that the proposed planner achieves higher cumulative rewards using significantly fewer particles and planning simulations than purely sampling-based methods under equivalent computational budgets. These results suggest that structured high-dimensional robotic problems admitting tractable sufficient statistics can be effectively leveraged within the RB-POMDP framework for computationally feasible online decision-making.

> 在具有高维状态空间的部分可观测环境中运行的机器人系统，在面对不确定性时进行在线规划依然是一项根本性挑战。虽然基于采样的POMDP求解器能够在大规模或连续域中进行近似决策，但由于基于蒙特卡洛的估计固有的高方差，当信念空间维度增加时，其性能会随之下降。
> 
> 在这项工作中，我们扩展了 Rao-Blackwellized 在线 POMDP (RB-POMDP) 框架，通过混合连续-离散信念表示来提升其在高维环境中的泛化能力。通过在基于树的规划过程中解析地传播与边缘化状态分量相关的不确定性，所提出的方法降低了价值估计中由采样引入的方差。我们通过将该框架与 FastSLAM 2.0 相结合，展示了其在机器人搜救任务中的有效性。实验结果表明，在同等的计算预算下，所提出的规划器使用显著较少的粒子和规划模拟，即可获得更高的累积奖励。这些结果表明，在 RB-POMDP 框架内，可以有效利用那些具有可处理充分统计量的结构化高维机器人问题，从而实现计算上可行的在线决策。

---

## Access & Resources
* **Full-Text PDFs & Sources:** [View PDF](https://arxiv.org/pdf/2609.01351) | [HTML (Experimental)](https://arxiv.org/html/2609.01351v1) | [TeX Source](https://src/2609.01351)
* **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01351) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01351) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01351)

> ## 访问与资源
> * **全文 PDF 与源码：** [查看 PDF](https://arxiv.org/pdf/2609.01351) | [HTML（实验性）](https://arxiv.org/html/2609.01351v1) | [TeX 源码](https://src/2609.01351)
> * **引用与参考文献：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01351) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01351) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01351)