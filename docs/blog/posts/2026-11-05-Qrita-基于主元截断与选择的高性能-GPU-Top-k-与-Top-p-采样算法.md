---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-11-05
hide:
  - navigation
tags:
  - Qrita
  - Top-k
  - Top-p
  - Triton
  - vLLM
  - GPU采样
  - 大语言模型
title: "Qrita：基于主元截断与选择的高性能 GPU Top-k 与 Top-p 采样算法"
---

# Qrita：基于主元截断与选择的高性能 GPU Top-k 与 Top-p 采样算法

> **arXiv:2602.01518** [cs.AI]  
> **Subjects:** Artificial Intelligence (cs.AI)  
> **Authors:** Jongseok Park, Sunga Kim, Alvin Cheung, Ion Stoica  
> **Submitted:** 2 Feb 2026; Last revised: 2 Nov 2026  
> **DOI / Paper:** [10.48550/arXiv.2602.01518](https://doi.org/10.48550/arXiv.2602.01518)  
> **Project / Code:** [vLLM Top-k/Top-p Triton Kernel](https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/ops/topk_topp_triton.py)

### 文章背景与核心概要
在大语言模型 (Large Language Model, LLM) 的推理部署流水线中，生成每一个新 Token 的最后关键一步，就是对词表概率分布进行 Top-k 与 Top-p (核采样 / Nucleus Sampling)。随着现代开源大模型词表规模从传统的 3.2 万暴增至 12.8 万甚至更多，传统的全排序算法在 GPU 上带来了沉重的计算开销与显存带宽瓶颈。由加州大学伯克利分校等知名机构学者联合推出的 Qrita 算法，独辟蹊径地采用了基于主元截断与快速选择的创新机制：通过高斯 $\sigma$ 动态截断大幅裁减搜索空间，并利用支持重复值判别的四元主元搜索将迭代次数减半。相较于 SGLang 与 FlashInfer 等顶尖推理引擎，Qrita 实现了高达 1.4 倍的端到端吞吐量提升，显存占用降低 50%，且输出与严格排序完全一致。目前该算法已作为默认算子正式合入 vLLM。

---

## 核心概要

> ## Summary

随着现代语言模型规模的持续膨胀，其词表体积急剧扩张，使得在 GPU 上高效实现 **Top-k** 与 **Top-p** 采样算法成为推理系统面临的一大关键挑战。传统的基于排序的方案在 GPU 上会引入高昂的计算负担与显存开销，而随机近似算法又往往以牺牲输出准确率与稳定性为代价。

> As modern language models scale, their vocabulary sizes grow significantly, making efficient implementation of **Top-k** and **Top-p** sampling algorithms a major challenge on GPUs. Traditional sorting-based approaches introduce heavy computation and memory overhead, while stochastic alternatives compromise output accuracy.

本文提出了 **Qrita**，一种基于主元截断与选择的高性能 GPU Top-k 和 Top-p 采样算法。通过融合**基于高斯分布的 $\sigma$ 截断**（极大压缩了词表的候选搜索空间）与**带重复值处理的四元主元搜索**（将主元迭代次数减半并确保确定性输出），Qrita 相比于 SGLang 和 FlashInfer 等业界领先的大语言模型推理引擎，实现了高达 **1.4 倍的端到端推理服务吞吐量提升**，同时**显存占用直接减半**。Qrita 完全使用 Triton 语言编写，目前已作为 vLLM 官方默认的 Top-k 和 Top-p 采样算子投入生产使用。

> This paper introduces **Qrita**, a high-performance GPU algorithm for Top-k and Top-p sampling utilizing pivot-based truncation and selection. By integrating **Gaussian-based $\sigma$-truncation** (which drastically reduces the vocabulary search space) and **quaternary pivot search with duplication handling** (which halves iterations and ensures deterministic outputs), Qrita achieves up to **1.4$\times$ higher end-to-end serving throughput** with **half the memory usage** compared to leading LLM engines like SGLang and FlashInfer. Qrita is implemented using Triton and serves as the default Top-k and Top-p sampler in vLLM.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 编号：** [arXiv:2602.01518](https://arxiv.org/abs/2602.01518) [cs.AI]
* **作者团队：** Jongseok Park, Sunga Kim, Alvin Cheung, Ion Stoica
* **提交日期：** 2026 年 2 月 2 日（最新修订：2026 年 11 月 2 日）
* **开源协议：** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />

> * **arXiv ID:** [arXiv:2602.01518](https://arxiv.org/abs/2602.01518) [cs.AI]
> * **Authors:** Jongseok Park, Sunga Kim, Alvin Cheung, Ion Stoica
> * **Submitted:** February 2, 2026 (Last revised: November 2, 2026)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />

---

## 论文摘要

> ## Abstract

尽管 Top-k 和 Top-p 算法在模型采样中扮演着至关重要的角色，但随着每次新模型发布时词表规模的不断攀升，高效实现这两种采样算法在 GPU 上构成了巨大的工程挑战。现有的方案要么依赖于全局排序，从而在 GPU 上造成极其严重的计算与显存带宽开销；要么依赖于随机近似方法，导致算法输出发生改变。在本项工作中，我们提出了 Qrita——一种基于主元截断与选择的高效 Top-k 和 Top-p 采样算法。Qrita 在 Top-k 与 Top-p 两个任务中均深度利用主元搜索，并引入了两大关键技术：
1. **基于高斯的 $\sigma$ 截断**：大幅削减词表的搜索空间；
2. **带重复值处理的四元主元搜索**：将主元搜索迭代次数减半，并保证完全确定性的输出结果。

> Despite their importance in model sampling, efficient implementation of Top-k and Top-p algorithms poses a significant challenge as model vocabularies grow with every new model release. Existing approaches often rely on sorting, which incurs significant computation and memory overhead on GPUs, or on stochastic approaches that alter the algorithm's output. In this work, we propose Qrita, an efficient Top-k and Top-p algorithm based on a pivot-based truncation and selection. Qrita leverages pivot-based search for both Top-k and Top-p with two key techniques: 
> 1. Gaussian-based $\sigma$-truncation, which greatly reduces the search space of the vocabulary, and 
> 2. Quaternary pivot search with duplication handling, which halves the number of pivot search iterations and guarantees deterministic output.

我们使用 Triton 语言实现了 Qrita，并在与 SGLang、FlashInfer 等高性能大语言模型执行引擎的 Top-k 和 Top-p 算子对比中评估了其性能。结果表明，Qrita 在端到端推理服务吞吐量上提升高达 1.4 倍，显存占用降低一半，同时能提供与基于稳定排序的 Top-k 和 Top-p 算法完全相同的输出结果。Qrita 目前已成为 vLLM 默认采用的 Triton 版 Top-k 和 Top-p 采样算子，其开源实现可在[官方仓库链接](https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/ops/topk_topp_triton.py)直接获取。

> We implement Qrita using Triton and evaluate its performance against the Top-k and Top-p kernels of high-performance LLM execution engines such as SGLang and FlashInfer, improving end-to-end serving throughput up to 1.4$\times$ with half the memory usage, while providing the same output of stable sort-based Top-k and Top-p algorithms. Qrita is now the default Triton Top-k and Top-p sampler of vLLM, and its implementation is available at [this link](https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/ops/topk_topp_triton.py).

---

## 核心特性与技术要点

> ## Key Features & Techniques

* **基于高斯的 $\sigma$ 截断 (Gaussian-based $\sigma$-Truncation)**：通过自适应缩小候选搜索空间，最大程度消除不必要的词表遍历开销。
* **带重复值处理的四元主元搜索 (Quaternary Pivot Search with Duplication Handling)**：将所需的主元搜索迭代次数直接减半，同时确保输出与标准基线排序完全一致且确定。
* **原生 Triton 实现 (Triton Implementation)**：具备高度优化的原生 GPU 执行效率，并已无缝集成至 vLLM 等工业级主流大模型推理引擎中。

> * **Gaussian-based $\sigma$-Truncation:** Minimizes unnecessary vocabulary exploration by dynamically narrowing down the candidate search space.
> * **Quaternary Pivot Search with Duplication Handling:** Cuts the required pivot search iterations in half while ensuring fully deterministic, stable outputs matching sort-based baselines.
> * **Triton Implementation:** Native high-performance GPU execution integrated directly into production engines like vLLM.
