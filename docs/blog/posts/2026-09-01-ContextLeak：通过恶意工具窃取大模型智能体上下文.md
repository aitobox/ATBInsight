---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 大模型安全
- 智能体隐私
- 数据窃取
- 强化学习
- 攻击复现
title: ContextLeak：通过恶意工具窃取大模型智能体上下文
---
### 文章背景与核心概要
本文介绍了名为 **ContextLeak** 的前沿安全研究，聚焦于大语言模型（LLM）智能体（Agent）所面临的隐私与安全风险。随着大模型智能体被赋予越来越多的工具调用权限，用户的运行时上下文（如提示词、执行轨迹以及可用工具列表）极易成为攻击者的目标。现有研究多关注工具选择与数据传输通道，而本文则首次填补了“诱导智能体将敏感上下文作为恶意工具输入参数”这一关键技术空白。

研究团队创新性地引入强化学习（RL）技术，通过微调“攻击大模型”来自动生成具有欺骗性的工具名称与描述。实验证明，即使在模拟训练环境与真实受害者环境存在显著差异的情况下，该攻击方法依然表现出极高的有效性和泛化能力，远超现有的同类恶意工具攻击手段。

---

## ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

## Summary
> **ContextLeak** is a security research paper investigating privacy and security risks associated with Large Language Model (LLM) agents. Specifically, the paper highlights how malicious tools can be weaponized to exfiltrate a user's runtime context—such as user prompts, execution trajectories, and available tool lists. While prior work focuses on tool selection and data exfiltration channels, **ContextLeak** addresses the previously unexplored problem of inducing the agent to pass sensitive runtime context as input arguments to the malicious tool. 
> 
> The authors propose using reinforcement learning (RL) to fine-tune an "attack LLM" that automatically crafts deceptive tool names and descriptions. This approach is proven to be highly effective even when simulated training contexts differ substantially from real-world victim environments.

---

## Metadata

> * **arXiv ID:** [arXiv:2608.27800](https://arxiv.org/abs/2608.27800) [cs.CR]
> * **Subjects:** Cryptography and Security (`cs.CR`); Artificial Intelligence (`cs.AI`)
> * **Submission Date:** August 28, 2026
> * **DOI:** [10.48550/arXiv.2608.27800](https://doi.org/10.48550/arXiv.2608.27800)

### Authors
> * Yuqi Jia
> * Ruiqi Wang
> * Patrick Li
> * Yuepeng Hu
> * Peinian Li
> * Neil Gong

---

## Abstract

窃取大模型智能体的运行时上下文（例如用户提示词、执行轨迹和工具列表）会给用户带来严重的安全性与隐私风险。此类攻击可以通过恶意工具实施，通常需要满足三个条件：
1. 智能体选择该恶意工具来执行任务。
2. 智能体将其运行时上下文作为输入参数传递给该工具。
3. 工具的实现逻辑将这些输入传输至攻击者控制的端点。

现有研究主要集中在条件 (1) 和条件 (3) 上，而对条件 (2) 的研究却基本处于空白状态，尽管它在实现成功的上下文窃取中起着关键作用。

> Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: 
> 1. The agent selects the malicious tool for task execution.
> 2. The agent passes its runtime context as input arguments to the tool.
> 3. The tool's implementation transmits these inputs to an attacker-controlled endpoint. 
> 
> Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration.

在这项工作中，我们开发了 `ContextLeak` 这一恶意工具攻击方法，从而填补了这一空白。该方法能够诱导智能体同时选择该工具并泄露其上下文作为输入参数。我们通过精心设计工具的名称和描述来实现这一攻击，并利用强化学习技术。具体而言，ContextLeak 采用了一个大模型（称为攻击大模型）来自动生成恶意工具的名称和描述。为了提升攻击效果，我们在具有多样化模拟智能体上下文的一组影子用户（shadow users）上，通过强化学习对攻击大模型进行微调。我们核心的技术贡献在于设计了专门针对上下文窃取目标的全新奖励函数（reward functions），从而实现了基于强化学习的攻击大模型的高效微调。广泛的评估表明，即使影子用户的上下文与受害者的上下文存在显著差异，我们的攻击依然保持高度有效。此外，在适配到该场景时，ContextLeak 的表现显著优于现有的恶意工具攻击方法。

> In this work, we bridge this gap by developing `ContextLeak`, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

---

## Access & Resources

* **全文选项：** [查看 PDF](https://arxiv.org/pdf/2608.27800) | [HTML（实验性）](https://arxiv.org/html/2608.27800v1) | [TeX 源码](https://arxiv.org/src/2608.27800)
* **外部链接：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27800) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27800) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27800)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2608.27800) | [HTML (Experimental)](https://arxiv.org/html/2608.27800v1) | [TeX Source](https://arxiv.org/src/2608.27800)
> * **External Links:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27800) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27800) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27800)