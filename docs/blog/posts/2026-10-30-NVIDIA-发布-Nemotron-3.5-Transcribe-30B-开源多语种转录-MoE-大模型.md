---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-30
hide:
  - navigation
tags:
  - NVIDIA
  - Nemotron
  - 语音识别
  - 混合专家模型
  - 开源模型
title: "NVIDIA 发布 Nemotron 3.5 Transcribe：30B 开源多语种语音转录 MoE 大模型"
---

# NVIDIA 发布 Nemotron 3.5 Transcribe：30B 开源多语种语音转录 MoE 大模型，仅需约 4B 激活参数

> # NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language Transcription with ~4B Active Parameters

### 文章背景与核心概要
长期以来，语音识别领域大多依赖传统的级联系统，将语音转录、说话人区分、时间戳对齐等任务拆分到不同模块中，不仅部署繁琐，也难以根据上下文灵活调整输出格式。NVIDIA 此次开源的 Nemotron 3.5 Transcribe 突破性地将 40 种语言的自动语音识别、说话人日志、时间戳对齐与多语种翻译统一集成到单个混合专家大模型 (MoE) 架构中。该模型总参数达 34B，但得益于稀疏激活机制，单次推理仅需约 4.3B 激活参数，甚至可通过量化在消费级显卡上流畅运行。这一开源成果在多项基准测试中刷新了开源模型纪录，不仅极大降低了长音频会议转录与多模态交互的门槛，也为开源语音大模型技术树立了崭新的里程碑。

---

## 内容概要

> ## Summary

NVIDIA 正式推出了 **Nemotron 3.5 Transcribe**，这是一款前沿的开源权重语音大语言模型 (Large Language Model, LLM)，旨在化繁为简、重塑语音转录全流程。该模型支持 40 种主流语言，单次能够处理长达 1 小时的完整音频，将自动语音识别 (Automatic Speech Recognition, ASR)、说话人日志 (Speaker Diarization，即分辨谁在什么时间说了什么)、时间戳强制对齐以及跨语种翻译全部整合进统一的模型架构中。借助纯文本提示词 (Prompt) 驱动，用户可以随心所欲定制转录格式与风格——无论是分毫不差的原声逐字转录、规范的书面整理格式，还是带有精准说话人标记、融合上下文背景的意译均可轻松胜任。尽管该模型在主流 ASR 公开评测基准中刷新了开源模型的领先纪录，但它目前仅支持离线批处理，且在复杂的多人远场普通话会议场景下仍存在一定的准确率短板。

> NVIDIA has introduced **Nemotron 3.5 Transcribe**, a cutting-edge, open-weights speech Large Language Model (LLM) designed to streamline transcription tasks. Capable of handling 40 languages and recordings up to one hour in length, the model unifies automatic speech recognition (ASR), speaker diarization, alignment, and translation into a single framework. Driven by text instructions, users can customize output styles—ranging from verbatim and written forms to speaker-attributed and context-aware translations. While it outperforms existing open-weights models on major ASR leaderboards, it operates strictly offline and exhibits lower accuracy in complex multi-speaker Mandarin meeting scenarios.

---

## 核心速览 (TL;DR)

> ## TL;DR

* **模型规模**：总参数量达 34B，推理时动态激活约 4.3B 参数；原生支持 65,536 个 Token 的超长上下文窗口，单次最大支持 1 小时音频。
* **硬件要求**：BF16 精度下可在单张 H100 80 GB GPU 上运行。官方还提供了深度优化的 FP8 (约 35 GB 显存) 和 NVFP4 (约 21 GB 显存) 权重，其中 NVFP4 版本可在消费级 RTX 5090 显卡上流畅部署。此外还提供专为 `NeMo-Speech.cpp` 定制的 GGUF 格式。
* **基准性能**：在英语及多语种 Open ASR 排行榜上全面领跑主流开源模型，但与业界顶尖的商业闭源 API 相比仍有微弱差距。
* **核心优势**：在 9 个公开的英语 Open ASR 评测集上创下平均 4.71% 词错误率 (Word Error Rate, WER) 的顶尖成绩，显著优于此前开源模型的 4.94%。
* **主要短板**：在 AliMeeting 中文远场多人会议场景下的串联字错误率 (cpCER) 高达 34.95%，识别能力有待提升。
* **总结评价**：一款集文本转录、说话人角色标签、精准时间戳与跨语种翻译于一体的顶尖开源语音模型，虽然目前仅限离线部署且中文会议场景表现相对偏弱，但综合实用价值极高。

> * **Size:** 34B total parameters and ~4.3B active parameters; supports a 65,536-token context window and audio lengths up to 1 hour.
> * **Hardware Requirements:** Runs on 1x H100 80 GB in BF16. Optimized FP8 (~35 GB) and NVFP4 (~21 GB) checkpoints are available (with NVFP4 capable of running on an RTX 5090). GGUF files are tailored for `NeMo-Speech.cpp`.
> * **Performance:** Leads open-weights models on English and multilingual Open ASR Leaderboards, though top commercial APIs still maintain an edge.
> * **Strengths:** Achieves a leading 4.71% mean WER across 9 public English Open ASR sets (surpassing the previous open model benchmark of 4.94%).
> * **Weaknesses:** Registers 34.95% cpCER on AliMeeting Mandarin far-field meetings.
> * **Bottom Line:** A unified open model providing transcripts, speaker labels, timestamps, and translation, though limited to offline deployment with weaker Mandarin meeting performance.

---

## 什么是 Nemotron 3.5 Transcribe？

> ## What is Nemotron 3.5 Transcribe?

Nemotron 3.5 Transcribe 是由 NVIDIA 研发的语音增强语言模型 (Speech-Augmented Language Model, SALM)，它能够将输入的音频与文本指令直接转化为结构化的文本输出。通过将音频编码特征直接注入大模型解码器，该模型让语音转录天生具备了“可提示词调优 (Promptable)”的强大能力。正如 NVIDIA 在其[技术研究报告](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf)中所述，语音转录本质上具有极强的主观性——例如数字是写成阿拉伯数字还是中文汉字、是否过滤口头语气词、专业术语如何规范书写等，都高度取决于阅读者的实际意图。因此，NVIDIA 将这款模型精准定位于专注于语音转录任务的“超级专家”，而非面面俱到的通用聊天助手。

> Nemotron 3.5 Transcribe is a speech-augmented language model (SALM) developed by NVIDIA that translates audio inputs and text instructions into structured text outputs. By routing audio embeddings through an encoder directly into an LLM decoder, the model makes transcription natively promptable. According to NVIDIA’s [technical research report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf), transcription is inherently subjective—formatting choices like numbers, fillers, and domain-specific terms depend heavily on the reader's intent. Consequently, NVIDIA positions this model as a dedicated transcription specialist rather than a general-purpose assistant.

---

## 它的底层架构是如何运作的？

> ## How Does the Architecture Work?

该模型的核心架构主要由以下三大组件构成：

> The model’s architecture consists of three primary components:

* **并行专家编码器 (Parallel Expert Encoder)**：由一个可训练的 0.6B Transformer 语音识别编码器，与一个冻结权重的 [Nemotron 3 Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization) 说话人日志模型并行运行。该日志模块能够同时追踪多达 8 位说话人，每隔 80 毫秒将说话人活跃度特征无缝融入 ASR 特征中。这使得大语言模型无需改动核心架构，便能在原生状态下敏锐捕捉说话人轮替与转换。
* **大模型主干网络 (LLM Backbone)**：基于 [Nemotron 3.5 Lightning 30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) 混合架构，融合了 Mamba-2 与 Transformer 混合专家模型 (Mixture of Experts, MoE)。模型共包含 52 层网络 (23 层 Mamba-2、23 层 MoE 以及 6 层自注意力机制 Attention 层)。每一层 MoE 都会将 Token 动态路由至 128 个专家中的 6 个，并外加 1 个共享专家。大幅精简注意力层使得处理长达一小时的超长音频时，键值缓存 (KV Cache) 依然保持极其轻量紧凑。
* **功能扩展插件 (Add-ons)**：配备了一个共享的多 Token 预测 (Multi-Token Prediction, MTP) 层，用于在投机解码 (Speculative Decoding) 中快速生成候选 Token；同时集成了参数量仅为 50M 的 CTC 适配器模块，用于在转录完成后将文本与原始音频强制对齐，从而输出毫秒级的精准字词时间戳。

> * **Parallel Expert Encoder:** A trainable 0.6B Transformer ASR encoder running alongside a frozen [Nemotron 3 Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization) model. The diarizer tracks up to 8 speakers, feeding speaker activity directly into the ASR features every 80 ms. This allows the LLM to inherently recognize speaker turns without altering its core architecture.
> * **LLM Backbone:** Built on the [Nemotron 3.5 Lightning 30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) hybrid Mamba-Transformer Mixture-of-Experts (MoE). It contains 52 layers (23 Mamba-2, 23 MoE, and 6 attention layers). Each MoE layer routes tokens to 6 of 128 experts plus 1 shared expert. The minimal use of attention layers keeps the KV cache compact for hour-long audio files.
> * **Add-ons:** Includes a shared multi-token prediction (MTP) layer to draft tokens for speculative decoding, alongside a 50M-parameter CTC adapter that force-aligns completed transcripts with audio to provide precise word timestamps.

虽然官方将其命名为“30B-A4B”，但该模型的实际检查点文件总计包含约 340 亿参数，多出的部分主要来自 1.3B 的 MTP 模块与音频前置处理组件。在训练流程上，团队首先在由 256 张 H100 GPU 组成的高性能集群上进行了 28,500 步的监督微调 (Supervised Fine-Tuning, SFT)，随后执行了精炼的强化学习阶段 (以 $1 - \text{WER}$ 为奖励指标进行了 400 次 GSPO 策略更新)。在整个训练周期内，模型累计学习了约 172 万小时各不相同的真实音频 (计入多轮重复训练后累计达 650 万小时)。

> Although named "30B-A4B," the checkpoint contains roughly 34 billion parameters, with the additional weight driven by the 1.3B MTP module and audio components. Training utilized a supervised fine-tuning stage across 256 H100 GPUs for 28,500 steps, followed by a brief reinforcement learning stage (400 GSPO updates using a reward metric of $1 - \text{WER}$). The model was exposed to ~1.72M unique hours of audio (6.5M hours including repeats).

---

## 基准测试性能表现

> ## Benchmark Performance

*所有指标数据均源自 NVIDIA 在其[技术研究报告](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf)中公布的实测结果。*

> *All metrics are self-reported by NVIDIA in their [technical research report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf).*

* **英语公开 ASR 评测 (9 个公开数据集)**：取得 4.71% 的平均词错误率 (WER)，超越了此前表现最优的开源模型 [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) (4.94%)；而顶尖的闭源商业系统 (如 OtterAI speech-v3.1) 则仍以 3.88% 保持领先。
* **多语种公开 ASR 评测 (7 种主流语言)**：测得 4.62% 的平均 WER，大幅优于 Qwen3-ASR-1.7B 的 6.49%；该类别的榜首由商业系统 ElevenLabs Scribe v2 以 3.56% 占据。
* **长音频 ASR 转录**：平均 WER 达到 10.98%，显著超越 Parakeet-TDT-0.6B-v3 (13.37%)。
* **完整多人会话场景**：平均串联词错误率 (Concatenated Permutation WER, cpWER) 达到 15.80%，击败了基于 DiariZen 的 DiCoW v3.3 传统方案 (16.83%)，成为该领域首个性能超越传统级联方案的语音增强大模型 (SALM)。
* **上下文感知 ASR**：通过在提示词中附加专业实体列表，ContextASR-Bench 评测上的命名实体识别错误率从 12.21% 骤降至 2.20%。

> * **English Open ASR (9 public sets):** Achieves a mean Word Error Rate (WER) of 4.71%, beating the next best open model, [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) (4.94%). Commercial systems like OtterAI speech-v3.1 still lead at 3.88%.
> * **Multilingual Open ASR (7 languages):** Records a mean WER of 4.62%, compared to 6.49% for Qwen3-ASR-1.7B. ElevenLabs Scribe v2 leads this category at 3.56%.
> * **Long-form ASR:** Scores 10.98% mean WER, outperforming Parakeet-TDT-0.6B-v3 (13.37%).
> * **Multi-speaker Full Sessions:** Reaches 15.80% mean cpWER, beating DiCoW v3.3 with DiariZen (16.83%), making it the first SALM to outperform cascaded systems in this domain.
> * **Contextual ASR:** Utilizing an entity list reduces named-entity WER on ContextASR-Bench from 12.21% down to 2.20%.

---

## 如何部署 Nemotron 3.5 Transcribe

> ## How to Deploy Nemotron 3.5 Transcribe

目前，模型完整权重已正式上线 Hugging Face，提供 [BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)、[FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-FP8)、[NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4) 以及 [GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) 多种格式，同时还配套了可选的 [DFlash2 草稿模型](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-DFlash2)。开源协议遵循对商业应用十分友好的 [OpenMDW-1.1 开源协议](https://openmdw.ai/license/1-1/)。

> Model weights are available on Hugging Face in [BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B), [FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-FP8), [NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4), and [GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) formats, with an optional [DFlash2 draft model](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-DFlash2). Usage is governed by the commercial-friendly [OpenMDW-1.1 license](https://openmdw.ai/license/1-1/).

在推理运行时方面，该模型已支持 vLLM 0.32.0 (需配合 [NeMo Speech 插件](https://github.com/NVIDIA-NeMo/Speech))、Hugging Face Transformers 以及 [SGLang-Omni 0.2.0](https://sgl-project.github.io/sglang-omni/cookbook/nemotron_transcribe.html)；其中 vLLM 还提供了与 OpenAI 完全兼容的标准 API 接口。

> Supported runtimes include vLLM 0.32.0 (with the [NeMo Speech plugin](https://github.com/NVIDIA-NeMo/Speech)), Hugging Face Transformers, and [SGLang-Omni 0.2.0](https://sgl-project.github.io/sglang-omni/cookbook/nemotron_transcribe.html), with vLLM providing an OpenAI-compatible API.

若追求极限吞吐量，搭载 NVFP4 精度与 DFlash2 的 Nemotron Transcribe NIM 微服务可在单张 RTX PRO 6000 Blackwell 服务器版 GPU 上达到每秒处理 2,238 秒音频的惊人速度，转录一段 30 秒的语音片段仅需 0.13 秒。虽然基于开源 vLLM 的实现方案速度约为 NIM 的一半，但单张 H100 在 BF16 精度搭配 MTP2 下依然能实现约 410 倍实时转录速率 (RTFx)。

> For maximum throughput, the Nemotron Transcribe NIM (utilizing NVFP4 and DFlash2) enables an RTX PRO 6000 Blackwell Server Edition to process 2,238 seconds of audio per second, returning a 30-second clip in just 0.13 seconds. While open-source vLLM implementations run roughly twice as slow, a single H100 in BF16 with MTP2 achieves approximately 410 RTFx.

---

## 与其他主流开源 ASR 模型的横向对比

> ## Comparison with Other Open ASR Models

| 特性 (Feature) | **Nemotron 3.5 Transcribe** | [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | [Canary-Qwen-2.5B](https://huggingface.co/nvidia/canary-qwen-2.5b) | [Whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| :--- | :--- | :--- | :--- | :--- |
| **参数量 (Parameters)** | 总计 34B，激活约 4.3B | 1.7B | 2.5B | 1.55B |
| **支持语言数 (Languages)** | 40 种 | 30 种 + 22 种中文方言 | 仅限英语 | 99 种 (HF 标签) |
| **单次请求最大音频时长** | 1 小时 | 未公开 | 训练时为 40 秒 | 30 秒窗口 (长音频分块切片) |
| **说话人归属识别** | 原生内置 (支持多达 8 位说话人) | 未列出 | 未列出 | 未列出 |
| **字词级时间戳** | 原生内置 (CTC 适配器) | 需外接独立 ForcedAligner-0.6B | 未列出 | 支持 (词级) |
| **开源许可协议** | OpenMDW-1.1 | Apache-2.0 | CC-BY-4.0 | Apache-2.0 |
| **英语 Open ASR (9个公开集，平均 WER)** | **4.71%** | 4.94%\* | 5.38%\* | 6.66%\* |
| **多语种 Open ASR (7种语言，平均 WER)** | **4.62%** | 6.49%\* | 不适用 (仅限英语) | 7.94%\* |
| **参考运行硬件** | 1 张 H100 80 GB (BF16) | 未公开 | 已在 A6000、A100、RTX 5090 上测试 | 未公开 |

*\*更新后的 9 集排行榜上的竞品分数引自 NVIDIA 技术报告，参考了 2026 年 10 月的 Hugging Face 排行榜评测结果。*\*

> *\*Competitor scores on the updated 9-set leaderboard are sourced from NVIDIA's technical report, referencing Hugging Face leaderboard evaluations from October 2026.\*

---

## 核心要点总结

> ## Key Takeaways

* **全功能一体化整合**：在单一开源模型中完整囊括了 40 种语言的基础文本转录、说话人日志、毫秒级时间戳以及跨语种翻译。
* **领跑开源生态的顶尖性能**：在英语语音识别开源方案中斩获 4.71% 的领先 WER，不过头部商业闭源 API 仍保持着微弱优势。
* **灵活适配不同算力硬件**：仅需约 4.3B 动态激活参数，适配弹性极广——既可以在数据中心以 BF16 跑在 H100 上，也能通过 NVFP4 量化本地部署在消费级 RTX 5090 显卡上。
* **出色的上下文精准度**：只需在提示词中附带专业术语或实体词表，即可将命名实体识别错误率从 12.21% 锐减至 2.20%。
* **当前存在的技术局限**：目前仅支持离线批处理模式，且在中文普通话远场会议以及中英混杂 (Code-Switching) 场景下的错误率相对偏高。

> * **All-in-One Capability:** Handles raw transcriptions, speaker diarization, timestamps, and translations across 40 languages within a single open model.
> * **Top-Tier Open Performance:** Achieves a leading 4.71% English WER among open-weights solutions, though commercial APIs maintain a slight advantage.
> * **Flexible Footprint:** Features ~4.3B active parameters that scale across environments—from BF16 on an H100 down to NVFP4 running locally on an RTX 5090.
> * **Contextual Precision:** Providing an entity list drastically reduces named-entity error rates from 12.21% down to 2.20%.
> * **Current Limitations:** Restricted to offline batch processing, with notably higher error rates on Mandarin meetings and code-switching tasks.

---

## 资源链接

> ## Resource Links

* **技术文档与代码**：[技术报告](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) | [项目主页](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) | [在线演示 (Live Demo)](https://huggingface.co/spaces/nvidia/nemotron-transcribe)
* **模型权重下载**：[Hugging Face 权重集合](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)

> * **Documentation & Code:** [Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) | [Project Page](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) | [Live Demo](https://huggingface.co/spaces/nvidia/nemotron-transcribe)
> * **Model Weights:** [Hugging Face Collection](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)
