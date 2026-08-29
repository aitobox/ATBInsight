---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 视频语言模型
- 幻觉缓解
- 反事实视频生成
- 直接偏好优化
- 计算机视觉
title: CounterVid：用于缓解视频-语言模型中动作与时间幻觉的反事实视频生成
---
### 文章背景与核心概要
视频-语言模型（VLMs）在多模态理解方面表现出色，但由于过度依赖语言先验而非细粒度视觉动态，经常在动作和时间顺序上产生幻觉。为了解决这一问题，**CounterVid** 提出了一种可扩展的反事实视频生成框架，能够合成语义困难负样本（即共享相同场景上下文但动作或时间结构不同的视频）。利用该方法，作者构建了一个包含约 2.6 万个偏好对的合成数据集，并开发了 **MixDPO**——一种融合了文本和视觉偏好的统一直接偏好优化（Direct Preference Optimization）技术。

将 MixDPO 应用于 Qwen2.5-VL 和 InternVL3 等主流主干网络后，模型在保持通用视频理解能力的同时，大幅提升了动作识别和时间排序的能力。该研究为解决多模态大模型的视觉幻觉问题提供了一条极具前景的新途径，对提升视频智能理解的可靠性具有重要意义。

---

## 📋 Summary
> Video-language models (VLMs) excel at multimodal understanding but frequently suffer from hallucinations regarding actions and temporal order due to an over-reliance on language priors rather than fine-grained visual dynamics. To tackle this, **CounterVid** introduces a scalable counterfactual video generation framework that synthesizes semantic hard negatives (videos sharing identical scene contexts but varying in specific actions or temporal structures). Using this approach, the authors constructed a synthetic dataset of ~26k preference pairs and developed **MixDPO**, a unified Direct Preference Optimization technique that merges textual and visual preferences. Applied to backbones like Qwen2.5-VL and InternVL3, MixDPO substantially improves action recognition and temporal ordering while preserving general video understanding capabilities.

---

## 📌 Metadata
> - **arXiv ID:** [arXiv:2601.04778](https://arxiv.org/abs/2601.04778) [cs.CV]
> - **Conference:** EMNLP 2026
> - **Subjects:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Multimedia (cs.MM)
> - **Submitted:** January 8, 2026 *(Last revised: August 27, 2026)*
> - **Authors:** Tobia Poppi, Burak Uzkent, Amanmeet Garg, Lucas Porto, Garin Kessler, Yezhou Yang, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara, Florian Schiffers

---

## 👥 Authors & Affiliations
> * Tobia Poppi
> * Burak Uzkent
> * Amanmeet Garg
> * Lucas Porto
> * Garin Kessler
> * Yezhou Yang
> * Marcella Cornia
> * Lorenzo Baraldi
> * Rita Cucchiara
> * Florian Schiffers

---

## 📄 Abstract
> Video-language models (VLMs) achieve strong multimodal understanding but remain prone to hallucinations, especially when reasoning about actions and temporal order. Existing mitigation strategies, such as textual filtering or random video perturbations, often fail to address the root cause: over-reliance on language priors rather than fine-grained visual dynamics. 

> We propose a scalable framework for counterfactual video generation that synthesizes videos differing only in actions or temporal structure while preserving scene context. Our pipeline combines multimodal LLMs for action proposal and editing guidance with diffusion-based image and video models to generate semantic hard negatives at scale. 

> Using this framework, we build **CounterVid**, a synthetic dataset of ~26k preference pairs constructed from short counterfactual action clips and targeting both action recognition and controlled action-sequence ordering. We further introduce **MixDPO**, a unified Direct Preference Optimization approach that jointly leverages textual and visual preferences. Across Qwen2.5-VL and InternVL3 backbones, MixDPO substantially improves action recognition and temporal ordering, yields gains on most standard video hallucination benchmarks, and largely preserves general video understanding.

---

## 🔗 Links & Resources
> - **Project Website & Datasets:** [Official Project Page](https://aimagelab.github.io/CounterVid)
> - **Full-Text Access:** 
>   - [View PDF](https://arxiv.org/pdf/2601.04778)
>   - [HTML Version (Experimental)](https://arxiv.org/html/2601.04778v2)
>   - [TeX Source Code](https://arxiv.org/src/2601.04778)
> - **Citations & References:** 
>   - [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.04778)
>   - [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.04778)
>   - [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.04778)