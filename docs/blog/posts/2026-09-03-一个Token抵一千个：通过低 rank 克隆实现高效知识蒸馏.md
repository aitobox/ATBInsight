---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 知识蒸馏
- 模型压缩
- 小型语言模型
- 低秩投影
- 大语言模型
title: 一个Token抵一千个：通过低 rank 克隆实现高效知识蒸馏
---
### 文章背景与核心概要
训练高性能的小型语言模型（SLMs）通常需要消耗大量的计算资源，即便采用传统的知识蒸馏和来自大型教师模型的剪枝技术，现有方法依然存在三大核心瓶颈：1. 激进的硬剪枝导致的严重信息丢失；2. 隐藏表示的对齐效率低下；3. 信息丰富激活值（特别是来自前馈网络 FFN 的信号）的利用率不足。

为了克服这些挑战，本文引入了 **低秩克隆（Low-Rank Clone, LRC）** 这一高效的预训练框架，旨在构建能够行为上模仿强大教师模型的 SLMs。LRC 利用一组低RANK投影矩阵，同时实现*软剪枝*（压缩教师权重）与*激活克隆*（将学生模型的激活及 FFN 信号与教师模型进行对齐）。这种统一的架构最大限度地提升了知识迁移效率，同时消除了对独立对齐模块的需求。

使用最先进的开源教师模型（如 `Llama-3.2-3B-Instruct` 和 `Qwen2.5-3B/7B-Instruct`）进行的实验结果表明，LRC 仅需 **200 亿（20B）个 Token**，就能达到或超越在数万亿 Token 上训练的顶级模型水平，实现了惊人的 **1,000 倍训练效率提升**。

---

# A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone

## 📋 Summary
> Training high-performing Small Language Models (SLMs) is notoriously resource-intensive, even when leveraging traditional knowledge distillation and pruning from larger teacher models. Existing approaches typically suffer from three major bottlenecks:
> 1. **Information loss** caused by aggressive hard pruning.
> 2. **Inefficient alignment** of hidden representations.
> 3. **Underutilization** of informative activations, particularly those originating from Feed-Forward Networks (FFNs).
> 
> To overcome these challenges, the paper introduces **Low-Rank Clone (LRC)**—an efficient pre-training framework that builds SLMs to behaviorally mimic strong teacher models. LRC utilizes a set of low-rank projection matrices designed to simultaneously perform *soft pruning* (compressing teacher weights) and *activation cloning* (aligning student activations and FFN signals with the teacher's). This unified architecture maximizes knowledge transfer while eliminating the need for standalone alignment modules. 
> 
> Experimental results using state-of-the-art open-source teacher models (such as `Llama-3.2-3B-Instruct` and `Qwen2.5-3B/7B-Instruct`) demonstrate that LRC matches or exceeds the performance of top-tier models trained on trillions of tokens—using a mere **20 billion tokens**, achieving an astonishing **1,000x improvement in training efficiency**.

---

## 📌 Metadata

| 字段 | 详情 |
| :--- | :--- |
| **arXiv 标识符** | `arXiv:2505.12781` [cs.CL] |
| **主要学科** | 计算与语言 (`cs.CL`) |
| **次要学科** | 人工智能 (`cs.AI`) |
| **作者** | Jitai Hao, Qiang Huang, Hao Liu, Xinyan Xiao, Zhaochun Ren, Jun Yu |
| **会议场地** | NeurIPS 2025 Spotlight |
| **提交历史** | • v1: 2025年5月19日<br>• v5 (最新): 2026年9月1日 |

> | Field | Details |
> | :--- | :--- |
> | **arXiv Identifier** | `arXiv:2505.12781` [cs.CL] |
> | **Primary Subject** | Computation and Language (`cs.CL`) |
> | **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
> | **Authors** | Jitai Hao, Qiang Huang, Hao Liu, Xinyan Xiao, Zhaochun Ren, Jun Yu |
> | **Conference Venue** | NeurIPS 2025 Spotlight |
> | **Submission History** | • v1: May 19, 2025<br>• v5 (Latest): September 1, 2026 |

---

## 🔗 Resources & Artifacts

* **全文论文：** [查看 PDF](https://arxiv.org/pdf/2505.12781) | [HTML 版本](https://arxiv.org/html/2505.12781v5) | [TeX 源码](https://arxiv.org/src/2505.12781)
* **代码库：** [GitHub - LowRankClone](https://github.com/CURRENTF/LowRankClone)
* **模型权重：** [Hugging Face 集合](https://huggingface.co/collections/JitaiHao/low-rank-clone-lrc-6828389e96a93f1d4219dfaf)

> * **Full-Text Papers:** [View PDF](https://arxiv.org/pdf/2505.12781) | [HTML Version](https://arxiv.org/html/2505.12781v5) | [TeX Source](https://arxiv.org/src/2505.12781)
> * **Code Repository:** [GitHub - LowRankClone](https://github.com/CURRENTF/LowRankClone)
> * **Model Checkpoints:** [Hugging Face Collection](https://huggingface.co/collections/JitaiHao/low-rank-clone-lrc-6828389e96a93f1d4219dfaf)

---

## 📑 Abstract

> 训练高性能的小型语言模型（SLMs）依然成本高昂，即便使用来自较大教师模型的知识蒸馏和剪枝技术也是如此。现有工作通常面临三个关键挑战：(1) 硬剪枝带来的信息丢失，(2) 表示对齐效率低下，以及 (3) 信息丰富的激活值（特别是来自前馈网络 FFN 的激活值）利用不足。为了解决这些挑战，我们引入了低秩克隆（LRC），这是一种高效的预训练方法，旨在构建渴望与强大教师模型行为对齐的 SLMs。LRC 训练了一组低秩投影矩阵，它们同时通过压缩教师权重来实现软剪枝，并通过将学生模型的激活（包括 FFN 信号）与教师模型的激活对齐来实现激活克隆。这种统一的设计最大化了知识迁移，同时消除了对显式对齐模块的需求。使用开源教师模型（例如 Llama-3.2-3B-Instruct、Qwen2.5-3B/7B-Instruct）进行的广泛实验表明，LRC 能够匹配或超越在数万亿 Token 上训练的最先进模型——而仅使用了 200 亿个 Token，实现了超过 1,000 倍的训练效率。

> Training high-performing Small Language Models (SLMs) remains costly, even with knowledge distillation and pruning from larger teacher models. Existing work often faces three key challenges: (1) information loss from hard pruning, (2) inefficient alignment of representations, and (3) underutilization of informative activations, particularly from Feed-Forward Networks (FFNs). To address these challenges, we introduce Low-Rank Clone (LRC), an efficient pre-training method that constructs SLMs aspiring to behavioral equivalence with strong teacher models. LRC trains a set of low-rank projection matrices that jointly enable soft pruning by compressing teacher weights, and activation clone by aligning student activations, including FFN signals, with those of the teacher. This unified design maximizes knowledge transfer while removing the need for explicit alignment modules. Extensive experiments with open-source teachers (e.g., Llama-3.2-3B-Instruct, Qwen2.5-3B/7B-Instruct) show that LRC matches or surpasses state-of-the-art models trained on trillions of tokens--while using only 20B tokens, achieving over 1,000x training efficiency.

---

## 🏷️ License & References

* **许可证：** [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **外部引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2505.12781) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2505.12781) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2505.12781)

> * **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2505.12781) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2505.12781) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2505.12781)