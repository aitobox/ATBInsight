---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 磁约束聚变
- 偏滤器热通量
- 深度学习
- 时频先验
- SafeDivertor
title: SafeDivertor：通过利用时频先验从宏观等离子体状态信号中高保真重建偏滤器热通量
---
### 文章背景与核心概要
在磁约束聚变装置中，对偏滤器热通量的分析对于监测等离子体与壁相互作用以及保护面向等离子体部件（PFCs）至关重要。传统的基于红外热成像的反演技术通常依赖于放电后的离线分析，这需要复杂的热传导建模以及针对特定装置材料属性和几何结构的约束条件。

为了克服这些局限性，本文引入了 **SafeDivertor**，这是一种面向在线应用的新型范式，能够直接从实时宏观等离子体状态信号中重建出具有时间解析力的径向热通量剖面。该研究不仅构建了首个多源放电数据集 **DivMPS2HF** 作为基准，还提出了一套结合物理先验、输入扰动、时频感知优化以及渐进式训练的任务驱动型深度学习框架，实验证明其在各项核心指标上均显著超越传统的时序基线模型。

---

# SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation

## Summary
Divertor heat-flux analysis is vital for monitoring plasma-wall interactions and protecting plasma-facing components in magnetic-confinement fusion devices. Traditional infrared-based inversion techniques rely on post-discharge analysis, which requires complex heat-conduction modeling and device-specific constraints. To overcome these limitations, this paper introduces **SafeDivertor**, a novel online-oriented paradigm that directly reconstructs time-resolved radial heat-flux profiles from real-time macroscopic plasma state signals. 

> Divertor heat-flux analysis is vital for monitoring plasma-wall interactions and protecting plasma-facing components in magnetic-confinement fusion devices. Traditional infrared-based inversion techniques rely on post-discharge analysis, which requires complex heat-conduction modeling and device-specific constraints. To overcome these limitations, this paper introduces **SafeDivertor**, a novel online-oriented paradigm that directly reconstructs time-resolved radial heat-flux profiles from real-time macroscopic plasma state signals. 

---

## Metadata & Publication Details
* **arXiv Identifier:** `arXiv:2608.05669` [physics.plasm-ph]
* **Primary Subject:** Plasma Physics (`physics.plasm-ph`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computer Vision and Pattern Recognition (`cs.CV`)
* **Submission Date:** August 6, 2026
* **Authors:** Hao Si, Zehua Chen, Qingquan Yang, Xiao Wang, Dengdi Sun, Wanli Lyu, Gaoting Chen, Guosheng Xu, Hang Su, Jin Tang, and Jun Zhu

> ## Metadata & Publication Details
> * **arXiv Identifier:** `arXiv:2608.05669` [physics.plasm-ph]
> * **Primary Subject:** Plasma Physics (`physics.plasm-ph`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computer Vision and Pattern Recognition (`cs.CV`)
> * **Submission Date:** August 6, 2026
> * **Authors:** Hao Si, Zehua Chen, Qingquan Yang, Xiao Wang, Dengdi Sun, Wanli Lyu, Gaoting Chen, Guosheng Xu, Hang Su, Jin Tang, and Jun Zhu

---

## Abstract
Divertor heat-flux analysis is essential for understanding plasma-wall interactions and protecting plasma-facing components in magnetic-confinement fusion devices, while conventional infrared-based inversion is usually performed after discharge and requires heat-conduction modeling with device-specific material properties, divertor geometry, and boundary conditions. 

> Divertor heat-flux analysis is essential for understanding plasma-wall interactions and protecting plasma-facing components in magnetic-confinement fusion devices, while conventional infrared-based inversion is usually performed after discharge and requires heat-conduction modeling with device-specific material properties, divertor geometry, and boundary conditions. 

Rather than accelerating this conventional infrared-based inversion paradigm, the authors introduce a new online-oriented signal-based reconstruction paradigm that directly reconstructs time-resolved radial heat-flux profiles from multi-source macroscopic plasma-state signals available during discharge. 

> Rather than accelerating this conventional infrared-based inversion paradigm, the authors introduce a new online-oriented signal-based reconstruction paradigm that directly reconstructs time-resolved radial heat-flux profiles from multi-source macroscopic plasma-state signals available during discharge. 

To enable systematic study of this task, the work introduces **DivMPS2HF**, a multi-source discharge dataset that provides the data foundation and benchmark for signal-based divertor heat-flux reconstruction. Furthermore, the authors propose **SafeDivertor**, a task-driven framework designed to address the key challenges of signal-based heat-flux reconstruction:
* **Physical Prior-Aware Initialization:** Provides radial-distribution guidance for target channels.
* **Input Perturbation:** Reduces over-reliance on specific heterogeneous signals.
* **Spectral-Aware Reconstruction Optimization:** Exploits time-frequency priors and preserves transient dynamics.
* **Progressive Training:** Stabilizes the optimization of these complementary objectives.

> To enable systematic study of this task, the work introduces **DivMPS2HF**, a multi-source discharge dataset that provides the data foundation and benchmark for signal-based divertor heat-flux reconstruction. Furthermore, the authors propose **SafeDivertor**, a task-driven framework designed to address the key challenges of signal-based heat-flux reconstruction:
> * **Physical Prior-Aware Initialization:** Provides radial-distribution guidance for target channels.
> * **Input Perturbation:** Reduces over-reliance on specific heterogeneous signals.
> * **Spectral-Aware Reconstruction Optimization:** Exploits time-frequency priors and preserves transient dynamics.
> * **Progressive Training:** Stabilizes the optimization of these complementary objectives.

Experimental evaluations on the **DivMPS2HF** dataset demonstrate that SafeDivertor outperforms evaluated time-series baselines across all five core metrics, establishing a new performance benchmark for signal-based divertor heat-flux reconstruction.

> Experimental evaluations on the **DivMPS2HF** dataset demonstrate that SafeDivertor outperforms evaluated time-series baselines across all five core metrics, establishing a new performance benchmark for signal-based divertor heat-flux reconstruction.

---

## Full-Text & External Resources
* **[View PDF](https://arxiv.org/pdf/2608.05669)**
* **[Source Code Repository (GitHub)](https://github.com/Event-AHU/OpenFusion)**
* **[arXiv HTML Version](https://arxiv.org/html/2608.05669v1)**
* **References & Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05669) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05669) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05669)

> ## Full-Text & External Resources
> * **[View PDF](https://arxiv.org/pdf/2608.05669)**
> * **[Source Code Repository (GitHub)](https://github.com/Event-AHU/OpenFusion)**
> * **[arXiv HTML Version](https://arxiv.org/html/2608.05669v1)**
> * **References & Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05669) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05669) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05669)