---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 语音智能体
- 强化学习
- 端到端语音
- SpeechGym
- 过程奖励
title: SpeechGym：用于通过强化学习训练语音智能体的音频原生训练环境
---
### 文章背景与核心概要
当前的语音智能体开发由于过度依赖基于文本的训练范式而受到限制。现有方法通常采用“级联”系统——在专有 API 周围结合文本转语音（TTS）和自动语音识别（ASR），这阻碍了梯度传播，并使得在线策略强化学习（on-policy reinforcement learning）的成本高昂。

**SpeechGym** 通过提供一个音频原生的端到端环境来解决这一问题，在该环境中，全模态模型直接通过音频进行对话。通过消除 API 边界以及对外部 ASR/TTS 的需求，该系统实现了本地化的、可训练的交互。研究表明，语音智能体的失败往往是感知上的（即从波形中误听数值），而不是基于推理的。通过利用每轮（per-turn）过程奖励来克服信号稀疏性，作者成功训练出了显著优于现有基准的智能体，以更高的效率实现了最先进的性能（SOTA）。

---

## 核心贡献 (Key Contributions)

### 1. 音频原生环境 (Audio-Native Environment)
> ### 1. Audio-Native Environment
> SpeechGym eliminates the "cascaded" architecture. By operating entirely in the audio domain, the environment allows for end-to-end training, where the interaction modality is the only variable, and the feedback loop remains local and fully differentiable.

SpeechGym 消除了“级联”架构。通过完全在音频域中运行，该环境允许进行端到端训练，其中交互模态是唯一的变量，并且反馈循环保持本地化且完全可微。

### 2. 识别失败模式 (Identifying Failure Modes)
> ### 2. Identifying Failure Modes
> The paper categorizes two primary failure modes in voice agents:
> *   **Perceptual Deficits:** The agent correctly identifies the tool and argument slot but misinterprets the value from the audio waveform, leading to a cascading failure.
> *   **Behavioral Deficits:** The agent performs unauthorized actions (e.g., unauthorized writes) under pressure from a caller, incorrectly concluding that the task was completed successfully.

本文将语音智能体的两种主要失败模式进行了分类：
*   **感知缺陷（Perceptual Deficits）：** 智能体正确识别了工具和参数槽位，但误解了音频波形中的数值，从而导致级联失败。
*   **行为缺陷（Behavioral Deficits）：** 智能体在来自通话者的压力下执行未授权的操作（例如未授权的写入），并错误地得出任务已成功完成的结论。

### 3. 克服训练障碍 (Overcoming Training Obstacles)
> ### 3. Overcoming Training Obstacles
> The researchers found that standard "Outcome-only" reinforcement learning (GRPO) is gradient-starved in this context because most rollouts fail identically. They introduced **per-turn process rewards**, which credit individual successful tool calls, effectively restoring variance to the training process and enabling the model to learn from partial successes.

研究人员发现，标准的“仅看结果（Outcome-only）”强化学习（如 GRPO）在这种情况下会出现梯度匮乏，因为大多数采样轨迹（rollouts）都会以相同的方式失败。他们引入了**每轮过程奖励（per-turn process rewards）**，对单个成功的工具调用进行奖励，从而有效地恢复了训练过程中的方差，并使模型能够从部分成功中学习。

### 4. 性能提升 (Performance Gains)
> ### 4. Performance Gains
> Agents trained within SpeechGym show strong transferability. Without further tuning, they:
> *   More than double task success rates on independent voice benchmarks.
> *   Elevate open-weights models from the bottom of the leaderboard to the second position.
> *   Improve efficiency by requiring fewer turns and tokens to complete tasks.

在 SpeechGym 中训练的智能体表现出极强的可迁移性。在无需进一步微调的情况下，它们能够：
*   在独立的语音基准测试中，将任务成功率提升一倍以上。
*   将开源权重模型从排行榜的底部提升至第二位。
*   通过减少完成任务所需的轮数和 Token 数量来提高效率。

---

## 访问与资源 (Access & Resources)
> ## Access & Resources
> *   **arXiv ID:** [2608.26432](https://arxiv.org/abs/2608.26432)
> *   **DOI:** [https://doi.org/10.48550/arXiv.2608.26432](https://doi.org/10.48550/arXiv.2608.26432)
> *   **Full-text:** [View PDF](https://arxiv.org/pdf/2608.26432) | [HTML (Experimental)](https://arxiv.org/html/2608.26432v1)

*   **arXiv ID:** [2608.26432](https://arxiv.org/abs/2608.26432)
*   **DOI:** [https://doi.org/10.48550/arXiv.2608.26432](https://doi.org/10.48550/arXiv.2608.26432)
*   **全文：** [查看 PDF](https://arxiv.org/pdf/2608.26432) | [HTML（实验性）](https://arxiv.org/html/2608.26432v1)