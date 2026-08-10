---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- 手语识别
- 计算机视觉
- Transformer
- 轻量化模型
- 边缘计算
title: TransSLR：用于手语识别的轻量级 Transformer
---
### 文章背景与核心概要
针对中非手语（CASL）等代表性不足的语言，自动化手语识别（ASR）技术长期面临数据规模受限以及与大规模语料库存在领域鸿沟等严峻挑战。为解决这一难题，研究人员提出了 **TransSLR**——一个完全从头开始训练、基于 64 帧归一化姿态序列的轻量级时间维度 Transformer 编码器。

通过利用几何关键点代替原始 RGB 图像数据，TransSLR 在 CASL-W60 基准测试中实现了最先进（SOTA）的准确率，同时显著降低了资源受限环境下的计算开销。该研究成果不仅大幅提升了少数群体语言的手语识别性能，也为边缘设备的实际部署提供了切实可行的轻量化解决方案。

---

# TransSLR: A Lightweight Transformer for Sign Language Recognition

## Summary

Automated Sign Language Recognition (ASR) for under-represented languages—such as Central African Sign Language (CASL)—faces severe challenges due to limited data scale and domain gaps with large-scale corpora. To address this, researchers propose **TransSLR**, a lightweight Temporal Transformer Encoder trained entirely from scratch on 64-frame normalized pose sequences. By utilizing geometric keypoints instead of raw RGB data, TransSLR achieves state-of-the-art accuracy on the CASL-W60 benchmark while significantly reducing computational overhead for resource-constrained environments.

> Automated Sign Language Recognition (ASR) for under-represented languages—such as Central African Sign Language (CASL)—faces severe challenges due to limited data scale and domain gaps with large-scale corpora. To address this, researchers propose **TransSLR**, a lightweight Temporal Transformer Encoder trained entirely from scratch on 64-frame normalized pose sequences. By utilizing geometric keypoints instead of raw RGB data, TransSLR achieves state-of-the-art accuracy on the CASL-W60 benchmark while significantly reducing computational overhead for resource-constrained environments.

---

## Metadata

* **arXiv ID:** [arXiv:2608.06407](https://arxiv.org/abs/2608.06407) [cs.CV]
* **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`)
* **Authors:** Lucia Yen Wanchi, Samuel Johnny, Victor Tolulope Olufemi, Emmanuel Aaron, Moise Busogi
* **Submission Date:** August 3, 2026
* **Accepted Presentation:** Oral presentation at *Deep Learning Indaba 2026* (hosted on the IJCAI platform)

> * **arXiv ID:** [arXiv:2608.06407](https://arxiv.org/abs/2608.06407) [cs.CV]
> * **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`)
> * **Authors:** Lucia Yen Wanchi, Samuel Johnny, Victor Tolulope Olufemi, Emmanuel Aaron, Moise Busogi
> * **Submission Date:** August 3, 2026
> * **Accepted Presentation:** Oral presentation at *Deep Learning Indaba 2026* (hosted on the IJCAI platform)

---

## Abstract

Automated Sign Language Recognition for under-represented languages remains a largely unsolved problem. Central African Sign Language (CASL) exemplifies this gap: the only available benchmark, **CASL-W60**, has a best reported accuracy of 69.93%, and we show that the common heuristic of fine-tuning high-resource models fails to close it. 

This failure stems from two compounding factors:
1. The limited scale of available CASL data.
2. The significant lexical and visual domain gap between CASL and large-scale corpora such as WLASL, which renders pre-trained representations largely uninformative.

To address this, we propose **TransSLR**, a lightweight Temporal Transformer Encoder trained from scratch on 64-frame normalized pose sequences, with average pooling and a classification head. By operating on geometric keypoint representations rather than raw RGB, TransSLR achieves signer-independent generalization without relying on visual appearance. 

On the CASL-W60 benchmark, TransSLR establishes a new state-of-the-art accuracy of **80.39%**, surpassing the prior best by **+10.46%**. Beyond accuracy, our encoder-only design significantly reduces computational overhead, making deployment feasible in resource-constrained environments.

> Automated Sign Language Recognition for under-represented languages remains a largely unsolved problem. Central African Sign Language (CASL) exemplifies this gap: the only available benchmark, **CASL-W60**, has a best reported accuracy of 69.93%, and we show that the common heuristic of fine-tuning high-resource models fails to close it. 

> This failure stems from two compounding factors:
> 1. The limited scale of available CASL data.
> 2. The significant lexical and visual domain gap between CASL and large-scale corpora such as WLASL, which renders pre-trained representations largely uninformative.

> To address this, we propose **TransSLR**, a lightweight Temporal Transformer Encoder trained from scratch on 64-frame normalized pose sequences, with average pooling and a classification head. By operating on geometric keypoint representations rather than raw RGB, TransSLR achieves signer-independent generalization without relying on visual appearance. 

> On the CASL-W60 benchmark, TransSLR establishes a new state-of-the-art accuracy of **80.39%**, surpassing the prior best by **+10.46%**. Beyond accuracy, our encoder-only design significantly reduces computational overhead, making deployment feasible in resource-constrained environments.

---

## Links and Resources

* **Full Text:** [View PDF](https://arxiv.org/pdf/2608.06407) | [HTML Version (Experimental)](https://arxiv.org/html/2608.06407v1)
* **Conference Paper Link:** [Deep Learning Indaba 2026 Submission](https://chairingtool.com/conferences/dli2026/main-track/submissions/356)
* **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06407) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06407) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06407)

> * **Full Text:** [View PDF](https://arxiv.org/pdf/2608.06407) | [HTML Version (Experimental)](https://arxiv.org/html/2608.06407v1)
> * **Conference Paper Link:** [Deep Learning Indaba 2026 Submission](https://chairingtool.com/conferences/dli2026/main-track/submissions/356)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06407) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06407) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06407)