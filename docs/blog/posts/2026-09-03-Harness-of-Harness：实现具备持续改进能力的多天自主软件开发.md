---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 大语言模型
- 自主软件开发
- 智能体框架
- 持续改进
- 软件工程
title: Harness-of-Harness：实现具备持续改进能力的多天自主软件开发
---
### 文章背景与核心概要

随着大语言模型（LLM）的飞速发展，利用AI进行自主软件开发已成为学术界和工业界的前沿热点。然而，现有的编码智能体（Coding Agents）在面对长周期、多天候的复杂软件构建任务时，往往会面临错误累积、上下文退化、难以平衡功能扩展与Bug修复等瓶颈，难以在无人类干预的情况下实现软件的持续演进。

为了突破这一限制，本文介绍了全新框架 **Harness-of-Harness (HoH)**。HoH 运行于现有编码智能体框架之上，通过将智能体的执行过程组织为“规划-编码-测试”的迭代循环，并在其中引入版本化项目历史、职责解耦、渐进式暴露技能与工具等核心机制，有效解决了长周期开发中的稳定性与演进难题。在多个基准测试（如 GameCraft-Bench、FrontierSWE 和 ProgramBench）中，HoH 展现出卓越的性能，平均相对增益高达 52.25%，并成功在跨越70多个迭代、历时多天的部署中，自主开发出包含完整故事情节、核心机制、精致视觉和集成音效的第一人称射击游戏。

---

# Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

**arXiv ID:** [arXiv:2609.01481](https://arxiv.org/abs/2609.01481) [cs.AI]  
**Submitted on:** September 1, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**Authors:** Haoyang Yan, Min-le Su, Hangfan Zhang, Zhanhao Li, Chen Zhang, Shao Zhang, Yang Chen, Lei Bai, Shuyue Hu  

> **arXiv ID:** [arXiv:2609.01481](https://arxiv.org/abs/2609.01481) [cs.AI]  
> **Submitted on:** September 1, 2026  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **Authors:** Haoyang Yan, Min-le Su, Hangfan Zhang, Zhanhao Li, Chen Zhang, Shao Zhang, Yang Chen, Lei Bai, Shuyue Hu  

---

## 📌 Summary

**Harness-of-Harness (HoH)** is a novel framework designed to enable Large Language Model (LLM)-based coding agents to continually improve software across long-duration, multi-day autonomous development cycles without human intervention. By operating on top of existing coding-agent harnesses, HoH structures agent executions into iterative planning-coding-testing loops while maintaining versioned project histories, balancing capability growth with bug repair, and separating implementation-time testing from independent evaluation. Across multiple benchmarks, HoH significantly outperforms standalone coding harnesses, demonstrating the ability to build complex, fully playable systems (such as a first-person shooter game with audio and polished visuals) over dozens of autonomous iterations.

> **Harness-of-Harness (HoH)** is a novel framework designed to enable Large Language Model (LLM)-based coding agents to continually improve software across long-duration, multi-day autonomous development cycles without human intervention. By operating on top of existing coding-agent harnesses, HoH structures agent executions into iterative planning-coding-testing loops while maintaining versioned project histories, balancing capability growth with bug repair, and separating implementation-time testing from independent evaluation. Across multiple benchmarks, HoH significantly outperforms standalone coding harnesses, demonstrating the ability to build complex, fully playable systems (such as a first-person shooter game with audio and polished visuals) over dozens of autonomous iterations.

---

## 📝 Abstract

This paper studies autonomous software development, in which LLM-based coding agents transform high-level requirements into complete, functional, and usable software systems without human intervention. We introduce **Harness-of-Harness (HoH)**, a framework that enables coding agents to continually improve software during autonomous development. 

HoH operates on existing coding-agent harnesses, and organizes their executions into iterative planning-coding-testing loops. To sustain improvement across loops, HoH:
* Balances repair with capability growth.
* Scopes development into small and verifiable increments.
* Separates implementation-time testing from independent evaluation.
* Constrains verifiable outputs rather than prescribing agent workflows.
* Progressively exposes deliverables, role-specific tools, and skills.
* Encourages reuse rather than recreation.
* Maintains versioned project histories.

### Performance Highlights
On **GameCraft-Bench**, **FrontierSWE**, and **ProgramBench**—evaluated across three harness-model pairs (*Codex with GPT-5.5, OpenCode with DeepSeek-V4-Pro, and Pi with MiniMax-M3*)—HoH consistently outperforms standalone harnesses, achieving:
* An average relative gain of **52.25%**
* A maximum gain of **82.86%** after three iterations

In a multi-day deployment spanning more than 70 iterations, HoH autonomously developed a first-person-shooter game featuring a coherent storyline, fully implemented core mechanics, a human-playable experience, polished visuals, and integrated audio.

> This paper studies autonomous software development, in which LLM-based coding agents transform high-level requirements into complete, functional, and usable software systems without human intervention. We introduce **Harness-of-Harness (HoH)**, a framework that enables coding agents to continually improve software during autonomous development. 
> 
> HoH operates on existing coding-agent harnesses, and organizes their executions into iterative planning-coding-testing loops. To sustain improvement across loops, HoH:
> * Balances repair with capability growth.
> * Scopes development into small and verifiable increments.
> * Separates implementation-time testing from independent evaluation.
> * Constrains verifiable outputs rather than prescribing agent workflows.
> * Progressively exposes deliverables, role-specific tools, and skills.
> * Encourages reuse rather than recreation.
> * Maintains versioned project histories.
> 
> ### Performance Highlights
> On **GameCraft-Bench**, **FrontierSWE**, and **ProgramBench**—evaluated across three harness-model pairs (*Codex with GPT-5.5, OpenCode with DeepSeek-V4-Pro, and Pi with MiniMax-M3*)—HoH consistently outperforms standalone harnesses, achieving:
> * An average relative gain of **52.25%**
> * A maximum gain of **82.86%** after three iterations
> 
> In a multi-day deployment spanning more than 70 iterations, HoH autonomously developed a first-person-shooter game featuring a coherent storyline, fully implemented core mechanics, a human-playable experience, polished visuals, and integrated audio.

---

## 🔗 Project Resources

* **GitHub Repository:** [Flesymeb/HarnessOfHarness](https://github.com/Flesymeb/HarnessOfHarness)
* **Project Page:** [flesymeb.github.io/HarnessOfHarness](https://flesymeb.github.io/HarnessOfHarness/)
* **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2609.01481)

> * **GitHub Repository:** [Flesymeb/HarnessOfHarness](https://github.com/Flesymeb/HarnessOfHarness)
> * **Project Page:** [flesymeb.github.io/HarnessOfHarness](https://flesymeb.github.io/HarnessOfHarness/)
> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2609.01481)