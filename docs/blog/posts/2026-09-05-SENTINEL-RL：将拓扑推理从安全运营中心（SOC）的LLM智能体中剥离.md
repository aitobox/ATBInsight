---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 大语言模型
- 安全运营中心
- 强化学习
- 图神经网络
- 网络安全
title: SENTINEL-RL：将拓扑推理从安全运营中心（SOC）的LLM智能体中剥离
---
### 文章背景与核心概要

在现代企业安全运营中心（SOC）中，大语言模型（LLM）智能体正日益被广泛用作自主分析师。然而，在企业级规模下，它们的发展受到两个根本性约束的阻碍：一是上下文窗口的限制，导致LLM无法在其有限的容量内处理包含数千台主机的认证图；二是缺乏拓扑保证，自由形式的文本生成无法确定性地保证所推荐的遏制操作与目标基础设施在拓扑结构上保持一致。

为了克服这些挑战，研究人员推出了 **Sentinel-RL**，这是一种将“拓扑推理”与“语义推理”解耦的智能体SOC架构。该架构利用异构图注意力编码器将动态认证子图总结为固定维度的状态，通过近端策略优化（PPO）引擎将其映射到受约束的有效操作中，并严格限制LLM仅用于处理策略推荐、生成人类可读的分析报告。实验结果表明，该系统在保证极高准确率的同时，将端到端遏制循环的延迟显著缩短至中位数 6.3 秒。

---

## 執行摘要 / Executive Summary

大语言模型 (LLM) 智能体正越来越多地被用作自主安全运营中心 (SOC) 分析师。然而，有两个基本限制阻碍了它们在企业规模下的可靠性：
1. **上下文窗口限制：** LLM 无法在其有限的上下文窗口内处理包含数千个主机的认证图。
2. **缺乏拓扑保证：** 自由形式的文本生成无法提供确定性的保证，即推荐的遏制操作与其目标基础设施在拓扑上保持一致。

为了克服这些挑战，研究人员引入了 **Sentinel-RL**，这是一种将*拓扑推理*与*语义推理*解耦的智能体 SOC 架构。

> Large Language Model (LLM) agents are increasingly utilized as autonomous Security Operations Center (SOC) analysts. However, two fundamental constraints hinder their reliability at enterprise scale:
> 1. **Context Window Limitations:** An LLM cannot process multi-thousand-host authentication graphs within its finite context window.
> 2. **Lack of Topological Guarantees:** Free-form text generation provides no deterministic assurance that a recommended containment action is topologically consistent with the infrastructure it targets.
> 
> To overcome these challenges, the researchers introduce **Sentinel-RL**, an agentic-SOC architecture that decouples *topological reasoning* from *semantic reasoning*.

---

## 核心架构组件 / Key Architectural Components

Sentinel-RL 在各个专业层之间分担职责，以确保速度、准确性和结构安全性：

* **拓扑编码器（Topological Encoder）：** 异构图注意力编码器将实时认证子图概括为固定维度的状态。
* **强化学习策略引擎（RL Policy Engine）：** 近端策略优化 (PPO) 策略将编码后的状态映射到一组受约束的有效调查和遏制操作。
* **语义 LLM 智能体与评论家（Semantic LLM Agent & Critic）：** LLM 被严格限制为仅消费策略的推荐、进行翻译，并生成通过验证评论家审查的人类可读分析师叙述。

> Sentinel-RL delegates responsibilities across specialized layers to ensure speed, accuracy, and structural safety:
> 
> * **Topological Encoder:** A heterogeneous graph attention encoder summarizes live authentication subgraphs into fixed-dimensional states.
> * **RL Policy Engine:** A Proximal Policy Optimization (PPO) policy maps the encoded states to a constrained set of valid investigative and containment actions.
> * **Semantic LLM Agent & Critic:** The LLM is strictly restricted to consuming the policy's recommendations, translating them, and producing human-readable analyst narratives that pass through a validation critic.

---

## 实证结果 / Empirical Results

该系统在 LANL 综合多源网络安全事件数据集和印第安纳大学 Quartz HPC 集群上进行了实例化和测试，取得了四项主要成果：

1. **摄取性能：** 两阶段的 `CREATE` 摄取模式在单个 32 核节点上仅用 **14.2 分钟** 就成功将包含 2400 万条边的认证子图加载到 Neo4j 中——大约比基于常规 `MERGE` 的流水线快 $24\times$。
2. **告警引擎速度：** 滑动窗口告警引擎在 50 次试验中，能够在 **$\le 2.5$ 秒** 内稳定触发 25 个事件/10 秒的阈值。
3. **PPO 收敛与准确率：** PPO 经过 200 次迭代训练，收敛到 $8.74 \pm 0.31$ 的平均单次回报，在标记的红队事件上实现了 **0.91** 的保留精确度和 **0.87** 的召回率。
4. **端到端延迟：** 集成的遏制循环在 **6.3 秒** 的中位时间内完成完整的*检测-调查-推荐-人工批准*循环。

> The system was instantiated and tested on the LANL Comprehensive, Multi-Source Cyber-Security Events dataset and the Indiana University Quartz HPC cluster, yielding four primary results:
> 
> 1. **Ingestion Performance:** A two-phase `CREATE` ingestion pattern successfully loaded a 24-million-edge authentication subgraph into Neo4j in **14.2 minutes** on a single 32-core node—roughly $24\times$ faster than canonical `MERGE`-based pipelines.
> 2. **Alert Engine Speed:** A sliding-window alert engine reliably trips a 25-event / 10-second threshold in **$\le 2.5$ seconds** across 50 trials.
> 3. **PPO Convergence & Accuracy:** PPO training over 200 iterations converged to a mean episodic return of $8.74 \pm 0.31$, achieving a held-out precision of **0.91** and a recall of **0.87** on labeled red-team events.
> 4. **End-to-End Latency:** The integrated containment loop completes a full *detect-investigate-recommend-human-approve* cycle in a median time of **6.3 seconds**.

---

## 贡献与工程洞察 / Contributions & Engineering Insights

除了核心架构之外，本文还贡献了几个可复用的部署和企业级模式：
* **高并发节点死锁解决方案（Hot-node deadlock workaround）：** 针对高并发图更新的强健工程模式。
* **锚点节点共址（Anchor-node co-location）：** 针对性能优化的可移植 HPC 部署模式。
* **企业就绪性分析（Enterprise-readiness analysis）：** 全面涵盖误报经济学、可逆性保证、审计合规性，以及人机回路批准的严格边界。

> Beyond the core architecture, the paper contributes several reusable deployment and enterprise patterns:
> * **Hot-node deadlock workaround:** A robust engineering pattern for high-concurrency graph updates.
> * **Anchor-node co-location:** A portable HPC deployment pattern optimized for performance.
> * **Enterprise-readiness analysis:** Comprehensive coverage of false-positive economics, reversibility guarantees, audit compliance, and the strict boundaries of human-in-the-loop approval.

---

*[通过 arXiv 查看 PDF](https://arxiv.org/pdf/2609.04159) | [实验性 HTML 版本](https://arxiv.org/html/2609.04159v1)*

> *[View PDF via arXiv](https://arxiv.org/pdf/2609.04159) | [Experimental HTML Version](https://arxiv.org/html/2609.04159v1)*