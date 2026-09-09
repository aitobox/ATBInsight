---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 计算机视觉
- 第一视角视频
- 具身智能
- 大模型
- 视觉基础监督
title: Ambient @ EgoProactive 2026：基于视觉基础监督的主动式第一视角辅助系统
---
### 文章背景与核心概要

本文介绍了 ECCV 2026 可穿戴 AI 大挑战赛（Wearable AI Grand Challenge）中 EgoProactive 赛道的夺冠技术报告。该方案在大型模型组（large-model division）中斩获第一名，在 $\le 2\text{B}$ 参数量组中获得第二名。核心任务要求可穿戴助手在每八秒的第一视角视频片段后，判断是应该进行干预还是保持沉默。

该方法主要包含两项核心贡献：首先，通过重新归一化的 token 概率将干预时机预测转化为二分类任务，而非依赖自由文本生成，从而将宏平均 F1 值（macro-F1）提升了 0.249，G-mean 提升了 0.30；其次，提出使用工具调用视频代理（tool-calling video agent）生成补充训练数据，而非依赖规模更大的纯旁白文本语料库，这证明了对于主动式第一视角辅助任务而言，“视觉基础监督（visual grounding）”比单纯的“标注规模”更为重要。

---

# Ambient @ EgoProactive 2026: Proactive Egocentric Assistance with Visually Grounded Supervision

**arXiv:** [2609.07099](https://arxiv.org/abs/2609.07099) [cs.CV]  
**Submitted:** September 7, 2026  
**Authors:** Logesh Kumar Umapathi  
**Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)  

---

## 📌 Summary

> This paper presents the winning solution technical report for the **EgoProactive track of the ECCV 2026 Wearable AI Grand Challenge**. The submission ranked **first in the large-large-model division** and **second in the $\le 2\text{B}$ division**. 
>
> The core task requires a wearable assistant to determine—after each eight-second segment of egocentric video—whether to intervene or remain silent. The proposed approach introduces two main contributions:
> 1. **Single-Token Classification:** Reformulating intervention timing as a binary prediction task using renormalised token probabilities rather than free-form generation (improving macro-F1 by 0.249 and G-mean by 0.30).
> 2. **Visually Grounded Supervision:** Generating supplementary training data via a tool-calling video agent rather than relying on larger narration-only text corpora, highlighting that visual grounding outweighs annotation volume for proactive egocentric assistance.

---

## 📄 Abstract

> We present our submission to the EgoProactive track of the ECCV 2026 Wearable AI Challenge, which ranked first in the large-model division and second in the $\le 2\text{B}$ division. The task requires a wearable assistant to decide after each eight-second segment of egocentric video whether to intervene or remain silent.
>
> Our approach has two main components. First, we reformulate intervention timing as single-token classification. Rather than generating either $\text{interrupt}\langle\text{utterance}\rangle$ or $\text{silent}$, the model predicts yes or no, and we derive the decision from the renormalised probabilities of these two tokens. This formulation improved macro-F1 by 0.249 and G-mean by 0.30 over free-form generation. Second, because labelled data were limited to the released validation set, we generated additional supervision using a tool-calling video agent that inspects each clip and assigns intervention timestamps. A narration-only alternative was four times larger and ten times cheaper, but transferred worse than supervision from an unrelated real corpus, suggesting that visual grounding is more important than annotation volume for this task.

---

## 🔗 Links & Resources

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.07099) | [HTML (Experimental)](https://arxiv.org/html/2609.07099v1) | [TeX Source](https://arxiv.org/src/2609.07099)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.07099](https://doi.org/10.48550/arXiv.2609.07099)
> * **External Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.07099) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.07099) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.07099)
>
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="display:none;" />