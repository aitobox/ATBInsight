---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-29
hide:
  - navigation
tags:
  - AI智能体
  - 多智能体
  - CUDA优化
  - 软件工程
  - vLLM
title: "Evolving Agent Teams：进化式智能体团队突破复杂工程的局部最优"
---

# Evolving Agent Teams：进化式智能体团队突破复杂工程的局部最优

> **arXiv:2610.36848** [cs.AI]  
> **Subject:** Artificial Intelligence (`cs.AI`)  
> **Authors:** Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica  
> **Submitted:** 27 October 2026  
> **Paper:** [arXiv:2610.36848](https://arxiv.org/abs/2610.36848)  
> **Code:** [GitHub - caoshiyi/EAT](https://github.com/caoshiyi/EAT)

### 文章背景与核心概要

随着大语言模型编程能力的飞速跃升，研究人员开始尝试将 AI 智能体 (AI Agent) 引入 GPU 底层算子优化 (Kernel Optimization) 等高难度工程任务。然而，现有的单智能体或固定协作模式极易在真实工业级复杂代码上陷入“局部最优”——不断在细枝末节打转却无法实现架构级突破。为此，来自 UC Berkeley 的 Shiyi Cao、Joseph E. Gonzalez 与 Ion Stoica 等学者提出了进化式智能体团队 (Evolving Agent Teams, EAT)，通过设置中央主管动态重构智能体分工，并结合持久化文件系统沉淀试错经验，成功攻克了代码优化的局部停滞难题。实验表明，该团队从零编写的 CUDA 算子性能超越了顶尖专家手写的 FlashInfer 与 vLLM 实现，横跨 NVIDIA、AMD 及 Apple 芯片均刷新了吞吐纪录，为复杂软件系统的自动化极限优化开辟了全新范式。

---

## 总结与亮点概览

> ## Summary

**Evolving Agent Teams** 是一套专为突破开放式软件工程任务 (例如 GPU 算子优化) 中局部最优 (Local Optima) 困境而设计的全新多智能体框架 (Multi-Agent Framework)。在面对复杂的真实工程挑战时，传统的代码编写 AI 智能体往往容易陷入瓶颈而停滞不前。该框架创新性地引入了中央主管角色，负责诊断当前陷入的局部最优并动态重组智能体团队；同时配合一套持久化文件系统 (Persistent File System) (持续追踪经验学习文档、团队进化历史以及各团队的专属产物)，使后续的探索迭代始终建立在累积经验的基础之上。在相同的 Token 预算下，该框架全面超越了各类强劲的代码智能体基准；而在放宽 Token 预算后，它更能从零自动生成顶级水准的 CUDA 算子，在多种异构硬件环境下均超越了 FlashInfer MLA、vLLM 和 FlashKDA 等工业级生产基线。

> **Evolving Agent Teams** is a novel multi-agent framework designed to overcome local optima in open-ended software engineering tasks (such as GPU kernel optimization). Traditional coding agents frequently get stuck when tackling complex, real-world problems. This framework introduces a central supervisor that diagnoses local optima and restructures agent teams accordingly, alongside a persistent file system (tracking a learning document, evolution history, and per-team artifacts) to ground future iterations in accumulated experience. Under matched token budgets, the framework consistently outperforms strong coding baselines, while extended token budgets allow it to generate state-of-the-art CUDA kernels, outperforming production baselines like FlashInfer MLA, vLLM, and FlashKDA across diverse hardware environments.

---

## 论文元数据

> ## Metadata

* **arXiv 编号**：[arXiv:2610.36848](https://arxiv.org/abs/2610.36848) [cs.AI]
* **研究主题**：人工智能 (`cs.AI`)
* **提交日期**：2026 年 10 月 27 日
* **论文作者**：Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica
* **代码仓库**：[GitHub - caoshiyi/EAT](https://github.com/caoshiyi/EAT)

> * **arXiv ID:** [arXiv:2610.36848](https://arxiv.org/abs/2610.36848) [cs.AI]
> * **Subject:** Artificial Intelligence (`cs.AI`)
> * **Submission Date:** 27 October 2026
> * **Authors:** Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica
> * **Code Repository:** [GitHub - caoshiyi/EAT](https://github.com/caoshiyi/EAT)

---

## 论文摘要

> ## Abstract

软件工程智能体的迅猛发展，激发了人们将其应用于 GPU 算子优化等开放式复杂任务的浓厚兴趣。然而研究发现，现有的代码生成智能体在面对专家手写打造的生产级算子 (如 FlashInfer) 时，往往会迅速收敛并陷入局部最优。为此，我们提出了 **Evolving Agent Teams**，一个能够自主跳出此类局部最优陷阱的多智能体框架。

> The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce **Evolving Agent Teams**, a multi-agent framework that escapes such local optima.

该框架的核心特性包括：

> It features:

1. **中央主管 (Central Supervisor)**：深入诊断每一次出现的局部最优瓶颈，并相应地动态重构智能体团队结构；
2. **持久化文件系统 (Persistent File System)**：包含经验学习文档、团队进化历史和各团队专属产物，为团队重组与后续探索提供坚实的经验沉淀。

> 1. A **central supervisor** that diagnoses each local optimum and restructures a team of agents.
> 2. A **persistent file system** that comprises a learning document, an evolution history, and per-team artifacts, grounding restructuring with accumulated experience.

在消耗同等 Token 预算的前提下，Evolving Agent Teams 的表现持续显著优于各类强大的代码智能体基线。而在扩展 Token 预算后，Evolving Agent Teams 能够从零开始生成全新 CUDA 算子，相比工业级生产环境中的 FlashInfer MLA 分页解码 (Paged Decode) 算子实现了平均 **1.2 倍的速度提升**，并在 FlashInfer-Bench 的 47 个生产级负载测试中斩获了 36 项优胜 (在其余 11 项中亦达到 0.86–0.99 倍性能)。

> Under a matched token budget, Evolving Agent Teams consistently outperforms strong coding-agent baselines. With an extended token budget, Evolving Agent Teams generates a CUDA kernel that reaches a **1.2× mean speedup** over the production FlashInfer MLA paged decode kernel from scratch and wins on 36 of 47 production workloads from FlashInfer-Bench (0.86–0.99× on the remaining 11).

此外，该框架还在多项极具挑战性的任务中展现出卓越的性能突破：

> It also demonstrates superior performance on tasks such as:

* **AMD MI350X 平台上的 KDA Prefill**：达到 vLLM 的 3.01 倍加速；
* **NVIDIA B200 平台**：达到 FlashKDA 的 3.44 倍加速；
* **Apple Silicon 芯片上的 MoE 专家卸载 (Expert-Offload) 推理服务**：在搭载 48 GB 统一内存的 M4 Pro 芯片上，使用 MLX 4-bit 精度运行 `Qwen3.8-Flash-Next` 实现了 30.3 tokens/s 的解码吞吐；
* **RoboDojo 机器人操作任务**：在测试随机种子上取得了 62.1 分，大幅超越此前榜单最高分 55.3 分。

> * **KDA prefill on AMD MI350X:** 3.01× over vLLM
> * **NVIDIA B200:** 3.44× over FlashKDA
> * **MoE expert-offload serving on Apple silicon:** 30.3 tokens/s decode for `Qwen3.8-Flash-Next` in MLX 4-bit on a 48 GB M4 Pro
> * **RoboDojo robot manipulation:** 62.1 on held-out seeds vs. 55.3 for the best leaderboard entry.
