---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- Transformer
- 语言生成
- 连分数
- 模型压缩
- 架构创新
title: CoFrGeNet：面向语言生成的连分数架构
---
### 文章背景与核心概要
尽管 Transformer 架构在语言生成领域长期占据统治地位，但其参数规模巨大、计算成本高昂的问题依然存在。本文介绍了一种名为 **CoFrGeNet（Continued Fraction Generative Networks，连分数生成网络）** 的全新函数类与架构家族，其灵感来源于数学中的连分数。研究的核心突破在于利用连分数推导出的架构组件，能够以极少的参数替代 Transformer 块中的多头注意力机制（MHA）和前馈网络（FFN），同时开发了定制化的梯度优化公式，提升了优化精度和效率。

该方法具备即插即用的特性，能够无缝融入现有的工业级训练与推理流程中。通过在 GPT2-xl (1.5B) 和 Llama3 (3.2B) 等主流架构上的大量实验（分别在 OpenWebText/GneissWeb 以及包含九个数据集的 docling 混合数据上进行预训练），结果表明：在仅使用原模型 $\frac{1}{2}$ 到 $\frac{2}{3}$ 的参数量且预训练时间更短的情况下，CoFrGeNet 在下游分类、问答、推理和文本理解任务上的性能依然能够与原模型相媲美甚至超越。这项研究为大语言模型的高效架构设计开辟了新路径。

---

# CoFrGeNet: Continued Fraction Architectures for Language Generation

**arXiv ID:** [2601.21766](https://arxiv.org/abs/2601.21766) [cs.CL]  
**Authors:** Amit Dhurandhar, Vijil Chenthamarakshan, Dennis Wei, Tejaswini Pedapati, Karthikeyan Natesan Ramamurthy, Rahul Nair  
**Submitted:** 29 January 2026; Last revised: 27 August 2026 (v5, earlier version accepted to ICML 2026)  
**License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) `[view license]` <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## Executive Summary

虽然 Transformer 仍然是语言生成领域的主导架构，但本文引入了 **CoFrGeNet（连分数生成网络）**——这是一种受连分数启发的全新函数类。

该研究的主要亮点包括：
* **高效替换：** 提出了源自连分数的架构组件，用于替代 Transformer 块中的多头注意力机制（MHA）和前馈网络（FFN），且所需参数显著减少。
* **自定义梯度优化：** 开发了专门的梯度公式，比标准基于 PyTorch 的梯度能够更准确、更高效地优化这些组件。
* **即插即用集成：** 对现有的训练或推理流程只需进行极小改动，从而便于顺利融入大型工业工作流。
* **竞争力的性能：** 在 OpenWebText/GneissWeb 上预训练的 GPT2-xl (1.5B) 以及在 9 个数据集的 docling 混合数据上预训练的 Llama3 (3.2B) 上进行了评估。结果表明，尽管仅使用了 $\frac{1}{2}$ 到 $\frac{2}{3}$ 的参数并缩短了预训练时间，其在下游分类、问答、推理和文本理解方面的性能仍能匹配或超越原始模型。

> While Transformers remain the dominant architecture for language generation, this paper introduces **CoFrGeNets (Continued Fraction Generative Networks)**—a novel function class inspired by continued fractions. 
> 
> Key highlights of the research include:
> * **Efficient Replacement:** Proposes architectural components derived from continued fractions to replace Multi-Head Attention (MHA) and Feed-Forward Networks (FFNs) in Transformer blocks using significantly fewer parameters.
> * **Custom Gradient Optimization:** Develops specialized gradient formulations to optimize these components more accurately and efficiently than standard PyTorch-based gradients.
> * **Plug-and-Play Integration:** Requires minimal changes to existing training or inference procedures, facilitating smooth adoption into large industrial workflows.
> * **Competitive Performance:** Evaluated on GPT2-xl (1.5B) pre-trained on OpenWebText/GneissWeb and Llama3 (3.2B) pre-trained on the 9-dataset docling mix. Results show performance on downstream classification, Q&A, reasoning, and text understanding that matches or outperforms original models—despite using only $\frac{1}{2}$ to $\frac{2}{3}$ of the parameters and requiring shorter pre-training times.

---

## Abstract

Transformer 可以说是语言生成领域的首选架构。在本文中，受连分数的启发，我们引入了一种用于生成建模的全新函数类。实现该函数类的架构系列被命名为 CoFrGeNets——连分数生成网络（Continued Fraction Generative Networks）。我们基于该函数类设计了新颖的架构组件，可以替代 Transformer 块中的多头注意力机制和前馈网络，同时需要少得多的参数。我们推导了自定义的梯度公式，以比使用标准基于 PyTorch 的梯度更准确、更高效地优化所提出的组件。我们的组件是一种插件式替代方案，对已经建立的基于 Transformer 的模型的训练或推理流程只需进行微小改动，从而使我们的方法易于并入大型工业工作流中。我们在两种截然不同的 Transformer 架构（GPT2-xl (1.5B) 和 Llama3 (3.2B)）上进行了实验，其中前者在 OpenWebText 和 GneissWeb 上进行预训练，后者在包含九个不同数据集的 docling 数据混合上进行预训练。结果表明，我们的模型在下游分类、问答、推理和文本理解任务上的性能具有竞争力，有时甚至优于原始模型，且参数量仅为后者的 $\frac{2}{3}$ 到 $\frac{1}{2}$，预训练时间更短。我们相信，未来针对硬件定制的实现将进一步发挥我们架构的真正潜力。

> Transformers are arguably the preferred architecture for language generation. In this paper, inspired by continued fractions, we introduce a new function class for generative modeling. The architecture family implementing this function class is named CoFrGeNets - Continued Fraction Generative Networks. We design novel architectural components based on this function class that can replace Multi-head Attention and Feed-Forward Networks in Transformer blocks while requiring much fewer parameters. We derive custom gradient formulations to optimize the proposed components more accurately and efficiently than using standard PyTorch-based gradients. Our components are a plug-in replacement requiring little change in training or inference procedures that have already been put in place for Transformer-based models thus making our approach easy to incorporate in large industrial workflows. We experiment on two very different transformer architectures GPT2-xl (1.5B) and Llama3 (3.2B), where the former we pre-train on OpenWebText and GneissWeb, while the latter we pre-train on the docling data mix which consists of nine different datasets. Results show that the performance on downstream classification, Q&A, reasoning and text understanding tasks of our models is competitive and sometimes even superior to the original models with $\frac{2}{3}$ to $\frac{1}{2}$ the parameters and shorter pre-training time. We believe that future implementations customized to hardware will further bring out the true potential of our architectures.

---

## Access & Resources

* **全文选项：** 
  * [查看 PDF](https://arxiv.org/pdf/2601.21766)
  * [HTML（实验性）](https://arxiv.org/html/2601.21766v5)
  * [TeX 源码](https://arxiv.org/src/2601.21766)
* **外部引用与工具：**
  * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2601.21766)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.21766)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.21766)
* **书签：** [BibSonomy](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2601.21766&description=CoFrGeNet: Continued Fraction Architectures for Language Generation) | [Reddit](https://reddit.com/submit?url=https://arxiv.org/abs/2601.21766&title=CoFrGeNet: Continued Fraction Architectures for Language Generation)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2601.21766)
>   * [HTML (experimental)](https://arxiv.org/html/2601.21766v5)
>   * [TeX Source](https://arxiv.org/src/2601.21766)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.21766)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.21766)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.21766)
> * **Bookmarks:** [BibSonomy](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2601.21766&description=CoFrGeNet: Continued Fraction Architectures for Language Generation) | [Reddit](https://reddit.com/submit?url=https://arxiv.org/abs/2601.21766&title=CoFrGeNet: Continued Fraction Architectures for Language Generation)