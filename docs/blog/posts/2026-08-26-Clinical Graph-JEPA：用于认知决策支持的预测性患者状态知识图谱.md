---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 医疗知识图谱
- 联合嵌入预测架构
- 临床决策支持
- MIMIC-IV
- 多智能体系统
title: Clinical Graph-JEPA：用于认知决策支持的预测性患者状态知识图谱
---
### 文章背景与核心概要
将临床记录转化为可靠、结构化的知识图谱，由于提取错误、本体不匹配、关系缺失以及时间模糊性等问题，历来极具挑战性，这些错误很容易传播到下游系统中。为了解决这一痛点，**Clinical Graph-JEPA** 提出了一种全新的临床知识图谱构建与优化框架。该方法没有将临床知识图谱视为静态人工产物，而是将其作为预测性的患者状态表示。

通过结合多智能体关系建议（multi-agent relation proposal）、本体感知归一化（ontology-aware normalization）、确定性证据评分（deterministic evidence scoring）以及基于 JEPA 的潜在空间优化，该系统有效地恢复了未观测到的临床关系，并显著改善了用于认知决策支持的患者状态建模。该研究在 MIMIC-IV 数据集上进行了严格评估，证明了实体基础上的文本注入能够带来显著的性能提升。

---

# Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support

## Summary

将临床记录转化为可靠、结构化的知识图谱历来是一项挑战，因为提取错误、本体不匹配、关系缺失以及时间模糊性很容易传播到下游系统中。**Clinical Graph-JEPA** 引入了一种新颖的临床知识图谱构建与优化框架。该方法不将临床知识图谱视为静态产物，而是将其视为预测性的患者状态表示。通过结合多智能体关系建议、本体感知归一化、确定性证据评分以及基于 JEPA 的潜在空间优化，该系统有效地恢复了留存的临床关系，并显著改善了用于认知决策支持的患者状态建模。

> Converting clinical records into reliable, structured knowledge graphs has historically been challenging due to extraction errors, ontology mismatches, missing relations, and temporal ambiguities that easily propagate into downstream systems. **Clinical Graph-JEPA** introduces a novel clinical knowledge graph construction and refinement framework. Rather than treating a clinical knowledge graph as a static artifact, this approach treats it as a predictive patient-state representation. By combining multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement, the system effectively recovers held-out clinical relations and significantly improves patient state modeling for cognitive decision support.

---

## Metadata & Document Information

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.22583](https://arxiv.org/abs/2608.22583) |
| **主要分类** | 机器学习 (`cs.LG`), 人工智能 (`cs.AI`) |
| **录用会议** | WM@Booth 2026 |
| **提交日期** | 2026年8月23日 |
| **DOI** | [10.48550/arXiv.2608.22583](https://doi.org/10.48550/arXiv.2608.22583) |

### 作者
* Kushagra Yadav
* Nalin Prabhath
* Amit Lamba
* Goeun Han
* Yining Mao

---

## Abstract

临床记录包含关于患者状态的丰富证据，但将这些证据转换为可靠、结构化的知识图谱仍然很困难，因为提取错误、本体不匹配、关系缺失和时间模糊性可能会传播到下游系统中。

我们提出了一种临床知识图谱构建与优化框架，该框架结合了多智能体关系建议、本体感知归一化、确定性证据评分和基于 JEPA 的潜在空间优化。我们不将临床知识图谱视为静态的提取产物，而是将其视为预测性的患者状态表示。对于每次入院，系统根据结构化的 MIMIC-IV 记录和推断的临床交叉链接构建带有证据评分的图谱，然后学习从观测到的图谱上下文中恢复留存的临床关系。

我们通过无泄漏的留一法边恢复（MRR 和 Hits@k）以及留存批次掩码评估（AUC 和 MRR）来评估该优化器。为了隔离出院小结上下文的贡献，我们将无小结嵌入的配置与注入真实出院小结表示（仅注入到小结落地的实体中）的小结增强配置进行了比较。在相同的队列和评估协议下，基于实体的出院小结注入使整体留一法 MRR 实现了 **31% 的相对提升**。

> Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. 
> 
> We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather than treating a clinical knowledge graph as a static extraction artifact, we treat it as a predictive patient-state representation. For each admission, the system constructs an evidence-scored graph from structured MIMIC-IV records and inferred clinical cross-links, then learns to recover held-out clinical relations from the observed graph context. 
> 
> We evaluate the refiner with leakage-free leave-one-out edge recovery (MRR and Hits@k) and held-out batch-mask evaluation (AUC and MRR). To isolate the contribution of discharge-note context, we compare a note-embedding-free configuration with a note-augmented configuration that injects real discharge-note representations only into note-grounded entities. Under the same cohort and evaluation protocol, entity-grounded note injection improves overall leave-one-out MRR by a **31% relative improvement**.

---

## Access & Resources

* **PDF 版本:** [查看 PDF](https://arxiv.org/pdf/2608.22583)
* **HTML 版本:** [arXiv HTML（实验性）](https://arxiv.org/html/2608.22583v1)
* **TeX 源码:** [下载源码](https://arxiv.org/src/2608.22583)
* **外部引用:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22583) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22583) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22583)