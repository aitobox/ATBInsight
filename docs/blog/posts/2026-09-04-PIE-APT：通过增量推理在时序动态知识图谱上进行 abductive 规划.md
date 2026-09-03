---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 知识图谱
- 自动规划
- 描述逻辑
- 溯因推理
- 语义网
title: PIE-APT：通过增量推理在时序动态知识图谱上进行 abductive 规划
---
### 文章背景与核心概要

在开放世界和信息不完备的环境下，在时序动态知识图谱（Temporal Dynamic Knowledge Graphs, TDKGs）上进行规划一直面临着严峻的理论挑战。传统的动作形式化方法经常陷入可判定性问题以及“分支问题”（Ramification Problem），而结构化的溯因推理（abduction）往往需要庞大的组合搜索空间。为了克服这些障碍，本文提出了 PIE-APT 框架。

该框架包含两个核心组件：一是 **PIE-Abducer**（增量直接推导溯因模块），它通过将目标的逻辑否定注入到一致的描述逻辑（DL）分支中来合成缺失的前提，从而绕过了传统的最小hitting集（MHS）枚举；二是 **PIE-APT**（溯因规划模块），它采用递归的“生成-测试”（Generate-and-Test）架构，将后向链式 A* 搜索与 PIE-Abducer 相结合，并通过前向链式的时序投射（Temporal Projection）进行验证。

该框架原生运行在表达能力强大的 $\mathcal{SROIQ}$ 描述逻辑和 OWL 之上，成功保持了可判定性，并在高级 OWL 基准测试中展现出优于经典规划器的性能。

---

## 摘要 (Abstract)

> Planning over Temporal Dynamic Knowledge Graphs (TDKGs) presents theoretical challenges in open-world environments with incomplete information. Existing action formalisms often face decidability issues and the Ramification Problem, while structural abduction requires expansive combinatorial search spaces. 

在开放世界及信息不完备的环境中，在时序动态知识图谱（TDKGs）上进行规划带来了理论上的挑战。现有的动作形式化方法经常面临可判定性问题以及分支问题（Ramification Problem），而结构化溯因推理则需要庞大的组合搜索空间。

> We introduce a unified framework with two modules—**PIE-Abducer** (incremental direct-derivation abduction) and **PIE-APT** (Abductive Planning for TDKGs)—operating natively on the expressive $\mathcal{SROIQ}$ Description Logic. Modeling state transitions as non-monotonic updates to deductively closed DL theories, we represent actions natively in OWL. This leverages an incremental reasoner to preserve decidability and natively bypass the Ramification Problem. 

我们引入了一个包含两个模块的统一框架——**PIE-Abducer**（增量直接推导溯因）和 **PIE-APT**（针对 TDKGs 的溯因规划），它们原生运行在表达能力强的 $\mathcal{SROIQ}$ 描述逻辑上。我们将状态转换建模为对演绎封闭的 DL 理论的非单调更新，并在 OWL 中原生表示动作。这利用了增量推理机来保持可判定性，并原生绕过了分支问题。

> To address incomplete knowledge, PIE-Abducer circumvents Minimal Hitting Set (MHS) enumeration. Instead of combinatorial search, it injects the logical negation of a goal into a consistent DL branch and synthesizes missing premises via direct refutation consequences. PIE-APT employs a recursive Generate-and-Test architecture, interleaving backward-chaining A* search with PIE-Abducer to synthesize both action sequences and abductive assumptions. Candidates undergo strict validation via forward-chaining Temporal Projection to evaluate logical trajectories. 

为了解决知识不完备问题，PIE-Abducer 绕过了最小 Hitting 集（MHS）的枚举。它不进行组合搜索，而是将目标的逻辑否定注入到一致的 DL 分支中，并通过直接反驳推论来合成缺失的前提。PIE-APT 采用递归的“生成-测试”架构，将后向链式 A* 搜索与 PIE-Abducer 交织在一起，以合成动作序列和溯因假设。候选方案通过前向链式的时序投射进行严格验证，以评估逻辑轨迹。

> We evaluate four OWL benchmarks targeting semantic abilities missing from classical planning:
> * Parameterized goals with witness search
> * Mid-search DL entailment
> * Open-world assumption injection
> * Adversarial plan synthesis

我们评估了四个针对经典规划所缺少的语义能力的 OWL 基准测试：
* 带有见证搜索（witness search）的参数化目标
* 搜索中期的 DL 蕴涵
* 开放世界假设注入
* 对抗性计划合成

> Results show qualitative superiority over classical planners and prove our direct-derivation approach significantly outperforms an MHS-faithful baseline in abductive enrichment.

结果表明，该方法在定性上优于经典规划器，并证明了我们的直接推导方法在溯因丰富化方面显著优于符合 MHS 的基线。

---

## 访问与链接 (Access and Links)

> * [View PDF](https://arxiv.org/pdf/2607.27287)
* [TeX Source](https://arxiv.org/src/2607.27287)
* [Experimental HTML Version](https://arxiv.org/html/2607.27287v2)

* [查看 PDF](https://arxiv.org/pdf/2607.27287)
* [TeX 源码](https://arxiv.org/src/2607.27287)
* [实验性 HTML 版本](https://arxiv.org/html/2607.27287v2)