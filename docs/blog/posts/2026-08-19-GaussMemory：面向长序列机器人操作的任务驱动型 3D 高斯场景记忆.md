---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 机器人操作
- 3D高斯泼溅
- 空间记忆
- 具身智能
- 任务驱动
title: GaussMemory：面向长序列机器人操作的任务驱动型 3D 高斯场景记忆
---
### 文章背景与核心概要
长序列机器人操作任务往往容易失败，其根本原因在于当前的 3D 记忆系统多为被动记录器——它们采用固定且人工设计的规则来存储观测数据，无法区分关键的任务物体与无关的背景噪声。为此，本文介绍了 GaussMemory，它将空间记忆视为一种主动的、任务驱动的认知过程，从而实现了范式转变。

该系统摒弃了人工设计的记录规则，通过端到端学习来追踪精确物体、确定更新频率并丢弃无关数据。GaussMemory 将 3D 高斯泼溅（3D Gaussian Splatting）作为持久的几何基底，统一了记忆的更新与读取，使任务需求能够主动塑造更新策略，反之亦然。在 LIBERO 和 VLABench 等标准基准测试中，GaussMemory 的性能显著优于现有模型。

---

## 摘要 (Abstract)

> Long-horizon robotic manipulation fundamentally relies on persistent spatial memory. However, existing 3D memory systems function merely as passive recorders: they store observations using fixed, hand-crafted rules, treating every scene element—whether a critical grasp target or an irrelevant background wall—with equal importance. 
长序列机器人操作从根本上依赖于持久的空间记忆。然而，现有的 3D 记忆系统仅起到被动记录器的作用：它们使用固定、人工设计的规则存储观测数据，将场景中的每个元素（无论是关键的抓取目标还是无关的背景墙）都视作同等重要。

> In this paper, we propose a paradigm shift from passive storage to active, task-driven spatial memory. We argue that a robot's memory should not simply record what it sees, but actively learn how to remember—discovering which objects to track precisely, how aggressively to update them, and what to discard, all learned end-to-end without hand-designed rules. Crucially, this active paradigm is realized by unifying memory update and readout as two sides of the same cognitive process, enabling bidirectional flow where task needs shape update strategies and vice versa. 
在本文中，我们提出了从被动存储到主动、任务驱动型空间记忆的范式转变。我们认为，机器人的记忆不应仅仅记录它所看到的内容，而应主动学习如何记忆——弄清楚应该精确追踪哪些物体、以多大强度去更新它们、以及丢弃什么，所有这些都通过端到端学习实现，无需人工设计的规则。至关重要的是，这种主动范式通过将记忆的更新和读取统一为同一认知过程的两个方面来实现，从而支持双向信息流：任务需求塑造更新策略，反之亦然。

> To instantiate this vision, we introduce **GaussMemory**, which leverages 3D Gaussian Splatting as a persistent geometric substrate. On LIBERO, GaussMemory outperforms MemoryVLA on *Goal* and *Long-10*; on VLABench, it surpasses $\pi_0$-FAST by +5.2% (Track 1) and +6.0% (Track 6).
为了将这一愿景变为现实，我们推出了 **GaussMemory**，它利用 3D 高斯泼溅（3D Gaussian Splatting）作为持久的几何基底。在 LIBERO 基准测试中，GaussMemory 在 *Goal* 和 *Long-10* 任务集上的表现优于 MemoryVLA；在 VLABench 上，它比 $\pi_0$-FAST 基线分别高出 +5.2%（赛道 1）和 +6.0%（赛道 6）。

---

## 论文元数据 (Paper Metadata)

> | Attribute | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.14986](https://arxiv.org/abs/2608.14986) [cs.RO] |
| **Authors** | Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa |
| **Primary Subject** | Robotics (`cs.RO`) |
| **Accepted Venue** | IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2026) |
| **Submitted Date** | August 15, 2026 |
| **Full-Text Access** | [View PDF](https://arxiv.org/pdf/2608.14986) \| [HTML Version](https://arxiv.org/html/2608.14986v1) |
| 属性 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.14986](https://arxiv.org/abs/2608.14986) [cs.RO] |
| **作者** | Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa |
| **主要学科** | 机器人学 (`cs.RO`) |
| **录用会议** | IEEE/RSJ 智能机器人与系统国际会议 (IROS 2026) |
| **提交日期** | 2026年8月15日 |
| **全文访问** | [查看 PDF](https://arxiv.org/pdf/2608.14986) \| [HTML 版本](https://arxiv.org/html/2608.14986v1) |

---

## 核心基准与结果 (Key Benchmarks & Results)

> * **LIBERO Benchmark:** Outperforms `MemoryVLA` on both *Goal* and *Long-10* task suites.
* **LIBERO 基准：** 在 *Goal* 和 *Long-10* 任务集上均优于 `MemoryVLA`。

> * **VLABench Benchmark:** Surpasses the $\pi_0$-FAST baseline by:
  * **+5.2%** on Track 1
  * **+6.0%** on Track 6
* **VLABench 基准：** 超越了 $\pi_0$-FAST 基线：
  * 赛道 1 提升 **+5.2%**
  * 赛道 6 提升 **+6.0%**