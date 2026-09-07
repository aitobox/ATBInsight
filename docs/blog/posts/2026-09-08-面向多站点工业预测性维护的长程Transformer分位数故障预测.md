---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 预测性维护
- 工业AI
- Transformer
- 分位数回归
- 时间序列
title: 面向多站点工业预测性维护的长程Transformer分位数故障预测
---
### 文章背景与核心概要
在工业4.0和智能制造的背景下，预测性维护（Predictive Maintenance）对于降低设备停机时间和运营成本至关重要。然而，传统的预测模型通常聚焦于短期内（如数小时内）的故障预警，而长程预测性维护则要求模型能够在几天甚至几周的宽广规划窗口内，准确区分缓慢的设备退化与正常的运营工况波动。这对于跨站点、多设备的复杂工业环境构成了严峻的技术挑战。

本文介绍了一种名为 **TQRNN30d** 的创新框架，专为解决多站点工业环境中的长程故障预测而设计。该方法巧妙地结合了两阶段分位数回归神经网络（QRNN）特征提取器与多流时间融合分类器，将81通道的机器行为数据映射为高维分位数状态表示，并通过门控残差处理、因果循环编码以及元数据条件交叉模态注意力机制进行深度特征融合。在涵盖9个制造工厂、共72台机器的独立数据集上的评估表明，TQRNN30d在7天、14天和30天的固定阈值测试中全面超越了18个基准模型，尤其在30天长程预测中取得了79.97%的F1分数和0.820的ROC-AUC，为长程工业预测性维护树立了新的性能标杆。

---

# 长程Transformer分位数故障预测用于多站点工业预测性维护 (Long Horizon Transformer Quantile Fault Prediction for Multi Site Industrial Predictive Maintenance)

**作者:** David J. Poland, Daniele Ravi, Na Helian  
**主要学科:** 人工智能 (`cs.AI`)  
**arXiv ID:** [arXiv:2609.04840 [cs.AI]](https://arxiv.org/abs/2609.04840)  
**提交时间:** 2026年9月4日  

---

## 执行摘要 (Executive Summary)

长程预测性维护要求模型能够在以天（而非小时）为单位的规划窗口内，将缓慢演变的设备退化与正常的运行工况波动区分开来。本文推出了 **TQRNN30d** 框架，该框架利用显式的条件分位数表示和多流时间融合来实现稳健的长程故障预测。

在跨越9个制造工厂中72台机器的机台独立（machine-disjoint）数据集上进行的评估表明，TQRNN30d在固定的7天、14天和30天阈值下超越了18个基准模型——在30天预测视界下实现了 **79.97%** 的F1分数和 **0.820** 的ROC-AUC。

> Long-horizon predictive maintenance requires distinguishing slow degradation from normal operational variation over extended planning windows (days rather than hours). This paper introduces **TQRNN30d**, a framework utilizing explicit conditional-quantile representations and multi-stream temporal fusion for robust long-range fault prediction. 
> 
> Evaluated across a machine-disjoint dataset spanning 72 machines in nine manufacturing facilities, TQRNN30d outperforms 18 baseline models across fixed 7-, 14-, and 30-day thresholds—achieving an F1 score of **79.97%** and an ROC-AUC of **0.820** at the 30-day horizon.

---

## 摘要 (Abstract)

长程预测性维护要求模型在以天而非小时计的规划窗口内，区分缓慢演变的退化与正常运行工况的波动。本文评估了显式条件分位数表示是否能为该问题提供信息丰富的分类器接口。

所提出的 **TQRNN30d** 框架将双阶段分位数回归神经网络（QRNN）特征提取器与多流时间融合分类器结合起来。
* 81通道机器行为的每个小时级词元（word）都被映射为324维的分位数状态表示。
* 720个有序的小时级词元组成了提供给长程模型的30天“文档”。

该分类器通过门控残差处理、因果循环编码以及元数据条件交叉模态注意力机制，将分位数状态与动态协变量、通道级静态元数据以及168小时的潜在历史流进行融合。在最长预测视界下，衍生自持续的一步超前预测误差分歧的有界不稳定性感知信号提供了辅助记忆调制。

> Long-horizon predictive maintenance requires models to distinguish slowly evolving degradation from normal operating-regime variation over planning windows measured in days rather than hours. This paper evaluates whether an explicit conditional-quantile representation provides an informative classifier interface for this problem. 
> 
> The proposed **TQRNN30d** framework combines a dual-stage quantile regression neural network (QRNN) feature extractor with a multi-stream temporal fusion classifier. 
> * Each hourly word of 81-channel machine behavior is mapped to a 324-dimensional quantile-state representation.
> * 720 ordered hourly words form the 30-day document supplied to the long-horizon model.
> 
> The classifier fuses quantile states with dynamic covariates, channel-level static metadata, and a 168-hour latent-history stream using gated residual processing, causal recurrent encoding, and metadata-conditioned cross-modal attention. A bounded instability-aware signal derived from sustained one-word-ahead prediction-error divergence provides auxiliary memory modulation at the longest horizon.

---

## 评估与结果 (Evaluation and Results)

* **数据集分配:** 在9个制造工厂的72台机器中，采用按机器划分的 43/14/15 训练/验证/测试集划分方案。
* **30天性能指标:**
  * **F1 分数:** 79.97%
  * **召回率 (Recall):** 80.18%
  * **精确率 (Precision):** 81.82%
  * **准确率 (Accuracy):** 82.39%
  * **ROC-AUC:** 0.820
* **对比性能:** 在7天、14天和30天的固定阈值比较中，该模型领先于所有18个被评估的基准模型，并在14天大关处展示出最大的相对F1优势。

*注：结果验证了其在观察到的同质九工厂车队内留出机器（held-out machines）上的性能，但向未见站点、跨设备类型或不同工业领域的泛化能力仍有待确立。*

> * **Dataset Allocation:** Machine-disjoint 43/14/15 train/validation/test split across 72 machines in 9 manufacturing facilities.
> * **30-Day Performance Metrics:**
>   * **F1 Score:** 79.97%
>   * **Recall:** 80.18%
>   * **Precision:** 81.82%
>   * **Accuracy:** 82.39%
>   * **ROC-AUC:** 0.820
> * **Comparative Performance:** Leads all 18 evaluated baselines at fixed-threshold comparisons for 7, 14, and 30 days, displaying the largest relative F1 advantage at the 14-day mark.
> 
> *Note: Results validate performance on held-out machines within the observed homogeneous nine-facility fleet, but generalisation to unseen sites, cross-equipment types, or different industrial sectors remains to be established.*

---

## 文章访问与资源 (Article Access & Resources)

* **全文选项:** [查看 PDF](https://arxiv.org/pdf/2609.04840) | [HTML 版本](https://arxiv.org/html/2609.04840v1) | [TeX 源码](https://arxiv.org/src/2609.04840)
* **数字对象唯一标识符 (DOI):** [10.48550/arXiv.2609.04840](https://doi.org/10.48550/arXiv.2609.04840)
* **外部文献计量工具:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.04840)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.04840)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.04840)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2609.04840) | [HTML Version](https://arxiv.org/html/2609.04840v1) | [TeX Source](https://arxiv.org/src/2609.04840)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.04840](https://doi.org/10.48550/arXiv.2609.04840)
> * **External Bibliographic Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.04840)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.04840)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.04840)