---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- LLM
- 递归推理
- 隐式 Transformer
- Chain-of-Thought
- 逻辑推理
title: 深思熟虑，一语中的：ReLIT，一种递归潜在隐式 Transformer 框架
---
### 文章背景与核心概要
大语言模型（LLM）的思维链（Chain-of-Thought, CoT）提示词技术虽然能够激发强大的推理能力，但由于强迫模型输出离散的中间推理步骤词元（tokens），带来了巨大的计算开销。近期的潜空间推理方法试图将这一过程内部化为连续的隐藏状态，然而像微型递归模型（TRM）这样的现有模型虽然擅长符号任务，却难以保持自然语言的连贯性。

为了解决这一局限，作者团队引入了 **ReLIT（Recursive Latent Implicit Transformer，递归潜在隐式 Transformer）**。该框架将冻结的基础 LLM 主干（**TinyLlama-1.1B**）与一个轻量级、可训练的递归模块相结合，使 ReLIT 在生成最终输出之前，能够迭代式地优化其潜在思维（$z$）。这种方法成功地将语言直觉与算法处理解耦，通过梯度隔离的循环回路实现了高效的“深度思考”，且无需承担显式词元生成的延迟。

---

# Think Deep, Speak Once: ReLIT, A Recursive Latent Implicit Transformer Framework

**Authors:** Abhishek Panwar, Maheep Singh, Saksham Bansal  
**Submitted:** August 8, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [2608.08113](https://arxiv.org/abs/2608.08113)

---

## 📋 Executive Summary

> Chain-of-Thought (CoT) prompting enables powerful reasoning in Large Language Models (LLMs) but introduces substantial computational overhead by forcing models to output discrete tokens for intermediate steps. Recent latent reasoning methods internalize this process into continuous hidden states, yet current models like Tiny Recursive Models (TRMs) excel at symbolic tasks while failing to maintain natural language coherence. 

> To resolve this limitation, the authors introduce **ReLIT (Recursive Latent Implicit Transformer)**. By coupling a frozen foundational LLM backbone (**TinyLlama-1.1B**) with a lightweight, trainable recursive block, ReLIT iteratively refines its latent thinking ($z$) prior to final output generation. This approach successfully separates linguistic intuition from algorithmic processing, allowing for high-efficiency "deep thinking" via gradient-isolated recurrent loops without explicit token latency.

---

## 📝 Abstract

思维链（CoT）提示词已成为激发大语言模型（LLM）推理能力的主流范式，但它迫使模型将中间推理步骤外化为离散的词元，从而产生了巨大的计算开销。近期的潜空间推理方法试图将这一过程内部化到连续的隐藏状态中。作为潜空间推理领域的最新进展之一，微型递归模型（TRMs）擅长符号推理，但在自然语言环境中却难以保持语义连贯性。为了弥合这一鸿沟，我们推出了 ReLIT（递归潜在隐式 Transformer），这是一种将深度递归推理扎根于基础模型丰富语义表示中的混合框架。ReLIT 通过一个轻量级、可训练的递归模块增强了冻结的 LLM 主干（TinyLlama-1.1B），在确定最终输出之前迭代优化其潜在思维（$z$），从结构上将语言直觉与算法处理解耦，并通过梯度隔离的循环回路实现“深度思考”，同时免去了显式词元生成的延迟。从实证来看，ReLIT 在 GLoRE 逻辑推理基准测试中实现了极高的参数效率，在 ProofWriter 和 RuleTaker 等具有挑战性的任务上，以极少的监督达到了甚至超越了显著更大规模模型的水平。这些结果表明，推理能力不仅可以通过扩展参数宽度来提升，更可以通过递归计算深度进行高效规模化，从而为语义落地的隐式推理提供了一个有原则的框架。

> Chain-of-Thought (CoT) prompting has become the dominant paradigm for eliciting reasoning in Large Language Models (LLMs), yet it creates substantial computational overhead by forcing models to externalize intermediate reasoning steps as discrete tokens. Recent latent reasoning approaches attempt to internalize this process within continuous hidden states. One of the latest advancements in the field of latent reasoning, Tiny Recursive Models (TRMs) excel at symbolic reasoning but struggle to preserve semantic coherence in natural language settings. To bridge this gap, we introduce ReLIT (Recursive Latent Implicit Transformer), a hybrid framework that grounds deep recursive reasoning within the rich semantic representations of a foundational model. ReLIT augments a frozen LLM backbone (TinyLlama-1.1B) with a lightweight, trainable recursive block that iteratively refines its latent thinking ($z$) before committing to a final output, structurally solving linguistic intuition from algorithmic processing and enabling "deep thinking" via gradient-isolated recurrent loops without the latency of explicit token generation. Empirically, ReLIT achieves high parameter efficiency on the GLoRE logical reasoning benchmark, matching or outperforming significantly larger models on challenging tasks such as ProofWriter and RuleTaker despite minimal supervision. These results demonstrate that reasoning capability can't just be scaled efficiently through recurrent depth rather than parameter width, offering a principled framework for semantically grounded implicit reasoning.

---

## 🔑 Key Innovations & Contributions

* **潜空间推理的语义基础：** 通过将深度递归结构与强大的基础语言模型主干相结合，解决了以往侧重符号的潜在模型（如 TRMs）在语言连贯性上的局限。
* **梯度隔离的循环回路：** 在幕后迭代更新和细化潜在思维（$z$），在不引入词元生成延迟的情况下实现“深度思考”能力。
* **极高的参数效率：** 在严苛的逻辑推理基准测试（**GLoRE**、**ProofWriter** 和 **RuleTaker**）中，以极少的监督超越或匹配了参数规模显著更大的模型。
* **深度优于宽度：** 证明了先进的推理能力可以通过递归计算深度的增加来有效扩展，而无需单纯扩大模型的原始宽度。

> * **Semantic Grounding for Latent Reasoning:** Solves the linguistic coherence limitations of prior symbolic-focused latent models (like TRMs) by combining deep recursive structures with a robust foundational language model backbone.
> * **Gradient-Isolated Recurrent Loops:** Iteratively updates and refines latent thoughts ($z$) behind the scenes, allowing "deep thinking" capabilities without incurring token generation latency.
> * **High Parameter Efficiency:** Outperforms or matches substantially larger parameter-scale models on rigorous logical reasoning benchmarks (**GLoRE**, **ProofWriter**, and **RuleTaker**) using minimal supervision.
> * **Depth over Width:** Demonstrates that advanced reasoning capabilities scale effectively via recurrent computational depth rather than expanding raw model width.

---

## 📊 Additional Metadata

* **论文长度：** 14 页，6 幅图表
* **永久 DOI：** [10.48550/arXiv.2608.08113](https://doi.org/10.48550/arXiv.2608.08113)
* **全文与访问链接：**
  * [查看 PDF](https://arxiv.org/pdf/2608.08113)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.08113v1)
  * [TeX 源码](https://arxiv.org/src/2608.08113)
  * ![license icon](./images/345c7ad61f1b.png) [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)

> * **Paper Length:** 14 pages, 6 figures
> * **Permanent DOI:** [10.48550/arXiv.2608.08113](https://doi.org/10.48550/arXiv.2608.08113)
> * **Full-Text & Access Links:**
>   * [View PDF](https://arxiv.org/pdf/2608.08113)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.08113v1)
>   * [TeX Source](https://arxiv.org/src/2608.08113)
>   * ![license icon](./images/345c7ad61f1b.png) [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

---

## 🔗 External Resources & Tools

* **代码与仓库：** [CatalyzeX Code Finder](https://www.catalyzex.com), [Hugging Face](https://huggingface.co/huggingface)
* **学术引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08113), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08113), [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.08113)
* **交互式演示与工具：** [alphaXiv](https://alphaxiv.org/), [Connected Papers](https://www.connectedpapers.com/), [Litmaps](https://www.litmaps.co/), [scite.ai](https://www.scite.ai/)

> * **Code & Repositories:** [CatalyzeX Code Finder](https://www.catalyzex.com), [Hugging Face](https://huggingface.co/huggingface)
> * **Scholarly Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08113), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08113), [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.08113)
> * **Interactive Demos & Tools:** [alphaXiv](https://alphaxiv.org/), [Connected Papers](https://www.connectedpapers.com/), [Litmaps](https://www.litmaps.co/), [scite.ai](https://www.scite.ai/)