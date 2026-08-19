---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 大语言模型
- 信号处理
- 数学推理
- 强化学习
- Qwen2.5
title: SignalReasoner：评估3B模型在信号数学推理中的性能上限
---
### 文章背景与核心概要
尽管诸如监督思维链（CoT）微调和强化学习（RL）等后训练方法已成功提升了大语言模型（LLM）的数学推理能力，但它们在信号处理领域的应用仍未得到充分探索。本报告研究了强化微调策略，旨在利用 **WirelessMATHBench-XL** 将 **Qwen2.5-3B-Base** 模型适配于研究生级别的信号数学问题。

该研究对两种主要的训练范式进行了基准测试：1. 基于可验证奖励在 WirelessMATHBench-XL 上直接进行强化学习（Direct RL）；2. 在蒸馏得到的无线领域 CoT 语料库上进行监督微调（SFT），随后进入相同的领域特定强化学习阶段。在两种范式中，作者评估了三种策略优化算法：群相对策略优化（GRPO）、群序列策略优化（GSPO）以及几何平均策略优化（GMPO），并通过实验揭示了初始化影响、算法稳定性和整体性能表现。

---

# SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning

**Authors:** Guozheng Sun  
**Submitted:** August 18, 2026  
**Primary Subject:** Computer Science > Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [arXiv:2608.17301](https://arxiv.org/abs/2608.17301) | **DOI:** [10.48550/arXiv.2608.17301](https://doi.org/10.48550/arXiv.2608.17301)

---

## 📋 Summary

尽管后训练方法（如监督思维链（CoT）微调和强化学习（RL））已成功增强了大语言模型（LLM）的数学推理能力，但它们在信号处理领域的应用在很大程度上仍未得到充分探索。

> While post-training methods like supervised chain-of-thought (CoT) fine-tuning and reinforcement learning (RL) have successfully enhanced the mathematical reasoning of large language models (LLMs), their application to signal processing remains largely under-explored. 

本报告研究了强化微调策略，旨在利用 **WirelessMATHBench-XL** 将 **Qwen2.5-3B-Base** 模型适配于研究生级别的信号数学问题。该研究对两种主要的训练范式进行了基准测试：
1. **直接强化学习（Direct RL）**：在 WirelessMATHBench-XL 上使用可验证奖励进行训练。
2. **监督微调（SFT）**：在蒸馏得到的无线领域 CoT 语料库上进行 SFT，随后进行相同的领域特定强化学习阶段。

在两种范式中，作者评估了三种策略优化算法：**群相对策略优化（GRPO）**、**群序列策略优化（GSPO）**和**几何平均策略优化（GMPO）**。

> This report investigates reinforcement fine-tuning strategies to adapt the **Qwen2.5-3B-Base** model for graduate-level signal mathematical problems using **WirelessMATHBench-XL**. The study benchmarks two primary training paradigms:
> 1. **Direct RL** on WirelessMATHBench-XL using verifiable rewards.
> 2. **Supervised Fine-Tuning (SFT)** on a distilled wireless-domain CoT corpus, followed by the same domain-specific RL stage.
> 
> Across both paradigms, the author evaluates three policy optimization algorithms: **Group Relative Policy Optimization (GRPO)**, **Group Sequence Policy Optimization (GSPO)**, and **Geometric-Mean Policy Optimization (GMPO)**. 

### Key Findings
* **初始化影响**：评估了领域感知的 CoT SFT 是否能有效初始化后续的强化学习。
* **算法稳定性**：评估了 GSPO 或 GMPO 相比于 GRPO 是否具备稳定性或准确性优势。
* **性能表现**：表现最好的模型取得了 **39.12%** 的总体准确率，较未训练的 Base 模型（12.37%）实现了**超过三倍的提升**。

> ### Key Findings
> * **Initialization Impact:** Evaluated whether domain-aware CoT SFT effectively initializes subsequent RL.
> * **Algorithm Stability:** Assessed whether GSPO or GMPO provide stability or accuracy advantages over GRPO.
> * **Performance:** The best-performing model achieved an overall accuracy of **39.12%**, marking a **more than threefold improvement** over the untrained Base model (12.37%).

---

## 🔗 Quick Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.17301) | [HTML（实验性）](https://arxiv.org/html/2608.17301v1) | [TeX 源码](https://arxiv.org/src/2608.17301)
* **开源许可：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17301) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17301) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17301)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.17301) | [HTML (Experimental)](https://arxiv.org/html/2608.17301v1) | [TeX Source](https://arxiv.org/src/2608.17301)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17301) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17301) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17301)