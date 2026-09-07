---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 推荐系统
- 小型语言模型
- 电子商务
- 用户偏好预测
- 深度学习
title: DeepAffinity：利用小型语言模型预测电子商务中的长期商品属性偏好
---
### 文章背景与核心概要
在电子商务领域，精准捕捉用户的长期偏好对于提升推荐质量、搜索体验以及营销效果至关重要。本文探讨了一项被称为“属性偏好（Aspect Affinity）”的新任务，即预测用户对特定商品属性（如品牌、尺寸和颜色）的长期偏好。通过将该任务构建为基于时间排序的交互历史的时间序列预测任务，作者超越了仅关注当前会话的局限，能够捕捉随时间演变的长期用户偏好。

为了解决这一挑战，研究团队提出了 DeepAffinity 框架。该框架利用配备了结构化提示词（Structured Prompts）和专用预测头（Specialized Prediction Heads）的小型语言模型（SLMs），并进行了针对性的微调。实验结果表明，DeepAffinity 的表现显著优于标准的生成式微调方法；而缺乏任务特定微调的通用开源大语言模型（LLMs）则表现较差，凸显了它们在建模细微行为时的局限性。最终，DeepAffinity 在一个大型跨国电商平台上成功验证了其提升推荐质量的实际效用。

---

## 摘要 (Summary)

> **DeepAffinity** is a novel framework designed to predict long-term eCommerce user preferences for specific product aspects (such as brand, size, and color)—a task the authors define as **Aspect Affinity**. By framing this as a temporal prediction task using time-ordered interaction histories, DeepAffinity leverages **Small Language Models (SLMs)** equipped with structured prompts and specialized prediction heads. The research demonstrates that DeepAffinity outperforms standard generative fine-tuning methods and generalizes much better than general-purpose open-source LLMs (which struggle without task-specific tuning), ultimately enhancing recommendation quality on a large-scale multinational eCommerce platform.

DeepAffinity 是一个新颖的框架，旨在预测电子商务用户对特定商品属性（如品牌、尺寸和颜色）的长期偏好——作者将这一任务定义为**属性偏好（Aspect Affinity）**。通过利用按时间排序的交互历史将其构建为时间预测任务，DeepAffinity 采用了配备结构化提示词和专用预测头的**小型语言模型（SLMs）**。研究表明，DeepAffinity 的性能优于标准的生成式微调方法，并且比通用开源大语言模型（在没有针对特定任务微调时表现不佳）具有更好的泛化能力，最终提升了大规模型跨国电商平台上的推荐质量。

---

## 元数据 (Metadata)

* **arXiv 标识符:** [arXiv:2609.02468](https://arxiv.org/abs/2609.02468) [cs.LG]
* **主要学科:** 机器学习 (`cs.LG`)
* **次要学科:** 人工智能 (`cs.AI`)
* **会议收录:** 已被 `RecTemp@ACM RecSys 2026` 接收
* **发布日期:** 
  * 提交于：2026年9月2日
  * 最后修订：2026年9月4日 (v2)
* **DOI:** [10.48550/arXiv.2609.02468](https://doi.org/10.48550/arXiv.2609.02468)

---

## 作者 (Authors)
* Yotam Eshel
* Guy Hadad
* Guy Feigenblat
* Yuri M. Brovman
* Matt Gearhart
* Bracha Shapira

---

## 摘要正文 (Abstract)

> We explore predicting eCommerce user preferences for product aspects such as brand, size, and color — a task we define as **Aspect Affinity**. Solving this task improves customer understanding and enables fine-grained personalization in recommendation, search, and marketing. 

我们探讨了预测电子商务用户对商品属性（如品牌、尺寸和颜色）偏好的任务，我们将其定义为**属性偏好（Aspect Affinity）**。解决这一任务可以加深对客户的理解，并在推荐、搜索和营销中实现细粒度的个性化。

> We frame Aspect Affinity as a temporal prediction task: forecasting a user's future aspect choices from their time-ordered interaction history, capturing long-term preferences that evolve beyond the current session. To this end, we propose **DeepAffinity**, which leverages Small Language Models (SLMs) with structured prompts and specialized prediction heads fine-tuned for this task. 

我们将属性偏好构架为一个时间预测任务：根据用户按时间排序的交互历史预测其未来的属性选择，从而捕捉超越当前会话演变的长期偏好。为此，我们提出了 **DeepAffinity**，它利用配备了结构化提示词和专用预测头的小型语言模型（SLMs），并针对该任务进行了微调。

> We show DeepAffinity outperforms standard generative fine-tuning methods, while general-purpose open-source LLMs perform poorly without task-specific tuning, highlighting their limits in modeling nuanced behavior. Finally, DeepAffinity enhances recommendation quality on a large-scale multinational eCommerce platform.

我们证明了 DeepAffinity 的表现优于标准的生成式微调方法，而通用开源大语言模型在没有进行任务特定微调的情况下表现不佳，这突显了它们在建模细微行为方面的局限性。最后，DeepAffinity 提升了一个大型跨国电商平台上的推荐质量。

---

## 全文与资源 (Full-Text & Resources)
* [查看 PDF](https://arxiv.org/pdf/2609.02468)
* [实验性 HTML 版本](https://arxiv.org/html/2609.02468v2)
* [TeX 源码](https://arxiv.org/src/2609.02468)