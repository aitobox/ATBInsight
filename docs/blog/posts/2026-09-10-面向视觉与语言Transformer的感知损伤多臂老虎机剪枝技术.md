---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- Transformer
- 模型剪枝
- 多臂老虎机
- 视觉语言模型
- 模型压缩
title: 面向视觉与语言Transformer的感知损伤多臂老虎机剪枝技术
---
### 文章背景与核心概要

随着视觉和语言Transformer模型规模的不断膨胀，如何在有限的计算资源下对其进行高效压缩已成为深度学习领域的核心挑战之一。传统剪枝方法往往忽略了不同功能单元（如注意力头和MLP通道组）在协同工作时产生的交互影响，且在评估过程中容易受到批次间差异的干扰。

本文介绍了一篇由 Salem Ameen 和 Sunil Vadera 于2026年8月提交的最新研究《Damage-Aware Bandit Pruning for Vision and Language Transformers》。该论文提出了一种新颖的结构化训练后剪枝技术，将 Transformer 模型中的功能单元选择建模为受约束评估预算下的“感知损伤多臂老虎机问题”（damage-aware multi-armed bandit problem）。通过引入成对损伤计算（Paired Damage Calculation）以及平滑有界奖励函数驱动的 UCB 或 Thompson 采样策略，该方法能够在极少评估预算下实现高效、稳健的剪枝。

在包含 GPT-2、OPT、Qwen2.5、ViT 及 Swin 等多种视觉与语言模型的广泛实验中，该方法相比随机、幅度、静态显著性及预算贪心等传统基线，显著降低了模型性能衰退。各项统计检验（如自助法置信区间和配对检验）充分验证了其优越的统计显著性与鲁棒性。

---

# 面向视觉与语言Transformer的感知损伤多臂老虎机剪枝技术 (Damage-Aware Bandit Pruning for Vision and Language Transformers)

## 摘要 (Summary)

> **Damage-Aware Bandit Pruning for Vision and Language Transformers** is a research paper authored by Salem Ameen and Sunil Vadera (submitted on August 2, 2026). The paper introduces a novel structured post-training pruning technique for transformer models that frames functional unit selection (such as attention heads and MLP channel groups) as a **damage-aware multi-armed bandit problem** under a constrained evaluation budget.

**面向视觉与语言Transformer的感知损伤多臂老虎机剪枝技术**是一篇由 Salem Ameen 和 Sunil Vadera 于 2026 年 8 月 2 日提交的研究论文。该论文为 Transformer 模型引入了一种新颖的结构化训练后剪枝技术，该技术将功能单元（如注意力头和 MLP 通道组）的选择在受限的评估预算下建模为**感知损伤的多臂老虎机问题**。

> Key highlights of the methodology and findings include:
> * **Paired Damage Calculation:** Attention heads and MLP channel groups are temporarily masked on calibration batches. "Paired damage" is defined as the masked loss minus the base loss on the exact same batch, significantly reducing batch-to-batch variation.
> * **Bandit Policies & Selection:** A smooth, bounded reward function drives either a UCB-style policy or fractional-Beta Thompson Sampling. The final pruning mask is constructed sequentially by adding one unit at a time.
> * **Evaluation & Models:** Experiments span multiple language and vision models (including GPT-2, OPT, Pythia, Qwen2.5, SmolLM2, ViT-B/16, DeiT-Tiny, and Swin-Tiny) across datasets like WikiText-2, LAMBADA, and Imagenette.
> * **Statistical Rigor:** Compared against random, magnitude, static-saliency, and budgeted-greedy selection methods, the bandit approaches consistently reduce degradation. Out of 28 highlighted comparisons, 23 bootstrap confidence intervals exclude zero, 11 paired tests achieve $p < 0.05$, and six pass the Benjamini-Hochberg correction ($q < 0.05$ across 116 total dataset-wise tests).

该方法论和研究发现的核心亮点包括：
* **成对损伤计算（Paired Damage Calculation）：** 在校准批次上对注意力头和 MLP 通道组进行临时掩码。所谓“成对损伤”定义为完全相同的批次上，掩码后的损失减去基础损失，从而显着减少批次间的变异性。
* **老虎机策略与选择（Bandit Policies & Selection）：** 一个平滑、有界的奖励函数驱动着 UCB 风格的策略或分数 Beta 汤普森采样（fractional-Beta Thompson Sampling）。最终的剪枝掩码通过每次添加一个单元的方式顺序构建。
* **评估与模型（Evaluation & Models）：** 实验涵盖了多个语言和视觉模型（包括 GPT-2、OPT、Pythia、Qwen2.5、SmolLM2、ViT-B/16、DeiT-Tiny 和 Swin-Tiny），涉及 WikiText-2、LAMBADA 和 Imagenette 等数据集。
* **统计严谨性（Statistical Rigor）：** 与随机、幅度、静态显著性和预算贪心选择方法相比，老虎机方法持续降低了性能退化。在 28 个重点比较中，有 23 个自助法置信区间不包含零，11 个配对检验达到了 $p < 0.05$，并且有 6 个通过了本杰米尼-霍赫贝格校正（在总共 116 个数据集层面的检验中 $q < 0.05$）。

---

## 文档详情 (Document Details)

> * **arXiv Identifier:** [arXiv:2609.05448](https://arxiv.org/abs/2609.05448) [cs.AI]
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Secondary Subjects:** Machine Learning (`cs.LG`)
> * **Authors:** Salem Ameen, Sunil Vadera
> * **Submission Date:** August 2, 2026
> * **Document Length:** 23 pages, 6 figures

* **arXiv 标识符：** [arXiv:2609.05448](https://arxiv.org/abs/2609.05448) [cs.AI]
* **主要主题：** 人工智能 (`cs.AI`)
* **次要主题：** 机器学习 (`cs.LG`)
* **作者：** Salem Ameen, Sunil Vadera
* **提交日期：** 2026年8月2日
* **文档页数：** 23页，6张图表

---

## 访问与资源 (Access & Resources)

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2609.05448)
> * **DOI:** [10.48550/arXiv.2609.05448](https://doi.org/10.48550/arXiv.2609.05448)
> * **External Links:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05448)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05448)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.05448)

* **全文 PDF：** [查看 PDF](https://arxiv.org/pdf/2609.05448)
* **DOI：** [10.48550/arXiv.2609.05448](https://doi.org/10.48550/arXiv.2609.05448)
* **外部链接：** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05448)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05448)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.05448)