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
title: X$^2$Localizer：用于渐进式跨视角视频地理定位的跨粒度对齐框架
---
### 文章背景与核心概要
传统的跨视角视频地理定位（CVG）方法通常依赖于固定长度的输入以及事后求精机制，这严重限制了其在局部或动态观测场景下的在线定位能力。为了弥合学术基准测试与真实世界部署之间的鸿沟，本文提出了渐进式跨视角视频地理定位（PCVG）这一面向部署的扩展评估协议，并推出了名为 **X$^2$Localizer** 的新型跨粒度对齐框架。

X$^2$Localizer 通过结合预算相关的非对称目标函数，实现了对全局前缀-航拍图像检索以及标记聚合（token-aggregated）帧-航拍图块匹配的联合监督。此外，该研究还引入了一种滑动窗口重新定位（SWRL）策略，能够在无需重新处理完整序列的情况下动态刷新候选区域，从而实现故障恢复和长距离部署。实验表明，该方法不仅保留了传统全视频的性能优势，还在早期定位、单帧粗检索以及随机起点和长距离等复杂场景下展现出了卓越的鲁棒性。

---

# X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization

## Summary

**X$^2$Localizer** is a novel cross-grained alignment framework designed for **Progressive Cross-view Video Geo-localization (PCVG)**—a deployment-oriented evaluation protocol that addresses the limitations of traditional Cross-view Video Geo-localization (CVG) methods. While conventional approaches rely on fixed-length inputs and post-hoc refinement, X$^2$Localizer supports online-oriented localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. 

Key contributions and technical highlights include:
- **Cross-grained Alignment Framework:** Jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching utilizing a budget-dependent asymmetric objective.
- **Sliding-Window Re-Localization (SWRL) Strategy:** Dynamically refreshes candidate regions to enable failure recovery and long-range deployment without requiring full-sequence reprocessing.
- **Superior Empirical Performance:** Preserves conventional full-video performance while drastically improving early localization, single-frame coarse retrieval, and robustness under random-start and long-distance scenarios.

> **X$^2$Localizer** 是一个新颖的跨粒度对齐框架，专为**渐进式跨视角视频地理定位（PCVG）**设计——这是一个面向部署的评估协议，旨在解决传统跨视角视频地理定位（CVG）方法的局限性。传统方法依赖于固定长度的输入和事后求精（post-hoc refinement），而 X$^2$Localizer 则支持在不同时间预算、基于前缀的推理、随机起点评估以及带中断的长距离定位下进行面向在线的定位。
> 
> 主要贡献与技术亮点包括：
> - **跨粒度对齐框架：** 利用预算相关的非对称目标函数，对全局前缀-航拍检索以及标记聚合的帧-航拍图块匹配进行联合监督。
> - **滑动窗口重新定位（SWRL）策略：** 动态刷新候选区域，实现故障恢复和长距离部署，而无需重新处理完整序列。
> - **卓越的实验性能：** 在保持传统全视频性能的同时，大幅提升了早期定位、单帧粗检索能力，以及在随机起点和长距离场景下的鲁棒性。

---

## Paper Metadata

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
> - **研究领域：** 计算机视觉与模式识别 (`cs.CV`)；人工智能 (`cs.AI`)；机器人学 (`cs.RO`)
> - **录用会议：** 第37届英国机器视觉会议（**BMVC 2026**）
> - **时间线：** 2026年8月17日提交；2026年8月27日最后修订（v2版本）。
> - **作者：** 
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

## Abstract

Cross-view Video Geo-localization (CVG) aims to localize ground-view videos by retrieving their corresponding geo-tagged aerial images. However, CVG approaches rely on fixed-length inputs and post-hoc refinement, hindering online-oriented localization under partial or dynamic observations. 

In this work, we formulate Progressive Cross-view Video Geo-localization (PCVG) as a deployment-oriented extension and evaluation protocol of CVG, enabling localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. To explore PCVG, we introduce **X$^2$Localizer**, a cross-grained alignment framework that jointly supervises global prefix-to-aerial retrieval and token-aggregated frame–aerial-tile matching with a budget-dependent asymmetric objective. 

Furthermore, we introduce a **Sliding-Window Re-Localization (SWRL)** strategy that dynamically refreshes candidate regions for failure recovery and long-range deployment without full-sequence reprocessing. Extensive experiments show that X$^2$Localizer preserves conventional full-video performance, with marginal gains of +0.1 Recall@1 and +0.3 Recall@10, while substantially improving early localization. In the challenging single-frame setting, X$^2$Localizer improves coarse retrieval by +4.7 Recall@1 and +11.5 Recall@10 over the previous state-of-the-art method. With SWRL, our approach further enables robust progressive localization under random-start and long-distance scenarios, narrowing the gap between benchmark evaluation and real-world deployment.

> 跨视角视频地理定位（CVG）旨在通过检索与其对应的带地理标签的航拍图像来定位地面视角视频。然而，现有的 CVG 方法依赖于固定长度的输入和事后求精，阻碍了其在部分或动态观测下的在线定位。
> 
> 在这项工作中，我们将渐进式跨视角视频地理定位（PCVG）构想为 CVG 的面向部署的扩展与评估协议，使其能够在不同的时间预算、基于前缀的推理、随机起点评估以及带中断的长距离定位下进行定位。为了探索 PCVG，我们推出了 **X$^2$Localizer**——一个跨粒度对齐框架，它通过预算相关的非对称目标函数，联合监督全局前缀-航拍检索与标记聚合的帧-航拍图块匹配。
> 
> 此外，我们引入了一种**滑动窗口重新定位（SWRL）策略**，该策略能够动态刷新候选区域以实现故障恢复和长距离部署，而无需对完整序列进行重新处理。大量实验表明，X$^2$Localizer 在保持传统全视频性能的同时（Recall@1 提升 +0.1，Recall@10 提升 +0.3），大幅提升了早期定位能力。在极具挑战性的单帧设置下，相较于先前最先进的方法，X$^2$Localizer 将粗检索能力分别提升了 +4.7 Recall@1 和 +11.5 Recall@10。借助 SWRL 策略，我们的方法进一步在随机起点和长距离场景下实现了鲁棒的渐进式定位，缩小了基准评估与真实世界部署之间的差距。

---

## Additional Resources & Full-Text Links

- **PDF Download:** [View PDF](https://arxiv.org/pdf/2608.16658)
- **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.16658v2)
- **Source Code / TeX:** [TeX Source](https://arxiv.org/src/2608.16658)
- **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)

> - **PDF 下载：** [查看 PDF](https://arxiv.org/pdf/2608.16658)
> - **HTML 版本：** [arXiv HTML（实验性）](https://arxiv.org/html/2608.16658v2)
> - **源代码 / TeX：** [TeX 源码](https://arxiv.org/src/2608.16658)
> - **许可协议：** [知识共享 署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)