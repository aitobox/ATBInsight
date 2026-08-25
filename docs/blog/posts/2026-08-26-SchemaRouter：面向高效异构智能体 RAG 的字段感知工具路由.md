---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- RAG
- 智能体
- 工具路由
- 知识图谱
- 检索增强生成
title: SchemaRouter：面向高效异构智能体 RAG 的字段感知工具路由
---
### 文章背景与核心概要

异构智能体检索增强生成（RAG）系统通常需要协调多种外部 API、内部数据库、向量存储和图数据库。传统的工具选择方法（如将所有工具描述暴露给大模型，或仅依赖向量相似度）往往面临“过度获取”导致的高延迟与高 Token 消耗，以及“获取不足”导致的信息缺失等关键问题。

本文提出了 **SchemaRouter**，这是一个轻量级的路由层，它将工具、端点、参数、响应字段、领域概念、单位、来源及许可策略建模为一个互联的模式图（Schema Graph）。通过结合轻量级 LLM 的意图提取与图上的确定性字段投影，SchemaRouter 在大幅降低 Token 消耗和延迟的同时，显著提升了工具匹配的精确度，并首次实现了对数据来源和许可策略的有效溯源。

---

## 执行摘要

异构智能体检索增强生成（RAG）系统经常需要协调各种外部 API、内部数据库、向量存储和图存储。传统方法——例如将所有工具描述暴露给 LLM，或严格依赖向量相似度进行工具选择——通常会遭遇两种关键的失效模式：
1. **过度获取（Over-fetching）：** 增加了负载大小，消耗了更多 Token，并增加了延迟。
2. **获取不足（Under-fetching）：** 遗漏了制定准确答案所需的关键字段。

为了解决这些挑战，本文引入了 **SchemaRouter**，这是一个轻量级的路由层，它将工具、端点、参数、响应字段、领域概念、单位、来源和许可策略建模为一个互联的模式图。

> Heterogeneous agentic retrieval-augmented generation (RAG) systems frequently coordinate a mix of external APIs, internal databases, vector stores, and graph stores. Traditional approaches—such as exposing all tool descriptions to an LLM or relying strictly on vector similarity for tool selection—typically suffer from two critical failure modes:
> 1. **Over-fetching:** Inflates payload sizes, increases token consumption, and adds latency.
> 2. **Under-fetching:** Omits essential fields required to formulate accurate answers.
>
> To resolve these challenges, this paper introduces **SchemaRouter**, a lightweight routing layer that models tools, endpoints, parameters, response fields, domain concepts, units, provenance, and license policies as an interconnected schema graph.

---

## 核心方法论

* **模式图表示：** 将端点、参数、领域概念、响应字段、单位以及治理策略（来源和许可）整合为一个统一的图结构。
* **混合路由流水线：**
    * 轻量级 LLM 提取核心用户意图、相关领域概念和源约束。
    * 通过意图组投影和基于别名层的概念-字段匹配，在图上确定性地执行字段选择。

> * **Schema Graph Representation:** Combines endpoints, parameters, domain concepts, response fields, units, and governance policies (provenance and licenses) into a unified graph.
> * **Hybrid Routing Pipeline:** 
>   * A lightweight LLM extracts the core user intent, relevant domain concepts, and source constraints.
>   * Field selection is executed deterministically over the graph leveraging intent-group projection and concept-field matching via an alias layer.

---

## 实证性能与基准测试结果

在包含 110 个查询的材料科学基准测试中，**SchemaRouter** 在多项指标上表现强劲：

* **答案准确性：** 准确率达到 **0.71**，与“全量获取”基准持平（在重叠置信区间内），并优于“提示所有”基准的 **0.66**。
* **Token 效率：** 仅消耗 **227 个检索上下文 Token**，而“全量获取”方法则需要 **2,066 个 Token**。
* **延迟：** 端到端延迟比“提示所有”策略降低了 **2.7 倍**。
* **精确度与有效性：** 工具精确匹配率高达 **0.93**，参数有效性得分达到 **1.0**。
* **治理溯源：** 在 **62% 的答案**中成功关联了来源和许可元数据，而所有基准方法在该指标上几乎为 **0%**。

### 消融实验洞察
研究指出，过度最小化所选字段的数量会适得其反：这会将答案准确率降至 **0.56** 且几乎没有节省 Token，而保留召回率的投影方法则成功恢复了峰值准确率。

> Evaluated on a materials-science benchmark comprising 110 queries, **SchemaRouter** demonstrated strong performance across several metrics:
>
> * **Answer Accuracy:** Achieves an accuracy score of **0.71**, matching the "fetch-everything" baseline (within overlapping confidence intervals) and outperforming the "prompt-all" baseline score of **0.66**.
> * **Token Efficiency:** Consumes only **227 retrieved-context tokens** compared to **2,066 tokens** for the fetch-everything approach.
> * **Latency:** Delivers **2.7× lower end-to-end latency** than the prompt-all strategy.
> * **Precision & Validity:** Attains the highest tool-exact match rate of **0.93** and a parameter validity score of **1.0**.
> * **Governance Grounding:** Successfully grounds provenance and license metadata in **62% of answers**, compared to approximately **0%** across all baseline methods.
>
> ### Ablation Insight
> The study notes that aggressively minimizing the count of selected fields is counterproductive: it drops answer accuracy to **0.56** with negligible token savings, whereas recall-preserving projection successfully restores peak accuracy.

---

## 许可与资源

* **许可：** [<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

> * **License:** [<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)