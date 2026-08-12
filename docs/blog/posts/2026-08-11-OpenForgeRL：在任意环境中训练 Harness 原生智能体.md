---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- 强化学习
- AI智能体
- OpenForgeRL
- 开源框架
- 代理工具
title: OpenForgeRL：在任意环境中训练 Harness 原生智能体
---
### 文章背景与核心概要
现代 AI 智能体广泛采用复杂的推理 harness（例如 *Claude Code*、*Codex* 和 *OpenClaw*）来管理多轮推理、工具执行以及与外部系统的交互。然而，由于标准的监督微调（SFT）和强化学习（RL）技术栈难以原生表达具有状态且支持多进程的 harness 推理过程，长期以来使用开源基础设施端到端训练这些复杂的 harness 一直非常困难。

为了填补这一空白，作者推出了 **OpenForgeRL**，这是一个旨在跨多样化环境大规模端到端训练基于 harness 智能体的开源框架。该框架通过一个轻量级代理（Proxy）和一个 Kubernetes 编排器，解耦了训练与推理，使研究人员能够直接在真实的部署 harness 和环境中训练、评估和改进智能体，从而在各项基准测试中展现出业界领先的性能。

---

**arXiv:** [arXiv:2607.21557](https://arxiv.org/abs/2607.21557) [cs.AI]  
**Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao  
**Submitted:** 23 Jul 2026 (Last revised 7 Aug 2026)  

> **arXiv:** [arXiv:2607.21557](https://arxiv.org/abs/2607.21557) [cs.AI]  
> **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao  
> **Submitted:** 23 Jul 2026 (Last revised 7 Aug 2026)  

---

## 📌 執行摘要 (Executive Summary)

现代 AI 智能体利用复杂的推理 harness（如 *Claude Code*、*Codex* 和 *OpenClaw*）来管理多轮推理、工具执行和外部系统交互。然而，由于标准的监督微调（SFT）和强化学习（RL）技术栈难以原生表达有状态的、多进程的 harness 推理，使用开源基础设施端到端训练这些复杂的 harness 以往一直非常困难。

为了弥合这一差距，作者推出了 **OpenForgeRL**，这是一个开源框架，旨在跨多样化环境大规模端到端训练基于 harness 的智能体。

> ## 📌 Executive Summary
> 
> Modern AI agents utilize elaborate inference harnesses (such as *Claude Code*, *Codex*, and *OpenClaw*) to manage multi-turn reasoning, tool execution, and external system interactions. However, training these complex harnesses end-to-end with open-source infrastructure has traditionally been difficult because standard Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) stacks struggle to natively express stateful, multi-process harness inference. 
> 
> To bridge this gap, the authors introduce **OpenForgeRL**, an open-source framework designed to train harness-based agents end-to-end across diverse environments at scale. 

---

## 🛠️ OpenForgeRL 的工作原理 (How OpenForgeRL Works)

OpenForgeRL 将训练与推理进行解耦，使研究人员能够直接在真实的部署 harness 和环境中训练、评估和提升智能体。它通过以下方式实现这一点：
1. **轻量级代理（A Lightweight Proxy）：** 服务于 harness 的模型调用，同时将其记录为与标准 RL 代码库（例如 *veRL*）兼容的高质量训练数据。
2. **Kubernetes 编排器（A Kubernetes Orchestrator）：** 在隔离的远程容器中管理并执行每次 rollout（运行采样），从而支持在任何 harness 与环境组合上进行可扩展的执行。

> ## 🛠️ How OpenForgeRL Works
> 
> OpenForgeRL decouples training and inference, allowing researchers to train, evaluate, and improve agents directly within the real deployment harnesses and environments. It achieves this via:
> 1. **A Lightweight Proxy:** Serves the harness's model calls while recording them as high-quality training data compatible with standard RL codebases (e.g., *veRL*).
> 2. **A Kubernetes Orchestrator:** Manages and executes each rollout inside an isolated remote container, enabling scalable execution across any harness and environment combination.

---

## 📊 基准测试结果 (Benchmark Results)

在复杂的基于工具/claw 的框架以及多模态 GUI 浏览器/计算机操作智能体（computer-use agents）上进行评估时，OpenForgeRL 仅使用几百到几千个任务就展现出了最先进的性能：

* **OpenForgeClaw（基于 Claw 的智能体）：**
  * **ClawEval：** 达到了 `31.7 pass^3` 和 `55.9 pass@3`
  * **QwenClawBench：** 得分 `33.7`
* **OpenForgeGUI（多模态 GUI 智能体）：**
  * **OSWorld-Verified：** 达到了 `37.7`
  * **Online-Mind2Web：** 达到了 `63.0`
  * **WebVoyager：** 达到了 `72.3`

*这两种变体均持续超越同等规模的开源基线，在 GUI 设置中甚至可媲美或超过体积大数倍的模型。*

> ## 📊 Benchmark Results
> 
> Evaluated across complex tool/claw-based frameworks and multimodal GUI browser/computer-use agents, OpenForgeRL demonstrates state-of-the-art performance using only hundreds to a few thousand tasks:
> 
> * **OpenForgeClaw (Claw-based Agents):**
>   * **ClawEval:** Reaches `31.7 pass^3` and `55.9 pass@3`
>   * **QwenClawBench:** Scores `33.7`
> * **OpenForgeGUI (Multimodal GUI Agents):**
>   * **OSWorld-Verified:** Reaches `37.7`
>   * **Online-Mind2Web:** Reaches `63.0`
>   * **WebVoyager:** Reaches `72.3`
> 
> *Both variants consistently outperform open-source baselines of comparable sizes, matching or exceeding models several times larger in the GUI setting.*

---

## 🧠 关于智能体行为与强化学习的关键发现 (Key Findings on Agent Behavior & RL)

* **Harness 复杂度各不相同：** 某些 harness（例如 *ZeroClaw*、*OpenClaw*、*Codex*）对模型而言，其学习难度要显著高于其他 harness。
* **强化学习的影响：** 强化学习显著提高了智能体的可靠性——增强了诸如自我验证、工具覆盖率以及多步计划执行等能力。
* **遗留的局限性：** 尽管整体性能有所提升，但诸如强大的错误恢复等关键能力依然较弱，需要未来的进一步研究。

> ## 🧠 Key Findings on Agent Behavior & RL
> 
> * **Harness Complexity Varies:** Certain harnesses (e.g., *ZeroClaw*, *OpenClaw*, *Codex*) are substantially more challenging for models to learn from than others.
> * **Impact of RL:** Reinforcement learning significantly improves agentic reliability—boosting capabilities like self-verification, tool coverage, and multi-step plan execution.
> * **Remaining Limitations:** Despite overall performance gains, critical abilities such as robust error recovery remain weak and require future research.

---

## 🔗 参考资料与全文链接 (References & Full-Text Links)

* **arXiv 摘要：** [arXiv:2607.21557](https://arxiv.org/abs/2607.21557)
* **PDF 下载：** [查看 PDF](https://arxiv.org/pdf/2607.21557)
* **HTML 版本：** [arXiv HTML（实验性）](https://arxiv.org/html/2607.21557v3)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>

> ## 🔗 References & Full-Text Links
> 
> * **arXiv Abstract:** [arXiv:2607.21557](https://arxiv.org/abs/2607.21557)
> * **PDF Download:** [View PDF](https://arxiv.org/pdf/2607.21557)
> * **HTML Version:** [arXiv HTML (experimental)](https://arxiv.org/html/2607.21557v3)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>