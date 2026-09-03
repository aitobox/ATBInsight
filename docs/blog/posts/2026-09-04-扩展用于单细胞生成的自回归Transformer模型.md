---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 单细胞生成
- 自回归Transformer
- 标度律
- 基因表达
- 基础模型
title: 扩展用于单细胞生成的自回归Transformer模型
---
### 文章背景与核心概要
单细胞测序技术的快速发展对生物学和机器学习交叉领域的建模提出了新要求。本文探讨了针对单细胞基因表达向量的自回归生成任务，其核心目标是给定特定细胞类型的一组表达向量，生成具有高真实度的新基因表达向量。

在技术实现上，该研究采用因果Transformer（Causal Transformer）架构，并结合了经学习的量化变分自编码器（VAE）分词器（Tokenizer），通过交叉熵损失函数进行训练。为了全面评估模型的表现，作者通过在保留的细胞类型基因表达向量上进行条件生成，并将生成的分布与真实的细胞类型分布进行对比，从而验证了其生物学保真度。此外，本文深入研究了该架构在不同参数规模和训练数据量下的扩展特性，首次拟合出了单细胞基础模型的双指数标度律（two-exponent scaling law）以及计算最优边界（compute-optimal frontier）。最后，文章还探讨了如何将预训练模型微调用于细胞扰动响应预测，为单细胞多组学研究提供了重要的理论与工具支撑。

---

# Scaling an Autoregressive Transformer for Single-Cell Generation

**Authors:** Aleksandr Sharipov, Yusif Mukhtarov, Igor Molybog  
**arXiv:** [arXiv:2608.02961 [cs.LG]] (https://arxiv.org/abs/2608.02961)  
**Submitted:** 3 August 2026; *Last revised: 1 September 2026*  
**Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Genomics (`q-bio.GN`)

---

## Summary

本文探讨了一项专注于单细胞基因表达向量的自回归生成任务。给定对应于特定细胞类型的一组向量，其目标是为该相同细胞类型生成更多真实的基因表达向量。

核心贡献包括：
* **模型架构：** 采用因果Transformer并配对一个经学习的量化VAE分词器，使用交叉熵损失函数进行训练。
* **模型评估：** 通过将模型条件化于保留的（held-out）基因表达向量上，并将生成的分布与真实的细胞类型分布进行对比，来评估生物学保真度。
* **标度律（Scaling Laws）：** 研究了在不同参数规模和训练数据量下的扩展特性，据信这是首次为单细胞基础模型拟合出联合双指数标度律和计算最优边界。
* **下游应用：** 探讨了将预训练模型进行微调以用于扰动响应预测的潜在策略。

> This paper explores a self-supervised generation task focused on single-cell gene expression vectors. Given a set of vectors corresponding to a specific cell type, the objective is to generate additional realistic gene expression vectors for that same cell type. 
> 
> Key contributions include:
> * **Model Architecture:** Utilizes a causal transformer paired with a learned quantized VAE tokenizer, trained using a cross-entropy loss function.
> * **Evaluation:** Evaluates biological fidelity by conditioning the model on held-out gene expression vectors and comparing the generated distribution against the ground-truth cell-type distribution.
> * **Scaling Laws:** Investigates the scaling properties across varying parameter sizes and training data volumes, establishing what is believed to be the first jointly-fit two-exponent scaling law and compute-optimal frontier for a single-cell foundation model.
> * **Downstream Applications:** Discusses potential fine-tuning strategies to adapt the pretrained model for perturbation response prediction.

---

## Abstract

我们研究了针对单细胞基因表达向量的自回归生成任务：给定来自某个细胞类型的一组向量，我们的目标是生成该细胞类型的额外基因表达向量。针对此任务，我们表征了生成的基因表达向量的生物学保真度以及预训练损失的标度行为。该模型是一个因果Transformer，配对一个经学习的量化VAE分词器，并使用交叉熵损失进行训练。为了评估模型，我们将模型条件化于某一细胞类型的保留基因表达向量上并生成基因表达向量，将由此产生的基因表达向量分布与该细胞类型的真实分布进行对比。我们通过改变训练参数的数量和训练数据量，研究了所提架构的标度属性。据我们所知，我们找到了单细胞基础模型的首个联合拟合双指数标度律与计算最优边界。最后，我们讨论了如何微调该预训练模型以用于扰动响应预测。

> We study a self-supervised generation task for single-cell gene expression vectors: given a set of vectors from a cell type, we aim to generate additional gene expression vectors of that cell type. For this task we characterize both the biological fidelity of the generated gene expression vectors and the scaling behavior of the pretraining loss. The model is a causal transformer paired with a learned quantized VAE tokenizer, trained with a cross-entropy loss. To evaluate the model, we condition it on held-out gene expression vectors of a cell type and generate vectors of gene expression, comparing the resulting distribution over gene expression vectors to the ground truth distribution of that cell type. We study the scaling properties of the proposed architecture by varying the number of trained parameters and the amount of training data. To our knowledge, we find the first jointly-fit two-exponent scaling law and compute-optimal frontier for a single-cell foundation model. Finally, we discuss how this pretrained model could be finetuned for perturbation response prediction.

---

## Additional Resources & Links

* **全文选项：** [查看 PDF](https://arxiv.org/pdf/2608.02961) | [HTML（实验性）](https://arxiv.org/html/2608.02961v2) | [TeX 源码](https://arxiv.org/src/2608.02961)
* **许可协议：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)  
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="32" />
* **引用：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.02961) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.02961) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.02961)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2608.02961) | [HTML (Experimental)](https://arxiv.org/html/2608.02961v2) | [TeX Source](https://arxiv.org/src/2608.02961)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="32" />
> * **Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.02961) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.02961) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.02961)