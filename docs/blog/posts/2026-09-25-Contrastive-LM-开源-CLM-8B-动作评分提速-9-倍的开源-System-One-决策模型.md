---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-09-25
hide:
  - navigation
tags:
  - CLM-8B
  - Contrastive-LM
  - AI 智能体
  - System One 模型
  - 动作评估
  - 开源模型
title: "Contrastive-LM 开源 CLM-8B：动作评分提速 9 倍的开源 System One 决策模型"
---

# Contrastive-LM 开源 CLM-8B：动作评分提速 9 倍的开源 System One 决策模型

> # Contrastive-LM Releases CLM-8B: An Open System One Model That Scores Agent Actions Up to 9× Faster Than Jev

### 文章背景与核心概要
在 AI 智能体 (AI Agent) 的决策循环中，传统大语言模型大多采用自回归机制逐字生成文本，这种“深思熟虑”的 System Two 慢思考架构在需要频繁评估候选动作时往往带来高昂的时间延迟。为此，Contrastive-LM 正式开源了首个对比语言模型 (Contrastive Language Model, CLM) —— **CLM-8B**，开创了专用于动作评估的开源 System One“快思考”决策模型新范式。该模型由冻结的 Qwen3-8B 骨干网络与仅 20M 参数的轻量投影头构成，彻底摆脱了冗长的文本生成，直接利用状态与动作嵌入向量的点积极速输出动作的概率分布。在零样本基准测试中，CLM-8B 的动作评分速度比闭源模型 Jev 提升高达 9 倍，候选动作扩展至 1,000 个时更可提速 13 倍，并在 DeepSWE 和 Terminal-Bench 2.1 编程基准上刷新了代码验证器的业界最前沿 (SOTA) 成绩。作为基于 Apache-2.0 许可证完全开源且仅需单张消费级 GPU 即可流畅部署的模型，CLM-8B 为高实时性智能体系统和代码验证流水线注入了兼具极致性能与开源可控的全新动力。

---

## 核心概述

> ## Summary

Contrastive-LM 正式发布了 **CLM-8B**，这是全新一类**对比语言模型 (Contrastive Language Model, CLM) **中的首个开源力作。与传统模型逐字生成文本不同，CLM 会对照当前环境状态对所有候选动作进行快速评估并直接输出概率，为 TypeSafe AI 旗下的 Jev 等闭源商业模型提供了一个高性能的开源替代方案。该模型基于 Apache-2.0 许可证开源发布，仅重 75 MB 的轻量级头部借助 vLLM 驱动的 Qwen3-8B 编码器，可在单张 NVIDIA GPU 上极其高效地运行。得益于深度优化的向量缓存机制与扎实的三阶段训练策略，CLM-8B 在零样本任务中的推理延迟比 Jev 降低了最高达 9 倍，并在 DeepSWE 和 Terminal-Bench 2.1 等代码基准测试中树立了验证器 (Verifier) 性能的业界全新标杆。

> Contrastive-LM has introduced **CLM-8B**, the first open-source model in a new class of **Contrastive Language Models (CLMs)**. Instead of generating text, CLM evaluates candidate actions against the current state and outputs probabilities, providing a high-performance open alternative to proprietary models like TypeSafe AI's Jev. Distributed under the Apache-2.0 license, the 75 MB head runs efficiently on a single NVIDIA GPU using vLLM for the Qwen3-8B encoder. Featuring optimized caching mechanisms and a robust three-stage training recipe, CLM-8B achieves up to 9× faster latency than Jev in zero-shot tasks and establishes new state-of-the-art verifier results on coding benchmarks like DeepSWE and Terminal-Bench 2.1.

---

## System One 模型的核心功用

> ## What a System One Model Does

TypeSafe AI 打造的 Jev 并不会返回长篇文字，而是直接返回带有明确概率分布的类型化数值。CLM 完全对齐了这一交互接口，并在 [CLM GitHub 仓库](https://github.com/Contrastive-LM/CLM) 中提供了一套完全兼容的 API，主要支持三大核心查询类型：

> TypeSafe AI's Jev returns typed values with probabilities instead of text. CLM targets this exact interface, offering a compatible API through the [CLM GitHub repository](https://github.com/Contrastive-LM/CLM) that exposes three core question types:

* **Noul：** 计算并返回某个陈述或命题为真时的置信概率。
* **Choice (单选) ：** 从预先声明的候选集合中挑选一个最优项，并附带各自的概率分布。
* **Score (评分) ：** 在有序的量表或评分准则上，计算并返回期望的得分等级。

> * **Noul:** Returns the probability that a statement is true.
> * **Choice:** Picks one option from a declared set, accompanied by probabilities.
> * **Score:** Returns an expected level on an ordered rubric.

针对 TypeSafe API 所设计的结构化请求，可以直接使用 CLM 的 Python 客户端进行无缝重放和执行，无需对调用逻辑做任何更改。

> Requests structured for TypeSafe’s API can be seamlessly replayed using CLM’s Python client.

---

## CLM 的工作原理

> ## How CLM Works

CLM 通过双向 InfoNCE 损失函数 (InfoNCE Loss) 同时训练状态编码器 (State Encoder) 与动作编码器 (Action Encoder) 。两个编码器均采用冻结的 [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) 骨干网络，仅外挂一个 20M 参数的可训练投影头 (Projection Head) 。在训练阶段，模型会拉近每个当前状态与实际所采取动作之间的表征距离，同时将该状态与所有未被采纳的备选动作推远，形成鲜明的对比表征。

> CLM trains a state encoder and an action encoder utilizing a bidirectional InfoNCE loss. Each encoder consists of a frozen [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) backbone coupled with a 20M-parameter trainable projection head. During training, the model pulls each state toward the action actually taken while pushing it away from alternatives.

在推理阶段，系统通过计算状态向量与各个动作嵌入向量的点积 (Dot Product) 来为候选动作打分，再经过 Softmax 函数将其转化为标准答案的概率分布。在典型的 AI 智能体运行循环中，环境状态在每一步都会改变，但可选动作集合通常基本保持固定。针对这一特点，`clm-serve` 引入了高效的向量缓存机制，从而规避了大量冗余运算。在配备 3 个可选动作的单张 RTX 4090 显卡上，复访状态的推理延迟从 1.7 ms 骤降至 0.6 ms；而当候选动作扩展到约 1,000 个时，其运行速度最高可达 Jev 的 13 倍。

> At inference time, candidate actions are scored via the dot product of the state and action embeddings, converted into an answer distribution via softmax. Because agent states change every step while action sets remain mostly fixed, `clm-serve` caches vectors to avoid redundant computations. On a single RTX 4090 with 3 actions, revisited state latency drops from 1.7 ms to 0.6 ms, enabling speeds up to 13× faster than Jev with ~1,000 candidates.

---

## 三阶段训练秘方

> ## A 3-Stage Training Recipe

1. **预训练 (Pre-training) ：** 基于约 6000 万对 [Nemotron DQA 问答对数据](https://huggingface.co/datasets/Contrastive-LM/CLM-v0.1-Pretrain-Nemotron) 展开基础预训练。
2. **中期训练 (Mid-training) ：** 引入由 Gemini 2.5 Flash-Lite 合成的约 3000 万条高质量难负例 (Hard Negatives) 数据进行强化训练。
3. **后训练 (Post-training) ：** 融合源自 Agent Data Protocol、Endless-Terminals 和 LiteCoder-Terminal-SFT 的约 100 万条真实智能体运行轨迹 (Agent Trajectories) 数据。

> 1. **Pre-training:** Performed on ~60M [Nemotron DQA question-answer pairs](https://huggingface.co/datasets/Contrastive-LM/CLM-v0.1-Pretrain-Nemotron).
> 2. **Mid-training:** Utilizes ~30M synthetic hard negatives generated by Gemini 2.5 Flash-Lite.
> 3. **Post-training:** Incorporates ~1M agent trajectories sourced from Agent Data Protocol, Endless-Terminals, and LiteCoder-Terminal-SFT.

在约 10 万道预留的测试问答上，仅进行预训练即可达到 52.1% 的 Top-1 准确率；而在经历中期训练后，该指标进一步跃升至 69.2%  (相比之下，若从一开始就完全只在难负例数据上训练，准确率在过拟合之前便会过早触顶停留在 62.4%) 。

> On ~100K held-out questions, pre-training alone achieves 52.1% top-1 accuracy, which rises to 69.2% after mid-training (whereas training exclusively on hard negatives from the start peaks prematurely at 62.4% before overfitting).

---

## 与 Jev 的零样本性能对比

> ## Zero-Shot Results Against Jev

| 评估任务 | CLM-8B 延迟 | Jev 延迟 | CLM-8B 成功率 | Jev 成功率 |
| :--- | :--- | :--- | :--- | :--- |
| T-Rex 游戏 | 16.5 ms | 149.8 ms | 5/5 | 5/5 |
| 工具调用 (BFCL v4) | 76.8 ms | 125.5 ms | 95.2% | 99.2% |
| WikiRacing (维基竞速) | 79.8 ms | 225 ms | 26/30 | 30/30 |
| Super Mario (超级马里奥) | 33.5 ms | 132.6 ms | 5/5 | 5/5 |

> | Task | CLM-8B Latency | Jev Latency | CLM-8B Success | Jev Success |
> | :--- | :--- | :--- | :--- | :--- |
> | T-Rex game | 16.5 ms | 149.8 ms | 5/5 | 5/5 |
> | Tool calling (BFCL v4) | 76.8 ms | 125.5 ms | 95.2% | 99.2% |
> | WikiRacing | 79.8 ms | 225 ms | 26/30 | 30/30 |
> | Super Mario | 33.5 ms | 132.6 ms | 5/5 | 5/5 |

最为惊艳的 9 倍加速成果出现在 [T-Rex 游戏](https://github.com/Contrastive-LM/CLM/blob/main/examples/t_rex/README.md) 中，因为在该任务中相同的动作会在不同状态间频繁重复出现。在任务表现方面，CLM 在 T-Rex 游戏与 Super Mario 任务上与 Jev 打成平手，在工具调用和 WikiRacing 上略有微小差距；但在推理响应速度上，CLM 在所有测试基准中均展现出压倒性优势，全面大幅超越 Jev。

> The headline 9× speedup is observed on the [T-Rex game](https://github.com/Contrastive-LM/CLM/blob/main/examples/t_rex/README.md), where actions frequently repeat across states. While CLM matches Jev on the T-Rex and Super Mario tasks and slightly trails on tool calling and WikiRacing, it consistently outperforms Jev in inference speed across the board.

---

## CLM 充当编程智能体的结果验证器

> ## CLM as a Verifier for Coding Agents

在典型的智能体验证流水线中，通常由生成器 (Generator) 采样出多个候选解决方案，再由验证器 (Verifier) 选出其中的最优解。研究团队在单张 H100 GPU 上针对预留测试子集进行了全面评估  (其中 DeepSWE 的候选方案由 Opus 5 生成，Terminal-Bench 2.1 的候选方案由 Fable 5 生成) ：

> In agent verification pipelines, a generator samples multiple candidate solutions and a verifier selects the best one. Evaluated on held-out subsets (using Opus 5 for DeepSWE and Fable 5 for Terminal-Bench 2.1 candidates) on an H100:

| 基准测试 | Pass@1 基础值 | CLM (微调版) | Jev | CLM 延迟 | Jev 延迟 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSWE | 73.7% | 81.6% | 71.1% | 79 ms | 449 ms |
| Terminal-Bench 2.1 | 84.0% | 87.6% | 83.1% | 32 ms | 131 ms |

> | Benchmark | Pass@1 | CLM (Fine-Tuned) | Jev | CLM Latency | Jev Latency |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | DeepSWE | 73.7% | 81.6% | 71.1% | 79 ms | 449 ms |
> | Terminal-Bench 2.1 | 84.0% | 87.6% | 83.1% | 32 ms | 131 ms |

这些评测结果在验证器基准测试上创下了全新的业界最前沿 (SOTA) 纪录。值得注意的是，Jev 评测得分甚至低于未经挑选的基线 Pass@1 指标，这意味着使用 Jev 进行筛选其表现反而不如随机抽样；相比之下，CLM 借助轻量级的 [微调预测头](https://github.com/Contrastive-LM/CLM/blob/main/docs/FINETUNING.md)，不仅显著提升了解题准确率，还同时实现了 4.1 倍至 5.7 倍的推理加速。

> These results establish new SOTA verifier benchmarks. Notably, Jev scores below the baseline Pass@1 metric, meaning selection with Jev degrades performance compared to random sampling, whereas CLM delivers accuracy improvements alongside a 4.1× to 5.7× speedup utilizing lightweight [fine-tuned heads](https://github.com/Contrastive-LM/CLM/blob/main/docs/FINETUNING.md).

---

## 核心要点总结

> ## Key Takeaways

* **颠覆传统架构：** CLM-8B 直接对候选动作进行打分与概率评估，彻底告别了自回归逐字生成文本的传统模式。
* **极致推理能效：** 在零样本任务评测中，推理延迟相比 Jev 降低最高达 9 倍。
* **强悍的验证器能力：** 经过微调的预测头在 DeepSWE 上取得了 81.6% 的准确率，在 Terminal-Bench 2.1 子集上斩获 87.6% 的优异成绩。
* **专为智能体循环优化：** 深度缓存状态与动作向量，大幅削减智能体多步执行中的单步等待延迟。
* **完全开源自由：** 预测头基于 Apache-2.0 许可证发布，专为在单张 NVIDIA GPU 上私有化部署量身打造。

> * **Alternative Architecture:** CLM-8B evaluates and scores candidate actions rather than generating text autoregressively.
> * **High Efficiency:** Delivers up to 9× lower latency than Jev during zero-shot evaluations.
> * **Strong Verifier Performance:** Fine-tuned model heads achieve 81.6% accuracy on DeepSWE and 87.6% on Terminal-Bench 2.1 subsets.
> * **Optimized Agent Loops:** Caches state and action vectors to drastically lower step-by-step latency.
> * **Open Source:** Apache-2.0 licensed head designed for self-hosting on a single NVIDIA GPU.

---

## 相关资源与链接

> ## Resources & Links

* [Hugging Face 上的 CLM-8B 模型主页](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)
* [官方 GitHub 代码仓库](https://github.com/Contrastive-LM/CLM)
* [项目博客与 Notion 主页](https://contrastive-lm.notion.site/)
* [完整数据集与模型合集](https://huggingface.co/Contrastive-LM)

> * [CLM-8B Model on Hugging Face](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)
> * [Official GitHub Repository](https://github.com/Contrastive-LM/CLM)
> * [Project Blog & Notion](https://contrastive-lm.notion.site/)
> * [Data & Models Collection](https://huggingface.co/Contrastive-LM)
