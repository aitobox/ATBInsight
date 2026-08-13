---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 类激活映射
- 可解释人工智能
- 计算机视觉
- 卷积神经网络
- Transformer
title: 可解释计算机视觉中的类激活映射：CNN、Transformer与基础模型时代视觉解释的方法论中心综述
---
### 文章背景与核心概要
类激活映射（CAM）是可解释人工智能（XAI）领域的一项基础且广泛应用的技术。其核心目标直观明了：将模型内部的证据转化为可视化热力图，从而高亮显示支持目标类别或概念的具体图像区域、卷积通道、标记或图像块。

这篇全面综述综合了2016年以来发表的57篇以方法为核心的严选论文。它深入探讨了CAM类方法的发展演变——从早期基于全局平均池化的卷积神经网络（CNN），逐步演变为基于梯度的后验解释、无梯度得分/消融方法、高分辨率上采样、弱监督定位/分割、Transformer标记归因、因果/去偏框架，以及利用CLIP、DINO、SAM和特征分布比较等架构的现代基础模型时代方法。

---

## 执行摘要 / Executive Summary

Class Activation Mapping (CAM) is a foundational and widely utilized technique in Explainable Artificial Intelligence (XAI). Its primary objective is intuitive: translating internal model evidence into a visual heatmap that highlights the specific image regions, convolutional channels, tokens, or patches supporting a target class or concept. 

> 类激活映射（CAM）是可解释人工智能（XAI）领域的一项基础且广泛应用的技术。其核心目标直观明了：将模型内部的证据转化为可视化热力图，从而高亮显示支持目标类别或概念的具体图像区域、卷积通道、标记或图像块。

This comprehensive review synthesizes a strict corpus of **57 method-centered papers** published from 2016 onward. It explores the evolution of CAM-style methods—moving away from early global-average-pooled Convolutional Neural Networks (CNNs) toward gradient-based post-hoc explanations, gradient-free score/ablation methods, high-resolution upscaling, weakly supervised localization/segmentation, transformer token attribution, causal/debiasing frameworks, and modern foundation-model-era approaches leveraging architectures like CLIP, DINO, SAM, and feature-distribution comparisons.

> 这篇全面综述综合了2016年以来发表的**57篇以方法为核心的严选论文**。它深入探讨了CAM类方法的发展演变——从早期基于全局平均池化的卷积神经网络（CNN），逐步演变为基于梯度的后验解释、无梯度得分/消融方法、高分辨率上采样、弱监督定位/分割、Transformer标记归因、因果/去偏框架，以及利用CLIP、DINO、SAM和特征分布比较等架构的现代基础模型时代方法。

---

## 核心亮点与发现 / Key Highlights & Findings

- **Evolution of Architectures:** Traces the paradigm shift from explaining a single class score in a low-resolution CNN layer toward multi-layer, comparative, probabilistic, token-aware, and foundation-model-aware explanations.
> - **架构演进：** 追溯了从解释低分辨率CNN层中的单一类别得分，向多层、对比、概率、标记感知以及基础模型感知解释的范式转变。

- **Methodological Taxonomy:** Categorizes existing literature by:
  - Attribution mechanism
  - Architectural dependence
  - Evaluation objective
> - **方法论分类：** 按照以下维度对现有文献进行分类：
  - 归因机制
  - 架构依赖性
  - 评估目标

- **Evaluative Fragmentation:** Highlights a persistent challenge in the field—evaluation metrics remain fragmented. Faithfulness, localization accuracy, robustness, computational efficiency, and human trust are frequently measured using entirely different, non-standardized protocols.
> - **评估碎片化：** 突出了该领域面临的一个持续挑战——评估指标仍然呈碎片化状态。忠实度、定位准确性、鲁棒性、计算效率和人类信任度往往采用完全不同且非标准化的协议进行测量。

- **Open Gaps:** Emphasizes not merely what each method contributes, but crucially identifies the unresolved gaps left behind and how subsequent literature attempts to bridge them.
> - **未竟空白：** 不仅强调了每种方法的贡献，更关键的是指出了遗留的未解决空白，以及后续文献如何尝试填补这些空白。

---

## 提交历史 / Submission History

- **[v1]** Wed, 12 Aug 2026, 17:45:03 UTC *(957 KB)*
> - **[v1]** 2026年8月12日 周三 17:45:03 UTC *(957 KB)*

---

*For full-text access, view the [PDF on arXiv](https://arxiv.org/pdf/2608.12299).*
> *如需全文访问，请查看 [arXiv上的PDF](https://arxiv.org/pdf/2608.12299)。*