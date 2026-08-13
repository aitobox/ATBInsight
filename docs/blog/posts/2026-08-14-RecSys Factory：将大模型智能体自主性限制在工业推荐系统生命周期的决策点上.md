---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 推荐系统
- 大模型智能体
- 工业应用
- 腾讯
- 系统架构
title: RecSys Factory：将大模型智能体自主性限制在工业推荐系统生命周期的决策点上
---
### 文章背景与核心概要
将大模型（LLM）智能体部署到工业级推荐系统中，会暴露出一个核心的运营冲突，即所谓的**“自主性-确定性-效率”三难困境（autonomy-determinism-efficiency trilemma）**。要在保持端到端高效率和工业级确定性的同时平衡通用的智能体自主性，是极其困难的。

为了解决这一问题，作者推出了 **RecSys Factory**，这是一个在腾讯三个异构推荐业务线上部署了 78 天的 LLM 智能体平台。该平台的核心设计原则是**“在决策点上实现自主，而非掌控整个流水线（Autonomy at decision points, not over pipelines）”**。通过对运行时、能力和人机回环工作流进行解构，RecSys Factory 成功管理了复杂的推荐流水线，同时维持了极高的确定性和效率标准。

---

# RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industrial Recommender Lifecycle

**arXiv ID:** [arXiv:2608.11241](https://arxiv.org/abs/2608.11241) [cs.AI]  
**Authors:** Dongyang Ao, Kaixiang Fang, Shijie Xu  
**Submitted:** July 31, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**Secondary Subjects:** Information Retrieval (`cs.IR`)  
**ACM Classes:** H.3.3; I.2.11; D.2.11  

> **arXiv ID:** [arXiv:2608.11241](https://arxiv.org/abs/2608.11241) [cs.AI]  
> **Authors:** Dongyang Ao, Kaixiang Fang, Shijie Xu  
> **Submitted:** July 31, 2026  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **Secondary Subjects:** Information Retrieval (`cs.IR`)  
> **ACM Classes:** H.3.3; I.2.11; D.2.11  

---

## 📋 Executive Summary

Deploying Large Language Model (LLM) agents into industrial recommender systems reveals a core operational conflict known as the **autonomy-determinism-efficiency trilemma**. Balancing general agent autonomy with industrial determinism and end-to-end efficiency is exceptionally difficult. 

To solve this, the authors introduce **RecSys Factory**, an LLM-agent platform deployed across three heterogeneous Tencent recommender business lines over a 78-day period. The platform's foundational design principle is **"autonomy at decision points, not over pipelines."** By deconstructing runtime, capabilities, and human-in-the-loop workflows, RecSys Factory successfully manages complex recommender pipelines while maintaining high standards of determinism and efficiency.

> ## 📋 Executive Summary
> 
> Deploying Large Language Model (LLM) agents into industrial recommender systems reveals a core operational conflict known as the **autonomy-determinism-efficiency trilemma**. Balancing general agent autonomy with industrial determinism and end-to-end efficiency is exceptionally difficult. 
> 
> To solve this, the authors introduce **RecSys Factory**, an LLM-agent platform deployed across three heterogeneous Tencent recommender business lines over a 78-day period. The platform's foundational design principle is **"autonomy at decision points, not over pipelines."** By deconstructing runtime, capabilities, and human-in-the-loop workflows, RecSys Factory successfully manages complex recommender pipelines while maintaining high standards of determinism and efficiency.

---

## 🛠️ Key Architectural Deconstructions

RecSys Factory addresses the trilemma by breaking down system requirements into three manageable pillars:

### 1. Runtime Deconstruction (Efficiency)
* **Event-Driven Architecture:** Emits events via three host sources (Claude Code Stop hooks, corporate-IM webhooks, and workflow scheduler APIs).
* **Resource Optimization:** The platform maintains **no long-running daemons** during wait phases, consuming zero CPU during the 94% of wall-clock time spent waiting on heavy Spark or GPU jobs.

### 2. Capability Deconstruction (Determinism)
* **Skill Ecosystem:** Utilizes a 29-file skill ecosystem containing 8,971 lines of code.
* **PitfallStore Integration:** Individual skill pitfall tables mechanically compile into a centralized 400-entry `PitfallStore`. 
* **Bounded Autonomy:** Confines agent decision-making exclusively to typed, safe decision surfaces inside pre-committed pipelines.

### 3. Human-in-the-Loop & Deployment (Safety & Governance)
* **Business Diversity:** Successfully deployed across three distinct business lines featuring disjoint label semantics, A/B testing layer topologies, and operator personas.
* **Audit Protocols:** Retains human oversight at critical diagnostic-versus-execution boundaries using a human-in-the-loop card protocol. This protocol functions as an audit-trail primitive that is schema-validated, idempotent, and fully replayable.

> ## 🛠️ Key Architectural Deconstructions
> 
> RecSys Factory addresses the trilemma by breaking down system requirements into three manageable pillars:
> 
> ### 1. Runtime Deconstruction (Efficiency)
> * **Event-Driven Architecture:** Emits events via three host sources (Claude Code Stop hooks, corporate-IM webhooks, and workflow scheduler APIs).
> * **Resource Optimization:** The platform maintains **no long-running daemons** during wait phases, consuming zero CPU during the 94% of wall-clock time spent waiting on heavy Spark or GPU jobs.
> 
> ### 2. Capability Deconstruction (Determinism)
> * **Skill Ecosystem:** Utilizes a 29-file skill ecosystem containing 8,971 lines of code.
> * **PitfallStore Integration:** Individual skill pitfall tables mechanically compile into a centralized 400-entry `PitfallStore`. 
> * **Bounded Autonomy:** Confines agent decision-making exclusively to typed, safe decision surfaces inside pre-committed pipelines.
> 
> ### 3. Human-in-the-Loop & Deployment (Safety & Governance)
> * **Business Diversity:** Successfully deployed across three distinct business lines featuring disjoint label semantics, A/B testing layer topologies, and operator personas.
> * **Audit Protocols:** Retains human oversight at critical diagnostic-versus-execution boundaries using a human-in-the-loop card protocol. This protocol functions as an audit-trail primitive that is schema-validated, idempotent, and fully replayable.

---

## 📊 Operational Metrics & Results

During its **78-day evaluation window** across three Tencent business lines, RecSys Factory achieved the following performance metrics:
* **Total CLI-Tool Dispatches:** 1,624 operations recorded.
* **Aggregate Success Rate:** 78.6%.
* **Pilot Scale:** Backed by an 8-day, 16-run diagnostic pilot.

> ## 📊 Operational Metrics & Results
> 
> During its **78-day evaluation window** across three Tencent business lines, RecSys Factory achieved the following performance metrics:
> * **Total CLI-Tool Dispatches:** 1,624 operations recorded.
> * **Aggregate Success Rate:** 78.6%.
> * **Pilot Scale:** Backed by an 8-day, 16-run diagnostic pilot.

---

## 🔗 Full-Text & Access Links

* **arXiv Abstract:** [https://arxiv.org/abs/2608.11241](https://arxiv.org/abs/2608.11241)
* **Direct PDF:** [Download PDF](https://arxiv.org/pdf/2608.11241)
* **Experimental HTML:** [arXiv HTML View](https://arxiv.org/html/2608.11241v1)
* **DOI:** [10.48550/arXiv.2608.11241](https://doi.org/10.48550/arXiv.2608.11241)

*(Companion Paper Note: This platform shares a substrate with **AutoResearch (P3b)**, which applies similar autonomous architectures to scientific research.)*

> ## 🔗 Full-Text & Access Links
> 
> * **arXiv Abstract:** [https://arxiv.org/abs/2608.11241](https://arxiv.org/abs/2608.11241)
> * **Direct PDF:** [Download PDF](https://arxiv.org/pdf/2608.11241)
> * **Experimental HTML:** [arXiv HTML View](https://arxiv.org/html/2608.11241v1)
> * **DOI:** [10.48550/arXiv.2608.11241](https://doi.org/10.48550/arXiv.2608.11241)
> 
> *(Companion Paper Note: This platform shares a substrate with **AutoResearch (P3b)**, which applies similar autonomous architectures to scientific research.)*