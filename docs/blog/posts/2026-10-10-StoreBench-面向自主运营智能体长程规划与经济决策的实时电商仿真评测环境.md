---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-10
hide:
  - navigation
tags:
  - StoreBench
  - AI 智能体
  - 智能体评测
  - 电商运营
  - GRPO
  - 长程决策
  - arXiv论文
title: "StoreBench：面向自主运营智能体长程规划与经济决策的实时电商仿真评测环境"
---

# StoreBench：面向自主运营智能体长程规划与经济决策的实时电商仿真评测环境

> # StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents

> **arXiv:2610.10942** [cs.AI, cs.CL, cs.LG]  
> **Subjects:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)  
> **Authors:** Daksh Raghuvanshi, Ved Vedere, Yifan Wang  
> **Submitted:** October 7, 2026  
> **DOI:** [arXiv:2610.10942](https://arxiv.org/abs/2610.10942)

### 文章背景与核心概要

评估自主运营智能体在真实商业环境中的实战能力一直面临严峻挑战：传统的静态基准测试通常只有在智能体产生动作时时间才会步进，难以还原现实中时间持续流逝与高度不确定的市场动态。为此，研究团队构建了 **StoreBench**——一个依托工业生产级电商后台运转、实现 24/7 全天候实时模拟的动态电商仿真评测环境，真实再现了顾客昼夜下单、供应链价格剧烈波动以及偶发市场冲击等复杂运营工况。研究团队在跨度从 30 天到 1 整年的长程模拟周期中系统评测了包括 *DeepSeek-V4-Pro* 在内的 7 款前沿大语言模型 (Large Language Models, LLMs) ，发现前沿模型在平均表现上全面落后于基于启发式规则编写的脚本策略，同时也逊色于拥有相同预算的人类专家。然而令人瞩目的是，仅使用 5 个互不重叠的任务进行群体相对策略优化 (Group Relative Policy Optimization, GRPO) 后训练，便使 *Qwen3.5-27B* 在未见评测任务上的综合得分从 0.136 跃升至 0.373 ，展现了强化学习在赋能长程经济决策智能体上的巨大潜力。

---

## 内容概要

> ## Summary

**StoreBench** 是一款专为评估与训练自主运营智能体 (Autonomous Operator Agents) 而打造的动态实时电商仿真评测环境，重点考察智能体在面对不确定性时的长程规划与经济决策能力。与以往那些“智能体不采取行动、时间就停滞不前”的静态基准测试不同，StoreBench 依托工业生产级电商后端，逼真模拟了一家 24/7 全天候持续运转的线上服装店铺。

> **StoreBench** is a dynamic, live-commerce simulation environment designed to evaluate and train autonomous operator agents on long-horizon planning and economic decision-making under uncertainty. Unlike static benchmarks where time only advances alongside agent actions, StoreBench simulates a continuous 24/7 online apparel store powered by a production-grade commerce backend. 

该仿真环境的核心特性包括：

> Key features of the environment include:

* **实时动态性 (Real-time Dynamics) ：** 顾客全天候不间断下单，供应商可能遭遇价格波动或供货中断，同时环境还会随机出现意料之外的市场冲击。
* **受控延迟与预算约束 (Controlled Latency & Budgeting) ：** 智能体使用与人类运营专家完全相同的 29 种商家工具进行操作；系统引入了窗口化运营预算机制，将仿真推进时间与模型的推理延迟彻底解耦。
* **严谨的验证机制 (Rigorous Verification) ：** 所有性能评估指标均经过脚本化基准策略的严格校准，并对奖励机制进行了加固以防止作弊 (“奖励黑客” / Reward Hacking) 。在给定的动作序列下，每个测试回合 (Episode) 均可实现完全确定性的精准重现。

> * **Real-time Dynamics:** Customers place orders around the clock, suppliers experience pricing fluctuations and failures, and unexpected market shocks occur.
> * **Controlled Latency & Budgeting:** Agents operate using the exact same 29 merchant tools available to human operators, bound by a windowed operational budget that decouples simulated time from model inference latency.
> * **Rigorous Verification:** Performance metrics are calibrated against scripted anchor policies, and rewards are hardened against exploitation ("reward hacking"). Every episode is deterministically reproducible given a fixed action sequence.

### 核心评估结论

> ### Key Evaluation Takeaways

* **前沿模型 vs. 启发式策略 (Frontier Models vs. Heuristics) ：** 在涵盖 30 天到整整 1 年仿真周期的多个测试场景下，研究团队评测了 7 款前沿大语言模型 (LLMs) 。结果显示，没有任何一款模型的平均表现能够超越预先编写的“智能分流” (Smart-Triage) 脚本策略。其中综合表现最佳的模型 *DeepSeek-V4-Pro* ，在“任务-随机种子单元”上的通过率仅为 49% ，而启发式规则策略的通过率高达 97% 。
* **人类专家表现 (Human Expertise) ：** 使用完全相同工具集与运营预算的人类商业专家，综合表现超越了所有参评模型（平均综合得分为 **0.708** ，相比之下最佳模型为 **0.700** ）。
* **后训练收益 (Post-Training Gains) ：** 仅利用 5 个互不重叠的训练任务对 *Qwen3.5-27B* 进行群体相对策略优化 (Group Relative Policy Optimization, GRPO) 后训练，就使其在预留的未见评测任务上的平均综合得分从 **0.136** 显著提升至 **0.373** 。

> * **Frontier Models vs. Heuristics:** Evaluated across seven frontier large language models (LLMs) over scenarios ranging from 30 days to a full simulated year, no model outperformed the scripted smart-triage policy on average. The top-performing model, *DeepSeek-V4-Pro*, achieved a 49% pass rate on task-seed cells compared to the heuristic's 97%.
> * **Human Expertise:** Human experts utilizing the identical toolset and operational budget outperformed all evaluated models (mean composite score of **0.708** vs. **0.700**).
> * **Post-Training Gains:** Utilizing a Group Relative Policy Optimization (GRPO) post-training run on *Qwen3.5-27B* using just five disjoint training tasks dramatically raised its mean composite score on held-out evaluation tasks from **0.136** to **0.373**.

---

## 资源获取与访问

> ## Access and Resources

* **论文与代码 (Paper & Code) ：** 
  * [查看 PDF (View PDF)](https://arxiv.org/pdf/2610.10942)
  * [网页版 (实验性) (HTML Version (Experimental))](https://arxiv.org/html/2610.10942v1)
  * [TeX 源码 (TeX Source)](https://arxiv.org/src/2610.10942)
* **公开发布资产 (Released Artifacts) ：** 为防止基准污染 (Benchmark Contamination) ，完整的环境与评测套件暂不公开；但作者团队开源了 **5 个示例训练拆分任务**、**10 条示例轨迹** 以及相关的评分和验证工具链。
* **许可证 (License) ：** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **Paper & Code:** 
>   * [View PDF](https://arxiv.org/pdf/2610.10942)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2610.10942v1)
>   * [TeX Source](https://arxiv.org/src/2610.10942)
> * **Released Artifacts:** To prevent benchmark contamination, the full environment and evaluation suite are withheld; however, the authors released **five example training-split tasks**, **ten sample trajectories**, and the associated scoring and verification tooling.
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 出版与学科信息

> ## Publication Details

* **主要学科方向 (Primary Subject) ：** 人工智能 (`cs.AI`)
* **次要学科方向 (Secondary Subjects) ：** 计算与语言 (`cs.CL`)；机器学习 (`cs.LG`)
* **引用格式 (Cite As) ：** `arXiv:2610.10942 [cs.AI]`

> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Secondary Subjects:** Computation and Language (`cs.CL`); Machine Learning (`cs.LG`)
> * **Cite As:** `arXiv:2610.10942 [cs.AI]`
