---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 边缘AI
- 两轮车安全
- 时间序列预测
- 机器学习
- 智能交通
title: MotoSafety：利用学习型时间重要性在时间压力下进行两轮车碰撞风险评估的边缘AI
---
### 文章背景与核心概要
两轮机动车（PTW）驾驶员在复杂的道路交通环境中面临着极高的安全风险，而诸如时间压力（TP）等认知应激因素会显著加剧这一威胁。为了解决传统碰撞风险评估模型计算开销大、难以在资源受限的边缘设备上部署以及忽略认知压力影响的问题，研究人员开发了 MotoSafety 架构。该研究通过引入独特的“学习型时间重要性”原则，并结合大规模模拟驾驶数据集，在保证极高分类与预测准确率的同时，大幅降低了计算复杂度和推理延迟。

MotoSafety 不仅在碰撞风险分类和时间序列预测上超越了现有的多种基线模型（如 TimesNet、LLM4TS、Time-LLM 和 iTransformer），还展现出了极高的实用性和跨领域迁移能力，仅需少量的传感器特征即可实现低成本、高效率的边缘端实时部署，为未来的智能交通安全系统提供了全新的技术支撑。

---

# MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure

> MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure

**arXiv:** [2608.17823](https://arxiv.org/abs/2608.17823)  
**Authors:** Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil, Subasish Das  
**Submitted:** 18 Aug 2026  
**Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Human-Computer Interaction (cs.HC)

> **arXiv:** [2608.17823](https://arxiv.org/abs/2608.17823)  
> **Authors:** Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil, Subasish Das  
> **Submitted:** 18 Aug 2026  
> **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Human-Computer Interaction (cs.HC)

---

## Summary

> ## Summary

*MotoSafety* 是一种轻量级、高性能的边缘AI架构，专为评估两轮机动车（PTW）的碰撞风险而设计，特别针对诸如**时间压力（TP）**等认知应激因素的影响进行了优化。通过利用新颖的“学习型时间重要性”原则，该模型在分类和预测任务上均实现了 SOTA（业界领先）的性能，同时保持了足以部署在低成本边缘硬件上的高效率。

> *MotoSafety* is a lightweight, high-performance Edge-AI architecture designed to assess collision risk for powered two-wheelers (PTWs), specifically addressing the impact of cognitive stressors like **Time Pressure (TP)**. By utilizing a novel "Learned Temporal Importance" principle, the model achieves state-of-the-art performance in both classification and forecasting while remaining efficient enough for deployment on low-cost edge hardware.

---

## Key Highlights

> ## Key Highlights

### 1. Dataset & Methodology

> ### 1. Dataset & Methodology

*   **大规模数据：** 本研究引入了一个包含超过 129,000 个标记多元时间序列序列的数据集，该数据集源自 153 次模拟器骑行（51 名参与者）。
*   **特征集：** 捕获了 64 个不同的特征，包括车辆动力学、控制输入、邻近度和行为违规情况。
*   **归纳偏置：** 将真实的 TP 作为归纳偏置引入，使分类准确率从 94.09% 提升至 94.97%。

> *   **Large-Scale Data:** The study introduces a dataset comprising over 129,000 labeled multivariate time-series sequences derived from 153 simulator rides (51 participants).
> *   **Feature Set:** Captures 64 distinct features, including vehicle dynamics, control inputs, proximity, and behavioral violations.
> *   **Inductive Bias:** Incorporating ground-truth TP as an inductive bias improved classification accuracy from 94.09% to 94.97%.

### 2. Performance Metrics

> ### 2. Performance Metrics

*   **分类性能：** 准确率达到 94.97%，ROC AUC 达到 99.33%，优于包括 *TimesNet* 和 *LLM4TS* 在内的十个基线模型。
*   **预测性能：** 实现了 0.039 的 MSE 和 0.094 的 MAE，与 *Time-LLM* 和 *iTransformer* 相比，误差降低了 4.4 倍。
*   **效率：** 该模型仅拥有 115 万个参数，运行延迟仅为 0.135 毫秒，非常适合低成本 CPU 边缘设备部署。

> *   **Classification:** 94.97% accuracy and 99.33% ROC AUC, outperforming ten baselines, including *TimesNet* and *LLM4TS*.
> *   **Forecasting:** Achieved 0.039 MSE and 0.094 MAE, representing a 4.4x reduction in error compared to *Time-LLM* and *iTransformer*.
> *   **Efficiency:** The model features only 1.15M parameters and operates with a latency of just 0.135 ms, making it ideal for low-cost CPU edge deployment.

### 3. Practicality & Transferability

> ### 3. Practicality & Transferability

*   **即用型部署：** 该模型仅使用 21 个 IMU+GPS 特征就保持了高准确率（93.91%），从而促进了真实场景中的落地实施。
*   **领域通用性：** 除了 PTW 安全领域外，该架构在人类活动识别（97.66%）和临床领域（99.65%）中也表现出强大的迁移能力。

> *   **Deployment Ready:** The model maintains high accuracy (93.91%) using only 21 IMU+GPS features, facilitating real-world implementation.
> *   **Domain Versatility:** Beyond PTW safety, the architecture demonstrates strong transferability to human activity recognition (97.66%) and clinical domains (99.65%).

---

## Access & Resources

> ## Access & Resources

*   **全文：** [查看 PDF](https://arxiv.org/pdf/2608.17823) | [HTML（实验性）](https://arxiv.org/html/2608.17823v1)
*   **许可协议：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)
    <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> *   **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.17823) | [HTML (Experimental)](https://arxiv.org/html/2608.17823v1)
> *   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
>     <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## Metadata

> ## Metadata

*   **评论：** 40 页
*   **MSC 类别：** 68T07, 68T05, 62M10
*   **ACM 类别：** I.2.1; I.5.4; J.2
*   **DOI：** [10.48550/arXiv.2608.17823](https://doi.org/10.48550/arXiv.2608.17823)

> *   **Comments:** 40 pages
> *   **MSC Classes:** 68T07, 68T05, 62M10
> *   **ACM Classes:** I.2.1; I.5.4; J.2
> *   **DOI:** [10.48550/arXiv.2608.17823](https://doi.org/10.48550/arXiv.2608.17823)