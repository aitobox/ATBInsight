---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- KV缓存
- 模型推理
- 大语言模型
- 内存优化
- 检索与生成
title: KV-Rescue：通过逐步交织恢复推理语言模型的KV缓存淘汰损失
---
### 文章背景与核心概要
在大语言模型处理长推理轨迹时，键值（KV）缓存淘汰（KV cache eviction）是控制内存开销的常用技术。然而，这种方法本质上是有损的，会导致模型在部分历史视图下解码。在激进的内存预算下，这不仅会降低准确率，还会引发“失控退化”（runaway degeneration），即模型输出重复或不连贯的词元，直至达到长度极限。

本文作者将这种性能损失定义为“信息差”（缺少上下文），而非“能力差”（模型容量限制）。为此，他们推出了 **KV-Rescue**，这是一个无需训练的推理框架，它将经过淘汰的基础模型与一个轻量级的全上下文辅助模型配对。通过交织推理步骤并利用基于在线熵和可压缩性的检测器及早终止退化候选，KV-Rescue 有效恢复了丢失的推理性能。

---

# KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving

**Authors:** Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun, Sungjoo Yoo  
**Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
**arXiv ID:** [arXiv:2608.15797](https://arxiv.org/abs/2608.15797)  
**Submitted:** August 16, 2026  

---

## 📌 Summary

键值（KV）缓存淘汰是限制大语言模型中长推理轨迹内存成本的常用技术。然而，它本质上有损，迫使模型从局部的历史视图进行解码。在激进的预算下，这不仅会导致准确率下降，还会引发**失控退化**（即模型输出重复或不连贯的词元，直到达到长度极限）。

作者将这种损失描述为*信息差距*（缺少上下文）而不是*能力差距*（模型容量限制）。为了解决这个问题，他们引入了 **KV-Rescue**，这是一个无需训练的推理框架，它将一个被淘汰的基础模型与一个轻量级的全上下文辅助模型配对。通过交织推理步骤并利用基于在线熵和可压缩性的检测器来尽早终止退化的候选者，KV-Rescue 有效地恢复了丢失的推理性能。

> Key-Value (KV) cache eviction is a common technique to cap the memory cost of long reasoning traces in large language models. However, it is inherently lossy, forcing models to decode from a partial historical view. Under aggressive budgets, this causes not only accuracy degradation but also **runaway degeneration** (where models output repetitive or incoherent tokens until hitting length limits). 
> 
> The authors characterize this loss as an *information gap* (missing context) rather than a *capability gap* (model capacity limits). To address this, they introduce **KV-Rescue**, a training-free inference framework that pairs an evicted base model with a lightweight full-context helper. By interleaving reasoning steps and utilizing an online entropy- and compressibility-based detector to halt degenerated candidates early, KV-Rescue effectively recovers lost reasoning performance.

---

## 🔍 Abstract

KV 缓存淘汰限制了长推理轨迹的内存成本，但它本质上是有损的，因为模型是从其历史的局部视图进行解码的。在激进的预算下，这不仅会降低准确率，还会导致失控退化，即模型产生不连贯或重复的词元，直到达到长度限制。

我们将这种损失的大部分归结为由缺少上下文引起的信息差距，而不是由有限模型容量引起的能力差距。被淘汰的 7B 模型和全上下文的 1.5B 模型会产生互补的错误，在其答案之间进行预言机（oracle）选择可以恢复与全 KV 7B 模型之间 79% 的准确率差距。

基于这一观察，我们提出了 **KV-Rescue**，这是一个无需训练的推理框架，它利用轻量级全上下文辅助模型来弥合 KV 淘汰引入的信息差距。KV-Rescue 将两个模型的推理步骤交织到一个共享的轨迹中。在线检测器使用熵和可压缩性来动态终止不连贯或重复的基础模型候选者的生成。

在五个数学基准测试中，使用 `Qwen2.5-Math 7B` 和 `72B`，KV-Rescue 在淘汰预算 $B=64$ 的情况下恢复了平均 **87%** 因淘汰而损失的准确率。解码成本分析进一步表明，防止失控退化平均将基础模型的词元生成量减少了 **43%**。

> KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tokens until reaching the length limit. 
> 
> We characterize much of this loss as an information gap caused by missing context, rather than a capability gap caused by limited model capacity. An evicted 7B model and a full-context 1.5B model make complementary errors, and an oracle choice between their answers recovers 79% of the accuracy gap to the full-KV 7B model. 
> 
> Based on this observation, we propose **KV-Rescue**, a training-free inference framework that bridges the information gap introduced by KV eviction using a lightweight full-context helper. KV-Rescue interleaves reasoning steps from the two models into a shared trajectory. An online detector uses entropy and compressibility to terminate the generation of incoherent or repetitive base-model candidates early. 
> 
> Across five math benchmarks with `Qwen2.5-Math 7B` and `72B`, KV-Rescue recovers an average of **87%** of the accuracy lost to eviction at an eviction budget of $B=64$. A decode-cost analysis further shows that preventing runaway degeneration cuts base-model token generation by **43%** on average.

---

## 🛠️ Key Contributions & Highlights

* **信息差距的识别：** 证明了 KV 淘汰损失主要由上下文丢失驱动，而非模型容量限制。
* **互补错误恢复：** 表明将淘汰的大型模型（例如 7B）与全上下文辅助模型（例如 1.5B）结合，可以实现显著的准确率恢复。
* **KV-Rescue 框架：** 一种无需训练的推理方法，可在不同模型之间逐步交织推理轨迹。
* **在线退化检测器：** 利用词元熵和可压缩性动态捕捉并终止失控的重复或不连贯现象。
* **显著的性能与效率提升：** 在五个数学基准测试中恢复了 87% 丢失的准确率，同时将基础模型的词元生成开销减少了 43%。

> * **Identification of the Information Gap:** Demonstrates that KV eviction loss is primarily driven by missing context rather than model capacity constraints.
> * **Complementary Error Recovery:** Shows that combining an evicted large model (e.g., 7B) with a full-context helper model (e.g., 1.5B) captures significant accuracy recovery.
> * **KV-Rescue Framework:** A training-free inference approach that stepwise-interleaves reasoning traces between models.
> * **Online Degeneration Detector:** Leverages token entropy and compressibility to dynamically catch and terminate runaway repetitions or incoherence.
> * **Substantial Performance & Efficiency Gains:** Recovers 87% of lost accuracy across five math benchmarks while simultaneously cutting base-model generation token overhead by 43%.

---

## 🔗 Links & Resources

* **查看 PDF：** [arXiv:2608.15797 PDF](https://arxiv.org/pdf/2608.15797)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.15797v1)
* **DOI：** [10.48550/arXiv.2608.15797](https://doi.org/10.48550/arXiv.2608.15797)

> * **View PDF:** [arXiv:2608.15797 PDF](https://arxiv.org/pdf/2608.15797)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.15797v1)
> * **DOI:** [10.48550/arXiv.2608.15797](https://doi.org/10.48550/arXiv.2608.15797)