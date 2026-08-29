---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大模型
- 物理推理
- 多模态基准
- 基准评测
- PhysElite
title: PhysElite：大语言模型距离解决奥林匹克级物理题还有多远？
---
### 文章背景与核心概要
随着大语言模型（LLM）和多模态大模型（MLLM）的迅速发展，评估其在各领域中达到专家级推理能力的上限成为了研究热点。然而，现有的许多基准测试往往存在难度不足、视觉模态单一以及缺乏全面的分步推理数据等局限性，难以准确衡量模型在高级物理推理方面的真正水平。为此，研究人员推出了 *PhysElite* 这一大规模、双语、多模态基准测试集。

*PhysElite* 涵盖了 11,586 道奥林匹克级别的物理难题，每道题目均包含高质量的视觉图表、详尽的中英双语解题推导过程以及最终答案。通过对全球 18 个主流多模态大模型的基准测试发现，表现最好的模型准确率也仅为 33.7%，充分暴露出当前 AI 在处理专家级物理推理任务时的重大缺陷，并为未来的架构改进指明了方向。

---

# PhysElite：大语言模型距离解决奥林匹克级物理题还有多远？

> # PhysElite: How Far Are LLMs from Solving Olympiad-Level Physics Problems?

**arXiv:** [2608.25097](https://arxiv.org/abs/2608.25097)  
**日期：** 2026年8月25日  
**研究领域：** 人工智能 (cs.AI)；多媒体 (cs.MM)；数理物理 (math-ph)

---

## 摘要

> **arXiv:** [2608.25097](https://arxiv.org/abs/2608.25097)  
> **Date:** August 25, 2026  
> **Subjects:** Artificial Intelligence (cs.AI); Multimedia (cs.MM); Mathematical Physics (math-ph)

---

## Summary

*PhysElite* 是一个大规模、双语、多模态基准测试，旨在评估大语言模型（LLM）在奥林匹克级别的物理推理能力。针对现有基准测试的局限性——通常缺乏足够的难度、视觉多样性和全面的分步推理——*PhysElite* 提供了 11,586 道高水平物理题。每个条目都包含视觉图表、详细的中英双语解题推导以及最终答案。对 18 个领先的 MLLM 进行测试后发现，模型表现存在显式差距，表现最好的模型准确率仅为 33.7%，凸显了当前 AI 在专家级物理推理方面的局限性。

> *PhysElite* is a large-scale, bilingual, multimodal benchmark designed to evaluate the physical reasoning capabilities of Large Language Models (LLMs) at the Olympiad level. Addressing the limitations of existing benchmarks—which often lack sufficient difficulty, visual diversity, and comprehensive step-by-step reasoning—*PhysElite* provides 11,586 high-tier physics problems. Each entry includes visual diagrams, detailed bilingual (Chinese-English) solution derivations, and final answers. Testing across 18 leading MLLMs revealed a significant performance gap, with the top-performing model achieving only 33.7% accuracy, highlighting the current limitations of AI in expert-level physical reasoning.

---

## 作者

> ## Authors

Ruoran Xu, Wending Gao, Liyunfeng Chen, Aixin Shi, Haoyu Cheng, Zixiang Fang, Yiqiang Zou, and Qiufeng Wang.

> Ruoran Xu, Wending Gao, Liyunfeng Chen, Aixin Shi, Haoyu Cheng, Zixiang Fang, Yiqiang Zou, and Qiufeng Wang.

---

## 数据集核心特点

> ## Key Features of the Dataset

*   **规模：** 11,586 道奥林匹克级物理题。
*   **多模态：** 每道题目都包含原始的视觉图表。
*   **透明度：** 提供分步解题推导，以便进行过程级诊断评估。
*   **双语支持：** 所有内容均提供中文和英文版本。
*   **易获取性：** 该数据集已在 [Hugging Face](https://huggingface.co/datasets/physelite/PhysElite) 上公开。

> *   **Scale:** 11,586 Olympiad-tier physics problems.
> *   **Multimodality:** Includes original visual diagrams for every problem.
> *   **Transparency:** Provides step-by-step solution derivations to allow for process-level diagnostic evaluation.
> *   **Bilingual Support:** All content is provided in both Chinese and English.
> *   **Accessibility:** The dataset is publicly available on [Hugging Face](https://huggingface.co/datasets/physelite/PhysElite).

---

## 研究发现

> ## Research Findings

作者对 18 个开源和闭源的多模态大模型（MLLMs）进行了基准测试。研究发现：
1.  **性能天花板：** 即使是最先进的模型也面临巨大挑战，最高记录准确率仅为 33.7%。
2.  **推理诊断：** 通过进行步骤级的过程评估，研究人员识别出了当前模型推理链中的特定失效点，为未来提升物理推理架构提供了路线图。

> The authors benchmarked 18 open-source and closed-source Multimodal Large Language Models (MLLMs). The study found:
> 1.  **Performance Ceiling:** Even the most advanced models struggle significantly, with the highest accuracy recorded at only 33.7%.
> 2.  **Reasoning Diagnostics:** By conducting step-level process evaluations, the researchers identified specific failure points in the reasoning chains of current models, providing a roadmap for future improvements in physical reasoning architectures.

---

## 访问论文

> ## Accessing the Paper

*   **[查看 PDF](https://arxiv.org/pdf/2608.25097)**
*   **[HTML 页面（实验性）](https://arxiv.org/html/2608.25097v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.25097)**
*   **[DOI](https://doi.org/10.48550/arXiv.2608.25097)**

> *   **[View PDF](https://arxiv.org/pdf/2608.25097)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.25097v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.25097)**
> *   **[DOI](https://doi.org/10.48550/arXiv.2608.25097)**

---

## 许可协议

> ## License

<a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
<span>查看许可协议 (CC BY 4.0)</span>
</a>

> <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> <span>View License (CC BY 4.0)</span>
> </a>