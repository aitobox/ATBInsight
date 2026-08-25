---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 尼日利亚皮钦语
- 情感理解
- 讽刺检测
- 文化推理
- 大语言模型评估
title: Wazobia Eval：尼日利亚皮钦语情感理解、讽刺检测与文化推理基准
---
### 文章背景与核心概要
尼日利亚皮钦语（Nigerian Pidgin）是非洲使用最广泛的语言之一，然而在现代语言模型的评估中，该语言却长期面临严重的代表性不足问题。现有的基准测试通常局限于基础的翻译、转录或通用情感分析，难以评估深层次的文化语境语言理解能力。为此，本文推出了 Wazobia Eval，这是一个开创性的评估基准，旨在弥补这一差距。

该项目包含一个经过人工精细标注、包含 550 多个样本的数据集，并配套了一个专门的 16 分类情感分类法，能够准确捕捉常规情感框架中缺失的复杂文化情感寄存器。通过建立标准化的评估协议，Wazobia Eval 为评估大模型在尼日利亚皮钦语情感理解、讽刺检测和文化推理方面的性能提供了关键的基础设施，极大地推动了非洲本土语言人工智能的研究进程。

---

# Wazobia Eval: A Benchmark for Nigerian Pidgin Emotion Understanding, Sarcasm Detection, and Cultural Reasoning

## Summary
**Wazobia Eval** is a foundational evaluation benchmark designed to bridge the representation gap for Nigerian Pidgin—one of Africa's most widely spoken languages—in modern language models. While existing benchmarks primarily focus on basic translation, transcription, or generic sentiment analysis, Wazobia Eval targets nuanced, culturally grounded language understanding. It features a manually annotated dataset of over 550 examples coupled with a specialized 16-category emotion taxonomy to capture intricate cultural emotional registers. The project establishes standardized evaluation protocols for emotion understanding, sarcasm detection, and cultural reasoning, providing critical infrastructure for future research in Nigerian language AI.

> **Wazobia Eval** 是一个基础评估基准，旨在弥合现代语言模型中尼日利亚皮钦语（非洲使用最广泛的语言之一）的代表性差距。现有的基准主要侧重于基础翻译、转录或通用情感分析，而 Wazobia Eval 则聚焦于细致入微、植根于文化的语言理解。它具有一个包含 550 多个样本的手动标注数据集，并搭配了专门的 16 分类情感分类法，以捕捉复杂的文化情感语域。该项目为情感理解、讽刺检测和文化推理建立了标准化的评估协议，为未来尼日利亚语言人工智能的研究提供了关键的基础设施。

---

## Metadata & Document Information

| Field | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.21369](https://arxiv.org/abs/2608.21369) [cs.CL] |
| **Primary Subject** | Computer Science > Computation and Language (`cs.CL`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **Author** | Stephanie Okoye |
| **Submission Date** | June 21, 2026 |
| **DOI** | [10.48550/arXiv.2608.21369](https://doi.org/10.48550/arXiv.2608.21369) |

> | 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.21369](https://arxiv.org/abs/2608.21369) [cs.CL] |
| **一级学科** | 计算机科学 > 计算与语言 (`cs.CL`) |
| **二级学科** | 人工智能 (`cs.AI`) |
| **作者** | Stephanie Okoye |
| **提交日期** | 2026年6月21日 |
| **DOI** | [10.48550/arXiv.2608.21369](https://doi.org/10.48550/arXiv.2608.21369) |

---

## Abstract
Nigerian Pidgin is one of Africa's most widely spoken languages, yet remains severely underrepresented in language model evaluation. Existing benchmarks primarily focus on translation, transcription, or generic sentiment analysis, leaving critical aspects of culturally grounded language understanding unmeasured. We introduce Wazobia Eval, a benchmark for evaluating Nigerian Pidgin emotion understanding, sarcasm detection, and cultural reasoning. The benchmark is built on a manually annotated dataset containing over 550 examples and a 16-category emotion taxonomy designed to capture culturally specific emotional registers that are not represented in conventional sentiment frameworks. Wazobia Eval provides standardized evaluation protocols and benchmark tasks for assessing model performance on nuanced Nigerian language understanding. We present the benchmark design, annotation methodology, taxonomy development process, and preliminary pilot evaluation results. Our goal is to provide foundational evaluation infrastructure for Nigerian language AI and establish a reproducible benchmark for future research.

> 尼日利亚皮钦语是非洲使用最广泛的语言之一，但在语言模型评估中却严重代表性不足。现有的基准主要侧重于翻译、转录或通用情感分析，导致植根于文化的语言理解的关键方面无法得到衡量。我们推出了 Wazobia Eval，这是一个用于评估尼日利亚皮钦语情感理解、讽刺检测和文化推理的基准。该基准建立在包含 550 多个样本的手动标注数据集以及一个 16 分类的情感分类法之上，旨在捕捉传统情感框架中未曾体现的具有文化特异性的情感语域。Wazobia Eval 提供了标准化的评估协议和基准任务，用于评估模型在细致入微的尼日利亚语言理解方面的性能。我们介绍了基准设计、标注方法、分类法开发过程以及初步的试点评估结果。我们的目标是为尼日利亚语言人工智能提供基础评估基础设施，并为未来的研究建立一个可复现的基准。

---

## Resources & Links
* **Dataset:** [Hugging Face Repository](https://huggingface.co/WAZOBIALABS)
* **Source Code:** [GitHub Repository](https://github.com/steffokoye/wazobia-eval)
* **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.21369)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> * **数据集：** [Hugging Face 仓库](https://huggingface.co/WAZOBIALABS)
* **源码：** [GitHub 仓库](https://github.com/steffokoye/wazobia-eval)
* **论文访问：** [查看 PDF](https://arxiv.org/pdf/2608.21369)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)