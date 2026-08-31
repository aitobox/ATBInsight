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
- 机械可解释性
- 模乘法
- 傅里叶变换
- 离散对数
title: 离散对数时钟：Transformer 如何学习模乘法
---
### 文章背景与核心概要
当小型 Transformer 模型对模乘法产生“突发性过拟合（grokking）”时，先前的研究表明，其学习到的嵌入（embeddings）需要使用所有可用频率的“稠密”傅里叶谱。本文证明，这种感知到的稠密性仅仅是在错误的数学基底中分析模型所产生的产物。通过应用乘法特征变换（multiplicative character transform）而非标准的加法离散傅里叶变换（DFT），作者揭示了在 $a \cdot b \bmod 113$ 上训练的 Transformer 具有高度稀疏的嵌入谱。

研究结果表明，Transformer 有效地将乘法转化为离散对数空间中的加法，实现了一种“离散对数时钟（Discrete-Log Clock）”算法。这一发现凸显了机械可解释性研究中的一个核心原则：将分析基底与任务的代数结构相匹配，能够在标准工具只能看到噪声的地方揭示出高度可解释的结构。

---

## 摘要 (Abstract)

When small transformers grok modular multiplication, prior work reports that the learned embedding has a "dense" Fourier spectrum requiring all frequencies. This contrasts with modular addition, where only a sparse set of key frequencies suffices. 

> 当小型 Transformer 对模乘法产生突发性过拟合（grokking）时，先前的研究报告称，其学习到的嵌入具有需要所有频率的“稠密”傅里叶谱。这与模加法形成鲜明对比，在模加法中，仅需一小部分稀疏的关键频率就足够了。

We show this density is an artifact of analyzing in the wrong basis. The natural Fourier transform for multiplication is not the standard additive DFT but the multiplicative character transform, which decomposes functions on the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$ into its irreducible representations. Applying this transform to a grokked transformer trained on $a \cdot b \bmod 113$, we find the embedding spectrum becomes highly sparse (Gini coefficient 0.58 vs. 0.07 in the additive basis) with only 4 key frequencies carrying significant energy. 

> 我们证明，这种稠密性是在错误基底下进行分析所产生的人为产物。乘法的自然傅里叶变换不是标准的加法 DFT，而是乘法特征变换，它将乘法群 $(\mathbb{Z}/p\mathbb{Z})^*$ 上的函数分解为其不可约表示。通过将该变换应用于在 $a \cdot b \bmod 113$ 上训练完成过拟合的 Transformer，我们发现嵌入谱变得高度稀疏（基尼系数为 0.58，而在加法基底下为 0.07），并且只有 4 个关键频率承载了显著的能量。

Furthermore, 96.9% of MLP neurons are cleanly tuned to a single multiplicative frequency, and neuron activation heatmaps reveal 2D-periodic structure when reordered by the discrete logarithm. These results demonstrate the transformer reduces multiplication to addition in discrete-log space, implementing a "Discrete-Log Clock" algorithm analogous to Nanda et al.'s Clock algorithm for addition. The methodology generalizes: matching the analysis basis to the algebraic structure of the task reveals interpretable structure where standard tools see noise.

> 此外，96.9% 的 MLP 神经元被清晰地调谐到单一的乘法频率上，并且当按离散对数重新排序时，神经元激活热图显示出二维周期性结构。这些结果表明，Transformer 将乘法简化为离散对数空间中的加法，实现了一种类似于 Nanda 等人针对加法的时钟算法的“离散对数时钟”算法。这种方法具有通用性：将分析基底与任务的代数结构相匹配，能够在标准工具看到噪声的地方揭示出可解释的结构。

---

## 关联资源 (Associated Resources)

* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
* **Code, Data & Media Tools:** Available via arXivLabs integrations (including [alphaXiv](https://alphaxiv.org/), [CatalyzeX Code Finder](https://www.catalyzex.com), and [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)).

> * **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)
> * **代码、数据与媒体工具：** 可通过 arXivLabs 集成获取（包括 [alphaXiv](https://alphaxiv.org/)、[CatalyzeX Code Finder](https://www.catalyzex.com) 以及 [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)）。