---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 人工智能
- 集成光子学
- 大语言模型
- 逆向设计
- 自动化
title: VortexChat：用于自主多目标集成光子设计的智能体框架
---
### 文章背景与核心概要

现代集成光子学的发展长期受限于依赖人工仿真和专家经验的传统设计流程。尽管逆向设计提供了一种替代方案，但它仍受限于对专家监督的过度依赖，且缺乏真正的端到端自动化能力。

为了解决这些挑战，研究团队提出了 **VortexChat**，这是一个能够直接根据自然语言规范进行集成光子器件自主、端到端逆向设计的智能体框架。该系统通过将大语言模型（LLM）决策智能体与拓扑生成、基于梯度的优化以及全波电磁仿真相结合，构建了一个闭环架构。它能够自主分解设计目标、调度计算工具，并根据仿真反馈迭代优化策略。

VortexChat 在 *Vortex100 Benchmark* 的严格指标约束下，实现了完全无需人工干预的器件设计。实验验证中，该系统自主设计的宽带太赫兹完美涡旋光束复用器在物理测试中表现出高效率、高模式纯度和低串扰，与仿真结果高度吻合，证明了 LLM 智能体在处理复杂光子系统设计任务中的巨大潜力。

---

## 📄 摘要

> The advancement of modern integrated photonics is frequently bottlenecked by device design workflows that rely heavily on manual simulation and expert intuition. While inverse design offers an alternative, it remains constrained by expert supervision and a lack of end-to-end automation. To address these issues, we present VortexChat, an agentic framework for the autonomous, end-to-end inverse design of integrated photonic devices directly from natural language specifications. VortexChat couples a large language model (LLM) decision agent with topology generation, gradient-based refinement, and full-wave electromagnetic simulation. This closed-loop architecture enables the system to iteratively decompose design objectives, orchestrate computational tools, and update strategies based on feedback with minimal human intervention. Constrained by the absolute metrics of the Vortex100 Benchmark, VortexChat autonomously generates devices that strictly meet all predefined performance thresholds without any human-in-the-loop. As an experimental demonstration, we fabricated a broadband terahertz perfect vortex beam multiplexer, autonomously designed by VortexChat, with measurements confirming high-efficiency operation, high mode purity and low inter-channel crosstalk in agreement with full-wave simulations. These results demonstrate that an LLM agent can assume key aspects of expert decision-making in photonic inverse design while maintaining physical fidelity and fabrication feasibility, providing a scalable route towards autonomous design of complex integrated photonic systems.

现代集成光子学的进步经常受到依赖人工仿真和专家直觉的器件设计工作流程的阻碍。虽然逆向设计提供了一种替代方案，但它仍然受到专家监督和缺乏端到端自动化的限制。为了解决这些问题，我们提出了 VortexChat，这是一个用于直接根据自然语言规范对集成光子器件进行自主、端到端逆向设计的智能体框架。VortexChat 将大语言模型（LLM）决策智能体与拓扑生成、基于梯度的细化和全波电磁仿真相结合。这种闭环架构使系统能够迭代地分解设计目标、编排计算工具，并根据反馈更新策略，且只需极少的人工干预。在 Vortex100 基准测试的绝对指标约束下，VortexChat 自主生成了严格满足所有预定义性能阈值的器件，且无需任何人工参与。作为实验演示，我们制造了一个由 VortexChat 自主设计的宽带太赫兹完美涡旋光束复用器，测量结果证实了其高效率运行、高模式纯度和低通道间串扰，与全波仿真结果一致。这些结果表明，LLM 智能体可以在保持物理保真度和制造可行性的同时，承担光子逆向设计中专家决策的关键方面，为复杂集成光子系统的自主设计提供了一条可扩展的途径。

---

## 🔗 链接与资源

* **全文 PDF:** [View PDF](https://arxiv.org/pdf/2608.20688)
* **DOI:** [10.48550/arXiv.2608.20688](https://doi.org/10.48550/arXiv.2608.20688)
* **外部参考:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20688) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20688) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20688)

---
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">