---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 多智能体系统
- 医疗AI
- 卒中评估
- 人机交互
- 院前急救
title: StrokeGuard：用于院前卒中评估的多智能体引导系统
---
### 文章背景与核心概要
卒中（中风）具有极高的致残率和致死率，院前的快速准确评估对于争取黄金救治时间至关重要。尽管基于FAST（面部、手臂、言语、时间）的临床筛查标准已被广泛采用，但在家庭或社区等非临床场景中，普通用户往往难以准确描述症状并遵循复杂的评估流程。

为了解决这一痛点，本文介绍了 StrokeGuard——一个旨在规范并提高院前卒中评估准确性的创新型多智能体系统。该系统通过引入“双通道智能体机制”，将正式的临床症状评估与流程支持（如实时反馈和纠错）进行解耦。借助多智能体协作、状态机控制以及阶段局部回退恢复机制，StrokeGuard 具备极高的流程容错能力。基于 MATES-9 量表的实际用户评估表明，与传统的纸质表单相比，该系统使用户体验得分实现了 23.8% 的相对提升。

---

# StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment

**Authors:** Wentao Yang, Zhenye Xu, Ruoyi Li, Musen Zhang, Yao Guo  
**Date:** August 25, 2026  
**Subject:** Human-Computer Interaction (cs.HC); Artificial Intelligence (cs.AI); Multiagent Systems (cs.MA)  
**Cite as:** [arXiv:2608.24555](https://arxiv.org/abs/2608.24555)

---

## Summary

**StrokeGuard** 是一个创新的多智能体系统，旨在规范和提高院前卒中评估的准确性。虽然基于临床的 FAST（面部、手臂、言语、时间）筛查是标准做法，但在家庭或社区环境中的非临床用户往往难以提供准确的症状描述，也难以应对复杂的程序要求。

> **StrokeGuard** is an innovative multi-agent system designed to standardize and improve the accuracy of prehospital stroke assessments. While clinical FAST-based (Face, Arm, Speech, Time) screenings are standard, non-clinical users in home or community settings often struggle with inaccurate symptom descriptions and complex procedural requirements. 

StrokeGuard 通过利用**双通道智能体机制**（将正式的临床评估与程序支持（如实时反馈和纠错）分离开来）解决了这些空白。通过采用多智能体协作、状态机控制和阶段局部回退恢复，该系统确保了极高的程序容错能力。使用 **MATES-9** 量表的用户评估表明，StrokeGuard 显着优于传统的纸质表单，使用户体验得分实现了 23.8% 的相对增长。

> StrokeGuard addresses these gaps by utilizing a **dual-channel agent mechanism** that separates formal clinical assessment from procedural support (such as real-time feedback and error correction). By employing multi-agent collaboration, state-machine control, and stage-local fallback recovery, the system ensures high procedural fault tolerance. User evaluations using the **MATES-9** scale demonstrated that StrokeGuard significantly outperforms traditional paper-based forms, achieving a 23.8% relative increase in user experience scores.

---

## Key Features

*   **双通道交互：** 将症状评估（面瘫、手臂无力、言语障碍）与程序指导（分步提示和纠错）解耦。
    > **Dual-Channel Interaction:** Decouples the assessment of symptoms (facial palsy, arm weakness, speech impairment) from the procedural guidance (step-by-step prompts and error correction).
*   **智能控制：** 利用状态机控制和阶段局部回退机制，即使在用户遇到困难时也能保持连续性。
    > **Intelligent Control:** Utilizes state-machine control and stage-local fallback mechanisms to maintain continuity even when users encounter difficulties.
*   **自动报告：** 通过受限的预训练视频评估模块，将特定阶段的评分与结构化报告生成相结合。
    > **Automated Reporting:** Integrates stage-specific scoring via constrained pretrained video assessment modules with structured report generation.
*   **经过验证的功效：** 在模拟院前场景中，与标准方法相比，该系统在 MATES-9 量表上的用户表现和体验提高了 10.83 分。
    > **Proven Efficacy:** In simulated prehospital scenarios, the system improved user performance and experience by 10.83 points on the MATES-9 scale compared to standard methods.

---

## Accessing the Paper

*   **[View PDF](https://arxiv.org/pdf/2608.24555)**
*   **[HTML (Experimental)](https://arxiv.org/html/2608.24555v1)**
*   **[TeX Source](https://arxiv.org/src/2608.24555)**

---

## Metadata & Citations

*   **DOI:** [10.48550/arXiv.2608.24555](https://doi.org/10.48550/arXiv.2608.24555)
*   **References:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.24555) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.24555) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.24555)