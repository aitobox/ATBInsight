---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 大模型智能体
- 提示词注入
- 安全基准
- 数据集
- 行为分析
title: AgentDrift：带有步骤标签的提示词注入劫持大模型智能体轨迹基准
---
### 文章背景与核心概要
随着大语言模型（LLM）智能体越来越多地通过工具调用序列与外部环境交互，间接提示词注入攻击（Indirect Prompt Injection）成为了一大核心安全隐患。恶意输入可能隐藏在外部观察结果中，导致智能体从原本的良性行为不知不觉地滑向服务于攻击者的恶意操作。为了深入研究和评估这一威胁，本文推出了 AgentDrift 基准。

AgentDrift 是首个提供逐步骤详细标签的大规模基准测试，涵盖 5 个智能体领域的 12,536 条合成工具调用轨迹以及 71,024 个独立步骤。不同于以往只关注最终成败的评估方法，该数据集将每个步骤细分为良性、注入点、被劫持和注入失败四类状态。通过系统的生成、验证和人工审计，研究揭示了传统表层特征检测在应对隐蔽劫持时的局限性，为未来构建更具鲁棒性的智能体安全防护体系奠定了重要的数据与方法基础。

---

## AgentDrift：带有步骤标签的提示词注入劫持大模型智能体轨迹基准

> ## AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories

## 摘要

> ## Summary

**AgentDrift** 是一个全面的基准测试，旨在评估和研究大语言模型（LLM）智能体所面临的间接提示词注入攻击。由于 LLM 智能体通过一系列工具调用来运行，外部观察结果可能会充当恶意注入的载体，导致智能体从良性行为过渡到执行攻击者的指令。

> **AgentDrift** is a comprehensive benchmark designed to evaluate and study indirect prompt injection attacks on Large Language Model (LLM) agents. Because LLM agents operate via sequences of tool calls, external observations can act as vectors for malicious injections, causing an agent to transition from benign behavior to attacker-serving actions.

与以往仅衡量整体成功或失败的基准不同，AgentDrift 在 12,536 条合成工具调用轨迹中提供了逐步标签。它涵盖了五个智能体领域，并具有 71,024 个独立步骤，这些步骤被分为四种不同的类别：*良性（benign）*、*注入点（injection point）*、*被劫持（hijacked）* 和 *注入失败（failed injection）*。该数据集附带文档，并在 CC BY 4.0 许可证下开源发布。

> Unlike previous benchmarks that only measure overall success or failure, AgentDrift provides step-by-step labels across 12,536 synthetic tool-call trajectories. It covers five agent domains and features 71,024 individual steps classified into four distinct categories: *benign*, *injection point*, *hijacked*, and *failed injection*. The dataset is paired with documentation and released openly under the CC BY 4.0 license.

---

## 元数据与出版详情

> ## Metadata & Publication Details

* **arXiv ID:** [arXiv:2609.06972](https://arxiv.org/abs/2609.06972) [cs.CR]
* **主要主题:** 密码学与安全 (`cs.CR`)
* **次要主题:** 人工智能 (`cs.AI`)、机器学习 (`cs.LG`)
* **作者:** Asif Pinjari, Mithun Paul Saint-Germain
* **提交日期:** 2026年9月7日
* **数据集与代码库:** [GitHub - Asif-0209/AgentDrift](https://github.com/Asif-0209/AgentDrift)

---

## 数据集的核心特征

> ## Key Features of the Dataset

* **规模:** 12,536 条合成工具调用轨迹，包含跨 5 个独特智能体领域的 71,024 个标注步骤。
* **轨迹分布:**
  * **4,000** 条良性轨迹
  * **5,536** 条受攻击轨迹
  * **1,500** 条攻击失败轨迹（智能体成功抵抗注入）
  * **1,500** 条难负样本轨迹（类似攻击的合法内容，用于测试误报率）
* **步骤级标注:** 语料库中的每一步都打上了四种状态之一的标签：
  1. `benign`（良性）
  2. `injection point`（注入点）
  3. `hijacked`（被劫持）
  4. `failed injection`（注入失败）

> * **Scale:** 12,536 synthetic tool-call trajectories containing 71,024 annotated steps across 5 unique agent domains.
> * **Trajectory Distribution:**
>   * **4,000** Benign trajectories
>   * **5,536** Attacked trajectories
>   * **1,500** Failed-attack trajectories (where the agent successfully resisted the injection)
>   * **1,500** Hard-negative trajectories (legitimate content resembling attacks to test false-positive rates)
> * **Step-Level Labeling:** Every step in the corpus is tagged with one of four states:
>   1. `benign`
>   2. `injection point`
>   3. `hijacked`
>   4. `failed injection`

---

## 方法论与发现

> ## Methodology & Findings

* **生成与验证:** 轨迹使用受类别特定协议约束的开源模型生成，通过闭集词汇结构验证器进行验证，由 LLM 裁判进行筛选，并对 1,200 条轨迹进行了人工审计。值得注意的是，审计显示 LLM 裁判经常被难负样本（hard negatives）所欺骗。
* **行为检测挑战:** 基于表层特征的逻辑回归仅能恢复 **55.4%** 的攻击（F1 分数为 0.647），其中仅成功识别了 8.2% 的部分劫持和 23.1% 的延迟执行。这凸显出近半数的攻击需要对行为序列进行综合建模，而不仅仅是简单的特征检查。
* **数据特征:** 本研究对生成数据集中的模板集中度、攻击目标族崩溃（attack-goal-family collapse）以及世界身份泄漏进行了测量和分析。

> * **Generation & Validation:** Trajectories were generated using an open model governed by category-specific protocols, validated via a closed-vocabulary structural validator, screened by an LLM judge, and manually audited across 1,200 trajectories. Notably, audits revealed that the LLM judge was frequently fooled by hard negatives.
> * **Behavioral Detection Challenges:** A surface-feature logistic regression recovers only **55.4%** of attacks (F1 score of 0.647), successfully identifying merely 8.2% of partial hijacks and 23.1% of delayed executions. This highlights that nearly half of the attacks necessitate comprehensive modeling of the behavioral sequence rather than simple feature checks.
> * **Data Characteristics:** The study measures and analyzes template concentration, attack-goal-family collapse, and world-identity leakage within the generated dataset.