---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-11
hide:
- navigation
tags:
- NVIDIA
- Magpie TTS
- 语音AI
- 低延迟
- 多语言
title: 构建低延迟多语言语音智能体：NVIDIA Magpie TTS 带来开源权重与全面部署控制
---
### 文章背景与核心概要
在实时对话式人工智能中，低延迟对于维持自然交互至关重要。NVIDIA 推出的 Magpie Multilingual TTS 是一款拥有 364M 参数的开源权重文本转语音（TTS）模型，专为高性能、低延迟部署而设计。该模型支持 12 种语言（包括新加入的现代标准阿拉伯语、韩语和巴西葡萄牙语），并利用了帧堆叠（frame stacking）和局域 Transformer（local transformers）等先进的架构改进，在 NVIDIA B200 硬件上实现了低至 32 毫秒的首音频时间（TTFA）。

结合生产就绪的 NVIDIA NIM 和 NVIDIA NeMo 框架，Magpie 为开发者提供了完整的基建控制权、特定领域的定制能力以及企业级的隐私保护，助力构建稳健的多语言语音智能体。本文详细介绍了其架构优势、延迟性能基准以及如何利用开源生态构建完整的语音应用。

---

[![newsletter-speech-ai-customer](./images/097e56c95ebd.png)](./images/097e56c95ebd.png)

Every voice interaction has a latency budget.

> 每次语音交互都有一个延迟预算。

By the time a user hears your application respond, you've already spent precious milliseconds capturing audio, transcribing speech, running an LLM, retrieving context, and generating a response. Text-to-speech (TTS) is the final step — and the one users notice most. If speech generation is slow, the whole experience feels slow.

> 当用户听到您的应用程序做出响应时，您已经花费了宝贵的毫秒来捕获音频、转录语音、运行大语言模型（LLM）、检索上下文并生成响应。文本转语音（TTS）是最后一步——也是用户最容易察觉的一步。如果语音生成速度慢，整个体验就会显得迟钝。

The more of that pipeline you can run and tune yourself, the more of the latency budget you get back.

> 您能够自己运行和调优的流水线环节越多，您夺回的延迟预算就越多。

Voice AI is moving fast. Integrated speech models offer simplicity — one API call, audio in, audio out — but they trade the ability to fine-tune each component for your domain, swap in better models as they ship, enforce data residency, and understand exactly where latency is coming from. For more control, a cascaded architecture — purpose-built ASR, TTS, and LLM components running together — keeps each layer independently tunable and deployable on infrastructure you own.

> 语音 AI 正在快速发展。集成式语音模型提供了极大的便利性——只需一次 API 调用，输入音频，输出音频——但它们牺牲了针对您的领域微调每个组件的能力、在更好模型发布时进行替换的能力、执行数据驻留合规的能力，以及准确了解延迟来源的能力。为了获得更多控制权，采用级联架构（由专为特定任务构建的 ASR、TTS 和 LLM 组件共同运行）可以保持每一层都能独立调优，并可部署在您自己拥有的基础设施上。

[NVIDIA Magpie Multilingual TTS](https://huggingface.co/nvidia/magpie_tts_multilingual_357m) is built for that. With open weights, [production-ready NVIDIA NIM](https://build.nvidia.com/nvidia/magpie-tts-multilingual), and support for 12 languages, you can deploy multilingual speech inside your own infrastructure, optimize latency for your workload, and customize the model for your domain — end to end, in your own environment.

> [NVIDIA Magpie 多语言 TTS](https://huggingface.co/nvidia/magpie_tts_multilingual_357m) 正为此而生。借助开源权重、[生产就绪的 NVIDIA NIM](https://build.nvidia.com/nvidia/magpie-tts-multilingual) 以及对 12 种语言的支持，您可以在自己的基础设施内部署多语言语音，针对您的工作负载优化延迟，并为您的领域定制模型——在您自己的环境中实现端到端的掌控。

The latest release expands multilingual coverage with Modern Standard Arabic, Korean, and Brazilian Portuguese, while improving quality across many existing languages through updated training data and model improvements.

> 最新版本通过引入现代标准阿拉伯语、韩语和巴西葡萄牙语扩展了多语言覆盖范围，同时通过更新的训练数据和模型改进，提升了许多现有语言的语音质量。

Whether you're building customer support agents, healthcare assistants, enterprise copilots, translation systems, or conversational AI applications, Magpie provides an open foundation for production voice AI.

> 无论您是在构建客户支持智能体、医疗保健助手、企业级 Copilot、翻译系统还是对话式 AI 应用，Magpie 都为生产级语音 AI 提供了一个开放的基础。

---

## Voice AI Is Becoming Multilingual by Default

> 语音 AI 正默认走向多语言化

Today's voice applications don't serve a single language.

> 如今的语音应用不再只服务于单一语言。

Global customer support, enterprise assistants, healthcare documentation, retail automation, and translation workflows increasingly require natural conversations across multiple languages — all while maintaining low latency.

> 全球客户支持、企业助手、医疗文档、零售自动化和翻译工作流越来越需要在保持低延迟的同时，实现多语言之间的自然对话。

Supporting more languages is only part of the challenge. Developers also need the ability to:

> 支持更多语言只是挑战的一部分。开发者还需要具备以下能力：

* Deploy where their data lives  
* Meet enterprise privacy requirements  
* Customize pronunciation and voices  
* Predict latency under production workloads  
* Scale on their own infrastructure

> * 在数据所在地进行部署  
> * 满足企业隐私要求  
> * 定制发音和声音  
> * 预测生产工作负载下的延迟  
> * 在自己的基础设施上进行扩展

**Open models change what's possible on every one of these.**

> **开源模型改变了上述每一项任务的可能性。**

---

## One Open Model, Twelve Languages

> 一个开源模型，十二种语言

Magpie TTS Multilingual is a 364M-parameter open-weights model supporting:

> Magpie TTS 多语言版是一个拥有 3.64 亿参数的开源权重模型，支持：

**English · Spanish · French · German · Italian · Vietnamese · Mandarin · Hindi · Japanese · Modern Standard Arabic (new) · Korean (new) · Brazilian Portuguese (new)**

> **英语 · 西班牙语 · 法语 · 德语 · 意大利语 · 越南语 · 普通话 · 印地语 · 日语 · 现代标准阿拉伯语（新） · 韩语（新） · 巴西葡萄牙语（新）**

Each language includes male and female speaker voices through a shared multilingual speaker representation.

> 通过共享的多语言说话人表征，每种语言均包含男性和女性说话人的声音。

This release also improves multilingual flexibility with expanded code-switching support for Hindi and Japanese, enabled through IPA grapheme-to-phoneme processing and custom pronunciation dictionaries — making it easier to accurately pronounce names, technical terminology, and mixed-language content.

> 此版本还通过 IPA（国际音标）字素到音素处理以及自定义发音词典，增强了对印地语和日语的代码混合（Code-switching）支持，从而提高了多语言的灵活性——这使得准确发音人名、技术术语和混合语言内容变得更加容易。

Instead of maintaining separate TTS models for different regions, developers can build multilingual applications on a single open foundation.

> 开发者无需为不同地区维护独立的 TTS 模型，而是可以在单一的开放基础之上构建多语言应用程序。

---

## The Latency Your Users Actually Notice

> 用户真正能察觉到的延迟

In conversational AI, text-to-speech is the final stage before users hear a response. That makes Time to First Audio (TTFA) — the delay between speech generation beginning and the first audio reaching the user — one of the most important latency metrics in a voice pipeline.

> 在对话式 AI 中，文本转语音是用户听到响应前的最后阶段。这使得首音频时间（TTFA，即语音生成开始与第一段音频送达用户之间的延迟）成为语音流水线中最关键的延迟指标之一。

Because Magpie TTS can be deployed inside your own environment, the latency you measure is the server-side latency you actually control, with no managed-service round-trip in the number.

> 由于 Magpie TTS 可以部署在您自己的环境中，您所测得的延迟就是您实际掌控的服务端延迟，其中不包含托管服务的网络往返开销。

| GPU | 1-stream TTFA | 1-stream RTFX | 64-stream TTFA | 64-stream RTFX |
| :---| :---| :---| :---| :---|
| **B200** | 32 ms | 12.1× | 239 ms | 319.81× |
| **H100** | 47 ms | 14.7× | 275 ms | 290.79× |
| **DGX Spark** | 53 ms | 9.8× | 962 ms | 75.88× |
| **A100** | 79 ms | 12.2× | 395 ms | 197× |

*Source: [NVIDIA TTS NIM Performance documentation](https://docs.nvidia.com/nim/speech/26.07.0/reference/performances/tts/performance.html) (v26.07), average of three trials, on-prem.*  
*TTFA = latency to first audio; RTFX = throughput as a multiple of real time.*

> *来源：[NVIDIA TTS NIM 性能文档](https://docs.nvidia.com/nim/speech/26.07.0/reference/performances/tts/performance.html)（v26.07），本地部署（on-prem）三次试验的平均值。*  
> *TTFA = 首音频延迟；RTFX = 以实时倍数表示的吞吐量。*

At 32ms on B200, Magpie's TTFA leaves the rest of the latency budget for ASR and LLM processing — keeping total end-to-end latency within the sub-200ms window natural conversation requires. Across NVIDIA GPUs, Magpie delivers first audio in 32–79ms on a single stream. At 64 concurrent streams, B200 reaches 239ms TTFA while delivering throughput at 320× real time — generating audio more than 300 times faster than it plays back, even under concurrent load.

> 在 B200 上达到 32ms 时，Magpie 的 TTFA 为 ASR 和 LLM 处理留出了充足的延迟预算——将总端到端延迟保持在自然对话所需的 200ms 以下窗口内。在各种 NVIDIA GPU 上，Magpie 在单流下可在 32–79ms 内输出第一段音频。在 64 个并发流下，B200 的 TTFA 达到 239ms，同时提供 320 倍实时吞吐量——即使在并发负载下，其音频生成速度也比播放速度快 300 多倍。

The table above shows Magpie served as the NVIDIA NIM, measured on-prem — the optimized container running on your own GPU. The open Hugging Face checkpoint is the same model and your path for research and fine-tuning; the NIM is the tuned serving stack that produces these production latencies. Both run on hardware you control.

> 上表展示了作为 NVIDIA NIM 提供服务的 Magpie，在本地进行测量的结果——即运行在您自己的 GPU 上的优化容器。Hugging Face 上的开源检查点是同一个模型，也是您进行研究和微调的途径；而 NIM 是能够实现这些生产级低延迟的调优推理栈。两者均运行在您控制的硬件上。

Because the model runs on your own infrastructure, you can benchmark performance directly, tune it for your deployment, and scale according to your workload. For real-time voice agents, that's the difference between conversations that feel responsive and conversations that feel delayed.

> 由于模型运行在您自己的基础设施上，您可以直接进行性能基准测试、针对部署进行调优，并根据工作负载进行扩展。对于实时语音智能体而言，这就是对话感觉灵敏与感觉迟钝之间的本质区别。

---

## Optimized for Real-Time Speech Generation

> 针对实时语音生成进行优化

Low latency isn't accidental. Magpie introduces two complementary architectural improvements that reduce inference time while maintaining speech quality.

> 低延迟并非偶然。Magpie 引入了两项互补的架构改进，在保持语音质量的同时缩短了推理时间。

* **Frame stacking:** The decoder predicts two audio frames during each decoding step rather than one. This cuts the number of decoder iterations in half, shortening generation time and improving throughput.
* **Local transformer:** Frame stacking alone would reduce audio quality by introducing dependencies between simultaneously generated codebook tokens. The local transformer models those dependencies and refines the generated audio, recovering the quality that frame stacking would otherwise sacrifice.

> * **帧堆叠（Frame stacking）：** 解码器在每个解码步骤中预测两个音频帧，而不是一个。这使解码器的迭代次数减少了一半，缩短了生成时间并提高了吞吐量。
> * **局域 Transformer（Local transformer）：** 单独使用帧堆叠会在同时生成的码本（codebook）标记之间引入依赖关系，从而降低音频质量。局域 Transformer 对这些依赖关系进行建模并精炼生成的音频，从而恢复了帧堆叠原本可能牺牲的质量。

Together, these techniques deliver both faster generation and natural speech synthesis. The architecture is described in [Frame-Stacked Local Transformers for Efficient Multi-Codebook Speech Generation](https://arxiv.org/abs/2509.19592) (ICASSP 2026).

> 这些技术共同实现了更快的生成速度和更自然的语音合成。该架构已在论文[《用于高效多码本语音生成的帧堆叠局域 Transformer》](https://arxiv.org/abs/2509.19592)（ICASSP 2026）中进行了描述。

---

## Faster Doesn't Matter If It Doesn't Sound Natural

> 如果听起来不自然，速度快也毫无意义

This release doesn't only add languages — it also improves synthesis quality across many existing ones. Compared to the previous release, Magpie shows reduced character error rates (CER) and higher speaker similarity (SSIM) on several languages, with the clearest gains on French and Spanish:

> 此版本不仅增加了语言支持，还提升了许多现有语言的合成质量。与上一版本相比，Magpie 在几种语言上的字符错误率（CER）有所降低，说话人相似度（SSIM）有所提高，其中在法语和西班牙语上的提升最为明显：

| Language | CER (prev) | CER (this release) | SSIM (prev) | SSIM (this release) |
| :---| :---| :---| :---| :---|
| **French** | 2.70% | 1.54% | 0.703 | 0.747 |
| **Spanish** | 1.14% | 0.60% | 0.715 | 0.793 |
| **German** | 0.66% | 0.80% | 0.626 | 0.742 |

*Source: [Magpie TTS Multilingual model card](https://huggingface.co/nvidia/magpie_tts_multilingual_357m). CER lower is better; SSIM higher is better.*

> *来源：[Magpie TTS 多语言模型卡片](https://huggingface.co/nvidia/magpie_tts_multilingual_357m)。CER 越低越好；SSIM 越高越好。*

The newly added Arabic (1.62% CER), Korean (2.69%), and Brazilian Portuguese (2.91%) models establish baseline quality for future improvements.

> 新增的阿拉伯语（1.62% CER）、韩语（2.69%）和巴西葡萄牙语（2.91%）模型为未来的改进奠定了基准质量。

While objective metrics help measure progress, speech quality is ultimately perceptual. You can hear the difference yourself on [NVIDIA Build](https://build.nvidia.com/nvidia/magpie-tts-multilingual) or the [Hugging Face demo](https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo).

> 尽管客观指标有助于衡量进展，但语音质量归根结底是主观感知的。您可以在 [NVIDIA Build](https://build.nvidia.com/nvidia/magpie-tts-multilingual) 或 [Hugging Face 演示页面](https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo)上亲自聆听这种差异。

---

## Why Open Weights Matter

> 为什么开源权重至关重要

Latency you can measure is useful. Latency you can control is even better.

> 可以度量的延迟很有用。能够掌控的延迟则更好。

Open weights give developers capabilities that come from owning the deployment. With Magpie you can:

> 开源权重赋予了开发者由掌控部署所带来的各项强大能力。借助 Magpie，您可以：

* **Deploy on infrastructure you control** — run entirely within your own infrastructure, including private or air-gapped environments.  
* **Own your latency budget** — no managed-service round-trip, and you optimize directly for your hardware and workload.  
* **Customize pronunciation and voices** — fine-tune with NeMo for your own brand, domain vocabulary, or speaker data.  
* **Scale on your own terms** — optimize the serving stack for your infrastructure and workload.
* **Maintain enterprise control** — keep sensitive conversations and customer data inside your environment.

> * **在您控制的基础设施上部署** —— 完全在您自己的基础设施（包括私有或气隙隔离环境）内运行。  
> * **掌控您的延迟预算** —— 没有托管服务的网络往返开销，您可以直接针对您的硬件和工作负载进行优化。  
> * **定制发音和声音** —— 使用 NeMo 针对您的品牌、领域词汇或说话人数据进行微调。  
> * **按需扩展** —— 为您的基础设施和工作负载优化推理服务栈。
> * **维持企业级控制** —— 将敏感对话和客户数据保留在您的环境中。

For enterprises building production voice AI, this control over deployment, performance, and customization is often what matters most.

> 对于构建生产级语音 AI 的企业而言，这种对部署、性能和定制化的控制权通常是最核心的诉求。

---

## Build Complete Voice Agents — Not Just Better Speech

> 构建完整的语音智能体 —— 不仅仅是更动听的语音

Voice AI in production is a system of models, not a single one. Magpie TTS is part of the [NVIDIA Nemotron Voice Agent Developer Example](https://build.nvidia.com/nvidia/nemotron-voice-agent), a reference implementation showing how purpose-built speech, language, and reasoning models work together as a coordinated system — so you can build always-on voice agents, not just better-sounding speech.

> 生产环境中的语音 AI 是一个模型系统，而非单一模型。Magpie TTS 是 [NVIDIA Nemotron 语音智能体开发者示例](https://build.nvidia.com/nvidia/nemotron-voice-agent)的一部分，该参考实现展示了专用的语音、语言和推理模型如何作为协调系统协同工作——从而让您能够构建全天候运行的语音智能体，而不仅仅是生成声音更好听的语音。

Developers can combine:

> 开发者可以组合使用：

* Nemotron Speech for streaming speech recognition  
* Magpie TTS for natural multilingual speech synthesis  
* Nemotron language and multimodal models for reasoning, tool calling, and multimodal understanding  
* NVIDIA NIM for GPU-optimized, production-ready inference microservices  
* NeMo for customization and fine-tuning

> * 用于流式语音识别的 Nemotron Speech  
> * 用于自然多语言语音合成的 Magpie TTS  
> * 用于推理、工具调用和多模态理解的 Nemotron 语言与多模态模型  
> * 用于 GPU 优化、生产就绪推理微服务的 NVIDIA NIM  
> * 用于定制和微调的 NeMo

The Nemotron Voice Agent developer example provides an end-to-end reference implementation that developers can clone, customize, and deploy in hours. It includes production patterns for:

> Nemotron 语音智能体开发者示例提供了一个端到端的参考实现，开发者可以在几小时内对其进行克隆、定制和部署。它包含以下生产级模式：

* Real-time interruptible (barge-in) conversations  
* Multimodal voice agents with vision understanding  
* Multi-agent orchestration and tool calling  
* Multilingual voice interactions  
* Sub-second end-to-end latency using NVIDIA NIM

> * 实时可打断（Barge-in）对话  
> * 具备视觉理解能力的多模态语音智能体  
> * 多智能体编排与工具调用  
> * 多语言语音交互  
> * 使用 NVIDIA NIM 实现亚秒级端到端延迟

Rather than assembling individual components from scratch, developers can start from a complete reference architecture and adapt it to their own applications.

> 开发者无需从头开始组装各个组件，而是可以从完整的参考架构出发，将其适配到自己的应用程序中。

---

## Get Started

> 快速入门

### Try the Model
* [NVIDIA Build](https://build.nvidia.com/nvidia/magpie-tts-multilingual) 
* [Hugging Face demo](https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo)

> ### 体验模型
> * [NVIDIA Build](https://build.nvidia.com/nvidia/magpie-tts-multilingual) 
> * [Hugging Face 演示](https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo)

### Deploy to Production
* [NVIDIA Magpie Multilingual TTS NIM](https://build.nvidia.com/nvidia/magpie-tts-multilingual) — optimized inference containers

> ### 部署到生产环境
> * [NVIDIA Magpie 多语言 TTS NIM](https://build.nvidia.com/nvidia/magpie-tts-multilingual) —— 优化的推理容器

### Customize for Your Domain
* [NVIDIA NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) — fine-tuning and training

> ### 针对您的领域进行定制
> * [NVIDIA NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) —— 微调与训练

### Build Complete Voice Agents
* [NVIDIA voice-agent-examples](https://github.com/NVIDIA-AI-Blueprints/nemotron-voice-agent)

> ### 构建完整的语音智能体
> * [NVIDIA 语音智能体示例](https://github.com/NVIDIA-AI-Blueprints/nemotron-voice-agent)

### Open Weights and License
* [Model card on Hugging Face](https://huggingface.co/nvidia/magpie_tts_multilingual_357m) — open weights under the NVIDIA Open Model License.

> ### 开源权重与许可
> * [Hugging Face 上的模型卡片](https://huggingface.co/nvidia/magpie_tts_multilingual_357m) —— 遵循 NVIDIA 开放模型许可证（NVIDIA Open Model License）的开源权重。

---

### Recommended Inference Configuration

> ### 推荐的推理配置

```py
cfg_scale = 2.5          # classifier-free guidance — raise for tighter text adherence
temperature = 0.6
top_k = 80
apply_attention_prior = True
prior_epsilon = 0.1
```