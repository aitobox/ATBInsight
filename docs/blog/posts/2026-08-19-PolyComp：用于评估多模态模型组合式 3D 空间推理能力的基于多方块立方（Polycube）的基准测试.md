---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 3D空间推理
- 多模态模型
- 基准测试
- 计算机视觉
- 空间认知
title: PolyComp：用于评估多模态模型组合式 3D 空间推理能力的基于多方块立方（Polycube）的基准测试
---
### 文章背景与核心概要

随着多模态大语言模型在视觉感知领域的快速发展，其对复杂 3D 空间关系的理解和组合推理能力变得至关重要。现有的许多基准测试往往无法充分检验模型对 3D 物体组合与拆解的深度认知。为此，本文推出了 PolyComp 基准测试，旨在严格评估和压力测试现代多模态模型在视觉识别与组合式 3D 空间推理方面的表现。

PolyComp 包含 120 个跨越四个几何类别的独特问题，并通过三种不同的呈现格式进行包装，形成每个模型需面对的 360 个测试任务。评估结果表明，当前最先进的多模态模型（如 GPT-5.6 Sol、Claude Fable 5 和 Gemini 3.1 Pro Preview）在面对复杂的 3D 空间重构和组合推理任务时仍面临严峻挑战，最高准确率仅为 50.0%，凸显出未来在机器空间智能领域仍有巨大的提升空间。

---

## 执行摘要

> **PolyComp** is a procedurally generated and rigorously verified benchmark designed to evaluate and stress-test visual recognition and compositional 3D spatial reasoning in modern multimodal models.

**PolyComp** 是一个通过程序生成并经过严格验证的基准测试，旨在评估和压力测试现代多模态模型的视觉识别与组合式 3D 空间推理能力。

### 核心机制
> ### Core Mechanics
> In each benchmark problem, a model is presented with a **target solid** and must identify which of four given options correctly shows a pair of polycube components that can be combined to form that target solid.

在每个基准测试问题中，模型会看到一个**目标立体图形**（target solid），并必须从给出的四个选项中识别出哪一个选项正确地展示了一对多方块立方（polycube）组件，这两个组件可以组合在一起来形成该目标立体图形。

### 关键亮点与规模
> ### Key Highlights & Scale
> * **Dataset Size:** 120 unique problems spanning four geometry families.
> * **Presentation Formats:** Each problem is delivered in three distinct presentation formats (utilizing either single or multiple images), resulting in 360 presented problems per evaluated model.
> * **Random Guessing Baseline:** 25%

* **数据集规模：** 120 个独占问题，涵盖四个几何类别。
* **呈现格式：** 每个问题均采用三种不同的呈现格式（使用单张或多张图像），导致每个被评估的模型需要完成 360 个测试问题。
* **随机猜测基准线：** 25%

---

## 基准测试性能与模型评估

> ## Benchmark Performance & Model Evaluation

> Across the 360 presented problems per model, current state-of-the-art multimodal models performed as follows:

在每个模型测试的 360 个问题中，当前最先进的多模态模型的表现如下：

| 模型 | 配置 / 努力程度 | 准确率 (%) | 95% 问题簇置信区间 | 每个问题的平均成本 ($) |
| :--- | :--- | :---: | :---: | :---: |
| **GPT-5.6 Sol** | 最大努力 (Max Effort) | **50.0%** | 43.3% – 56.7% | $0.951 |
| **Claude Fable 5** | 最大努力 (Max Effort) | **39.4%** | 33.1% – 46.1% | $0.701 |
| **Gemini 3.1 Pro Preview** | 思考级别：高 (Thinking Level: High) | **27.5%** | 22.8% – 32.5% | $0.350 |

> *Note: Gemini 3.1 Pro Preview performed close to the random guessing baseline of 25%. Furthermore, findings indicate that the observed accuracy spread across different geometry families was larger than the spread across presentation formats.*

*注：Gemini 3.1 Pro Preview 的表现接近 25% 的随机猜测基准线。此外，研究结果表明，不同几何类别之间的准确率差距大于不同呈现格式之间的差距。*

---

## 论文元数据与详情

> ## Paper Metadata & Details

> * **arXiv Identifier:** [arXiv:2608.14741](https://arxiv.org/abs/2608.14741) [cs.CV]
> * **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
> * **Secondary Subject:** Artificial Intelligence (`cs.AI`)
> * **Author:** Siddharth Patel
> * **Submission Date:** August 13, 2026
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

* **arXiv 标识符：** [arXiv:2608.14741](https://arxiv.org/abs/2608.14741) [cs.CV]
* **主要学科：** 计算机视觉与模式识别 (`cs.CV`)
* **次要学科：** 人工智能 (`cs.AI`)
* **作者：** Siddharth Patel
* **提交日期：** 2026年8月13日
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 资源与全文访问

> ## Resources & Full-Text Access

> * [View PDF](https://arxiv.org/pdf/2608.14741)
> * [Experimental HTML Version](https://arxiv.org/html/2608.14741v1)
> * [TeX Source Code](https://arxiv.org/src/2608.14741)

* [查看 PDF](https://arxiv.org/pdf/2608.14741)
* [实验性 HTML 版本](https://arxiv.org/html/2608.14741v1)
* [TeX 源代码](https://arxiv.org/src/2608.14741)