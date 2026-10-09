---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-10
hide:
  - navigation
tags:
  - Mooncake
  - Kimi
  - Moonshot AI
  - KVCache
  - 分离式架构
  - 大语言模型服务
  - arXiv论文
title: "Mooncake：面向大模型服务的 KVCache 中心化分离架构设计与 Kimi 生产实战"
---

# Mooncake：面向大模型服务的 KVCache 中心化分离架构设计与 Kimi 生产实战

> # Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving

> **arXiv:2407.00079** [cs.DC, cs.AI, cs.AR]  
> **Subjects:** Distributed, Parallel, and Cluster Computing (cs.DC); Artificial Intelligence (cs.AI); Hardware Architecture (cs.AR)  
> **Authors:** Ruoyu Qin, Zheming Li, Weiran He, Mingxing Zhang, Yongwei Wu, Weimin Zheng, Xinran Xu  
> **Submission Date:** June 24, 2024 (Last revised: October 8, 2026)  
> **DOI / Paper:** [arXiv:2407.00079](https://arxiv.org/abs/2407.00079)

### 文章背景与核心概要

在大语言模型 (Large Language Model, LLM) 迈向超长文本与高并发服务的演进过程中，传统的单体推理架构受限于 Prefill 计算密集与 Decoding 访存受限两者之间的资源争抢，难以在保证极致吞吐量的同时守住严苛的延迟服务等级目标 (Service Level Objectives, SLOs) 。作为支撑 Moonshot AI 旗下旗舰产品 Kimi 的核心服务系统，Mooncake 突破性地提出了以 KVCache 为中心的分离式架构 (KVCache-Centric Disaggregated Architecture) ，将首字填充预处理集群与自回归解码集群进行物理隔离。该平台创新性地盘活了 GPU 服务器中原本闲置的主机 CPU、DRAM 内存与本地 SSD 固态硬盘，构建起超大容量的分离式 KVCache 共享存储层与自适应调度中心，并配合前瞻性的过载早期拒绝机制确保流量洪峰下的系统鲁棒性。在生产实践中，Mooncake 不仅在模拟评测中取得了高达 525% 的有效吞吐量飞跃，更直接赋能 Kimi 在真实高负载业务中提升了 75% 的并发请求承载能力，为全球大模型工业级工程化部署提供了标杆范式。

---

## 内容概要

> ## Summary

**Mooncake** 是支撑由 Moonshot AI 研发的知名大语言模型 (Large Language Model, LLM) 服务 **Kimi** 的底层推理平台。该平台创新性地引入了全新的**以 KVCache 为中心的分离式架构 (KVCache-Centric Disaggregated Architecture)** ，专为高效应对高并发、长上下文的大模型业务负载而量身打造。通过将 Prefill (首字填充预处理) 与 Decoding (自回归生成解码) 集群进行物理拆分，并充分调用 GPU 集群中闲置的 CPU、DRAM 内存与本地 SSD 固态硬盘资源构建分离式 KVCache 存储层，Mooncake 在严守延迟服务等级目标 (Service Level Objectives, SLOs) 的前提下，将系统的整体有效吞吐量推向了极致。此外，它还配备了基于预测的过载请求早拒策略，从容应对超高负载流量洪峰。实验结果表明，在模拟场景下 Mooncake 的系统吞吐量提升高达 **525%** ，在真实生产负载中更是将系统的并发请求承载能力提升了 **75%** 。

> **Mooncake** is the serving platform powering **Kimi**, a prominent Large Language Model (LLM) service developed by Moonshot AI. The platform introduces a novel, **KVCache-centric disaggregated architecture** designed specifically to handle high-load, long-context LLM workloads efficiently. By separating prefill and decoding clusters and utilizing underutilized CPU, DRAM, and SSD resources across the GPU cluster as a disaggregated KVCache layer, Mooncake maximizes effective throughput while strictly adhering to latency Service Level Objectives (SLOs). Additionally, it features a prediction-based early rejection policy to gracefully manage severely overloaded scenarios. Experimental results demonstrate up to a **525% increase in throughput** in simulated scenarios and a **75% increase in request capacity** under real-world workloads.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 编号：** [arXiv:2407.00079](https://arxiv.org/abs/2407.00079) [cs.DC]
* **主要学科分类：** 分布式、并行与集群计算 (`cs.DC`)
* **其他学科分类：** 人工智能 (`cs.AI`) 、计算机硬件架构 (`cs.AR`)
* **提交日期：** 2024年6月24日 (最新修订：2026年10月8日) 
* **论文作者：** 
  * Ruoyu Qin
  * Zheming Li
  * Weiran He
  * Mingxing Zhang
  * Yongwei Wu
  * Weimin Zheng
  * Xinran Xu

> * **arXiv Identifier:** [arXiv:2407.00079](https://arxiv.org/abs/2407.00079) [cs.DC]
> * **Primary Subject:** Distributed, Parallel, and Cluster Computing (`cs.DC`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Hardware Architecture (`cs.AR`)
> * **Submission Date:** June 24, 2024 (Last revised: October 8, 2026)
> * **Authors:** 
>   * Ruoyu Qin
>   * Zheming Li
>   * Weiran He
>   * Mingxing Zhang
>   * Yongwei Wu
>   * Weimin Zheng
>   * Xinran Xu

---

## 论文摘要

> ## Abstract

Mooncake 是为 Moonshot AI 旗下的前沿大模型服务 Kimi 量身定制的高性能推理服务平台。它采用了以 KVCache 为中心的分离式架构，将计算密集型的 Prefill 集群与访存密集型的 Decoding 集群进行了解耦拆分；同时，它充分挖掘并复用了 GPU 集群中常态化闲置的 CPU、DRAM 以及本地 SSD 资源，构建起分布式的 KVCache 共享缓存池。Mooncake 的技术核心在于其以 KVCache 为中心的自适应调度器，能够在严格满足延迟相关的服务等级目标 (SLOs) 的同时，最大化系统的整体有效吞吐量。与以往假设所有请求都能够被完全处理的传统学术研究不同，Mooncake 在工业界真实落地中必须直面极端的高并发过载冲击。为此，我们设计了一套基于预测的过载早拒策略以从容化解雪崩风险。实验表明，Mooncake 在超长上下文场景下表现尤为亮眼：相比基线方案，Mooncake 在满足 SLOs 的约束下，特定仿真场景中的吞吐量提升高达 525%；而在真实的生产环境流量下，这一创新架构帮助 Kimi 额外承载了 75% 的用户请求量。

> Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. It features a KVCache-centric disaggregated architecture that separates the prefill and decoding clusters. It also leverages the underutilized CPU, DRAM, and SSD resources of the GPU cluster to implement a disaggregated cache of KVCache. The core of Mooncake is its KVCache-centric scheduler, which balances maximizing overall effective throughput while meeting latency-related Service Level Objectives (SLOs). Unlike traditional studies that assume all requests will be processed, Mooncake faces challenges due to highly overloaded scenarios. To mitigate these, we developed a prediction-based early rejection policy. Experiments show that Mooncake excels in long-context scenarios. Compared to the baseline method, Mooncake can achieve up to a 525% increase in throughput in certain simulated scenarios while adhering to SLOs. Under real workloads, Mooncake's innovative architecture enables Kimi to handle 75% more requests.

---

## 核心特性与架构亮点

> ## Key Features & Architecture Highlights

1. **Prefill 与 Decoding 分离架构 (Disaggregated Prefill and Decoding) ：**
   将计算密集型的首字填充 (Prefill) 阶段与显存带宽受限的自回归解码 (Decoding) 阶段彻底解耦部署到独立的计算集群中，从而实现硬件资源利用率的最优配置。
2. **分离式 KVCache 存储层 (Disaggregated KVCache Layer) ：**
   全面盘活并复用 GPU 机器节点内部未充分利用的辅助硬件资源 (包括主机 CPU、DRAM 内存和本地 SSD 硬盘) ，构建起超大规模、高效流转的分布式 KVCache 缓存体系。
3. **以 KVCache 为核心的智能调度器 (KVCache-Centric Scheduler) ：**
   全局感知长文本 KVCache 的分布与网络传输开销，在严格保障端到端延迟服务等级目标 (SLOs) 的底线之上，智能最大化集群的实际有效吞吐量。
4. **基于预测的过载早拒策略 (Prediction-Based Early Rejection Policy) ：**
   在突发流量洪峰与极端过载场景下，提前预测请求能否在满足 SLOs 的前提下顺利完成；对注定超时的请求果断执行早期拒绝，避免算力资源被无谓浪费与系统雪崩。

> 1. **Disaggregated Prefill and Decoding:**
>    Separates compute-heavy prefill phases from memory-bound decoding phases into distinct clusters, optimizing hardware utilization.
> 2. **Disaggregated KVCache Layer:**
>    Leverages underutilized hardware resources (CPU, DRAM, and SSD) within the GPU cluster to store and manage KVCache efficiently.
> 3. **KVCache-Centric Scheduler:**
>    Intelligently balances overall effective throughput while respecting strict latency-related SLOs.
> 4. **Prediction-Based Early Rejection Policy:**
>    Gracefully handles extreme, overloaded traffic scenarios by predicting feasibility and rejecting requests early rather than failing under resource exhaustion.
