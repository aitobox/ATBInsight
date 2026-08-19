---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 大语言模型
- 智能体安全
- 群体极化
- 记忆机制
- 社交网络
title: GraphWake：基于大模型智能体社区中记忆介导的极化级联效应引发群体极化
---
### 文章背景与核心概要

随着大语言模型（LLM）驱动的智能体开始自主交互并形成在线社区，社区层面的新型安全漏洞逐渐显现。本文提出了 **GraphWake** 框架，旨在揭示恶意行为者如何利用智能体的记忆机制在 LLM 智能体社区中诱导群体极化。

不同于以往依赖修改智能体提示词或构建孤立回声室等不切实际的方法，作者提出了一种名为“记忆介导的极化级联”（Memory-Mediated Polarization Cascade）的新型威胁模型。该模型利用智能体的记忆作为持久化渠道，以公共讨论作为传播媒介，通过结构化的三阶段操纵手段，在社区内引发广泛的极化效应。

---

## 📌 摘要

随着大语言模型（LLM）驱动的智能体自主交流并形成在线社区，新的社区级安全漏洞随之出现。本文介绍了 **GraphWake**，这是一个展示恶意行为者如何诱导 LLM 智能体社区内群体极化的框架。

作者没有依赖于修改智能体提示词或构建孤立回声室等不切实际的方法，而是制定了一种名为“记忆介导的极化级联”的新型威胁模型。该威胁利用智能体记忆作为持久化渠道，以公共话语作为传播渠道，通过结构化的三阶段操纵推动广泛的社区极化。

> As Large Language Model (LLM)-driven agents autonomously communicate and form online communities, new community-level security vulnerabilities emerge. This paper introduces **GraphWake**, a framework demonstrating how malicious actors can induce group polarization within LLM-agent communities. 
>
> Rather than relying on impractical methods like altering agent prompts or building isolated echo chambers, the authors formulate a novel threat model known as **Memory-Mediated Polarization Cascade**. This threat leverages agent memory as a persistence channel and public discourse as a propagation channel, driving widespread community polarization through structured three-stage manipulation.

---

## 🛠️ 威胁模型：记忆介导的极化级联

所提出的威胁模型分为三个不同阶段：

1. **暴露与记忆留存：** 攻击者将一小部分目标智能体暴露于强化其既有立场的论点中。智能体的底层记忆系统会对这些论点进行处理并安全留存。
2. **检索与再现：** 一场共享的、立场中立的公共讨论作为提示线索，促使目标智能体检索并表达其记忆中存储的论点。
3. **迭代传播：** 社区内未受干预的智能体接触到这些被再现的论点，随后采纳、重述并进一步传播它们。

> The proposed threat model operates across three distinct stages:
>
> 1. **Exposure and Memory Retention:** 
>    The attacker exposes a small subset of target agents to arguments that reinforce their pre-existing stances. The agents' underlying memory systems process and securely retain these arguments.
> 2. **Retrieval and Reproduction:** 
>    A shared, stance-neutral public discussion acts as a cue, prompting the targeted agents to retrieve and articulate the arguments stored in their memory.
> 3. **Iterative Propagation:** 
>    Untreated agents within the community are exposed to these reproduced arguments, subsequently adopting, restating, and spreading them further.

---

## ⚙️ GraphWake 的核心组件

GraphWake 通过三个技术组件实现了这一威胁模型：

* **立场支持论证知识图谱：** 构建结构化的、基于知识的论点，旨在强化特定观点。
* **面向公理的三元组选择：** 对构建的知识图谱进行提炼，以确保目标智能体记忆系统能够可靠地留存和再现这些内容。
* **立场中立的记忆提示：** 在中立讨论中触发极化论点的并发检索与再现，从而启动更大规模的传播级联。

> GraphWake instantiates this threat model via three technical components:
>
> * **Stance-Support Argumentation Knowledge Graphs:** Constructs structured, knowledge-based arguments tailored to reinforce specific viewpoints.
> * **Axiom-Oriented Triple Selection:** Distills the constructed knowledge graphs to ensure reliable retention and reproduction by the target agents' memory systems.
> * **Stance-Neutral Memory Cueing:** Triggers concurrent retrieval and reproduction of polarized arguments during neutral discussions, initiating the broader propagation cascade.

---

## 📈 主要发现

在多个讨论主题和不同记忆架构下的实验结果表明，**GraphWake 显著增加了群体极化**。这些发现凸显了去中心化 LLM 智能体生态系统中固有的重大社区级安全和极化风险。

> Experimental results across multiple discussion topics and diverse memory architectures demonstrate that **GraphWake substantially increases group polarization**. These findings highlight significant community-level security and polarization risks inherent in decentralized LLM-agent ecosystems.

---

## 🔗 链接与资源

* [查看 PDF](https://arxiv.org/pdf/2608.17665)
* [TeX 源码](https://arxiv.org/src/2608.17665)
* [DOI (DataCite)](https://doi.org/10.48550/arXiv.2608.17665)

> * [View PDF](https://arxiv.org/pdf/2608.17665)
> * [TeX Source](https://arxiv.org/src/2608.17665)
> * [DOI (DataCite)](https://doi.org/10.48550/arXiv.2608.17665)