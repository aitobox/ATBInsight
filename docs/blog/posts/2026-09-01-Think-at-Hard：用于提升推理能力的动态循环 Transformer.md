---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 大语言模型
- 推理能力
- 循环Transformer
- 动态迭代
- ICML 2026
title: Think-at-Hard：用于提升推理能力的动态循环 Transformer
---
### 文章背景与核心概要
本文介绍了已被 ICML '26 接收的论文《Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning》。提升大语言模型（LLM）的推理能力（尤其是在严格的参数限制下）一直是实际部署中的核心痛点。传统的循环 Transformer（Lopped Transformers）通过执行多次潜在迭代来超越标准的单次前向传播，从而精炼 Token，但它们通常会遭遇“潜在过度思考”（latent overthinking）问题——即在第一次前向传播中就已经预测正确的 Token，在后续迭代中往往会被无意间修改为错误结果。

为了解决这一难题，作者团队提出了 **Think-at-Hard (TaH)**——一种针对选择性迭代进行优化的循环 Transformer。TaH 核心引入了三大技术创新：1）轻量级神经决策器（Neural Decider），仅对初始前向传播后可能出错的 Token 选择性触发潜在迭代；2）深度感知 LoRA 模块，将潜在迭代的目标从通用的“下一个 Token 预测”转变为专注的“困难 Token 精炼”；3）双因果注意力机制（Duo-Causal Attention Mechanism），在 Token 序列维度之外扩展了额外的迭代深度维度，在保持完全序列并行性的同时实现跨迭代的信息流动。

实验表明，TaH 在数学、问答（QA）和代码编写等九个基准测试中均展现出稳定的性能提升。在参数量相同的情况下，TaH 比始终迭代的基线模型提升了 3.8–4.4%，同时跳过了 93% Token 的迭代；当引入小于 3% 的额外参数（用于 LoRA 和神经决策器）时，性能增益进一步扩大。

# Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning

**arXiv ID:** [2511.08577v4](https://arxiv.org/abs/2511.08577)  
**Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`); Performance (`cs.PF`)  
**Conference:** Accepted by ICML '26  
**Authors:** Tianyu Fu, Yichen You, Zekai Chen, Guohao Dai, Huazhong Yang, Yu Wang  
**Links:** [View PDF](https://arxiv.org/pdf/2511.08577) | [GitHub Repository](https://github.com/thu-nics/TaH)  

---

## Summary

增强大语言模型（LLM）的推理能力——特别是在严格的参数约束下——仍然是真实世界部署中的一个主要障碍。传统的循环 Transformer 通过执行多次潜在迭代来精炼 Token（超越了标准的前向传播），但它们往往会遭受**潜在过度思考（latent overthinking）**的困扰。当在第一次前向传播中已经被正确预测的 Token 在后面的迭代中被无意中修改为错误时，就会发生这种情况。

为了解决这个问题，作者推出了 **Think-at-Hard (TaH)**，这是一种针对选择性迭代进行优化的循环 Transformer。TaH 利用了：
1. **轻量级神经决策器：** 仅对初始前向传播后被识别为可能不正确的 Token 选择性地触发潜在迭代。
2. **深度感知 LoRA 模块：** 将潜在迭代的目标从通用的下一个 Token 预测转变为专注的困难 Token 精炼。
3. **双因果注意力机制：** 将注意力从 Token 序列维度扩展到一个额外的迭代深度维度，允许跨迭代的信息流，同时保持完全的序列并行性。

### 核心结果
* **效率与准确性：** 在参数量相同的情况下，比始终迭代的基线模型高出 **3.8–4.4%**，同时跳过了 **93% 的 Token** 的迭代。
* **基线比较：** 超越单迭代 Qwen3 基线 **3.0–3.8%**。
* **极小的参数开销：** 通过 LoRA 和神经决策器引入不到 3% 的额外参数，可将增益进一步推高至 **5.3–6.2%**（对比始终迭代）和 **6.1–6.8%**（对比单迭代 Qwen3）。
* **广泛的适用性：** 在涵盖数学、问答（QA）和代码任务的九个基准测试中展现出一致的性能提升。

---

## Abstract

> > 在真实世界应用中，提升大语言模型（LLM）的推理能力至关重要，尤其是在参数受限的情况下。循环 Transformer 通过对每个 Token 执行多次潜在迭代来进行精炼，从而超越了单次前向传播。然而，我们发现了一种潜在的过度思考现象：大多数 Token 预测在经过第一次传递后就已经正确了，但有时在后期的迭代中会被修改为错误。我们探讨了有选择地跳过潜在迭代是否可以提高准确性，并揭示了预言机（oracle）迭代策略具有巨大的潜力，可将性能提升高达 7.3%。
> > 
> > 受此启发，我们提出了 **Think-at-Hard (TaH)**，这是一种针对选择性迭代进行优化的循环 Transformer。TaH 采用轻量级神经决策器来触发潜在迭代，且仅在标准前向传播后可能不正确的 Token 上触发。在潜在迭代期间，深度感知低秩自适应（LoRA）模块将目标从通用的下一个 Token 预测转变为专注的困难 Token 精炼。双因果注意力机制将注意力从 Token 序列维度扩展到额外的迭代深度维度，在实现完全序列并行性的同时支持跨迭代信息流动。
> > 
> > 在九个基准测试上的实验表明，数学、QA 和代码任务均获得了持续的性能提升。在参数量相同的情况下，TaH 比始终迭代的基线模型高出 3.8-4.4%，同时跳过了 93% 的 Token 迭代，并且超过了单迭代 Qwen3 基线 3.0-3.8%。当允许通过 LoRA 和决策器增加小于 3% 的参数时，增益分别进一步增加到 5.3-6.2% 和 6.1-6.8%。

---

## Submission History

* **[v1]** 2025年11月11日 星期二 (573 KB)
* **[v2]** 2026年4月26日 星期日 (2,849 KB)
* **[v3]** 2026年6月14日 星期日 (912 KB)
* **[v4]** 2026年8月28日 星期五 *(本版本)*