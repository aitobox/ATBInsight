---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- NVFP4
- 量化
- PTQ
- 大语言模型
- OCGQuant
title: OCGQuant：面向 NVFP4 量化的异常值伴随分组法
---
### 文章背景与核心概要
随着大语言模型规模的不断扩大，低比特推理的高效部署已成为学术界和工业界的研究热点。NVFP4 是一种用于低比特推理的高效微缩放（microscaling）格式，但在 NVFP4 块内，激活异常值往往会主导块缩放因子（block scale），从而加剧同块内其余数值的量化误差。现有的后训练量化（PTQ）方法虽然能够通过混合精度、旋转或残差补偿等策略缓解异常值带来的误差，但它们要么并非专门针对 NVFP4 设计，要么会引入额外的计算开销。

为了解决这一痛点，本文提出了 **OCGQuant**，这是一种创新的后训练量化方法。它引入了 **异常值伴随分组（Outlier-Companion Grouping, OCG）** 技术，自适应地将异常值通道与低幅值的伴随通道进行配对，在不引入额外计算的前提下最大限度地减少了“连带量化误差”（Collateral Quantization Error）。在 Llama3 和 Qwen3 等主流模型上的实验表明，OCGQuant 在保持极快预填充速度和较低峰值解码内存的同时，实现了最优的 WikiText-2 困惑度（perplexity）和下游任务准确率。

---

## OCGQuant：面向 NVFP4 量化的异常值伴随分组法

> ## OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization

## 摘要
**OCGQuant** 是一种创新的后训练量化（PTQ）方法，旨在利用 NVFP4 微缩放格式提高低比特推理效率。它解决了 NVFP4 块内的激活异常值问题，这些异常值通常会主导块缩放，并增加其余数值的量化误差。通过引入 **异常值伴随分组（OCG）** 自适应地将异常值通道与低幅值伴随通道配对，OCGQuant 在不引入额外计算的情况下，有效地最小化了*连带量化误差*。对 Llama3 和 Qwen3 等模型的评估表明，OCGQuant 实现了更优的 WikiText-2 困惑度和下游准确率，同时保持了快速的预填充速度和较低的峰值解码内存。

> ## Summary
> **OCGQuant** is an innovative post-training quantization (PTQ) method designed to improve low-bit inference efficiency using the NVFP4 microscaling format. It addresses the issue of activation outliers within NVFP4 blocks, which typically dominate the block scale and increase quantization errors for remaining values. By introducing **Outlier-Companion Grouping (OCG)** to adaptively pair outlier channels with low-magnitude companion channels, OCGQuant effectively minimizes the *Collateral Quantization Error* without introducing additional computation. Evaluations on models like Llama3 and Qwen3 demonstrate that OCGQuant achieves superior WikiText-2 perplexity and downstream accuracy while maintaining fast prefill speeds and low peak decoding memory.

---

## 论文元数据

* **arXiv ID:** [arXiv:2609.00066](https://arxiv.org/abs/2609.00066)
* **主要学科:** 计算与语言 (`cs.CL`)
* **其他学科:** 人工智能 (`cs.AI`), 机器学习 (`cs.LG`)
* **提交日期:** 2026年8月30日
* **会议状态:** 已被 EMNLP 2026（主会）接受
* **作者:** Yishan Yao, Binjun Li, Hanling Yi, Pengyu Li, Xiaoqing Liu, Zihan Yang, Xiaotian Yu, Zhiwen Yu

---

> ## Paper Metadata
> 
> * **arXiv ID:** [arXiv:2609.00066](https://arxiv.org/abs/2609.00066)
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
* **Submission Date:** August 30, 2026
* **Conference Status:** Accepted to EMNLP 2026 (Main Conference)
* **Authors:** Yishan Yao, Binjun Li, Hanling Yi, Pengyu Li, Xiaoqing Liu, Zihan Yang, Xiaotian Yu, Zhiwen Yu

---

## 摘要

NVFP4 是一种用于低比特推理的高效微缩放格式，但激活异常值仍会降低 NVFP4 块内的量化准确率。在每个量化块中，较大的激活值可能会主导块缩放因子，从而增加共享同一缩放因子的其余数值的量化误差。现有的后训练量化（PTQ）方法通过混合精度、旋转或残差补偿等策略来减轻异常值误差，但这些方法要么并非专门针对 NVFP4 量身定制，要么会引入额外的计算。

在这项工作中，我们从通道分组的角度重新审视了 NVFP4，并将由块最大值设定的缩放比例下，其余块值所产生可约简的误差定义为 **连带量化误差（Collateral Quantization Error）**。基于这一见解，我们提出了 **OCGQuant**，这是一种以 **异常值伴随分组（OCG）** 为核心的后训练量化方法，它自适应地将异常值通道与低幅值伴随通道配对，以改善 NVFP4 激活块的组成。在 Llama3 和 Qwen3 上的实验表明，在评估的 PTQ 方法中，OCGQuant 实现了最低的 WikiText-2 困惑度和最高的平均下游准确率，同时保持了接近 RTN 的预填充加速并与其峰值解码内存相匹配。

> ## Abstract
> NVFP4 is an efficient microscaling format for low-bit inference, but activation outliers can still degrade quantization accuracy within NVFP4 blocks. Within each quantization block, large activations can dominate the block scale, increasing the quantization error of the remaining values sharing the same scale. Existing post-training quantization (PTQ) methods mitigate outlier errors through strategies such as mixed precision, rotation, or residual compensation, but these approaches are either not specifically tailored to NVFP4 or introduce additional computation. 
> 
> In this work, we revisit NVFP4 from a channel-grouping perspective and define the reducible error incurred by remaining block values under the scale set by the block maximum as **Collateral Quantization Error**. Based on this insight, we propose **OCGQuant**, a post-training quantization method centered on **Outlier-Companion Grouping (OCG)**, which adaptively pairs outlier channels with low-magnitude companion channels to improve NVFP4 activation block composition. Experiments on Llama3 and Qwen3 show that OCGQuant achieves the lowest WikiText-2 perplexity and highest average downstream accuracy among evaluated PTQ methods, while maintaining prefill speedup close to RTN and matching its peak decoding memory.

---

## 资源与链接

* **PDF 版本:** [查看 PDF](https://arxiv.org/pdf/2609.00066)
* **HTML 版本:** [arXiv HTML（实验性）](https://arxiv.org/html/2609.00066v1)
* **源代码:** [GitHub 仓库](https://github.com/Eshamont/OCGQuant)
* **DOI:** [10.48550/arXiv.2609.00066](https://doi.org/10.48550/arXiv.2609.00066)

> ## Resources & Links
> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2609.00066)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2609.00066v1)
> * **Source Code:** [GitHub Repository](https://github.com/Eshamont/OCGQuant)
> * **DOI:** [10.48550/arXiv.2609.00066](https://doi.org/10.48550/arXiv.2609.00066)