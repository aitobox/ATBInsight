---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 多模态智能体
- 3D生成
- 强化学习
- 3D视觉
- VibeWorlding
title: VibeWorlding：多模态智能体能否端到端构建3D开放世界？
---
### 文章背景与核心概要
构建沉浸式、互动的3D开放世界一直是人工智能和计算机图形学领域的核心目标之一。然而，现有的方法大多局限于处理简单、理想化的提示词，难以系统地评估和训练多模态智能体在多轮交互中理解用户意图、规划场景布局以及调用3D工具的能力。为了解决这一痛点，本文提出了 **VibeWorlding** 统一框架，旨在对能够根据自然语言和视觉查询自主构建3D世界的智能体进行基准测试与训练。

本文的核心贡献主要包含三个方面：一是推出了包含2,616个高质量3D资产、323个种子世界以及6,828个多模态用户查询的综合基准 **VWE-BENCH**；二是开发了联合多模态强化学习（RL）后训练框架 **VibeWorlding-Gym**，集成了基于MCP工具的沙盒环境和基于评分标准的验证器；三是训练并开源了 **VibeWorlder** 系列模型，其实验结果表明，强化学习后训练能够有效突破开源多模态大模型在精确3D世界编辑上的瓶颈，旗舰模型 *VibeWorlder-30B-A3B* 甚至在 Pass@1 性能上超越了现有的闭源前沿模型。

---

# VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?

**Authors:** Yansong Ning, Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang, Hao Liu  
**Subjects:** Artificial Intelligence (cs.AI)  
**ArXiv ID:** [arXiv:2608.15265 [cs.AI]](https://arxiv.org/abs/2608.15265)  
**Submitted:** August 15, 2026 (Last revised August 19, 2026)  

---

## 📌 Summary

> **VibeWorlding** introduces a unified framework to benchmark and train multimodal agents capable of autonomously constructing interactive 3D open worlds from natural language and visual queries. While existing methods are typically evaluated on simplistic, idealized prompts, this paper addresses the challenge of multi-turn agent interactions—where models must interpret user intent, plan scene layouts, invoke 3D tools, and adapt based on multimodal feedback. 
> 
> To achieve this, the authors present:
> 1. **VWE-BENCH**: A comprehensive benchmark featuring 2,616 high-quality 3D assets, 323 human-annotated seed worlds, and 6,828 reverse-synthesized multimodal user queries.
> 2. **VibeWorlding-Gym**: A joint multimodal Reinforcement Learning (RL) post-training framework combining a unified sandbox environment (using Model Context Protocol tools) and a rubric-based verifier.
> 3. **New Models (`VibeWorlder`)**: Demonstrating that RL post-training allows open-source Multimodal Large Language Models (MLLMs) to overcome current bottlenecks in precise 3D world editing, with the flagship *VibeWorlder-30B-A3B* surpassing even closed-source frontier models in Pass@1 performance.

---

## 📝 Abstract

> Constructing an interactive 3D open world from a user query is important. However, existing methods are primarily evaluated on idealized, simple queries, making it difficult to systematically analyze and compare how multimodal agents understand user intent, use 3D tools, and reason over textual and visual 3D world information. To this end, we propose **VibeWorlding**, a unified framework for benchmarking and training vibe worlding agents: a multimodal agent that can autonomously infer user intent, plan scene layout, invoke 3D tools, and reflect on the multimodal feedback in a multi-turn agent-environment interaction process. 
> 
> To achieve this, we first build **VWE-BENCH**, a benchmark of 2,616 high-quality 3D assets, 323 human-annotated seed 3D worlds, and 6,828 reverse-synthesized multimodal user queries, split into verified queries with ground-truth and unverified queries with carefully designed rubrics. Moreover, we develop **VibeWorlding-Gym**, a joint multimodal RL post-training framework that integrates (1) a sandbox environment unifying asset retrieval, editing, and image rendering as MCP tools, and (2) a rubric-based verifier that combines physical feasibility and intent fulfillment verification, supporting both fair model evaluation and scalable multimodal RL reward service. 
> 
> Our experiments show that current frontier MLLMs are far from solving the vibe worlding agent task, with even GPT-5.5 and Qwen3.8-Max reaching below 60% success rate, and trace the bottleneck to precise 3D world editing. We further find that RL training can ease this weakness and enable open-source MLLMs to even surpass closed-source frontiers: our VibeWorlder-8B is comparable to frontier MLLMs, while our flagship **VibeWorlder-30B-A3B** attains the best overall Pass@1 among all evaluated models.

从用户查询出发构建交互式的3D开放世界至关重要。然而，现有方法的评估主要基于理想化、简单的查询，这使得系统化分析和比较多模态智能体如何理解用户意图、使用3D工具以及对文本与视觉3D世界信息进行推理变得十分困难。为此，我们提出了 **VibeWorlding**，这是一个用于基准测试和训练氛围世界构建智能体（vibe worlding agents）的统一框架：该多模态智能体能够在多轮智能体-环境交互过程中，自主推断用户意图、规划场景布局、调用3D工具，并对多模态反馈进行反思。

为了实现这一目标，我们首先构建了 **VWE-BENCH**，这是一个包含2,616个高质量3D资产、323个经人工标注的种子3D世界以及6,828个逆向合成的多模态用户查询的基准。该基准分为带有真实真值的已验证查询和采用精心设计评分标准（rubrics）的未验证查询。此外，我们开发了 **VibeWorlding-Gym**，这是一个联合的多模态强化学习（RL）后训练框架，它集成了（1）将资产检索、编辑和图像渲染统一为MCP工具的沙盒环境，以及（2）结合了物理可行性和意图满足度验证的基于评分标准的验证器，从而同时支持公平的模型评估和可扩展的多模态RL奖励服务。

我们的实验表明，当前的前沿多模态大模型（MLLM）距离解决氛围世界构建智能体任务还很遥远，即便是 GPT-5.5 和 Qwen3.8-Max 的成功率也低于 60%，并且瓶颈主要在于精确的3D世界编辑。我们进一步发现，RL训练可以缓解这一弱点，并使开源MLLM甚至能够超越闭源前沿模型：我们的 VibeWorlder-8B 与前沿MLLM表现相当，而我们的旗舰模型 **VibeWorlder-30B-A3B** 在所有评估模型中取得了最佳的整体 Pass@1 成绩。

---

## 🔗 Quick Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.15265) | [HTML (Experimental)](https://arxiv.org/html/2608.15265v2) | [TeX Source](https://arxiv.org/src/2608.15265)
* **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15265) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15265) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15265)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) *(View License icon below)*  
  <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="height: 20px; vertical-align: middle;"></a>