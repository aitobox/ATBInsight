---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 视觉-语言-动作模型
- 机器人操作
- 空间基础
- 具身智能
title: Pointing-VLA：面向视觉-语言-动作操作的类型化空间基础接口
---
### 文章背景与核心概要
视觉-语言-动作（VLA）模型在连接多模态推理与机器人执行时，往往依赖于较为脆弱的接口，例如自回归文本坐标或不透明的动作 token。为了解决这一痛点，Pointing-VLA 基于 *Embodied-R1* 推出了一种类型化隐藏状态空间读出机制（typed hidden-state spatial readout）。

模型摒弃了将几何结构序列化为文本的做法，转而利用特定几何结构的预测头直接预测：归一化点、物体功能基础（OFG）热力图以及视觉轨迹。通过建立显式的执行契约（将 `PICK` 分配给条件化的 OFG，将 `PLACE` 分配给 Pointing），Pointing-VLA 提供了与阶段相契合的空间目标，从而显著提升了操作性能、运行速度以及真实机器人的自主性。

---

## 📌 Summary
Vision-Language-Action (VLA) models often rely on fragile interfaces—such as autoregressive text coordinates or opaque action tokens—to bridge multimodal reasoning and robot execution. To address this, **Pointing-VLA** introduces a typed hidden-state spatial readout built upon *Embodied-R1*. 

Instead of serializing geometry into text, the model uses geometry-specific heads to predict:
* Normalized points
* Object-functional grounding (OFG) heatmaps
* Visual trajectories

By establishing an explicit execution contract (assigning `PICK` to source-conditioned OFG and `PLACE` to Pointing), Pointing-VLA delivers stage-aligned spatial targets that significantly enhance manipulation performance, speed, and real-robot autonomy.

> 视觉-语言-动作（VLA）模型通常通过自回归文本坐标或不透明的动作 token 来暴露空间基础，这在多模态推理和机器人执行之间造成了脆弱的接口。
> 
> 我们提出了 **Pointing-VLA**，这是一种构建在 Embodied-R1 之上的类型化隐藏状态空间读出机制。特定几何结构的预测头能够预测归一化点、物体功能基础（OFG）热力图和视觉轨迹，而无需将几何结构序列化为文本。对于评估过的 Bridge/WidowX 以及物理抓取放置部署，显式的执行契约将 `PICK` 分配给源条件化的 OFG，将 `PLACE` 分配给 Pointing，从而提供直接且与阶段对齐的空间目标。

---

## 📋 Abstract
Vision-language-action (VLA) models often expose spatial grounding through autoregressive text coordinates or opaque action tokens, creating brittle interfaces between multimodal reasoning and robot execution. 

We present **Pointing-VLA**, a typed hidden-state spatial readout built on Embodied-R1. Geometry-specific heads predict normalized points, object-functional grounding (OFG) heatmaps, and visual trajectories without serializing geometry as text. For the evaluated Bridge/WidowX and physical pick-place deployments, an explicit execution contract assigns `PICK` to source-conditioned OFG and `PLACE` to Pointing, providing direct stage-aligned spatial targets. 

Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging **72.9%** across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution. Pointing and OFG show complementary strengths across native and cross-dataset evaluations. The OFG/contact readout transfers to NORA-1.5, preserving or improving success while reducing recorded controller time by more than **20×**; typed heads are also **6.68–6.90×** faster than Embodied-R1 text decoding on a shared external suite. When integrated as spatial guidance for a $\pi_{0.5}$ action policy, Pointing-VLA raises autonomous real-robot success from **52.7% to 80.7%** across three visual contexts. These results establish typed spatial readouts as an efficient, inspectable interface between embodied reasoning and robot execution.

> Pointing-VLA 在 Bridge/WidowX 上实现了 SOTA（最先进的）性能，在启用碰撞检测的 CuRobo 执行下，在评估的四个任务集上平均成功率达到 **72.9%**（无需进行 Bridge 专用的微调）。在原生和跨数据集评估中，Pointing 和 OFG 展现出了互补的优势。OFG/接触读出模块可迁移至 NORA-1.5，在保持或提升成功率的同时，将记录的控制器时间缩短了 **20倍** 以上；在共享的外部测试套件上，类型化预测头的速度也比 Embodied-R1 文本解码快 **6.68–6.90倍**。当作为 $\pi_{0.5}$ 动作策略的空间引导集成时，Pointing-VLA 将真实机器人跨三个视觉上下文的自主操作成功率从 **52.7% 提升至 80.7%**。这些结果确立了类型化空间读出机制作为具身推理与机器人执行之间高效、可审查接口的地位。

---

## 🔗 Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.23138) | [HTML (Experimental)](https://arxiv.org/html/2608.23138v1) | [TeX Source](https://arxiv.org/src/2608.23138)
* **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23138) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23138) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23138)

> * **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.23138) | [HTML（实验性）](https://arxiv.org/html/2608.23138v1) | [TeX 源码](https://arxiv.org/src/2608.23138)
> * **引用与指标：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23138) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23138) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23138)