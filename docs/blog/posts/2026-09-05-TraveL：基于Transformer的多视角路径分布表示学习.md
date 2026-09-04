---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 路径表示学习
- Transformer
- 空间时序动态
- 交通智能
- 深度学习
title: TraveL：基于Transformer的多视角路径分布表示学习
---
### 文章背景与核心概要
路径表示学习（PRL）作为路网分析的核心技术，以往通常侧重于捕捉路段与路径之间的共现关系，以生成静态的向量表示。然而，这类传统方法往往忽略了动态的出行者行为以及路径内部的区域相关性，难以全面刻口复杂的交通场景。

为了弥补这一研究空白，本文提出了 **TraveL**（基于Transformer的多视角分布表示学习）框架。该方法将路径及其出发时间编码为全面的*分布表示*，能够解码路径上各种可能的出行者行为。此外，该框架引入了一种创新的**区域注意力**机制来捕捉区域相关性与路段关系，并在训练过程中利用**柯尔莫哥洛夫-斯米尔诺夫（K-S）检验**将采样得到的出行者行为与真实数据进行对齐。实验表明，TraveL在多项基准测试中显著超越了当前最先进的方法。

---

# TraveL: Transformer-based Multi-view Path Distributional Representation Learning

**arXiv:** [2609.03427 [cs.LG]]  
**Authors:** Fang He, Tao-yang Fu, Wang-chien Lee  
**Submitted:** September 3, 2026  
**Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`)  

---

## 📌 Summary
路网的路径表示学习（PRL）通常侧重于捕捉路段和路径之间的共现关系，以生成静态向量表示。然而，这些方法往往忽略了路径中动态的出行者行为和区域相关性。

> Path representation learning (PRL) for road networks usually focuses on capturing co-occurrence relationships among road segments and paths to generate static vector representations. However, these methods often overlook dynamic traveler behaviors and regional correlations within paths.

为了弥补这一差距，本文推出了 **TraveL**（基于Transformer的多视角分布表示学习）。TraveL 将路径及其出发时间编码为全面的*分布表示*，能够解码路径上可能出现的出行者行为。此外，该框架引入了一种新颖的**区域注意力**机制来捕捉区域相关性和路段关系，并在训练期间利用**柯尔莫哥洛夫-斯米尔诺夫（K-S）检验**将采样的出行者行为与真实数据进行对齐。

> To bridge this gap, this paper introduces **TraveL** (Transformer-based Multi-view Distributional Representation Learning). TraveL encodes a path—along with its starting travel time—into a comprehensive *distributional representation* capable of decoding possible on-path traveler behaviors. Furthermore, the framework introduces a novel **regional attention** mechanism to capture regional correlations and road segment relationships, and utilizes the **Kolmogorov-Smirnov (K-S) test** to align sampled traveler behaviors against ground-truth data during training.

---

## 🚀 Key Contributions & Methodology
* **分布式路径表示：** 超越了传统的点向量表示，能够捕获多样化出行者行为和区域依赖的全谱系特征。
* **基于Transformer的多视角架构：** 集成了出行出发时间和顺序路径数据，以对复杂的空间时序动态进行建模。
* **区域注意力机制：** 分析区域相关性，以有效编码路段之间的多样化关系。
* **K-S 检验驱动的训练：** 采用柯尔莫哥洛夫-斯米尔诺夫检验来对比采样的出行者行为与收集的真实分布，从而促进稳健的模型优化。

> * **Distributional Path Representation:** Moves beyond traditional point-vector representations to capture the full spectrum of varied traveler behaviors and regional dependencies.
* **Transformer-based Multi-view Architecture:** Integrates travel start-times and sequential path data to model complex spatial-temporal dynamics.
* **Regional Attention Mechanism:** Analyzes regional correlations to effectively encode diverse relationships between road segments.
* **K-S Test-Driven Training:** Employs the Kolmogorov-Smirnov test to compare sampled traveler behaviors against collected ground-truth distributions, facilitating robust model optimization.

---

## 📊 Experimental Results
在合成数据集和真实数据集上进行评估，所提出的 **TraveL** 框架显著优于当前最先进的基线方法：
* 出行时间分布估计的平均 K-S 距离**提升了 14.7%**。
* 路径相似度预测的平均绝对误差（MAE）**降低了 16.7%**。
* 目的地预测的平均绝对误差（MAE）**降低了 3.97%**。

> Evaluated on both synthetic and real-world datasets, the proposed **TraveL** framework significantly outperforms state-of-the-art baselines:
* **14.7% improvement** in Mean K-S distance for travel time distribution estimation.
* **16.7% reduction** in Mean Absolute Error (MAE) for path similarity prediction.
* **3.97% reduction** in Mean Absolute Error (MAE) for destination prediction.

---

## 🔗 Links & Resources
* [查看 PDF](https://arxiv.org/pdf/2609.03427)
* [arXiv HTML 版本](https://arxiv.org/html/2609.03427v1)
* [DOI 参考](https://doi.org/10.48550/arXiv.2609.03427)

> * [View PDF](https://arxiv.org/pdf/2609.03427)
* [arXiv HTML Version](https://arxiv.org/html/2609.03427v1)
* [DOI Reference](https://doi.org/10.48550/arXiv.2609.03427)