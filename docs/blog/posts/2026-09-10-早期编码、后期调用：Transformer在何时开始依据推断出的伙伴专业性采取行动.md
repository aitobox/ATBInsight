---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- Transformer
- 机械可解释性
- 对话建模
- 因果干预
- 语言模型
title: 早期编码、后期调用：Transformer在何时开始依据推断出的伙伴专业性采取行动
---
### 文章背景与核心概要

随着大语言模型（LLM）在多轮对话中的应用日益广泛，模型理解并适应对话伙伴特征（如专业水平）的能力变得至关重要。然而，模型内部是如何随时间推移处理这些隐式推断出的关系属性的，此前并未得到充分研究。本文探讨了 Transformer 模型在多轮对话过程中处理隐式推断关系属性（具体为对话伙伴的专业水平）的内部机制。

研究团队利用包含四个专业水平的模型扮演角色的合成语料库（*ExpertCollab*），发现了一个重要的时间差现象：伙伴的专业性信息在网络早期层最容易被解码，但在网络中点之前其可解码性会降至接近随机水平。通过反事实修补（counterfactual patching）进行的因果干预实验表明，早期层（注入专业性差异对后期层读数影响微乎其微）与中点之后的层（注入几乎完全传播）之间存在巨大的分离（超过一个数量级）。

这些发现明确了大语言模型中能够有效干预或读出“受伙伴条件约束行为”的神经网络区域，为未来精准调控模型社交与互动能力提供了重要的机制指引。

---

# Encoded Early, Used Late: Where Transformers Begin to Start Acting on an Inferred Partner's Expertise

**Authors:** Mika Okamoto, Gabriele Sarti  
**Published:** Scientific Understanding of Foundation Models (Sci-FM) Workshop at COLM 2026  
**arXiv:** [2609.07139 [cs.AI]](https://arxiv.org/abs/2609.07139) | **DOI:** [10.48550/arXiv.2609.07139](https://doi.org/10.48550/arXiv.2609.07139)  
**Submitted:** September 7, 2026  

> # Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise
> 
> **Authors:** Mika Okamoto, Gabriele Sarti  
> **Published:** Scientific Understanding of Foundation Models (Sci-FM) Workshop at COLM 2026  
> **arXiv:** [2609.07139 [cs.AI]](https://arxiv.org/abs/2609.07139) | **DOI:** [10.48550/arXiv.2609.07139](https://doi.org/10.48550/arXiv.2609.07139)  
> **Submitted:** September 7, 2026  

---

## Summary

本文研究了 Transformer 模型如何在多轮对话进程中处理隐式推断出的关系属性——具体而言，即对话伙伴的专业水平。

> ## Summary
> 
> This paper investigates how transformer models process implicitly inferred relational attributes—specifically, the expertise level of a dialogue partner—over the course of a multi-turn conversation. 

尽管先前的研究表明，直接输入的表述信息在模型的残余流（residual stream）中可读的位置与它实际影响输出的位置之间存在时间差，但本研究证明，这一现象对于通过逐步推断得出的属性同样适用。作者利用一个包含四个专业水平模型角色扮演的合成语料库（*ExpertCollab*）进行了对话分析，揭示了以下几点：
* **早期编码（Early Encoding）：** 伙伴的专业性最容易在网络的浅层（早期层）中被解码。
* **网络中点低谷（Mid-Network Dip）：** 在网络中点之前，可解码性会骤降至接近随机猜测的水平。
* **因果激活间隙（Causal Activation Gap）：** 反事实修补实验表明，浅层（在其中注入专业性差异几乎不会影响深层读数）与中点之后的深层（注入会几乎完全传播）之间存在巨大的分离，其跨度超过一个数量级。

这些发现界定了在大型语言模型中能够有效干预或读出伙伴条件行为（partner-conditioned behavior）的区域范围。

> While previous research has shown a temporal gap between where directly stated input information is readable in a model's residual stream and where it actually influences the output, this study demonstrates that the same phenomenon holds true for gradually inferred attributes. Utilizing a synthetic corpus (*ExpertCollab*) of dialogues featuring model-played personas across four expertise levels, the authors reveal that:
> * **Early Encoding:** Partner expertise is most easily decodable in the early layers of the network.
> * **Mid-Network Dip:** Decodability drops to near chance levels before the network's midpoint.
> * **Causal Activation Gap:** Counterfactual patching experiments show a dramatic separation (more than an order of magnitude) between early layers (where injecting expertise differences barely affects late-layer readouts) and post-midpoint layers (where injections propagate almost completely).
> 
> These findings bound the regions where interventions can effectively steer or read out partner-conditioned behavior in large language models.