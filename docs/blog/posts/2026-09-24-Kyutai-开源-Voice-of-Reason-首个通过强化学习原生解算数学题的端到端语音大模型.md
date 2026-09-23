---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-24
hide:
- navigation
tags:
- Kyutai
- Voice of Reason
- 端到端语音模型
- 强化学习
- GRPO
- 数学推理
title: Kyutai 开源 Voice of Reason：首个通过强化学习原生解算数学题的端到端语音大模型
---
# Kyutai 开源 Voice of Reason：首个通过强化学习原生解算数学题的端到端语音大模型

> # Kyutai Releases Voice of Reason: A Speech-Native Model that Solves Spoken Math with Reinforcement Learning

### 文章背景与核心概要

长期以来，传统语音交互主要依赖“语音转文字 $\rightarrow$ 文本大模型 $\rightarrow$ 文字转语音”的级联架构，不仅通信时延高，还会损失语调与情绪等副语言特征；而新一代原生端到端语音模型虽然能实现无缝实时对话，却因必须按节律持续输出音频流，在面对复杂数学多步推理任务时举步维艰。为攻克这一核心技术难题，开源人工智能前沿机构 Kyutai 正式开源了 **Voice of Reason** 系列模型，这是业界首个通过强化学习 (Reinforcement Learning, RL) 原生解算口语数学题的端到端语音大模型。该方案基于开源的 `GLM-4-Voice-9B`，巧妙融合高质量监督微调 (Supervised Fine-Tuning, SFT) 与类 GRPO 的强化学习策略，彻底摆脱了中间文本转录与外部文本大语言模型 (Large Language Model, LLM) 的依赖。实验评测显示，该模型在口语 GSM8K 数学基准测试上的解题准确率从基线的 27.3% 飙升至 77.1%，同时完美保持了语音的高自然度与流畅度。目前两款 9B 参数的 BF16 权重已全面开源，单张 H100 GPU 即可实现低成本私有化部署，为打造真正具备深度逻辑思考能力的原生实时语音交互智能体铺平了道路。

---

## 核心速览与内容概要

> ## TL;DR / Summary

人工智能研究机构 Kyutai 正式发布了开源权重模型 **Voice of Reason**。该项目基于开源模型 `GLM-4-Voice-9B` 打造，包含两款能够直接在语音交互中“边说边想”解算数学难题的原生端到端语音模型。通过将监督微调 (Supervised Fine-Tuning, SFT) 与强化学习 (Reinforcement Learning, RL) 有机结合——全程无需任何中间文本转录或外部文本大语言模型——新模型将口语版 GSM8K 数学评测基准的准确率从基准的 **27.3% 跨越式提升至 77.1%**。目前，两款 BF16 精度的模型权重文件均已在 Hugging Face 开放下载，单张 H100 GPU 即可完成本地私有化部署。

> Kyutai has released **Voice of Reason**, a pair of open-weight speech-to-speech models built on top of `GLM-4-Voice-9B` that solve math problems natively out loud. By combining Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL)—without any intermediate transcription steps or text LLMs—the models dramatically boost spoken GSM8K accuracy from a baseline of **27.3% up to 77.1%**. Both BF16 checkpoints are available on Hugging Face and can be self-hosted on a single H100 GPU.

---

## 部署要求与开源资源

> ## Deployment & Availability

* **硬件要求**：两款 BF16 精度权重均可完整装入单张 H100 GPU。运行需依赖 [GLM-4-Voice 代码仓库](https://github.com/THUDM/GLM-4-Voice) 提供的语音编解码器 (Speech Tokenizer & Decoder) 。
* **开源协议**：沿用 GLM-4-Voice 的开源许可证。
* **模型权重文件 (Checkpoints) **：
  * [`glm-4-voice-of-reason-9b`](https://hf.co/kyutai/glm-4-voice-of-reason-9b)
  * [`glm-4-voice-of-reason-stitch-9b`](https://hf.co/kyutai/glm-4-voice-of-reason-stitch-9b)

> * **Hardware Requirements:** Both BF16 checkpoints fit on a single H100 GPU. Requires the [GLM-4-Voice repo](https://github.com/THUDM/GLM-4-Voice) for its speech tokenizer and decoder.
> * **License:** Inherits the GLM-4-Voice license. 
> * **Checkpoints:** 
>   * [`glm-4-voice-of-reason-9b`](https://hf.co/kyutai/glm-4-voice-of-reason-9b)
>   * [`glm-4-voice-of-reason-stitch-9b`](https://hf.co/kyutai/glm-4-voice-of-reason-stitch-9b)

---

## 为什么语音模型在数学推理上普遍表现不佳？

> ## Why Speech Models Lag on Math

在复杂推理任务中，传统的级联流水线架构 (即语音转文字 $\rightarrow$ 文本大语言模型 $\rightarrow$ 文字转语音) 依然占据主导地位。然而，各个独立阶段不仅会不断累加响应延迟，还会丢失诸如语调、重音等至关重要的副语言信息 (Paralinguistic Cues) 。

> Traditional cascaded pipelines (speech-to-text $\rightarrow$ text LLM $\rightarrow$ text-to-speech) still dominate in reasoning tasks. However, each stage introduces latency and drops crucial paralinguistic cues like tone. 

相比之下，原生语音模型必须以恒定的时间间隔持续吐出音频，以维持实时的人机对话互动感，这极大地限制了模型在幕后用于深度思考的“隐藏推理 Token”数量。在基准表现上，原始版本的 `GLM-4-Voice` 在 [GSM8K](https://arxiv.org/abs/2110.14168) 上的得分仅为 27.3%；尽管此前的 [STITCH](https://arxiv.org/abs/2507.15375) 方法通过引入推理块机制将得分提升到了 58.7%，但 Voice of Reason 真正开创了先河——它标志着强化学习首次在原生语音模型的数学逻辑推理中获得成功应用。

> Speech-native models must emit audio at regular intervals to maintain interactivity, strictly limiting the hidden reasoning tokens they can afford. While the base `GLM-4-Voice` scores 27.3% on [GSM8K](https://arxiv.org/abs/2110.14168), and the earlier [STITCH](https://arxiv.org/abs/2507.15375) method raised that to 58.7% using reasoning chunks, Voice of Reason marks the first successful application of Reinforcement Learning to math reasoning in speech-native models.

---

## 模型训练机制详解

> ## How the Training Works

在底层输出结构上，`GLM-4-Voice` 采用了序列交替机制：按固定节律**生成 13 个文本 Token，紧接着生成 26 个音频 Token**，循环往复。

> `GLM-4-Voice` interleaves its outputs sequentially: **13 text tokens followed by 26 audio tokens**, repeating.

1. **第一阶段：监督微调 (Stage-1 SFT) **：模型在来自 [Orca-Math](https://arxiv.org/abs/2402.14830) 的 150,616 道题目上进行微调。所有题目均使用 Qwen3-235B 进行了口语化重写，并借助 Kyutai 自研的 [DSM TTS](https://arxiv.org/abs/2509.08753) 系统合成为多种说话风格的口语音频。仅靠监督微调阶段，模型的数学解题准确率就直接从 27.3% 攀升至 61.7%。
2. **第二阶段：强化学习 (Stage-2 RL) **：对于每一个口语数学问题，模型在采样温度 0.9 下采样生成 4 个回答候选。裁判模型 (`Qwen3-235B-A22B-2507`) 在盲审机制下 (即不依赖标准参考答案) 对解码后的文本给出 0 或 1 的二元奖励 (Binary Reward) 。算法采用与 [GRPO](https://arxiv.org/abs/2402.03300) 相关的 REINFORCE 目标函数计算群组相对奖励 (Group-Relative Rewards) ，并移除了 PPO 中的截断裁剪操作与 KL 散度正则化约束。强化学习训练共调用了 16 张 H100 GPU，历经 1,500 次 RL 梯度更新完成训练。

> 1. **Stage-1 SFT:** Trained on 150,616 problems from [Orca-Math](https://arxiv.org/abs/2402.14830). Problems were rewritten for speech using Qwen3-235B and voiced in various styles using Kyutai's [DSM TTS](https://arxiv.org/abs/2509.08753). SFT alone lifts accuracy from 27.3% to 61.7%.
> 2. **Stage-2 RL:** For each spoken question, the model samples 4 replies at temperature 0.9. A judge (`Qwen3-235B-A22B-2507`) scores the decoded text via a binary reward (blind to the reference answer). Rewards are group-relative using a REINFORCE objective related to [GRPO](https://arxiv.org/abs/2402.03300), while dropping PPO clipping and KL regularization. Training used 16 H100 GPUs for 1,500 RL updates.

### 关键架构与工程设计选择

> ### Critical Design Choices

* **采样温度校正 (Temperature Correction) **：在损失函数计算 log-softmax 之前，将 Logits 除以采样温度。消融实验证明，如果不进行这一温度校正，模型在 GSM8K 上的准确率会直接从 65.5% 暴跌至 12.3%。
* **音频 Token 聚合 (Audio-Token Merging) **：在每一个音频生成位置，将整个音频词表中的所有概率求和合并为一个统一的抽象 Token。损失函数只需验证下一个出现的 Token 是否为音频，无需强行预测每一个具体的音频 Token，从而大幅简化了语音强化学习的优化难度。

> * **Temperature Correction:** Logits are divided by the sampling temperature prior to the log-softmax in the loss function. Omitting this caused GSM8K accuracy to crash from 65.5% down to 12.3%.
> * **Audio-Token Merging:** At each audio position, all audio-vocabulary probabilities are summed into a single abstract token. The loss checks simply whether audio arrived next, avoiding the need to predict specific audio tokens.

---

## 正式发布的两个模型版本

> ## The 2 Released Checkpoints

* **`glm-4-voice-of-reason-9b`**：直接回答版本。不使用额外的隐藏推理 Token，解题时的所有演算与推导步骤均直接在语音中朗读出来。
* **`glm-4-voice-of-reason-stitch-9b`**：采用 Stitch 拼接机制的版本。在口语发音语段之间插入 100 个 Token 的无声隐式推理块。当模型播放前一段语音时，后续的推理块已经在后台并发生成，从而在增强深思熟虑能力的同时完全消除了额外延迟。

> * **`glm-4-voice-of-reason-9b`:** Answers directly without extra reasoning tokens; any step-by-step working is spoken aloud.
> * **`glm-4-voice-of-reason-stitch-9b`:** Inserts silent 100-token reasoning chunks between spoken blocks. Later chunks generate concurrently while earlier speech plays, preventing extra latency.

---

## 实验结果与基准评测

> ## Results & Benchmarks

| 模型 (Model) | 参数量 (Params) | GSM8K 准确率 (%) |
| :--- | :--- | :--- |
| PersonaPlex (全双工) | 8B | 3.2 |
| GLM-4-Voice | 9B | 27.3 |
| STITCH (Chiang 等人) | 9B | 58.7 |
| **Voice of Reason** | 9B | **65.5 ± 1.1** *(开源版本 70.3)* |
| **Voice of Reason (Stitch)** | 9B | **74.8 ± 1.1** *(开源版本 77.1)* |
| Qwen2.5-Omni (文本输出) | 7B | 84.7 |
| Qwen3-Omni (文本输出) | 30B | 94.6 |
| 级联架构 ASR-LLM-TTS-ASR | 31B LLM | 95.7 |

> | Model | Params | GSM8K (%) |
> | :--- | :--- | :--- |
> | PersonaPlex (full-duplex) | 8B | 3.2 |
> | GLM-4-Voice | 9B | 27.3 |
> | STITCH (Chiang et al.) | 9B | 58.7 |
> | **Voice of Reason** | 9B | **65.5 ± 1.1** *(70.3 released)* |
> | **Voice of Reason (Stitch)** | 9B | **74.8 ± 1.1** *(77.1 released)* |
> | Qwen2.5-Omni (text output) | 7B | 84.7 |
> | Qwen3-Omni (text output) | 30B | 94.6 |
> | Cascaded ASR-LLM-TTS-ASR | 31B LLM | 95.7 |

### 其他重要发现

> ### Other Findings

* **真实语音评测表现稳健**：当使用 [Qwen3-ASR-1.7B](https://arxiv.org/abs/2601.21337) 对实际生成的口语音频进行自动转录与判分时，Stitch 版本模型仍取得了 **72.0 ± 1.9%** 的出色准确率。
* **语音自然度完美保留**：经过强化学习迭代后，模型的语音自然度指标 (UTMOSv2) 得分几乎没有变化 (直接回答版从 4.067 微变至 4.069；Stitch 版从 4.174 微变至 4.164) 。
* **推理效率明显提升**：强化学习有效缩短了直接回答模型的平均语音回复时长 (从 41.9 秒下降至 36.4 秒) ，而 Stitch 版本的隐式推理 Token 消耗量基本保持稳定 (从 167 仅微增至 176) 。
* **极高的数据利用效率**：在仅使用 10% 监督微调数据的极限低数据量下，通过延长强化学习训练轮次，模型准确率仍可攀升至 58.5% (相比之下仅微调时仅为 43.9%) 。
* **通用通识知识的轻微回落**：在口语 TriviaQA 常识问答基准上，直接回答模型的得分从 40.6% 小幅微降至 34.0%，消融实验表明该现象主要源于全量 SFT 阶段带来的知识遗忘，而非强化学习本身所致。

> * **Robust in Real Speech:** Transcribed using [Qwen3-ASR-1.7B](https://arxiv.org/abs/2601.21337), the Stitch model achieves **72.0 ± 1.9%**.
> * **Naturalness Maintained:** UTMOSv2 scores remained virtually unchanged (4.067 to 4.069 for direct; 4.174 to 4.164 for Stitch) post-RL.
> * **Efficiency:** RL reduced the direct model’s average reply time from 41.9 to 36.4 seconds, while Stitch reasoning tokens barely shifted (167 to 176).
> * **Data Efficiency:** With only 10% of SFT data, an extended RL run hit 58.5% (compared to 43.9% for SFT alone).
> * **General Knowledge Dip:** Spoken TriviaQA dropped slightly from 40.6% to 34.0% for the direct model, attributed primarily to full-data SFT rather than RL.

---

## 核心亮点与技术总结

> ## Key Takeaways

* Kyutai 提出的强化学习框架成功将 `GLM-4-Voice` 在口语 GSM8K 数学基准上的解题表现从 27.3% 跨越式提升至 **77.1%**。
* 直接回答模型在无需任何隐藏推理 Token 的情况下达到了 **70.3%** 的高准确率，超越了此前依靠外接推理块的 STITCH 方法 (58.7%) 。
* 采样温度校正机制必不可少——一旦移除该机制，模型推理准确率将直接暴跌至 12.3%。
* 在强化学习深度优化之后，模型的口语发音自然度与韵律感染力依然完好无损。
* 两款 9B 参数规模的开源模型均已在 Hugging Face 发布，仅需单张 H100 GPU 即可实现本地私有化部署。

> * Kyutai’s RL framework successfully scales GLM-4-Voice performance from 27.3% to **77.1%** on spoken GSM8K.
> * The direct model reaches **70.3%** without reasoning tokens, outperforming STITCH's 58.7%.
> * Temperature correction is vital—removing it collapses model accuracy to 12.3%.
> * Speech naturalness is preserved after RL optimization.
> * Both 9B open-weight checkpoints are available on Hugging Face and self-hostable on a single H100.

---

欢迎查阅 [论文原文 (Paper)](https://arxiv.org/abs/2609.18677)、[直接回答版模型 (Direct Model)](https://hf.co/kyutai/glm-4-voice-of-reason-9b) 以及 [Stitch 架构版模型 (Stitch Model)](https://hf.co/kyutai/glm-4-voice-of-reason-stitch-9b)。

> *Check out the [Paper](https://arxiv.org/abs/2609.18677), the [Direct Model](https://hf.co/kyutai/glm-4-voice-of-reason-9b), and the [Stitch Model](https://hf.co/kyutai/glm-4-voice-of-reason-stitch-9b).*
