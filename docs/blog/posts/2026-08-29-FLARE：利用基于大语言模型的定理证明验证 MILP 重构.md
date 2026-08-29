---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- MILP
- 大语言模型
- Lean
- 形式化验证
- 组合优化
title: FLARE：利用基于大语言模型的定理证明验证 MILP 重构
---
### 文章背景与核心概要

混合整数线性规划（MILP）是组合优化领域的核心工具，但在设计计算效率高的模型时，人工建模往往面临巨大挑战。尽管大语言模型（LLM）在自动化建模和模型增强方面展现出巨大潜力，但如何确保生成的模型与原始优化问题在逻辑上等价，仍是制约其工业应用的关键瓶颈。

本文提出了一种基于 Lean 定理证明器的 MILP 重构形式化定义，并开发了 FLARE（Formulation-Level Automated Reformulation Evaluation）框架。该框架通过 LLM 智能体与 Lean 证明助手的协同，能够自动验证 MILP 重构的正确性并生成机器可验证的证明证书。此外，作者还发布了包含 20 个问题和 109 个重构模型的 FormulationBench 数据集，实验证明 FLARE 在 NP-hard 问题子集上达到了 100% 的验证准确率。

---

## 摘要

> Mixed-Integer Linear Programming (MILP) is a fundamental tool for combinatorial optimization with extensive real-world applications. A central challenge is designing computationally efficient MILP formulations. Large Language Models (LLMs) offer new opportunities to automate the modeling process, from deriving formulations to strengthening them. Reliable automation requires robust methods for verifying that proposed formulations preserve the underlying optimization problem. However, existing approaches evaluate formulations numerically and fail to reason about general problem instances. We resolve this limitation by introducing a constructive definition of MILP reformulation that can be formalized in Lean and machine-checked. We develop FLARE (Formulation-Level Automated Reformulation Evaluation), a method that uses an LLM-based agent and the Lean proof assistant to verify proposed reformulations against a reference formulation. To evaluate our approach, we introduce FormulationBench, a challenging dataset of 20 problems and 109 formulations. FLARE outperforms existing methods, with 100% accuracy on the NP-hard subset of FormulationBench. Furthermore, FLARE produces a machine-checkable certificate for every reformulation it accepts. For cases where formal guarantees are not necessary, we introduce FLARE-NL, a fast and cheap LLM proxy that matches FLARE's accuracy but produces no certificate. These methods enable reliable verification in automated optimization modeling.

混合整数线性规划（MILP）是组合优化领域的基础工具，具有广泛的现实应用。设计计算效率高的 MILP 模型是一个核心挑战。大语言模型（LLM）为自动化建模过程提供了新的机遇，涵盖了从推导模型到增强模型性能的各个方面。可靠的自动化需要稳健的方法来验证所提出的模型是否保持了底层优化问题的本质。然而，现有的方法仅通过数值检查来评估模型，无法对一般性问题实例进行逻辑推理。我们通过引入一种可在 Lean 中形式化并进行机器检查的 MILP 重构构造性定义，解决了这一局限性。我们开发了 FLARE（模型级自动化重构评估），这是一种利用基于 LLM 的智能体和 Lean 证明助手来验证所提重构与参考模型之间等价性的方法。为了评估我们的方法，我们引入了 FormulationBench，这是一个包含 20 个问题和 109 个重构模型的挑战性数据集。FLARE 的表现优于现有方法，在 FormulationBench 的 NP-hard 子集上达到了 100% 的准确率。此外，FLARE 为其接受的每一个重构生成了机器可检查的证书。对于不需要形式化保证的情况，我们引入了 FLARE-NL，这是一种快速且低成本的 LLM 代理，它在不生成证书的情况下达到了与 FLARE 相同的准确率。这些方法为自动化优化建模中的可靠验证提供了支持。

---

## 关键贡献

1. **构造性 MILP 重构定义：** 形式化了一套严谨的 MILP 重构定义，使其能够在 Lean 证明助手内部进行机器检查。
> 1. **Constructive MILP Reformulation Definition:** Formalized a rigorous definition of MILP reformulation capable of being machine-checked inside the Lean proof assistant.

2. **FLARE 框架：** 将 LLM 智能体与形式化定理证明相结合，自动验证 MILP 重构并生成机器可检查的证书。
> 2. **FLARE Framework:** Combines LLM agents with formal theorem proving to automatically verify MILP reformulations and generate machine-checkable certificates.

3. **FormulationBench 数据集：** 一个由 20 个问题和 109 个多样化模型组成的严谨基准测试套件。
> 3. **FormulationBench Dataset:** A rigorous benchmark suite consisting of 20 problems and 109 diverse formulations.

4. **FLARE-NL：** 一种轻量级、高性能的 LLM 代理，专为不需要严格形式化证书的快速验证工作流而设计。
> 4. **FLARE-NL:** A lightweight, high-performance LLM proxy tailored for rapid validation workflows where formal certificates are not strictly required.