---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- Qwen3-27B
- 代码翻译
- C2Rust
- 微调
- 静态分析
title: 微调 Qwen3-27B 实现 C 到 Rust 代码转换：包含预训练、调试感知 SFT 与特定任务 SFT 的三阶段课程
---
### 文章背景与核心概要

将陈旧的 C 语言代码库转换为安全、地道的 Rust 代码是消除内存安全漏洞、提升软件工程质量的关键目标。然而，开箱即用的通用大语言模型（LLM）在此类任务上往往表现不佳，因为常规的预训练缺乏对地道 Rust 代码生成、跨语言语义等价性以及编译器反馈集成的专项优化。

本文针对 **Qwen3-27B** 模型提出了一种**三阶段微调课程**：1. **以 Rust 为中心的预训练**（在 Rust 语料库上持续预训练以建立地道语法和标准库使用的先验）；2. **调试感知监督微调（SFT）**（使用 `microsoft/Verus_Training_Data` 数据集训练模型的调试与自我修复能力）；3. **特定任务 SFT**（在成对的 C/Rust LeetCode 解决方案上训练，以实现直接、准确的语义转换）。

研究团队使用 **SACTOR** 框架对最终的模型进行了评估。该框架是一个智能体式的、由静态分析引导的验证工具，具备两阶段转换流程（从非地道到地道）以及基于外部函数接口（FFI）的端到端（E2E）测试，结果表明微调后的模型性能显著优于基线模型。

---

## 摘要 (Abstract)

Translating C code into safe, idiomatic Rust is a longstanding software-engineering goal because it can eliminate entire classes of memory-safety vulnerabilities while preserving the functional behavior of legacy systems. Large language models (LLMs) have shown promise for this task but typically underperform when applied off-the-shelf, since general-purpose pretraining rarely emphasizes idiomatic Rust generation, cross-language semantic equivalence, or the ability to reason about and repair compiler/runtime feedback. 

将 C 代码转换为安全且地道的 Rust 一直是软件工程领域长期追求的目标，因为这不仅能保留遗留系统的功能行为，还能根除一整类内存安全漏洞。大语言模型（LLM）在这一任务中展现出了巨大潜力，但直接拿来即用时往往表现不佳，因为通用预训练很少强调地道的 Rust 生成、跨语言语义等价性，也缺乏对编译器/运行时反馈的推理和修复能力。

> Translating C code into safe, idiomatic Rust is a longstanding software-engineering goal because it can eliminate entire classes of memory-safety vulnerabilities while preserving the functional behavior of legacy systems. Large language models (LLMs) have shown promise for this task but typically underperform when applied off-the-shelf, since general-purpose pretraining rarely emphasizes idiomatic Rust generation, cross-language semantic equivalence, or the ability to reason about and repair compiler/runtime feedback. 

In this report we describe a three-stage fine-tuning curriculum applied to Qwen3-27B that is designed to progressively specialize the model for the C-to-Rust (C2Rust) translation task: 
1. **Continued pretraining** on Rust-centric corpora to strengthen the model's prior over idiomatic Rust syntax and standard-library usage; 
2. **Supervised fine-tuning (SFT)** on the `microsoft/Verus_Training_Data` dataset to instill debugging and self-repair behavior over Rust code; and 
3. **Task-specific SFT** on paired C/Rust solutions derived from LeetCode problems to teach direct semantic translation. 

在本报告中，我们描述了应用于 Qwen3-27B 的三阶段微调课程，旨在逐步让该模型专门适应 C 到 Rust (C2Rust) 的转换任务：
1. **持续预训练**：在以 Rust 为中心的语料库上进行预训练，以增强模型对地道 Rust 语法和标准库使用的先验知识；
2. **监督微调（SFT）**：在 `microsoft/Verus_Training_Data` 数据集上进行训练，以培养模型对 Rust 代码的调试和自我修复行为；
3. **特定任务 SFT**：在源自 LeetCode 问题的成对 C/Rust 解决方案上进行训练，以教授直接的语义转换。

> In this report we describe a three-stage fine-tuning curriculum applied to Qwen3-27B that is designed to progressively specialize the model for the C-to-Rust (C2Rust) translation task: 
> 1. **Continued pretraining** on Rust-centric corpora to strengthen the model's prior over idiomatic Rust syntax and standard-library usage; 
> 2. **Supervised fine-tuning (SFT)** on the `microsoft/Verus_Training_Data` dataset to instill debugging and self-repair behavior over Rust code; and 
> 3. **Task-specific SFT** on paired C/Rust solutions derived from LeetCode problems to teach direct semantic translation. 

We evaluate the resulting model using the agentic, static-analysis-guided verification framework of **SACTOR**, which performs structure-aware, two-phase (unidiomatic to idiomatic) translation with foreign-function-interface (FFI)-based end-to-end (E2E) testing. We report success rate, idiomaticity (Clippy lint counts, unsafe-code fraction), and failure-mode analyses, and compare our fine-tuned model against baseline Qwen3-27B and other LLMs evaluated under the same framework.

我们使用智能体式的、由静态分析引导的验证框架 **SACTOR** 对最终模型进行了评估。该框架执行结构感知、两阶段（从非地道到地道）的翻译，并结合了基于外部函数接口（FFI）的端到端（E2E）测试。我们报告了成功率、地道性（Clippy lint 计数、不安全代码占比）以及失败模式分析，并将微调后的模型与基线 Qwen3-27B 以及在相同框架下评估的其他 LLM 进行了对比。

> We evaluate the resulting model using the agentic, static-analysis-guided verification framework of **SACTOR**, which performs structure-aware, two-phase (unidiomatic to idiomatic) translation with foreign-function-interface (FFI)-based end-to-end (E2E) testing. We report success rate, idiomaticity (Clippy lint counts, unsafe-code fraction), and failure-mode analyses, and compare our fine-tuned model against baseline Qwen3-27B and other LLMs evaluated under the same framework.

---

## 概要与元数据 (Summary & Metadata)

* **arXiv ID:** [arXiv:2608.13681](https://arxiv.org/abs/2608.13681) [cs.SE]
* **主要学科:** 软件工程 (`cs.SE`)
* **其他学科:** 人工智能 (`cs.AI`), 新兴技术 (`cs.ET`)
* **提交日期:** 2026年8月13日
* **DOI:** [10.48550/arXiv.2608.13681](https://doi.org/10.48550/arXiv.2608.13681)

> * **arXiv ID:** [arXiv:2608.13681](https://arxiv.org/abs/2608.13681) [cs.SE]
> * **Primary Subject:** Software Engineering (`cs.SE`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Emerging Technologies (`cs.ET`)
> * **Submission Date:** August 13, 2026
> * **DOI:** [10.48550/arXiv.2608.13681](https://doi.org/10.48550/arXiv.2608.13681)

---

## 作者 (Authors)

* Pu Zhao
* Changdi Yang
* Yixiao Chen
* Yi Gao
* Yifan Cao
* Haochen Zeng
* Yanzhi Wang

> * Pu Zhao
> * Changdi Yang
> * Yixiao Chen
> * Yi Gao
> * Yifan Cao
> * Haochen Zeng
> * Yanzhi Wang

---

## 全文与资源 (Full-Text and Resources)

* [查看 PDF](https://arxiv.org/pdf/2608.13681)
* [HTML 版本（实验性）](https://arxiv.org/html/2608.13681v1)
* [TeX 源码](https://arxiv.org/src/2608.13681)
* **许可证:** [知识共享署名-相同方式共享 4.0 国际版](http://creativecommons.org/licenses/by-sa/4.0/)

> * [View PDF](https://arxiv.org/pdf/2608.13681)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.13681v1)
> * [TeX Source](https://arxiv.org/src/2608.13681)
> * **License:** [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)