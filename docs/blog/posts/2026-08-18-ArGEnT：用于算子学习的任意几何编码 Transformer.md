---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- 算子学习
- Transformer
- 几何建模
- 科学机器学习
- 物理模拟
title: ArGEnT：用于算子学习的任意几何编码 Transformer
---
### 文章背景与核心概要

在科学机器学习领域，如何在任意几何形状上学习解算子（Solution Operators）一直是一个核心挑战，特别是在涉及多查询模拟、物理信息学习以及几何形状演变的场景中。现有的算子学习方法往往依赖于结构化离散化、显式几何参数化或点云公式，这些方法将几何表示与解查询采样紧密耦合，限制了其在不规则和非参数化域上的灵活性。

ArGEnT（任意几何编码 Transformer）通过将几何编码与查询点评估解耦，提出了一种全新的几何条件注意力框架。该框架包含自注意力、交叉注意力和混合注意力三种变体。通过这种解耦设计，ArGEnT 实现了与网格无关的场预测，降低了对查询点分布的敏感性，并允许利用紧凑的几何表示来调节大规模评估。在流体力学、固体力学和电化学系统等多个基准测试中，ArGEnT 表现出显著的精度提升和泛化能力，在降低预测误差的同时大幅减少了训练成本。

---

## ArGEnT：用于算子学习的任意几何编码 Transformer

### 摘要

> Learning solution operators on arbitrary geometries remains a central challenge in scientific machine learning, especially for many-query simulation, physics-informed learning, and evolving geometries requiring accurate, geometry-aware predictions at arbitrary spatial locations. Existing operator-learning methods often rely on structured discretizations, explicit geometry parameterizations, or point-cloud formulations that couple geometric representation with solution-query sampling, limiting flexibility on irregular and non-parameterized domains. We propose the Arbitrary Geometry-encoded Transformer (ArGEnT), a geometry-conditioned attention framework that decouples geometry encoding from query-point evaluation. We develop three variants: self-attention, cross-attention, and hybrid-attention. ArGEnT can be used independently or integrated with neural operators to incorporate non-geometric physical inputs. In the cross-attention variant, geometry is represented by an independently sampled point cloud used to construct keys and values, while arbitrary solution-query points construct queries. This design enables mesh-independent field prediction, reduces sensitivity to query-point distribution, and allows compact geometric representations to condition large-scale solution evaluations. Across benchmarks in fluid dynamics, solid mechanics, and electrochemical systems, ArGEnT consistently improves accuracy and generalization over standard DeepONet, point-cloud-based operator learning, and geometry-aware transformer baselines. In several cases, it reduces prediction errors by more than an order of magnitude while requiring substantially lower training cost than transformer-based baselines. These results demonstrate that decoupled geometry-query attention provides an accurate, scalable, and flexible framework for operator learning on arbitrary geometries.

在任意几何形状上学习解算子仍然是科学机器学习中的一个核心挑战，特别是在许多需要查询模拟、物理信息学习以及在任意空间位置进行精确几何感知预测的演变几何场景中。现有的算子学习方法通常依赖于结构化离散化、显式几何参数化或点云公式，这些方法将几何表示与解查询采样耦合在一起，限制了在不规则和非参数化域上的灵活性。我们提出了任意几何编码 Transformer (ArGEnT)，这是一个将几何编码与查询点评估解耦的几何条件注意力框架。我们开发了三种变体：自注意力、交叉注意力和混合注意力。ArGEnT 可以独立使用，也可以与神经算子集成，以结合非几何物理输入。在交叉注意力变体中，几何形状由独立采样的点云表示，用于构建键（keys）和值（values），而任意解查询点则构建查询（queries）。这种设计实现了与网格无关的场预测，降低了对查询点分布的敏感性，并允许紧凑的几何表示来调节大规模解评估。在流体力学、固体力学和电化学系统的基准测试中，ArGEnT 在准确性和泛化能力上始终优于标准的 DeepONet、基于点云的算子学习和几何感知 Transformer 基线。在某些情况下，它将预测误差降低了一个数量级以上，同时比基于 Transformer 的基线需要更低的训练成本。这些结果表明，解耦的几何-查询注意力为任意几何上的算子学习提供了一个准确、可扩展且灵活的框架。

---

## 论文元数据

* **arXiv ID:** [arXiv:2602.11626](https://arxiv.org/abs/2602.11626) [cs.LG]
* **学科:** 机器学习 (`cs.LG`); 人工智能 (`cs.AI`); 化学物理 (`physics.chem-ph`); 计算物理 (`physics.comp-ph`); 流体力学 (`physics.flu-dyn`)
* **报告编号:** PNNL-SA-219947
* **提交历史:**
  * **v1:** 2026年2月12日
  * **v2:** 2026年5月14日
  * **v3 (当前版本):** 2026年8月14日

---

## 作者

* **Wenqian Chen**
* **Zhi-Feng Wei**
* **Yucheng Fu**
* **Michael Penwarden**
* **Pratanu Roy**
* **Panos Stinis**

---

## 全文及访问链接

* [查看 PDF](https://arxiv.org/pdf/2602.11626)
* [HTML 版本 (实验性)](https://arxiv.org/html/2602.11626v3)
* [TeX 源码](https://arxiv.org/src/2602.11626)
* [DOI (DataCite)](https://doi.org/10.48550/arXiv.2602.11626)