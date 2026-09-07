---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 大语言模型
- 深度学习
- Dropout
- 模型训练
- 模型推理
title: 别放弃Dropout：优化层稀疏性以实现高效的LLM训练与推理
---
### 文章背景与核心概要
本文重新评估了Transformer架构中的层丢弃（Layer Dropout，又称随机深度 stochastic depth）技术，挑战了现代大语言模型（LLM）预训练中普遍抛弃Dropout的惯例。作者通过系统性地研究最优的层分布、时间调度策略以及优化器超参数，证明了科学配置的层Dropout不仅能降低训练过程中的验证损失，还能在相同训练步数下**节省高达 25% 的训练 FLOPs（浮点运算次数）**。

此外，该研究指出层Dropout能够无缝解锁丰富的后训练（Post-training）效率优化手段，包括早期退出（Early Exiting）、中间层跳过（Layer Skipping）和自投机解码（Self-speculative Decoding），在对精度几乎无损的前提下实现了**高达 1.5 倍的推理加速**。实验部分涵盖了超 2400 场预训练实验（模型规模从 271M 到 8.2B、数据集高达 160B tokens），并在 Cerebras CS-3 系统上验证了其在大规模训练场景下的鲁棒性与有效性。

---

## 摘要
层Dropout（即随机深度）已被证明能够在语言和视觉Transformer中实现更快的训练速度、更高的准确率以及对零样本层剪枝的鲁棒性。然而，随着模型和数据集规模的扩大，Dropout——特别是层Dropout——在很大程度上已从大语言模型（LLM）的预训练配方中消失。尽管先前的一些研究报告称Dropout可能会降低准确率，但此前并没有全面的研究来量化、更不用说缓解这种负面影响。

在这项研究中，我们表明在最先进的LLM训练中应当使用层Dropout，并为其训练和后训练阶段的收益确立了最佳实践与缩放分析（scaling analysis）。具体而言，通过采用最优的层分布、时间调度和优化器超参数，我们发现，在相同的训练FLOPs下，层Dropout可以带来更低的损失。对于给定的训练步数，LLM在实现更低或相似的验证损失的同时，可以节省高达25%的训练FLOPs。此外，层Dropout还能带来显著的后训练优化，例如早期退出、中间层跳过和自投机解码，在精度损失可以忽略不计的情况下，带来高达1.5倍的推理加速。通过对2400多项训练实验（涵盖271M到8.2B参数的模型以及高达160B tokens的数据集）的研究，我们证明了这些发现在大规模训练机制下同样稳健可靠。所有的预训练实验均在Cerebras CS-3系统上运行。

> Layer dropout (a.k.a. stochastic depth) has been shown to enable faster training, higher accuracy, and robustness to zero-shot layer pruning in both language and vision transformers. However, as models and datasets have scaled, dropout - particularly layer dropout - has largely disappeared from large language models (LLMs) pre-training recipes. While some prior work has reported that dropout can degrade accuracy, no comprehensive study has quantified, let alone mitigated, this effect. 
> 
> In this study, we show that layer dropout should be used in state-of-the-art LLM training, establishing best practices and scaling analysis for both training and post-training benefits. Concretely, with optimal layer distribution, time schedule, and optimizer hyperparameters, we observe that at the same training FLOPs layer dropout leads to lower loss. For a given number of training steps, LLMs can achieve lower or similar validation loss while saving upto 25% of training FLOPs. Moreover, layer dropout enables significant post-training optimizations, such as early exit, intermediate-layer skipping, and self-speculative decoding, yielding up to 1.5x speedup with negligible accuracy loss. Across more than 2400 training experiments, spanning models from 271M to 8.2B parameters and datasets up to 160B tokens, we demonstrate that these findings extend reliably to large-scale training regimes. All pre-training experiments were run on Cerebras CS-3 systems.

---

## 全文与外部链接

* **获取论文：** 
  * [查看 PDF](https://arxiv.org/pdf/2609.05275)
  * [HTML 版本（实验性）](https://arxiv.org/html/2609.05275v1)
  * [TeX 源码](https://arxiv.org/src/2609.05275)
* **许可证：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **外部引用与工具：**
  * [谷歌学术搜索](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05275)
  * [Semantic Scholar API](https://api.semanticscholar.org/arXiv:2609.05275)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05275)

> ## Full-Text & External Links
> 
> * **Access Paper:** 
>   * [View PDF](https://arxiv.org/pdf/2609.05275)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2609.05275v1)
>   * [TeX Source](https://arxiv.org/src/2609.05275)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **External Citations & Tools:**
>   * [Google Scholar Search](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05275)
>   * [Semantic Scholar API](https://api.semanticscholar.org/arXiv:2609.05275)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05275)