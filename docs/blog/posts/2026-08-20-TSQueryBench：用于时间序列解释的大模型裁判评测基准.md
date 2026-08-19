---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 时间序列
- 大模型评测
- LLM-as-a-Judge
- 可解释性AI
- 机器学习
title: TSQueryBench：用于时间序列解释的大模型裁判评测基准
---
### 文章背景与核心概要
随着基础模型越来越多地在高风险领域为时间序列数据生成自然语言解释，确保事实准确性变得至关重要。与标准文本评估不同，验证时间序列解释需要对照结构化数据核对数值声明。

**TSQueryBench** 是一个全新且受控的合成基准，旨在评估这一能力。它包含跨越 10 种查询类型的 500 个时间序列实例，并配有不同准确程度的解释（完全正确、部分正确和错误）。研究揭示了一个显著的**生成与评估不对称性**：虽然大模型在*生成*数值正确的解释时往往表现吃力，但它们在*识别或评分*这些解释时却高度可靠。这表明，将大模型用作“裁判”（LLM-as-a-Judge）是评估数值扎实推理的一种可扩展且有效的策略。

---

# TSQueryBench: LLM-as-a-Judge for Time Series Explanations

**Authors:** Preetham Sivalingam, Murari Mandal, Dhruv Kumar, Saurabh Deshpande  
**Published:** April 2, 2026 (v2: August 18, 2026)  
**Venue:** Accepted at ICML FMSD  
**Subject:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL)  
**DOI:** [10.48550/arXiv.2604.02118](https://doi.org/10.48550/arXiv.2604.02118)

---

## Summary
As foundation models increasingly generate natural language explanations for time series data in high-stakes domains, ensuring factual accuracy is paramount. Unlike standard text evaluation, verifying time series explanations requires checking numerical claims against structured data. 

**TSQueryBench** is a new, controlled synthetic benchmark designed to evaluate this capability. It consists of 500 time series instances across 10 query types, paired with varying levels of explanatory accuracy (correct, partially correct, and incorrect). The study reveals a significant **generation evaluation asymmetry**: while LLMs often struggle to *generate* numerically correct explanations, they are highly reliable at *identifying or scoring* them. This suggests that using LLMs as "judges" is a scalable and effective strategy for evaluating numerically grounded reasoning.

---

## 关键研究发现
*   **不对称鸿沟：** 大模型创建解释的能力与其评估解释的能力之间存在明显的性能差距。
*   **LLM-as-a-Judge 的可靠性：** 事实证明，在大模型中采用基于评分标准的评估（Rubric-guided evaluation），对于时间序列推理而言比直接生成要可靠得多。
*   **基准实用性：** TSQueryBench 为测试四个不同任务的模型提供了一个强有力的框架：
    1. 解释生成
    2. 相对排序
    3. 独立评分
    4. 多重异常检测

> ## Key Research Findings
> *   **The Asymmetry Gap:** There is a distinct performance gap between an LLM's ability to create an explanation and its ability to evaluate one.
> *   **Reliability of LLM-as-a-Judge:** Rubric-guided evaluation by LLMs proves substantially more reliable than direct generation for time series reasoning.
> *   **Benchmark Utility:** TSQueryBench provides a robust framework for testing models across four distinct tasks:
>     1.  Explanation Generation
>     2.  Relative Ranking
>     3.  Independent Scoring
>     4.  Multi-Anomaly Detection

---

## 访问与资源
*   **论文 PDF：** [在 arXiv 上查看](https://arxiv.org/pdf/2604.02118)
*   **代码与数据：** [GitHub 仓库](https://github.com/Prxxthxm/TSQueryBench/)
*   **HTML 版本：** [实验性 HTML](https://arxiv.org/html/2604.02118v2)

> ## Access & Resources
> *   **Paper PDF:** [View on arXiv](https://arxiv.org/pdf/2604.02118)
> *   **Code & Data:** [GitHub Repository](https://github.com/Prxxthxm/TSQueryBench/)
> *   **HTML Version:** [Experimental HTML](https://arxiv.org/html/2604.02118v2)

---

## 引用
如果您使用了本项工作，请通过以下标识符进行引用：
**arXiv:2604.02118 [cs.AI]**

> ## Citation
> If you use this work, please refer to it via the following identifier:
> **arXiv:2604.02118 [cs.AI]**