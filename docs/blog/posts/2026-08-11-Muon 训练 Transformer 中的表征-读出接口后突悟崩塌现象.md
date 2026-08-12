---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- Transformer
- Muon优化器
- 突悟现象
- 深度学习
- 动力学分析
title: Muon 训练 Transformer 中的表征-读出接口后突悟崩塌现象
---
### 文章背景与核心概要
本文研究了在使用 Muon 优化器训练的 Transformer 模型中出现的一种奇特现象：模型能够迅速“突悟”（grok，即在训练集拟合后发生泛化），但随后又会失去其泛化能力。通过广泛的实证分析，作者将这种不稳定的根本原因追溯至**表征-读出接口（representation-readout interface）**。在该接口处，不同的优化器动力学（Muon 与 AdamW）以及步长弹性差异，导致尽管训练集成功收敛，模型依然发生了灾难性的性能退化。

这项研究深入剖析了混合优化器策略（Muon 处理隐藏矩阵，AdamW 管理嵌入层和输出头）在模运算任务中的表现，并通过干预实验和傅里叶分析，揭示了突悟现象背后底层的电路机制与优化动态。

---

## 摘要与核心发现 (Abstract & Key Findings)

在标准的训练拆分下，Muon 处理隐藏矩阵，而 AdamW 管理嵌入层和输出头。尽管 Muon 比标准方法快得多地实现了模加法的突悟，但其解法从根本上是不稳定的：

> Under the standard training split, Muon handles hidden matrices while AdamW manages the embeddings and output head. Although Muon groks modular addition much faster than standard approaches, its solutions are fundamentally unstable:

* **普遍的不稳定性：** 在针对 $(a+b) \bmod 113$ 测试的所有九种配置中，模型都经历了突悟随后又失去了泛化能力。基线 AdamW 在五个随机种子中有四个低于阈值（达到了 27.59%）。这种不稳定性在改变模数、网络宽度、训练数据比例、减法任务以及网络深度时依然保持稳健。
* **接口失效：** 这种失效精确地表现在表征-读出接口处。在解决训练集后（此时梯度降至 $10^{-6}$），优化器的反应截然不同：
  * **步长弹性（Step-size elasticity）：** Muon 为 $-0.03$，而 AdamW 为 $+1.5$。
  * **参数移动速度：** Muon 组的每个参数移动速度是 AdamW 组的 **8.0 倍**。
* **干预结果：** 从位相同的状态开始，冻结其中任何一组都可以完全防止失效。冻结嵌入层和读出层可以在五个成对种子的 451,400 个训练步中消除突悟后的退化（未冻结组记录了 137–321 次低于阈值的评估，而冻结组为零）。
* **傅里叶滤波：** 使用傅里叶分析将电路失效与掩蔽（masking）分离，结果表明任务对齐的族群可以独立达到 100% 的准确率。重新缩放该组件可恢复 99.9% 的性能，这证明了突悟本质上是一个向上解析（resolving upward）的状态。

> * **Pervasive Instability:** Across all nine configurations tested on $(a+b) \bmod 113$, models grok and subsequently lose generalization. The baseline AdamW reference falls below threshold in four out of five seeds (reaching 27.59%). This instability remains robust across alterations in moduli, widths, training fractions, subtraction tasks, and network depth.
> * **The Interface Failure:** The failure manifests precisely at the representation-readout interface. After solving the training set (where gradients fall to $10^{-6}$), the optimizers respond differently:
>   * **Step-size elasticity:** $-0.03$ for Muon vs. $+1.5$ for AdamW.
>   * **Parameter movement:** The Muon group moves **8.0 times faster** per parameter.
> * **Intervention Results:** Freezing either group from bit-identical states prevents failure entirely. Freezing embeddings and readout eliminates post-grokking degradation over 451,400 steps across five paired seeds (unfrozen arms recorded 137–321 sub-threshold evaluations, while frozen arms recorded zero).
> * **Fourier Filtering:** Using Fourier analysis to separate circuit failure from masking reveals that task-aligned families can independently achieve 100% accuracy. Rescaling this component restores 99.9% performance, demonstrating that grokking is fundamentally a condition of resolving upward.

---

## 元数据与参考信息 (Metadata & Reference Information)

* **arXiv ID:** [arXiv:2608.07436](https://arxiv.org/abs/2608.07436) [cs.AI]
* **发布日期:** 2026年8月7日
* **作者:** Ali Janati, Kaoutar El Maghraoui, Andrei Kanavalau, Anass Belfatmi
* **主要主题:** 人工智能 (`cs.AI`), 机器学习 (`cs.LG`)
* **代码仓库:** [GitHub - Na00s/muon-grokking](https://github.com/Na00s/muon-grokking)
* **许可证:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) *(见下方许可证图标)*  
  ![License Icon](./images/345c7ad61f1b.png)

> * **arXiv ID:** [arXiv:2608.07436](https://arxiv.org/abs/2608.07436) [cs.AI]
> * **Published Date:** August 7, 2026
> * **Authors:** Ali Janati, Kaoutar El Maghraoui, Andrei Kanavalau, Anass Belfatmi
> * **Primary Subject:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
> * **Code Repository:** [GitHub - Na00s/muon-grokking](https://github.com/Na00s/muon-grokking)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(See license icon below)*  
>   ![License Icon](./images/345c7ad61f1b.png)