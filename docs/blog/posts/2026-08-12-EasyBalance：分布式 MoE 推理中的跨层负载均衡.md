---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 混合专家模型
- 负载均衡
- 分布式推理
- 深度学习优化
- ICML
title: EasyBalance：分布式 MoE 推理中的跨层负载均衡
---
### 文章背景与核心概要
在混合专家模型（MoE）的分布式推理过程中，专家并行（expert-parallel）的负载均衡一直是一个主要的性能瓶颈。由于 Token 路由在各个专家之间的分布天然存在倾斜，托管较轻负载专家的设备被迫处于闲置状态，等待负载最重的设备完成计算。传统的平衡方法依赖于层内的专家复制或迁移，这会引入显著的开销且扩展性较差。

为了解决这一问题，本文作者推出了 **EasyBalance**，这是一种全新的跨层负载均衡策略。EasyBalance **无需修改专家与设备的映射关系**，从而实现了几乎零开销的即时适应能力。该方法建立在两个核心洞察之上：1. 其他层的专家可以自然地充当当前层的冗余计算资源；2. 可以联合执行跨层 MoE 工作负载，以平滑单个层的负载不均。

通过在每个 MoE 步骤中贪婪地调度一部分跨层工作负载并延迟其余部分，EasyBalance 有效地缓解了跨层工作负载的差异。大量实验表明，EasyBalance 持续加速了分布式 MoE 推理，在大多数配置下将 GPU 的闲置时间减少了 40% 以上。

---

## # EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference

**Authors:** Yize Wu, Ke Gao, Ling Li, Yanjun Wu  
**Published:** August 8, 2026 (ICML 2026)  
**Primary Subject:** Machine Learning (cs.LG)  
**arXiv ID:** [arXiv:2608.07964 [cs.LG]](https://arxiv.org/abs/2608.07964)

> **Authors:** Yize Wu, Ke Gao, Ling Li, Yanjun Wu  
> **Published:** August 8, 2026 (ICML 2026)  
> **Primary Subject:** Machine Learning (cs.LG)  
> **arXiv ID:** [arXiv:2608.07964 [cs.LG]](https://arxiv.org/abs/2608.07964)

---

## 📋 Summary

> ## 📋 Summary

在混合专家（MoE）模型的专家并行分布式推理中，负载均衡已成为一个关键问题。由于路由分布在各个专家之间通常是倾斜的，托管较轻负载专家的设备必须闲置以等待最重的设备完成专家计算，从而导致低效。现有的负载均衡方法主要依赖于每一层内的专家复制或迁移，这引入了额外的开销并限制了它们的灵活性和可扩展性。为了解决这个问题，我们提出了 EasyBalance，这是一种跨层负载均衡策略，它不需要修改专家到设备的映射，从而实现了即时适应性且几乎不会产生额外的开销。我们的核心见解是：（1）其他层的专家可以被视为当前层的天然冗余，以及（2）可以联合执行跨层 MoE 工作负载以减轻其各自的不平衡。基于这些观察，EasyBalance 在每个 MoE 步骤中贪婪地调度一小部分跨层工作负载以运行，并延迟其余工作负载以获得未来的平衡机会，从而有效地利用了跨层不平衡缓解。跨模型、任务和配置的大量实验表明，EasyBalance 持续加速了分布式 MoE 推理，将 GPU 闲置时间减少了大部分超过 40%。代码可在[此链接](https://github.com/yize-wu/EasyInfra)获取。

> In distributed inference of Mixture-of-Experts (MoE) models, expert-parallel load balancing is a major bottleneck. Because token routing distributions across experts are inherently skewed, devices hosting lightly loaded experts are forced to sit idle, waiting for the heaviest-loaded devices to finish computation. Traditional balancing methods rely on intra-layer expert replication or migration, which add significant overhead and scale poorly. 
> 
> To resolve this, the authors introduce **EasyBalance**, a novel cross-layer load balancing strategy. EasyBalance requires **no modifications to expert-device mappings**, allowing for instant adaptability with virtually zero overhead. The approach is built on two core insights:
> 1. Experts in other layers naturally act as redundant computational resources for the current layer.
> 2. Cross-layer MoE workloads can be jointly executed to smooth out individual layer imbalances.
> 
> By greedily scheduling a subset of cross-layer workloads at each MoE step and deferring the rest, EasyBalance effectively mitigates cross-layer workload disparities. Extensive experiments show that EasyBalance consistently accelerates distributed MoE inference, reducing GPU idling time by over 40% in most configurations.

---

## 🛠️ Resources & Links

> ## 🛠️ Resources & Links

* **查看 PDF：** [arXiv:2608.07964 PDF](https://arxiv.org/pdf/2608.07964)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.07964v1)
* **源代码：** [GitHub 仓库 (yize-wu/EasyInfra)](https://github.com/yize-wu/EasyInfra)
* **DOI：** [10.48550/arXiv.2608.07964](https://doi.org/10.48550/arXiv.2608.07964)

> * **View PDF:** [arXiv:2608.07964 PDF](https://arxiv.org/pdf/2608.07964)
> * **HTML Version:** [arXiv HTML (experimental)](https://arxiv.org/html/2608.07964v1)
> * **Source Code:** [GitHub Repository (yize-wu/EasyInfra)](https://github.com/yize-wu/EasyInfra)
> * **DOI:** [10.48550/arXiv.2608.07964](https://doi.org/10.48550/arXiv.2608.07964)

---

## 📑 Abstract

> ## 📑 Abstract

> Load Balancing has emerged as a critical problem in expert-parallel distributed inference of Mixture-of-Experts (MoE) models. As routing distributions are typically skewed across experts, devices hosting lighter-loaded experts must idle to wait for the heaviest during expert computing, leading to inefficiency. Existing load-balancing approaches primarily rely on expert replication or migration within each layer, which introduce additional overhead and limit their flexibility and scalability. To address this problem, we propose EasyBalance, a cross-layer load balancing strategy that requires no modifications to the expert-device mapping, enabling instant adaptability and incurring essentially no additional overhead. Our key insights are that (1) experts of other layers can be viewed as naturally redundant for the current layer, and (2) cross-layer MoE workloads can be jointly executed to mitigate their individual imbalance. Based on these observations, EasyBalance greedily schedules a subset of cross-layer workloads to run at each MoE step and defers the remaining workloads for future balancing opportunities, effectively leveraging cross-layer imbalance mitigation. Extensive experiments across models, tasks, and configurations demonstrate that EasyBalance consistently accelerates distributed MoE inference, reducing GPU idling by mostly over 40%. Code is available at [this link](https://github.com/yize-wu/EasyInfra).

---

*(Note: License icon preserved per system requirements)*
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">