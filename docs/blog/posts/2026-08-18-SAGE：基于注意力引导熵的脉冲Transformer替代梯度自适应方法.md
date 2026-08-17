---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- 脉冲神经网络
- Transformer
- 替代梯度
- 注意力机制
- 机器学习
title: SAGE：基于注意力引导熵的脉冲Transformer替代梯度自适应方法
---
### 文章背景与核心概要
脉冲神经网络（SNNs）凭借其稀疏的事件驱动计算特性，成为传统深度神经网络的一种极具潜力且节能的替代方案。然而，训练脉冲神经网络面临着重大瓶颈，因为不可导的脉冲函数需要使用替代梯度（surrogate gradients），而其固定的形状在不同层和训练阶段往往并非最优。

为了解决这一局限性，研究人员推出了 **SAGE**（Surrogate-gradient Adaptation via Attention-Guided Entropy，基于注意力引导熵的替代梯度自适应），这是一种专门为基于 Transformer 的 SNN 设计的不确定性调制替代梯度机制。SAGE 利用从归一化自注意力熵中派生出的块级不确定性，动态调整替代梯度的斜率，同时保持最终的推理模型轻量且未经修改。

---

# SAGE：基于注意力引导熵的脉冲Transformer替代梯度自适应方法 (SAGE: Surrogate-gradient Adaptation via Attention-Guided Entropy for Spiking Transformers)

## 执行摘要 (Executive Summary)

脉冲神经网络（SNNs）凭借其稀疏的事件驱动计算，为传统的深度神经网络提供了一种节能的替代方案，但它们的训练仍然具有挑战性，因为不可导的脉冲函数需要替代梯度，而其固定形状在各个层和训练阶段可能并非最优。

为了解决这一局限性，研究人员引入了 **SAGE**（Surrogate-gradient Adaptation via Attention-Guided Entropy），这是一种针对基于 Transformer 的 SNN 的不确定性调制替代梯度机制。SAGE 利用从归一化自注意力熵中导出的块级不确定性来动态调整替代梯度的斜率，同时保持推理模型不变。通过仅调制训练时的替代参数，该方法在提高优化灵活性的同时，保持了原始架构和部署成本不变。

> ## Executive Summary
> Spiking neural networks (SNNs) present a promising, energy-efficient alternative to conventional deep neural networks due to their sparse, event-driven computation. However, training them presents a major bottleneck because non-differentiable spike functions require surrogate gradients, whose fixed shapes often remain suboptimal across different layers and training stages. 
> 
> To resolve this limitation, researchers have introduced **SAGE** (Surrogate-gradient Adaptation via Attention-Guided Entropy), an uncertainty-modulated surrogate-gradient mechanism tailored for Transformer-based SNNs. SAGE dynamically adjusts the surrogate-gradient slope using block-level uncertainty derived from normalized self-attention entropy, leaving the final inference model lightweight and unmodified.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [2608.13702](https://arxiv.org/abs/2608.13702)
* **主要学科:** 机器学习 (`cs.LG`)
* **次要学科:** 人工智能 (`cs.AI`)、计算机视觉与模式识别 (`cs.CV`)、神经与进化计算 (`cs.NE`)
* **提交日期:** 2026年8月13日
* **状态:** 会议审稿中

> * **arXiv ID:** [2608.13702](https://arxiv.org/abs/2608.13702)
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computer Vision and Pattern Recognition (`cs.CV`), Neural and Evolutionary Computing (`cs.NE`)
> * **Submission Date:** August 13, 2026
> * **Status:** In-Review at a Conference

### 作者 (Authors)
* **Kiran Nair**
* **Rodrigue Rizk**
* **KC Santosh**

> ### Authors
> * **Kiran Nair**
> * **Rodrigue Rizk**
> * **KC Santosh**

---

## 摘要 (Abstract)

脉冲神经网络（SNNs）通过利用稀疏的事件驱动计算，为传统的深度神经网络提供了一种节能的替代方案，但它们的训练仍然具有挑战性，因为不可导的脉冲函数需要替代梯度，而其固定形状在各个层和训练阶段可能并非最优。

在这项工作中，我们引入了 **SAGE**，这是一种针对基于 Transformer 的 SNN 的不确定性调制替代梯度机制。SAGE 从归一化自注意力熵中估计块级不确定性，并使用该信号在训练期间自适应调整替代梯度的斜率，同时保持推理模型不变。通过仅调制训练时的替代参数，所提出的方法在改善优化灵活性的同时，保留了原始架构和部署成本。

在 CIFAR-10/100 上的实验表明，SAGE 实现了优于固定替代基线的准确率，在多个模拟时间步长上均获得了 $1\text{--}2\%$ 的稳定提升。这些结果突出了注意力衍生不确定性作为轻量级训练信号，在基于 Transformer 的 SNN 中进行自适应替代梯度学习的潜力。

> ## Abstract
> Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep neural networks by exploiting sparse event-driven computation, but their training remains challenging because the non-differentiable spike function requires surrogate gradients whose fixed shape may be suboptimal across layers and training stages. 
> 
> In this work, we introduce **SAGE**, an uncertainty-modulated surrogate-gradient mechanism for Transformer-based SNNs. SAGE estimates block-level uncertainty from normalized self-attention entropy and uses this signal to adapt the surrogate-gradient slope during training while leaving the inference model unchanged. By modulating only the training-time surrogate parameter, the proposed method preserves the original architecture and deployment cost while improving optimization flexibility. 
> 
> Experiments on CIFAR-10/100 demonstrate that SAGE achieves improved accuracy over fixed-surrogate baselines, with results up to $1\text{--}2\%$ consistent gains across multiple simulation time steps. These results highlight the potential of attention-derived uncertainty as a lightweight training signal for adaptive surrogate-gradient learning in transformer-based SNNs.

---

## 核心亮点与创新 (Key Highlights & Innovations)

* **注意力引导熵：** 利用归一化自注意力熵来有效衡量块级网络不确定性。
* **动态斜率自适应：** 在训练阶段根据实时不确定性信号自动调整替代梯度斜率。
* **零部署开销：** 仅修改训练过程，完全不触及推理架构和部署成本。
* **持续的性能提升：** 在 CIFAR-10 和 CIFAR-100 基准测试中，跨不同的模拟时间步长，相比标准固定替代基线，实现了稳定的 $1\text{--}2\%$ 准确率提升。

> ## Key Highlights & Innovations
> 
> * **Attention-Guided Entropy:** Utilizes normalized self-attention entropy to effectively gauge block-level network uncertainty.
> * **Dynamic Slope Adaptation:** Automatically adapts the surrogate-gradient slope during the training phase based on real-time uncertainty signals.
> * **Zero Deployment Overhead:** Modifies exclusively the training process, leaving the inference architecture and deployment costs entirely untouched.
> * **Consistent Performance Boosts:** Delivers stable $1\text{--}2\%$ accuracy improvements over standard fixed-surrogate baselines on CIFAR-10 and CIFAR-100 benchmarks across varied simulation time steps.

---

## 全文与参考链接 (Full-Text & Reference Links)

* **查看 PDF:** [arXiv:2608.13702 PDF](https://arxiv.org/pdf/2608.13702)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.13702v1)
* **源码文件:** [TeX 源码](https://arxiv.org/src/2608.13702)
* **外部引用:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13702)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13702)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13702)

> ## Full-Text & Reference Links
> 
> * **View PDF:** [arXiv:2608.13702 PDF](https://arxiv.org/pdf/2608.13702)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.13702v1)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2608.13702)
> * **External Citations:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13702)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13702)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13702)

---
*许可证:* [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

> ---
> *License:* [Creative Commons Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)