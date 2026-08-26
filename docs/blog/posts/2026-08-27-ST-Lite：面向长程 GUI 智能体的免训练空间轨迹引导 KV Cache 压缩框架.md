---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- GUI智能体
- KV Cache压缩
- 视觉语言模型
- 边缘计算
- 模型推理优化
title: ST-Lite：面向长程 GUI 智能体的免训练空间轨迹引导 KV Cache 压缩框架
---
### 文章背景与核心概要

ST-Lite 是一款专为视觉语言 GUI 智能体设计的创新型免训练 KV Cache 压缩框架，旨在解决智能体在内存和延迟受限环境下的部署难题。传统的 KV Cache 压缩方法主要针对通用语言任务，在 GUI 场景下往往表现不佳，在标准预算下仅能保留约 39% 的关键 KV 对。

该研究深入分析了 GUI 任务的三大核心工作负载特性：高帧间视觉冗余、极小的 UI 元素空间占用以及近乎均匀的跨层注意力稀疏性。针对这些特性，ST-Lite 引入了轨迹感知语义门控（TSG）、组件中心空间显著性（CSS）和扁平化层级预算分配策略。实验表明，在七个 GUI 基准测试中，ST-Lite 在 20% 的缓存预算下即可达到甚至超过全量缓存的准确率，并实现了高达 2.35 倍的解码加速。

---

## 论文概览

| 领域 | 详情 |
| :--- | :--- |
| **标题** | ST-Lite: Training-Free KV Cache Compression with Spatio-Trajectory Guidance for Long-Horizon GUI Agents |
| **作者** | Bowen Zhou, Zhou Xu, Wanli Li, Jingyu Xiao, Pingan Gan, Haoqian Wang |
| **主要学科** | 计算机视觉与模式识别 (`cs.CV`) |
| **次要学科** | 人工智能 (`cs.AI`), 机器学习 (`cs.LG`) |
| **状态** | 已被 EMNLP 2026 Findings 录用 (最终版，37 页) |
| **arXiv 标识符** | [arXiv:2603.00188](https://arxiv.org/abs/2603.00188) |
| **官方仓库** | [GitHub - ST-Lite](https://github.com/94wen94/ST-Lite) |

> | Field | Details |
> | :--- | :--- |
> | **Title** | ST-Lite: Training-Free KV Cache Compression with Spatio-Trajectory Guidance for Long-Horizon GUI Agents |
> | **Authors** | Bowen Zhou, Zhou Xu, Wanli Li, Jingyu Xiao, Pingan Gan, Haoqian Wang |
> | **Primary Subject** | Computer Vision and Pattern Recognition (`cs.CV`) |
> | **Secondary Subjects** | Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`) |
> | **Status** | Accepted to Findings of EMNLP 2026 (Camera-ready, 37 pages) |
> | **arXiv Identifier** | [arXiv:2603.00188](https://arxiv.org/abs/2603.00188) |
> | **Official Repository** | [GitHub - ST-Lite](https://github.com/94wen94/ST-Lite) |

---

## 摘要

在内存和延迟受限的情况下部署视觉语言 GUI 智能体时，免训练 KV Cache 压缩至关重要。然而，现有的压缩方法大多是为通用语言工作负载设计的，忽略了 GUI 交互轨迹的独特结构。

> Training-free KV cache compression is essential for deploying vision-language GUI agents under memory and latency constraints, yet existing methods are designed for generic language workloads and ignore the distinctive structure of GUI interaction traces. 

作者总结了导致现有方案在 20% 标准预算下仅能保留约 39% 重要 KV 对的**三个 GUI 特有工作负载属性**：
1. 高帧间视觉冗余。
2. 极小的 UI 元素空间占用。
3. 近乎均匀的跨层注意力稀疏性。

> The authors characterize **three GUI-specific workload properties** that cause existing schemes to retain as few as 39% of oracle-important KV pairs at the standard 20% budget:
> 1. High inter-frame visual redundancy.
> 2. Extremely small UI-element spatial footprints.
> 3. Near-uniform cross-layer attention sparsity.

为了解决这些局限性，**ST-Lite** 引入了一种免训练压缩方案，其每个组件都针对特定属性进行优化：
* **轨迹感知语义门控 (TSG)：** 过滤冗余的历史帧。
* **组件中心空间显著性 (CSS)：** 保留细粒度的元素边界。
* **扁平化层级预算 (Flat Per-Layer Budget)：** 避免层级分配失误。

> To address these limitations, **ST-Lite** introduces a training-free compression scheme where each component targets a specific property:
> * **Trajectory-aware Semantic Gating (TSG):** Filters redundant historical frames.
> * **Component-centric Spatial Saliency (CSS):** Preserves fine-grained element boundaries.
> * **Flat Per-Layer Budget:** Avoids hierarchical misallocation.

在 10%–40% 的部署相关预算窗口内，ST-Lite 在七个 GUI 基准测试和两个骨干网络上始终优于所有现有的压缩基线。在 20% 的预算下，它在主干网络上的任务准确率达到或超过了全量缓存（Full Cache），同时在五倍压缩下实现了高达 **2.35 倍的解码加速**。

> Across seven GUI benchmarks and two backbones in the deployment-relevant 10%–40% window, ST-Lite consistently outperforms all existing compression baselines. It matches or exceeds Full Cache task accuracy on the primary backbone at the 20% budget while delivering up to a **2.35× decoding speedup** at fivefold compression.

---

## 提交历史

* **[v1]** 2026 年 2 月 27 日，星期五，01:27:20 UTC *(11,919 KB)*
* **[v2]** 2026 年 8 月 25 日，星期二，15:47:14 UTC *(7,263 KB)* — *当前版本*

> * **[v1]** Fri, 27 Feb 2026 01:27:20 UTC *(11,919 KB)*
> * **[v2]** Tue, 25 Aug 2026 15:47:14 UTC *(7,263 KB)* — *This current version*

---

## 获取资源

* [查看 PDF](https://arxiv.org/pdf/2603.00188)
* [实验性 HTML 版本](https://arxiv.org/html/2603.00188v2)
* [TeX 源码文件](https://arxiv.org/src/2603.00188)
* [查看许可协议](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

> * [View PDF](https://arxiv.org/pdf/2603.00188)
> * [Experimental HTML Version](https://arxiv.org/html/2603.00188v2)
> * [TeX Source Files](https://arxiv.org/src/2603.00188)
> * [View License](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)