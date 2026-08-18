---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 强化学习
- 时间感知
- 基准测试
- 具身智能
- 人机交互
title: Chronocooked：强化学习智能体隐式区间计时基准测试
---
### 文章背景与核心概要
在当前的强化学习（RL）研究中，智能体往往在空间导航和模式识别方面表现出色，但却严重缺乏对时间维度的处理能力。为了填补这一空白，研究人员推出了 *Chronocooked* 这一全新基准测试套件。该环境灵感来源于热门游戏《胡闹厨房》（Overcooked），旨在评估智能体执行隐式区间计时（implicit interval timing）的能力。

该研究的核心在于模拟时间信息未被显式提供、但对实现最优性能至关重要的烹饪任务。通过保持环境的简洁性，研究人员能够进行可控实验，并支持开发出具有生物学似然性的模型。这项工作强调了提升人工智能时间感知能力的紧迫性，特别是对于需要在注重时效的人类社会中开展人机交互的智能体而言具有重要意义。

---

# Chronocooked: A Benchmark for Implicit Interval Timing in Reinforcement Learning Agents

**Authors:** Amrapali Pednekar, Alvaro Garrido-Perez, Yara Khaluf, Pieter Simoens  
**Date:** August 17, 2026  
**Subject:** Artificial Intelligence (cs.AI)  
**DOI:** [10.48550/arXiv.2608.16666](https://doi.org/10.48550/arXiv.2608.16666)

> **Authors:** Amrapali Pednekar, Alvaro Garrido-Perez, Yara Khaluf, Pieter Simoens  
> **Date:** August 17, 2026  
> **Subject:** Artificial Intelligence (cs.AI)  
> **DOI:** [10.48550/arXiv.2608.16666](https://doi.org/10.48550/arXiv.2608.16666)

---

## Summary
*Chronocooked* is a new reinforcement learning (RL) benchmark suite designed to evaluate the capacity of agents to perform **implicit interval timing**. Inspired by the popular *Overcooked* game, the environment presents cooking tasks where temporal awareness is not explicitly provided but is essential for achieving optimal performance. By keeping the environment simple, the researchers aim to facilitate controlled experiments and support the development of biologically plausible models. The study highlights the critical need for better time perception in AI, particularly for agents intended for human-robot interaction in time-sensitive societies.

> *Chronocooked* is a new reinforcement learning (RL) benchmark suite designed to evaluate the capacity of agents to perform **implicit interval timing**. Inspired by the popular *Overcooked* game, the environment presents cooking tasks where temporal awareness is not explicitly provided but is essential for achieving optimal performance. By keeping the environment simple, the researchers aim to facilitate controlled experiments and support the development of biologically plausible models. The study highlights the critical need for better time perception in AI, particularly for agents intended for human-robot interaction in time-sensitive societies.

---

## Research Overview
The benchmark addresses a significant gap in current RL research: the lack of focus on temporal processing. While many agents excel at spatial navigation or pattern recognition, they often struggle with tasks where success depends on "knowing when" to act rather than just "what" to do.

> The benchmark addresses a significant gap in current RL research: the lack of focus on temporal processing. While many agents excel at spatial navigation or pattern recognition, they often struggle with tasks where success depends on "knowing when" to act rather than just "what" to do.

### Key Features
*   **Temporal Decision Making:** Tasks are structured to require precise timing, even though temporal information is unobserved.
*   **Controlled Complexity:** The environment is intentionally simplified to allow for rigorous testing of different model architectures.
*   **Baseline Comparisons:** The paper provides performance baselines for three distinct model types:
    *   Non-recurrent models
    *   Recurrent models
    *   Biologically plausible models

> ### Key Features
> *   **Temporal Decision Making:** Tasks are structured to require precise timing, even though temporal information is unobserved.
> *   **Controlled Complexity:** The environment is intentionally simplified to allow for rigorous testing of different model architectures.
> *   **Baseline Comparisons:** The paper provides performance baselines for three distinct model types:
>     *   Non-recurrent models
>     *   Recurrent models
>     *   Biologically plausible models

### Motivation
As artificial agents are increasingly deployed in human-centric environments, the ability to process time—a fundamental aspect of human social interaction—becomes paramount. *Chronocooked* serves as a diagnostic tool to expose the limitations of current RL agents in this domain and encourages the integration of temporal processing mechanisms into future AI architectures.

> ### Motivation
> As artificial agents are increasingly deployed in human-centric environments, the ability to process time—a fundamental aspect of human social interaction—becomes paramount. *Chronocooked* serves as a diagnostic tool to expose the limitations of current RL agents in this domain and encourages the integration of temporal processing mechanisms into future AI architectures.

---

## Accessing the Paper
*   **[View PDF](https://arxiv.org/pdf/2608.16666)**
*   **[HTML (Experimental)](https://arxiv.org/html/2608.16666v1)**
*   **[TeX Source](https://arxiv.org/src/2608.16666)**

> ## Accessing the Paper
> *   **[View PDF](https://arxiv.org/pdf/2608.16666)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.16666v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.16666)**

---

## Citation & References
*   **Cite as:** arXiv:2608.16666 [cs.AI]
*   **External Links:**
    *   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.16666)
    *   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.16666)
    *   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.16666)

> ## Citation & References
> *   **Cite as:** arXiv:2608.16666 [cs.AI]
> *   **External Links:**
>     *   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.16666)
>     *   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.16666)
>     *   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.16666)