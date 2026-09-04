---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- Bioinformatics
- LLM Agents
- Multi-Agent Systems
- BixBench
- LAB-Bench 2
title: Bioinfoysis技术报告：面向长期生物信息学任务的持久化构件锚定多智能体系统
---
### 文章背景与核心概要
大语言模型（LLM）智能体在生物信息学领域展现出了巨大的应用潜力，然而现有的系统往往将规划、工具使用和代码执行视为仅关注最终答案的短暂交互。在需要结论严格追溯至底层数据、计算和中间证据的**长期生物信息学任务**中，这种范式往往会失效。

为了克服这一局限性，作者推出了 **Bioinfoysis**，这是一个创新的多智能体系统，它将每一个用户请求视为持久化的、*以构件为基础的分析运行*。通过将全局规划与逐步、以证据驱动的重新规划、受控运行时、特定角色上下文以及持久化记忆相结合，Bioinfoysis 取得了最先进的性能表现：在 BixBench 上达到了 **82.4%** 的准确率；在 LAB-Bench 2 (SeqQA2) 上，跨四个底层 LLM 的平均准确率从 **27.81% 跃升至 64.13%**；在 LAB-Bench 2 (DbQA2) 上，平均准确率从 **3.13% 跃升至 31.25%**。

---

# Bioinfoysis技术报告 (Bioinfoysis Technical Report)

> **arXiv:** [2609.03871](https://arxiv.org/abs/2609.03871) [cs.AI]  
> **Subjects:** Artificial Intelligence (`cs.AI`); Multiagent Systems (`cs.MA`)  
> **Submitted on:** 3 September 2026  
> **Authors:** Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang, Zihao Yang, Tong Ye, Yangqi Zhang, Jiakang Xu, Xiaoqing Yan, Xuan Luo, Keyi Li, Enci Fan, Kai Kang, Zhuohan Liu, Xingyu Jin, Chunran Teng, Tao Li, Xinyu Lv, Minghui Wang, Wenfeng Li, Yidan Gao, Siyu Liu, Mingrui Luo, Zhu Liang, Guanren Qiao, Zhiping Xu  
> **Links:** [View PDF](https://arxiv.org/pdf/2609.03871) | [HTML Version](https://arxiv.org/html/2609.03871v1) | [Demo Website](https://report.bioinfoysis.com/)

---

## 执行摘要 (Executive Summary)

虽然大语言模型（LLM）智能体在生物信息学中展现出巨大的潜力，但现有系统往往将规划、工具使用和代码执行视为仅关注最终答案的瞬时交互。这种范式在**长周期生物信息学任务**中会失效，因为在这些任务中，结论必须保持对底层数据、计算和中间证据的严格可追溯性。

为了克服这一局限性，作者引入了 **Bioinfoysis**，这是一个新颖的多智能体架构，将每个用户请求视为持久的、*以构件为基础的分析运行（artifact-grounded analysis run）*。通过将全局规划与逐步的、由证据驱动的重新规划、受控运行时、特定角色上下文以及持久记忆相结合，Bioinfoysis 实现了SOTA（最先进）的结果：
* **BixBench：** 实现了 **82.4%** 的 SOTA 准确率。
* **LAB-Bench 2 (SeqQA2)：** 在四个底层 LLM 上，平均准确率从 **27.81% 提高到 64.13%**。
* **LAB-Bench 2 (DbQA2)：** 在四个底层 LLM 上，平均准确率从 **3.13% 提高到 31.25%**。

> While large language model (LLM) agents show immense potential in bioinformatics, existing systems often treat planning, tool usage, and code execution as transient interactions focused purely on the final answer. This paradigm fails in **long-horizon bioinformatics tasks**, where conclusions must maintain rigorous traceability back to underlying data, computations, and intermediate evidence. 
> 
> To overcome this limitation, the authors introduce **Bioinfoysis**, a novel multi-agent harness that treats every user request as a persistent, *artifact-grounded analysis run*. By coupling global planning with step-wise, evidence-driven replanning, a controlled runtime, role-specific contexts, and persistent memory, Bioinfoysis achieves state-of-the-art results:
> * **BixBench:** Achieves a state-of-the-art accuracy of **82.4%**.
> * **LAB-Bench 2 (SeqQA2):** Increases average accuracy from **27.81% to 64.13%** across four underlying LLMs.
> * **LAB-Bench 2 (DbQA2):** Increases average accuracy from **3.13% to 31.25%** across four underlying LLMs.

---

## 核心架构与方法论 (Core Architecture and Methodology)

Bioinfoysis 依赖于一个复杂的框架，旨在保持严格的证据流和严谨的运行时执行：

1. **持久的构件锚定分析：** 请求被构建为持久的分析运行，其中数据和中间计算与相应的证据显式绑定。
2. **全局规划与逐步重新规划：** 该系统采用维护可执行检查表的规划器。待处理的步骤会在每次工作执行后返回的结构化交接（handoffs）帮助下不断修正。
3. **结构化交接：** 这些机制将中间结果直接绑定到负责的智能体、检查表步骤和计划生成。这防止了在计划修订后静默重用过时或陈旧的证据。
4. **受控运行时：** 在将生成的脚本、表格和图表用于下游分析或报告*之前*，自动对其进行验证。
5. **受控的生物信息学技能与记忆：** 利用特定角色的上下文、持久记忆和受控的生物信息学工具，来支持可靠的、长轨迹的数据分析。

> Bioinfoysis relies on a sophisticated framework designed to maintain strict evidence flow and rigorous runtime execution:
> 
> 1. **Persistent Artifact-Grounded Analysis:** Requests are structured as persistent analysis runs where data and intermediate computations are explicitly tied to the corresponding evidence.
> 2. **Global Planning & Step-Wise Replanning:** The system employs a planner that maintains an executable checklist. Pending steps are continually revised using structured handoffs returned after each worker execution.
> 3. **Structured Handoffs:** These mechanisms bind intermediate results directly to the responsible agent, checklist step, and plan generation. This prevents outdated or stale evidence from being silently reused after a plan revision.
> 4. **Controlled Runtime:** Automatically validates generated scripts, tables, and figures *before* they are utilized in downstream analysis or reporting.
> 5. **Governed Bioinformatics Skills & Memory:** Leverages role-specific context, persistent memory, and governed bioinformatics tools to support reliable, long-trajectory data analysis.

---

## 基准测试性能 (Benchmark Performance)

Bioinfoysis 在为复杂计算生物学挑战设计的基准数据集上进行了严格评估：

| Benchmark / Track | Baseline Average Accuracy | Bioinfoysis Performance |
| :--- | :---: | :---: |
| **BixBench** | — | **82.4%** *(SOTA)* |
| **LAB-Bench 2 (SeqQA2)** | 27.81% | **64.13%** |
| **LAB-Bench 2 (DbQA2)** | 3.13% | **31.25%** |

*(Note: SeqQA2 and DbQA2 accuracy metrics represent averages evaluated across four underlying language models.)*

> Bioinfoysis was rigorously evaluated on benchmark datasets designed for complex computational biology challenges:
> 
> | Benchmark / Track | Baseline Average Accuracy | Bioinfoysis Performance |
> | :--- | :---: | :---: |
> | **BixBench** | — | **82.4%** *(SOTA)* |
> | **LAB-Bench 2 (SeqQA2)** | 27.81% | **64.13%** |
> | **LAB-Bench 2 (DbQA2)** | 3.13% | **31.25%** |
> 
> *(Note: SeqQA2 and DbQA2 accuracy metrics represent averages evaluated across four underlying language models.)*

---

## 结论与资源 (Conclusion & Resources)

Bioinfoysis 的成功表明，强大的生物信息学自动化不仅高度依赖底层模型的原始能力，同样也依赖于**控制规划、执行、记忆和证据流的系统架构（harness）**。

* **项目演示：** [report.bioinfoysis.com](https://report.bioinfoysis.com/)
* **arXiv 条目：** [arXiv:2609.03871](https://arxiv.org/abs/2609.03871)

> The success of Bioinfoysis highlights that robust bioinformatics automation depends as heavily on the **harness governing planning, execution, memory, and evidence flow** as it does on the underlying model's raw capabilities. 
> 
> * **Project Demo:** [report.bioinfoysis.com](https://report.bioinfoysis.com/)
> * **arXiv Entry:** [arXiv:2609.03871](https://arxiv.org/abs/2609.03871)

---
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">