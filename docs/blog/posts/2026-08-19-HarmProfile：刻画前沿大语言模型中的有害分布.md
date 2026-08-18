---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 大模型安全
- HarmProfile
- 风险评估
- 基准测试
- AI对齐
title: HarmProfile：刻画前沿大语言模型中的有害分布
---
### 文章背景与核心概要
长期以来，传统的前沿大语言模型（LLM）安全评估通常将有害文本生成视为一种二元的攻击结果，而缺乏对其进行深度的细节研究。为了填补这一空白，本研究推出了 **HarmProfile**——一个以内容为中心的基准数据集，旨在捕获不同危害类别和模型家族中的模型失范行为。

该研究将模型产生的有害输出分布定义为模型级别的风险profile（风险画像）。研究表明，尽管前沿大语言模型表面上看起来非常安全，但其输出的有害性和多样性实际上会随着模型能力的增强而增长，这暴露出其对齐表象下潜藏的危险知识。

---

# HarmProfile: Characterizing Harmful Distributions in Frontier LLMs

## Summary
传统安全 evaluations of frontier Large Language Models (LLMs) often treat harmful generation as a binary attack outcome rather than an object of detailed study. **HarmProfile** addresses this gap by introducing a content-centric benchmark dataset that captures model misbehavior across a diverse range of harm categories and model families. By defining the resulting harmful-output distribution as a model-level risk profile, the research demonstrates that while frontier LLMs appear safe on the surface, both the harmfulness and diversity of their outputs grow with model capability, exposing underlying dangerous knowledge.

> Traditional safety evaluations of frontier Large Language Models (LLMs) often treat harmful generation as a binary attack outcome rather than an object of detailed study. **HarmProfile** addresses this gap by introducing a content-centric benchmark dataset that captures model misbehavior across a diverse range of harm categories and model families. By defining the resulting harmful-output distribution as a model-level risk profile, the research demonstrates that while frontier LLMs appear safe on the surface, both the harmfulness and diversity of their outputs grow with model capability, exposing underlying dangerous knowledge.

---

## Metadata
* **arXiv ID:** [arXiv:2608.14577](https://arxiv.org/abs/2608.14577) [cs.CL]
* **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)
* **Submission Date:** June 11, 2026
* **Authors:** Zhouyuan Ma, Yutao Wu, Hanxun Huang, Xiang Zheng, Xiao Liu, Yixin Cao, Zuxuan Wu, Xingjun Ma, Yu-Gang Jiang

> * **arXiv ID:** [arXiv:2608.14577](https://arxiv.org/abs/2608.14577) [cs.CL]
> * **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)
> * **Submission Date:** June 11, 2026
> * **Authors:** Zhouyuan Ma, Yutao Wu, Hanxun Huang, Xiang Zheng, Xiao Liu, Yixin Cao, Zuxuan Wu, Xingjun Ma, Yu-Gang Jiang

---

## Abstract
前沿大语言模型（LLMs）的安全评估在很大程度上将有害生成视为一种攻击结果，而不是作为分析的对象。因此，人们对模型失范期间产生的有害输出知之甚少，部分原因是大规模、高质量的前沿大语言模型失范语料库很难获取。

> Frontier large language models (LLMs) safety evaluation has largely treated harmful generation as an attack outcome rather than as an object of analysis. Consequently, little is known about the harmful outputs produced during model misbehavior, partly because large-scale, high-quality collections of frontier-LLM misbehavior are difficult to obtain. 

为了填补这一空白，作者推出了 **HarmProfile**，这是一个以内容为中心的基准数据集，它收集了跨越不同危害类别和模型家族的模型失范行为，并将由此产生的有害输出分布定义为模型级别的风险画像。其前提是：正如可以从语句语料库中表征语言行为一样，模型的风险也可以从其安全失败的内容、严重程度和变化来表征。

> To address this gap, the authors introduce **HarmProfile**, a content-centric benchmark dataset that collects model misbehavior across diverse harm categories and model families, and defines the resulting harmful-output distribution as a model-level risk profile. The premise is that, just as linguistic behavior can be characterized from an utterance corpus, model risk can be characterized from the content, severity, and variation of its safety failures. 

### Key Findings & Dataset Scope / 核心发现与数据集范围
* **规模 (Scale)：** 包含来自 **23个前沿大模型**、跨越 **13个模型家族** 的超过 **80,000个经过验证的构件（artifacts）**。
* **分类体系 (Taxonomy)：** 划分为 **15个危害类别** 和 **57个子类别**。
* **核心洞察 (Key Insight)：** 前沿大语言模型能够在大规模下可靠地产生有害内容，同时表现出鲜明的风险画像。有害性和多样性均随着模型能力的提升而上升，这表明前沿大模型虽然表面上看起来安全，但在对齐表象下却隐藏着日益危险的知识。

> ### Key Findings & Dataset Scope
> * **Scale:** Contains over **80,000 validated artifacts** from **23 frontier LLMs** across **13 model families**.
> * **Taxonomy:** Organized into **15 harm categories** and **57 subcategories**.
> * **Key Insight:** Frontier LLMs reliably produce harmful content at scale while exhibiting distinct risk profiles. Both harmfulness and diversity scale upward with model capability, suggesting that frontier LLMs may appear safe yet harbor increasingly dangerous knowledge beneath the alignment surface.

---

## Links & Resources / 链接与资源
* **[查看 PDF (View PDF)](https://arxiv.org/pdf/2608.14577)**
* **[开源代码 (Source Code - GitHub)](https://github.com/fresh-ma/HarmProfile)**
* **[TeX 源码 (TeX Source)](https://arxiv.org/src/2608.14577)**

> ## Links & Resources
> * **[View PDF](https://arxiv.org/pdf/2608.14577)**
> * **[Source Code (GitHub)](https://github.com/fresh-ma/HarmProfile)**
> * **[TeX Source](https://arxiv.org/src/2608.14577)**