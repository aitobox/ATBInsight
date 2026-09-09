---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- EasyCrypt
- 密码学证明
- 多模态推理
- 大语言模型
- 形式化验证
title: Scratchy：基于视觉草稿板的多模态推理在EasyCrypt密码学证明生成中的应用
---
### 文章背景与核心概要

在形式化证明生成领域，大语言模型（LLMs）不断取得进展，但在密码学领域仍面临重大障碍。密码学证明需要精确协调概率、对抗博弈、不变量、假设和数学边界——这些通常通过像 EasyCrypt 这样的框架进行管理。由于证明论的依赖关系在线性文本表示中通常是隐式的，且分散在多个程序中，标准的 LLMs 很难对其进行有效的推理。

为了克服这一挑战，本文作者推出了 **Scratchy**，这是一种通过暴露隐藏的证明依赖关系来实现多模态生成的视觉草稿板方法。通过将自然语言安全描述、形式化上下文和目标命题转换为带类型的证明关系图，结构保持视觉编译器能够生成富含公式的视觉证明状态。然后，这些状态引导多模态模型准确生成 EasyCrypt 证明。此外，作者还引入了 **Scratchy-eval**，这是一个包含 114 个任务的数据集，其中包含源自官方 EasyCrypt 文件的 64 个安全形式证明生成任务和 50 个多项选择知识测试。评估表明，当利用 Scratchy 的结构化视觉证明表示时，经典 LLMs（如 GPT-5.6-Sol 和 Claude-Opus-5）的表现显著提升。

---

# Scratchy: Visual-Scratchpad Multimodal Reasoning for Cryptographic Proof Generation in EasyCrypt

**Authors:** Yupeng Ren, Zhaoxuan Li, Rui Zhang  
**Published:** September 5, 2026  
**arXiv ID:** [2609.06226](https://arxiv.org/abs/2609.06226) [cs.CR]  

---

## 📋 Summary

> Large Language Models (LLMs) continue to advance in formal proof generation, yet face significant hurdles within the cryptographic domain. Cryptographic proofs require the precise coordination of probabilities, adversarial games, invariants, assumptions, and mathematical bounds—traditionally managed via frameworks like EasyCrypt. Because proof-theoretic dependencies are typically implicit in linear text representations and scattered across multiple programs, standard LLMs struggle to reason through them effectively. 

> To overcome this, the authors introduce **Scratchy**, a visual-scratchpad approach that exposes hidden proof dependencies for multimodal generation. By transforming natural-language security descriptions, formal contexts, and target propositions into typed proof-relation graphs, a structure-preserving visual compiler generates formula-rich visual proof states. These states then guide multimodal models in accurately producing EasyCrypt proofs. Additionally, the authors introduce **Scratchy-eval**, a 114-task dataset comprising 64 security-form proof generations and 50 multiple-choice knowledge tests derived from official EasyCrypt files. Evaluations demonstrate that classical LLMs (such as GPT-5.6-Sol and Claude-Opus-5) perform significantly better when utilizing Scratchy's structured visual proof representations.

---

## 📑 Document Metadata

> | Field | Details |
> | :--- | :--- |
> | **Primary Subject** | Cryptography and Security (`cs.CR`) |
> | **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
> | **Submission Date** | September 5, 2026 |
> | **Document Length** | 12 pages, 5 figures, 5 tables |
> | **Full-Text Links** | [View PDF](https://arxiv.org/pdf/2609.06226) \| [HTML Version](https://arxiv.org/html/2609.06226v1) \| [TeX Source](https://arxiv.org/src/2609.06226) |
> | **DOI** | [10.48550/arXiv.2609.06226](https://doi.org/10.48550/arXiv.2609.06226) |

---

## 🔑 Key Innovations of Scratchy

> * **Typed Proof-Relation Graphs:** Normalizes security descriptions, formal contexts, and target propositions to explicitly track dependencies.
> * **Structure-Preserving Visual Compiler:** Converts abstract dependency graphs into formula-rich visual proof states designed for multimodal consumption.
> * **Scratchy-eval Dataset:** A rigorous benchmark consisting of 114 tasks (64 security-form proof generations and 50 knowledge tests) sourced from official EasyCrypt files to evaluate semantic grounding, relational invariants, and game reductions.