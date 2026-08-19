---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 视频生成
- 任务完成度
- 视觉语言模型
- 基准评测
- 计算机视觉
title: SemComp-Bench：视频生成中的语义任务完成度基准评测
---
### 文章背景与核心概要
随着视频生成技术的飞速发展，现有的评估指标大多局限于逐帧的一致性或中间步骤的准确性，往往忽视了视频是否真正完成了指定的复杂语义任务。为了填补这一空白，本文推出了 SemComp-Bench，这是一个全新的、以结果为导向的视频生成模型评估框架。

该研究的核心在于引入了语义任务完成度（Semantic Task Completion）的概念，并通过构建包含六个不同领域的精心策划数据集（SemComp-Data），结合视觉语言模型（VLM）提出了两大关键评估指标：结果达成度（OA Score）和生成可靠性（GR Score）。初步实验表明，尽管当前视频生成模型取得了长足进步，但在精准实现任务结果和保持强大的语义基础方面，依然面临着巨大的挑战。

---

# SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation

**arXiv:** [2608.17426](https://arxiv.org/abs/2608.17426)  
**Date:** August 18, 2026  
**Subjects:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

> **arXiv:** [2608.17426](https://arxiv.org/abs/2608.17426)  
> **Date:** August 18, 2026  
> **Subjects:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

---

## Summary

**SemComp-Bench** introduces a novel, outcome-oriented framework for evaluating video generation models. Unlike traditional benchmarks that prioritize frame-by-frame consistency or intermediate step accuracy, this approach focuses on **Semantic Task Completion**. The core objective is to determine whether a generated video successfully achieves a specified outcome while maintaining high-level semantic grounding relative to a reference image.

> **SemComp-Bench** introduces a novel, outcome-oriented framework for evaluating video generation models. Unlike traditional benchmarks that prioritize frame-by-frame consistency or intermediate step accuracy, this approach focuses on **Semantic Task Completion**. The core objective is to determine whether a generated video successfully achieves a specified outcome while maintaining high-level semantic grounding relative to a reference image.

To facilitate this, the authors provide:
*   **SemComp-Data:** A curated dataset spanning six distinct domains, featuring reference images, instructions, and outcome-centric video clips.
*   **SemComp-Bench:** A structured evaluation protocol utilizing Vision-Language Models (VLMs) to assess performance via two key metrics:
    *   **OA Score (Outcome Achievement):** Measures the successful completion of the intended task.
    *   **GR Score (Generation Reliability):** Measures the semantic grounding and task-relevant consistency.

> To facilitate this, the authors provide:
> *   **SemComp-Data:** A curated dataset spanning six distinct domains, featuring reference images, instructions, and outcome-centric video clips.
> *   **SemComp-Bench:** A structured evaluation protocol utilizing Vision-Language Models (VLMs) to assess performance via two key metrics:
>     *   **OA Score (Outcome Achievement):** Measures the successful completion of the intended task.
>     *   **GR Score (Generation Reliability):** Measures the semantic grounding and task-relevant consistency.

Initial experiments indicate that while current video generation models are advancing, achieving both precise task outcomes and robust semantic grounding remains a significant challenge.

> Initial experiments indicate that while current video generation models are advancing, achieving both precise task outcomes and robust semantic grounding remains a significant challenge.

---

## Authors

*   Keyu Tu
*   Zhuowei Chen
*   Mengqi Huang
*   Yuxin Wang
*   Jiahao Zhu
*   Zhendong Mao
*   Yongdong Zhang

> *   Keyu Tu
> *   Zhuowei Chen
> *   Mengqi Huang
> *   Yuxin Wang
> *   Jiahao Zhu
> *   Zhendong Mao
> *   Yongdong Zhang

---

## Access & Resources

*   **[View PDF](https://arxiv.org/pdf/2608.17426)**
*   **[HTML (Experimental)](https://arxiv.org/html/2608.17426v1)**
*   **[TeX Source](https://arxiv.org/src/2608.17426)**
*   **DOI:** [10.48550/arXiv.2608.17426](https://doi.org/10.48550/arXiv.2608.17426)

> *   **[View PDF](https://arxiv.org/pdf/2608.17426)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.17426v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.17426)**
> *   **DOI:** [10.48550/arXiv.2608.17426](https://doi.org/10.48550/arXiv.2608.17426)

---

## Citation

For citation purposes, please refer to the [arXiv landing page](https://arxiv.org/abs/2608.17426) for BibTeX and other reference formats.

> For citation purposes, please refer to the [arXiv landing page](https://arxiv.org/abs/2608.17426) for BibTeX and other reference formats.