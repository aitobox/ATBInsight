---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 数据库
- 云原生
- 自动扩展
- 资源调度
- AnalyticDB
title: ScaleSense：阿里巴巴 AnalyticDB 中基于学习型资源评估的成本智能扩展框架
---
### 文章背景与核心概要

云原生无服务器（Serverless）数据仓库通过存算分离架构实现了细粒度的弹性扩展。然而，如何为异构的即席查询（Ad-hoc queries）确定最优资源配置，一直是工业界的一大难题。本文通过对阿里巴巴 AnalyticDB 生产工作负载的深入分析，揭示了“配置陷阱”（provisioning trap）现象：用户因担心资源耗尽而长期过度配置硬件，这不仅造成了巨大的预算浪费，且往往无法解决非 CPU 瓶颈（如 I/O 饱和）问题。

为了解决这一挑战，作者提出了 ScaleSense，这是一个主动的、查询级的资源扩展框架。通过采用多面查询编码器（Multi-faceted query encoder）和基于分位数的资源预测器（Quantile-based resource predictor），ScaleSense 能够精确估计多维物理资源占用。结合自动扩展控制器，该框架成功在性能与成本的帕累托前沿（Pareto frontier）上实现了最优平衡，在严格满足用户性能要求的前提下，将货币成本降低了最高 5.22 倍。

---

## 📌 执行摘要

云原生无服务器数据仓库依赖于存算分离来实现细粒度的弹性。然而，为异构的即席查询确定最优资源分配仍然是主要的工业障碍。在本文中，作者分析了阿里巴巴 AnalyticDB 的生产工作负载，并揭示了“配置陷阱”——即由于担心灾难性的资源耗尽，导致用户长期过度配置硬件。这在浪费巨额财务预算的同时，并未解决非 CPU 瓶颈（如 I/O 饱和）问题。

> Cloud-native serverless data warehouses rely on decoupling storage from compute to achieve fine-grained elasticity. However, determining optimal resource allocations for heterogeneous ad-hoc queries remains a major industrial hurdle. In this paper, the authors analyze production workloads in **Alibaba AnalyticDB** and uncover the **"provisioning trap"**—where fear of catastrophic resource depletion leads users to chronically over-provision hardware. This wastes immense financial budgets without resolving non-CPU bottlenecks (such as I/O saturation). 

为了解决这个问题，作者引入了 ScaleSense，这是一个主动的、查询级的资源扩展框架。通过利用多面查询编码器和基于分位数的资源预测器，ScaleSense 可以准确估计多维物理足迹。结合自动扩展控制器，该框架成功地导航了性能-成本帕累托前沿，在严格满足用户定义的性能要求的同时，将货币成本降低了高达 **5.22 倍**。

> To solve this, the authors introduce **ScaleSense**, a proactive, query-level resource scaling framework. By utilizing a multi-faceted query encoder and a quantile-based resource predictor, ScaleSense accurately estimates multi-dimensional physical footprints. Combined with an auto-scaling controller, the framework successfully navigates the performance-cost Pareto frontier, cutting monetary costs by up to **5.22x** while strictly meeting user-defined performance requirements.

---

## 📊 关键亮点与成果

- **规模与验证：** 在超过 **136 万条生产查询**上进行了广泛评估。
- **预测准确性：** 实现了具有稳健预测区间覆盖率的最先进预测准确性。
- **资源配置选择：** 在选择最优资源配置方面，比最佳基准方法有 **76.7% 的相对提升**。
- **成本效率：** 在满足自定义性能优化策略的同时，将运营货币成本降低了 **最高 5.22 倍**。
- **低开销：** 保持了极低的推理延迟，证明了其在高吞吐量企业生产部署中的可行性。

> - **Scale & Validation:** Evaluated extensively on over **1.36 million production queries**.
> - **Prediction Accuracy:** Achieves state-of-the-art prediction accuracy with robust prediction interval coverage.
> - **Resource Configuration Selection:** Delivers a **76.7% relative improvement** over the best baseline approach in choosing optimal resource configurations.
> - **Cost Efficiency:** Satisfies custom performance-optimization policies while reducing operational monetary costs by **up to 5.22x**.
> - **Low Overhead:** Maintains minimal inference latency, proving its viability for high-throughput enterprise production deployments.

---

## 🛠️ ScaleSense 的核心架构

1. **多面查询编码器：** 将复杂的查询执行计划拓扑与底层硬件规范进行联合建模。
2. **基于分位数的资源预测器：** 准确预测多维物理资源足迹，作为防止资源耗尽的可靠安全网。
3. **自动扩展控制器：** 动态调整分配，以平衡帕累托前沿上的性能与成本偏好，无需针对变化的业务优先级进行模型重训练。

> 1. **Multi-Faceted Query Encoder:** Jointly models complex query execution plan topologies alongside underlying hardware specifications.
> 2. **Quantile-Based Resource Predictor:** Predicts multi-dimensional physical resource footprints accurately, acting as a dependable safety net against resource exhaustion.
> 3. **Auto-Scaling Controller:** Dynamically tailors allocations to balance performance against cost preferences along the Pareto frontier, requiring **no model retraining** for changing business priorities.

---

## 🔗 链接与资源

- **查看 PDF：** [arXiv:2608.07945 PDF](https://arxiv.org/pdf/2608.07945)
- **DOI：** [10.48550/arXiv.2608.07945](https://doi.org/10.48550/arXiv.2608.07945)
- **全文来源：** TeX 源码及相关元数据可通过 arXiv 门户获取。

> - **View PDF:** [arXiv:2608.07945 PDF](https://arxiv.org/pdf/2608.07945)
> - **DOI:** [10.48550/arXiv.2608.07945](https://doi.org/10.48550/arXiv.2608.07945)
> - **Full-Text Sources:** TeX Source and associated metadata are available via the arXiv portal.

<img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">