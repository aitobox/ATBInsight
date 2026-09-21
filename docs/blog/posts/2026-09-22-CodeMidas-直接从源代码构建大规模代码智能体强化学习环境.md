---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-22
hide:
  - navigation
tags:
  - CodeMidas
  - 智能体代码生成
  - 强化学习环境
  - GRPO
  - 自动化验证
title: "CodeMidas：直接从源代码构建大规模代码智能体强化学习环境"
---

# CodeMidas：直接从源代码构建大规模代码智能体强化学习环境

> # CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

### 文章背景与核心概要

当前，利用强化学习 (Reinforcement Learning, RL) 训练具备复杂软件工程能力的代码智能体 (Coding Agent)，核心瓶颈在于缺乏海量且自带可靠验证器的真实任务环境。传统做法高度依赖 GitHub 的 Issue 讨论与提交历史 (Commit)，不仅数据获取难度大，且任务类型极为受限。为此，研究团队提出了创新框架 CodeMidas，首次实现仅以开源源代码本身为任务输入，端到端自动生成具备可执行验证能力的大规模强化学习环境。实验证明，在该环境下通过组相对策略优化 (Group Relative Policy Optimization, GRPO) 训练的模型，在问题修复、完整程序构建及终端操作等多个基准测试中均实现大幅跃升，并展现出更深入的代码探索与自主验证行为。该成果为低成本、大规模构建智能体强化学习数据飞轮提供了全新的范式。

---

## 内容概要

> ## Summary

要通过强化学习 (RL) 培养出能力稳健的代码智能体，通常需要大量兼具多样性且配备可靠验证器的真实任务。然而，传统构建方法往往严重依赖软件开发过程中留下的痕迹——例如 GitHub 上的 Issue 问题单和提交历史 (Commit)。这种模式极大地限制了能够被提取出来的任务数量与任务形态的多样性。

> Training robust coding agents via reinforcement learning (RL) typically requires diverse tasks paired with reliable verifiers. Traditionally, methods rely heavily on development artifacts like GitHub issues and commits, which restricts the overall volume and variety of extractable tasks.

为了打破这一瓶颈，**CodeMidas** 推出了一套极具创新性的智能体流水线。它无需任何辅助的开发日志，直接将已有代码库中已经实现的功能转化为可交互、可运行的强化学习环境，把源代码本身作为唯一针对特定任务的输入源。

> To overcome this bottleneck, **CodeMidas** introduces an innovative agentic pipeline that transforms the implemented functionality of existing codebases directly into executable RL environments using source code as the sole task-specific input.

该方法的核心亮点包括：

> Key highlights of the approach include:

* **全流程智能体算力分配 (Agentic Compute Allocation)**：让智能体深度参与环境构建的每一个阶段——由智能体自主探索代码库功能以拟定软件行为规范，基于原始代码构建具备真实执行反馈的测试用例，并通过实际运行检查和多次解法推演 (Rollout) 对候选任务进行严格过滤。
* **空前的数据集规模 (Massive Scale)**：构建出的数据集包含了从 **3,185 个开源代码库**中提炼出的 **5,545 个训练任务**，广泛覆盖 **23 种编程语言**与 **15 个技术领域**。
* **显著的性能跃升 (Performance Gains)**：在这些任务上使用组相对策略优化 (GRPO) 对 MiMo-V2.5 模型进行训练，在五项不同的软件工程基准测试中全面提升了模型表现：
  * **问题修复 (Issue Repair)**：DeepSWE (+11.7%)
  * **完整程序构建 (Whole-Program Construction)**：ProgramBench (+17%)
  * **终端操作工作 (Terminal Work)**：Terminal-Bench v2.1 (+8.5%)
* **智能体行为的深度进化 (Behavioral Improvements)**：消融实验与轨迹分析表明，扩大高质量训练任务的规模能够促使智能体进行更深入的代码库探索，并自发展现出更加丰富多样的自我验证行为。

> * **Agentic Compute Allocation:** Agents explore codebase functionality to formulate behavioral specifications, build execution-grounded tests based on original code, and rigorously filter tasks via execution checks and repeated solution rollouts.
> * **Massive Scale:** The resulting dataset encompasses **5,545 training tasks** extracted from **3,185 open-source codebases**, spanning **23 programming languages** and **15 technical domains**.
> * **Performance Gains:** Training the MiMo-V2.5 model using Group Relative Policy Optimization (GRPO) on these tasks significantly boosts performance across five diverse software benchmarks:
>   * **Issue Repair:** DeepSWE (+11.7%)
>   * **Whole-Program Construction:** ProgramBench (+17%)
>   * **Terminal Work:** Terminal-Bench v2.1 (+8.5%)
> * **Behavioral Improvements:** Ablations and trajectory analysis demonstrate that scaling high-quality training tasks encourages agents to perform deeper codebase exploration and exhibit more diverse self-verification behaviors.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 编号 (arXiv ID)**：[arXiv:2609.22068](https://arxiv.org/abs/2609.22068) [cs.AI]
* **主要学科领域 (Primary Subject)**：计算机科学 > 人工智能 (`cs.AI`)
* **提交日期 (Submission Date)**：2026 年 9 月 18 日
* **论文作者 (Authors)**：Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, Hanglong Lv, Yuanxin Liu, Wenhan Ma, Hao Tian, Rang Li, Jinhao Dong, Yikai Zhao, Xiangwei Deng, Hailin Zhang, Liang Zhao, Qi Liu, Lingpeng Kong, Tong Yang, Fuli Luo

> * **arXiv ID:** [arXiv:2609.22068](https://arxiv.org/abs/2609.22068) [cs.AI]
> * **Primary Subject:** Computer Science > Artificial Intelligence (`cs.AI`)
> * **Submission Date:** September 18, 2026
> * **Authors:** Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, Hanglong Lv, Yuanxin Liu, Wenhan Ma, Hao Tian, Rang Li, Jinhao Dong, Yikai Zhao, Xiangwei Deng, Hailin Zhang, Liang Zhao, Qi Liu, Lingpeng Kong, Tong Yang, Fuli Luo

---

## 论文摘要

> ## Abstract

通过强化学习 (RL) 训练高水平的代码智能体，离不开配有可靠验证器的多样化任务。虽然开源代码库蕴藏着海量此类任务的宝藏，但现有方法通常依赖于代码开发过程中留下的衍生记录（如 Issue 问题单和提交历史 Commit），这极大地限制了可提取任务的范围与丰富度。为了更好地扩大强化学习环境的规模，我们提出了 **CodeMidas**——这是一个基于智能体的新型流水线，仅将源代码作为针对特定任务的唯一输入，就能将现有代码库中已实现的功能直接转化为可交互执行的强化学习环境。

> Training capable coding agents via reinforcement learning (RL) requires diverse tasks with reliable verifiers. Open-source codebases offer a rich source of such tasks, while existing methods typically rely on development artifacts such as issues and commits, limiting the range of tasks that can be extracted. To better scale RL environments, we present **CodeMidas**, an agentic pipeline that turns implemented functionality in existing codebases into executable RL environments using source code as its only task-specific input.

CodeMidas 在环境构建的每个阶段都充分投入了智能体算力：由智能体深入探索已实现的代码功能以制定软件行为规范；基于对原始代码的真实运行构建验证测试；并通过代码执行检查与多次解法推演 (Rollout) 来检验并筛选候选任务。最终构建生成的数据集包含了来自 3,185 个开源代码库的 5,545 个训练任务，涵盖 23 种编程语言以及 15 个技术领域。

> CodeMidas allocates agentic compute to every stage of environment construction: agents explore implemented functionality to formulate behavioral specifications, construct tests grounded in execution of the original code, and validate and filter candidate tasks through execution checks and repeated solution rollouts. The resulting dataset has 5,545 training tasks from 3,185 open-source codebases spanning 23 programming languages and 15 technical domains.

在这些任务上使用 GRPO 算法对 MiMo-V2.5 模型进行训练，显著提升了其在五项各具特色的基准测试上的表现，涵盖问题修复 (DeepSWE 提升 11.7%)、完整程序构建 (ProgramBench 提升 17%) 以及终端操作工作 (Terminal-Bench v2.1 提升 8.5%)。消融实验表明，增加高质量训练任务的数量能够稳步推动性能提升。轨迹分析进一步显示，经强化学习训练后的智能体展现出了更优秀的自主行为，例如显著增加了对代码库的探索深度，并展现出更为丰富多样的自我验证行为。这些研究结果证明，仅凭源代码本身即可作为可扩展的基础底座，用于构建高质量强化学习环境并全面提升代码智能体解决各类复杂软件任务的能力。

> Training MiMo-V2.5 on these tasks with GRPO improves performance on all five diverse benchmarks, covering issue repair (DeepSWE + 11.7%), whole-program construction (ProgramBench +17%), and terminal work (Terminal-Bench v2.1 +8.5%). Ablations show that increasing the number of high-quality training tasks improves performance. Trajectory analysis shows the RL-trained agent demonstrates better behaviors like increasing codebase exploration and more diverse self-verification. These results establish source code as a scalable foundation for constructing RL environments that improve coding agents across diverse software tasks.

---

## 资源获取与论文链接

> ## Access & Resources

* **论文全文链接 (Full-Text Links)**：[阅读 PDF](https://arxiv.org/pdf/2609.22068) | [网页版 HTML (实验版)](https://arxiv.org/html/2609.22068v1) | [TeX 源码](https://arxiv.org/src/2609.22068)
* **数字对象标识符 (DOI)**：[10.48550/arXiv.2609.22068](https://doi.org/10.48550/arXiv.2609.22068)

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2609.22068) | [HTML (Experimental)](https://arxiv.org/html/2609.22068v1) | [TeX Source](https://arxiv.org/src/2609.22068)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.22068](https://doi.org/10.48550/arXiv.2609.22068)
