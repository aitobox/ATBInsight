---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 图论
- 自动化定理证明
- 人工智能
- Lean 4
- 机器学习
title: AutoGraphForge：迈向图论的自动化发现
---
### 文章背景与核心概要
本文介绍了 AutoGraphForge，这是一个旨在实现图论中定理的自动化猜想、反驳、形式化和证明的计算管线。通过结合传统的组合生成技术、大规模经验数据集以及现代神经定理证明器，该系统旨在自主发现并验证图不变量之间的新数学关系。

该系统通过迭代式的反例引导方法生成猜想，利用线性规划对 559 种经典关系进行新颖性过滤，并针对包含约 34,000 个图的经验数据集进行严格的压力测试。最终，存活下来的猜想会被自动转换为 Lean 4 语句骨架，并结合神经证明器与独立核心验证（Kernel-verification）进行证明。

---

## 概述 (Overview)
> **AutoGraphForge** is an ongoing computational pipeline designed for the automated conjecturing, refuting, formalizing, and proving of theorems in graph theory. By combining traditional combinatorial generation techniques, large-scale empirical datasets, and modern neural theorem provers, the system aims to autonomously discover and verify novel mathematical relationships between graph invariants.

**AutoGraphForge** 是一个正在开发中的计算管线，旨在实现图论中定理的自动化猜想、反驳、形式化和证明。通过结合传统的组合生成技术、大规模经验数据集以及现代神经定理证明器，该系统旨在自主发现并验证图不变量之间的新数学关系。

---

## 管线的核心组件 (Key Components of the Pipeline)

### 1. 猜想生成 (Conjecture Generation)
> * **Method:** Employs a counterexample-guided approach running in iterative rounds.
> * **Mechanism:** A Graffiti3 generator proposes conjectures based on a small, evolving snapshot table $T$ (initially comprising a few hundred graphs and their computed invariants). This table expands exclusively by integrating counterexamples generated against previous rounds of conjectures.

* **方法：** 采用在迭代轮次中运行的反例引导方法。
* **机制：** Graffiti3 生成器基于一个小型且不断演进的快照表 $T$（最初包含几百个图及其计算出的不变量）提出猜想。该表通过整合针对上一轮猜想生成的反例来进行扩展。

### 2. 新颖性过滤 (Novelty Filtering)
> * **Scope:** Evaluates candidates against $559$ classical and folklore relations.
> * **Logic:** The filter is closed under transitive composition and linear identity substitution. 
> * **Execution:** Utilizes a linear program to determine whether a candidate conjecture is already mathematically implied by existing, established results.

* **范围：** 评估候选猜想是否符合 559 种经典和民间关系。
* **逻辑：** 该过滤器在传递复合（transitive composition）和线性恒等式代换下是闭合的。
* **执行：** 利用线性规划来确定候选猜想是否已经被现有、确立的结果在数学上所隐含。

### 3. 经验反驳数据集 (Empirical Refutation Dataset)
> * **Dataset Scale:** Consists of approximately $348,000$ graphs.
> * **Composition:** 
>   * Complete House of Graphs invariant export.
>   * Exhaustive census of all connected graphs on $\le 9$ vertices.
>   * Extremal families (strongly regular, minimal Ramsey, Cayley, cages, barbells, lollipops, spiders).
>   * Random graph models.
> * **Process:** Surviving candidates from the novelty filter undergo rigorous stress-testing against this dataset via active counterexample-search algorithms.

* **数据集规模：** 由大约 348,000 个图组成。
* **组成部分：**
  * 完整的 House of Graphs 不变量导出数据。
  * 对所有顶点数 $\le 9$ 的连通图进行穷举统计。
  * 极值族（强正则图、极小 Ramsey 图、Cayley 图、笼图、哑铃图、棒棒糖图、蜘蛛图）。
  * 随机图模型。
* **流程：** 通过新颖性过滤的候选猜想将通过主动反例搜索算法，针对该数据集进行严格的压力测试。

### 4. 形式化与自动化证明 (Formalization and Automated Proving)
> * **Translation:** Automatically and deterministically translates surviving conjectures into Lean 4 statement skeletons.
> * **Kernel Verification:** Every candidate proof undergoes rigorous kernel-verification against a pinned version of `mathlib4` combined with a custom invariant preamble.
> * **Neural Provers:** Integrates two neural provers—**DeepSeek-Prover-V2-671B** (served via vLLM) and the Lean-specialized **OProver-32B**—running upstream of the independent kernel check.

* **翻译：** 自动且确定性地将存活下来的猜想转换为 Lean 4 语句骨架。
* **核心验证：** 每个候选证明都要针对固定版本的 `mathlib4` 以及自定义的不变量前言（preamble）进行严格的核心验证。
* **神经证明器：** 集成了两个神经证明器——**DeepSeek-Prover-V2-671B**（通过 vLLM 提供服务）和专注于 Lean 的 **OProver-32B**——它们在独立核心检查之前运行。

---

## 当前结果与状态 (Current Results and Status)
> * **Yield:** Following multiple rounds on an High-Performance Computing (HPC) cluster, the loop successfully produced **$6,522$ conjectures** that survived the refutation dataset, novelty filter, and active-search runs.
> * **Notable Discoveries:** The discovered conjectures include non-trivial relationships between the **annihilation number** and the **edge-cover number** for bipartite and regular graphs, which have also been successfully proven by hand.
> * **Status:** The end-to-end implementation passes initial sanity checks, with the complete automated pipeline currently executing on the cluster.

* **产出：** 在高性能计算（HPC）集群上经过多轮运行后，该循环成功产生了 **6,522 个猜想**，这些猜想通过了反驳数据集、新颖性过滤器和主动搜索运行的考验。
* **重要发现：** 发现的猜想包括二分图和正则图的**湮灭数（annihilation number）**与**边覆盖数（edge-cover number）**之间非平凡的关系，这些关系也已经通过人工证明成功证实。
* **状态：** 端到端实现已通过初始合理性检查（sanity checks），完整的自动化管线目前正在集群上执行。

---

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">