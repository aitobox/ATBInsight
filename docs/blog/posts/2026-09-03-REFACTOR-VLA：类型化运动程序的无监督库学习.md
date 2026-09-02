---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- VLA模型
- 机器人学
- 运动程序
- 库学习
- 强化学习
title: REFACTOR-VLA：类型化运动程序的无监督库学习
---
### 文章背景与核心概要

当前的视觉-语言-动作（VLA）模型（如 OpenVLA、$\pi_0$、RT-2 和 RDT-1B）大多作为单一整体系统运行，直接输出原始的运动指令或简短的动作片段，而未能将复杂的行为组织为可重用的抽象。因此，这些模型在长周期（long-horizon）任务上的表现往往会下降，且缺乏可解释性。

为了克服这些局限性，作者推出了 **REFACTOR-VLA**，这是一个专为类型化运动程序的无监督库学习而设计的“清醒/睡眠”（wake/sleep）系统。该系统通过清醒阶段生成类型化 lambda 项，并结合睡眠阶段利用行为等效核进行运动程序聚类，同时通过最小描述长度（MDL）和回报保持门控机制来精炼技能库。实验证明，该方法显著超越了现有的先进基线模型，为解决机器人具身智能的可解释性与长序贯规划难题提供了新途径。

---

# REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs

**Authors:** Riyaaz Shaik, Chandru Venkataraman  
**Published:** September 1, 2026  
**Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Robotics (`cs.RO`)  
**arXiv:** [2609.01215 [cs.LG]](https://arxiv.org/abs/2609.01215)  

> **Authors:** Riyaaz Shaik, Chandru Venkataraman  
> **Published:** September 1, 2026  
> **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Robotics (`cs.RO`)  
> **arXiv:** [2609.01215 [cs.LG]](https://arxiv.org/abs/2609.01215)

---

## Executive Summary

Most current Vision-Language-Action (VLA) models (such as OpenVLA, $\pi_0$, RT-2, and RDT-1B) operate as monolithic systems that emit raw motor commands or short action chunks without organizing behavior into reusable abstractions. Consequently, these models often degrade on long-horizon tasks and lack interpretability. 

To overcome these limitations, the authors introduce **REFACTOR-VLA**, a wake/sleep system designed for unsupervised library learning of typed motor programs. 

### Key Innovations & Findings

* **Wake/Sleep Architecture:** 
  * **Sleep Phase:** Clusters motor-program fragments using a Behavioral-Equivalence Kernel (BEK) computed from rollouts of a learned latent world model ($M_\phi$).
  * **Wake Phase:** Emits typed lambda terms over a Hindley-Milner-inspired vocabulary, which are then consumed by a library-conditioned rectified-flow action decoder.
* **Gating Mechanisms:** Abstractions are only admitted if they successfully pass Minimum Description Length (MDL) and return-preservation gates.
* **Model Capacity vs. Objective Quality:** Scaling the world model from 188M to 430M parameters actually degraded performance across all 4 LIBERO suites, proving that capacity alone is insufficient. Instead, the training objective is paramount: incorporating an auxiliary supervised contrastive (InfoNCE) loss during world-model warmup drastically improves sleep-phase clustering.
* **Performance:** REFACTOR-VLA outperforms the strongest published baseline across all 4 LIBERO suites by a mean $\Delta$ of $+0.184$, achieving Normalized Mutual Information (NMI) scores of:
  * **Object:** $0.462 \pm 0.021$
  * **Spatial:** $0.867 \pm 0.025$
  * **Goal:** $0.915 \pm 0.013$
  * **LIBERO-10:** $0.754 \pm 0.010$

> ## 执行摘要
> 
> 大多数当前的视觉-语言-动作（VLA）模型（如 OpenVLA、$\pi_0$、RT-2 和 RDT-1B）作为单一整体系统运行，输出原始运动指令或短动作片段，而未能将行为组织为可重用的抽象。因此，这些模型在长跨度任务上经常性能退化，并且缺乏可解释性。
> 
> 为了克服这些局限性，作者推出了 **REFACTOR-VLA**，这是一个专为类型化运动程序的无监督库学习而设计的清醒/睡眠（wake/sleep）系统。
> 
> ### 核心创新与发现
> 
> * **清醒/睡眠架构：** 
>   * **睡眠阶段：** 使用从学习到的潜在世界模型（$M_\phi$）的轨迹展开（rollouts）计算出的行为等效核（BEK）对运动程序片段进行聚类。
>   * **清醒阶段：** 在受 Hindley-Milner 启发词汇表的基础上发射类型化 lambda 项，随后由库条件化的整流流（rectified-flow）动作解码器对其进行消费。
> * **门控机制：** 只有成功通过最小描述长度（MDL）和回报保持门控的抽象才会被收录。
> * **模型容量与目标质量：** 将世界模型从 1.88 亿参数扩展到 4.3 亿参数实际上导致了所有 4 个 LIBERO 套件性能的下降，这证明仅靠模型容量是不够的。相反，训练目标至关重要：在世界模型预热期间引入辅助监督对比（InfoNCE）损失，会大大改善睡眠阶段的聚类效果。
> * **性能表现：** REFACTOR-VLA 在所有 4 个 LIBERO 套件上均超越了最强的已发布基线，平均提升 $\Delta$ 为 $+0.184$，并取得了以下归一化互信息（NMI）得分：
>   * **物体（Object）：** $0.462 \pm 0.021$
>   * **空间（Spatial）：** $0.867 \pm 0.025$
>   * **目标（Goal）：** $0.915 \pm 0.013$
>   * **LIBERO-10：** $0.754 \pm 0.010$

---

## Metadata & Reference Links

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.01215) | [HTML Version](https://arxiv.org/html/2609.01215v1)
* **Citation DOI:** [10.48550/arXiv.2609.01215](https://doi.org/10.48550/arXiv.2609.01215)

> ## 元数据与参考链接
> 
> * **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.01215) | [HTML 版本](https://arxiv.org/html/2609.01215v1)
> * **引用 DOI：** [10.48550/arXiv.2609.01215](https://doi.org/10.48550/arXiv.2609.01215)

---
*License:* [<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> View License](http://creativecommons.org/licenses/by/4.0/)

> *许可证：* [<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> 查看许可证](http://creativecommons.org/licenses/by/4.0/)