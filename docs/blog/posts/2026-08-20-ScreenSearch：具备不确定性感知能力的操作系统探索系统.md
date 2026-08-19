---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- GUI代理
- 操作系统探索
- 状态图
- 不确定性感知
- 强化学习
title: ScreenSearch：具备不确定性感知能力的操作系统探索系统
---
### 文章背景与核心概要
在桌面图形用户界面（GUI）代理的发展过程中，部分可观测性（partial observability）一直是一个核心挑战。由于视觉上相似的屏幕可能对应着完全不同的底层工作流状态，代理在执行任务时往往难以准确区分这些状态，从而导致执行结果的不稳定。

为了解决这一问题，本文介绍了全新系统 **ScreenSearch**。该系统将操作系统交互建模为一个状态探索问题，创新性地结合了结构化屏幕检索与具备歧义感知能力的图老虎机（graph-bandit）模型，从而能够高效、精准地对复杂的桌面环境进行映射和探索。研究表明，将新颖性（拓展探索边界）与状态歧义性（解析不确定状态）相结合，是构建鲁棒的桌面 GUI 自动化代理的关键所在。

---

# ScreenSearch: Uncertainty-Aware OS Exploration

**arXiv:** [2605.16024](https://arxiv.org/abs/2605.16024)  
**Authors:** Michael Solodko, Justin Wagle  
**Subject:** Artificial Intelligence (cs.AI)  
**Date:** Submitted 15 May 2026; Revised 17 Aug 2026

---

## 摘要

**ScreenSearch** 是一个旨在应对桌面 GUI 代理中部分可观测性挑战的新型系统。由于视觉相似的屏幕可能代表不同的底层工作流状态，代理经常难以区分这些状态，从而导致不一致的结果。ScreenSearch 通过将操作系统交互构建为状态探索问题来解决这一痛点，它利用结构化屏幕检索和一个具备歧义感知的图老虎机模型，有效地对桌面环境进行了映射。

> ## Summary
> **ScreenSearch** is a novel system designed to address the challenges of partial observability in desktop GUI agents. Because visually similar screens can represent different underlying workflow states, agents often struggle to distinguish between states, leading to inconsistent outcomes. ScreenSearch tackles this by framing OS interaction as a state-exploration problem, utilizing structural screen retrieval and an ambiguity-aware graph-bandit model to effectively map desktop environments.

---

## 核心特性与方法论

*   **结构化检索**：系统将 UIA（用户界面自动化）树转换为具位置感知的结构化特征，从而通过稀疏词符（token）搜索和元数据过滤实现高效索引。
*   **共享状态图**：系统维护了一个去重且跨虚拟机（cross-VM）的状态图，允许多个工作线程（workers）进行协同探索。
*   **歧义感知探索**：系统采用了一种 **PUCT（应用于树的预测置信度上界）图老虎机** 方法。它基于匹配动作的结果离散度定义了“歧义信号”——如果在相似屏幕上执行相同的动作产生不同的结果，系统就会优先对该状态进行进一步探测。
*   **新颖性与歧义性的权衡**：研究表明，虽然减少歧义至关重要，但仅靠它本身并不足以作为单一目标；有效的探索需要平衡新颖性（拓展探索前沿）与状态歧义性的解决。

> ## Key Features & Methodology
> 
> *   **Structural Retrieval:** The system converts UIA (User Interface Automation) trees into location-aware structural features, enabling efficient indexing through sparse token search and metadata filtering.
> *   **Shared State Graph:** It maintains a deduplicated, cross-VM state graph, allowing for collaborative exploration across multiple workers.
> *   **Ambiguity-Aware Exploration:** The system employs a **PUCT (Predictor Upper Confidence Bound applied to Trees) graph-bandit** approach. It defines an "ambiguity signal" based on matched-action outcome dispersion—if identical actions on similar screens yield different results, the system prioritizes further probing of that state.
> *   **Novelty vs. Ambiguity Trade-off:** The research demonstrates that while ambiguity reduction is critical, it is not a sufficient objective on its own; effective exploration requires balancing novelty (expanding the frontier) with the resolution of state ambiguity.

---

## 性能与结果

*   **规模**：该系统成功处理了来自 11 个不同桌面应用程序的超过 100 万张截图和 30,000 个去重状态。
*   **洞察**：作者发现，更强的提案先验（proposal priors）能够显著提升对独特状态的发现能力。研究结果强调，状态同一性、动作提案的质量以及智能探测策略，都是构建强大桌面 GUI 自动化的必不可少的核心组件。

> ## Performance & Results
> *   **Scale:** The system successfully processed over 1 million screenshots and 30,000 deduplicated states across 11 distinct desktop applications.
> *   **Insights:** The authors found that stronger proposal priors significantly improve the discovery of unique states. The results highlight that state identity, the quality of action proposals, and intelligent probing strategies are all essential components for robust desktop GUI automation.

---

## 元数据

*   **评论**：22 页，8 张图表，21 个表格
*   **DOI**：[https://doi.org/10.48550/arXiv.2605.16024](https://doi.org/10.48550/arXiv.2605.16024)
*   **全文访问**：[PDF](https://arxiv.org/pdf/2605.16024) | [HTML (实验性)](https://arxiv.org/html/2605.16024v2) | [TeX 源码](https://arxiv.org/src/2605.16024)

> ## Metadata
> *   **Comments:** 22 pages, 8 figures, 21 tables
> *   **DOI:** [https://doi.org/10.48550/arXiv.2605.16024](https://doi.org/10.48550/arXiv.2605.16024)
> *   **Full-Text Access:** [PDF](https://arxiv.org/pdf/2605.16024) | [HTML (Experimental)](https://arxiv.org/html/2605.16024v2) | [TeX Source](https://arxiv.org/src/2605.16024)