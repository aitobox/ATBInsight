---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 内存管理
- 企业数据检索
- RAG
- 动态多级层次结构
- 深度学习
title: MEMONDEMAND：面向大规模企业数据的内存管理系统
---
### 文章背景与核心概要
随着大规模、异构且持续更新的企业数据急剧增长，传统检索系统在处理复杂业务数据时面临着严重的内存瓶颈和效率低下问题。为了应对这一挑战，本文提出了 MEMONDEMAND（按需内存管理系统），这是一个专为大规模企业数据设计的新型内存管理框架。该系统通过构建特定集合的层次结构、低成本路由、详细证据加载以及工作负载感知的内存更新，提供了一个统一的解决方案。

MEMONDEMAND 的核心技术创新在于其动态多级层次结构和双内存架构，能够在每个层级上将精简的路由信息与详细证据进行隔离。此外，系统通过按需内存提升机制动态更新节点优先级，同时保持有限的活跃状态预算，从而确保了极高的运行效率。在 EnterpriseRAG-Bench、FinanceBench 和 HotpotQA 等多个基准测试中，该系统在各种数据规模下均展现出卓越的性能和通用性。

---

# MEMONDEMAND: A Memory Management System for Large-Scale Enterprise Data

**Authors:** Xinyuan Song, Bowen Zhu, Hasibul Haque, Liang Zhao  
**Date:** August 22, 2026  
**Primary Subject:** Artificial Intelligence (cs.AI)  
**arXiv ID:** [2608.22141](https://arxiv.org/abs/2608.22141)

> # MEMONDEMAND: A Memory Management System for Large-Scale Enterprise Data
> 
> **Authors:** Xinyuan Song, Bowen Zhu, Hasibul Haque, Liang Zhao  
> **Date:** August 22, 2026  
> **Primary Subject:** Artificial Intelligence (cs.AI)  
> **arXiv ID:** [2608.22141](https://arxiv.org/abs/2608.22141)

---

## Summary
MEMONDEMAND（按需内存）是一种新颖的内存管理系统，旨在解决处理大规模、异构且持续更新的企业数据所带来的挑战。与现有检索系统不同，它为特定集合的层次结构构建、低成本路由、详细证据加载以及工作负载感知的内存更新提供了一个统一的框架。通过利用动态多级层次结构和双内存架构，该系统在各种数据规模和检索基准（包括 EnterpriseRAG-Bench、FinanceBench 和 HotpotQA）中实现了卓越的性能。

> ## Summary
> **MEMONDEMAND** (On-Demand Memory) is a novel memory management system designed to address the challenges of handling large-scale, heterogeneous, and continuously updated enterprise data. Unlike existing retrieval systems, it provides a unified framework for collection-specific hierarchy construction, low-cost routing, detailed evidence loading, and workload-aware memory updates. By utilizing a dynamic multi-level hierarchy and dual-memory architecture, the system achieves superior performance across various data scales and retrieval benchmarks, including EnterpriseRAG-Bench, FinanceBench, and HotpotQA.

---

## Key Mechanisms
该系统通过三个协同机制运行：

1. **动态多级层次结构：** 为每个单独的数据集合确定最优的抽象结构和深度。
2. **双内存架构：** 在每个层次结构级别实现双层系统，将精简的路由信息与详细证据相隔离。
3. **按需内存提升：** 动态更新节点优先级，同时维持有限的活跃状态预算以确保效率。

> ## Key Mechanisms
> The system operates through three coordinated mechanisms:
> 
> 1.  **Dynamic Multi-level Hierarchy:** Determines the optimal abstraction structure and depth for each individual data collection.
> 2.  **Dual Memory Architecture:** Implements a two-tier system at every hierarchy level, separating distilled routing information from detailed evidence.
> 3.  **On-Demand Memory Promotion:** Updates node priority dynamically while maintaining a bounded active-state budget to ensure efficiency.

---

## Performance Highlights
MEMONDEMAND 相比现有的最先进解决方案展现出了显著的改进：
* **可扩展性：** 在从 10M 标记（tokens）到完整的 618M 标记集合的每一个规模上，均超越了最强大的已发布基准。
* **效率：** 在 10M 规模下实现了 **12.23%** 的性能提升，在 618M 规模下实现了 **4.66%** 的性能提升。
* **通用性：** 证明了其在金融分析、多跳推理和事实检索等多样化领域中的有效性。

> ## Performance Highlights
> MEMONDEMAND has demonstrated significant improvements over existing state-of-the-art solutions:
> *   **Scalability:** Outperforms the strongest published benchmarks at every scale, ranging from 10M tokens to the full 618M-token collection.
> *   **Efficiency:** Achieved performance gains of **12.23%** at the 10M scale and **4.66%** at the 618M scale.
> *   **Versatility:** Proven effectiveness across diverse domains, including financial analysis, multi-hop reasoning, and fact-retrieval tasks.

---

## Resources
* **论文访问：** [查看 PDF](https://arxiv.org/pdf/2608.22141)
* **源代码：** [GitHub 仓库](https://github.com/xfab-xinyuansong/MemOnDemand.git)
* **许可证：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ## Resources
> *   **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.22141)
> *   **Source Code:** [GitHub Repository](https://github.com/xfab-xinyuansong/MemOnDemand.git)
> *   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
> 
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">