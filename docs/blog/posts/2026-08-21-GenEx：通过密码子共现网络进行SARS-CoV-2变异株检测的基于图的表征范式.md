---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 生物信息学
- 机器学习
- 图神经网络
- SARS-CoV-2
- 基因组学
title: GenEx：通过密码子共现网络进行SARS-CoV-2变异株检测的基于图的表征范式
---
### 文章背景与核心概要
传统的生物信息学方法（如序列比对、系统发育分析和突变频率统计）通常将病毒基因序列视为线性字符串，并使用成对的密码子或核苷酸距离矩阵进行分析，这往往会忽略复杂的上下文相互依赖关系。为了克服这一局限性，作者推出了 **GenEx**，这是一个将原始基因序列转化为**密码子共现图**并提取25种以上图特征的新型管道。GenEx借鉴了计算语言学的表征范式，将密码子序列视为具有结构化的符号词汇表。

本文的核心贡献包括提出多尺度密码子共现图（MSCG）和线性时间邻接PMI密码子图（LAPCG）两种核心算法，用于图生成和特征提取；实现了基于奇异值平方（$\sigma^2$）的奇异值分解（SVD）谱图特征提取，增强了分类任务中的类间可分性；并在23个基准机器学习模型上进行了严格评估，证明其在检测SARS-CoV-2主要变异株（Beta、Gamma、Delta和Omicron）方面具有卓越的性能。

---

# GenEx: A Graph-Based Representational Paradigm for SARS-CoV-2 Variant Detection via Codon Co-occurrence Networks

**arXiv:** [2608.18238](https://arxiv.org/abs/2608.18238) [cs.AI]  
**Submitted on:** 18 August 2026  
**Authors:** Arefin Amin, Labiba Faiza Karim, M. Monir Uddin  

---

## Summary

> Classical bioinformatics methods (such as Sequence Alignment, Phylogenetic Analysis, and Mutation Frequency Statistics) often analyze viral gene sequences by treating them as linear strings using pairwise codon or nucleotide distance matrices, overlooking complex contextual interdependencies. 

传统的生物信息学方法（如序列比对、系统发育分析和突变频率统计）通常将病毒基因序列视为线性字符串，并使用成对的密码子或核苷酸距离矩阵进行分析，这往往会忽略复杂的上下文相互依赖关系。

> To overcome this limitation, the authors introduce **GenEx**, a novel pipeline that converts raw gene sequences into **codon co-occurrence graphs** and extracts over 25 graph features. By borrowing representational paradigms from computational linguistics, GenEx treats codon sequences as structured symbolic vocabularies. 

为了克服这一局限性，作者推出了 **GenEx**，这是一个将原始基因序列转化为**密码子共现图**并提取25种以上图特征的新型管道。GenEx借鉴了计算语言学的表征范式，将密码子序列视为具有结构化的符号词汇表。

### Key Contributions & Techniques:
* **MSCG & LAPCG:** The two primary algorithms used for graph generation and feature extraction are *Multi-Scale Codon Co-occurrence Graph (MSCG)* and *Linear-time Adjacency PMI Codon Graph (LAPCG)*.
* **Spectral Graph Feature Extraction:** Implements Singular Value Decomposition (SVD) using the squared singular value ($\sigma^2$) instead of traditional eigenvalues. This amplifies the separation between dominant and subdominant spectral components, enhancing inter-class separability for downstream classification tasks.
* **Robust Machine Learning Evaluation:** Validated across 23 benchmarked machine learning models, demonstrating remarkable performance in detecting prominent SARS-CoV-2 variants (Beta, Gamma, Delta, and Omicron).

> ### 核心贡献与技术：
> * **MSCG 与 LAPCG：** 用于图生成和特征提取的两个主要算法分别是*多尺度密码子共现图（MSCG）*和*线性时间邻接PMI密码子图（LAPCG）*。
> * **谱图特征提取：** 实现了使用奇异值平方（$\sigma^2$）而非传统特征值的奇异值分解（SVD）。这放大了主导与次主导谱分量之间的分离，增强了下游分类任务的类间可分性。
> * **强大的机器学习评估：** 在23个基准机器学习模型上进行了验证，证明其在检测突出的 SARS-CoV-2 变异株（Beta、Gamma、Delta 和 Omicron）方面具有卓越的性能。

---

## Article Metadata

| Field | Details |
| :--- | :--- |
| **Title** | GenEx: A Graph-Based Representational Paradigm for SARS-CoV-2 Variant Detection via Codon Co-occurrence Networks |
| **Primary Subject** | Artificial Intelligence (`cs.AI`) |
| **Secondary Subject** | Quantitative Methods (`q-bio.QM`) |
| **DOI** | [10.48550/arXiv.2608.18238](https://doi.org/10.48550/arXiv.2608.18238) |
| **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

> ## 文章元数据
> 
> | 字段 | 详情 |
> | :--- | :--- |
> | **标题** | GenEx: A Graph-Based Representational Paradigm for SARS-CoV-2 Variant Detection via Codon Co-occurrence Networks |
> | **主要学科** | 人工智能 (`cs.AI`) |
> | **次要学科** | 定量方法 (`q-bio.QM`) |
> | **DOI** | [10.48550/arXiv.2608.18238](https://doi.org/10.48550/arXiv.2608.18238) |
> | **许可证** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

---

## Access & Resources

* **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2608.18238) | [HTML Version](https://arxiv.org/html/2608.18238v1) | [TeX Source](https://arxiv.org/src/2608.18238)
* **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18238) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18238) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18238)

> ## 访问与资源
> 
> * **全文选项：** [查看 PDF](https://arxiv.org/pdf/2608.18238) | [HTML 版本](https://arxiv.org/html/2608.18238v1) | [TeX 源码](https://arxiv.org/src/2608.18238)
> * **外部引用：** [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18238) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18238) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18238)