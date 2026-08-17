---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- VLA模型
- 机器人学
- 长程任务
- 科学实验
- 智能体插件
title: AtomBridge：面向科学实验长程任务的智能体化 VLA 推理插件
---
### 文章背景与核心概要
机器人实验室通过实现可扩展、连续的实验执行，在自主科学探索中发挥着关键作用。近期的视觉-语言-动作（VLA）模型为机器人实验室提供了有前景的基础。然而，科学实验通常涉及由多个原子任务组成的长程任务，现有的 VLA 模型在执行通过重排和组合这些已知原子动作所构成的复合任务时往往会失败。

这种局限性源于由**机器人状态不匹配（robot-state mismatch）**所引起的技能链条断层（skill-chaining gap）：即一个技能的终端机器人状态可能落入下一个技能的有效初始状态分布之外。为了解决这一挑战，本文提出了 **AtomBridge**，这是一个专为科学实验长程任务设计的智能体化 VLA 推理插件。

AtomBridge 在推理阶段外挂于已在原子任务上微调过的 VLA 策略，同时保持其权重固定。在每个任务边界处，它利用基于大语言模型的转换推理和机器人动作代码生成，在连续任务之间插入过渡动作。这种即插即用的设计无需额外的 VLA 微调或长程组合序列的演示，即可缓解由机器人状态不匹配引起的技能链条断层。在模拟环境和真实世界实验环境的科学操作序列中，AtomBridge 显著提升了执行连续性和每步原子任务的成功率。在 8 步复合任务中，AtomBridge 将全序列成功率提升了 **10% 到 25%**。

---

## AtomBridge: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments

## Summary
* **Authors:** Yiwen Pang, Bo Zhou, Changjin Li, Xuanhao Wang, Shengxiang Xu, Deng-Bao Wang, Peng Cheng, Shimin Di, Jingkuan Song, and Min-Ling Zhang
* **Field:** Robotics (cs.RO) / Artificial Intelligence (cs.AI)
* **arXiv ID:** [arXiv:2602.09430](https://arxiv.org/abs/2602.09430)
* **Key Contribution:** Introduces **AtomBridge**, a plug-and-play Agentic Vision-Language-Action (VLA) inference plugin designed to solve the *skill-chaining gap* in long-horizon scientific experiments without requiring additional fine-tuning or training demonstrations.

> ## 摘要
> 机器人实验室通过实现可扩展、连续的实验执行，在自主科学探索中发挥着关键作用。近期的视觉-语言-动作（VLA）模型为机器人实验室提供了有前景的基础。然而，科学实验通常涉及由多个原子任务组成的长程任务，现有的 VLA 模型在执行通过重排和组合这些已知原子动作所构成的复合任务时往往会失败。
> 
> 这种局限性源于由**机器人状态不匹配**所引起的技能链条断层：一个技能的终端机器人状态可能落入下一个技能的有效初始状态分布之外。为了解决这一挑战，我们提出了 **AtomBridge**，这是一个面向科学实验长程任务的智能体化 VLA 推理插件。
> 
> AtomBridge 在推理阶段外挂于已在原子任务上微调过的 VLA 策略，同时保持其权重固定。在每个任务边界处，它利用基于 LLM 的转换推理和机器人动作代码生成，在连续任务之间插入过渡动作。这种即插即用的设计无需额外的 VLA 微调或长程组合序列的演示，即可缓解由机器人状态不匹配引起的技能链条断层。
> 
> 在模拟环境和真实世界实验环境的科学操作序列中，AtomBridge 提升了执行连续性和每步原子任务的成功率。在 8 步复合任务中，AtomBridge 将全序列成功率提升了 **10% 到 25%**。

> ## Abstract
> Robotic laboratories play a critical role in autonomous scientific discovery by enabling scalable, continuous experimental execution. Recent vision-language-action (VLA) models offer a promising foundation for robotic laboratories. However, scientific experiments typically involve long-horizon tasks composed of multiple atomic tasks. Existing VLA models may fail to perform composed tasks formed by reordering and composing these known atomic actions. 
> 
> This limitation can arise from a skill-chaining gap caused by **robot-state mismatch**: the terminal robot state of one skill can fall outside the valid initial-state distribution of the next. To address this challenge, we propose **AtomBridge**, an Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments. 
> 
> AtomBridge attaches at inference time to a VLA policy already fine-tuned on atomic tasks, while keeping its weights fixed. At each task boundary, it uses LLM-based transition reasoning and robotic-action code generation to insert transitional actions between consecutive tasks. This plug-and-play design mitigates the skill-chaining gap caused by robot-state mismatch without additional VLA fine-tuning or demonstrations of composed long-horizon sequences. 
> 
> Across scientific manipulation sequences in simulation and a real-world experimental environment, AtomBridge improves execution continuity and per-step atomic-task success. On 8-step composed tasks, AtomBridge improves full-sequence success by **10% to 25%**.

## Article Metadata & Links

* **Primary Subject:** Robotics (`cs.RO`)
* **Associated Subjects:** Artificial Intelligence (`cs.AI`)
* **Submission History:** 
  * [v1] Tue, 10 Feb 2026
  * [v2] Fri, 14 Aug 2026 (Current Version)
* **Full-Text & Resources:**
  * [View PDF](https://arxiv.org/pdf/2602.09430)
  * [HTML Version (Experimental)](https://arxiv.org/html/2602.09430v2)
  * [TeX Source](https://arxiv.org/src/2602.09430)
  * [DOI Link](https://doi.org/10.48550/arXiv.2602.09430)

---
*(Note: Preserved element from template source)*
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">