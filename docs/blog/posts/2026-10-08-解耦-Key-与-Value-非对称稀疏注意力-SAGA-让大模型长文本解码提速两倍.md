---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-08
hide:
  - navigation
tags:
  - SAGA
  - 非对称注意力
  - 稀疏注意力
  - GQA
  - 解码加速
  - NeurIPS 2026
  - arXiv论文
title: "解耦 Key 与 Value：非对称稀疏注意力 SAGA 让大模型长文本解码提速两倍"
---

# 解耦 Key 与 Value：非对称稀疏注意力 SAGA 让大模型长文本解码提速两倍

> # More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding

### 文章背景与核心概要

在大语言模型 (Large Language Model, LLM) 的自回归文本生成过程中，注意力机制的显存占用与计算开销一直是制约长文本推理速度的核心痛点。虽然稀疏注意力机制能够大幅减少对非关键 Token 的计算，但研究人员敏锐地发现：稀疏化之后，注意力概率与 Value 向量相乘的计算开销已微乎其微，真正的性能瓶颈转移到了 Query 与 Key 的匹配计算上。为此，入选 NeurIPS 2026 的这项研究突破性地提出了**非对称稀疏分组查询注意力 (Sparse Asymmetric Group-Query Attention, SAGA)** 与**近似 Top-N 注意力 (Approximate top-N, Atop-N)** 架构，创新性地将 Key 和 Value 的注意力头数量进行解耦——通过大幅削减 Key 头数量来打破瓶颈加速推理，同时保留更多 Value 头以维系模型的强大表达能力。在长上下文场景下，SAGA 配合 Atop-N 实现了端到端解码速度超 $2\times$ 的显著飞跃，且模型质量几乎无损；研究团队还进一步设计了轻量高效的微调方法，让现有预训练大模型无需从头训练即可快速无缝升级。

---

## 内容概要

> ## Summary

本文提出了**非对称稀疏分组查询注意力 (Sparse Asymmetric Group-Query Attention, SAGA)** 以及**近似 Top-N 注意力 (Approximate top-N, Atop-N)** ，旨在全面加速大语言模型 (Large Language Model, LLM) 的自回归生成过程。研究人员观察到，在各类稀疏注意力方法中，注意力概率与 Value 向量相乘的计算开销已经被大幅压缩到几乎可以忽略，整个系统的性能瓶颈由此转移到了 Query 与 Key 的乘积计算上。基于这一核心洞察，作者提出将 Key 与 Value 的头数量彻底解耦：大幅减少 Key 头的数量以打通 Query-Key 的计算瓶颈，同时保留较多的 Value 头以维持模型原有的表征能力。实验表明，在长上下文场景下，SAGA 结合 Atop-N 带来了超过 $2\times$ 的端到端解码提速，且模型生成质量依然十分稳健；此外，该方案不仅支持从零开始训练，还配备了一套高效的微调方法。

> This paper introduces **Sparse Asymmetric Group-Query Attention (SAGA)** and **approximate top-N (Atop-N) attention** to accelerate autoregressive generation in Large Language Models (LLMs). By observing that sparse attention methods render probability-value multiplications negligible, the authors propose decoupling key and value head counts—reducing key heads to alleviate query-key bottlenecks while preserving more value heads to maintain capacity. Together, SAGA and Atop-N achieve over $2\times$ end-to-end decoding speedups at long contexts while preserving competitive model quality, supported by both an efficient fine-tuning method and training from scratch.

---

## 论文发表信息

> ## Publication Details

* **arXiv ID：** [arXiv:2610.04753 [cs.CL]](https://arxiv.org/abs/2610.04753)
* **DOI 链接：** [10.48550/arXiv.2610.04753](https://doi.org/10.48550/arXiv.2610.04753)
* **学术会议：** 已被 NeurIPS 2026 接收录用
* **学科领域：** 计算与语言 (`cs.CL`) ；人工智能 (`cs.AI`)
* **提交动态：** 2026年10月3日首次提交；2026年10月6日最新修订 (v2 版本)

> * **arXiv ID:** [arXiv:2610.04753 [cs.CL]](https://arxiv.org/abs/2610.04753)
> * **DOI:** [10.48550/arXiv.2610.04753](https://doi.org/10.48550/arXiv.2610.04753)
> * **Conference:** Accepted to NeurIPS 2026
> * **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)
> * **Submission Timeline:** Submitted on October 3, 2026; Last revised on October 6, 2026 (v2)

---

## 论文作者

> ## Authors

* Noam Elata
* Itay Lamprecht
* Mikey Shechter
* Daniel Ohayon
* Itay Hubara
* Daniel Soudry

> * Noam Elata
> * Itay Lamprecht
> * Mikey Shechter
> * Daniel Ohayon
> * Itay Hubara
> * Daniel Soudry

---

## 论文摘要

> ## Abstract

大语言模型 (LLM) 在执行自回归文本生成任务时，常常受限于注意力机制庞大的显存开销与计算需求。稀疏注意力方法通过仅挑选注意力矩阵中高概率的有效条目，在一定程度上减轻了这一负担。然而我们观察到，在许多现有的稀疏注意力方法中，这种过滤使得注意力概率与 Value 向量相乘的计算量变得微不足道，反倒使系统的整体瓶颈转移到了 Query 与 Key 的匹配计算环节。因此，我们可以大幅削减 Key 头的数量以加速推理，同时保留更多的 Value 头，这样既能维护模型的表征容量，又几乎不会引入额外的解码开销。

> Autoregressive generation in Large Language Models (LLMs) is constrained by the memory and computational demands of attention mechanisms. Sparse attention methods mitigate this cost by selecting only high-probability entries of the attention matrix. We observe that in many such methods, this renders the probability-value multiplication negligible, shifting the bottleneck to the query-key step. Key heads can therefore be reduced to accelerate inference, while retaining more value heads preserves capacity with limited additional decoding cost. 

针对这一发现，我们提出了**非对称稀疏分组查询注意力 (Sparse Asymmetric Group-Query Attention, SAGA)** ，通过解耦 Key 与 Value 的头数量来充分释放这一机制的潜能；同时，我们搭配了**近似 Top-N 注意力 (Approximate top-N, Atop-N)** ——一种专门用于探究稀疏性与头数非对称性相互作用的简洁稀疏注意力方法。我们在理论上对这种非对称设计的增益进行了严格形式化推演，并在高达 1.5B 参数规模的模型上，通过端到端延迟实测与生成质量评测完成了充分的实证验证。实验结果表明，在长上下文场景下，SAGA 与 Atop-N 相比全注意力 GQA 基线实现了超过 $2\times$ 的端到端解码加速。在各大基准测试中，基于 SAGA 从零开始训练的模型，其综合表现几乎完全媲美同等配置的 GQA 变体。为了便于工业界和学术界快速落地采用，我们还推出了一种高效的微调方法，能够将已有的预训练模型直接转换为 SAGA 架构，让开发者无需承受高昂的重训成本便能直接享受加速红利。

> We introduce **Sparse Asymmetric Group-Query Attention (SAGA)**, which decouples key and value head counts to exploit this principle, and pair it with **approximate top-N (Atop-N) attention**, a simple sparse attention method designed to study the interaction between sparsity and head-count asymmetry. We formalize the benefits of this asymmetry theoretically and validate them empirically through latency measurements and quality evaluations on models up to 1.5B parameters. Together, SAGA and Atop-N achieve end-to-end decoding speedups exceeding $2\times$ over our full-attention GQA baseline at long contexts. Models trained from scratch with SAGA nearly match the quality of comparable GQA variants on the evaluated benchmarks. To facilitate adoption, we introduce an efficient fine-tuning method that converts pretrained models to the SAGA architecture, enabling practitioners to benefit from our approach without costly retraining.

---

## 相关资源与链接

> ## Additional Resources & Links

* **论文全文：** [查看 PDF (View PDF)](https://arxiv.org/pdf/2610.04753) | [HTML 在线版本 (HTML Version)](https://arxiv.org/html/2610.04753v2) | [TeX 源码 (TeX Source)](https://arxiv.org/src/2610.04753)
* **代码与社区生态：** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX 算法检索](https://www.catalyzex.com) | [DagsHub](https://dagshub.com/)
* **学术引用检索：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.04753) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.04753) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.04753)

> * **Full-Text:** [View PDF](https://arxiv.org/pdf/2610.04753) | [HTML Version](https://arxiv.org/html/2610.04753v2) | [TeX Source](https://arxiv.org/src/2610.04753)
> * **Code & Integrations:** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [DagsHub](https://dagshub.com/)
> * **Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.04753) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.04753) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.04753)
