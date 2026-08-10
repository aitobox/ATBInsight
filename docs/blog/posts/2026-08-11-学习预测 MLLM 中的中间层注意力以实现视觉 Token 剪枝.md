---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- MLLM
- 视觉Token剪枝
- 模型效率
- 注意力机制
- 动态蒸馏
title: 学习预测 MLLM 中的中间层注意力以实现视觉 Token 剪枝
---
### 文章背景与核心概要
多模态大语言模型（MLLM）虽然功能强大，但由于需要处理大量的视觉 Token，导致计算成本极为高昂。虽然视觉 Token 剪枝技术可以缓解这一问题，但传统方法通常依赖于模型固定中间层的注意力图。本文指出了该方法的两个致命缺陷：一是样本多变性（最优剪枝层随输入不同而显著变化），二是计算延迟（等待提取中间层注意力意味着已经消耗了大量计算资源）。

为了解决这些问题，作者提出了**中间层注意力预测（MAP）**。MAP 利用“问题对比教师选择”机制来识别样本特定的教师层，然后将该注意力蒸馏到一个轻量级预测器中，从而在首个大语言模型层*之前*评估 Token 的重要性。通过将这些重要性得分与多样性准则相结合，MAP 在 LLaVA-NeXT-7B 上实现了 **3.09 倍的端到端加速**，在仅使用 5.56% 视觉 Token 的情况下，保留了 **97.5% 的原始性能**。

---

# 学习预测 MLLM 中的中间层注意力以实现视觉 Token 剪枝

**作者：** Yuyao Sun, Tao Deng, Shuang Li, Deqing Wang, Hao Geng, Minjun Yu  
**日期：** 2026年8月4日  
**arXiv ID：** [2608.06411](https://arxiv.org/abs/2608.06411)  
**学科：** 人工智能 (cs.AI)；计算机视觉与模式识别 (cs.CV)

---

## 摘要
多模态大语言模型（MLLM）功能强大，但由于处理的视觉 Token 数量庞大，计算成本高昂。虽然视觉 Token 剪枝可以缓解这一问题，但它传统上依赖于模型固定中间层的注意力图。本文指出了该方法的两个关键缺陷：
1. **样本多变性：** 基于注意力剪枝的最优层在不同输入之间存在显著差异，这使得固定层策略并非最优。
2. **计算延迟：** 等待从中间层提取注意力意味着已经消耗了大量的计算。

为了解决这些问题，作者引入了**中间层注意力预测（MAP）**。MAP 利用“问题对比教师选择”机制来识别样本特定的教师层。然后，它将此注意力蒸馏到一个轻量级预测器中，该预测器在第一层语言模型层*之前*估计 Token 的重要性。通过将这些重要性得分与多样性准则相结合，MAP 在 LLaVA-NeXT-7B 上实现了 **3.09 倍的端到端加速**，同时仅使用 5.56% 的视觉 Token 就保留了 **97.5% 的原始性能**。

> MLLMs are powerful but computationally expensive due to the high volume of visual tokens processed. While visual token pruning can mitigate this, it traditionally relies on attention maps from fixed middle layers of the model. This paper identifies two critical flaws in that approach:
> 1. **Sample Variability:** The optimal layer for attention-based pruning varies significantly across different inputs, making a fixed-layer strategy suboptimal.
> 2. **Computational Latency:** Waiting to extract attention from middle layers means significant computation has already been expended.
> 
> To solve these issues, the authors introduce **Middle-layer Attention Prediction (MAP)**. MAP utilizes a "Question Contrastive Teacher Selection" mechanism to identify a sample-specific teacher layer. It then distills this attention into a lightweight predictor that estimates token importance *before* the first language model layer. By combining these importance scores with a diversity criterion, MAP achieves a **3.09x end-to-end speedup** on LLaVA-NeXT-7B while retaining **97.5% of the original performance** using only 5.56% of the visual tokens.

---

## 核心贡献
* **动态教师选择：** 实现了问题对比教师选择机制，以为每个特定输入识别最具响应性的层。
* **轻量级预测：** 将注意力蒸馏到紧凑的模型中，允许在初始语言模型层之前进行 Token 剪枝。
* **推理效率：** 在实际推理阶段不需要任何注意力图，确保与现有加速技术的完全兼容性。
* **高性能：** 在十个基准测试中展现出 SOTA（最先进）的效率，在大幅减少视觉 Token 处理的同时保持了高准确率。

> * **Dynamic Teacher Selection:** Implements Question Contrastive Teacher Selection to identify the most responsive layer for each specific input.
> * **Lightweight Prediction:** Distills attention into a compact model, allowing for token pruning prior to the initial language model layer.
> * **Inference Efficiency:** Requires no attention maps during the actual inference phase, ensuring full compatibility with existing acceleration techniques.
> * **High Performance:** Demonstrates state-of-the-art efficiency across ten benchmarks, maintaining high accuracy with a massive reduction in visual token processing.

---

## 获取与资源
* **PDF：** [查看论文](https://arxiv.org/pdf/2608.06411)
* **HTML：** [实验性 HTML 视图](https://arxiv.org/html/2608.06411v1)
* **TeX 源码：** [下载源码](https://arxiv.org/src/2608.06411)
* **许可证：** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/)

> * **PDF:** [View Paper](https://arxiv.org/pdf/2608.06411)
> * **HTML:** [Experimental HTML View](https://arxiv.org/html/2608.06411v1)
> * **TeX Source:** [Download Source](https://arxiv.org/src/2608.06411)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">