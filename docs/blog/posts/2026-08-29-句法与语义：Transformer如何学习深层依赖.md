---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- Transformers
- 深度学习
- 梯度饥饿
- 思维链
- 语义依赖
title: 句法与语义：Transformer如何学习深层依赖
---
### 文章背景与核心概要
尽管大型语言模型（LLM）展现出了令人印象深刻的句法流畅度，但它们习得深层语义依赖背后的优化动态机制仍然知之甚少。本文引入了一个机械论框架，将这一学习过程建模为**表层统计（Surface Statistics）**与**深层语义（Deep Semantics）**之间的竞争。

作者发现了**“梯度饥饿（Gradient Starvation）”**现象——即稀疏语义依赖的误差信号在早期被抑制，从而延迟了结构化推理，直到它作为相变突然出现。该研究解释了思维链（CoT）提示词为何能成功绕过这种抑制，并在Llama-3.1-8B和Qwen2.5-Coder-7B等模型上验证了这些见解，同时引入了一种拓扑对齐的对比目标函数，使变量绑定性能比标准交叉熵微调提升了2倍以上。

---

# 句法与语义：Transformer如何学习深层依赖

**作者：** Jiangrui Zhao, Xiaoting Du  
**发布时间：** 2026年6月26日  
**主要学科：** 计算与语言 (`cs.CL`)  
**次要学科：** 人工智能 (`cs.AI`)  
**arXiv：** [2608.26139](https://arxiv.org/abs/2608.26139) | **DOI：** [10.48550/arXiv.2608.26139](https://doi.org/10.48550/arXiv.2608.26139)

---

## 📌 摘要

> ## 📌 Summary

尽管大型语言模型（LLM）展现出卓越的句法流畅度，但控制其获取深层语义依赖的优化动态机制仍未得到充分理解。我们提出了一种机械论框架，将这一学习过程建模为**表层统计**与**深层语义**之间的竞争。

> While Large Language Models (LLMs) display impressive syntactic fluency, the optimization dynamics behind their acquisition of deep semantic dependencies remain poorly understood. This paper introduces a mechanistic framework modeling this learning process as a competition between **Surface Statistics** and **Deep Semantics**. 

我们的理论分析识别出了一种“梯度饥饿”现象，在此现象中，稀疏语义依赖的误差信号在早期优化过程中被主动抑制。这种抑制阻碍了结构化推理的学习，并导致其表现为一种突发的相变。

> The authors discover a **"Gradient Starvation"** phenomenon—where error signals for sparse semantic dependencies are suppressed early on, delaying structural reasoning until it abruptly emerges as a phase transition. The study explains why Chain-of-Thought (CoT) prompting successfully bypasses this suppression, validates these insights across models like Llama-3.1-8B and Qwen2.5-Coder-7B, and introduces a **topology-aligned contrastive objective** that improves variable binding performance by over 2x compared to standard cross-entropy fine-tuning.

此外，该框架为思维链（CoT）策略的有效性提供了机械论基础。通过将中间推理步骤外部化为具体的Token，CoT有效地绕过了隐式推理固有的抑制机制。我们在从玩具级Transformer到生产级模型（Llama-3.1-8B、Qwen2.5-Coder-7B）的不同规模上验证了这些发现。最后，在该理论的指导下，我们提出了一种拓扑对齐的对比目标，明确纠正了梯度几何形状。变量绑定任务的实验表明，我们的方法实现的性能提升是标准交叉熵微调的两倍以上。

> ## 🧠 Abstract

---

## 🧠 抽象

> Large Language Models demonstrate remarkable syntactic fluency, yet the optimization dynamics governing their acquisition of deep semantic dependencies remain poorly understood. We propose a mechanistic framework that models this learning process as a competition between **Surface Statistics** and **Deep Semantics**. 

*(重复摘要内容以保持双语段落对应)*

> Our theoretical analysis identifies a *"Gradient Starvation"* phenomenon where the error signals for sparse semantic dependencies are actively suppressed during early optimization. This suppression impedes the learning of structural reasoning and causes its emergence to manifest as a sudden phase transition. 

*(重复摘要内容以保持双语段落对应)*

> Furthermore, this framework offers a mechanistic basis for the effectiveness of Chain-of-Thought (CoT) strategies. By externalizing intermediate reasoning steps into concrete tokens, CoT effectively bypasses the suppression regime inherent to implicit reasoning. We validate these findings across scales ranging from toy transformers to production models (Llama-3.1-8B, Qwen2.5-Coder-7B). Finally, guided by this theory, we propose a topology-aligned contrastive objective that explicitly rectifies the gradient geometry. Experiments on variable binding tasks demonstrate that our method achieves an improvement that is over 2x larger than that obtained via standard cross-entropy fine-tuning.

---

## 🔗 链接与资源

> ## 🔗 Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.26139) | [HTML（实验性）](https://arxiv.org/html/2608.26139v1) | [TeX 源码](https://arxiv.org/src/2608.26139)
* **引用与元数据：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26139) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26139) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26139)
* **相关代码与工具：** [Hugging Face](https://huggingface.co/) | [alphaXiv](https://alphaxiv.org/) | [CatalyzeX](https://www.catalyzex.com)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.26139) | [HTML (Experimental)](https://arxiv.org/html/2608.26139v1) | [TeX Source](https://arxiv.org/src/2608.26139)
> * **Citation & Metadata:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26139) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26139) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26139)
> * **Associated Code & Tools:** [Hugging Face](https://huggingface.co/) | [alphaXiv](https://alphaxiv.org/) | [CatalyzeX](https://www.catalyzex.com)

---

*(许可协议参考：![许可图标](./images/345c7ad61f1b.png) [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/))*

> *(License Reference: ![license icon](./images/345c7ad61f1b.png) [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/))*