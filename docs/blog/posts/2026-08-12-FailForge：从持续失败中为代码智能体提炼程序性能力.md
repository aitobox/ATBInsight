---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 代码智能体
- 强化学习
- 拒绝采样微调
- 大语言模型
- SWE-bench
title: FailForge：从持续失败中为代码智能体提炼程序性能力
---
### 文章背景与核心概要
在软件工程任务中，拒绝采样微调（RFT）是训练代码智能体的主流方法，它通过筛选出通过测试的成功轨迹来进行训练。然而，传统的RFT方法会直接丢弃所有失败的尝试，从而浪费了最宝贵的训练信号——即那些最具信息量的高难度边界情况。

为了解决这一痛点，本文作者推出了 **FailForge** 这一创新性智能体框架，它能够将失败的执行轨迹转化为可操作的训练数据。通过诊断错误、将其提炼为简洁的技能并指导模型进行二次尝试，FailForge 成功恢复了超过 26% 的先前失败案例。在经过扩充的语料库上对 `Qwen3.5-4B` 模型进行训练，使其在 SWE-bench Verified 基准测试的解决率上取得了显著提升，相比强大的 RFT 基线提高了 **6.6 个百分点**，且在最具挑战性的任务上增幅最大。

---

## 📌 执行摘要 (Executive Summary)

拒绝采样微调（RFT）是训练代码智能体的一种主流方法，它通过在可验证的软件任务上学习成功的轨迹来实现。然而，标准的 RFT 会丢弃所有失败的运行轨迹，从而浪费了最具价值的训练信号：即那些最困难、最具信息量的边界情况。

为了克服这一局限性，作者推出了 **FailForge**，这是一个创新的智能体框架，可将失败的运行轨迹转化为可操作的训练数据。通过诊断错误、将其提炼为简洁的技能，并引导模型进行二次尝试，FailForge 成功恢复了超过 26% 的先前失败实例。在这一增强语料库上训练 `Qwen3.5-4B` 模型，相较于强大的 RFT 基线，在 SWE-bench Verified 的解决率上实现了显著的 **6.6 个百分点** 提升，其中在最具挑战性的任务上收益最为明显。

> Rejection Sampling Fine-Tuning (RFT) is a prominent method for training code agents by learning from successful trajectories on verifiable software tasks. However, standard RFT discards all failed rollouts, wasting the most valuable training signals: the hardest and most informative edge cases. 
> 
> To overcome this limitation, the authors introduce **FailForge**, an innovative agentic framework that transforms failed rollouts into actionable training data. By diagnosing errors, distilling them into concise skills, and guiding models through secondary attempts, FailForge successfully recovers over 26% of previously failed instances. Training the `Qwen3.5-4B` model on this augmented corpus yields a significant **6.6-point improvement** in the SWE-bench Verified resolve rate over a strong RFT baseline, with the greatest gains on the most challenging tasks.

---

## 👥 作者 (Authors)
* Dongyi Lv
* Fushun E
* Aichen Cai
* Liang Huang
* Ya Zhang
* Qiuyu Ding
* Canhui Wu
* Zhi Wang
* Yuesong Zhang
* Jiaqi Wang
* Nan Duan

> * Dongyi Lv
> * Fushun E
> * Aichen Cai
> * Liang Huang
> * Ya Zhang
> * Qiuyu Ding
> * Canhui Wu
> * Zhi Wang
> * Yuesong Zhang
> * Jiaqi Wang
> * Nan Duan

---

## 📖 摘要 (Abstract)

拒绝采样微调（RFT）被广泛用于训练代码智能体：它通过在可验证的软件工程任务上生成轨迹，保留通过测试的轨迹，并对成功的运行轨迹进行微调。然而，即使是强大的代码智能体，也会在相当一部分此类任务上频频失败，而标准的 RFT 却直接将这些失败案例丢弃了。这些被丢弃的样本恰恰是最困难、最具信息量的样本，它们源自那些成本高昂且来之不易的可验证实例。

更强大的基础模型或许可以减少失败次数，但剩余的难题依然构成了进一步提升模型性能的前沿阵地。为此，我们提出了 **FailForge**，这是一个能够将失败的运行轨迹转化为训练信号的智能体框架。针对每个失败的实例，智能体会根据错误反馈和执行轨迹来诊断失败原因，将诊断结果提炼为简洁且可操作的技能，并将该技能注入到智能体上下文中，以引导其进行第二次尝试。在技能指导下获得成功的轨迹将被重新纳入 RFT 语料库中。

至关重要的是，该技能在训练时会被移除，因此模型内部会内化恢复后的行为，而不会在推理时依赖外部提示。FailForge 以极小的额外成本恢复了超过 26% 的先前失败实例，并且在增强后的语料库上训练 `Qwen3.5-4B` 模型，使 SWE-bench Verified 的解决率比强大的 RFT 基线提升了 **6.6 个百分点**，其中性能增益主要集中在最困难的问题上。

> Rejection sampling fine-tuning (RFT) is widely used to train code agents by generating trajectories on verifiable software engineering tasks, retaining those that pass the tests, and fine-tuning on the successful rollouts. However, even strong code agents repeatedly fail on a substantial fraction of such tasks, and standard RFT simply discards these failures. The discarded samples are precisely the hardest and most informative ones, drawn from verifiable instances that are costly to curate. 
> 
> Stronger base models may reduce the number of failures, but the remaining hard cases still define the frontier for further improvement. We propose **FailForge**, an agentic framework that converts failed rollouts into training signal. For each failed instance, an agent diagnoses the failure from error feedback and execution traces, distills the diagnosis into a concise and actionable skill, and injects the skill into the agent context for a guided second attempt. Trajectories that succeed under skill guidance are folded back into the RFT corpus. 
> 
> Crucially, the skill is removed at training time, so the model internalizes the recovered behavior rather than relying on external hints at inference. FailForge recovers over 26% of previously failed instances at marginal additional cost, and training `Qwen3.5-4B` on the augmented corpus improves the SWE-bench Verified resolve rate by **6.6 points** over a strong RFT baseline, with gains concentrated on the hardest problems.

---

## 🔗 其他资源与链接 (Additional Resources & Links)

* **全文选项：**
  * [查看 PDF](https://arxiv.org/pdf/2608.08570)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.08570v1)
  * [TeX 源码](https://arxiv.org/src/2608.08570)
* **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2608.08570](https://doi.org/10.48550/arXiv.2608.08570)
* **引用与参考：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.08570)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08570)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08570)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2608.08570)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.08570v1)
>   * [TeX Source](https://arxiv.org/src/2608.08570)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.08570](https://doi.org/10.48550/arXiv.2608.08570)
> * **Citations & References:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.08570)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08570)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08570)