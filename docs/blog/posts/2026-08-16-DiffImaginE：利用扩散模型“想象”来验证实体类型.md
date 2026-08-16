---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 多模态命名实体识别
- 扩散模型
- 条件潜空间扩散
- 实体类型验证
title: DiffImaginE：利用扩散模型“想象”来验证实体类型
---
### 文章背景与核心概要
多模态命名实体识别（MNER）旨在确定文本和视觉联合证据是否支持每个候选文本片段及其对应的实体类型假设。传统的“想象与比较”验证器将每个（片段，类型）对映射到单一的预测视觉特征，这不仅将多样化的视觉表现压缩为了单一原型，而且在缺乏显式概率语义的情况下提供兼容性评分。

为了解决这一痛点，本文推出了 **DiffImaginE**，它将 MNER 类型验证建模为条件潜空间扩散推理。给定片段局部的视觉证据，类型条件去噪器会预测注入其标准化潜空间中的噪声。由此产生的去噪误差为类型条件负对数似然提供了一个与 ELBO 一致的替代指标，从而允许根据不同类型假设解释观测结果的优劣来进行排序。

DiffImaginE 保留了标准的的多模态编码器栈，并用采用 Min-SNR 加权训练的无分类器引导（classifier-free-guided）扩散评分器取代了确定性的验证器。我们直接监督每种类型的扩散分数作为分类逻辑值（logits），学习跨噪声水平的聚合，并利用对偶采样（antithetic sampling）来降低蒙特卡洛比较方差。Twitter-2015 和 Twitter-2017 上的实验表明，在相同的编码器、辅助目标和评估协议下，该方法相较于确定性的 ImaginE 控制组取得了持续的性能提升。

---

# DiffImaginE: Imagine to Verify Entity Types with Diffusion

> # DiffImaginE: Imagine to Verify Entity Types with Diffusion

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/) ![License Icon](./images/345c7ad61f1b.png)

> [![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/) ![License Icon](./images/345c7ad61f1b.png)

## Overview & Metadata
* **arXiv ID:** [arXiv:2608.03025](https://arxiv.org/abs/2608.03025) [cs.AI]
* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **Submission Timeline:** Submitted on August 4, 2026; last revised on August 13, 2026 (v3).
* **Authors:** Feng Zhang, Feiyu Han, Rongxin Yang, Yang Liu, Yancheng Chen, Rui Wang, Yingguang Yang, Tian Xueyun, Chongyang Zhang, Hao Zheng, Xu Kefu, Congjing Ran, Fuhai Chen, and Bin Chong.

> ## Overview & Metadata
> * **arXiv ID:** [arXiv:2608.03025](https://arxiv.org/abs/2608.03025) [cs.AI]
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Submission Timeline:** Submitted on August 4, 2026; last revised on August 13, 2026 (v3).
> * **Authors:** Feng Zhang, Feiyu Han, Rongxin Yang, Yang Liu, Yancheng Chen, Rui Wang, Yingguang Yang, Tian Xueyun, Chongyang Zhang, Hao Zheng, Xu Kefu, Congjing Ran, Fuhai Chen, and Bin Chong.

---

## Abstract

Multimodal named entity recognition (MNER) determines whether each candidate span and entity-type hypothesis is supported by joint textual and visual evidence. Existing imagine-and-compare verifiers map each (span, type) pair to one predicted visual feature, compressing diverse visual realisations into a single prototype and providing a compatibility score without explicit probabilistic semantics. 

We introduce **DiffImaginE**, which formulates MNER type verification as conditional latent diffusion inference. Given span-localised visual evidence, a type-conditioned denoiser predicts noise injected into its standardised latent. The resulting denoising error provides an ELBO-consistent surrogate for type-conditional negative log-likelihood, allowing competing type hypotheses to be ranked by how well they explain the observation. 

DiffImaginE retains a standard multimodal encoder stack and replaces the deterministic verifier with a classifier-free-guided diffusion scorer trained using Min-SNR weighting. We directly supervise per-type diffusion scores as classification logits, learn aggregation across noise levels, and use antithetic sampling to reduce Monte Carlo comparison variance. 

Our analysis shows that classifier-free guidance sharpens the induced type posterior and characterises when antithetic pairing reduces variance at equal denoiser cost. Experiments on Twitter-2015 and Twitter-2017 show consistent gains over a matched deterministic ImaginE control under the same encoder, auxiliary objectives, and evaluation protocol, supported by ablations and paired significance tests.

> ## Abstract
>
> Multimodal named entity recognition (MNER) determines whether each candidate span and entity-type hypothesis is supported by joint textual and visual evidence. Existing imagine-and-compare verifiers map each (span, type) pair to one predicted visual feature, compressing diverse visual realisations into a single prototype and providing a compatibility score without explicit probabilistic semantics. 
>
> We introduce **DiffImaginE**, which formulates MNER type verification as conditional latent diffusion inference. Given span-localised visual evidence, a type-conditioned denoiser predicts noise injected into its standardised latent. The resulting denoising error provides an ELBO-consistent surrogate for type-conditional negative log-likelihood, allowing competing type hypotheses to be ranked by how well they explain the observation. 
>
> DiffImaginE retains a standard multimodal encoder stack and replaces the deterministic verifier with a classifier-free-guided diffusion scorer trained using Min-SNR weighting. We directly supervise per-type diffusion scores as classification logits, learn aggregation across noise levels, and use antithetic sampling to reduce Monte Carlo comparison variance. 
>
> Our analysis shows that classifier-free guidance sharpens the induced type posterior and characterises when antithetic pairing reduces variance at equal denoiser cost. Experiments on Twitter-2015 and Twitter-2017 show consistent gains over a matched deterministic ImaginE control under the same encoder, auxiliary objectives, and evaluation protocol, supported by ablations and paired significance tests.

---

## Access & Resources

* **Full-Text Links:**
  * [View PDF](https://arxiv.org/pdf/2608.03025)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.03025v3)
  * [TeX Source](https://arxiv.org/src/2608.03025)
* **External References & Bibliographic Tools:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.03025)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.03025)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.03025)

> ## Access & Resources
>
> * **Full-Text Links:**
>   * [View PDF](https://arxiv.org/pdf/2608.03025)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.03025v3)
>   * [TeX Source](https://arxiv.org/src/2608.03025)
> * **External References & Bibliographic Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.03025)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.03025)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.03025)