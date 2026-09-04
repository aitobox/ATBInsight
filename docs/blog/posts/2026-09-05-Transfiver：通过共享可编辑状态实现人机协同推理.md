---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 人机交互
- 协同推理
- 状态管理
- 人工智能
title: Transfiver：通过共享可编辑状态实现人机协同推理
---
### 文章背景与核心概要
长期的人机交互往往会失效，因为引导模型推理的内部信息是以隐式方式更新的，对用户而言始终是不透明的。为了解决这一痛点，研究人员引入了 **Transfiver**（交互式、可验证、可编辑表示的透明框架）。Transfiver 建立了一种架构，其中人类和人工智能通过单一的、持久的且可编辑的共享状态（$S_t$）进行协同推理。

这种设计使得人类的纠正可以直接改变计算状态，而不仅仅是作为一条独立的指令，从而弥合了隐式模型更新与显式用户控制之间的鸿沟。该研究不仅提升了人机交互的透明度与可控性，还为构建更加稳定、可干预的 AI 系统提供了全新的技术范式。

---

# Transfiver: Human-AI Co-Inference through a Shared Editable State

> # Transfiver: Human-AI Co-Inference through a Shared Editable State

## Summary

> ## Summary

长期的人机交互往往会失效，因为引导模型推理的内部信息是由模型隐式更新的，用户无法直接检查或控制。为了解决这个问题，研究人员引入了 **Transfiver**（交互式、可验证、可编辑表示的透明框架，TRANSparent Framework for Interactive, Verifiable, Editable Representation）。Transfiver 建立了一种架构，使人类和 AI 能够通过单一的、持久的且可编辑的共享状态（$S_t$）进行协同推理。这使得人类的纠正可以直接改变计算状态，而不是作为单独的指令，从而弥合了隐式模型更新与显式用户控制之间的鸿沟。

> Long-term human-AI interactions often break down because the internal information guiding the model's inference is updated implicitly and remains opaque to the user. To solve this, researchers introduce **Transfiver** (TRANSparent Framework for Interactive, Verifiable, Editable Representation). Transfiver establishes an architecture where both the human and the AI co-infer via a single, persistent, and editable shared state ($S_t$). This allows human corrections to directly alter the computational state rather than acting as a separate instruction, bridging the gap between implicit model updates and explicit user control.

---

## Metadata

> ## Metadata

* **arXiv ID:** [arXiv:2609.03797](https://arxiv.org/abs/2609.03797) [cs.AI]
> * **arXiv ID:** [arXiv:2609.03797](https://arxiv.org/abs/2609.03797) [cs.AI]
* **Subjects:** 人工智能 (`cs.AI`); 计算与语言 (`cs.CL`); 人机交互 (`cs.HC`)
> * **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`); Human-Computer Interaction (`cs.HC`)
* **Authors:** Minji Park, Seunghyun Yoon, Hyuk Lim
> * **Authors:** Minji Park, Seunghyun Yoon, Hyuk Lim
* **Submitted:** 2026年9月3日
> * **Submitted:** September 3, 2026
* **DOI:** [10.48550/arXiv.2609.03797](https://doi.org/10.48550/arXiv.2609.03797)
> * **DOI:** [10.48550/arXiv.2609.03797](https://doi.org/10.48550/arXiv.2609.03797)

---

## Abstract

> ## Abstract

长期的人机交互之所以困难，是因为引导推理的信息是由模型隐式更新的，用户既不能直接检查，也不能直接控制。我们介绍了 **TRANSparent Framework for Interactive, Verifiable, Editable Representation (Transfiver)**，这是一种通过共享可编辑状态进行人机协同推理的架构。其核心思想是：特定于交互的信息保存在一个单一的持久状态（$S_t$）中，模型和人类都可以对其进行更新。

> Long-term human-AI interaction is difficult because the information that guides inference is updated implicitly by the model and is not directly inspectable or controllable by the user. We introduce the **TRANSparent Framework for Interactive, Verifiable, Editable Representation (Transfiver)**, an architecture for human-AI co-inference through a shared editable state. Its central idea is that interaction-specific information is maintained in a single persistent state ($S_t$) that both the model and the human update.

Transfiver 区分了状态演化的两种模式：
1. **隐式流更新（Implicit Stream Update）：** 模型解释正在进行的交互，并决定新信息是修改现有的状态项还是创建一个新项。
2. **显式定向编辑（Explicit Directed Edit）：** 人类检查并修改指定的目标项。

> Transfiver distinguishes two modes of state evolution:
> 1. **Implicit Stream Update:** The model interprets ongoing interaction and decides whether new information revises an existing state item or creates a new one.
> 2. **Explicit Directed Edit:** A human inspects and modifies an addressed item. 

这两者都作用于相同的底层状态，因此人类的纠正会改变后续计算所读取的状态，而不是添加另一条指令或单独的记录。

> Both act on the same underlying state, so a human correction changes the state that subsequent computation reads, rather than adding another instruction or separate record.

该架构将普通使用前预先学习的共享参数（$\theta$），与在部署过程中不断演化且无需重新训练参数的持久状态（$S_t$）分离开来。将 Transfiver 扩展到丰富的自然语言、关系型和大规模共享状态，目前仍然是一个开放的研究方向。

> The architecture separates shared parameters ($\theta$), learned before ordinary use, from the persistent state ($S_t$), which evolves during deployment without parameter retraining. Extending Transfiver to rich natural-language, relational, and large-scale shared states remains open.

---

## Links & Resources

> ## Links & Resources

* [查看 PDF](https://arxiv.org/pdf/2609.03797)
> * [View PDF](https://arxiv.org/pdf/2609.03797)
* [HTML 版本（实验性）](https://arxiv.org/html/2609.03797v1)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.03797v1)
* [TeX 源码](https://arxiv.org/src/2609.03797)
> * [TeX Source](https://arxiv.org/src/2609.03797)
* [查看许可协议](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)
> * [View License](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)