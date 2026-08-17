---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- MIMO
- 深度学习
- 信号处理
- 迭代检测与译码
- Transformer
title: 面向大规模与高阶MIMO检测的“学习转换”（Learning-to-Transition）框架
---
### 文章背景与核心概要

高阶多输入多输出（MIMO）检测在现代通信系统中面临着严峻挑战：一方面需要在庞大的离散符号空间中进行高效搜索，另一方面需要为信道译码提供可靠的软信息。随着天线数量和调制阶数的增加，传统的检测算法往往在计算复杂度和性能之间难以取得平衡。

本文提出了一种名为“学习转换”（Learning-to-Transition, L2T）的创新框架，将MIMO检测建模为完整向量状态的随机转换序列。该方法通过引入通道耦合的Transformer架构，动态更新实例嵌入与采样策略，并利用分块自回归分解有效处理流间依赖。在硬判决检测中，该框架通过“残差到误码率（Residual-to-BER）”的课程学习策略进行训练；在软判决接收中，通过参数级策略克隆，将训练好的硬判决策略迁移至迭代检测与译码（IDD）接收机中，实现了高效的软信息生成，为LDPC译码提供了精确的对数似然比（LLR）。

---

## 摘要 (Abstract)

高阶多输入多输出（MIMO）检测需要在庞大的离散符号空间中进行高效搜索，同时为信道译码提供可靠的软信息。本文开发了一种“学习转换”（Learning-to-Transition, L2T）框架，将MIMO检测建模为完整向量转换的随机序列。在每次转换中，一个通道耦合的Transformer会同时更新实例嵌入和采样策略，而分块自回归分解则以适度的顺序复杂度捕捉流间依赖。对于硬输出检测，转换网络被递归应用，并通过“残差到误码率（residual-to-BER）”的课程学习进行训练，该过程首先从精确的残差度量中学习MIMO搜索几何结构，然后将策略与传输比特的准确性对齐。对于软输出接收，训练有素的硬判决策略在参数层面被克隆到非绑定（untied）软输入软输出迭代检测与译码（IDD）接收机的每一层中。这种从绑定到非绑定的迁移保留了已学习的零先验搜索动态，同时实现了在译码器反馈下针对特定层和轮次的专业化。在每一轮IDD中，译码器先验根据贝叶斯规则调整候选生成，似然加权的终端假设产生用于LDPC译码的后验和外在对数似然比（LLR）。多阶段训练策略通过让接收机逐步接触合成的和循环内译码器生成的先验，进一步稳定了从硬判决到软判决的迁移。

> High-order multiple-input multiple-output (MIMO) detection requires efficient search over a large discrete symbol space while producing reliable soft information for channel decoding. This paper develops a learning-to-transition (L2T) framework that formulates MIMO detection as a stochastic sequence of complete-vector transitions. At each transition, a channel-coupled Transformer updates both the instance embedding and the sampling policy, while a blockwise autoregressive factorization captures inter-stream dependence with moderate sequential complexity. For hard-output detection, a transition network is applied recursively and trained through a residual-to-BER curriculum, which first learns the MIMO search geometry from the exact residual metric and then aligns the policy with transmitted-bit accuracy. For soft-output reception, the well-trained hard policy is cloned at the parameter level into every layer of an untied soft-input soft-output iterative detection and decoding (IDD) receiver. This tied-to-untied transfer preserves the learned zero-prior search dynamics while enabling layer- and round-specific specialization under decoder feedback. Within each IDD round, decoder priors tilt candidate generation according to Bayes' rule, and likelihood-weighted terminal hypotheses produce posterior and extrinsic log-likelihood ratios for LDPC decoding. A multi-stage training strategy further stabilizes the hard-to-soft transfer by progressively exposing the receiver to synthetic and in-loop decoder-generated priors.

---

## 链接与资源 (Links & Resources)

* **全文访问:** [View PDF](https://arxiv.org/pdf/2608.14511) | [HTML (Experimental)](https://arxiv.org/html/2608.14511v1) | [TeX Source](https://arxiv.org/src/2608.14511)
* **DOI:** [10.48550/arXiv.2608.14511](https://doi.org/10.48550/arXiv.2608.14511)
* **引用工具:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.14511) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.14511) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.14511)