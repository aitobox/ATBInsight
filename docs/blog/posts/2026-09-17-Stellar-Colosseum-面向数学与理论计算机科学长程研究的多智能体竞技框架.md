---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-17
hide:
  - navigation
tags:
  - 多智能体
  - 理论计算机科学
  - 数学推理
  - 长程科研
title: "Stellar Colosseum：面向数学与理论计算机科学长程研究的多智能体竞技框架"
---
### 文章背景与核心概要

尽管现代大语言模型在生成简短数学证明方面表现出色，但在面对需要长程决策与精密推演的前沿科学研究时，往往容易因链条脆弱和不确定性累积而遭遇瓶颈。为了攻克这一难题，来自学术界与 Google 等机构的研究团队联合推出了 **Stellar Colosseum** —— 一个与模型无关的多智能体协同与推理竞技框架，专为数学和理论计算机科学 (Theoretical Computer Science, TCS) 等高难度长程科研任务量身打造。该框架创新性地引入了备选策略探索、成熟度门控、结构化证明图、针对性证伪反馈闭环以及重叠随机采样树聚合机制，让多智能体在协同博弈中不断锤炼严密的学术论证。在涵盖 FOCS、STOC 等顶级学术会议的 TCS-Bench 定理证明评测中，Stellar Colosseum 斩获了高达 71.0% 的准确率，并在复杂算法挑战赛中攻克了绝大部分难题，为 AI 辅助前沿科学探索迈出了坚实一步。

---

# Stellar Colosseum：面向数学与理论计算机科学长程研究的多智能体竞技框架

> # Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science

**作者：** Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni  
**arXiv 预印本：** [arXiv:2609.15983 [cs.AI]](https://arxiv.org/abs/2609.15983) (提交于 2026 年 9 月 14 日，最后修订于 2026 年 9 月 15 日)   
**主分类：** 人工智能 (`cs.AI`)  
**其他分类：** 计算与语言 (`cs.CL`)、机器学习 (`cs.LG`)  

> **Authors:** Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni  
> **arXiv:** [arXiv:2609.15983 [cs.AI]]() (Submitted on 14 Sep 2026, last revised 15 Sep 2026)  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **Additional Subjects:** Computation and Language (`cs.CL`), Machine Learning (`cs.LG`)  

---

## 摘要

> ## Summary

虽然现代语言模型在给出看似严密自洽的简短证明方面表现抢眼，但在面对长程科研难题时却屡屡碰壁。这类长程探索的成败，往往完全取决于一连串环环相扣、充满不确定性且高度脆弱的连锁决策——稍有不慎，推演便前功尽弃。

> While modern language models excel at producing plausible short proofs, they frequently stumble on long-horizon research problems where success hinges on a fragile sequence of uncertain and interdependent decisions. 

为了突破这一瓶颈，研究团队推出了 **Stellar Colosseum** —— 一个专为数学与理论计算机科学 (Theoretical Computer Science, TCS) 复杂长程研究打造的模型无关推理框架。

> To bridge this gap, the authors introduce **Stellar Colosseum**, a model-agnostic inference framework designed for complex research in mathematics and theoretical computer science (TCS). 

### Colosseum 框架的核心创新点：

> ### Key Innovations of the Colosseum Framework:

1. **备选策略探索** (Alternative Strategy Exploration) ：在正式构建严谨证明之前，先行探索多种潜在的解题路线与突破策略。
2. **成熟度门控** (Readiness Gates) ：动态评估某条探索路线是否足够成熟，能否进一步拆解为子问题。
3. **结构化证明方案** (Structured Proof Plans) ：将推演中的证明抽象表示为由相互依赖、章节级子问题构成的网络图谱。
4. **针对性证伪与反馈闭环** (Targeted Falsification & Feedback Loops) ：并行生成多个候选推论方案，通过激进的对抗性证伪展开极限施压，并将验证器的批评意见精准反馈至论证受影响的具体环节。
5. **重叠随机采样树聚合** (Overlapping Random-Sample Tree Aggregation) ：将不同路线的候选论断与审查批评深度综合，融汇成结构自洽、高质量的完整学术研究成果。

> 1. **Alternative Strategy Exploration:** Explores multiple solution pathways prior to formal proof construction.
> 2. **Readiness Gates:** Dynamically evaluates whether a particular route is mature enough to be broken down into subproblems.
> 3. **Structured Proof Plans:** Represents the ongoing proof as a network of interdependent, section-level subproblems.
> 4. **Targeted Falsification & Feedback Loops:** Generates parallel candidates, attacks them with aggressive falsification, and routes verifier critiques directly back to the affected areas of the argument.
> 5. **Overlapping Random-Sample Tree Aggregation:** Synthesizes candidates and critiques into a cohesive, high-quality research artifact.

目前，Colosseum 工作流已作为 **Long Proof pattern** 成功集成至 Google Antigravity 的 *Teamwork framework* 中。

> The Colosseum workflow has been successfully integrated into Google Antigravity's *Teamwork framework* as the **Long Proof pattern**.

---

## 关键性能与基准测试

> ## Key Performance & Benchmarks

* **开放式前沿科研** (Open-Ended Research) ：在由 *Gemini 3.1 Pro* 驱动的 Colosseum 框架加持下，作者针对源自 **FOCS** 与 **JMLR** 等顶级学术会议与期刊中论文提出的多个未解开放问题，成功生成了数个全新的解决方案。
* **TCS-Bench 理论计算机科学基准** (TCS-Bench) ：在由 FOCS、STOC 和 SODA 顶会论文提炼出的科研级定理证明任务构成的严苛基准测试中，Colosseum 联合 *Gemini 3.1 Pro* 与 *Gemini 3.7 Flash* 实现了 **71.0% 的准确率**。
* **Codeforces 算法竞赛评测** (Codeforces Evaluation) ：在利用 *Gemini 3.1 Pro* 并融入执行反馈的面向证明流水线中，该系统在 **222 道难题中成功攻克了 218 道**。

> * **Open-Ended Research:** Utilizing Colosseum powered by *Gemini 3.1 Pro*, the authors generated several novel solutions addressing open problems originating from papers published at premier venues such as **FOCS** and **JMLR**.
> * **TCS-Bench:** On this rigorous benchmark consisting of research-level theorem-proving tasks drawn from FOCS, STOC, and SODA papers, Colosseum achieved **71.0% accuracy** using a combination of *Gemini 3.1 Pro* and *Gemini 3.7 Flash*.
> * **Codeforces Evaluation:** In a proof-oriented pipeline enhanced with execution feedback using *Gemini 3.1 Pro*, the system successfully solved **218 out of 222 problems**.
