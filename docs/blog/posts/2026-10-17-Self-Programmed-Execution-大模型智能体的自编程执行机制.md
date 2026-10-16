---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-17
hide:
  - navigation
tags:
  - 大语言模型
  - AI 智能体
  - 自编程执行
  - Spell语言
  - 架构创新
title: "Self-Programmed Execution：大模型智能体的自编程执行机制"
---

# Self-Programmed Execution：大模型智能体的自编程执行机制

> # Self-Programmed Execution for Language-Model Agents

> **arXiv ID:** [2605.06898v2](https://arxiv.org/abs/2605.06898v2) [cs.AI]  
> **Authors:** Luke J. O'Connor  
> **Subjects:** Artificial Intelligence (`cs.AI`)  
> **Conference:** Accepted at NeurIPS 2026 (Camera-ready version, 77 pages)  
> **Links:** [View PDF](https://arxiv.org/pdf/2605.06898) | [HTML Version](https://arxiv.org/html/2605.06898v2) | [GitHub Repository](https://github.com/lukejoconnor/spell)

### 文章背景与核心概要

长期以来，基于大语言模型 (Large Language Model, LLM) 构建的 AI 智能体 (AI Agent) 往往被束缚在外部框架设定的固定规则之中——轮次交替与工具调度的逻辑完全由系统宿主程序掌控，模型自身只是被动响应的调用接口。入选 NeurIPS 2026 的这篇长达 77 页的重磅论文打破了这一固有范式，创新性地提出了**自编程执行 (Self-Programmed Execution, SPE)** 机制：将模型生成的补全内容本身直接转化为动态编排程序，外部环境仅负责代码求值，不再强加任何僵化的预设策略。为了解决“代码源文件同时充当模型自身上下文窗口”这一独特的工程约束，作者专门打造了支持自我编辑与增量求值的专用 Lisp 方言 **Spell**，在避免副作用重复执行的同时赋予智能体前所未有的动态规划自由。令人瞩目的是，即便是未针对该机制进行专项微调的现有前沿大模型，仅凭上下文学习 (In-Context Learning, ICL) 即可迅速掌握 Spell 并成功解决复杂的智能体任务，为摆脱传统框架束缚、迈向完全自主演进的通用人工智能 (AGI) 奠定了坚实的基础。

---

## 内容概要

> ## Summary

在传统的语言模型智能体架构中，连续轮次之间的状态转移通常由系统外围环境（Harness）内置的外部编排程序严格掌控。本文则提出了**自编程执行 (Self-Programmed Execution, SPE)** 这一全新范式：在大语言模型补全内容的同时，该补全本身即作为编排程序运行，而外围系统仅负责对其进行求值解析，不再强加任何固定的编排策略与执行规则。

> In traditional language model agent architectures, state transitions between consecutive turns are managed by an external orchestrator program embedded within the system harness. This paper introduces **Self-Programmed Execution (SPE)**, a paradigm where the language model's own completion functions as the orchestrator program, while the harness merely evaluates it without imposing a fixed orchestration policy. 

为了克服“自编程执行程序的源代码同时兼作模型自身上下文窗口”这一独特的物理约束，作者专门提出了一种定制化的 Lisp 方言——**Spell**。Spell 具备自我编辑与自我重新求值的强大能力，同时对模型调用等产生副作用的有作用表达式进行了精心设计，确保程序在修改重算时绝不会重复触发副作用。实验表明，当前的主流前沿模型即使此前从未针对 SPE 或 Spell 进行过专门训练，也能成功通过上下文学习掌握 Spell 语法，并顺利执行各类极具挑战性的复杂智能体任务。

> To overcome the unique constraint that an SPE program's source code doubles as the model's context window, the author introduces **Spell**—a specialized Lisp dialect featuring self-editing and self-re-evaluation capabilities, alongside effectful expressions (like model invocations) structured to avoid replaying side effects upon re-evaluation. Experiments reveal that frontier models—even those not specifically trained for SPE or Spell—can successfully learn Spell *in-context* and execute complex agentic tasks.

---

## 论文摘要

> ## Abstract

语言模型智能体的核心在于一套编排调度程序，它统领着智能体在连续交互轮次之间的状态演进。然而在现有绝大多数系统中，这一程序均被固化在外部的系统脚手架（Harness）之中。本文正式提出自编程执行机制：由大语言模型生成的文本补全内容直接担任该编排程序，外部宿主环境仅负责解析并执行代码，不再强加任何固定的编排逻辑。从形式化定义来看，智能体机器的 SPE 状态允许模型补全在嵌入映射的意义下加载任意后续状态，其典型实现便是将模型生成的每段补全直接作为代码运行。但在实际工程中，由于代码源文件必须同时充当模型的上下文窗口，这要求编程语言具备罕见的技术特性。为此，作者设计并实现了 **Spell**——一种允许程序自主编辑源码并实现增量重新求值的 Lisp 方言；它通过精巧的状态结构设计，确保包含模型调用等产生外部副作用的表达式在重新求值时不会被重复触发。基于未经 SPE 或 Spell 专门微调的现有前沿模型进行的实验表明，当前顶尖大模型仅依靠上下文学习便能迅速掌握 Spell，并成功攻克高难度的智能体任务。这一成果清晰展示了语言模型如何在彻底摆脱预设编排策略的情况下自主扮演智能体，并引出了一个极具潜力的前瞻性问题：如果专门针对自编程执行展开训练，模型究竟能自主演化出怎样精妙的自编排策略？

> At the heart of a language model agent is an orchestrator program which is responsible for the state transition between consecutive turns. In existing systems, this program is implemented in the harness. This paper introduces self-programmed execution (SPE), in which the model completion is itself the orchestrator program, and the harness evaluates this program but does not impose any fixed orchestration policy. Formally, an SPE state of an agentic machine is one from which a model completion can load any successor state up to an embedding, and an instance of an SPE state is one which executes the model completion as a program. In practice, the program requires a language with unusual features, as its source code doubles as the content of the model's context window. I therefore introduce Spell, a Lisp dialect in which programs can edit and re-evaluate themselves, and effectful expressions like model invocations are structured such that re-evaluating an edited program does not replay its side effects. Experiments with existing models, not trained for SPE or Spell, show that frontier models can learn Spell in-context and accomplish challenging agentic tasks. These results demonstrate how a LM can act as an agent without any fixed orchestration policy, and they raise the question of what self-orchestration strategies might be learned by a model trained for self-programmed execution.

---

## 元数据与提交历史

> ## Metadata & Submission History

* **首次提交日期：** 2026 年 5 月 7 日 (v1)
* **最新修订日期：** 2026 年 10 月 15 日 (v2)
* **主要学科领域：** 人工智能 (`cs.AI`)
* **DOI 数字对象唯一标识符：** [10.48550/arXiv.2605.06898](https://doi.org/10.48550/arXiv.2605.06898)
* **开源协议：** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> * **Submitted:** 7 May 2026 (v1)
> * **Last Revised:** 15 Oct 2026 (v2)
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2605.06898](https://doi.org/10.48550/arXiv.2605.06898)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
