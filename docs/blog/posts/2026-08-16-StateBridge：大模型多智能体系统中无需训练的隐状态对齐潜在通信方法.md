---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 大语言模型
- 多智能体系统
- 隐状态通信
- 训练无关
- 知识对齐
title: StateBridge：大模型多智能体系统中无需训练的隐状态对齐潜在通信方法
---
### 文章背景与核心概要

传统的大语言模型（LLM）多智能体系统主要依赖离散的文本标记（tokens）进行通信，这种方式存在严重的“离散瓶颈”，导致隐状态中蕴含的丰富连续信息在转换过程中被丢失。虽然现有的潜在通信（latent communication）研究尝试直接传输隐表示，但通常需要复杂的逐层工作记忆注入或额外的训练投影层，这限制了方法的通用性和可移植性。

本文提出的 **StateBridge** 是一种无需训练的潜在通信方案。该方法通过闭式正交变换（closed-form orthogonal transformation），将发送方的最终层隐状态直接对齐到接收方的输入空间，并结合轻量级的范数校准和词表锚定技术，确保了与预训练分布的兼容性。实验结果表明，StateBridge 在数学推理、代码生成和问答任务中表现卓越，在 26 个测试模型-任务对中的 22 个上达到了最优或并列最优水平。

---

## 论文元数据

* **arXiv ID:** [`arXiv:2608.13317`](https://arxiv.org/abs/2608.13317) [cs.AI]
* **学科:** 人工智能 (`cs.AI`)
* **出版:** 被 COLM 2026 录用 (18 页, 3 张图, 4 张表)
* **提交日期:** 2026年8月13日
* **作者:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
* **许可协议:** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 摘要

> Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

基于大语言模型的多智能体系统通常使用文本（即离散标记）进行通信。然而，文本引入了离散瓶颈。将发送方的连续隐状态转换为离散标记会丢失仅靠标记身份无法捕获的信息。最近的研究提出了潜在通信作为替代方案，即智能体直接传输隐表示而不将其转换为文本。然而，现有的潜在方法要么在 Transformer 的每一层注入工作记忆，要么需要限制可移植性的训练投影层。我们提出了 StateBridge，这是一种无需训练的潜在通信方法，通过闭式正交变换将发送方的最终层隐状态对齐到接收方的输入空间。轻量级的范数校准和词表锚定确保了与预训练输入分布的兼容性。对齐后的状态作为连续前缀附加到接收智能体的输入之前。我们在数学推理、代码生成和问答任务中评估了 StateBridge，使用了来自两个系列的四个模型。StateBridge 在 26 个模型-任务对中的 22 个上取得了最优或并列最优分数，持续优于最强的基线模型。

---

## 关键链接与资源

* **全文访问:** [查看 PDF](https://arxiv.org/pdf/2608.13317) | [HTML (实验性)](https://arxiv.org/html/2608.13317v1) | [TeX 源码](https://arxiv.org/src/2608.13317)
* **引用与参考:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13317) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13317) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13317)