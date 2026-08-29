---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 同态加密
- Transformer
- 模型压缩
- 多目标优化
- 隐私计算
title: ATLAS：在一小时内自动化近似 Transformer 以实现高效同态推理
---
### 文章背景与核心概要
在完全同态加密（FHE）下运行 Transformer 模型，能够让服务器在不泄露用户隐私的前提下，对加密数据执行安全的模型推理。然而，Transformer 高度依赖非线性操作（如 softmax、归一化和激活函数），这些操作在 FHE 中计算代价极高，必须替换为与 CKKS 方案兼容的多项式近似。

过去，基于 FHE 的 Transformer 严重依赖人工调参和统一的近似设置（如迭代次数和多项式阶数），并将这些设置无差别地应用于所有层。这种手动方法不仅缓慢、易错，而且无法捕捉层与层之间的差异。此外，其搜索空间呈指数级膨胀——对于 BERT 和 ViT 约为 $10^{85}$，对于 LLaMA3 则高达 $10^{228}$——这使得传统的微调或人工搜索完全无法实现。

为了克服这些挑战，本文推出了 **ATLAS**。这是一个免训练的框架，可通过多目标优化（平衡延迟与准确率）自动搜寻最佳的层间近似设置。利用两阶段优化策略和代理模型，ATLAS 将搜索过程缩短至大约 **一小时**，在编码器型、解码器型和视觉 Transformer 上，以极小的准确率损失将乘法深度和端到端延迟降低了约 **35%**。

---

# ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour

> # ATLAS：在一小时内自动化近似 Transformer 以实现高效同态推理

**Authors:** Jianhang Xie, Sicheng Tan, Vishnu Naresh Boddeti, Zhichao Lu  
**Subjects:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)  
**arXiv ID:** [arXiv:2607.23478 [cs.CR]](https://arxiv.org/abs/2607.23478)  
**Links:** [View PDF](https://arxiv.org/pdf/2607.23478) | [HTML Version](https://arxiv.org/html/2607.23478v2) | [GitHub Repository](https://github.com/jianhayes/ATLAS)

> **作者：** Jianhang Xie, Sicheng Tan, Vishnu Naresh Boddeti, Zhichao Lu  
> **学科分类：** 密码学与安全 (cs.CR)；人工智能 (cs.AI)；机器学习 (cs.LG)  
> **arXiv ID:** [arXiv:2607.23478 [cs.CR]](https://arxiv.org/abs/2607.23478)  
> **链接：** [查看 PDF](https://arxiv.org/pdf/2607.23478) | [HTML 版本](https://arxiv.org/html/2607.23478v2) | [GitHub 仓库](https://github.com/jianhayes/ATLAS)

---

## Summary

> ## 摘要

Running Transformer models under Fully Homomorphic Encryption (FHE) allows a server to perform secure inference on encrypted user data without exposing privacy. However, Transformers rely heavily on non-linear operations (such as softmax, normalization, and activations) that are computationally expensive and must be replaced with polynomial approximations compatible with the CKKS scheme. 

> 在完全同态加密（FHE）下运行 Transformer 模型，能够让服务器在不泄露用户隐私的前提下，对加密数据执行安全的模型推理。然而，Transformer 高度依赖非线性操作（如 softmax、归一化和激活函数），这些操作在 FHE 中计算代价极高，必须替换为与 CKKS 方案兼容的多项式近似。

Historically, FHE Transformers relied on hand-tuned, uniform approximation settings (such as iteration counts and polynomial degrees) applied indiscriminately across all layers. This manual approach is slow, error-prone, and fails to capture layer-wise variations. Furthermore, the search space scales exponentially—reaching roughly $10^{85}$ for BERT and ViT, and $10^{228}$ for LLaMA3—making traditional fine-tuning or manual searches impossible.

> 过去，基于 FHE 的 Transformer 严重依赖人工调参和统一的近似设置（如迭代次数和多项式阶数），并将这些设置无差别地应用于所有层。这种手动方法不仅缓慢、易错，而且无法捕捉层与层之间的差异。此外，其搜索空间呈指数级膨胀——对于 BERT 和 ViT 约为 $10^{85}$，对于 LLaMA3 则高达 $10^{228}$——这使得传统的微调或人工搜索完全无法实现。

To overcome these challenges, the paper introduces **ATLAS**, a training-free framework that automates the search for optimal layer-wise approximation settings via multi-objective optimization (balancing latency and accuracy). Utilizing a two-stage optimization strategy and a surrogate model, ATLAS completes the search process in approximately **one hour**, cutting multiplicative depth and end-to-end latency by roughly **35%** with minimal accuracy loss across encoder-only, decoder-only, and vision Transformers.

> 为了克服这些挑战，本文推出了 **ATLAS**。这是一个免训练的框架，可通过多目标优化（平衡延迟与准确率）自动搜寻最佳的层间近似设置。利用两阶段优化策略和代理模型，ATLAS 将搜索过程缩短至大约 **一小时**，在编码器型、解码器型和视觉 Transformer 上，以极小的准确率损失将乘法深度和端到端延迟降低了约 **35%**。

---

## Metadata and References

> ## 元数据与参考文献

* **Submitted:** 26 Jul 2026 (v1), last revised 27 Aug 2026 (v2)
* **DOI:** [10.48550/arXiv.2607.23478](https://doi.org/10.48550/arXiv.2607.23478)
* **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/) `<img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">`

> * **提交时间：** 2026年7月26日 (v1)，最后修订于 2026年8月27日 (v2)
> * **DOI:** [10.48550/arXiv.2607.23478](https://doi.org/10.48550/arXiv.2607.23478)
> * **许可协议：** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-nd/4.0/) `<img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">`