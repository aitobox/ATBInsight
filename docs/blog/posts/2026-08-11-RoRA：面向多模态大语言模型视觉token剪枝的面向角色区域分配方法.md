---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- MLLM
- Token Pruning
- Computer Vision
- Model Acceleration
- RoRA
title: RoRA：面向多模态大语言模型视觉token剪枝的面向角色区域分配方法
---
### 文章背景与核心概要
多模态大语言模型（MLLMs）在处理图像时会将其编码为极长的视觉token序列，这导致预填充阶段以及KV缓存（KV-cache）存储面临巨大的计算开销。现有的免训练（training-free）剪枝方法通常将保留的token视为可互换的，而没有显式追踪对象相关区域的覆盖情况。

为了解决这一问题，**RoRA（Role-Oriented Regional Allocation，面向角色的区域分配）** 将视觉token剪枝构想为一个面向角色的区域证据分配问题。在固定的预算下，RoRA将token划分为受保护的语义核心、互补上下文以及细粒度细节。它利用注意力锚定区域（Attention-Anchored Regions, AARs）作为已覆盖对象支持的轻量级代理，从而在主流MLLM系列（如LLaVA和Qwen-VL）上实现了巨大的速度提升和卓越的准确率保持。

---

## 📋 摘要 (Summary)

> Multimodal large language models (MLLMs) encode images into extremely long visual token sequences, causing high computational overhead during prefilling and KV-cache storage. Existing training-free pruning methods often treat retained tokens as interchangeable without explicitly tracking object-related region coverage. 
> 
> To solve this, **RoRA (Role-Oriented Regional Allocation)** frames visual token pruning as a role-oriented regional evidence allocation problem. Under a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It leverages Attention-Anchored Regions (AARs) as lightweight proxies for covered object support, achieving massive speedups and superior accuracy retention across popular MLLM families (such as LLaVA and Qwen-VL).

多模态大语言模型（MLLMs）将图像编码为长的视觉token序列，这使得预填充和KV缓存存储成本高昂。现有的免训练剪枝方法通过重要性、多样性或空间覆盖来选择token，但它们将保留的token视为可互换的，并没有显式追踪哪些与对象相关的区域已经被覆盖。

我们提出了 **RoRA**，这是一个免训练框架，它将视觉token剪枝转化为面向角色的区域证据分配问题。在给定固定预算的情况下，RoRA将token划分为受保护的语义核心、互补上下文和细粒度细节。它首先通过位置先验和提示词校准的对象先验来校准文本条件下的注意力，然后从高置信度锚点构建**注意力锚定区域（AARs）**，作为已覆盖对象支持的轻量级代理。

上下文的探索主要在AARs外部进行，同时利用少量的AAR引导预算来恢复局部细节；成对相似性仅用于上下文阶段的冗余过滤。在匹配的预算下，RoRA在LLaVA和Qwen-VL系列中始终优于强有力的免训练基线，即便在激进的剪枝比例下也能保留绝大部分未剪枝的准确率，例如在LLaVA-1.5上**以88.9%的剪枝率保留了96.5%的完整性能**，并且在Qwen3-VL的75–90%剪枝率下比D2Pruner提升了约**5%**。在66.7%的剪枝率下，RoRA仅需 **0.7 ms** 即可完成token选择，并将端到端推理时间减少了 **24.6%**（在NVIDIA H800上实现了1.33倍的加速）。

---

## 📌 元数据与概览 (Metadata & Overview)

- **arXiv ID:** [arXiv:2608.07088](https://arxiv.org/abs/2608.07088) [cs.CV]
- **主分类:** 计算机视觉与模式识别 (`cs.CV`)
- **其他分类:** 人工智能 (`cs.AI`)
- **提交日期:** 2026年8月7日
- **作者:** Qiyanhui Lu, Han Wu, Rongjian Xu, Tingzhang Luo, Cheng Fan, Xinghao Chen, Minjing Dong, Jufeng Yang, Jianyuan Guo
- **官方代码仓库:** [GitHub - LukieLuu/RoRA](https://github.com/LukieLuu/RoRA)

---

## 🔍 摘要详述 (Abstract)

> Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. 
> 
> We present **RoRA**, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds **Attention-Anchored Regions (AARs)** from high-confidence anchors as lightweight proxies for covered object support. 
> 
> Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., **96.5% of full performance at 88.9% pruning** on LLaVA-1.5, and improving over D2Pruner by about **5% on Qwen3-VL at 75–90% pruning**. At a 66.7% pruning ratio, RoRA requires only **0.7 ms** for token selection and reduces end-to-end inference time by **24.6%** (a 1.33× speedup over unpruned inference on an NVIDIA H800).

多模态大语言模型（MLLMs）将图像编码为长的视觉token序列，这使得预填充和KV缓存存储成本高昂。现有的免训练剪枝方法通过重要性、多样性或空间覆盖来选择token，但它们将保留的token视为可互换的，并没有显式追踪哪些与对象相关的区域已经被覆盖。

我们提出了 **RoRA**，这是一个免训练框架，它将视觉token剪枝转化为面向角色的区域证据分配问题。在给定固定预算的情况下，RoRA将token划分为受保护的语义核心、互补上下文和细粒度细节。它首先通过位置先验和提示词校准的对象先验来校准文本条件下的注意力，然后从高置信度锚点构建**注意力锚定区域（AARs）**，作为已覆盖对象支持的轻量级代理。

上下文的探索主要在AARs外部进行，同时利用少量的AAR引导预算来恢复局部细节；成对相似性仅用于上下文阶段的冗余过滤。在匹配的预算下，RoRA在LLaVA和Qwen-VL系列中始终优于强有力的免训练基线，即便在激进的剪枝比例下也能保留绝大部分未剪枝的准确率，例如在LLaVA-1.5上**以88.9%的剪枝率保留了96.5%的完整性能**，并且在Qwen3-VL的75–90%剪枝率下比D2Pruner提升了约**5%**。在66.7%的剪枝率下，RoRA仅需 **0.7 ms** 即可完成token选择，并将端到端推理时间减少了 **24.6%**（在NVIDIA H800上实现了1.33倍的加速）。

---

## 🚀 核心性能亮点 (Key Performance Highlights)

- **高准确率保持：** 在LLaVA-1.5上，即使在88.9%的激进剪枝率下，仍能保留96.5%的完整模型性能。
- **卓越的泛化能力：** 在Qwen3-VL模型上，在75–90%的剪枝阈值下，性能超越了D2Pruner等强免训练基线约5%。
- **极低的延迟开销：** 在66.7%的剪枝率下，仅需0.7毫秒即可完成token选择。
- **真实场景效率：** 在NVIDIA H800 GPU上，端到端推理延迟降低了24.6%（实现1.33倍加速）。

> - **High Accuracy Retention:** Retains 96.5% of full model performance even under an aggressive 88.9% pruning ratio on LLaVA-1.5.
> - **Superior Generalization:** Outperforms strong training-free baselines like D2Pruner by ~5% on Qwen3-VL models at 75–90% pruning thresholds.
> - **Low Latency Overhead:** Requires merely 0.7 ms for token selection at a 66.7% pruning ratio.
> - **Real-world Efficiency:** Delivers a 24.6% reduction in end-to-end inference latency (1.33× speedup) on an NVIDIA H800 GPU.

---

## 🔗 快速链接 (Quick Links)

- **全文访问:** [查看 PDF](https://arxiv.org/pdf/2608.07088) | [HTML 版本](https://arxiv.org/html/2608.07088v1)
- **源码:** [GitHub 仓库](https://github.com/LukieLuu/RoRA)
- **引用与指标:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07088) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07088)