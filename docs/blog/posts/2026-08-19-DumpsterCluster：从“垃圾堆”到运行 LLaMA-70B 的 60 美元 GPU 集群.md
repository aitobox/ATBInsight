---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- GPU
- LLM
- 硬件架构
- 可持续计算
- 成本优化
title: DumpsterCluster：从“垃圾堆”到运行 LLaMA-70B 的 60 美元 GPU 集群
---
### 文章背景与核心概要

随着人工智能数据中心不断淘汰仍具功能的图形硬件，大量高性能加速器流入二手市场。本文探讨了“DumpsterCluster”的概念——一个完全由二手硬件组件从零构建，并已连续运行一年的 128 GPU 计算集群。

该研究评估了将退役 GPU 用于现代大语言模型（LLM）推理的经济与环境可行性。在经济方面，DumpsterCluster 的构建成本仅为 2.2 万美元，远低于 8 卡 B200 系统的 60 万美元，且通过流水线并行优化，实现了极具竞争力的 LLaMA-70B 推理吞吐量。

然而，在环境影响方面，旧硬件的单位 Token 能耗显著更高。研究指出，在电网平均能源结构下，二手系统运行 8B 模型产生的碳排放约为现代硬件的 4 倍，而在运行 70B 模型时则超过 40 倍。作者最终得出结论：单纯的硬件再利用并不足以实现可持续性，必须将其与低碳能源及具有电力成本优势的地区策略性地结合。

---

## 摘要

> As AI datacenters routinely retire functional graphics hardware, massive quantities of capable accelerators find their way into secondary markets. This paper explores the concept of the **"DumpsterCluster"**—a 128-GPU computing cluster built completely from scratch using strictly second-hand hardware components and operated continuously for one year. 

随着人工智能数据中心常规性地淘汰功能完好的图形硬件，大量具备处理能力的加速器流入了二手市场。本文探讨了“DumpsterCluster”的概念——一个完全由二手硬件组件从零构建，并已连续运行一年的 128 GPU 计算集群。

> The study evaluates the economic and environmental viability of repurposing retired GPUs for modern Large Language Model (LLM) inference:
> * **Economic Viability:** At current market pricing ($22K for the DumpsterCluster compared to $600K for an 8-GPU B200 system), the financial benefits are massive. Utilizing pipeline-parallel optimizations, the V100-based cluster achieves competitive LLaMA-70B inference throughput.
> * **Environmental Realities:** Older hardware architectures consume significantly higher energy per token. Consequently, total carbon costs are highly context-dependent. Under grid-average conditions, second-hand systems can produce roughly 4× higher carbon emissions per token for 8B models, and exceeding 40× for 70B models, compared to modern hardware. 

该研究评估了将退役 GPU 用于现代大语言模型（LLM）推理的经济与环境可行性：
* **经济可行性：** 按当前市场价格计算（DumpsterCluster 为 2.2 万美元，而 8 卡 B200 系统为 60 万美元），其财务收益巨大。通过利用流水线并行优化，基于 V100 的集群实现了极具竞争力的 LLaMA-70B 推理吞吐量。
* **环境现实：** 旧硬件架构的单位 Token 能耗显著更高。因此，总碳成本高度依赖于具体环境。在电网平均条件下，二手系统运行 8B 模型产生的单位 Token 碳排放约为现代硬件的 4 倍，而在运行 70B 模型时则超过 40 倍。

> Ultimately, the authors conclude that hardware repurposing is not universally sustainable on its own; it must be strategically paired with low-carbon energy sources and regions offering favorable power economics.

最终，作者得出结论：单纯的硬件再利用本身并不具备普适的可持续性；它必须与低碳能源以及具有电力成本优势的地区进行策略性结合。

---

## 链接与资源

> * [View PDF](https://arxiv.org/pdf/2608.14614)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.14614v1)
> * [TeX Source](https://arxiv.org/src/2608.14614)
> * [DOI Link](https://doi.org/10.48550/arXiv.2608.14614)

* [查看 PDF](https://arxiv.org/pdf/2608.14614)
* [HTML 版本（实验性）](https://arxiv.org/html/2608.14614v1)
* [TeX 源码](https://arxiv.org/src/2608.14614)
* [DOI 链接](https://doi.org/10.48550/arXiv.2608.14614)

### 许可协议

> <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> <span>View License (Creative Commons Attribution 4.0 International)</span>
> </a>

<a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
<span>查看许可协议 (知识共享署名 4.0 国际)</span>
</a>