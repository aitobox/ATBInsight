---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 计算机视觉
- 跨视角地理定位
- 视频定位
- BMVC 2026
- 跨粒度对齐
title: X$^2$Localizer：用于渐进式跨视角视频地理定位的跨粒度对齐方法
---
### 文章背景与核心概要
跨视角视频地理定位（CVG）旨在通过检索带地理标签的航拍图像来定位地面视角视频。然而，传统方法严重依赖固定长度的输入以及事后求精机制，这限制了其在面对局部或动态观测时的在线定位能力。

为了克服这些局限性，本文提出了渐进式跨视角视频地理定位（PCVG）这一面向实际部署的扩展与评估协议，支持在不同时间预算下的在线定位、前缀式推理、随机起点评估以及带中断的长距离定位。为此，作者推出了 **X$^2$Localizer**——一种新颖的跨粒度对齐框架，该框架利用预算依赖的非对称目标，对全局“前缀-航拍”检索以及“token聚合的帧-航拍图块”匹配进行联合监督。此外，本文还设计了滑动窗口重新定位（SWRL）策略，能够动态刷新候选区域以实现故障恢复和长距离部署，而无需重新处理整个视频序列。实验表明，该方法在保持传统全视频性能的同时，大幅提升了早期定位和单帧粗检索的准确性，缩小了基准评估与真实世界部署之间的差距。

---

# X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization

> # X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization

## Summary

> ## Summary

**X$^2$Localizer** is a novel cross-grained alignment framework designed for **Progressive Cross-view Video Geo-localization (PCVG)**—a deployment-oriented evaluation protocol that addresses the limitations of traditional Cross-view Video Geo-localization (CVG) methods. While conventional approaches rely on fixed-length inputs and post-hoc refinement, X$^2$Localizer supports online-oriented localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. 

> **X$^2$Localizer** is a novel cross-grained alignment framework designed for **Progressive Cross-view Video Geo-localization (PCVG)**—a deployment-oriented evaluation protocol that addresses the limitations of traditional Cross-view Video Geo-localization (CVG) methods. While conventional approaches rely on fixed-length inputs and post-hoc refinement, X$^2$Localizer supports online-oriented localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. 

Key contributions and technical highlights include:
- **Cross-grained Alignment Framework:** Jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching utilizing a budget-dependent asymmetric objective.
- **Sliding-Window Re-Localization (SWRL) Strategy:** Dynamically refreshes candidate regions to enable failure recovery and long-range deployment without requiring full-sequence reprocessing.
- **Superior Empirical Performance:** Preserves conventional full-video performance while drastically improving early localization, single-frame coarse retrieval, and robustness under random-start and long-distance scenarios.

> Key contributions and technical highlights include:
> - **Cross-grained Alignment Framework:** Jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching utilizing a budget-dependent asymmetric objective.
> - **Sliding-Window Re-Localization (SWRL) Strategy:** Dynamically refreshes candidate regions to enable failure recovery and long-range deployment without requiring full-sequence reprocessing.
> - **Superior Empirical Performance:** Preserves conventional full-video performance while drastically improving early localization, single-frame coarse retrieval, and robustness under random-start and long-distance scenarios.

---

> ---

## Paper Metadata

> ## Paper Metadata

- **arXiv ID:** [arXiv:2608.16658](https://arxiv.org/abs/2608.16658) [cs.CV]
- **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`); Robotics (`cs.RO`)
- **Accepted Venue:** The 37th British Machine Vision Conference (**BMVC 2026**)
- **Timeline:** Submitted on August 17, 2026; Last revised on August 27, 2026 (v2).
- **Authors:** 
  - Zichao Zeng
  - Weijia Fan
  - Yufan Chen
  - June Moh Goo
  - Junwei Zheng
  - Ruiping Liu
  - Kunyu Peng
  - Jiaming Zhang
  - Rainer Stiefelhagen
  - Jan Boehm

> - **arXiv ID:** [arXiv:2608.16658](https://arxiv.org/abs/2608.16658) [cs.CV]
> - **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`); Robotics (`cs.RO`)
> - **Accepted Venue:** The 37th British Machine Vision Conference (**BMVC 2026**)
> - **Timeline:** Submitted on August 17, 2026; Last revised on August 27, 2026 (v2).
> - **Authors:** 
>   - Zichao Zeng
>   - Weijia Fan
>   - Yufan Chen
>   - June Moh Goo
>   - Junwei Zheng
>   - Ruiping Liu
>   - Kunyu Peng
>   - Jiaming Zhang
>   - Rainer Stiefelhagen
>   - Jan Boehm

---

> ---

## Abstract

> ## Abstract

Cross-view Video Geo-localization (CVG) aims to localize ground-view videos by retrieving their corresponding geo-tagged aerial images. However, CVG approaches rely on fixed-length inputs and post-hoc refinement, hindering online-oriented localization under partial or dynamic observations. 

> Cross-view Video Geo-localization (CVG) aims to localize ground-view videos by retrieving their corresponding geo-tagged aerial images. However, CVG approaches rely on fixed-length inputs and post-hoc refinement, hindering online-oriented localization under partial or dynamic observations. 

In this work, we formulate Progressive Cross-view Video Geo-localization (PCVG) as a deployment-oriented extension and evaluation protocol of CVG, enabling localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. To explore PCVG, we introduce **X$^2$Localizer**, a cross-grained alignment framework that jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching with a budget-dependent asymmetric objective. 

> In this work, we formulate Progressive Cross-view Video Geo-localization (PCVG) as a deployment-oriented extension and evaluation protocol of CVG, enabling localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. To explore PCVG, we introduce **X$^2$Localizer**, a cross-grained alignment framework that jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching with a budget-dependent asymmetric objective. 

Furthermore, we introduce a **Sliding-Window Re-Localization (SWRL)** strategy that dynamically refreshes candidate regions for failure recovery and long-range deployment without full-sequence reprocessing. Extensive experiments show that X$^2$Localizer preserves conventional full-video performance, with marginal gains of +0.1 Recall@1 and +0.3 Recall@10, while substantially improving early localization. In the challenging single-frame setting, X$^2$Localizer improves coarse retrieval by +4.7 Recall@1 and +11.5 Recall@10 over the previous state-of-the-art method. With SWRL, our approach further enables robust progressive localization under random-start and long-distance scenarios, narrowing the gap between benchmark evaluation and real-world deployment.

> Furthermore, we introduce a **Sliding-Window Re-Localization (SWRL)** strategy that dynamically refreshes candidate regions for failure recovery and long-range deployment without full-sequence reprocessing. Extensive experiments show that X$^2$Localizer preserves conventional full-video performance, with marginal gains of +0.1 Recall@1 and +0.3 Recall@10, while substantially improving early localization. In the challenging single-frame setting, X$^2$Localizer improves coarse retrieval by +4.7 Recall@1 and +11.5 Recall@10 over the previous state-of-the-art method. With SWRL, our approach further enables robust progressive localization under random-start and long-distance scenarios, narrowing the gap between benchmark evaluation and real-world deployment.

---

> ---

## Additional Resources & Full-Text Links

> ## Additional Resources & Full-Text Links

- **PDF Download:** [View PDF](https://arxiv.org/pdf/2608.16658)
- **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.16658v2)
- **Source Code / TeX:** [TeX Source](https://arxiv.org/src/2608.16658)
- **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)

> - **PDF Download:** [View PDF](https://arxiv.org/pdf/2608.16658)
> - **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.16658v2)
> - **Source Code / TeX:** [TeX Source](https://arxiv.org/src/2608.16658)
> - **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)