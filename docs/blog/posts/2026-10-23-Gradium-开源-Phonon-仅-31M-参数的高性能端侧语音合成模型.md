---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-23
hide:
  - navigation
tags:
  - Gradium Phonon
  - TTS
  - 端侧语音合成
  - 开源模型
  - Apache 2.0
title: "Gradium 开源 Phonon：仅 31M 参数的高性能端侧语音合成模型"
---

# Gradium 开源 Phonon：仅 31M 参数的高性能端侧语音合成模型

> # Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache 2.0

### 文章背景与核心概要

从云端大模型向终端边缘设备的下沉，是生成式 AI (Generative AI) 迈向普及的关键战役。长期以来，高品质的文本转语音 (Text-to-Speech, TTS) 技术往往严重依赖庞大的云端算力与持续的 API 计费，而在边缘计算与移动端设备上运行的轻量级模型，则常面临发音机械、错误率高和首包延迟过长的困境。由前 Kyutai 团队成员创立的法国语音 AI 初创公司 Gradium，正式开源了革命性的端侧语音合成模型家族 Phonon。其中专攻英语的 Phonon 31m 核心参数量仅有 31M (量化后仅占 64.5 MB 存储)，采用商业友好的 Apache 2.0 宽松协议开源，不仅在常规消费级 CPU 上实现了低至 7 毫秒的超低首音频延迟，更在涵盖复杂边缘用例的严苛文本基准测试中大幅超越了同类主流模型，为离线设备、具身机器人、智能穿戴及各类本地 AI 智能体 (AI Agent) 带来了真正轻量且开箱即用的高保真实时语音能力。

---

## 内容摘要

> ## Summary

Gradium 正式开源了轻量级语音合成模型家族 **Phonon**，专门针对本地端侧与边缘设备的高效运行而设计。该模型家族提供了 31M 与 40M 两种参数规格；其中专攻英语的 **Phonon 31m** 采用宽松的 Apache 2.0 协议开源，其 q8 量化权重体积仅为精巧的 64.5 MB。无论是常规 CPU、智能手机、以树莓派 5 (Raspberry Pi 5) 为代表的单板计算机，还是网页浏览器，Phonon 都能在脱离云端 API、无需独立 GPU 加速以及零字符计费成本的前提下，实现自然流畅的端侧实时语音生成。

> Gradium has open-sourced **Phonon**, a family of lightweight text-to-speech (TTS) models designed for local, on-device execution. Available in 31M and 40M parameter sizes, the English **Phonon 31m** model is licensed under Apache 2.0 and packs into a compact 64.5 MB file. It enables natural, real-time speech generation on CPUs, phones, single-board computers like the Raspberry Pi 5, and browsers without requiring cloud APIs, GPUs, or per-character billing.

---

## 核心速览

> ## TL;DR

* **模型体量**：核心模型参数量仅 31M (不含音频分词器)，q8 GGUF 格式下仅占 64.5 MB 存储，支持 24 kHz 单声道高品质输出；而多语种版本 Phonon 40m 拥有 40M 参数，权重文件仅 74.6 MB。
* **硬件支持**：通用于标准 CPU、智能手机、树莓派 5 (Raspberry Pi 5)、网页浏览器 (通过 WASM 与 WebGPU) 以及 NVIDIA GPU，完全不强求独立显卡。
* **推理性能**：在 Gradium 测试的所有开源模型中斩获最高的英语 Elo 评分；在标准消费级 CPU 上实现仅约 7 毫秒的首音频响应延迟。
* **核心优势**：在包含 500 个复杂边缘句式的严苛基准评测集中，单词错误率 (Word Error Rate, WER) 低至 1.70% (大幅超越了 Kokoro 的 3.50%)。
* **潜在短板**：在 Seed-TTS 大语言模型 WER 基准评测中，得分略逊于 Kokoro 与 Magpie 等竞品 (0.51% 对比 0.45%)。

> * **Size:** 31M parameters (excluding audio tokenizer), 64.5 MB q8 GGUF, 24 kHz mono output. Phonon 40m features 40M parameters in a 74.6 MB file.
> * **Hardware Support:** Runs on CPUs, smartphones, Raspberry Pi 5, browsers (WASM, WebGPU), and NVIDIA GPUs. No dedicated GPU required.
> * **Performance:** Top English Elo among open models tested by Gradium; achieves ~7 ms to first audio on standard CPUs.
> * **Pros:** Low Word Error Rate (WER) of 1.70% on a 500-sentence hard benchmark set (outperforming Kokoro's 3.50%).
> * **Cons:** Scores slightly behind models like Kokoro and Magpie on the Seed-TTS LLM WER benchmark (0.51% vs. 0.45%).

---

## 什么是 Gradium Phonon？

> ## What is Gradium Phonon?

Phonon 是由位于巴黎的语音 AI 初创团队 **Gradium** 开发的开源权重文本转语音模型家族。Gradium 脱胎于知名开源实验室 Kyutai，致力于将高保真、低延迟的语音合成能力无缝带入边缘计算设备、个人笔记本、智能手机以及网页浏览器端。

> Phonon is an open-weight TTS model family developed by **Gradium**, a Paris-based voice AI company spun out of Kyutai. It brings high-performance speech synthesis directly to edge devices, laptops, mobile phones, and web browsers.

该模型家族目前涵盖三大核心版本分支：

> The model family consists of three main variants:

* **Phonon 31m**：纯英文模型，内置 37 款丰富音色，采用最利于商业化落地的 Apache 2.0 协议开源。
* **Phonon 40m**：单语种独立模型，支持英语、法语、德语、西班牙语以及葡萄牙语 (遵循 CC BY-NC 4.0 非商业化许可)。
* **Phonon 40m Multilingual (多语种版)**：将上述 5 种语言融汇于单一模型之中，囊括多达 102 款预置音色 (遵循 CC BY-NC 4.0 非商业化许可)。

> * **Phonon 31m:** English-only, features 37 built-in voices, and is licensed under Apache 2.0.
> * **Phonon 40m:** Single-language models available for English, French, German, Spanish, and Portuguese (CC BY-NC 4.0).
> * **Phonon 40m Multilingual:** Combines all 5 languages into a single model with 102 voices (CC BY-NC 4.0).

---

## Phonon 的技术架构与工作原理

> ## How Does Phonon Work?

在底层原理上，Phonon 采用了因果 Transformer (Causal Transformer) 作为核心骨干网络，其前缀输入由待合成文本与发音人嵌入向量 (Speaker Embedding) 共同拼接而成。模型借助词表规模为 4,000 个 Token 的 SentencePiece 分词器直接解析原始文本字符，彻底摒弃了传统语音合成中繁琐且易出错的音素 (Phoneme) 转换管线。

> Phonon utilizes a causal transformer backbone that takes a prefix combining text and speaker embeddings. A SentencePiece tokenizer with a 4,000-token vocabulary parses raw text directly, bypassing traditional phoneme conversion steps.

Phonon 的端到端推理架构流水线设计极为紧凑高效：

> The architecture pipeline functions as follows:

1. **输入文本与发音人嵌入 (Input Text & Speaker Embedding)**：接收原始纯文本输入，并挂载内置预置音色、克隆音色或自定义发音人特征向量；
2. **SentencePiece 分词处理 (SentencePiece Tokenization)**：直接对文本完成 Token 切分，无须任何中介音素字典或注音前置步骤；
3. **因果 Transformer 骨干网络 (Causal Transformer)**：自回归 (Autoregressive) 地为每 80 毫秒的音频帧生成一个潜在向量 (在 31m 版本中包含 6 层结构、隐藏层维度 512，以及 8 个注意力头)；
4. **流匹配预测头 (Flow-Matching Head)**：通过单步流匹配 (Flow-Matching) 机制，一步到位将潜在向量与环境噪声解算为连续音频嵌入，并辅以语音终止检测头 (End-of-Speech Detection Head) 实时把控句尾断句；
5. **Mimi 音频解码器 (Mimi Decoder)**：采用源自 Kyutai 的 Mimi 神经音频解码器的轻量化精简变体，将连续嵌入快速解码还原为 24 kHz 高保真 PCM 音频流。

> 1. **Input Text & Speaker Embedding:** Accepts raw text alongside built-in, cloned, or custom speaker embeddings.
> 2. **SentencePiece Tokenization:** Direct text processing without phoneme intermediaries.
> 3. **Causal Transformer:** Generates one latent vector per 80 ms frame autoregressively (6 layers, width 512, and 8 attention heads in the 31m version).
> 4. **Flow-Matching Head:** Converts latents and noise into continuous audio embeddings in a single step, paired with an end-of-speech detection head.
> 5. **Mimi Decoder:** A streamlined variant of Kyutai’s Mimi decoder translates embeddings into 24 kHz PCM audio streams.

值得强调的是，Phonon 31m 与 40m 模型均是通过大规模教师模型进行知识蒸馏 (Knowledge Distillation) 提炼而成，整个训练过程在基于 NCCL 通信与 CUDA Graphs 深度优化的 NVIDIA H100 GPU 集群上高效完成。

> Both the 31m and 40m models are distilled from a larger teacher model, trained on an NVIDIA H100 cluster utilizing NCCL and CUDA Graphs.

---

## 基准测试与性能表现

> ## Benchmark Performance

在 Gradium 组织的双盲成对听觉评估测试中 (共计 1,189 位评审员参与，累计产生 17,270 次有效盲测投票)，美式英语系列模型展现出了卓越的主观听感表现：

> In blind pairwise listening tests conducted by Gradium across 1,189 raters and 17,270 votes, US English variants performed strongly:

* **Phonon 40m**：2117 Elo
* **Phonon 31m**：2098 Elo
* **Kokoro**：2043 Elo
* **NeuTTS**：2034 Elo
* **Magpie**：1939 Elo

> * **Phonon 40m:** 2117 Elo
> * **Phonon 31m:** 2098 Elo
> * **Kokoro:** 2043 Elo
> * **NeuTTS:** 2034 Elo
> * **Magpie:** 1939 Elo

在涵盖电话号码、电子邮箱地址以及邮政编码等大量棘手边缘用例的公开**高难度句式基准数据集 (Hard-sentence Dataset, 共 500 句)** 上，Phonon 31m 斩获了惊艳的 **1.70% WER**，显著优于主流轻量模型 Kokoro (3.50%) 与 NeuTTS Nano (8.71%)。不过，在相对基础平顺的 Seed-TTS 基准测试集上，差距有所收窄：Phonon 31m 录得了 0.51% 的大语言模型辅助 WER，略微落后于 Kokoro 的 0.45%。

> On a rigorous public **hard-sentence dataset** (comprising 500 sentences filled with edge cases like phone numbers, emails, and postal codes), Phonon 31m achieved a **1.70% WER**, significantly outperforming Kokoro (3.50%) and NeuTTS Nano (8.71%). However, on the simpler Seed-TTS benchmark set, performance normalizes slightly, with Phonon 31m recording a 0.51% LLM WER compared to Kokoro's 0.45%.

---

## CPU 性能与延迟表现

> ## CPU Performance & Latency

Phonon 针对超低延迟边缘侧部署进行了全方位的底层计算优化：

> Phonon is heavily optimized for low-latency edge deployment:

* **MacBook Air M5 (CPU 4 线程)**：首音频生成时间仅需 **6.9 毫秒**，推理吞吐达 **29.9 倍实时速率** (而在启用 KleidiAI 与 Apple Accelerate 加速库后，更进一步缩短至 5.4 毫秒，吞吐高达 46.7 倍实时速率)；
* **树莓派 5 (Raspberry Pi 5)**：仅需 **38 毫秒** 即可吐出首段音频，整体生成维持在 **3.7 倍实时速率**；
* **高通骁龙 8 至尊版 Gen 5 (Snapdragon 8 Elite Gen 5)**：首音频延迟仅 **7.5 毫秒**，达到 **24 倍实时速率**；
* **NVIDIA L40S (CUDA 加速)**：首段语音延迟更是压低至极速的 **5 毫秒**。

> * **MacBook Air M5 (CPU, 4 threads):** Reaches first audio in **6.9 ms** at **29.9x real-time speed** (improving to 5.4 ms and 46.7x with KleidiAI and Apple Accelerate).
> * **Raspberry Pi 5:** Starts in **38 ms** and runs at **3.7x real-time speed**.
> * **Snapdragon 8 Elite Gen 5:** First audio in **7.5 ms** at **24x real-time**.
> * **NVIDIA L40S (CUDA):** First speech achieved in **5 ms**.

---

## 主流端侧语音模型横向对比

> ## Model Comparison

| 评估特性 | Phonon 31m | Phonon 40m Multilingual | Kokoro-82M | NeuTTS Nano | Kitten TTS v0.8 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **开发者** | Gradium | Gradium | hexgrad | Neuphonic | KittenML |
| **参数量** | 31M (不含分词器) | 40M | 82M | 总计约 228.7M，激活约 116.8M | 15M / 40M / 80M |
| **权重体积** | 64.5 MB (q8) | 74.6 MB (q8) | 未披露 | 未披露 | 25 至 80 MB |
| **支持语种** | 英语 | 英语、法语、德语、西语、葡语 | 8 种语言 (v1.0) | 英语 (套件扩展西、法、德语) | 英语 |
| **开源协议** | Apache 2.0 | CC BY-NC 4.0 | Apache 2.0 | NeuTTS Open License 1.0 | Apache 2.0 |
| **高难度句式 WER (英语)** | 1.70% | 2.11% | 3.50% | 8.71% | 7.40% |
| **英语 Elo 评分** | 2098 | 2097 | 2043 | 2034 | 未测试 |
| **Seed-TTS LLM WER (英语)** | 0.51% | 0.48% | 0.45% | 0.62% | 未测试 |
| **首音频延迟 (M5 CPU)** | 6.9 ms | 8.8 ms | 517 ms | 未披露 | 未披露 |

> | Feature | Phonon 31m | Phonon 40m Multilingual | Kokoro-82M | NeuTTS Nano | Kitten TTS v0.8 |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | **Developer** | Gradium | Gradium | hexgrad | Neuphonic | KittenML |
> | **Parameters** | 31M (excl. tokenizer) | 40M | 82M | ~228.7M total, ~116.8M active | 15M / 40M / 80M |
> | **Weights** | 64.5 MB (q8) | 74.6 MB (q8) | Not disclosed | Not disclosed | 25 to 80 MB |
> | **Languages** | English | EN, FR, DE, ES, PT | 8 (v1.0) | English (collection adds ES, FR, DE) | English |
> | **License** | Apache 2.0 | CC BY-NC 4.0 | Apache 2.0 | NeuTTS Open License 1.0 | Apache 2.0 |
> | **Hard-set WER (EN)** | 1.70% | 2.11% | 3.50% | 8.71% | 7.40% |
> | **English Elo** | 2098 | 2097 | 2043 | 2034 | Not tested |
> | **Seed-TTS LLM WER (EN)** | 0.51% | 0.48% | 0.45% | 0.62% | Not tested |
> | **First Audio (M5 CPU)** | 6.9 ms | 8.8 ms | 517 ms | Not disclosed | Not disclosed |

---

## 开发者部署与生态集成

> ## Developer Deployment

官方推理运行时 (`xn-ptts`) 采用双重宽松开源协议 (MIT 或 Apache 2.0)，提供了极为宽广的多语言生态绑定，原生支持 Rust、Python (`pip install ptts`)、Swift、C、C++，并支持在浏览器端通过 `phonon-tts` 直接驱动。此外，运行时还开箱即用地内置了兼容 OpenAI 接口规范的服务端以及轻量级 WebSocket 服务端。生态整合方面，Phonon 能与 Hugging Face Transformers、MLX-Audio、Ollama 以及 LM Studio 等主流框架无缝协同。

> The official runtime (`xn-ptts`) is available under an MIT or Apache-2.0 license, supporting Rust, Python (`pip install ptts`), Swift, C, C++, and web browsers via `phonon-tts`. It also includes out-of-the-box support for an OpenAI-compatible server and a WebSocket server. Phonon integrates smoothly with Transformers, MLX-Audio, Ollama, and LM Studio.

---

## 总结与核心看点

> ## Key Takeaways

* **轻巧高效的开源利器**：**Phonon 31m** 提供了一个仅 31M 参数量的超轻量纯英语文本转语音模型，权重仅 64.5 MB，采用商业友好的 Apache 2.0 协议开源；
* **复杂长尾文本精准无误**：在包含缩写、数字及邮箱等复杂现实场景文本中表现极其稳健，单词错误率 (WER) 仅为 1.70%；
* **突破性的端侧超低延迟**：在现代消费级标准 CPU 上能够达成 7 毫秒以内的极速首包音频输出，并可在树莓派 5 等算力受限设备上流畅稳定运行；
* **多语种能力延展**：同步推出了覆盖 5 种欧洲语言的 40M 多语种版本，供学术研究与非商业应用探索。

> * **Phonon 31m** offers an efficient, Apache 2.0-licensed 31M parameter English TTS model weighing just 64.5 MB.
> * Delivers robust accuracy with a 1.70% WER on difficult text inputs.
> * Unlocks ultra-low latency processing, achieving first audio in under 7 ms on modern consumer CPUs and running seamlessly on resource-constrained hardware like the Raspberry Pi 5.
> * Multilingual 40m counterparts are available under non-commercial licensing terms.

---

欢迎查阅官方资源了解更多详情：[技术博客 (Technical Blog)](https://gradium.ai/blog/release-phonon-open-weight) | [模型主页 (Model Card)](https://huggingface.co/gradium/phonon-31m-en) | [GitHub 运行时代码库 (GitHub Runtime)](https://github.com/gradium-ai/xn-ptts) | [高难度基准数据集 (Hard-Sentence Dataset)](https://huggingface.co/datasets/gradium/tts-hard-sentences-202610)。

> *Check out the [Technical Blog](https://gradium.ai/blog/release-phonon-open-weight), [Model Card](https://huggingface.co/gradium/phonon-31m-en), [GitHub Runtime](https://github.com/gradium-ai/xn-ptts), and [Hard-Sentence Dataset](https://huggingface.co/datasets/gradium/tts-hard-sentences-202610).*
