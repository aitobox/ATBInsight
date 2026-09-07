---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 金融AI
- 智能体评估
- 分布式系统
- 终局性
- FinalityBench
title: FinalityBench：评估智能体在延迟与冲突金融终局性下决策的效果级基准
---
### 文章背景与核心概要
现代企业金融系统经常受到分布式不一致性的困扰：由于消息延迟、重复、丢包和乱序，商户的支付处理器、账本、ERP和银行流水在不同时间接收到消息。因此，这些系统可能会在数分钟内对同一笔订单持有完全矛盾的认知状态。

为了测试AI智能体在如此多变条件下的决策能力，本文推出了 **FinalityBench**——一个全新且可执行的基准测试。FinalityBench 不仅评估抽象推理，还根据特权参考基准测量智能体选择的**实际执行货币效果**（例如发货、重新提交扣款、退款或等待）。

本研究通过隐藏式规范日志、效果级评分以及严谨的任务语料库（包含321个任务），深入评估了9种程序化策略以及大语言模型（LLM）在面对金融终局性延迟时的表现。实验表明，诸如运行时门控（Gating）等机制能够有效防止不可逆操作带来的经济损失，而未经专门指令的LLM也能够自发发现最优的终局性门控策略。

---

# FinalityBench：评估智能体在延迟与冲突金融终局性下决策的效果级基准 (FinalityBench: An Effect-Level Benchmark for Agent Decisions Under Delayed and Conflicting Financial Finality)

**作者：** Abhishek Sharma  
**提交时间：** 2026年9月4日  
**主要学科：** 人工智能 (`cs.AI`)  
**arXiv：** [2609.04706](https://arxiv.org/abs/2609.04706)  

---

## 📌 执行摘要 (Executive Summary)

> Modern enterprise financial systems often suffer from distributed inconsistencies: a merchant's payment processor, ledger, ERP, and bank feed receive messages at varying times due to delays, duplicates, drops, and reorderings. Consequently, these systems can hold contradictory beliefs about the exact same order for minutes at a time. 

现代企业金融系统经常受到分布式不一致性的困扰：由于消息延迟、重复、丢包和乱序，商户的支付处理器、账本、ERP和银行流水在不同时间接收到消息。因此，这些系统可能会在数分钟内对同一笔订单持有完全矛盾的认知状态。

> **FinalityBench** is a novel, executable benchmark designed to test AI agent decision-making under such volatile conditions. Rather than evaluating abstract reasoning, FinalityBench measures the **executed monetary effects** of an agent's choices (such as shipping goods, re-submitting a capture, issuing a refund, or waiting) relative to a privileged reference baseline. 

**FinalityBench** 是一个全新且可执行的基准测试，旨在测试AI智能体在此类多变条件下的决策能力。FinalityBench 不评估抽象推理，而是根据特权参考基准（privileged reference baseline）来衡量智能体各项选择所产生的**实际执行货币效果**（例如发货、重新提交扣款、退款或等待）。

---

## 🔍 核心基准特征 (Key Benchmark Features)

> * **Hidden Canonical Log:** Maintains a single ground-truth event log, deriving each separate system's view via independent faulted delivery streams. Disagreements arise naturally from specified fault semantics rather than hand-authored scenarios.

* **隐藏规范日志（Hidden Canonical Log）：** 维护单一的真实事件日志，通过独立的故障投递流推导各个独立系统的视图。系统间的分歧自然地源于特定的故障语义，而不是人工编造的场景。

> * **Effect-Level Grading:** Episodes are scored based on the merchant's terminal economic position against a privileged reference that knows when pending captures eventually resolve.

* **效果级评分（Effect-Level Grading）：** 根据商户的终端经济地位进行评分，并将其与知晓待处理扣款最终何时解决的特权参考基准进行对比。

> * **Rigorous Task Corpus:** Features 321 total tasks, including **45 twin pairs (90 tasks)**. These twins share identical system views at the decision instant and return unknown from authoritative probes, yet demand different eventual correct dispositions. Snapshot indistinguishability is actively checked across evaluation seeds.

* **严谨的任务语料库（Rigorous Task Corpus）：** 包含总计 321 个任务，其中包括 **45 对双胞胎任务（共 90 个任务）**。这些双胞胎任务在决策瞬间共享相同的系统视图，并且从权威探测中返回未知状态，但它们需要不同的最终正确处置方案。系统会在各个评估种子（seeds）上主动检查快照的不可区分性。

---

## 📊 发现总结 (Summary of Findings)

> * **Performance Discrepancies:** Across 14,445 graded episodes evaluated against nine programmatic policies, single-task accuracy rankings diverged significantly from paired loss metrics in 7 instances. For example, a *"ship-on-first-sign"* policy ranked second-best in raw accuracy (65.7%) but performed the worst in the suite by paired loss because it fails to distinguish between twin task members.

* **性能差异（Performance Discrepancies）：** 在针对九种程序化策略进行评估的 14,445 个评分片段中，单任务准确率排名在 7 个实例中与配对损失指标存在显著分歧。例如，“见首个信号即发货”（*ship-on-first-sign*）策略在原始准确率上排名第二（65.7%），但由于它无法区分双胞胎任务成员，在配对损失评估中表现最差。

> * **The Power of Gating:** A runtime gating mechanism that blocks irreversible actions until an authoritative finality probe resolves achieved an impressive **85.4% accuracy** and lost nothing to secondary passes. Its residual loss stemmed almost entirely from a single archetype that directly prices finality information.

* **门控的力量（The Power of Gating）：** 运行时门控机制（在权威终局性探测解决之前阻止不可逆操作）实现了高达 **85.4% 的准确率**，并且在二次通过中没有任何损失。其剩余损失几乎完全源于一种直接对终局性信息进行定价的单一原型。

> * **Language Model Capabilities:** Uninstructed Large Language Models (LLMs) matched the exact success rate of the hand-written rule-based gate on a stratified subset. While they incurred roughly twice the monetary loss, the LLMs organically discovered the optimal finality-gating strategy without explicit instruction.

* **大语言模型能力（Language Model Capabilities）：** 在分层子集上，未经专门指令的大语言模型（LLM）达到了与手写基于规则的门控完全相同的成功率。尽管它们的货币损失大约高出一倍，但 LLM 在没有明确指令的情况下，自发地发现了最优的终局性门控策略。

---

## 🔗 资源与附加链接 (Resources & Additional Links)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2609.04706) | [Experimental HTML](https://arxiv.org/html/2609.04706v1) | [TeX Source](https://arxiv.org/src/2609.04706)

* **全文选项：** [查看 PDF](https://arxiv.org/pdf/2609.04706) | [实验性 HTML](https://arxiv.org/html/2609.04706v1) | [TeX 源码](https://arxiv.org/src/2609.04706)

> * **Code & Data Repository:** [GitHub Repository](https://github.com/abhisheksharma2411/finalitybench)

* **代码与数据仓库：** [GitHub 仓库](https://github.com/abhisheksharma2411/finalitybench)

> * **Zenodo Archive:** [DOI: 10.5281/zenodo.22262591](https://doi.org/10.5281/zenodo.22262591)

* **Zenodo 归档：** [DOI: 10.5281/zenodo.22262591](https://doi.org/10.5281/zenodo.22262591)

> * **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

* **许可协议：** [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">