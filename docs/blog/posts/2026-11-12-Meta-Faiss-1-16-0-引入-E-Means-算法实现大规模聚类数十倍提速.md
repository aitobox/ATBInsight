---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-12
hide:
  - navigation
tags:
  - Faiss
  - Meta
  - 聚类算法
  - 向量检索
  - E-Means
  - GPU加速
title: "Meta Faiss 1.16.0 引入 E-Means 算法：实现大规模聚类数十倍提速"
---

# Meta Faiss 1.16.0 引入 E-Means 算法：实现大规模聚类数十倍提速

![Meta Faiss 1.16.0](./images/14425fdba477.jpg)

### 文章背景与核心概要
在大语言模型与多模态 AI 时代，海量高维向量数据 (Embeddings) 的索引检索、量化压缩与清洗整理无处不在，而聚类算法是这一系列数据管线中最关键的基石。然而，沿用了数十年的经典 Lloyd k-means 算法在面对十亿乃至百亿规模的向量时，全量数据集迭代需要消耗巨大的显存与数以千计的 GPU 计算耗时。Meta 旗下 FAIR 团队联合巴黎高科路桥大学 (École Nationale des Ponts et Chaussées) 在全新发布的 Faiss 1.16.0 中正式推出了革命性的 e-means 算法。该算法通过小批次指数衰减更新机制与无需调参的自适应缩放法则，仅需 1.4 至 2.6 个轮次即可追平传统算法 25 轮的收敛精度，在 GPU 上带来高达 10 至 45 倍的端到端提速，更以极低成本完成了 100 亿级向量的超大规模聚类。

---

## 概述

> ## Summary

Meta 正式发布了 **Faiss 1.16.0**，带来了由 Meta 旗下 FAIR 实验室与法国巴黎高科路桥大学 (École Nationale des Ponts et Chaussées) 联合打造的全新 **e-means** 聚类算法。为了突破海量高维向量量化与数据整理中的算力瓶颈，e-means 彻底摒弃了传统 Lloyd k-means 繁重的数据集全量遍历，转而采用小批次 (mini-batch) 配合指数衰减的累加和与计数更新机制。研究表明，这项新技术仅需极少数训练轮次便能达到更低的损失值——只需 1.4 至 2.6 轮就能匹敌传统 Lloyd 算法运行 25 轮的精度，同时带来 10 至 45 倍的 GPU 端到端实际用时加速。本次发布包含完整的 CPU、GPU 及分布式运行方案，集成了 Triton 和 CuTe 高性能计算内核，并全面支持规模高达 100 亿条向量级超大数据集的处理工具链。

> Meta has released **Faiss 1.16.0**, introducing the **e-means** clustering algorithm developed by FAIR at Meta and École Nationale des Ponts et Chaussées. Designed to accelerate large-scale vector quantization and data curation, e-means replaces traditional Lloyd k-means iterations with exponentially decayed sums and counts from mini-batches. According to researchers, the new method achieves lower loss in a fraction of the epochs (reaching 25-epoch Lloyd accuracy in just 1.4 to 2.6 epochs) while delivering 10–45× GPU wall-clock speedups. The release includes full CPU, GPU, and distributed implementations, Triton and CuTe assignment backends, and tooling for datasets scaling up to 10 billion vectors.

---

## E-Means 如何更新聚类中心

> ## How E-Means Updates Centroids

K-means 聚类算法的核心目标是最小化各向量与其所属最近质心 (聚类中心) 之间的均方距离，这是信息检索、向量量化以及大规模数据整理中至关重要的底层操作。经典的 Lloyd 算法在每次迭代中必须将所有数据点分配给最近的质心，随后遍历完整数据集重新计算聚类统计量，计算代价极其昂贵；而 **e-means** 则采用了更巧妙高效的更新路径：

> K-means clustering minimizes the mean squared distance between vectors and their nearest centroid, a critical operation for retrieval, quantization, and data curation. While traditional Lloyd’s algorithm assigns every point to its nearest centroid and rebuilds cluster statistics from the full dataset, **e-means** takes a more efficient approach:

* **指数衰减更新机制 (Exponentially Decayed Updates)**：算法仅基于小批次数据持续更新运行中的累加和与样本计数，使较早批次的分配结果权重随时间呈指数级衰减，平滑降低其对当前聚类中心的影响。
* **自适应缩放法则 (Automatic Scaling Laws)**：内置两套拟合好的经验缩放法则，能够根据数据集规模、聚类簇数量以及预设的轮次预算，自动推导最佳批次大小与初始步长，免去了繁琐的手工超参数调优。同时结合余弦退火策略，随训练推进平滑递减步长。
* **死簇复活策略 (Cluster Revival)**：算法通过分裂活跃的供体簇 (donor cluster) 来激活并重置失效或利用率极低的“死簇”；在最后一个训练轮次中，每个簇则会严格采用最终分配样本的真实均值进行精确收尾。

> * **Exponentially Decayed Updates:** It updates running sums and counts from mini-batches, allowing older assignments to gradually lose influence. 
> * **Automatic Scaling Laws:** Two fitted scaling laws derive batch sizes and initial step sizes automatically based on dataset size, cluster count, and epoch budgets, removing the need for separate hyperparameter tuning. A cosine schedule gradually reduces the step size over time.
> * **Cluster Revival:** The algorithm prevents dead or underused clusters by splitting a donor cluster, finalizing each cluster with its exact mean over the final epoch's assignments.

研究团队通过多达 75,000 次优化运行拟合了这些缩放法则。在留出数据集 (held-out dataset) 测试中，步长缩放法则的中位数后悔值 (regret) 仅为 0.07%，而默认批次法则的后悔值也仅有 0.19%，展现出极高的一致性与泛化能力。

> Researchers fitted these scaling laws using 75,000 optimization runs, reporting a median held-out-dataset regret of just 0.07% for the step law and 0.19% for the default batch law.

---

## 基准测试：直面百亿级向量挑战

> ## Benchmarks Extend to Ten Billion Vectors

在 NVIDIA H100 GPU 与多核 Intel Xeon CPU 上的多项验证基准测试充分展示了 e-means 的巨大性能跃升：

> Validation tests on H100 and multi-core Xeon CPUs demonstrated massive efficiency gains:

* 在横跨 11 项 VIBE 向量嵌入基准测试中，e-means 仅耗费 **1.6 至 2.6 个轮次** 便达到了标准 Lloyd 算法运行 25 个轮次的同等误差水平。
* 在单块 H100 GPU 上，相比 Flash-KMeans 实现了 **8.0 至 22.8 倍的加速**；在配备 64 核 CPU 的服务器上，相比标准 Faiss 实现了 **9.0 至 15.0 倍的加速**。

> * Across 11 VIBE embedding tests, e-means reached standard Lloyd 25-epoch error levels in just **1.6 to 2.6 epochs**.
> * It achieved **8.0× to 22.8× speedups** against Flash-KMeans on a single H100 GPU, and **9.0× to 15.0× speedups** against standard Faiss running on 64 CPU cores.

### 超大规模验证：DINO10B 百亿向量集

> ### Massive Scale: DINO10B

在极限规模测试中，研究人员对庞大的 **DINO10B** 数据集进行了聚类划分——该数据集由 100 亿条 1,024 维的图像块向量嵌入 (patch embeddings) 构成。e-means 仅用了 2.5 个轮次就将其成功划分为约 1,670 万个聚类簇：

> At the extreme scale, researchers partitioned **DINO10B**—consisting of 10 billion 1,024-dimensional patch embeddings—into roughly 16.7 million clusters in 2.5 epochs:

* **精确分配 (Exact Assignment)**：通过 32 台机器共消耗 779 GPU·小时，测试误差即略微优于运行 25 轮的 Lloyd 基线水平。
* **倒排文件分配 (Inverted-File / IVF Assignment)**：借助 IVF 索引进行近似最近邻质心搜索，仅在一台 8 卡 GPU 机器上耗费 **23.2 GPU·小时**、迭代 3 个轮次便成功超越基线水平。这充分证明在百亿向量级别下，近似分配方案的算力成本比精确方案便宜约 34 倍。

> * **Exact Assignment:** Reached test error slightly lower than the 25-epoch Lloyd baseline using 779 GPU-hours across 32 machines.
> * **Inverted-File (IVF) Assignment:** Using approximate nearest-centroid search through an IVF index, the process crossed the baseline after three epochs using only **23.2 GPU-hours** on a single eight-GPU machine, proving that approximate assignment is roughly 34× cheaper at a ten-billion-vector scale.

---

## 可用性与已知限制

> ## Availability and Documented Limits

Faiss 1.16.0 为这一全新聚类范式提供了开箱即用的支持：

> Faiss 1.16.0 provides out-of-the-box support for the new clustering paradigm:

* **API 接口**：官方用户指南提供了面向 NumPy 数组的 `NumpyEmeans` 以及面向 PyTorch 张量的 `Emeans`。
* **硬件后端**：CPU 执行由 Faiss 直接管理，而 GPU 执行则基于支持 CUDA 的 PyTorch 构建 (在 H100 / H200 上使用 CuTe 内核，在其他受支持的 NVIDIA 硬件上使用 Triton 内核)。
* **多 GPU 支持**：框架内置副本质心 (replicated-centroid) 与分片质心 (sharded-centroid) 类来协调多卡训练。例如，1,600 万个质心的 FP32 累加和需要占用约 64 GiB 显存，因此在超大规模场景下分片管理至关重要。

> * **APIs:** The official user guide offers `NumpyEmeans` for NumPy data and `Emeans` for PyTorch tensors.
> * **Hardware Backends:** CPU execution is handled directly by Faiss, while GPU execution leverages CUDA-enabled PyTorch (using CuTe kernels on H100/H200 and Triton on other supported NVIDIA hardware).
> * **Multi-GPU Support:** Replicated- and sharded-centroid classes manage multi-GPU training. For instance, FP32 sums for 16 million centroids consume about 64 GiB, making sharding essential at massive scales.

### 官方使用注意事项

> ### Documented Caveats

* **低维数据局限**：内置缩放法则专为高维数据优化，在微型或低维数据集上的效果相对较弱 (当特征维度低于特定阈值时，默认配置会自动调整或直接禁用死簇复活机制)。
* **训练标签分配**：算法返回的训练集类别标签来自于最后一次遍历中的分配结果，并不一定严格等同于最终收敛质心的最近邻归属。
* **输入合法性校验**：GPU 流水线默认不会显式检查输入数据中是否存在 `NaN` 或无穷大 (infinite) 异常值。

> * **Low Dimensions:** The scaling laws were optimized for high-dimensional data and are less effective on tiny or low-dimensional datasets (defaults automatically adjust or disable cluster revival below specific dimension thresholds).
> * **Training Labels:** Returned training labels originate from the final pass and do not necessarily represent assignments to the final calculated centroids.
> * **Input Checks:** The GPU pipeline does not explicitly check inputs for `NaN` or infinite values.

---

*本文基于 Meta 旗下 FAIR 团队与巴黎高科路桥大学 (École Nationale des Ponts et Chaussées) 最初发表的研究成果编写。*

> *Article based on research originally published by FAIR at Meta and École Nationale des Ponts et Chaussées.*
