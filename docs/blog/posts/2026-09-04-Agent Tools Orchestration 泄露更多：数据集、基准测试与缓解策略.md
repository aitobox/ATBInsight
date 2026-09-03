---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- LLM安全
- 隐私泄露
- 工具编排
- 基准测试
- TOP-Align
title: Agent Tools Orchestration 泄露更多：数据集、基准测试与缓解策略
---
### 文章背景与核心概要
随着大语言模型（LLM）Agent 越来越多地接入各种外部工具，其安全性面临着前所未有的挑战。本文聚焦于一种名为“工具编排隐私风险（TOP-R）”的关键安全隐患，即 LLM Agent 将多个单独看并无害处的工具返回结果组合起来，从而无意中推断并泄露敏感结论。为了对这一风险进行形式化定义和严格评估，作者团队提出了一套四库逆向构建流水线（LRSE）以及包含 1,000 个实例的基准测试集（TOP-Bench）。

通过对多个 LLM Agent 的实证评估，研究发现无论是在最终回复还是在内部推理轨迹中，都存在严重的隐私泄露现象。实验进一步表明，仅靠提示词（Prompt）层面的安全防护是远远不够的。为此，作者提出了一种结合监督微调（SFT）与直接偏好优化（DPO）的新型方法（TOP-Align），能够有效学习并建立更安全的任务完成边界。这项研究已被 EMNLP 2026 Findings 录用，为大模型 Agent 的隐私保护提供了重要的理论与实践参考。

---

## 📋 摘要 (Summary)
This paper investigates a critical security concern termed **Tools Orchestration Privacy Risk (TOP-R)**, wherein Large Language Model (LLM) agents combine individually non-revealing tool returns to inadvertently infer and disclose sensitive conclusions. To formalize and evaluate this risk, the authors introduce a rigorous framework, a 4-library reverse-construction pipeline (**LRSE**), and a benchmark (**TOP-Bench**) containing 1,000 instances. Empirical evaluations across multiple LLM agents reveal substantial privacy leakage in both final responses and reasoning traces. The study further demonstrates that prompt-only safeguards are insufficient, proposing instead a novel Supervised Fine-Tuning and Direct Preference Optimization method (**TOP-Align**) to effectively learn safer task-completion boundaries.

> 本文研究了一项被称为“工具编排隐私风险（Tools Orchestration Privacy Risk, 简称 TOP-R）”的关键安全隐患，在该隐患中，大语言模型（LLM）Agent 将单独来看不具泄露性的工具返回结果组合起来，从而无意中推断并披露了敏感结论。为了将这一风险形式化并进行评估，作者引入了一个严谨的框架、一个 4 库逆向构建流水线（**LRSE**）以及一个包含 1,000 个实例的基准测试集（**TOP-Bench**）。对多个 LLM Agent 的实证评估表明，无论是在最终回复中还是在推理轨迹中，都存在大量的隐私泄露。研究进一步证明，仅靠提示词的安全防护是不够的，并提出了一种新颖的监督微调与直接偏好优化方法（**TOP-Align**），以有效地学习更安全的任务完成边界。

---

## 📌 元数据 (Metadata)
* **arXiv ID:** [arXiv:2512.16310 [cs.CR]] (v4)
* **Primary Subject:** Cryptography and Security (`cs.CR`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
* **Authors:** Yuxuan Qiao, Dongqin Liu, Hongchang Yang, Wei Zhou, Songlin Hu
* **Publication Venue:** Accepted to EMNLP 2026 Findings
* **Submitted / Revised:** Submitted Dec 18, 2025; Last revised Sep 2, 2026
* **Resources & Code:** [GitHub Repository (TOP-R)](https://github.com/1Ponder/TOP-R) | [DOI](https://doi.org/10.48550/arXiv.2512.16310)

> * **arXiv ID:** [arXiv:2512.16310 [cs.CR]] (v4)
> * **Primary Subject:** Cryptography and Security (`cs.CR`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
> * **Authors:** Yuxuan Qiao, Dongqin Liu, Hongchang Yang, Wei Zhou, Songlin Hu
> * **Publication Venue:** Accepted to EMNLP 2026 Findings
> * **Submitted / Revised:** Submitted Dec 18, 2025; Last revised Sep 2, 2026
> * **Resources & Code:** [GitHub Repository (TOP-R)](https://github.com/1Ponder/TOP-R) | [DOI](https://doi.org/10.48550/arXiv.2512.16310)

---

## 📑 摘要正文 (Abstract)
LLM agents can combine individually non-revealing tool returns and disclose a sensitive conclusion, creating Tools Orchestration Privacy Risk (TOP-R). We formalize TOP-R through three conditions: 
1. Conclusion sensitivity
2. Single-source non-inferability
3. Compositional inferability

We introduce Library-Grounded Reverse-Inference Seed Expansion (LRSE), a four-library reverse-construction pipeline, and use it to build TOP-Bench, a 1,000-instance benchmark evaluated under a controlled two-stage tool-use protocol. Across six LLM agents, average task completion, leakage, and H-score are 98.0 percent, 88.6 percent, and 20.4. 

With native reasoning enabled, four models average 81.4 percent final-response leakage and 82.4 percent reasoning-trace leakage. With reasoning disabled, three prompt-only safeguards improve H-score by an average of about 3.4 points on TOP-Bench. We further propose TOP-Align, an SFT+DPO method for learning safer task-completion boundaries. On a separate post-training evaluation set, TOP-Align improves H-score by 16.2 points over the base model, versus a 5.0-point average gain from prompt-only mitigation on the same set. These results show that TOP-R requires defenses beyond prompting alone.

> LLM Agent 可以将单独来看不具泄露性的工具返回结果组合起来，并披露敏感结论，从而产生工具编排隐私风险（TOP-R）。我们通过三个条件将 TOP-R 形式化：
> 1. 结论敏感性
> 2. 单源不可推理性
> 3. 组合可推理性
> 
> 我们引入了基于库的逆向推理种子扩展（Library-Grounded Reverse-Inference Seed Expansion, 简称 LRSE），这是一个四库逆向构建流水线，并用它构建了 TOP-Bench——一个包含 1,000 个实例的基准测试集，并在受控的两阶段工具使用协议下进行评估。在六个 LLM Agent 中，平均任务完成率、泄露率和 H 分数分别为 98.0%、88.6% 和 20.4。
> 
> 在启用原生推理的情况下，四个模型的平均最终回复泄露率为 81.4%，推理轨迹泄露率为 82.4%。在禁用推理的情况下，三种仅基于提示词的防护措施在 TOP-Bench 上的 H 分数平均提高了约 3.4 分。我们进一步提出了 TOP-Align，这是一种用于学习更安全任务完成边界的 SFT+DPO 方法。在单独的后训练评估集上，与同一数据集上仅靠提示词缓解获得的 5.0 分平均增幅相比，TOP-Align 使 H 分数比基础模型提高了 16.2 分。这些结果表明，应对 TOP-R 需要超越单纯提示词的防御机制。

---

## 🔍 核心贡献与方法论 (Key Contributions & Methodology)
* **Formalization of TOP-R:** Clearly defines the mechanism through which isolated, innocuous tool outputs can be synthesized to compromise user or system privacy.
* **LRSE Pipeline & TOP-Bench:** Develops the Library-Grounded Reverse-Inference Seed Expansion pipeline to construct TOP-Bench, a comprehensive 1,000-instance benchmark.
* **Evaluation Framework:** Tests six state-of-the-art LLM agents under a controlled two-stage tool-use protocol, uncovering high rates of leakage across both final outputs and internal reasoning traces.
* **TOP-Align Mitigation Strategy:** Introduces a combined Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) framework that significantly outperforms traditional prompt-based mitigations in establishing secure operational boundaries.

> * **TOP-R 的形式化定义：** 明确定义了孤立、无害的工具输出如何被综合利用以危害用户或系统隐私的机制。
> * **LRSE 流水线与 TOP-Bench：** 开发了基于库的逆向推理种子扩展流水线，用以构建包含 1,000 个实例的全面基准测试集 TOP-Bench。
> * **评估框架：** 在受控的两阶段工具使用协议下测试了六个先进的 LLM Agent，发现在最终输出和内部推理轨迹中均存在极高的泄露率。
> * **TOP-Align 缓解策略：** 引入了一个结合了监督微调（SFT）和直接偏好优化（DPO）的框架，在建立安全操作边界方面，其性能显著优于传统的基于提示词的缓解方法。