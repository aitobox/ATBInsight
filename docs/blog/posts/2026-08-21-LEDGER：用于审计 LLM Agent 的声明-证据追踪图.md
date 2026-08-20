---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- LLM Agent
- 可解释性
- 审计系统
- 追踪图
- 人机交互
title: LEDGER：用于审计 LLM Agent 的声明-证据追踪图
---
### 文章背景与核心概要

随着大语言模型（LLM）Agent 在处理长周期技术工作流（如复杂工具调用、代码执行及文件编辑）方面的能力不断增强，生产力的瓶颈已从“生成内容”转向“审计与验证”。现有的可观测性系统虽然能记录细粒度的执行事件，但往往缺乏逻辑关联，导致人工审计者难以梳理出哪些操作和产物支撑了最终结论。

本文提出的 **LEDGER**（执行审查的分层证据与决策图）系统，通过构建分层追踪图解决了这一难题。该系统将追踪记录归纳为“证据节点”和“工作流节点”，并将产物作为证据锚点，通过语义边将 Agent 的声明与支撑证据连接起来。这种方法不仅提升了复杂工作流的透明度，还为实现以证据为中心的自动化审计提供了有效路径。

---

# LEDGER：用于审计 LLM Agent 的声明-证据追踪图

## 摘要
> Large language model (LLM) agents are increasingly capable of executing long-horizon technical workflows involving complex tool use, code execution, file editing, and artifact generation. However, as agent productivity increases, the primary bottleneck shifts from generation to auditing—specifically, determining whether agent outputs are correct and trustworthy. 

大语言模型（LLM）Agent 现在能够执行涉及复杂工具使用、代码执行、文件编辑和生成产物的长周期技术工作流。随着 Agent 工作效率的提升，生产力的瓶颈已从产出内容转向审计这些产出是否正确且值得信赖。

> While existing agent observability systems provide visibility into fine-grained execution events, they often leave reviewers struggling to reconstruct which actions, artifacts, and validation steps are relevant to a particular conclusion. To address this, the authors introduce **LEDGER** (Layered Evidence and Decision Graphs for Execution Review), a novel tracing and review system designed to build layered trace graphs over observed agent sessions. By grouping trace records into Evidence Nodes and Workflow Nodes, anchoring artifacts, and connecting claims to supporting evidence via typed semantic edges, LEDGER facilitates evidence-centered audits for complex workflows.

现有的 Agent 可观测性系统虽然提供了细粒度执行事件的可见性，但仅凭这些信息，审查者仍难以重构出哪些操作、产物和验证步骤对特定结论至关重要。为了解决这一问题，作者引入了 **LEDGER**（执行审查的分层证据与决策图），这是一种新型追踪与审查系统，旨在为观测到的 Agent 会话构建分层追踪图。通过将追踪记录归组为证据节点和工作流节点，将产物作为证据锚点，并利用类型化的语义边将声明与支撑性的操作、产物及检查连接起来，LEDGER 为复杂工作流的证据中心化审计提供了便利。

---

## 论文元数据

* **arXiv 标识符：** [arXiv:2608.18398](https://arxiv.org/abs/2608.18398) [cs.HC]
* **标题：** LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents
* **作者：** Daehong Kim, Haichao Miao, Shusen Liu
* **提交日期：** 2026年8月19日
* **主要学科：** 人机交互 (`cs.HC`)
* **次要学科：** 人工智能 (`cs.AI`)
* **许可协议：** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 摘要 (原文)
> Large language model (LLM) agents can now carry out long-horizon technical workflows involving complex tool use, code execution, file edits, and generated artifacts. As agents do more work faster, the productivity bottleneck shifts from producing outputs to auditing whether those outputs are correct and trustworthy. Agent observability systems make fine-grained execution events visible, but visibility alone still leaves reviewers to reconstruct which actions, artifacts, and validation steps matter for a particular conclusion. 
>
> We introduce **LEDGER** — *Layered Evidence and Decision Graphs for Execution Review*, a tracing and review system that builds layered trace graphs over observed agent sessions. LEDGER preserves Trace Records while grouping them into Evidence Nodes and Workflow Nodes, representing artifacts as evidence anchors, and adding typed semantic edges that connect claims to supporting actions, artifacts, and checks. Through data-analysis and coding examples, we show how the resulting traces expose workflow decisions, artifact lineage, repair steps, validation coverage, and claim-support paths for evidence-centered audit.

---

## 分类详情
* **MSC 分类：** 68T42, 68U35
* **ACM 分类：** H.5.2; I.2.11; I.2.7; H.1.2
* **DOI：** [10.48550/arXiv.2608.18398](https://doi.org/10.48550/arXiv.2608.18398)

---

## 访问链接与资源
* **全文：** [查看 PDF](https://arxiv.org/pdf/2608.18398) | [HTML (实验性)](https://arxiv.org/html/2608.18398v1) | [TeX 源码](https://arxiv.org/src/2608.18398)
* **引用与参考：** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18398)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18398)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18398)