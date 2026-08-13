---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 代码理解
- 大语言模型
- Eclipse插件
- 软件工程
- 依赖图谱
title: Comprendia：AI 增强的代码理解工具
---
### 文章背景与核心概要
在大型软件开发和维护过程中，理解复杂的代码库一直是开发者面临的核心痛点之一。传统的代码导航工具往往局限于文本或简单的目录树，缺乏对深层结构关系的直观展示；而新兴的基于大语言模型（LLM）的编码助手虽然能够解释局部代码，但常常缺乏全局上下文，且容易产生幻觉。

为了解决这一挑战，来自学术界的研究人员开发了 **Comprendia**——一款专为 Eclipse 设计的插件。该工具通过将结构化依赖关系可视化与大语言模型驱动的代码解释无缝结合，在共享的交互式图谱上全面提升 Java 程序的理解效率。Comprendia 建立在四大核心支柱之上：多边类型依赖图谱、图感知的被调用者修剪（GACP）大语言模型解释、代码克隆检测叠加层以及 CVE 安全风险叠加层。该研究已被软件工程领域顶级会议 ICSME 2026 的工具演示与数据展板赛道（Tool Demonstration and Data Showcase Track）所接收。

---

## 摘要 (Summary)

**Comprendia** 是一款 Eclipse 插件，旨在通过将结构化依赖可视化与 LLM 驱动的代码解释相结合，在共享的交互式图谱上提升 Java 程序的理解能力。该工具依赖于四大支柱：多边类型依赖图谱、图感知 LLM 解释、克隆检测叠加层以及 CVE 风险叠加层。Comprendia 已被 **ICSME 2026 工具演示与数据展板赛道** 接收，它能够帮助开发者分析复杂的项目，同时让开发者始终牢牢掌控控制权。

> **Comprendia** is an Eclipse plugin designed to improve Java program comprehension by combining structural dependency visualization with LLM-powered code explanations on a shared, interactive graph. The tool rests on four main pillars: a multi-edge-type dependency graph, graph-aware LLM explanations, a clone-detection overlay, and a CVE risk overlay. Accepted at the **ICSME 2026 Tool Demonstration and Data Showcase Track**, Comprendia helps developers analyze complex projects while keeping them firmly in control.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2608.10290](https://arxiv.org/abs/2608.10290) [cs.SE]
* **作者 (Authors):** Costain Nachuma, Minhaz F. Zibran
* **提交时间 (Submitted):** 2026年8月10日
* **主学科 (Primary Subject):** 软件工程 (`cs.SE`)
* **其他学科 (Other Subjects):** 人工智能 (`cs.AI`)、人机交互 (`cs.HC`)、编程语言 (`cs.PL`)
* **会议 (Conference):** 已被 ICSME 2026 接收（工具演示与数据展板赛道）
* **相关链接 (Links):** 
  * [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.10290)
  * [HTML 版本 (HTML Version)](https://arxiv.org/html/2608.10290v1)
  * [屏幕录像演示 (Screencast Demo)](https://youtu.be/1wlh_RYehzA)

---

## 摘要详情 (Abstract)

Comprendia 是一款 Eclipse 插件，它在共享的交互式图谱上集成了结构化依赖可视化与基于 LLM 的代码解释，用于 Java 程序理解。该工具基于四个支柱：

1. **多边依赖图谱（Multi-Edge Dependency Graph）：** 配备了实时搜索和多种可视化布局的多边类型依赖图谱。
2. **图感知被调用者修剪（Graph-Aware Callee Pruning, GACP）：** 基于 GACP 的 LLM 解释，这是一种可审计的策略，它使用开发者所导航的完全相同的图来选择相关的被调用者。GACP 利用图距离、继承折叠和边类型加权来生成在各个 LLM 家族中可复现、且可追溯到可见图节点的提示词。
3. **克隆检测叠加层（Clone-Detection Overlay）：** 一个视觉叠加层，用于突出显示代码重复并建议提取到父类（extract-to-parent）的重构机会。
4. **CVE 风险叠加层（CVE Risk Overlay）：** 由 [OSV.dev](http://OSV.dev) 提供支持的安全风险叠加层。

作者在一个包含已知代码克隆和漏洞的 Java 项目上演示了 Comprendia，展示了统一的图谱基础如何在保持开发者主导权的同时支持代码理解。

> Comprendia is an Eclipse plugin that integrates structural dependency visualization with LLM-powered code explanation on a shared interactive graph for Java program comprehension. The tool rests on four pillars: 
> 
> 1. **Multi-Edge Dependency Graph:** A multi-edge-type dependency graph equipped with live search and multiple visualization layouts.
> 2. **Graph-Aware Callee Pruning (GACP):** LLM explanations grounded in GACP, an auditable strategy that selects relevant callees using the exact same graph the developer navigates. GACP uses graph distance, inheritance collapse, and edge-type weighting to produce prompts that are reproducible across LLM families and traceable to visible graph nodes.
> 3. **Clone-Detection Overlay:** A visual overlay that highlights code duplication and suggests extract-to-parent refactoring opportunities.
> 4. **CVE Risk Overlay:** A security risk overlay powered by [OSV.dev](http://OSV.dev).
> 
> The authors demonstrate Comprendia on a Java project containing known clones and vulnerabilities, showing how the unified graph substrate supports comprehension while keeping the developer in control.