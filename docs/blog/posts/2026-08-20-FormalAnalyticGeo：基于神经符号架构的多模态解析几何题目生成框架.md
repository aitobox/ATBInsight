---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 神经符号AI
- 多模态大模型
- 解析几何
- 自动数据生成
- 教育AI
title: FormalAnalyticGeo：基于神经符号架构的多模态解析几何题目生成框架
---
### 文章背景与核心概要
尽管多模态大模型（MLLMs）在数学推理能力上取得了显着进展，但由于带标注的训练样本严重匮乏，**解析几何**领域在很大程度上仍未得到充分探索。传统的几何图形生成方法面临着严峻限制：基于模板的方法无法处理约束驱动的布局，而纯生成式模型又无法达到正确渲染带标注圆锥曲线所需的几何精度。

为了克服这些挑战，本文作者推出了 **FormalAnalyticGeo**，这是一个具备高度可扩展性、全自动的神经符号框架，能够在无需人工标注的情况下生成多模态解析几何题目。该框架利用形式化语言，通过条件描述语言（CDL）将自由格式的题目文本与基于符号距离场（SDF）引擎的精确图形渲染无缝桥接，并通过多阶段的质量验证与闭环自动重试机制，确保了生成内容的高精度与可靠性。

---

## 形式化解析几何：多模态解析几何题目生成的神经符号框架

> ## FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation

## 元数据
- **arXiv ID:** [arXiv:2607.12982](https://arxiv.org/abs/2607.12982) [cs.AI]
- **研究领域:** 人工智能 (`cs.AI`)；多智能体系统 (`cs.MA`)；符号计算 (`cs.SC`)
- **作者:** Ruoran Xu, Wending Gao, Xiaoqing Kang, Qiufeng Wang
- **提交与修订时间:** 2026年7月14日提交；2026年8月17日最后修订 (v3)
- **链接:** [查看 PDF](https://arxiv.org/pdf/2607.12982) | [TeX 源码](https://arxiv.org/src/2607.12982) | [DOI](https://doi.org/10.48550/arXiv.2607.12982)

> ## Metadata
> - **arXiv ID:** [arXiv:2607.12982](https://arxiv.org/abs/2607.12982) [cs.AI]
> - **Subjects:** Artificial Intelligence (`cs.AI`); Multiagent Systems (`cs.MA`); Symbolic Computation (`cs.SC)`)
> - **Authors:** Ruoran Xu, Wending Gao, Xiaoqing Kang, Qiufeng Wang
> - **Submitted / Revised:** Submitted on 14 Jul 2026; Last revised 17 Aug 2026 (v3)
> - **Links:** [View PDF](https://arxiv.org/pdf/2607.12982) | [TeX Source](https://arxiv.org/src/2607.12982) | [DOI](https://doi.org/10.48550/arXiv.2607.12982)

---

## 摘要
尽管多模态大模型（MLLMs）在数学推理能力上取得了显着进展，但由于带标注的训练样本严重匮乏，**解析几何**领域在很大程度上仍未得到充分探索。传统的几何图形生成方法面临着严峻限制：基于模板的方法无法处理约束驱动的布局，而纯生成式模型又无法达到正确渲染带标注圆锥曲线所需的几何精度。

为了克服这一难题，作者引入了 **FormalAnalyticGeo**，这是一个可扩展、全自动的神经符号框架，能够在无需人工标注的情况下生成多模态解析几何题目。

> ## Summary
> While Multimodal Large Language Models (MLLMs) have advanced mathematical reasoning significantly, **analytic geometry** remains largely underexplored due to a critical scarcity of annotated training samples. Traditional diagram generation approaches face severe limitations: template-based methods cannot handle constraint-driven layouts, and purely generative models fail to achieve the geometric precision needed to correctly render annotated conic curves. 
> 
> To overcome this, the authors introduce **FormalAnalyticGeo**, a scalable, fully automated neural-symbolic framework for generating multimodal analytic geometry problems without requiring human annotation.

---

## 核心框架组件

该框架利用形式化语言，并围绕 **CDL（条件描述语言，Condition Description Language）** 构建——这是一种形式化的中间表示，通过**符号距离场（SDF）**引擎将自由格式的题目文本与精确的图形渲染无缝桥接。

该架构在顺序流水线中协同了四个专用的 LLM 组件：
1. **生成器（Generator）：** 生产多样化的解析几何题目。
2. **形式化器（Formalizer）：** 将每个题目转换为 CDL 以进行基于 SDF 的渲染。
3. **测量器（Measurer）：** 通过对渲染出的图表进行基于视觉的测量，提取标准答案（Ground-truth）。
4. **质量验证器（Quality Verifier）：** 在三个不同的阶段持续监控和评估输出结果。

来自质量验证器的结构化反馈会触发自动重试机制，从而建立起一个完全无需人工干预、稳健的闭环工作流。

> ## Key Framework Components
> 
> The framework leverages formal languages and is built around **CDL (Condition Description Language)**—a formal intermediate representation that seamlessly bridges free-form problem text with precise diagram rendering via a **Signed Distance Field (SDF)** engine. 
> 
> The architecture coordinates four specialized LLM components in a sequential pipeline:
> 1. **Generator:** Produces diverse analytic geometry problems.
> 2. **Formalizer:** Converts each problem into CDL for SDF-based rendering.
> 3. **Measurer:** Extracts ground-truth answers using vision-based measurement on the rendered diagrams.
> 4. **Quality Verifier:** Continuously monitors and evaluates outputs across three distinct stages.
> 
> Structured feedback from the Quality Verifier triggers an automated retry mechanism, establishing a robust closed-loop workflow that operates entirely without human intervention.

---

## 数据集与结果（`AnalyticGeo7K`）

大规模应用 **FormalAnalyticGeo** 框架产出了 **AnalyticGeo7K**，这是一个包含超过 **7,000 个经过验证的多模态题目**的综合数据集。

数据集中的每个题目均包含：
- 对齐的题目文本
- 几何精度的图表
- 形式化标注（CDL）
- 经过验证的标准答案

**实验亮点：**
- 生成的题目其中位数标准答案相对误差达到了 **0.70%**。
- 所有生成答案中有 **82.3%** 落在了精确符号解的严格 **5%** 容差范围内。

*注：作者计划将 FormalAnalyticGeo 框架和 AnalyticGeo7K 数据集全部开源。*

> ## Dataset & Results (`AnalyticGeo7K`)
> 
> Applying the **FormalAnalyticGeo** framework at scale yields **AnalyticGeo7K**, a comprehensive dataset comprising over **7,000 verified multimodal problems**. 
> 
> Each problem in the dataset features:
> - Aligned problem text
> - A geometrically precise diagram
> - Formal annotations (CDL)
> - Verified ground-truth solutions
> 
> **Experimental Highlights:**
> - The generated problems achieve a median ground-truth relative error of **0.70%**.
> - **82.3%** of all generated answers fall within a strict **5%** tolerance of the exact symbolic solution.
> 
> *Note: The authors plan to make both the FormalAnalyticGeo framework and the AnalyticGeo7K dataset publicly available.*

---
*(许可协议：[知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/))*

> *(License: [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/))*