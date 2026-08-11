---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 大语言模型
- 智能体技能
- 图对齐
- 安全检测
- 静态分析
title: SkillConsist：通过双向图对齐检测智能体技能中的不一致性
---
### 文章背景与核心概要
随着大语言模型（LLM）智能体的广泛应用，**智能体技能（Agent Skills）**成为了实现可复用能力的核心组件。然而，技能声明的意图与其真实实现代码之间如果存在不一致，往往会引入未披露的安全风险或导致技能选择错误。由于技能声明和实现跨越了文本和代码等多种异构格式，且精炼的声明通常对应复杂的、多步骤的代码实现，现有方法在检测这类不一致性时面临巨大挑战。

为了解决这一难题，本文作者推出了 **SkillConsist**——一个创新性框架。该框架结合了大语言模型与静态分析技术来分离行为记录，构建出不同的行为图，并通过**双向图对齐（Bidirectional Graph Alignment）**和图差分（Graph Differencing）来精准检测和定位冲突。在包含来自 ClawHub 和 SkillInject 的 633 个技能的新建基准测试上，SkillConsist 表现优异，包级别的检测 F1 分数达到了 **87.93%**，大幅超越现有基线。

---

# SkillConsist: Detecting Inconsistencies in Agent Skills via Bidirectional Graph Alignment

**Authors:** Chaofan Meng, Yuhang Zheng, Yingnan Zhou, Sihan Xu  
**arXiv ID:** [arXiv:2608.07639 [cs.LG]]  
**Submitted:** August 7, 2026  
**Subjects:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`)  

> **Authors:** Chaofan Meng, Yuhang Zheng, Yingnan Zhou, Sihan Xu  
> **arXiv ID:** [arXiv:2608.07639 [cs.LG]]  
> **Submitted:** August 7, 2026  
> **Subjects:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`)  

---

## 📋 Summary

Large Language Model (LLM) agents rely on **Agent Skills** for reusable capabilities. However, inconsistencies between a skill's declared intentions and its actual implementation can expose undisclosed security risks or lead to incorrect skill selection. 

Existing methods struggle because skill declarations and implementations span multiple formats (text and code), and concise declarations often map to complex, multi-step code implementations. To solve this, the authors introduce **SkillConsist**, a novel framework that uses LLMs and static analysis to separate behavior records, constructs distinct behavioral graphs, and applies **bidirectional graph alignment** and graph differencing to detect and localize conflicts.

Tested on a newly constructed benchmark of 633 skills from ClawHub and SkillInject, SkillConsist significantly outperforms existing baselines, achieving an **87.93% F1 score** for package-level detection.

> ## 📋 摘要概述
> 
> 大语言模型（LLM）智能体依赖**智能体技能（Agent Skills）**来实现可复用的能力。然而，技能声明的意图与其真实实现之间存在的不一致性，可能会暴露出未披露的安全风险，或者导致错误的技能选择。
> 
> 现有的方法难以应对这一问题，因为技能声明和实现跨越了多种格式（文本和代码），且简练的声明往往对应着复杂的多步骤代码实现。为了解决这一问题，作者推出了 **SkillConsist**——一个创新性框架，它利用 LLM 和静态分析来分离行为记录、构建不同的行为图，并应用**双向图对齐**和图差分技术来检测和定位冲突。
> 
> 在包含来自 ClawHub 和 SkillInject 的 633 个技能的新建基准测试中，SkillConsist 显著优于现有基线，在包级别检测上实现了 **87.93% 的 F1 分数**。

---

## 🔍 Abstract & Motivation

* **The Problem:** Agent Skill inconsistencies can cause wrong skill selection or conceal malicious, undisclosed behaviors. Prior approaches evaluate behaviors and security properties against static categories, while LLM-based models like PL-HCL struggle when declarations and implementations are split across diverse text and code structures.
* **The Solution (SkillConsist):**
  1. **Behavior Separation:** An LLM separates declaration and implementation components into distinct behavior records, supplemented by static analysis for code implementation.
  2. **Behavior Graphs:** These records form separate declaration and implementation behavior graphs.
  3. **Bidirectional Graph Alignment:** Starting from behavior records on either side, the system searches the opposing graph for candidate subgraphs, expanding them along relational paths until the source-side behavior is completely covered.
  4. **Graph Differencing:** Conflicts are surfaced by comparing the aligned subgraphs.

> ## 🔍 摘要与动机
> 
> * **问题所在：** 智能体技能的不一致性会导致错误的技能选择，或掩盖恶意的、未披露的行为。先前的多对静态类别评估行为和安全属性的方法，以及像 PL-HCL 这样基于 LLM 的模型，在面对跨越多样化文本和代码结构的声明与实现时往往力不从心。
> * **解决方案（SkillConsist）：**
>   1. **行为分离（Behavior Separation）：** LLM 将声明和实现组件分离为不同的行为记录，辅以针对代码实现的静态分析。
>   2. **行为图（Behavior Graphs）：** 这些记录构成了独立的声明行为图和实现行为图。
>   3. **双向图对齐（Bidirectional Graph Alignment）：** 从任一侧的行为记录出发，系统在对立的图中搜索候选子图，沿着关系路径对其进行扩展，直到完全覆盖源侧的行为。
>   4. **图差分（Graph Differencing）：** 通过对比对齐后的子图来浮现冲突。

---

## 📊 Benchmark & Evaluation Results

The authors constructed a robust benchmark comprising **633 Skills** (500 most-downloaded public skills from ClawHub and 133 Skill-Inject packages):
* **Composition:** 319 inconsistent skills, 314 consistent skills, and 442 localized inconsistency annotations.
* **Package-Level Detection:** 
  * **Precision:** 86.85%
  * **Recall:** 89.03%
  * **F1-Score:** 87.93% *(improving the best baseline by **20.43 percentage points**)*
* **Inconsistency Localization:** 
  * **Precision:** 67.60%
  * **Recall:** 58.14%
  * **F1-Score:** 62.52%

> ## 📊 基准测试与评估结果
> 
> 作者构建了一个包含 **633 个技能**（来自 ClawHub 下载量最高的前 500 个公开技能和 133 个 Skill-Inject 软件包）的强大基准测试：
> * **组成：** 319 个不一致的技能、314 个一致的技能，以及 442 个局部不一致注释。
> * **包级别检测：** 
>   * **精确率（Precision）：** 86.85%
>   * **召回率（Recall）：** 89.03%
>   * **F1 分数（F1-Score）：** 87.93% *（较最佳基线提升了 **20.43 个百分点**）*
> * **不一致性定位：** 
>   * **精确率（Precision）：** 67.60%
>   * **召回率（Recall）：** 58.14%
>   * **F1 分数（F1-Score）：** 62.52%

---

## 🔗 Links & Resources

* [View PDF](https://arxiv.org/pdf/2608.07639)
* [arXiv Abstract](https://arxiv.org/abs/2608.07639)
* [TeX Source](https://arxiv.org/src/2608.07639)
* [License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ## 🔗 链接与资源
> 
> * [查看 PDF](https://arxiv.org/pdf/2608.07639)
> * [arXiv 摘要](https://arxiv.org/abs/2608.07639)
> * [TeX 源码](https://arxiv.org/src/2608.07639)
> * [许可证 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)
> 
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">