---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-29
hide:
  - navigation
tags:
  - NVIDIA
  - Nemotron
  - 语音识别
  - 开源模型
  - 语音数据集
title: "NVIDIA 发布开源语音大模型 Nemotron 3.5 Transcribe 与 46 万小时语音数据集 Granary v2"
---

# NVIDIA 发布开源语音大模型 Nemotron 3.5 Transcribe 与 46 万小时语音数据集

> # NVIDIA Launches Open-Weight Speech Model and 463,062-Hour Audio Dataset

![NVIDIA Nemotron Speech Model](./images/fedc5743e0ea.jpg)

### 文章背景与核心概要

在人工智能从纯文本加速迈向全模态交互的浪潮中，语音作为人类最自然、最高效的信息载体，是构建下一代具身智能与交互式 AI 智能体 (AI Agent) 的核心拼图。然而长期以来，兼具超高转录精度、复杂多人声分辨与跨语言理解的顶尖语音大模型大多由闭源商业 API 把持，开源社区不仅面临高质量多语言训练音频严重匮乏的窘境，更受制于传统多任务流水线拼装带来的高延迟与性能瓶颈。2026 年 10 月 28 日，NVIDIA 正式开源了全新一代语音大模型 Nemotron 3.5 Transcribe，并同步推出了涵盖 48 种语言、超 46 万小时音频的 Granary v2 开放数据集及清洗管线。该模型将语音识别、说话人日志、多语言翻译及音频问答融于单一权重中，不仅在权威基准测试上刷新开源纪录，更凭借单卡每秒转录 2,238 秒音频的强悍性能，为全球开发者树立了开放语音智能的新标杆。

---

## 核心概述

> ## Summary

2026 年 10 月 28 日，NVIDIA 正式发布了功能强大的开源权重语音大模型 **Nemotron 3.5 Transcribe**。该模型开创性地将多语言语音转录、说话人归因、跨语言翻译以及音频问答等核心能力凝聚在同一个权重检查点 (Checkpoint) 中。与模型同步发布的还有 **Granary v2**——这是一个涵盖 48 种语言、超过 46.3 万小时音频的庞大开源语音数据集及其专属数据清洗流水线。该模型遵循 OpenMDW-1.1 协议，完全开放商用与非商用许可。凭借在多项主流基准测试中展现出的顶尖水准，Transcribe 为开源音频智能树立了崭新的行业标杆。

> On October 28, 2026, NVIDIA released **Nemotron 3.5 Transcribe**, a powerful open-weight speech model that integrates multilingual transcription, speaker attribution, translation, and audio question-answering into a single checkpoint. Released alongside **Granary v2**—an open speech dataset and curation pipeline covering over 463,062 hours of audio across 48 languages—the model supports commercial and non-commercial use under the OpenMDW-1.1 license. Delivering state-of-the-art performance across multiple benchmarks, Transcribe sets a new standard for open-weight audio intelligence.

---

## 模型架构与提示词交互

> ## Architecture and Prompting

Transcribe 在单个 340 亿 (34B) 参数的权重模型中，将高灵敏度语音编码器与强大的语言模型骨干网络深度融合，每个 Token 仅激活约 43 亿 (4.3B) 参数，并提供了高达 65,536 个 Token 的超长上下文窗口。

> Transcribe pairs a speech encoder with a language backbone in a single 34B-parameter checkpoint, utilizing approximately 4.3B active parameters per token and a 65,536-token context window. 

* **语音处理栈 (The Speech Stack)**：集成了一个 6 亿 (600M) 参数的 Transformer 自动语音识别 (Automatic Speech Recognition, ASR) 编码器、约 9,900 万 (99M) 参数的 Nemotron-3-Diarization 说话人日志 (Speaker Diarization) 编码器，以及一个用于输出词级时间戳的联结主义时间分类 (Connectionist Temporal Classification, CTC) 输出头。
* **语言骨干网络 (The Language Backbone)**：由 NVIDIA 的 Nemotron-3.5 Lightning 30B-A3B 驱动，这是一款结合了 Mamba-2 与 Transformer 的混合专家模型 (Mixture of Experts, MoE)。
* **模型发布格式 (Model Formats)**：默认提供 BF16 精度版本，并附带 FP8 和 NVFP4 量化变体，同时还提供可选的 DFlash2 草稿模型以支持推测解码 (Speculative Decoding)。

> * **The Speech Stack:** Combines a 600M-parameter Transformer ASR encoder, the ~99M-parameter Nemotron-3-Diarization speaker encoder, and a connectionist temporal classification head for word timestamps.
> * **The Language Backbone:** Powered by NVIDIA’s Nemotron-3.5 Lightning 30B-A3B, a hybrid Mamba-2–Transformer mixture-of-experts model. 
> * **Model Formats:** Shipped in BF16, with FP8 and NVFP4 quantized variants alongside an optional DFlash2 draft model for speculative decoding.

模型的输出行为完全由自然语言提示词控制。开发者不仅可以自由要求逐字原样转录还是规范书面语转录，还可以注入上下文专业词汇、指定输出说话人标签与词级精确时间戳、实现语音与英语之间的双向翻译，甚至直接对音频内容发起交互式智能问答。

> Outputs are controlled via natural-language prompts. Developers can request verbatim or clean written transcripts, supply context vocabulary, request speaker tags and word-level timestamps, translate speech to/from English, or query the audio directly. 

---

## 基准测试结果

> ## Benchmark Results

NVIDIA 报告了该模型在多项行业权威评测榜单上的领先性能表现：

> NVIDIA reports leading performance metrics across major industry leaderboards:

* **Hugging Face Open ASR 英文榜单**：在所有开源权重模型中位列第一（剔除闭源 API 模型），取得 **5.33% 的平均字错率 (Word Error Rate, WER)**。
* **多语言与长音频评测**：在开源模型中斩获最低的多语言错误率（跨 7 种语言的 **平均 WER 仅为 4.62%**），同时在长音频评测中实现最低的 **10.98%** 错误率。
* **说话人归因**：在 David AI 包含 21 种语言的 DAI-ASR-I18N 赛道上取得最低的说话人日志错误率 (18.26%)，并在 VoiceArena 的英文 Diarization-Bench 上强势夺冠。

> * **Hugging Face Open ASR English:** Ranks first among open-weight models with a **5.33% average word error rate (WER)** (API models excluded).
> * **Multilingual & Long-Form:** Achieves the lowest multilingual result (**4.62% mean WER** across seven languages) and the lowest long-form result (**10.98%**) among open-weight models.
> * **Speaker Attribution:** Posts the lowest diarization error rate (18.26%) on David AI's 21-language DAI-ASR-I18N track and secures first place on VoiceArena's English Diarization-Bench.

---

## Granary v2 数据集与清洗流水线

> ## Granary V2 Dataset and Pipeline

Granary v2 是支撑该模型训练混合配方的庞大开源数据基础设施。借助 NVIDIA NeMo Curator 工具构建，其公开元数据清单涵盖了来自 16 个源语料库、横跨 **48 种语言的 463,062 小时** 音频数据。

> Granary v2 is the massive open data infrastructure driving the model's training mixture. Built using NVIDIA NeMo Curator, its public manifest spans **463,062 hours across 48 languages** and 16 source corpora. 

该数据清洗流水线严格执行四阶段处理流程：

> The curation pipeline executes a four-stage process:

1. 元数据抽取与音频预处理；
2. 语音转录：结合主 ASR 模型与备用恢复模型，并通过幻觉检测机制进行质量门控；
3. 任务标签生成：辅以多模型一致性校验；
4. 高保真精细过滤：例如将 VoxPopuli 语料库从 35.4 万小时精简提炼至 11.1 万小时高质量音频。

> 1. Metadata and audio preparation.
> 2. Transcription utilizing primary and recovery ASR models gated by a hallucination check.
> 3. Task-label generation with agreement validations.
> 4. High-fidelity filtering (e.g., reducing the VoxPopuli corpus from 354,000 to 111,000 hours).

---

## 医疗场景微调实战案例与模型部署

> ## Medical Fine-Tuning Case Study and Deployment

为了展示模型强大的垂直领域适配能力，NVIDIA 重点介绍了针对印度医疗专业人员的垂直适配案例（基于 Eka Care 包含 3,619 条真实录音的基准测试集）。通过利用专业的合成数据与真实医疗数据集对模型进行微调，基准测试的字错率由 22.44% 显著降低至 **12.17%**（相对降幅高达 45.8%）。

> To demonstrate adaptability, NVIDIA highlighted a medical adaptation case study using Eka Care’s benchmark of 3,619 recordings from Indian healthcare professionals. Fine-tuning the model with specialized synthetic and medical datasets reduced the benchmark word error rate from 22.44% down to **12.17%** (a relative reduction of 45.8%).

### 部署方案与推理性能

> ### Deployment and Performance

* **硬件兼容性 (Hardware Compatibility)**：单张 NVIDIA GPU 即可高效运行，硬件支持覆盖从边缘端的 Jetson AGX Thor、工作站级的 DGX Spark，到数据中心级的 Blackwell 计算集群。
* **推理吞吐量 (Throughput)**：借助基于 NVFP4 精度与 DFlash2 推测解码优化后的 NIM 推理微服务实现，单张 RTX PRO 6000 Blackwell Server Edition GPU 每秒可处理多达 **2,238 秒的音频** 转录。
* **框架支持 (Framework Support)**：服务化部署支持搭载 NeMo Speech 插件的 vLLM 0.32.0，亦可通过 `NeMo-Speech.cpp` 轻松实现本地轻量化推理。

> * **Hardware Compatibility:** Runs efficiently on a single NVIDIA GPU, ranging from Jetson AGX Thor and DGX Spark to Blackwell data-center systems.
> * **Throughput:** Using an optimized NIM implementation with NVFP4 precision and DFlash2 speculative decoding, an RTX PRO 6000 Blackwell Server Edition GPU can transcribe up to **2,238 seconds of audio per second**.
> * **Framework Support:** Serving utilizes vLLM 0.32.0 with the NeMo Speech plugin or local inference via `NeMo-Speech.cpp`.
