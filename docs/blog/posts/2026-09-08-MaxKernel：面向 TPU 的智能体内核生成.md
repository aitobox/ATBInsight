---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- TPU
- LLM
- 智能体
- 代码生成
- 性能优化
title: MaxKernel：面向 TPU 的智能体内核生成
---
### 文章背景与核心概要
长期以来，为硬件加速器设计高性能的自定义内核需要深厚且专业的硬件工程专长。为此，本文推出了 **MaxKernel**，这是一个由大语言模型（LLM）和实时编译器反馈驱动的多智能体系统，旨在实现 TPU 内核生成的自动化与优化。该框架具备三种核心开发范式：人类参与回路（HITL）智能体、全自动（Auto）智能体以及基于图的自主搜索。

这些范式共享一个由子智能体组成的协作池，分别专注于规划、实现、自我调试、测试以及硬件性能分析。经过在 *JaxBench*（包含 50 个多样化 TPU 内核任务的基准测试套件）以及来自最先进开源模型的真实工作负载上的评估，MaxKernel 持续稳定地生成了达到专家级水平、高度优化的实现方案。

---

## 摘要

> ## Summary
> Designing high-performance custom kernels for hardware accelerators traditionally requires deep, specialized hardware expertise. **MaxKernel** introduces a multi-agent system powered by Large Language Models (LLMs) and real-time compiler feedback to automate and optimize TPU kernel generation. The framework features three core development paradigms:
> 1. **Human-in-the-Loop (HITL) Agent:** Enables collaborative, step-by-step kernel design.
> 2. **Autonomous (Auto) Agent:** Executes a fully automated, metric- and trace-driven optimization loop.
> 3. **Graph-Based Autonomous Search:** Scales the Auto agent for global exploration across the entire design space.
> 
> These paradigms share a collaborative pool of sub-agents dedicated to planning, implementation, self-debugging, testing, and hardware profiling. Evaluated on *JaxBench* (a suite of 50 diverse TPU kernel tasks) alongside real-world workloads from state-of-the-art open-source models, MaxKernel consistently generates expert-level, highly optimized implementations.

---

## 文档元数据

> ## Document Metadata

| 元数据字段 | 详情 |
| :--- | :--- |
| **arXiv 标识符** | [arXiv:2609.04523](https://arxiv.org/abs/2609.04523) [cs.AI] |
| **学科分类** | 人工智能 (`cs.AI`)；性能 (`cs.PF`)；编程语言 (`cs.PL`) |
| **提交日期** | 2026年9月3日 |
| **篇幅** | 14 页，6 幅图，4 个表格 |
| **作者** | Shangkun Wang, Nina Cai, Charles Hoong, Julian Walker, Gerson Kroiz, George Vanica, Deepak Patil, Andi Gavrilescu, Hassan Sipra, Sethu Sankaran |
| **源代码** | [GitHub 仓库](https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel) |

---

## 访问与全文链接

> ## Access & Full-Trust Links

* **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2609.04523)
* **HTML 版本：** [HTML（实验性）](https://arxiv.org/html/2609.04523v1)
* **TeX 源码：** [arXiv 源码文件](https://arxiv.org/src/2609.04523)
* **许可协议：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)