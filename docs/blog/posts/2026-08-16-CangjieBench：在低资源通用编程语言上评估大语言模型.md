---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 大语言模型
- 代码生成
- 仓颉编程语言
- 基准测试
- 低资源语言
title: CangjieBench：在低资源通用编程语言上评估大语言模型
---
### 文章背景与核心概要
尽管大语言模型（LLM）在处理高资源编程语言时表现卓越，但它们在面对低资源编程语言时往往表现不佳。现有的低资源编程语言研究主要集中在领域特定语言（DSLs），而那些面临严重数据稀缺的通用编程语言则鲜有涉足。为了填补这一空白，本文作者推出了 **CangjieBench**，这是一个专为“仓颉”（Cangjie，一种具有代表性的低资源通用编程语言）量身定制的无污染基准测试集。该基准包含 248 个从 *HumanEval* 和 *ClassEval* 手工翻译的高质量样本，涵盖了文本到代码（Text-to-Code）和代码到代码（Code-to-Code）任务。

通过在四种不同设置（直接生成、语法约束生成、RAG 以及智能体）下进行的系统性评估，该研究揭示了关于模型性能、语法约束效率以及代码翻译过程中负面迁移局限性的关键见解。这项工作不仅为评估 LLM 在未见过的低资源编程语言上的泛化能力提供了重要的测试平台，也为未来低资源语言的代码生成技术指明了优化方向。

---

# CangjieBench: Benchmarking LLMs on a Low-Resource General-Purpose Programming Language

**arXiv ID:** [arXiv:2603.14501](https://arxiv.org/abs/2603.14501) [cs.SE]  
**Authors:** Junhang Cheng, Fang Liu, Jia Li, Chengru Wu, Nanxiang Jiang, Li Zhang  
**Accepted by:** ESEM 2026  
**Last Revised:** August 12, 2026 (v2)  

> **arXiv ID:** [arXiv:2603.14501](https://arxiv.org/abs/2603.14501) [cs.SE]  
> **Authors:** Junhang Cheng, Fang Liu, Jia Li, Chengru Wu, Nanxiang Jiang, Li Zhang  
> **Accepted by:** ESEM 2026  
> **Last Revised:** August 12, 2026 (v2)

---

## Executive Summary

While Large Language Models (LLMs) excel at high-resource programming languages, they frequently struggle with low-resource alternatives. Existing research on low-resource coding largely targets Domain-Specific Languages (DSLs), leaving general-purpose languages suffering from severe data scarcity largely underexplored. 

To bridge this gap, the authors introduce **CangjieBench**, a contamination-free benchmark tailored for **Cangjie**—a representative low-resource, general-purpose programming language. The benchmark comprises 248 high-quality samples manually translated from *HumanEval* and *ClassEval*, covering both Text-to-Code and Code-to-Code tasks. 

Through a systematic evaluation across four distinct settings (Direct Generation, Syntax-Constrained Generation, RAG, and Agents), the study reveals crucial insights into model performance, the efficiency of syntax constraints, and the limitations of negative transfer during code translation.

> ## 执行摘要
> 
> 尽管大语言模型（LLM）在处理高资源编程语言时表现优异，但在面对低资源替代语言时往往力不从心。现有的低资源代码研究主要针对领域特定语言（DSLs），这使得遭受严重数据稀缺的通用编程语言在很大程度上未得到充分探索。
> 
> 为了弥补这一空白，作者推出了 **CangjieBench**，这是一个专为“仓颉”（**Cangjie**，一种具有代表性的低资源通用编程语言）量身定制的无污染基准测试集。该基准包含 248 个从 *HumanEval* 和 *ClassEval* 手工翻译的高质量样本，涵盖了文本到代码（Text-to-Code）和代码到代码（Code-to-Code）任务。
> 
> 通过在四种不同设置（直接生成、语法约束生成、RAG 和智能体）下进行的系统性评估，该研究揭示了关于模型性能、语法约束效率以及代码翻译中负面迁移局限性的关键见解。

---

## Key Highlights & Findings

- **Benchmark Composition:** 248 manually translated samples from *HumanEval* and *ClassEval* specifically designed for Cangjie.
- **Evaluation Settings Tested:**
  1. **Direct Generation:** Performs poorly due to a lack of training data.
  2. **Syntax-Constrained Generation:** Provides the optimal balance between accuracy and computational cost.
  3. **Retrieval-Augmented Generation (RAG):** Enhances context alignment for low-resource syntax.
  4. **Agent-based Approaches:** Achieve state-of-the-art accuracy, but suffer from exceptionally high token consumption.
- **Negative Transfer Phenomenon:** Code-to-code translation underperformed compared to text-to-code generation, indicating that models tend to overfit to the source language patterns rather than properly adapting.

> ## 核心亮点与发现
> 
> - **基准组成：** 包含 248 个从 *HumanEval* 和 *ClassEval* 手工翻译的样本，专为仓颉语言设计。
> - **测试的评估设置：**
>   1. **直接生成（Direct Generation）：** 由于缺乏训练数据，表现较差。
>   2. **语法约束生成（Syntax-Constrained Generation）：** 在准确率和计算成本之间提供了最佳平衡。
>   3. **检索增强生成（RAG）：** 增强了低资源语法上下文的对齐。
>   4. **基于智能体的方法（Agent-based Approaches）：** 达到了最先进（SOTA）的准确率，但消耗了极高的 Token 量。
> - **负面迁移现象：** 代码到代码的翻译表现不如文本到代码的生成，这表明模型倾向于过度拟合源语言模式，而未能进行适当的适应。

---

## Abstract

> Large Language Models excel in high-resource programming languages but struggle with low-resource ones. Existing research related to low-resource programming languages primarily focuses on Domain-Specific Languages (DSLs), leaving general-purpose languages that suffer from data scarcity underexplored. To address this gap, we introduce CangjieBench, a contamination-free benchmark for Cangjie, a representative low-resource general-purpose language. The benchmark comprises 248 high-quality samples manually translated from HumanEval and ClassEval, covering both Text-to-Code and Code-to-Code tasks. We conduct a systematic evaluation of diverse LLMs under four settings: Direct Generation, Syntax-Constrained Generation, Retrieval-Augmented Generation (RAG), and Agent. Experiments reveal that Direct Generation performs poorly, whereas Syntax-Constrained Generation offers the best trade-off between accuracy and computational cost. Agent achieve state-of-the-art accuracy but incur high token consumption. Furthermore, we observe that Code-to-Code translation often underperforms Text-to-Code generation, suggesting a negative transfer phenomenon where models overfit to the source language patterns. We hope that our work will offer valuable insights into LLM generalization to unseen and low-resource programming languages.

> ## 摘要
> 
> 大语言模型在处理高资源编程语言时表现卓越，但在处理低资源编程语言时却举步维艰。现有关于低资源编程语言的研究主要集中在领域特定语言（DSLs）上，使得面临数据稀缺的通用编程语言未得到充分探索。为了解决这一空白，我们推出了 CangjieBench，这是针对仓颉（一种具有代表性的低资源通用语言）的无污染基准测试。该基准包含 248 个从 HumanEval 和 ClassEval 手工翻译的高质量样本，涵盖文本到代码和代码到代码任务。我们在四种设置下对各种 LLM 进行了系统评估：直接生成、语法约束生成、检索增强生成（RAG）和智能体（Agent）。实验表明，直接生成表现不佳，而语法约束生成在准确率和计算成本之间提供了最佳权衡。智能体实现了最先进的准确率，但带来了高昂的 Token 消耗。此外，我们观察到代码到代码的翻译通常表现不如文本到代码的生成，这表明存在负面迁移现象，即模型过度拟合了源语言模式。我们希望这项工作能为 LLM 在未见过的低资源编程语言上的泛化能力提供宝贵的见解。

---

## Resources & Links

* **arXiv Abstract:** [https://arxiv.org/abs/2603.14501](https://arxiv.org/abs/2603.14501)
* **Direct PDF:** [View PDF](https://arxiv.org/pdf/2603.14501)
* **Code & Data Repository:** [GitHub - cjhCoder7/CangjieBench](https://github.com/cjhCoder7/CangjieBench)

> ## 资源与链接
> 
> * **arXiv 摘要：** [https://arxiv.org/abs/2603.14501](https://arxiv.org/abs/2603.14501)
> * **PDF 原文：** [查看 PDF](https://arxiv.org/pdf/2603.14501)
> * **代码与数据仓库：** [GitHub - cjhCoder7/CangjieBench](https://github.com/cjhCoder7/CangjieBench)