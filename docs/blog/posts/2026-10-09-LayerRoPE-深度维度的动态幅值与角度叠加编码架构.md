---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-09
hide:
  - navigation
tags:
  - LayerRoPE
  - 深度位置编码
  - Transformer
  - 残差连接
  - 大语言模型
  - arXiv论文
title: "LayerRoPE：深度维度的动态幅值与角度叠加编码架构"
---

# LayerRoPE：深度维度的动态幅值与角度叠加编码架构

> # LayerRoPE: Dynamic Depth-wise Magnitude & Angular Superposition

> **arXiv:2610.09179** [cs.LG]  
> **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)  
> **Authors:** Shikhar Srivastava, Christopher Kanan  
> **Submitted:** October 6, 2026  
> **DOI:** [10.48550/arXiv.2610.09179](https://doi.org/10.48550/arXiv.2610.09179)

### 文章背景与核心概要

在现代 Transformer 架构中，随着网络深度不断增加，隐藏状态的特征范数往往呈数量级剧烈膨胀，这种长期困扰深度网络训练的现象被学界称为“深度诅咒” (Curse of Depth) ，并普遍被视作阻碍深层模型稳定训练的病态缺陷而加以压制。然而，Shikhar Srivastava 与 Christopher Kanan 深入剖析了跨越 9 个模型家族的 16 款主流预训练大语言模型 (Large Language Models, LLMs) ，颠覆性地发现这种范数膨胀并非有害缺陷，而是网络为了区分不同层信息而自发演化出的“涌现式深度位置编码” (Emergent Depth-Positional Encoding) ——它主要由残差流上唯一的逐层可学习增益参数 $\gamma$ 所承载，通过幅值增长与方向旋转协同记录网络层索引。基于这一深刻洞见，作者团队提出了创新的 **LayerRoPE** 架构，将旋转位置编码 (Rotary Position Embedding, RoPE) 思想巧妙迁移至深度维度，仅用单个共享向量搭配深度条件标量全面替换原本冗余的逐层参数，在计算量 (FLOPs) 变动不足 $0.02\%$ 的同时显著精简了参数量。实验证明，LayerRoPE 不仅以节省 $3.4\times$ 的算力达到了与传统 Pre-Norm 相当的损失水平，更首次在 512 层极深网络中展现出强劲收敛性与近乎单调的性能提升，同时具备极高的学习率鲁棒性，并能无缝迁移至循环潜变量模型与视觉 Transformer (ViTs) 中，为下一代超深层模型架构的设计开辟了全新路径。

---

## 内容概要

> ## Summary

在现代 Transformer 架构中，随着特征在网络深度方向逐层传递，隐藏状态的范数通常会出现数个数量级的剧烈膨胀——这一现象被学界广泛称为“深度诅咒” (Curse of Depth) ，且长期以来都被视作一种亟待抑制的训练病态。然而，本文的研究彻底颠覆了这一固有假设。通过对涵盖稠密模型、混合专家模型 (Mixture-of-Experts) 、混合架构以及 Pre-Norm、Peri-Norm 和 Post-Norm 归一化设计的 9 大模型家族、共 16 款主流预训练大语言模型 (Large Language Models, LLMs) 进行系统性探究，作者团队发现：这一数值膨胀根本不是有害的系统缺陷，而是网络在训练过程中自发演化出的**涌现式深度位置编码** (Emergent Depth-Positional Encoding) 。

> In modern Transformer architectures, the norm of hidden states typically grows by orders of magnitude as data propagates through depth—a phenomenon widely known as the "curse of depth" and generally treated as a pathology that requires suppression. This paper challenges that premise. Investigating 16 pre-trained Large Language Models (LLMs) across 9 families (spanning dense, mixture-of-experts, hybrid, and Pre-, Peri-, and Post-Norm designs), the authors discover that this growth is actually an **emergent depth-positional encoding**. 

这项深度编码主要由归一化权重 $\gamma$ (残差流上唯一逐层可学习的增益参数) 负责承载：它不仅在幅值上逐步变大，还在空间方向上动态旋转，两者巧妙配合，共同完成了对网络层索引的精确编码。基于这一深刻洞见，作者团队正式推出了 **LayerRoPE**——一种在网络深度轴向上对标旋转位置编码 (Rotary Position Embedding, RoPE) 的隐式深度编码方案。LayerRoPE 巧妙地用单个全局共享向量结合深度条件标量，全面替换掉了原本各层独立的 $\gamma$ 向量；在有效精简模型参数量的同时，对整体计算量 (FLOPs) 的影响不足 $0.02\%$ 。

> This encoding is carried by the normalization weight $\gamma$ (the sole learned per-layer gain on the residual stream), which grows in magnitude and rotates in direction to jointly encode the layer index. Building on this insight, the authors introduce **LayerRoPE**—an implicit depth-axis analog to Rotary Position Embedding (RoPE). LayerRoPE replaces all layerwise $\gamma$ vectors with a single shared vector and depth-conditioned scalars, simultaneously reducing parameters and incurring $<0.02\%$ change in FLOPs. 

### 核心发现与性能表现

> ### Key Findings & Performance:

* **极致效率 (Efficiency) ：** LayerRoPE 仅需减少 **$3.4\times$ 的计算量**，即可达到传统 Pre-Norm 1.3B 模型的同等损失水平。
* **超强扩展性 (Scalability) ：** 当网络深度大幅扩展至 512 层时，LayerRoPE 是唯一展现出强劲收敛性与近乎单调性能提升的架构方案。
* **高鲁棒性 (Robustness) ：** 将模型对学习率的敏感度改善了 $3\text{–}10\times$ ，并且能够开箱即用地无缝迁移到循环潜变量模型与视觉 Transformer (ViTs) 中。
* **范式转变 (Conceptual Shift) ：** LayerRoPE 并非一味缩小或压制残差流，反而对其进行了拓宽——它抑制了各个计算模块从残差流读取的信息幅度，同时放大了各模块写回的信息幅度。这深刻揭示出：维持深层网络的稳定性，核心在于对各计算模块施加深度条件化的动态调控，而非生硬压制残差流本身。

> * **Efficiency:** LayerRoPE reaches a Pre-Norm 1.3B model's loss using **$3.4\times$ less compute**.
> * **Scalability:** It is the only approach showing strong convergence and near-monotonic improvement when depth is scaled up to 512 layers.
> * **Robustness:** Improves learning-rate sensitivity by $3\text{–}10\times$ and transfers out-of-the-box to looped latent models and Vision Transformers (ViTs).
> * **Conceptual Shift:** Rather than shrinking the residual stream, LayerRoPE widens it, dampening what each block reads while amplifying what it writes, suggesting that depth stability relies on depth-conditioned regulation of computational blocks rather than suppressing the residual stream.

---

## 论文元数据与参考信息

> ## Metadata & Reference Information

* **arXiv 编号 (arXiv Identifier) ：** `arXiv:2610.09179` [cs.LG]
* **论文作者 (Authors) ：** Shikhar Srivastava, Christopher Kanan
* **提交时间 (Submitted) ：** 2026年10月6日
* **主学科分类 (Primary Subject) ：** 机器学习 (`cs.LG`)
* **交叉学科分类 (Secondary Subjects) ：** 人工智能 (`cs.AI`)、计算与语言 (`cs.CL`)
* **DOI 链接 (DOI) ：** [10.48550/arXiv.2610.09179](https://doi.org/10.48550/arXiv.2610.09179)

> * **arXiv Identifier:** `arXiv:2610.09179` [cs.LG]
> * **Authors:** Shikhar Srivastava, Christopher Kanan
> * **Submitted:** October 6, 2026
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
> * **DOI:** [10.48550/arXiv.2610.09179](https://doi.org/10.48550/arXiv.2610.09179)

---

## 全文与访问链接

> ## Full-Text & Access Links

* [查看 PDF 全文 (View PDF)](https://arxiv.org/pdf/2610.09179)
* [HTML 网页版本 (实验性) (HTML Version)](https://arxiv.org/html/2610.09179v1)
* [TeX 源码包 (TeX Source)](https://arxiv.org/src/2610.09179)
* [开源授权协议 (CC BY 4.0) (License)](http://creativecommons.org/licenses/by/4.0/)

> * [View PDF](https://arxiv.org/pdf/2610.09179)
> * [HTML Version (Experimental)](https://arxiv.org/html/2610.09179v1)
> * [TeX Source](https://arxiv.org/src/2610.09179)
> * [License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)
