---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 视觉语言模型
- 机器人学
- 故障检测
- 基准测试
- 具身智能
title: FailBench：视觉语言模型在判断机器人任务成功率方面有多可靠？
---
### 文章背景与核心概要
视觉语言模型（VLM）目前被广泛用于评估机器人的操作结果，然而现有的基准测试缺乏对其跨领域泛化能力的严格验证。本文推出了 **FailBench**——一个用于机器人故障检测的综合基准测试，涵盖了来自 14 个不同来源（12 个真实世界场景和 2 个模拟场景）的 2,197 次操作尝试。

研究结果揭示了当前 VLM 性能的重大局限性：表现最好的 VLM 检测器的平均平衡准确率仅为 0.77；专门针对故障检测进行微调的模型，其表现反而不如通用 VLM 及其自身的预训练基线；模型在面对需要接触密集的装配任务时表现退化至接近随机猜测。此外，本文还展示了输入级别的优化（如空间定位和裁剪与任务结果相关的区域）无需额外训练即可提升检测性能。

---

## # FailBench: How Reliable are VLMs at Judging Robot Task Success?

* **arXiv ID:** [arXiv:2609.03611](https://arxiv.org/abs/2609.03611) [cs.RO]
* **Authors:** Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
* **Submitted:** September 3, 2026
* **Primary Subject:** Robotics (`cs.RO`)
* **Secondary Subject:** Artificial Intelligence (`cs.AI`)

> * **arXiv ID:** [arXiv:2609.03611](https://arxiv.org/abs/2609.03611) [cs.RO]
> * **Authors:** Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
> * **Submitted:** September 3, 2026
> * **Primary Subject:** Robotics (`cs.RO`)
> * **Secondary Subject:** Artificial Intelligence (`cs.AI`)

---

## 📌 执行摘要 (Executive Summary)

视觉语言模型（VLMs）经常被部署来评估机器人操作的结果，然而现有的基准缺乏跨域泛化能力的严谨证据。本文介绍了 **FailBench**，这是一个全面的机器人故障检测基准，包含来自 14 个不同来源（12 个真实世界和 2 个模拟）的 2,197 次操作尝试。

研究结果揭示了当前 VLM 性能的关键局限性：
* **整体准确率低：** 表现最好的 VLM 检测器的平均平衡准确率仅为 **0.77**。
* **微调悖论：** 专门针对故障检测进行微调的模型，其表现始终低于通用 VLM 及其自身的预训练基线。
* **任务依赖性：** 性能与视觉证据密切相关——在评估可观察的对象运动时，模型几乎达到饱和，但在接触密集的装配任务上，性能退化至接近随机水平（平衡准确率 $<0.60$）。
* **系统性偏差：** 在模糊证据下，模型表现出预测成功的强倾向性，即使增加推理工作量，这一问题依然存在。
* **简单干预：** 输入级别的优化（例如空间定位和裁剪与任务结果相关的区域）在无需额外训练的情况下，使顶级检测器的性能提升了 **2.4 个百分点**。

> ## 📌 Executive Summary
>
> Vision-Language Models (VLMs) are frequently deployed to evaluate robot manipulation outcomes, yet existing benchmarks lack rigorous evidence of cross-domain generalization. This paper introduces **FailBench**, a comprehensive benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 diverse sources (12 real-world and 2 simulated). 
> 
> The findings reveal critical limitations in current VLM performance:
> * **Low Overall Accuracy:** The top-performing VLM detector achieves a mere **0.77 mean balanced accuracy**.
> * **Fine-Tuning Paradox:** Models specifically fine-tuned for failure detection consistently underperform general-purpose VLMs and their own pretrained baselines.
> * **Task Dependency:** Performance is heavily tied to visual evidence—models nearly saturate when evaluating observable object motion, but degrade to near-chance performance ($<0.60$ balanced accuracy) on contact-intensive assembly tasks.
> * **Systematic Bias:** Models exhibit a strong bias toward predicting success under ambiguous evidence, an issue that persists even when reasoning effort is increased.
> * **Simple Intervention:** Input-level optimizations, such as spatially localizing and cropping regions relevant to the task outcome, improve the top detector by **2.4 percentage points** without requiring additional training.

---

## 📊 摘要与基准概览 (Abstract & Benchmark Overview)

> **摘要：** 视觉语言模型（VLMs）越来越多地被用于评估机器人操作结果，但现有的基准测试对于跨域泛化能力的证据十分有限。我们推出了 FailBench，这是一个用于机器人故障检测的基准测试，包含来自 14 个公共来源（12 个真实世界，2 个模拟）的 2,197 次操作尝试。在 FailBench 中，75% 的故障是自然发生的，且有六个真实世界来源来自非故障检测数据集。通过评估 13 个基于 VLM 的检测器，我们发现最好的模型的平均平衡准确率仅为 0.77。值得注意的是，专门针对故障检测进行微调的模型，其性能始终低于通用 VLM 及其自身的预训练基线。性能在很大程度上取决于所需的视觉证据：当结果取决于可观察的物体运动时，模型接近饱和状态；但在接触密集的装配任务上，性能则退化至接近随机（平衡准确率 $<0.60$）。错误分析表明，在模糊证据下，模型对预测成功存在系统性偏差，即使增加推理工作量，这种偏差依然存在。最后，我们表明输入级干预（空间定位和裁剪与结果相关的区域）在无需额外训练的情况下，使顶级检测器的性能提升了 2.4 个百分点。

> **Abstract:** Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-domain generalization. We introduce FailBench, a benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 public sources (12 real-world, 2 simulated). In FailBench, 75% of failures occur naturally, and six real-world sources come from non-failure-detection datasets. Evaluating 13 VLM-based detectors, we find the best model achieves only 0.77 mean balanced accuracy. Notably, models fine-tuned for failure detection consistently underperform general-purpose VLMs and their own pretrained baselines. Performance depends heavily on required visual evidence: models approach saturation when outcomes depend on observable object motion, but degrade to near-chance (<0.60 balanced accuracy) on contact-intensive assembly tasks. Error analysis reveals a systematic bias toward predicting success under ambiguous evidence, which persists even with increased reasoning effort. Finally, we show that input-level intervention--spatially localizing and cropping outcome-relevant regions--improves the top detector by 2.4 percentage points without extra training.

### FailBench 的核心组成
* **总尝试次数：** 2,197 次操作尝试
* **数据来源：** 14 个公共来源（12 个真实世界，2 个模拟）
* **自然故障：** 75% 的故障自然发生
* **来源多样性：** 包含 6 个源自非故障检测数据集的真实世界来源

> ### Key Composition of FailBench
> * **Total Attempts:** 2,197 manipulation attempts
> * **Data Sources:** 14 public sources (12 real-world, 2 simulated)
> * **Natural Failures:** 75% of failures occur naturally
> * **Source Diversity:** Includes 6 real-world sources originating from non-failure-detection datasets

---

## 🔗 链接与资源 (Links & Resources)

* **阅读论文：** [arXiv:2609.03611](https://arxiv.org/abs/2609.03611)
* **下载格式：** [查看 PDF](https://arxiv.org/pdf/2609.03611) | [HTML 版本](https://arxiv.org/html/2609.03611v1) | [TeX 源码](https://arxiv.org/src/2609.03611)
* **外部引用与工具：** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03611)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03611)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03611)

> ## 🔗 Links & Resources
> 
> * **Read the Paper:** [arXiv:2609.03611](https://arxiv.org/abs/2609.03611)
> * **Download Formats:** [View PDF](https://arxiv.org/pdf/2609.03611) | [HTML Version](https://arxiv.org/html/2609.03611v1) | [TeX Source](https://arxiv.org/src/2609.03611)
> * **External Citations & Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03611)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03611)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03611)