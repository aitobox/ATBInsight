---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- Terminal-Universe
- 智能体环境
- 强化学习
- 代码智能体
- 轨迹重建
title: Terminal-Universe：将智能体轨迹转化为可扩展的终端环境
---
### 文章背景与核心概要
尽管基于终端的代码智能体（Code Agents）正变得日益普及，但现实且可执行的交互式环境依然稀缺，这与海量的智能体轨迹形成了鲜明对比。这种环境的匮乏构成了重大障碍，因为智能体的后训练（Post-training）严重依赖于能够被重新查询、转化为多个可验证任务并提供执行反馈的交互式环境，而单纯的轨迹只是一份被冻结的单一示范。

本文介绍了 **Terminal-Universe**，这是一个创新的框架，它能够将原始的智能体轨迹转化为可复用、可扩展的终端环境。通过分析工具执行历史，该框架能够重建工作区文件、在广度（跨代码库查询）和深度（多轮交互会话）上合成新任务，并最终产出 37.3k 个任务充分的环境（task-sufficient environments）。在这一语料库上对诸如 `Qwen3.5-27B` 等模型进行微调，能够在 Terminal-Bench 2.1 和 EvoCode-Bench v2 等基准测试中带来显著的性能提升。

---

# Terminal-Universe：将智能体轨迹转化为可扩展的终端环境 (Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments)

**arXiv ID:** [arXiv:2609.04148](https://arxiv.org/abs/2609.04148)  
**Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
**Submitted:** September 3, 2026  
**Authors:** Jie Wu, Zhenru Zhang, Beichen Zhang, Xuwu Wang, Yuhui Su, Mouxiang Chen, Peng Wang, Zhihai Wang, Que Shen, Hao Zhou, An Yang, Fei Huang, Yujiu Yang, Dayiheng Liu  

> **arXiv ID:** [arXiv:2609.04148](https://arxiv.org/abs/2609.04148)  
> **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
> **Submitted:** September 3, 2026  
> **Authors:** Jie Wu, Zhenru Zhang, Beichen Zhang, Xuwu Wang, Yuhui Su, Mouxiang Chen, Peng Wang, Zhihai Wang, Que Shen, Hao Zhou, An Yang, Fei Huang, Yujiu Yang, Dayiheng Liu  

---

## 执行摘要 (Executive Summary)

尽管基于终端的代码智能体正变得日益普及，但现实且可执行的环境依然稀缺，这与海量的智能体轨迹形成了鲜明对比。这种稀缺性带来了重大的障碍，因为智能体的后训练严重依赖于交互式环境——这些环境可以被重新查询为多个可验证的任务并提供执行反馈，而轨迹仅仅是一个单一的、被冻结的示范。

本文介绍了 **Terminal-Universe**，这是一个新颖的框架，它将原始的智能体轨迹转化为可复用、可扩展的终端环境。通过分析工具执行历史，该框架重建了工作区文件，在广度（跨代码库查询）和深度（多轮交互会话）上合成了新任务，并产出了 37.3k 个任务充分的环境。在这一语料库上对 `Qwen3.5-27B` 等模型进行微调，在 Terminal-Bench 2.1 和 EvoCode-Bench v2 等基准测试上取得了大幅度的性能提升。

> While terminal-based code agents are becoming increasingly prevalent, realistic and executable environments remain scarce despite a surplus of agent trajectories. This scarcity presents a significant hurdle because agent post-training relies heavily on interactive environments that can be re-queried into multiple verifiable tasks and provide execution feedback—whereas a trajectory is merely a single, frozen demonstration. 
> 
> This paper introduces **Terminal-Universe**, a novel framework that transforms raw agent trajectories into reusable, scalable terminal environments. By analyzing tool-execution histories, the framework reconstructs workspace files, synthesizes new tasks across breadth (multi-codebase queries) and depth (multi-round interactive sessions), and produces 37.3k task-sufficient environments. Fine-tuning models like `Qwen3.5-27B` on this corpus yields substantial performance gains on benchmarks such as Terminal-Bench 2.1 and EvoCode-Bench v2.

---

## 核心创新与方法论 (Key Innovations & Methodology)

Terminal-Universe 的核心洞察在于：轨迹中记录的工具执行历史本身就暴露了其执行环境的结构与内容。该框架通过几个关键阶段运行：

1. **工作区重建：**
   - 重放轨迹中记录的文件操作，将每个文件恢复到修改前的状态，从而生成部分工作区。
   - 采用**补全智能体（completion agent）**来补充所有缺失的文件和依赖项。
2. **任务合成：**
   - 重建原始意图任务，同时基于恢复的工作区合成全新的任务。
3. **双轴扩展：**
   - **广度（Breadth）：** 挖掘相关环境之间的定向依赖关系，以合成跨多个代码库的跨工作区查询（模拟现实世界的软件开发）。
   - **深度（Depth）：** 使用用户智能体将单轮查询扩展为多轮会话，以捕捉迭代反馈和需求求精。

> The core insight of Terminal-Universe is that a trajectory's recorded tool-execution history inherently exposes the structure and contents of the environment in which it was executed. The framework operates through several key stages:
> 
> 1. **Workspace Reconstruction:** 
>    - Replays file operations recorded in a trajectory to restore each file to its pre-modified state, generating a partial workspace.
>    - Employs a **completion agent** to supply any missing files and dependencies.
> 2. **Task Synthesis:** 
>    - Reconstructs original intent tasks while simultaneously synthesizing entirely new ones based on the recovered workspace.
> 3. **Scaling Along Two Axes:**
>    - **Breadth:** Mines directional dependency relations between related environments to synthesize cross-workspace queries spanning multiple codebases (mirroring real-world software development).
>    - **Depth:** Extends single-turn queries into multi-round sessions using a user agent to capture iterative feedback and requirement refinement.

---

## 结果与性能 (Results & Performance)

* **环境生成：** Terminal-Universe 从公开的终端智能体轨迹中成功生成了 **37.3k 个任务充分的环境**。
* **监督微调（SFT）：** 在生成的语料库上对 `Qwen3.5-27B` 进行微调带来了以下成果：
  * 在 **Terminal-Bench 2.1** 上的单轮性能提升了 **11.9 个百分点**。
  * 在 **EvoCode-Bench v2 MT@4** 上的多轮性能提升了 **13.8 个百分点**。

> * **Environment Generation:** Terminal-Universe successfully produces **37.3k task-sufficient environments** from public terminal agent trajectories.
> * **Supervised Fine-Tuning (SFT):** Fine-tuning `Qwen3.5-27B` on the generated corpus results in:
>   * An **11.9-point improvement** in single-round performance on **Terminal-Bench 2.1**.
>   * A **13.8-point improvement** in multi-round performance on **EvoCode-Bench v2 MT@4**.

---

## 链接与资源 (Links and Resources)

* **arXiv 摘要：** [arXiv:2609.04148](https://arxiv.org/abs/2609.04148)
* **DOI：** [10.48550/arXiv.2609.04148](https://doi.org/10.48550/arXiv.2609.04148)
* **直接访问：** [查看 PDF](https://arxiv.org/pdf/2609.04148) | [TeX 源码](https://arxiv.org/src/2609.04148)

> * **arXiv Abstract:** [arXiv:2609.04148](https://arxiv.org/abs/2609.04148)
> * **DOI:** [10.48550/arXiv.2609.04148](https://doi.org/10.48550/arXiv.2609.04148)
> * **Direct Access:** [View PDF](https://arxiv.org/pdf/2609.04148) | [TeX Source](https://arxiv.org/src/2609.04148)