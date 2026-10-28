---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-29
hide:
  - navigation
tags:
  - 大语言模型
  - 模型量化
  - 条件记忆
  - DeepSeek
  - vLLM
title: "让门控做决定：面向大模型量化条件记忆的按需查表精度优化"
---

# 让门控做决定：面向大模型量化条件记忆的按需查表精度优化

> **arXiv:2610.35985** [cs.LG]  
> **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`)  
> **Authors:** Tianqi Chen, Xunchao Li, Linchuan Xie, Guanghua Yu, Jianchen Zhu, Peisong Wang, Jian Cheng  
> **Submitted:** 26 October 2026  
> **Paper:** [arXiv:2610.35985](https://arxiv.org/abs/2610.35985)

### 文章背景与核心概要

在大语言模型中引入条件记忆层 (例如 DeepSeek 提出的 Engram 哈希 n-gram 表) 能够显著拓宽模型的知识边界，但庞大的显存开销给端到端推理部署带来了严峻挑战。若直接使用传统的低比特量化技术，冷门长尾实体往往会优先遭遇灾难性的精度损失，而按照访问频次分配精度的直觉做法反而适得其反。本文作者深入探究发现了关键症结：查表向量的量化误差完全由其对应的“门控机制”所决定，高频词门控值极小，而罕见长尾知识的门控值极大。据此提出的 GateRQ 方案将表项分解为 1 比特残差阶梯，仅常驻基础层计算门控，再由门控决定是否按需读取更深层精度。在完全免重训的情况下，该技术将 GPU 显存占用削减了 7.8 倍，使 vLLM 吞吐量提升 11%–31%，且几乎无损模型性能。

---

## 📌 内容总结

> ## 📌 Summary

条件记忆层 (例如 DeepSeek 推出的 Engram 机制) 通过将庞大的哈希 n-gram 查找表挂载到大语言模型 (Large Language Model, LLM) 中，显著增强了模型的知识储备与推理能力——如果从 *DeepSeek-V4.1-Flash* 中移除该结构，模型的 PopQA 基准测试得分将剧烈下跌 **36.8 分**。然而，当采用低比特量化 (Quantization) 进行显存压缩时，长尾知识往往最先受损。更令人意外的是，行业惯用的常规优化手段——给访问频次更高的数据行分配更多比特——反而适得其反，其实际表现甚至比纯粹的随机分配还要糟糕。

> Conditional memory layers (such as DeepSeek’s Engram) integrate large hashed n-gram tables into Large Language Models (LLMs), significantly enhancing model capabilities—removing them from *DeepSeek-V4.1-Flash* incurs a heavy cost of **36.8 PopQA points**. However, low-bit quantization tends to degrade long-tail facts first. Conventional approaches that allocate more bits to frequently accessed rows actually backfire, performing worse than random distribution.

本项研究精准揪出了这一现象背后的本质根源：负责缩放每个检索向量的**门控机制 (Gate Mechanism)**。一次查表操作带来的量化误差，直接被其对应的门控值加权放大 (对于常见的高频 n-gram，门控值往往极小；而对于罕见的长尾实体，门控值却往往很大)。为此，作者团队提出了全新的 **GateRQ** 方法，将每一行向量存储为阶梯状的 1 比特残差编码。该方法仅在 GPU 显存中常驻第 1 级编码用于计算门控权重，并且只针对门控值评分最高的查表项，才按需深入读取更深层级的残差编码以提升精度。

> This paper identifies the root cause: the **gate** that scales each retrieved row. A lookup's quantization error is weighted directly by its gate value (which is small for frequent n-grams and large for rare long-tail entities). The authors introduce **GateRQ**, a novel method that stores each row as a ladder of 1-bit residual codes. It keeps level 1 in GPU memory to compute the gate, selectively reading deeper levels only for lookups ranked highest by the gate.

**核心成果：** 在完全无需重新训练的情况下，GateRQ 在 *DeepSeek-V4.1-Flash* 上实现了 **7.8 倍的 GPU 查表显存压缩**，相比 FP8 格式的表格将 `vLLM` 吞吐量提升了 **11%–31%**。在大幅降本提速的同时，模型性能依然坚挺：在两款评估模型上，单次查表平均仅需读取 1.50 比特即可将 PopQA 分数损失控制在 **1.0 分** 左右；当读取 2.10 比特时，性能损失更是微乎其微，仅有 **0.2 分**。

> **Key Results:** Without requiring retraining, GateRQ **reduces GPU table memory by 7.8×** on *DeepSeek-V4.1-Flash*, boosting `vLLM` throughput by **11%–31%** over FP8 tables. It achieves this while maintaining high performance, losing only about **1.0 PopQA point** at 1.50 bits read per lookup and **0.2 points** at 2.10 bits across two evaluated models.

---

## 📄 论文摘要

> ## 📄 Abstract

条件记忆层 (例如 DeepSeek 推出的 Engram) 将庞大的哈希 n-gram 查表机制挂载到语言模型上，如果将其从 DeepSeek-V4.1-Flash 中剥离，会导致 PopQA 测试下降 36.8 分。采用低比特量化时，长尾知识往往最先丢失，而行业常规的补救方案——为高频访问的数据行赋予更高比特——却适得其反：按访问频率优化查表精度，其表现甚至不如随机选择。我们将该现象归因于负责缩放每个检索向量的门控机制。查表带来的量化误差受门控值加权：对于高频 n-gram，门控值较小；而对于长尾实体的冷门 n-gram，门控值极大，且该门控值仅凭 1 比特编码即可计算得出。因此，GateRQ 将每一行向量存储为 1 比特残差编码阶梯，只在 GPU 显存中保留第 1 级编码以计算门控，并仅对门控评分最高的查表项读取更深层级的编码。在无需重新训练的前提下，GateRQ 将 DeepSeek-V4.1-Flash 的 GPU 表格显存占用水准削减了 7.8 倍，相比 FP8 查找表使 vLLM 吞吐量提升 11%–31%；同时在两个模型上的评估显示，单次查表平均读取 1.50 比特时仅损失约 1 个 PopQA 分数点，读取 2.10 比特时损失仅约 0.2 个点。

> Conditional memory layers, such as DeepSeek's Engram, attach large hashed n-gram tables to a language model, and removing them from DeepSeek-V4.1-Flash costs 36.8 PopQA points. Low-bit quantization loses long-tail facts first, and the standard remedy, giving more bits to frequently accessed rows, backfires: refining lookups by access frequency is worse than refining them at random. We trace this to the gate that scales each retrieved row. A lookup's quantization error is weighted by its gate, which is small for frequent n-grams, large for the rare n-grams of long-tail entities, and computable from a 1-bit code. GateRQ therefore stores each row as a ladder of 1-bit residual codes, keeps level 1 in GPU memory to compute the gate, and reads deeper levels only for the lookups the gate ranks highest. Without retraining, GateRQ cuts GPU table memory by 7.8x on DeepSeek-V4.1-Flash, which raises vLLM throughput by 11%-31% over FP8 tables, while losing about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits across two models.

---

## 🔗 相关链接与资源

> ## 🔗 Links & Resources

* **全文阅读选项：** 
  * [查看 PDF](https://arxiv.org/pdf/2610.35985)
  * [HTML 网页版 (实验性)](https://arxiv.org/html/2610.35985v1)
  * [TeX 源码](https://arxiv.org/src/2610.35985)
* **授权协议：** [知识共享署名 4.0 国际许可 (Creative Commons Attribution 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **引用与学术检索工具：** 
  * [Google Scholar 学术搜索](https://scholar.google.com/scholar_lookup?arxiv_id=2610.35985)
  * [Semantic Scholar 文献分析](https://api.semanticscholar.org/arXiv:2610.35985)
  * [SciX 平台](https://scixplorer.org/abs/arXiv:2610.35985)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2610.35985)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2610.35985v1)
>   * [TeX Source](https://arxiv.org/src/2610.35985)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> * **Citations & Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.35985)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.35985)
>   * [SciX](https://scixplorer.org/abs/arXiv:2610.35985)
