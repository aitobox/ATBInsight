---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 生成式AI
- 电子健康记录
- 医疗大模型
- 基础模型
- COVID-19
title: Foresight-England：新冠疫情期间用于医疗事件预测的国家级电子健康记录生成式AI模型开发
---
### 文章背景与核心概要
本文介绍了 *Foresight-England (Foresight-E)* 项目，这是一项旨在开发国家级电子健康记录 (EHR) 生成式基础模型的先锋性工作。该模型采用2430万参数的Transformer解码器架构，专门用于分析COVID-19疫情带来的复杂直接与间接影响。项目在英国国民健康制度（NHS England）的安全环境中进行训练，为全人群规模的医疗AI研究提供了方法论范例。

尽管该项目目前已被NHS England暂停，导致无法发布具体的量化结果，但本文详细记录了该倡议所开发的基础架构、分词（tokenization）策略以及评估框架。这为构建大规模EHR基础模型提供了宝贵的方法论模板，并凸显了开展此类国家级临床AI研究所面临的独特挑战。

---

# Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic

> # Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic

**arXiv:** [2608.16273](https://arxiv.org/abs/2608.16273)  
**Date:** August 17, 2026  
**Subject:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

> **arXiv:** [2608.16273](https://arxiv.org/abs/2608.16273)  
> **Date:** August 17, 2026  
> **Subject:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

---

## Summary

> ## Summary

*Foresight-England (Foresight-E)* 代表了一项开发电子健康记录（EHR）国家级生成式基础模型的开创性工作。该模型旨在分析COVID-19疫情带来的复杂直接和间接影响，采用了拥有2.43亿个参数的Transformer解码器架构。项目在NHS England的安全环境中进行训练，可作为人口规模健康AI的方法论案例研究。尽管该项目目前已被NHS England暂停——从而无法发布定量结果——但本文记录了为该倡议开发的基础架构、分词策略和评估框架。

> *Foresight-England (Foresight-E)* represents a pioneering effort to develop a national-scale generative foundation model for Electronic Health Records (EHRs). Designed to analyze the complex direct and indirect impacts of the COVID-19 pandemic, the model utilizes a 243-million-parameter transformer decoder architecture. Trained within the secure NHS England environment, the project serves as a methodological case study for population-scale health AI. While the project is currently paused by NHS England—precluding the release of quantitative results—this paper documents the foundational architecture, tokenization strategies, and evaluation frameworks developed for the initiative.

---

## Technical Overview

> ## Technical Overview

### Model Architecture

> ### Model Architecture

*   **类型：** Transformer解码器（2.43亿参数）。
*   **训练环境：** NHS England安全数据环境 (Secure Data Environment)。
*   **数据范围：** 约6100万个人的纵向EHR，整合了初级和二级医疗、死亡登记以及COVID-19特定数据集。
*   **训练周期：** 2018年11月至2022年12月（90%的数据用于训练/验证；10%作为保留集）。

> *   **Type:** Transformer decoder (243 million parameters).
> *   **Training Environment:** NHS England Secure Data Environment.
> *   **Data Scope:** Longitudinal EHRs of ~61 million individuals, integrating primary and secondary care, death registrations, and COVID-19 specific datasets.
> *   **Training Period:** November 2018 to December 2022 (90% of data used for training/validation; 10% held out).

### Methodology

> ### Methodology

*   **自回归预测：** 模型根据患者的历史时间线预测后续的医疗事件。
*   **零样本推理：** 能够预测约40,000个代码词汇表中的任何概念，无需进行任务特定的微调。
*   **分词技术：** 复杂的方案，在保留ICD-10、OPCS-4和SNOMED CT代码的临床粒度的同时，联合编码绝对和相对时间数据。

> *   **Autoregressive Prediction:** The model predicts subsequent medical events based on a patient’s historical timeline.
> *   **Zero-Shot Inference:** Capable of predicting any concept within a ~40,000-code vocabulary without requiring task-specific fine-tuning.
> *   **Tokenization:** A sophisticated scheme that preserves clinical granularity across ICD-10, OPCS-4, and SNOMED CT codes, while jointly encoding absolute and relative temporal data.

### Evaluation Framework

> ### Evaluation Framework

研究人员建立了一个强大的框架来评估：
*   30天COVID-19住院率和死亡率。
*   基于人口统计学和疫苗接种状况的亚组分析。
*   关于疫情间接影响的泛化能力以及对未见过的2023年数据的性能表现。
*   与传统模型（包括逻辑回归和XGBoost）的基准对比。

> The researchers established a robust framework to assess:
> *   30-day COVID-19 hospitalisation and mortality rates.
> *   Subgroup analyses based on demographics and vaccination status.
> *   Generalization capabilities regarding the pandemic's indirect effects and performance on unseen 2023 data.
> *   Benchmarking against traditional models, including logistic regression and XGBoost.

---

## Project Status

> ## Project Status

截至本报告发布时，NHS England已暂停访问Foresight-E项目所需的数据。因此，目前无法提供任何定量结果。作者发表这项工作是为了分享他们构建大规模EHR基础模型的方法论模板，并强调此类国家级临床AI研究所特有的挑战。

> As of the current report, NHS England has paused access to the data required for the Foresight-E project. Consequently, no quantitative results are available at this time. The authors have published this work to share their methodological template for building large-scale EHR foundation models and to highlight the unique challenges inherent in such national-scale clinical AI research.

---

## Full-Text & Resources

> ## Full-Text & Resources

*   [查看 PDF](https://arxiv.org/pdf/2608.16273)
*   [HTML (实验性)](https://arxiv.org/html/2608.16273v1)
*   [TeX 源码](https://arxiv.org/src/2608.16273)
*   **许可协议：** [知识共享署名-非商业性使用-禁止演绎 4.0 国际版](http://creativecommons.org/licenses/by-nc-nd/4.0/)

> *   [View PDF](https://arxiv.org/pdf/2608.16273)
> *   [HTML (Experimental)](https://arxiv.org/html/2608.16273v1)
> *   [TeX Source](https://arxiv.org/src/2608.16273)
> *   **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)

![license icon](./images/fb423b2203a9.png)

> ![license icon](./images/fb423b2203a9.png)

---

*注：本预印本未经同行评审。在未咨询多位领域专家之前，不应将其作为指导临床实践或健康相关行为的依据。*

> *Note: This e-print has not been peer-reviewed. It should not be relied upon to guide clinical practice or health-related behavior without consulting multiple experts in the field.*