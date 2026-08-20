---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 系外行星
- 深度学习
- 对比学习
- 光变曲线
- 太阳系外行星搜寻
title: DELOS：用于Kepler光变曲线低信噪比盲搜的对比深度学习方法
---
### 文章背景与核心概要
在天体物理学中，寻找开普勒（Kepler）空间望远镜等搜集的微弱系外行星凌星信号一直是一项核心挑战，尤其是在低信噪比（low-SNR）以及中长周期（如100-150天）的极端环境下，传统的方差拟合最小二乘法（BLS）和凌星最小二乘法（TLS）往往显得力不从心且计算开销巨大。为了解决这一痛点，本文提出了 DELOS（DEtection in phase-folded Light curves with cOntrastive Scoring）深度学习框架。该方法将GPU加速的相位折叠、优化的相位分箱以及定制的一维卷积编码器和对比评分机制相结合，摆脱了对预先检测阈值交叉事件的依赖，能够直接生成评分周期图。

DELOS 利用包含2000万条合成光变曲线的数据集进行训练，在验证集上达到了99.3%的高准确率。控制注入恢复实验表明，在低信噪比环境下，DELOS 的综合准确率-召回率性能比 BLS 提升了 15.5%，比 TLS 提升了 11.25%，同时搜索速度分别提升了约 3-5 倍和 74-80 倍。应用于选定的 Kepler 验证样本时，DELOS 成功恢复了测试周期范围内所有已知的中长周期浅凌星信号。这项研究不仅为低信噪比凌星搜寻提供了高效且敏感的框架，也为未来在 Kepler、K2、TESS、PLATO 以及“地球 2.0”等任务数据中搜寻更长周期的类地行星奠定了实用的方法论基础。

---

# DELOS: Contrastive Deep Learning for Low-SNR Blind Transit Searches in Kepler Photometry

## Summary
> **DELOS** (**DE**tection in phase-folded **L**ight curves with c**O**ntrastive **S**coring) is a novel deep-learning framework designed to perform blind searches for shallow exoplanet transits in Kepler photometry, particularly within the low Signal-to-Noise Ratio (low-SNR) regime. By combining GPU-accelerated phase folding, optimized phase binning, and a custom 1D convolutional encoder with contrastive scoring, DELOS produces score periodograms over trial periods without relying on pre-detected threshold-crossing events. 
> 
> Trained on 20 million synthetic light curves, DELOS achieves high precision, significantly outperforms traditional methods like Box-fitting Least Squares (BLS) and Transit Least Squares (TLS) in low-SNR environments, and accelerates search times by orders of magnitude.

---

## Metadata & Publication Details

> * **arXiv ID:** [arXiv:2605.29428](https://arxiv.org/abs/2605.29428) [astro-ph.EP]
> * **Journal Submission:** Submitted to *Astronomy & Astrophysics Journal* (25 pages, 19 figures, 1 table)
> * **Primary Subject:** Earth and Planetary Astrophysics (`astro-ph.EP`)
> * **Secondary Subjects:** Instrumentation and Methods for Astrophysics (`astro-ph.IM`); Artificial Intelligence (`cs.AI`)
> * **Submission Timeline:**
>   * **v1:** 28 May 2026
>   * **v2:** 1 August 2026
>   * **v3 (Latest):** 19 August 2026
> * **Authors:** 
>   * Qingtian Liu
>   * Jian Ge
>   * XingChen Yan
>   * Kevin Willis
>   * Xinyu Yao
>   * QuanQuan Hu
>   * Jiapeng Zhu

---

## Abstract

我们提出了基于对比评分的相位折叠光变曲线检测方法（DELOS），这是一个深度学习框架，它利用对比评分对 Kepler 光变曲线中的浅凌星进行盲搜索。DELOS 结合了 GPU 加速的相位折叠、优化的相位分箱以及定制的一维卷积编码器，为每个折叠的光变曲线赋予一个类似于凌星的评分，从而在无需依赖预先检测到的阈值交叉事件的情况下，生成针对试验周期的评分周期图。

> We present DEtection in phase-folded Light curves with cOntrastive Scoring (DELOS), a deep-learning framework that uses contrastive scoring to perform blind searches for shallow transits in Kepler photometry. DELOS combines GPU-accelerated phase folding, optimized phase binning, and a custom one-dimensional convolutional encoder to assign a transit-likeness score to each folded light curve, thereby producing a score periodogram over trial periods without relying on pre-detected threshold-crossing events. 

该研究聚焦于轨道周期为 100-150 天的中长周期信号，使用结合了真实凌星模型与类似 Kepler 噪声特性的 2000 万条合成光变曲线对 DELOS 进行了训练，在合成验证集上取得了 99.3% 的验证准确率。在受控的注入恢复实验中，在低信噪比（low-SNR）环境下，与方差拟合最小二乘法（BLS）相比，DELOS 的综合准确率-召回率性能提升了 15.5%，与凌星最小二乘法（TLS）相比提升了 11.25%。同时，与 BLS 和 TLS 相比，其搜索速度分别加快了约 3-5 倍和 74-80 倍。

> Focusing on intermediate-to-long-period signals with orbital periods of 100–150 days, DELOS was trained on 20 million synthetic light curves generated with realistic transit models and Kepler-like noise properties, achieving a validation accuracy of 99.3% on the synthetic validation set. In controlled injection-recovery experiments, DELOS improves the combined precision-recall performance by 15.5% relative to Box-fitting Least Squares (BLS) and 11.25% relative to Transit Least Squares (TLS) in the low Signal-to-Noise Ratios (low-SNR) regime. It also accelerates the search by factors of approximately 3–5 and 74–80 compared with BLS and TLS, respectively. 

将其应用于选定的 Kepler 验证样本时，DELOS 恢复了测试周期范围内所有已知的浅层中长周期凌星信号。这些结果表明，DELOS 为低信噪比凌星搜索提供了一个高效且敏感的框架，并且是未来在 Kepler、K2、TESS、PLATO 和“地球 2.0”数据中搜寻更长周期类地行星的务实一步。因此，本工作旨在进行方法学开发和验证研究，对新识别候选体的详细天体物理学验证留待未来工作完成。

> Applied to a selected Kepler validation sample, DELOS recovered all known shallow intermediate-to-long-period transit signals in the tested period range. These results demonstrate that DELOS provides an efficient and sensitive framework for low-SNR transit searches and represents a practical step toward future searches for longer-period terrestrial planets in Kepler, K2, TESS, PLATO, and Earth 2.0 data. Accordingly, this work is intended as a methodological development and validation study, with the detailed astrophysical validation of newly identified candidates deferred to future work.

---

## Links & Resources

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2605.29428) | [Experimental HTML](https://arxiv.org/html/2605.29428v3) | [TeX Source](https://arxiv.org/src/2605.29428)
> * **External References:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2605.29428) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.29428) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.29428)