---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- Transformer
- 位置编码
- 句法分析
- 自然语言处理
- 深度学习
title: 超越序列顺序：Transformer 的句法感知位置编码
---
### 文章背景与核心概要
传统的 Transformer 位置编码主要用于对序列顺序和词元间距进行编码，但在很大程度上忽视了底层的句法结构。本文引入了**句法感知位置编码（Syntax-informed Positional Embeddings, SiPE）**，这是一种在预训练期间从依存句法分析树中派生出来的轻量级句法先验。

SiPE 可以无缝集成到所有主流的位置编码家族中（包括绝对位置编码、相对位置编码和旋转位置编码），适用于编码器和解码器架构，且无需修改自注意力机制或核心模型架构。其实施策略根据模型架构的不同而有所调整：对于自回归解码器（相对位置编码），与注意力得分中的相对位置项进行乘法结合效果最佳；对于编码器，直接加到输入嵌入上并与原生位置机制相组合效果最好。

引入 SiPE 进行预训练可带来显著的性能提升，在 **SyntaxGym** 基准测试上的得分提升高达 **10.3%**，同时将困惑度（Perplexity）降低了 **9.0%**（这一指标通常会被现有的句法注入方法恶化）。此外，这些句法层面的改进能够迁移到真实的语言理解任务中，使 **GLUE** 基准测试分数提升高达 **8.2%**。与以往需要在推理时对多个解析树进行边缘化计算的句法语言模型不同，SiPE 仅需依赖单一的解析树，从而在句法监督和运行时推理成本之间建立了全新的帕累托前沿（Pareto frontier）。

---

# Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers

> **arXiv:** [2608.06111](https://arxiv.org/abs/2608.06111) [cs.CL]  
> **Submitted on:** August 6, 2026  
> **Authors:** Haris Riaz, Hyungji Kim, Mihai Surdeanu  

---

## 📌 Summary

> Traditional positional embeddings in Transformers encode sequence order and token distance, but they remain largely agnostic to syntactic structure. This paper introduces **Syntax-informed Positional Embeddings (SiPE)**, a lightweight syntactic prior derived from dependency parses during pretraining. 
>
> SiPE integrates seamlessly across all major positional embedding families (absolute, relative, and rotary) for both encoders and decoders, without altering self-attention or the core architecture. The placement strategy is architecture-dependent:
> * **Autoregressive Decoders (Relative PE):** Performs best when coupled multiplicatively with the relative-position term in attention scores.
> * **Encoders:** Performs best when added directly to input embeddings, composing with native positional mechanisms.
>
> Pretraining with SiPE yields substantial performance gains, improving scores on the **SyntaxGym** benchmark by up to **10.3%** while simultaneously reducing perplexity by **9.0%** (a metric frequently degraded by existing syntax-injection methods). Furthermore, these syntactic improvements transfer to real-world language understanding, raising **GLUE** benchmark scores by up to **8.2%**. Unlike prior syntactic language models that require marginalizing over multiple parses at inference time, SiPE conditions on a single parse, establishing a new Pareto frontier for syntactic supervision and runtime inference cost.

---

## 📑 Paper Metadata & Links

> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **Comments:** 21 pages, 9 figures
> * **Full-Text Links:**
>   * [View PDF](https://arxiv.org/pdf/2608.06111)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.06111v1)
>   * [TeX Source](https://arxiv.org/src/2608.06111)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)