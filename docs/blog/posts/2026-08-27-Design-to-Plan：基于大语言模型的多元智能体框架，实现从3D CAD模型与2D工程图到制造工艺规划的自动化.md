---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 大语言模型
- 多智能体框架
- 制造工艺规划
- 3D CAD
- 2D工程图
title: Design-to-Plan：基于大语言模型的多元智能体框架，实现从3D CAD模型与2D工程图到制造工艺规划的自动化
---
### 文章背景与核心概要
制造工艺规划是连接原始设计成果与可执行生产决策的关键桥梁。传统上，自动化方法往往举步维艰，因为它们只关注孤立的子任务（如特征识别或刀具选择），而无法支持完整、端到端的推理链条。

本文介绍了 **Design-to-Plan**，这是一个创新的基于大语言模型（LLM）的多智能体框架，旨在通过3D CAD模型和2D工程图自动化实现制造工艺规划。该框架没有将LLM作为独立的文本生成器，而是将其用作智能推理智能体，与确定性模块和知识库协同工作，从而提供可追溯、一致且具备上下文感知的制造工作流。

---

# Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings

**Authors:** Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng, Seung Ki Moon  
**Submitted on:** August 25, 2026 (Submitted to Elsevier Journal)  
**Subjects:** Robotics (`cs.RO`), Artificial Intelligence (`cs.AI`)  
**arXiv:** [2608.24039 [cs.RO]](https://arxiv.org/abs/2608.24039)  

---

## 📌 核心执行摘要 (Executive Summary)

制造工艺规划是连接原始设计成果与可执行生产决策的关键桥梁。传统上，自动化方法往往举步维艰，因为它们只关注孤立的子任务（如特征识别或刀具选择），而无法支持完整、端到端的推理链条。

> Manufacturing process planning bridges the gap between raw design artifacts and actionable production decisions. Traditionally, automated approaches have struggled because they focus solely on isolated subtasks (such as feature recognition or tool selection) rather than supporting the complete, end-to-end reasoning chain. 

本文介绍了 **Design-to-Plan**，这是一个创新的基于大语言模型（LLM）的多智能体框架，旨在通过3D CAD模型和2D工程图自动化实现制造工艺规划。该框架没有将LLM作为独立的文本生成器，而是将其用作智能推理智能体，与确定性模块和知识库协同工作，从而提供可追溯、一致且具备上下文感知的制造工作流。

> This paper introduces **Design-to-Plan**, an innovative Large Language Model (LLM)-based multi-agent framework designed to automate manufacturing process planning from both 3D CAD models and 2D engineering drawings. Instead of deploying LLMs as standalone text generators, the framework utilizes them as intelligent reasoning agents that collaborate with deterministic modules and knowledge bases to deliver traceable, consistent, and context-aware manufacturing workflows.

---

## 🏗️ 框架架构 (Framework Architecture)

**Design-to-Plan** 框架采用了一种混合架构，将专用的确定性模块与由中央**协调器（Orchestrator）**管理的协作式LLM驱动智能体结合起来：

> The **Design-to-Plan** framework leverages a hybrid architecture combining specialized deterministic modules with collaborative LLM-driven agents managed by a central **Orchestrator**:

* **协调器（Orchestrator）：** 协调所有专用智能体和模块之间的工作流与数据交换。
* **提取与分析模块（确定性 + 智能体）：**
  * 3D特征识别
  * 2D图纸分析
  * 2D-3D上下文融合
* **推理与规划智能体：**
  * 知识检索
  * 工艺排序
  * 刀具选择
  * 报告生成

> * **Orchestrator:** Coordinates the workflow and data exchange between all specialized agents and modules.
> * **Extraction & Analysis Modules (Deterministic + Agents):** 
>   * 3D Feature Recognition
>   * 2D Drawing Analysis
>   * 2D-3D Context Fusion
> * **Reasoning & Planning Agents:** 
>   * Knowledge Retrieval
>   * Process Sequencing
>   * Tool Selection
>   * Report Generation

在此设置中，确定性工具从CAD和图纸文件中提取精确的结构特征，而LLM智能体则处理复杂的上下文推理、解决冲突、查询特定领域的制造规则并生成最终的规划文档。

> In this setup, deterministic tools extract precise structural features from CAD and drawing files, while LLM agents handle complex contextual reasoning, resolve conflicts, query domain-specific manufacturing rules, and generate final planning documents.

---

## 📊 关键性能结果 (Key Performance Results)

该框架使用包含 **300个案例** 的稳健基准进行了评估，其中包括下游启用ReAct的智能体，以及对CAD识别、图纸解释和上下文融合的单独评估：

> The framework was evaluated using a robust benchmark of **300 cases**, incorporating downstream ReAct-enabled agents alongside individual evaluations for CAD recognition, drawing interpretation, and context fusion:

* **下游智能体成功率：** 下游规划智能体实现了高达 **100% 的完美成功率**。
* **刀具选择 F1 分数：** 介于 **95.9% 和 97.6%** 之间。
* **冲突解决准确率：** 在复杂的冲突分析中，源检测准确率达到了 **90%**。
* **Token效率：** 核心规划任务的 **Token使用量减少了 60% 至 68%**，证明了结构化多智能体架构的高效性。

> * **Downstream Agent Success Rate:** Achieved a flawless **100% success rate** across downstream planning agents.
> * **Tool Selection F1-Score:** Ranged between **95.9% and 97.6%**.
> * **Conflict Resolution Accuracy:** Reached **90% source detection accuracy** during complex conflict analyses.
> * **Token Efficiency:** Delivered a **60% to 68% reduction in token usage** for core planning tasks, proving the efficiency of the structured multi-agent architecture.

---

## 🔗 链接与资源 (Links and Resources)

* **查看PDF：** [arXiv:2608.24039 PDF](https://arxiv.org/pdf/2608.24039)
* **HTML版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.24039v1)
* **DOI：** [10.48550/arXiv.2608.24039](https://doi.org/10.48550/arXiv.2608.24039)
* **许可证：** [创作共用署名-非商业性使用-禁止演绎 4.0 国际许可协议 (Creative Commons BY-NC-ND 4.0)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

> * **View PDF:** [arXiv:2608.24039 PDF](https://arxiv.org/pdf/2608.24039)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.24039v1)
> * **DOI:** [10.48550/arXiv.2608.24039](https://doi.org/10.48550/arXiv.2608.24039)
> * **License:** [Creative Commons BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)