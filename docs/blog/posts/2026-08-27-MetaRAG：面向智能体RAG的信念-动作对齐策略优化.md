---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- RAG
- 大语言模型
- 强化学习
- 智能体
- 策略优化
title: MetaRAG：面向智能体RAG的信念-动作对齐策略优化
---
### 文章背景与核心概要
智能检索增强生成（Agentic RAG）赋予了语言模型动态决定何时继续搜索、何时综合最终答案的能力。然而，现有的强化学习（RL）方法主要依赖外部监督，却忽视了智能体关于“当前证据是否真正充足”的内部信念。

为了解决这一局限性，本文提出了 **MetaRAG** 框架，将搜索决策质量重新定义为**信念-动作对齐（belief-action alignment）**。通过引入“优先验证的动作生成”（Verify-first Action Generation）和“内部信念探测”（Internal Belief Probing），MetaRAG 衍生出一种由答案正确性门控的一致性奖励，从而避免对内部一致但错误的轨迹进行强化。至关重要的是，信念探测器仅在训练阶段使用，这意味着它**在推理时不会带来任何额外开销**。在七个公开问答基准上的实验表明，MetaRAG 显着提升了准确率与效率之间的权衡，并且其性能增益能够无缝迁移到深度研究环境、替代优化器以及多种模型骨干网络中。

---

# MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG

**arXiv:** [2608.24214](https://arxiv.org/abs/2608.24214) [cs.AI]  
**Conference:** EMNLP 2026 Main Conference  
**Submission Date:** August 25, 2026  

> **MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG**
> 
> **arXiv:** [2608.24214](https://arxiv.org/abs/2608.24214) [cs.AI]  
> **Conference:** EMNLP 2026 Main Conference  
> **Submission Date:** August 25, 2026  

---

## Authors

> ## Authors

* Qiuyi Qi
* Tian Liang
* Jiamu Wang
* Jinjian Zhang
* Wei Zhou
* Pengcheng Zhu
* Linjian Mo
* Ming Kong
* Jie Liu
* Qiang Zhu

> * Qiuyi Qi
> * Tian Liang
> * Jiamu Wang
> * Jinjian Zhang
> * Wei Zhou
> * Pengcheng Zhu
> * Linjian Mo
> * Ming Kong
> * Jie Liu
> * Qiang Zhu

---

## Summary

> ## Summary

Agentic retrieval-augmented generation (RAG) empowers language models to decide dynamically when to continue searching and when to synthesize a final answer. However, existing reinforcement learning (RL) methods predominantly rely on external supervision while neglecting the agent's internal belief regarding whether current evidence is genuinely sufficient. 

> Agentic retrieval-augmented generation (RAG) empowers language models to decide dynamically when to continue searching and when to synthesize a final answer. However, existing reinforcement learning (RL) methods predominantly rely on external supervision while neglecting the agent's internal belief regarding whether current evidence is genuinely sufficient. 

To resolve this limitation, **MetaRAG** reformulates search decision quality as **belief-action alignment**. By incorporating *Verify-first Action Generation* and *Internal Belief Probing*, MetaRAG derives a consistency reward gated by answer correctness—preventing the reinforcement of internally consistent yet incorrect trajectories. Crucially, the belief probe is restricted to training, meaning it introduces **zero inference-time overhead**. Experiments across seven public QA benchmarks demonstrate that MetaRAG significantly enhances the accuracy-efficiency trade-off, with performance gains that seamlessly transfer to deep research environments, alternative optimizers, and multiple model backbones.

> To resolve this limitation, **MetaRAG** reformulates search decision quality as **belief-action alignment**. By incorporating *Verify-first Action Generation* and *Internal Belief Probing*, MetaRAG derives a consistency reward gated by answer correctness—preventing the reinforcement of internally consistent yet incorrect trajectories. Crucially, the belief probe is restricted to training, meaning it introduces **zero inference-time overhead**. Experiments across seven public QA benchmarks demonstrate that MetaRAG significantly enhances the accuracy-efficiency trade-off, with performance gains that seamlessly transfer to deep research environments, alternative optimizers, and multiple model backbones.

---

## Abstract

> ## Abstract

Agentic retrieval-augmented generation (RAG) requires language models to decide when to continue searching and when to answer. Existing RL-based methods rely on external supervision and overlook the agent's internal belief about whether the current evidence is sufficient. 

> Agentic retrieval-augmented generation (RAG) requires language models to decide when to continue searching and when to answer. Existing RL-based methods rely on external supervision and overlook the agent's internal belief about whether the current evidence is sufficient. 

To address this problem, we reformulate the search decision quality as belief-action alignment and propose **MetaRAG**, a belief-action aligned policy optimization framework for agentic RAG. MetaRAG uses **Verify-first Action Generation** to elicit an explicit verification process before each actual action, and **Internal Belief Probing** to estimate the policy model's own answerability belief from the same question-history context. Based on these, MetaRAG derives a consistency reward that is further gated by answer correctness, avoiding reinforcement of internally consistent but incorrect trajectories. 

> To address this problem, we reformulate the search decision quality as belief-action alignment and propose **MetaRAG**, a belief-action aligned policy optimization framework for agentic RAG. MetaRAG uses **Verify-first Action Generation** to elicit an explicit verification process before each actual action, and **Internal Belief Probing** to estimate the policy model's own answerability belief from the same question-history context. Based on these, MetaRAG derives a consistency reward that is further gated by answer correctness, avoiding reinforcement of internally consistent but incorrect trajectories. 

The belief probe is used only during training and introduces no inference-time overhead. Experiments on seven public QA benchmarks show that MetaRAG consistently improves the accuracy-efficiency trade-off over strong RL-based agentic RAG baselines, with gains that transfer to deep research settings, different optimizers, and multiple model backbones.

> The belief probe is used only during training and introduces no inference-time overhead. Experiments on seven public QA benchmarks show that MetaRAG consistently improves the accuracy-efficiency trade-off over strong RL-based agentic RAG baselines, with gains that transfer to deep research settings, different optimizers, and multiple model backbones.

---

## Links & Resources

> ## Links & Resources

* **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.24214)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.24214v1)
* **TeX Source:** [arXiv Source File](https://arxiv.org/src/2608.24214)
* **DOI:** [10.48550/arXiv.2608.24214](https://doi.org/10.48550/arXiv.2608.24214)

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.24214)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.24214v1)
> * **TeX Source:** [arXiv Source File](https://arxiv.org/src/2608.24214)
> * **DOI:** [10.48550/arXiv.2608.24214](https://doi.org/10.48550/arXiv.2608.24214)