---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 多模态大模型
- 机器翻译
- 语音翻译
- 端到端架构
- 模块化融合
title: OmniFusion：基于模块化融合的端到端多语言多模态同步翻译
---
### 文章背景与核心概要
传统的纯文本翻译大语言模型（LLM）虽然具备出色的语言覆盖率和翻译质量，但在处理语音翻译时，通常依赖于“自动语音识别+文本翻译”的级联管道。这种传统方式不仅引入了额外的延迟（这在同传场景中尤为致命），还无法利用图像等多模态上下文来辅助语义消歧。另一方面，预训练的多模态基础模型（MMFM）虽然拥有强大的感知与推理能力，但往往缺乏专业翻译大模型所需的广泛多语言覆盖与精细化翻译性能。

为了弥合多模态基础模型与专业翻译大模型之间的鸿沟，本文提出了 OmniFusion——一个旨在实现同时多语言多模态翻译的端到端框架。该框架创新性地采用了模块化融合策略，将预训练 MMFM 多层的隐藏状态与翻译 LLM 进行连接，从而支持语音转文本、语音图像联合转文本以及图文转文本等多模态翻译任务的联合端到端训练。基于 Omni 2.5-7B 和 SeedX PPO-7B 构建的实验表明，OmniFusion 不仅能有效利用音视频输入，还能在同传翻译（SimulST）中将延迟降低 1 秒，并显著提升整体翻译质量。

---

# OmniFusion: Simultaneous Multilingual Multimodal Translations via Modular Fusion

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

## Summary

> **OmniFusion** is an end-to-end framework designed to bridge the gap between Multimodal Foundation Models (MMFMs) and specialized translation Large Language Models (LLMs). While traditional text-only translation LLMs offer strong language coverage, they rely on cascaded pipelines (automatic speech recognition followed by translation) for speech translation, introducing latency and preventing the use of helpful multimodal context like images. Conversely, MMFMs possess great perception skills but lack dedicated translation performance. 
> 
> By utilizing a novel modular fusion strategy that connects hidden states from multiple layers of a pretrained MMFM to a translation LLM, OmniFusion (built using Omni 2.5-7B and SeedX PPO-7B) enables joint end-to-end training for speech-to-text, speech-and-image-to-text, and text-and-image-to-text tasks. Experiments show that it reduces simultaneous speech translation (SimulST) latency by 1 second while boosting overall translation quality.

---

## Paper Metadata / 论文元数据

* **arXiv Identifier:** [arXiv:2512.00234 [cs.CL]](https://arxiv.org/abs/2512.00234) *(v3)*
* **DOI:** [10.48550/arXiv.2512.00234](https://doi.org/10.48550/arXiv.2512.00234)
* **Authors / 作者:** Sai Koneru, Matthias Huck, Jan Niehues
* **Primary Subject / 主学科:** Computation and Language (`cs.CL`)
* **Secondary Subjects / 次学科:** Artificial Intelligence (`cs.AI`)
* **Conference/Venue / 会议与期刊:** EMNLP 2026 Findings
* **Submitted / 提交日期:** 28 November 2025 (Last revised: 28 August 2026)

---

## Abstract / 摘要

> There has been significant progress in open-source text-only translation large language models (LLMs) with better language coverage and quality. However, these models can be only used in cascaded pipelines for speech translation (ST), performing automatic speech recognition first followed by translation. This introduces additional latency, which is particularly critical in simultaneous ST (SimulST), and prevents the model from exploiting multimodal context, such as images, which can aid disambiguation. Pretrained multimodal foundation models (MMFMs) already possess strong perception and reasoning capabilities across multiple modalities, but generally lack the multilingual coverage and specialized translation performance of dedicated translation LLMs. 

开源纯文本翻译大语言模型（LLM）近年来在语言覆盖率和翻译质量上取得了显著进展。然而，这些模型在用于语音翻译（ST）时只能采用级联管道，即先进行自动语音识别，然后再进行翻译。这引入了额外的延迟（在同传翻译 SimulST 中尤为关键），并阻碍了模型利用图像等多模态上下文来协助消歧。预训练的多模态基础模型（MMFMs）虽然已经在多模态上具备强大的感知和推理能力，但通常缺乏专用翻译 LLM 的多语言覆盖能力和专业翻译性能。

> To build an effective multimodal translation system, we propose an end-to-end approach that fuses MMFMs with translation LLMs. We introduce a novel fusion strategy that connects hidden states from multiple layers of a pretrained MMFM to a translation LLM, enabling joint end-to-end training. The resulting model, OmniFusion, built on Omni 2.5-7B as the MMFM and SeedX PPO-7B as the translation LLM, can perform speech-to-text, speech-and-image-to-text, and text-and-image-to-text translation. Experiments demonstrate that OmniFusion effectively leverages both audio and visual inputs, achieves a 1-second latency reduction in SimulST compared to cascaded pipelines and also improves the overall translation quality.

为了构建一个高效的多模态翻译系统，我们提出了一种将 MMFM 与翻译 LLM 相结合的端到端方法。我们引入了一种创新的融合策略，将预训练 MMFM 多个层的隐藏状态连接到翻译 LLM 中，从而实现联合端到端训练。由此产生的模型 OmniFusion 以 Omni 2.5-7B 作为 MMFM、SeedX PPO-7B 作为翻译 LLM，能够执行语音转文本、语音图像联合转文本以及图文转文本翻译。实验表明，OmniFusion 有效利用了音频和视觉输入，与级联管道相比，在同传翻译中实现了 1 秒的延迟降低，同时提升了整体翻译质量。

---

## Resources & Links / 资源与链接

* **Full-Text PDF / 全文 PDF:** [View PDF](https://arxiv.org/pdf/2512.00234)
* **Experimental HTML / 实验性 HTML 版本:** [arXiv HTML Version](https://arxiv.org/html/2512.00234v3)
* **Source Code / 源代码库:** [GitHub Repository](https://github.com/saikoneru/OmniFusion)
* **License / 许可协议:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)