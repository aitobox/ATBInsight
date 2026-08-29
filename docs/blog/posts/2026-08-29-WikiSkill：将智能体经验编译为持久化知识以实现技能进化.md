---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- AI Agent
- 技能进化
- 知识库
- 模型扩展
- 跨模型迁移
title: WikiSkill：将智能体经验编译为持久化知识以实现技能进化
---
### 文章背景与核心概要
随着人工智能大模型在复杂交互任务中的广泛应用，如何让智能体（AI Agent）通过历史经验自主学习和进化成为了研究热点。传统的技能进化方法通常将优化过程中的宝贵洞察散落在庞大且杂乱的原始执行历史中，导致这些经验无法被系统性地重复利用。为了解决这一痛点，本文介绍了创新框架 **WikiSkill**。

WikiSkill 的核心思想是通过清晰地区分“原始执行经验”、“累积知识库（Wiki）”和“可执行技能”，实现可执行技能与持久化知识库的协同进化。在运行过程中，框架持续将零散的执行经验提炼并内化到 Wiki 中，为后续的技能更新打下坚实基础。实验结果表明，WikiSkill 在多个基准测试和模型上均显著超越了现有的最先进方法，展现出极高的跨模型迁移能力和与模型规模扩展的协同效应。

---

## Summary

> **WikiSkill** is an innovative framework designed to enhance AI agent capabilities by co-evolving executable agent skills with a persistent knowledge base (wiki). Traditional skill-evolution methods often scatter optimization insights across raw execution histories, preventing systematic reuse. WikiSkill addresses this by clearly separating raw execution experience, accumulated knowledge, and executable skills. 
> 
> Key findings from the paper include:
> * **Superior Performance:** WikiSkill consistently outperforms state-of-the-art skill-evolution baselines across diverse benchmarks and models.
> * **Model Scaling Synergy:** Skill evolution complements model scaling—larger models leverage evolved skills more effectively, while smaller models equipped with WikiSkill can outperform significantly larger models that lack them.
> * **Cross-Model Transferability:** Evolved skills transfer seamlessly across models and model families, and skills evolved by other models can even surpass self-evolved skills.
> * **Persistent Knowledge Value:** Ablation studies confirm that continuous knowledge consolidation in the wiki is crucial for effective skill development.

---

## Paper Metadata

> * **arXiv ID:** `arXiv:2608.27454` [cs.AI]
> * **Subject Areas:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
> * **Submission Date:** August 27, 2026
> * **Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
> * **DOI:** [10.48550/arXiv.2608.27454](https://doi.org/10.48550/arXiv.2608.27454)

---

## Abstract

> Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. 
> 
> We introduce **WikiSkill**, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill development. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

---

## Resources & Links

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.27454) | [HTML Version](https://arxiv.org/html/2608.27454v1) | [TeX Source](https://arxiv.org/src/2608.27454)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> * **External Bibliographic Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27454)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27454)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27454)