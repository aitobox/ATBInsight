---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-21
hide:
  - navigation
tags:
  - FlashRT-PAI
  - 具身智能
  - 物理 AI
  - VLA
  - 推理加速
title: "FlashRT-PAI：算子快不等于流水线快——具身物理 AI 实时推理引擎突破"
---

# FlashRT-PAI：算子快不等于流水线快——具身物理 AI 实时推理引擎突破

> # FlashRT-PAI: Fast Kernels Are Not Fast Pipelines for Physical AI Inference

> **arXiv ID:** [2610.24349](https://arxiv.org/abs/2610.24349) [cs.AI]  
> **Authors:** Liang Su, David Chen, Jason Li, Kevin Guo, Teresa Lv  
> **Submitted:** October 17, 2026  
> **Links:** [View PDF](https://arxiv.org/pdf/2610.24349) | [GitHub Source Code](https://github.com/flashrt-project/FlashRT) | [Hugging Face Kernel Hub](https://huggingface.co/huggingface)

### 文章背景与核心概要

在具身智能与物理 AI (Physical AI) 的应用前沿，实体机器人需要在毫秒级控制周期内连续感知视觉流并做出精准动作决策，这对单批次 (Single-batch) 实时推理提出了极度严苛的低延迟 (Latency) 要求。然而业界长期陷入一个认知误区：以为把单个底层算子 (Kernel) 优化到极致就能让系统飞速运转；实际上在完整的端到端控制流水线中，成千上万个微小算子的频繁发射调度、算子边界间昂贵的数据搬运，以及连续决策间的大量无用重复计算，才是真正的性能绞杀元凶。为了打破这一“算子快但整体慢”的瓶颈，研究团队推出了 **FLASHRT-PAI** 低延迟推理引擎，首次在模型架构与计算硬件之间展开深度的流水线协同设计。该系统通过深度算子融合与发射重叠彻底抹平发射间隙，借助形式化的“执行契约”让连续动作决策能跨周期复用隐状态，并在 NVIDIA RTX 5090 与边缘车载计算单元 Jetson AGX Thor 上实现了最高达 12.66 倍的推理提速，不仅在 LIBERO-10 基准测试中以 4 位量化超越了官方 16 位浮点精度基线，更已作为核心加速组件被开源机器人框架 LeRobot 官方采纳，为高频灵巧的实体具身控制铺平了工程基石。

---

## 📌 核心概要

> ## 📌 Executive Summary

现代物理 AI 系统——例如**视觉-语言-动作 (Vision-Language-Action, VLA)**、**视频-动作 (Video-Action, VA)** 以及**世界动作模型 (World Action Models, WAMs)**——在单批次实时推理场景中正面临严峻的性能瓶颈。掣肘系统性能的真正根源往往不是孤立算子本身的计算吞吐量，而是系统级的综合开销：数以千计的微细小算子发射开销、跨算子边界的中间数据频繁搬移，以及在连续控制决策之间发生的无谓重复计算。

> Modern physical AI systems—such as **Vision-Language-Action (VLA)**, **Video-Action (VA)**, and **World Action Models (WAMs)**—face a major bottleneck in real-time, single-batch inference. Rather than individual kernel computations, system-level overhead limits performance: thousands of short kernel launches, intermediate data movement across operator boundaries, and redundant recomputations across consecutive decisions. 

通用图编译器在此类场景下往往收效甚微，因为它们大多孤立地对算子调用进行局部优化，无法感知跨决策调用的状态语义，更缺乏对端到端全局流水线结构的统筹视野。

> General-purpose graph compilers fall short because they optimize calls in isolation without visibility into cross-call state semantics or global pipeline structure. 

为了攻克这一难题，作者团队推出了 **FLASHRT-PAI**，这是一个立足于模型-硬件流水线协同设计的低延迟推理引擎。

> To overcome this, the authors introduce **FLASHRT-PAI**, a low-latency inference engine built on model-hardware pipeline co-design. 

---

## 🛠️ FLASHRT-PAI 的核心机制

> ## 🛠️ Core Mechanisms of FLASHRT-PAI

FLASHRT-PAI 依托三大基础机制对整个执行流水线进行深度精简与重构：

> FLASHRT-PAI leverages three foundational mechanisms to streamline execution:

1. **深度算子融合与发射重叠 (Deep Kernel Fusion with Launch Overlap)：** 彻底消除算子间的跨边界数据搬运开销，抹平算子连续发射间的调度空隙；
2. **执行契约 (Execution Contract)：** 将流水线各阶段的有向无环图 (Directed Acyclic Graph, DAG)、状态更新频率以及命名缓冲区进行形式化规范，实现跨决策周期的状态安全复用与按需选择性刷新；
3. **执行状态胶囊 (Execution-State Capsules)：** 针对常驻的持久化流水线状态，提供毫秒级极速快照保存、状态恢复与分支分叉能力。

> 1. **Deep Kernel Fusion with Launch Overlap:** Eliminates inter-operator boundaries and launch gaps.
> 2. **Execution Contract:** Formalizes the pipeline’s stage Directed Acyclic Graph (DAG), update rates, and named buffers to enable cross-decision state reuse and selective refresh.
> 3. **Execution-State Capsules:** Enables fast snapshot, restore, and fork operations for persistent pipeline states.

此外，该系统还支持在不修改 PyTorch 原生模型代码的前提下实现“即插即用”式的极速替换，通过兼顾数值一致性与延迟门控的算子替换机制保障模型无痛平滑迁移。

> Additionally, the system supports drop-in acceleration for unmodified PyTorch models via parity- and latency-gated kernel replacement.

---

## 📊 性能实测与评估

> ## 📊 Performance & Evaluation

研究人员在桌面旗舰硬件 **RTX 5090** 上评测了 **6 种策略模型**，并在车载边缘计算平台 **Jetson AGX Thor** 上评测了 **4 种策略模型**：

> The engine was evaluated across **six policies on the RTX 5090** and **four policies on the Jetson AGX Thor**.

* **在严格对齐的 16 位精度下：** FLASHRT-PAI 相比官方编译执行路径，取得了 **1.3 倍至 3.7 倍的显著加速**；
* **流水线协同设计 + 低精度优化：** 相比官方原生的即时执行 (Eager) 实现，带来了高达 **3.38 倍至 12.66 倍的惊人提速**；
* **LIBERO-10 基准测试精度表现：** 运行 4 位量化的 `pi0.5` 模型时，在 Thor 边缘平台上取得了 **94.04% 的任务成功率**，在 RTX 5090 上取得了 **93.32% 的成功率**，全面超越了官方实测的 FP16 浮点基线得分 (**92.4%**)。

> * **At matched 16-bit precision:** FLASHRT-PAI achieves a **1.3× to 3.7× speedup** over official compiled paths.
> * **Pipeline Co-design + Reduced Precision:** Delivers a **3.38× to 12.66× speedup** over official eager implementations.
> * **Accuracy on LIBERO-10:** A 4-bit `pi0.5` model achieves a **94.04% success rate on Thor** and **93.32% on the RTX 5090**, outperforming the measured official FP16 reference baseline of **92.4%**.

---

## 🌐 开源发布与生态采纳

> ## 🌐 Open Source & Adoption

* **开源代码仓库：** 项目已完全公开发布于 GitHub 与 Hugging Face Kernel Hub；
* **产业生态集成：** 针对 `pi0.5` 的可选优化算子已被知名开源具身机器人框架 **LeRobot** 官方正式合并采纳。

> * **Repository:** Distributed openly via GitHub and the Hugging Face Kernel Hub.
> * **Ecosystem Integration:** The opt-in `pi0.5` kernels have been officially adopted into the **LeRobot framework**.

---
*(注：根据版权规范保留授权图标 / Note: License icon preserved as per requirement: <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">)*
