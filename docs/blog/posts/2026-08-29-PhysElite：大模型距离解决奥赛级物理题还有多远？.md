---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大语言模型
- 多模态
- 物理推理
- 基准测试
- 人工智能
title: PhysElite：大模型距离解决奥赛级物理题还有多远？
---
### 文章背景与核心概要

PhysElite 是一个大规模、双语、多模态基准测试集，旨在评估大语言模型（LLMs）在奥林匹克竞赛级别的物理推理能力。针对现有基准测试在难度、视觉多样性及详细推理步骤方面的不足，PhysElite 提供了 11,586 道高水平物理题目。每道题目均包含视觉图表、详细的中英双语推导过程及最终答案。

通过对 18 个主流多模态大模型（MLLMs）的测试，研究发现模型表现存在显著差距，表现最好的模型准确率仅为 33.7%。这一结果凸显了当前 AI 在专家级物理推理任务中仍面临巨大挑战，并为未来提升模型推理架构提供了明确的诊断方向。

---

# PhysElite：大模型距离解决奥赛级物理题还有多远？

**arXiv:** [2608.25097](https://arxiv.org/abs/2608.25097)  
**日期:** 2026年8月25日  
**学科:** 人工智能 (cs.AI); 多媒体 (cs.MM); 数学物理 (math-ph)

---

## 摘要
> *PhysElite* is a large-scale, bilingual, multimodal benchmark designed to evaluate the physical reasoning capabilities of Large Language Models (LLMs) at the Olympiad level. Addressing the limitations of existing benchmarks—which often lack sufficient difficulty, visual diversity, and comprehensive step-by-step reasoning—*PhysElite* provides 11,586 high-tier physics problems. Each entry includes visual diagrams, detailed bilingual (Chinese-English) solution derivations, and final answers. Testing across 18 leading MLLMs revealed a significant performance gap, with the top-performing model achieving only 33.7% accuracy, highlighting the current limitations of AI in expert-level physical reasoning.

*PhysElite* 是一个大规模、双语、多模态基准测试，旨在评估大语言模型（LLMs）在奥赛级别的物理推理能力。针对现有基准测试的局限性——即往往缺乏足够的难度、视觉多样性和全面的分步推理——*PhysElite* 提供了 11,586 道高水平物理题目。每个条目都包含视觉图表、详细的中英双语推导过程和最终答案。对 18 个领先的多模态大模型（MLLMs）进行的测试揭示了显著的性能差距，表现最好的模型准确率仅为 33.7%，凸显了当前 AI 在专家级物理推理方面的局限性。

---

## 作者
> Ruoran Xu, Wending Gao, Liyunfeng Chen, Aixin Shi, Haoyu Cheng, Zixiang Fang, Yiqiang Zou, and Qiufeng Wang.

Ruoran Xu, Wending Gao, Liyunfeng Chen, Aixin Shi, Haoyu Cheng, Zixiang Fang, Yiqiang Zou, and Qiufeng Wang.

---

## 数据集主要特征
> *   **Scale:** 11,586 Olympiad-tier physics problems.
> *   **Multimodality:** Includes original visual diagrams for every problem.
> *   **Transparency:** Provides step-by-step solution derivations to allow for process-level diagnostic evaluation.
> *   **Bilingual Support:** All content is provided in both Chinese and English.
> *   **Accessibility:** The dataset is publicly available on [Hugging Face](https://huggingface.co/datasets/physelite/PhysElite).

*   **规模：** 11,586 道奥赛级物理题。
*   **多模态：** 每道题都包含原始视觉图表。
*   **透明度：** 提供分步推导过程，以便进行过程级的诊断评估。
*   **双语支持：** 所有内容均以中英文提供。
*   **可访问性：** 数据集已在 [Hugging Face](https://huggingface.co/datasets/physelite/PhysElite) 上公开。

---

## 研究发现
> The authors benchmarked 18 open-source and closed-source Multimodal Large Language Models (MLLMs). The study found:
> 1.  **Performance Ceiling:** Even the most advanced models struggle significantly, with the highest accuracy recorded at only 33.7%.
> 2.  **Reasoning Diagnostics:** By conducting step-level process evaluations, the researchers identified specific failure points in the reasoning chains of current models, providing a roadmap for future improvements in physical reasoning architectures.

作者对 18 个开源和闭源的多模态大模型（MLLMs）进行了基准测试。研究发现：
1.  **性能上限：** 即使是最先进的模型也面临巨大困难，最高准确率仅为 33.7%。
2.  **推理诊断：** 通过进行步骤级的过程评估，研究人员识别了当前模型推理链中的具体失败点，为未来改进物理推理架构提供了路线图。

---

## 获取论文
> *   **[View PDF](https://arxiv.org/pdf/2608.25097)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.25097v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.25097)**
> *   **[DOI](https://doi.org/10.48550/arXiv.2608.25097)**

*   **[查看 PDF](https://arxiv.org/pdf/2608.25097)**
*   **[HTML (实验性)](https://arxiv.org/html/2608.25097v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.25097)**
*   **[DOI](https://doi.org/10.48550/arXiv.2608.25097)**

---

## 许可协议
> <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> <span>View License (CC BY 4.0)</span>
> </a>

<a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
<span>查看许可协议 (CC BY 4.0)</span>
</a>