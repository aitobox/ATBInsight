---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- AI智能体
- 遥测技术
- 故障诊断
- 基准测试
- 可观测性
title: TelemetrySuffBench：智能体遥测数据是否足以进行故障根源诊断？
---
### 文章背景与核心概要
随着基于智能体（Agent-based）的系统日益普及，从执行轨迹中诊断故障根源的能力变得至关重要。本文引入了 **TelemetrySuffBench**，这是一个受控的基准测试，旨在评估当前的智能体遥测数据是否足以识别故障的根本原因。

研究揭示了一个显著的**检测-定位鸿沟（detection-localization gap）**：虽然现代语言模型在检测故障是否发生方面非常高效，但它们在准确查明该故障的具体成因时却举步维艰。研究表明，可靠的因果归因需要决策与溯源之间建立明确的链接，同时需要健全的拒绝回答保障机制（abstention safeguards），以处理证据不足的模糊情况。

---

# TelemetrySuffBench：智能体遥测数据是否足以进行故障根源诊断？

> # TelemetrySuffBench: Is Agent Telemetry Sufficient for Failure-Origin Diagnosis?

**作者：** Yuxuan Zhu, Peng Pu  
**日期：** 2026年8月8日  
**学科：** 人工智能 (cs.AI)  
**arXiv ID:** [2608.07899](https://arxiv.org/abs/2608.07899)

> **Authors:** Yuxuan Zhu, Peng Pu  
> **Date:** August 8, 2026  
> **Subject:** Artificial Intelligence (cs.AI)  
> **arXiv ID:** [2608.07899](https://arxiv.org/abs/2608.07899)

---

## 摘要

随着基于智能体的系统日益普及，从执行轨迹中诊断故障根源的能力变得至关重要。本文引入了 **TelemetrySuffBench**，这是一个受控的基准测试，旨在评估当前的智能体遥测数据是否足以识别故障的根本原因。

研究揭示了一个显著的**检测-定位鸿沟**：虽然现代语言模型在检测故障是否发生方面非常高效，但它们在准确查明该故障的具体成因时却举步维艰。研究表明，可靠的因果归因需要决策与溯源之间建立明确的链接，同时需要健全的拒绝回答保障机制，以处理证据不足的模糊情况。

> ## Summary
> As agent-based systems become more prevalent, the ability to diagnose the origin of failures from execution traces has become critical. This paper introduces **TelemetrySuffBench**, a controlled benchmark designed to evaluate whether current agent telemetry is sufficient for identifying the root cause of failures.
> 
> The research highlights a significant **detection-localization gap**: while modern language models are highly effective at detecting that a failure has occurred, they struggle to accurately pinpoint the specific origin of that failure. The study demonstrates that reliable causal attribution requires explicit links between decisions and provenance, as well as robust abstention safeguards to handle ambiguous cases where evidence is insufficient.

---

## 核心发现

*   **检测-定位鸿沟：** 尽管模型在故障检测方面取得了很高的 F1 分数（99.5%–100%），但在使用标准遥测格式（OpenTelemetry/OpenInference）时，它们在识别具体起源步骤上的准确率却显著下降，有时甚至降至 0.5%。
*   **内容的重要性：** 消融实验表明，从遥测数据中移除“决策内容”会使起源步骤的准确率降至零，而移除溯源信息则会导致性能大幅下降。
*   **安全拒绝机制：** 在面对证据模糊的情况时，模型是否能够拒绝回答表现出强烈依赖模型的差异。“证据门控”（Evidence gating）被证明可以在表现最好的模型中将无支撑的回答减少 12.5 到 48.6 个百分点。
*   **基准测试设计：** 该基准测试利用了带有延迟绑定故障（delayed-binding faults）的典型多组件追踪，为测试故障检测、故障源定位和安全拒绝提供了严谨的环境。

> ## Key Findings
> 
> *   **The Detection-Localization Gap:** While models achieve high F1 scores (99.5%–100%) in failure detection, their accuracy in identifying the specific origin step drops significantly, often to as low as 0.5% when using standard telemetry formats (OpenTelemetry/OpenInference).
> *   **Importance of Content:** Ablation studies reveal that removing "decision content" from telemetry reduces origin-step accuracy to zero, while removing provenance information leads to substantial performance degradation.
> *   **Safe Abstention:** There is a strong model-dependent variance in the ability to abstain from answering when evidence is ambiguous. "Evidence gating" was shown to reduce unsupported answers by 12.5 to 48.6 percentage points in top-performing models.
> *   **Benchmark Design:** The benchmark utilizes canonical multi-component traces with delayed-binding faults, providing a rigorous environment to test failure detection, fault-origin localization, and safe abstention.

---

## 资源

*   **论文访问：** [查看 PDF](https://arxiv.org/pdf/2608.07899) | [HTML（实验性）](https://arxiv.org/html/2608.07899v1)
*   **代码与数据：** [TelemetrySuffBench 仓库](https://anonymous.4open.science/r/TelemetrySuffBench-E635/README.md)

> ## Resources
> *   **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.07899) | [HTML (Experimental)](https://arxiv.org/html/2608.07899v1)
> *   **Code & Data:** [TelemetrySuffBench Repository](https://anonymous.4open.science/r/TelemetrySuffBench-E635/README.md)

---

## 元数据

*   **评论：** 10 页，3 张图表，4 个表格
*   **DOI:** [10.48550/arXiv.2608.07899](https://doi.org/10.48550/arXiv.2608.07899)

> ## Metadata
> *   **Comments:** 10 pages, 3 figures, 4 tables
> *   **DOI:** [10.48550/arXiv.2608.07899](https://doi.org/10.48550/arXiv.2608.07899)