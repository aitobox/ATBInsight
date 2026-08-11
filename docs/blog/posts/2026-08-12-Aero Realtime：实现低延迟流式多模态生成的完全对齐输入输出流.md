---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 多模态模型
- 实时生成
- 低延迟
- 流式处理
- AeroRealtime
title: Aero Realtime：实现低延迟流式多模态生成的完全对齐输入输出流
---
### 文章背景与核心概要

现有的流式多模态模型大多受限于“先预填充（prefill）后解码（decode）”的轮次模式，导致模型无法在生成过程中自然地处理新的输入，即缺乏双工（duplex）能力。为了解决这一问题，研究人员提出了 Aero Realtime，这是一个 4B 参数规模的流式多模态模型，旨在实现真正的实时交互。

Aero Realtime 的核心创新在于引入了共享时间网格（shared temporal grid），将视频、音频和文本输出对齐到约 80 毫秒的时间槽中。这种设计使得输入和输出能够同步推进，通过单一的自回归目标函数同时学习“何时响应”和“生成什么内容”。该模型在 NVIDIA A6000 GPU 集群上表现优异，中位处理延迟仅为 84 毫秒，证明了完全对齐的输入输出建模在实现主动式、硬件高效的多模态交互方面的可行性。

---

## Aero Realtime：实现低延迟流式多模态生成的完全对齐输入输出流

### 执行摘要

> **Aero Realtime** is a novel 4B streaming multimodal model featuring a duplex architecture designed for low-latency, real-time generation. Unlike traditional streaming models that rely on rigid turn-based prefill-then-decode patterns or fragmented polling mechanisms, Aero Realtime aligns video, audio, and textual outputs onto a shared temporal grid. This allows inputs and outputs to advance synchronously, enabling a single autoregressive objective to handle response timing and content generation simultaneously. Operating on four NVIDIA A6000 workstation GPUs, the model achieves a median processing lag of 84 ms and a P95 lag of 173 ms over continuous video streams, proving the viability of fully aligned input-output modeling for proactive, hardware-efficient multimodal interactions.

**Aero Realtime** 是一款新型 4B 参数流式多模态模型，采用双工架构设计，专为低延迟实时生成而生。与依赖僵化的“先预填充后解码”模式或碎片化轮询机制的传统流式模型不同，Aero Realtime 将视频、音频和文本输出对齐到一个共享的时间网格上。这使得输入和输出能够同步推进，从而允许单一的自回归目标函数同时处理响应时机和内容生成。该模型在四块 NVIDIA A6000 工作站 GPU 上运行，在连续视频流中实现了 84 毫秒的中位处理延迟和 173 毫秒的 P95 延迟，证明了完全对齐的输入输出建模在主动式、硬件高效的多模态交互中的可行性。

---

## 论文元数据

> * **arXiv ID:** [arXiv:2608.08469](https://arxiv.org/abs/2608.08469) [cs.AI]
> * **Submitted:** August 9, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Kaichen Zhang
>   * Wei Huang
>   * Keming Wu
>   * Bo Li
>   * Xiaojuan Qi
> * **DOI:** [10.48550/arXiv.2608.08469](https://doi.org/10.48550/arXiv.2608.08469)

* **arXiv ID:** [arXiv:2608.08469](https://arxiv.org/abs/2608.08469) [cs.AI]
* **提交日期:** 2026年8月9日
* **主要学科:** 人工智能 (`cs.AI`)
* **作者:** 
  * Kaichen Zhang
  * Wei Huang
  * Keming Wu
  * Bo Li
  * Xiaojuan Qi
* **DOI:** [10.48550/arXiv.2608.08469](https://doi.org/10.48550/arXiv.2608.08469)

---

## 摘要

> Existing streaming multimodal models process observations incrementally but still follow a turn-based prefill-then-decode pattern, making them non-duplex: new observations cannot naturally enter an active generation stream. Proactive alternatives use micro-turn polling or external response gates, which fragment continuous interaction, decouple response timing from language generation, and complicate KV-cache-friendly serving. 
> 
> We introduce **Aero Realtime**, a 4B streaming multimodal model with a duplex architecture for realtime generation. Aero Realtime aligns video, audio, and textual output on a shared temporal grid, where each approximately 80-ms audio slot predicts either a lexical token or a silence token. This allows input and output to advance together, enabling one autoregressive objective to learn both when to respond and what to generate. 
> 
> During inference, Aero Realtime appends only the newest multimodal slot, carries forward the previous output state, and reuses the KV cache for efficient incremental execution. We further provide a complete training and serving recipe, including realtime QA construction, slot-aligned supervision, hardware-aware distributed training, and resumable inference. 
> 
> On four NVIDIA A6000 workstation GPUs, Aero Realtime maintains 84-ms median and 173-ms P95 processing lag over 20 minutes of a continuously streamed video, remaining within 200 ms of the source timeline. These results demonstrate the feasibility of fully aligned input-output modeling for duplex, proactive, and hardware-aligned multimodal interaction.

现有的流式多模态模型虽然能增量处理观测数据，但仍遵循“先预填充后解码”的轮次模式，导致其不具备双工能力：新的观测数据无法自然地进入活跃的生成流中。主动式替代方案通常使用微轮询或外部响应门控，这会使连续交互碎片化，将响应时机与语言生成解耦，并使 KV 缓存友好的服务变得复杂。

我们引入了 **Aero Realtime**，这是一个具有双工架构的 4B 流式多模态模型，用于实时生成。Aero Realtime 将视频、音频和文本输出对齐在共享的时间网格上，其中每个约 80 毫秒的音频槽预测一个词汇标记或静音标记。这使得输入和输出能够共同推进，从而使单一的自回归目标能够同时学习何时响应以及生成什么内容。

在推理过程中，Aero Realtime 仅附加最新的多模态槽，延续之前的输出状态，并重用 KV 缓存以实现高效的增量执行。我们进一步提供了完整的训练和服务方案，包括实时问答构建、槽对齐监督、硬件感知分布式训练以及可恢复推理。

在四块 NVIDIA A6000 工作站 GPU 上，Aero Realtime 在 20 分钟的连续流式视频中保持了 84 毫秒的中位处理延迟和 173 毫秒的 P95 延迟，始终保持在源时间轴的 200 毫秒以内。这些结果证明了完全对齐的输入输出建模在双工、主动式和硬件对齐的多模态交互中的可行性。

---

## 关键贡献与架构亮点

> * **Duplex Architecture:** Bypasses conventional turn-based constraints, permitting continuous, bidirectional flow of multimodal inputs and outputs.
> * **Shared Temporal Grid:** Synchronizes video, audio, and text streams into ~80-ms slots, where each audio slot predicts lexical or silence tokens.
> * **Unified Autoregressive Objective:** Learns both *when* to respond and *what* to generate within a single training objective.
> * **Efficient Inference & Serving:** Leverages KV cache reuse by appending only the newest multimodal slot and carrying forward previous output states.
> * **Comprehensive Recipe:** Includes realtime QA construction, slot-aligned supervision, hardware-aware distributed training, and resumable inference pipelines.

* **双工架构：** 绕过了传统的轮次限制，允许多模态输入和输出的连续、双向流动。
* **共享时间网格：** 将视频、音频和文本流同步为约 80 毫秒的时间槽，每个音频槽预测词汇或静音标记。
* **统一自回归目标：** 在单一训练目标内同时学习“何时响应”和“生成什么”。
* **高效推理与服务：** 通过仅附加最新的多模态槽并延续之前的输出状态，利用 KV 缓存重用机制。
* **完整方案：** 包含实时问答构建、槽对齐监督、硬件感知分布式训练以及可恢复推理流水线。

---

## 访问与资源

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.08469) | [HTML Version](https://arxiv.org/html/2608.08469v1) | [TeX Source](https://arxiv.org/src/2608.08469)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2608.08469) | [HTML 版本](https://arxiv.org/html/2608.08469v1) | [TeX 源码](https://arxiv.org/src/2608.08469)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">