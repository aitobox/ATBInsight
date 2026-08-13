---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 阿拉伯音乐
- 木卡姆
- 实时生成式音乐
- 提示词工程
- 人机协作
title: MazzikaAI：用于实时阿拉伯木卡姆即兴伴奏的基于知识的演奏到提示词编译器
---
### 文章背景与核心概要
阿拉伯木卡姆（Maqam）音乐以其独特的微音程、调式及丰富的装饰音呼应为特征，然而现有的生成式音乐模型大多基于西方十二平均律训练，难以精准呈现这种复杂的非西方传统音乐。为了解决这一痛点，本文提出了 MazzikaAI 系统。该系统创新性地采用了一种基于知识的“演奏到提示词”（performance-to-prompt）编译器，充当实时智能中介。

MazzikaAI 能够将现场输入的 MIDI、手势信号以及和声上下文，实时编译为动态的文本提示词，从而在无需微调底层 AI 模型的前提下，精准引导 Google Lyria RealTime 模型生成具备文化真实感的伴奏。系统内置了针对六种核心木卡姆调式、特色装饰音及合奏动态的专家知识，在保持亚秒级低延迟响应的同时，显著提升了生成音频中的四分之一音（微音程）含量。这项研究不仅为多元文化的实时人机共创提供了可扩展的范式，也为互动伴奏、自适应音乐教育及全球多样化音乐生成开辟了新途径。

---

# MazzikaAI: A Knowledge-Based Performance-to-Prompt Compiler for Real-Time Arabic Maqam Accompaniment

> # MazzikaAI: A Knowledge-Based Performance-to-Prompt Compiler for Real-Time Arabic Maqam Accompaniment

**Authors:** Jiaxin Du, Boulbaba Abdeljaouad, Yong Zhuang, Haoyu Li  
**Date:** August 11, 2026  
**Subject:** Human-Computer Interaction (cs.HC); Artificial Intelligence (cs.AI); Audio and Speech Processing (eess.AS)  
**Identifier:** [arXiv:2608.10360](https://arxiv.org/abs/2608.10360)

> **Authors:** Jiaxin Du, Boulbaba Abdeljaouad, Yong Zhuang, Haoyu Li  
> **Date:** August 11, 2026  
> **Subject:** Human-Computer Interaction (cs.HC); Artificial Intelligence (cs.AI); Audio and Speech Processing (eess.AS)  
> **Identifier:** [arXiv:2608.10360](https://arxiv.org/abs/2608.10360)

---

## Summary

> ## Summary

**MazzikaAI** 是一个创新系统，旨在弥合以西方为中心的生成式音乐模型与阿拉伯木卡姆（*maqam*）音乐复杂微音程传统之间的鸿沟。通过利用基于知识的“演奏到提示词”编译器，该系统能够在无需对底层 AI 模型进行微调的情况下，实现实时、具有文化本真性的伴奏。该系统充当智能中介，将现场 MIDI、手势和和声背景转化为 Google Lyria RealTime 模型的动态文本提示词，确保了亚秒级的延迟和高音乐保真度。

> **MazzikaAI** is an innovative system designed to bridge the gap between Western-centric generative music models and the complex, microtonal traditions of Arabic *maqam* music. By utilizing a knowledge-based "performance-to-prompt" compiler, the system enables real-time, culturally authentic accompaniment without requiring the underlying AI model to be fine-tuned. The system acts as an intelligent intermediary, translating live MIDI, gestures, and harmonic context into dynamic text prompts for the Google Lyria RealTime model, ensuring sub-second latency and high musical fidelity.

---

## Abstract

阿拉伯木卡姆（*maqam*）音乐以微音程、调式化以及富有装饰音的呼应（call-and-response）性质为特征，是生成式音乐模型最缺乏服务的传统之一——其训练框架主要基于西方十二平均律。实时伴奏凸显了这一差距：AI 伙伴必须能够倾听、动态适应并尊重习语般的微音程结构。

流式文本转音乐模型提供了强大的生成能力，但缺乏精确的控制接口。我们提出了 **MazzikaAI**，这是一个基于知识的系统，它将自然语言用作实时控制循环的执行机构。通过将现场 MIDI、手势和推断的和声编译为持续更新的文本提示词，MazzikaAI 在无需模型微调的情况下，驱动了一个未加修改的流式生成器 *Google Lyria RealTime*。

该系统嵌入了对六个核心木卡姆（*maqamat*）、特征装饰音和合奏动态的专家知识，保持了实时的响应能力以及从按键到可听见更新的亚秒级延迟。实证评估表明，动态提示词编译可靠地将生成内容锚定在微音程音阶中，显著增加了脱离网格（off-grid）的四分之一音含量。除了核心实现外，MazzikaAI 还阐明了确定性基于知识的规则如何有效地弥合专家级非西方音乐传统与未微调的基础模型之间的鸿沟。该架构为实时人机共创建立了一个可扩展的范式，为全球不同地方音乐流派中的互动伴奏、自适应音乐教育和文化包容性生成音频提供了可推广的蓝图。

> Arabic *maqam* music—characterized by its microtonal, modal, and ornamented call-and-response nature—is among the traditions most underserved by generative music models, whose training frameworks remain predominantly Western and equal-tempered. Real-time accompaniment sharpens this gap: an AI partner must listen, adapt dynamically, and respect idiomatic microtonal structures. 
> 
> Streaming text-to-music models provide strong generative capabilities but lack precise control interfaces. We present **MazzikaAI**, a knowledge-based system that uses natural language as the actuator of a real-time control loop. By compiling live MIDI, gesture, and inferred harmony into continuously updated text prompts, MazzikaAI steers an unmodified streaming generator, *Google Lyria RealTime*, without requiring model fine-tuning. 
> 
> The system embeds expert knowledge of six core *maqamat*, characteristic ornaments, and ensemble dynamics, maintaining real-time responsiveness with sub-second key-to-audible-update latency. Empirical evaluations demonstrate that dynamic prompt compilation reliably grounds generation in microtonal scales, significantly increasing off-grid quartertone content over baseline generation. Beyond its core implementation, MazzikaAI illustrates how deterministic knowledge-based rules can effectively bridge expert, non-Western musical traditions and un-fine-tuned foundation models. This architecture establishes a scalable paradigm for real-time human-AI co-creation, offering a generalizable blueprint for interactive accompaniment, adaptive music education, and culturally inclusive generative audio across diverse global idioms.

---

## Access & Resources

*   **[查看 PDF](https://arxiv.org/pdf/2608.10360)**
*   **[HTML（实验性）](https://arxiv.org/html/2608.10360v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.10360)**
*   **DOI:** [10.48550/arXiv.2608.10360](https://doi.org/10.48550/arXiv.2608.10360)

> *   **[View PDF](https://arxiv.org/pdf/2608.10360)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.10360v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.10360)**
> *   **DOI:** [10.48550/arXiv.2608.10360](https://doi.org/10.48550/arXiv.2608.10360)

---

## Citation

如果您使用了这项工作，请通过以下标识符引用：
*   **arXiv:** 2608.10360 [cs.HC]

> If you use this work, please refer to it via the following identifier:
> *   **arXiv:** 2608.10360 [cs.HC]