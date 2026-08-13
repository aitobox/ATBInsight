---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 数据增强
- 生成式AI
- 极端值分析
- 航空运输
- 机器学习
title: TailBooster：用于极限值增强与操作有效性强制约束的双层生成式框架
---
### 文章背景与核心概要
在处理混合类型表格数据时，传统合成数据生成方法常常面临分布长尾（Tail）样本代表性不足以及生成不符合实际物理规律的“幻觉”实例两大挑战。本文介绍的 TailBooster 框架正是为解决这一极端值数据增强难题而设计的创新数据驱动且与模型无关的生成式框架。该研究以航空运输领域为例，针对严重到达延误或异常飞行时间等会引起大规模航班中断的罕见事件进行了专项突破。

TailBooster 创新性地采用了双层架构：统计层利用四分位距（IQR）提取极值，为专属生成模型（表格变分自编码器）提供集中于尾部的训练信号；深度学习层则利用基于自编码器的清洗机制，剔除违反历史数据操作边界的合成记录。在针对美国航班记录的多维度评估中，TailBooster 展现出了显著的性能提升。与传统合成数据生成方法相比，在六种回归算法中，使用 TailBooster 生成的合成记录进行训练，极端的飞行时间预测平均绝对误差（MAE）降低了 **47–49%**，极端到达延误预测的 MAE 降低了 **29–57%**。

---

## 摘要 (Summary)

> **TailBooster** is a novel, data-driven, and model-agnostic generative framework designed to tackle the challenge of extreme value augmentation in mixed-type tabular datasets. Applied here to air transport—where rare events like severe arrival delays or abnormal air times cause massive disruptions—the framework overcomes two major limitations of conventional synthetic data generation: 
> 1. Under-representation of distributional tails.
> 2. Production of operationally infeasible instances (e.g., short air times paired with unusually long flight distances).
> 
> The architecture achieves this through a dual-layer approach:
> * **A Statistical Layer:** Extracts extreme values using the interquartile range (IQR) to supply tail-concentrated training signals to a dedicated generative model (a Tabular Variational Autoencoder).
> * **A Deep Learning Layer:** Utilizes an autoencoder-based cleaning mechanism to discard synthetic records that violate the operational envelope learned from historical data.
> 
> Evaluated on US flight records across five dimensions (diversity, statistical similarity, fidelity, operational validity, and utility), TailBooster demonstrated substantial improvements. Across six regression algorithms, training on TailBooster’s synthetic records reduced Mean Absolute Error (MAE) by **47–49%** for extreme air time prediction and **29–57%** for extreme arrival delay prediction compared to conventional synthetic data generation.

**TailBooster** 是一种新颖的、数据驱动且与模型无关的生成式框架，旨在解决混合类型表格数据中极端值增强的难题。该框架被应用于航空运输领域（在此领域中，严重到达延误或异常飞行时间等罕见事件会导致大规模的航班中断），克服了传统合成数据生成的两大主要局限性：
1. 分布长尾（尾部）的代表性严重不足。
2. 产生在操作上不可行的实例（例如，极短的飞行时间却搭配异常长的飞行距离）。

该架构通过双层方法实现了这一目标：
* **统计层：** 使用四分位距（IQR）提取极值，向专用的生成模型（表格变分自编码器）提供集中于尾部的训练信号。
* **深度学习层：** 利用基于自编码器的清洗机制，丢弃违反从历史数据中学习到的操作边界的合成记录。

通过对美国航班记录在五个维度（多样性、统计相似性、保真度、操作有效性和效用）上的评估，TailBooster 表现出了实质性的改进。在六种回归算法中，与传统的合成数据生成相比，使用 TailBooster 的合成记录进行训练使极端飞行时间预测的平均绝对误差（MAE）降低了 **47–49%**，极端到达延误预测的 MAE 降低了 **29–57%**。

---

## 文档元数据 (Document Metadata)

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [`arXiv:2608.11951`](https://arxiv.org/abs/2608.11951) [cs.LG] |
> | **Subjects** | Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`) |
> | **Authors** | Karim Aly, Alexei Sharpanskykh, Jacco Hoekstra |
> | **Submitted On** | August 12, 2026 |
> | **Comments** | Preprint submitted to journal |
> | **DOI** | [10.48550/arXiv.2608.11951](https://doi.org/10.48550/arXiv.2608.11951) |
> | **License** | [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) |

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [`arXiv:2608.11951`](https://arxiv.org/abs/2608.11951) [cs.LG] |
| **主题分类** | 机器学习 (`cs.LG`)；人工智能 (`cs.AI`) |
| **作者** | Karim Aly, Alexei Sharpanskykh, Jacco Hoekstra |
| **提交时间** | 2026年8月12日 |
| **备注** | 已向期刊提交的预印本 |
| **DOI** | [10.48550/arXiv.2608.11951](https://doi.org/10.48550/arXiv.2608.11951) |
| **许可协议** | [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) |

---

## 访问链接与资源 (Access Links & Resources)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2608.11951) | [HTML (Experimental)](https://arxiv.org/html/2608.11951v1) | [TeX Source](https://arxiv.org/src/2608.11951)
> * **Code, Data & Demos:** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [Papers with Code / AlphaXiv](https://alphaxiv.org/)
> * **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11951) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11951) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11951)

* **全文选项：** [查看 PDF](https://arxiv.org/pdf/2608.11951) | [HTML (实验性)](https://arxiv.org/html/2608.11951v1) | [TeX 源码](https://arxiv.org/src/2608.11951)
* **代码、数据与演示：** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX 代码查找器](https://www.catalyzex.com) | [Papers with Code / AlphaXiv](https://alphaxiv.org/)
* **文献计量工具：** [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11951) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11951) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11951)