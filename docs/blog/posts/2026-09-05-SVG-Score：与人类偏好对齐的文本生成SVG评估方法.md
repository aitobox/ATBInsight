---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- SVG生成
- 评估指标
- 视觉语言模型
- 人类对齐
- 计算机视觉
title: SVG-Score：与人类偏好对齐的文本生成SVG评估方法
---
### 文章背景与核心概要
随着可缩放矢量图形（SVG）生成模型的日益成熟，该领域面临着一个显著的瓶颈：缺乏领域特定的评估协议。当前的方法严重依赖于为自然图像设计的指标（如 CLIPScore），这些指标无法捕捉矢量图形的细微特征。

为此，**SVG-Score** 提出了一种全新的人类对齐评估框架。通过分析模型如何处理特定错误（例如颜色错误、物体数量偏差和空间关系失调），作者证明了现有指标往往对 SVG 生成器的独特失败模式不敏感。本文引入了一个关于*语义对齐（Semantic Alignment）*的人类标注数据集，并提出了两个互补的评估器：1. **自适应 CLIP 评分器**：与人类偏好对齐，用于快速、大规模评估；2. **VLM 裁判**：通过监督微调和奖励塑造强化学习进行训练，以实现更具表达力和可解释性的评估。作者利用这些工具对主要的开源、商业以及基于优化的 SVG 生成器进行了基准测试。

# SVG-Score: Human-Aligned Evaluation of Text-to-SVG Generation

**arXiv:** [2609.03806](https://arxiv.org/abs/2609.03806)  
**Date:** September 3, 2026  
**Subjects:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

---

## 摘要 (Summary)

随着可缩放矢量图形（SVG）生成模型的日益成熟，该领域面临着一个显著的瓶颈：缺乏领域特定的评估协议。当前的方法严重依赖于像 CLIPScore 这样的指标，这些指标原本是为自然图像设计的，无法捕捉矢量图形的细微之处。

> As generative models for Scalable Vector Graphics (SVG) become more sophisticated, the field faces a significant bottleneck: the lack of domain-specific evaluation protocols. Current methods rely heavily on metrics like CLIPScore, which were designed for natural images and fail to capture the nuances of vector graphics.

**SVG-Score** 引入了一种与人类对齐的全新评估框架，旨在弥补这一空白。通过分析模型如何处理特定错误（例如颜色错误、物体数量错误和空间关系失调），作者证明了现有指标往往对 SVG 生成器的独特失败模式不敏感。本文引入了一个关于*语义对齐（Semantic Alignment）*的人类标注数据集，并提出了两个互补的评估器：
1. **自适应 CLIP 评分器（Adapted CLIP Scorers）：** 与人类偏好对齐，用于快速、大规模的评估。
2. **VLM 裁判（VLM Judges）：** 通过监督微调和奖励塑造强化学习进行训练，以实现更具表达力、可解释性的评估。

作者利用这些工具对主要的开源、商业以及基于优化的 SVG 生成器进行了基准测试。

> **SVG-Score** introduces a new human-aligned evaluation framework designed to address this gap. By analyzing how models handle specific errors—such as incorrect colors, object counts, and spatial relationships—the authors demonstrate that existing metrics are often insensitive to the unique failures of SVG generators. The paper introduces a human-annotated dataset for *Semantic Alignment* and proposes two complementary evaluators:
> 1. **Adapted CLIP Scorers:** Aligned to human preferences for fast, large-scale assessment.
> 2. **VLM Judges:** Trained via supervised fine-tuning and reward-shaped reinforcement learning for more expressive, interpretable evaluation.
> 
> The authors use these tools to benchmark major open-source, commercial, and optimization-based SVG generators.

---

## 作者 (Authors)

*   **Marco Cipriano**
*   **Leonardo Zini**
*   **Alexandra Schild**
*   **Valentin Teutschbein**
*   **Afsana Mimi**
*   **Marcella Cornia**
*   **Lorenzo Baraldi**
*   **Gerard de Melo**

---

## 获取与资源 (Access & Resources)

*   **[查看 PDF](https://arxiv.org/pdf/2609.03806)**
*   **[HTML（实验性）](https://arxiv.org/html/2609.03806v1)**
*   **[TeX 源码](https://arxiv.org/src/2609.03806)**
*   **许可协议：** [知识共享署名 4.0 国际版](http://creativecommons.org/licenses/by/4.0/)

> *   **[View PDF](https://arxiv.org/pdf/2609.03806)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2609.03806v1)**
> *   **[TeX Source](https://arxiv.org/src/2609.03806)**
> *   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---

## 元数据与引用 (Metadata & Citations)

*   **DOI：** [https://doi.org/10.48550/arXiv.2609.03806](https://doi.org/10.48550/arXiv.2609.03806)
*   **外部链接：**
    *   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03806)
    *   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03806)
    *   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03806)

> *   **DOI:** [https://doi.org/10.48550/arXiv.2609.03806](https://doi.org/10.48550/arXiv.2609.03806)
> *   **External Links:**
>     *   [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03806)
>     *   [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03806)
>     *   [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03806)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">