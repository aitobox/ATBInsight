---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 大语言模型
- 深度强化学习
- 认知行为疗法
- 心理咨询智能体
- 对话系统
title: DeepSAGE：用于结构化CBT咨询对话的阶段感知强化学习
---
### 文章背景与核心概要
尽管基于大语言模型（LLM）的心理咨询智能体在生成流利且富有支持性的文本方面表现出色，但它们往往缺乏连贯治疗所需的结构化、目标导向的发展进程。为了解决这一痛点，DeepSAGE（战略人工智能引导引擎）提出了一种混合了LLM与深度强化学习（DRL）的框架，专门用于基于认知行为疗法（CBT）初次会诊的阶段感知咨询对话。

DeepSAGE 将治疗过程细分为具有明确目标的十一个离散阶段，利用外部控制器来判断阶段的完成情况，同时通过 DRL 模型选择治疗意图，进而指导LLM生成响应。评估结果表明，该系统能够显著提升来访者的参与度和开放性，并在目标完成度与对话效率之间取得最佳平衡，不过未来仍需进行更深入的临床与安全性验证。

---

## 📋 Summary
> While Large Language Model (LLM)-based counseling agents excel at generating fluent and supportive text, they frequently lack the structured, goal-directed progression necessary for a coherent therapeutic session. To address this, **DeepSAGE** (Strategic AI Guidance Engine) introduces a hybrid LLM and Deep Reinforcement Learning (DRL) framework tailored for stage-aware counseling dialogue, specifically grounded in the first session of Cognitive Behavioral Therapy (CBT). 
> 
> By breaking down a therapy session into eleven discrete stages with explicit objectives, DeepSAGE utilizes an external controller to determine stage completion, while a DRL model selects therapeutic intentions to guide LLM response generation. Evaluations demonstrate superior client engagement, openness, and an optimal balance of goal completion and dialogue efficiency, though further clinical and safety validations remain necessary.

---

## 📌 Metadata
> * **arXiv ID:** [arXiv:2608.22615](https://arxiv.org/abs/2608.22615) [cs.AI]
> * **Submission Date:** August 23, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Qi Zhang
>   * Heajun An
>   * Prakriti Dumaru
>   * Sang Won Lee
>   * Lifu Huang
>   * Pamela J. Wisniewski
>   * Jin-Hee Cho

---

## 📝 Abstract
大语言模型（LLM）驱动的咨询智能体能够生成流利且富有支持性的回复，但它们通常缺乏进行连贯治疗所需的结构化、目标导向的发展进程。我们提出了 DeepSAGE（战略人工智能引导引擎），这是一个结合了 LLM 与深度强化学习（DRL）的混合框架，专为基于认知行为疗法（CBT）初次会诊的阶段感知咨询对话而设计。

> Large Language Model (LLM)-based counseling agents can generate fluent and supportive responses, but they often lack the structured, goal-directed progression required to conduct a coherent therapeutic session. We present DeepSAGE (Strategic AI Guidance Engine), a hybrid LLM–Deep Reinforcement Learning (DRL) framework for stage-aware counseling dialogue grounded in the first session of Cognitive Behavioral Therapy (CBT). 

DeepSAGE 将治疗会话表示为具有明确治疗目标的十1个阶段，其中外部控制器决定阶段的完成情况，而 DRL 模型则选择指导 LLM 回复生成的治疗意图。我们将 DeepSAGE 与六种基于检索、提示、阶段和策略的替代方案进行了评估。在阶段结构化系统中，DeepSAGE 能够激发模拟来访者更高的参与度和开放性，并实现了阶段目标完成度与对话效率的最强平衡。

> DeepSAGE represents the session as eleven stages with explicit therapeutic objectives, with an external controller determines stage completion and the DRL model selects therapeutic intentions that guide LLM response generation. We evaluate DeepSAGE against six retrieval-, prompting-, stage-, and policy-based alternatives. DeepSAGE elicits higher simulated client engagement and openness and achieves the strongest balance of stage-goal completion and dialogue efficiency among stage-structured systems. 

领域专家的评审进一步表明，生成的对话表现出大体合理的审视轨迹和可识别的 CBT 过程。由于评估主要依赖于模拟来访者和基于模型的指标，这些发现证明的是对话控制方面的相对改进，而非临床有效性。这些结果表明，将阶段结构化对话与学习到的策略选择相结合是 AI 咨询的一种有前景的方法，尽管临床有效性、安全性和实际应用价值仍需要进一步的人工评估。

> Domain expert review further indicates that the generated conversations exhibit broadly plausible emotional trajectories and recognizable CBT processes. Because the evaluation relies primarily on simulated clients and model-based metrics, these findings demonstrate comparative dialogue-control improvements rather than clinical effectiveness. These results suggest that combining stage-structured dialogue with learned strategy selection is a promising approach for AI counseling, though clinical effectiveness, safety, and real-world utility require further human evaluation.

---

## 🔗 Links & Resources
> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2608.22615)
>   * [HTML (Experimental)](https://arxiv.org/html/2608.22615v1)
>   * [TeX Source](https://arxiv.org/src/2608.22615)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
> * **External Citations:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22615)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22615)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22615)

---

*(License Icon Reference)*
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">