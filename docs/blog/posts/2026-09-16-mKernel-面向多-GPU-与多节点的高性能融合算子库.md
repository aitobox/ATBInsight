---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-16
hide:
  - navigation
tags:
  - 融合算子
  - 多GPU协同
  - 分布式计算
  - mKernel
title: "mKernel：面向多 GPU 与多节点的高性能融合算子库"
---

# mKernel：面向多 GPU 与多节点的高性能融合算子库

> # mKernel: Fast Multi-GPU, Multi-Node Fused Kernels

> **arXiv:** [2609.13585](https://arxiv.org/abs/2609.13585) [cs.DC]  
> **Submitted on:** 11 September 2026  
> **Authors:** Ziming Mao, Yihan Zhang, Shawn Wei Chew, Shuang Ma, Costin Raiciu, Yang Zhou, Scott Shenker, Ion Stoica  

### 文章背景与核心概要

随着大语言模型与前沿 AI 架构的参数规模不断攀升，单张显卡早已不堪重负，分布式训练与多卡推理已成为现代深度学习系统的基石。然而，跨 GPU 以及跨服务器节点之间的数据通信，往往是制约整体运行速度的严重瓶颈。传统方案通常在算子级别通过独立流来实现计算与通信重叠，带来的性能增益十分有限；而此前更高效的融合算子又普遍局限于单台机器内部的 NVLink 互联范围。为此，研究团队推出了 **mKernel** 算子库，首次在分块 (Tile) 粒度上实现了计算、节点内 NVLink 通信与跨节点 RDMA 网络传输的无缝流水线重叠。在 16 卡 H200 集群上的测试表明，mKernel 在 GEMM+AllReduce 和 Ring Attention 等核心算子上分别取得了高达 1.72 倍和 1.88 倍的显著加速，为大规模分布式 AI 系统的性能调优开辟了全新路径。

---

## 📌 概述

> ## 📌 Summary

在训练和部署庞大的机器学习模型时，多卡之间的数据通信开销往往是拖慢整体运行速度的头号瓶颈。传统的系统级优化方法通常是在粗粒度的算子级别尝试重叠通信与计算 (例如分配不同的 CUDA 流) ，但这种方式能够挤出的性能提升十分有限。相比之下，融合算子 (Fused Kernel) 的表现更为亮眼——它能在 GPU 刚算完一小块数据 (Tile) 时就立刻将其发走，从而极大掩盖通信延迟；然而，此前的融合算子技术基本都被局限在单台服务器内部的 NVLink 高速互联范围内，无法直接扩展到多机集群的广阔天地。

> Communication bottlenecks significantly hinder the distributed training and inference of large machine learning models. Traditional approaches that overlap communication with computation at the kernel granularity (using separate streams) yield only limited performance improvements. While fused kernels perform better by transmitting output tiles immediately upon production, their adoption has largely been restricted to a single NVLink domain.

为了打破这一限制，本文推出了全新的多 GPU、多节点融合算子库 **mKernel**。它专为大规模分布式集群环境打造，首次在细粒度的“数据分块 (Tile) ”层面上，将核心计算任务、单机节点内的 NVLink 互联通信以及节点间的跨机 RDMA 网络传输无缝重叠在一起。

> This paper introduces **mKernel**, a novel library of multi-GPU, multi-node fused kernels designed to seamlessly overlap computation, intra-node NVLink communication, and inter-node RDMA at tile granularity. 

### 核心创新点

> ### Key Innovations:

* **自适应 SM 资源划分 (Adaptive SM Partitioning) ：** 常驻算子将 GPU 流式多处理器 (Streaming Multiprocessors, SM) 灵活划分为专门负责“计算”与专门负责“通信”两类角色。GPU 板载控制器会在运行时根据具体执行的算子类型与输入张量形状，动态调配两者的比例，确保硬件资源始终物尽其用。
* **分层数据传输调度 (Hierarchical Data Movement) ：** 采用分层拓扑精心编排数据搬运流程，优先在单机内的高速总线上流转数据，最大程度减少跨机网络的通信流量。
* **GPU 驱动的直接网络访问 (GPU-Driven Network Access) ：** 通过轻量级命令队列以及基于 RDMA verbs 构建的宿主机代理，直接由 GPU 发起并驱动网络通信，能够无缝兼容任意主流网络后端 (例如 InfiniBand 和 AWS EFA) 。有趣的是，研究团队在实验中发现，相较于这种由 GPU 发起、宿主机轻度协同的通信架构，英伟达官方的 GPUDirect Async (IBGDA) 带来的额外收益其实微乎其微。
* **显著的性能飞跃 (Significant Performance Gains) ：** 研发团队在涵盖张量并行 (TP) 、序列并行 (SP) 以及专家并行 (EP) 的 5 类典型算子上实现了 mKernel。在包含 16 张 NVIDIA H200 GPU 的跨节点测试集群中，**mKernel** 在 GEMM+AllReduce 算子上取得了高达 **$1.72\times$** 的加速，而在长上下文至关重要的 Ring Attention 算子上更是取得了最高 **$1.88\times$** 的惊人性能提升。

> * **Adaptive SM Partitioning:** Persistent kernel streaming multiprocessors (SMs) are partitioned into compute and communication roles. An on-GPU controller dynamically tunes this partition at runtime based on the specific kernel and input shape.
> * **Hierarchical Data Movement:** Structures data movement hierarchically to minimize traffic across the inter-node network.
> * **GPU-Driven Network Access:** Drives the network directly from the GPU via a lightweight command queue and a host proxy built on RDMA verbs, supporting any network backend (such as InfiniBand and AWS EFA). Interestingly, the authors observed that GPUDirect Async (IBGDA) offers minimal additional benefit over host-assisted, GPU-initiated communication.
> * **Significant Performance Gains:** Implemented across five kernels spanning tensor, sequence, and expert parallelism. On two 16-GPU H200 clusters, **mKernel** achieves speedups of up to **$1.72\times$** on GEMM+AllReduce and **$1.88\times$** on Ring Attention.

---

## 📋 论文元数据

> ## 📋 Metadata

* **研究领域：** 分布式、并行与集群计算 (`cs.DC`) ；人工智能 (`cs.AI`) ；机器学习 (`cs.LG`) ；网络与互联网架构 (`cs.NI`)
* **DOI 标识：** [10.48550/arXiv.2609.13585](https://doi.org/10.48550/arXiv.2609.13585)
* **开源许可：** [知识共享署名 4.0 国际许可协议 (CC BY 4.0) ](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **Subjects:** Distributed, Parallel, and Cluster Computing (`cs.DC`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`); Networking and Internet Architecture (`cs.NI`)
> * **DOI:** [10.48550/arXiv.2609.13585](https://doi.org/10.48550/arXiv.2609.13585)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 🔗 全文与相关资源

> ## 🔗 Full-Text & Resources

* [查看 PDF 论文](https://arxiv.org/pdf/2609.13585)
* [查看 HTML 网页版 (实验性预览) ](https://arxiv.org/html/2609.13585v1)
* [TeX 源码](https://arxiv.org/src/2609.13585)
* **学术分析工具：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.13585) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.13585) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.13585)

> * [View PDF](https://arxiv.org/pdf/2609.13585)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.13585v1)
> * [TeX Source](https://arxiv.org/src/2609.13585)
> * **Associated Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.13585) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.13585) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.13585)
