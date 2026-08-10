---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- 自动驾驶
- VLA模型
- 模型蒸馏
- 扩散模型
- 自回归
title: WAM-Diff2：用于高效率自动驾驶VLA的分层自回归到扩散蒸馏
---
### 文章背景与核心概要
视觉-语言-动作（VLA）模型近年来在端到端自动驾驶领域备受关注，但传统自回归（AR）模型由于串行解码带来的高计算延迟和暴露偏差（exposure bias），严重制约了其实际部署效率。与此同时，专门的扩散策略虽能实现低延迟的并行执行，但从头训练往往导致多任务通用智能的缺失。

为了解决这一行业难题，本文介绍了 WAM-Diff2 框架。它通过创新的三阶段分层蒸馏策略（包括逐块自适应、逐块蒸馏以及模型级跨尺度蒸馏），成功弥合了因果自回归通用模型与并行扩散策略之间的鸿沟。该方法不仅完美保留了预训练模型丰富多任务认知智能，还将解码速度提升了 2.8 倍，若结合 FlashInfer 和 CUDA Graphs 等系统级优化，加速比更可高达 15.1 倍，为高性能实时自动驾驶开辟了新途径。

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2608.01035](https://arxiv.org/abs/2608.01035) [cs.RO]
* **研究领域:** 机器人学 (`cs.RO`), 人工智能 (`cs.AI`), 计算机视觉与模式识别 (`cs.CV`)
* **作者:** Zhihao Zhu, Hanlin Shang, Mingwang Xu, Feipeng Cai, Zhuolin He, Yaoyi Li, Jianhua Han, Hang Xu, Siyu Zhu
* **提交日期:** 2026年8月2日（修订版：2026年8月7日）
* **相关链接:** [查看 PDF](https://arxiv.org/pdf/2608.01035) | [HTML 版本](https://arxiv.org/html/2608.01035v2)

---

## 摘要 (Abstract)

视觉-语言-动作（VLA）模型已成为端到端自动驾驶的重要范式；然而，其高效部署受到串行自回归解码所带来的高计算延迟和暴露偏差的严重限制。

> Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however, their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential autoregressive decoding. 

相反，虽然专门的扩散策略能够实现低延迟的并行执行，但从头开始训练它们通常会产生狭隘的单任务架构，缺乏全局的视觉-语言推理能力。成功将预训练的自回归通用模型转化为并行扩散模型，本可以结合多任务认知智能与执行效率，但由于注意力模式（因果注意力与双向注意力）的不匹配以及优化目标的差异，这种转变带来了巨大的架构挑战。

> Conversely, while specialized diffusion policies enable low-latency, parallel execution, training them from scratch typically yields narrow, single-task architectures that lack holistic visual-linguistic reasoning. Successfully transforming pre-trained autoregressive generalists into parallel diffusion models could combine multi-task cognitive intelligence with execution efficiency, yet this transition presents a formidable architectural challenge due to mismatched attention patterns (causal versus bidirectional) and divergent optimization objectives. 

为了弥合这一鸿沟，作者推出了 **WAM-Diff2**，这是一个由三阶段分层蒸馏策略驱动的多任务离散扩散 VLA 框架：
1. **逐块自适应（Block-wise Adaptation）**
2. **逐块蒸馏（Block-wise Distillation）**
3. **模型级跨尺度蒸馏（Model-wise Cross-Scale Distillation）**

> To bridge this divide, the authors introduce **WAM-Diff2**, a multi-task discrete diffusion VLA framework powered by a three-stage hierarchical distillation strategy:
> 1. **Block-wise Adaptation**
> 2. **Block-wise Distillation**
> 3. **Model-wise Cross-Scale Distillation**

通过这些机制，WAM-Diff2 在加速推理的同时保留了基础模型的底层语义基础。在驾驶理解、感知和规划基准上的广泛评估表明，WAM-Diff2 有效缓解了暴露偏差，在大幅降低延迟的同时实现了与自回归基线相媲美的性能。

> Through these mechanisms, WAM-Diff2 preserves the underlying semantic foundations of the base model while accelerating inference. Extensive evaluations across driving understanding, perception, and planning benchmarks demonstrate that WAM-Diff2 effectively mitigates exposure bias and achieves performance parity with autoregressive baselines while drastically cutting down latency.