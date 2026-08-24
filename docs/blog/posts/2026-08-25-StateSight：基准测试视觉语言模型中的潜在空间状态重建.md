---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 视觉语言模型
- 空间推理
- 基准测试
- 计算机视觉
- StateSight
title: StateSight：基准测试视觉语言模型中的潜在空间状态重建
---
### 文章背景与核心概要
视觉语言模型（VLM）正越来越多地被部署于复杂的模态问答任务中。然而，由于广泛的基准测试往往将感知、OCR、语言先验和逻辑推理混为一谈，因此很难单独评估它们从单张图像中重建潜在空间核心能力。

为了填补这一空白，本文引入了 **StateSight**，这是一个通过程序生成的基准测试，旨在严格评估潜在空间状态重建能力。研究结果揭示了一个关键见解：**格式合规的 VLM 响应往往掩盖了其在恢复可验证视觉推理所需的精确空间结构方面的根本性失败。**

> Vision-Language Models (VLMs) are increasingly deployed for complex multimodal question-answering tasks. However, isolating their core ability to reconstruct latent spatial structures from a single image remains challenging because broad benchmarks conflate perception, OCR, linguistic priors, and logical reasoning. 
> 
> To address this gap, this paper introduces **StateSight**, a procedurally generated benchmark designed to rigorously evaluate latent spatial-state reconstruction. The findings reveal a critical insight: **format-valid VLM responses often mask fundamental failures to recover the precise spatial structures required for verifiable visual inference.**

---

## 状态洞察基准概览：StateSight

StateSight 通过三个不同的空间推理任务系列对模型进行评估，每个任务使用 300 个单图像提示，并配备确定性的标准答案（oracle labels）和精确匹配评分机制：

1. **立方体网格相对面推理（Cube-Net Opposite-Face Reasoning）**
2. **遮挡立方体塔计数（Occluded Cube-Tower Counting）**
3. **4-邻域连通分量计数（4-Neighbor Connected-Component Counting）**

### 配套数据集：StateSight-Steps
为了帮助分析中间推理路径，作者还推出了 **StateSight-Steps** 配套数据集，包含：
* 900 个交织的图文示例
* 3,600 个确定性的中间视觉状态

> ## Benchmark Overview: StateSight
> 
> StateSight evaluates models across three distinct spatial reasoning task families, utilizing 300 single-image prompts per task featuring deterministic oracle labels and exact-match scoring:
> 
> 1. **Cube-Net Opposite-Face Reasoning**
> 2. **Occluded Cube-Tower Counting**
> 3. **4-Neighbor Connected-Component Counting**
> 
> ### Companion Dataset: StateSight-Steps
> To help analyze intermediate reasoning paths, the authors also introduce **StateSight-Steps**, a companion dataset consisting of:
> * 900 interleaved image-text examples
> * 3,600 deterministic intermediate visual states

---

## 性能结果

领先的闭源视觉语言模型和人类基准在三个 StateSight 任务上的表现如下：

| 评估对象 | 任务 1：立方体网格相对面推理 | 任务 2：遮挡立方体塔计数 | 任务 3：4-邻域连通分量计数 | 格式错误 |
| :--- | :---: | :---: | :---: | :---: |
| **OpenAI GPT-5.5** (`gpt-5.5`) | **59.3%** | **33.3%** | **28.3%** | **0** |
| **Claude Sonnet 5** | 53.3% | 18.7% | 7.3% | **0** |
| **人类基准** *(30 名参与者 / 60 个项目)* | **80.8%** | **68.8%** | **64.3%** | — |

* **模型可靠性：** OpenAI GPT-5.5 和 Claude Sonnet 5 在直接执行运行中均实现了**零格式错误**。
* **人类优势：** 在所有三个任务中，由 30 名参与者组成的人类基准显著优于这两个 AI 模型。
* **错误分析：** 可视化推导分析揭示了根源于不正确的图像状态重建和有缺陷的推理过程的反复出现的故障模式。

> ## Performance Results
> 
> Leading proprietary vision-language models and human baselines performed across the three StateSight tasks as follows:
> 
> | Evaluation Subject | Task 1: Cube-Net Opposite-Face Reasoning | Task 2: Occluded Cube-Tower Counting | Task 3: 4-Neighbor Connected-Component Counting | Format Errors |
> | :--- | :---: | :---: | :---: | :---: |
> | **OpenAI GPT-5.5** (`gpt-5.5`) | **59.3%** | **33.3%** | **28.3%** | **0** |
> | **Claude Sonnet 5** | 53.3% | 18.7% | 7.3% | **0** |
> | **Human Baseline** *(30 participants / 60 items)* | **80.8%** | **68.8%** | **64.3%** | — |
> 
> * **Model Reliability:** Both OpenAI GPT-5.5 and Claude Sonnet 5 achieved **zero format errors** in direct execution runs.
> * **Human Superiority:** A 30-participant human baseline significantly outperformed both AI models across all three tasks.
> * **Error Analysis:** A visible-derivation analysis exposed recurring failure modes rooted in incorrect image-state reconstruction and flawed reasoning procedures.