---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- HTN规划
- 规划算法
- SMT
- 自动化规划
- 论文解读
title: 基于 SMT 的 HTN-SAT 编码实现数值型完全有序 HTN 规划
---
### 文章背景与核心概要
分层任务网络（HTN）规划近年来得到了蓬勃发展，然而其对数值推理的原生支持依然严重受限。本文深入研究了**数值型完全有序 HTN（TOHTN）规划**，并展示了如何利用可满足性模理论（SMT）自然地扩展标准的基于 SAT 的编码，以适应数值流畅量（numeric fluents）。

为了建立评估的基础标准，作者引入了一个专门针对数值型 TOHTN 规划的新基准测试集。其实验结果表明，这种直接的基于 SMT 的方法构成了一个极具竞争力的基准（baseline），为自动化规划中更具表现力的方法铺平了道路。

---

# 基于 SMT 的 HTN-SAT 编码实现数值型完全有序 HTN 规划

## 摘要与总结
> Hierarchical Task Network (HTN) planning has experienced substantial growth, yet native support for numerical reasoning remains severely restricted. This paper investigates **numerical Totally-Ordered HTN (TOHTN) planning** and demonstrates how standard SAT-based encodings can be naturally expanded using Satisfiability Modulo Theories (SMT) to accommodate numeric fluents. 
> 
> To establish a foundational standard for evaluation, the authors introduce a new benchmark suite tailored for numerical TOHTN planning. Their experimental findings indicate that this straightforward SMT-based approach serves as a highly competitive baseline, paving the way for significantly more expressive methodologies in automated planning.

分层任务网络（HTN）规划近年来得到了蓬勃发展，然而其对数值推理的原生支持依然严重受限。本文深入研究了**数值型完全有序 HTN（TOHTN）规划**，并展示了如何利用可满足性模理论（SMT）自然地扩展标准的基于 SAT 的编码，以适应数值流畅量。

为了建立评估的基础标准，作者引入了一个专门针对数值型 TOHTN 规划的新基准测试集。其实验结果表明，这种直接的基于 SMT 的方法构成了一个极具竞争力的基准，为自动化规划中更具表现力的方法铺平了道路。

---

## 元数据与出版详情
> ## Metadata & Publication Details

* **arXiv ID:** [arXiv:2609.03938](https://arxiv.org/abs/2609.03938) [cs.AI]
> * **arXiv ID:** [arXiv:2609.03938](https://arxiv.org/abs/2609.03938) [cs.AI]

* **学科分类:** 人工智能 (`cs.AI`)
> * **Subject:** Artificial Intelligence (`cs.AI`)

* **作者团队:** 
  * Gaspard Quenard
  * Takudzwa Togarepi
  * Damien Pellier
  * Humbert Fiorino
> * **Authors:** 
>   * Gaspard Quenard
>   * Takudzwa Togarepi
>   * Damien Pellier
>   * Humbert Fiorino

* **提交日期:** 2026年9月3日
> * **Submission Date:** September 3, 2026

* **期刊引用:** 第9届 ICAPS 分层规划研讨会论文集（HPlan 2026），第 32–36 页
> * **Journal Reference:** *Proceedings of the 9th ICAPS Workshop on Hierarchical Planning (HPlan 2026)* (pp. 32–36)

---

## 摘要原文
> ## Abstract

> While HTN planning has received significant attention in recent years, support for numerical reasoning remains very limited. In this paper, we investigate numerical Totally-Ordered HTN (TOHTN) planning and show how standard SAT-based encodings can be naturally extended with SMT to handle numeric fluents. In addition, we introduce a benchmark suite for numerical TOHTN planning, providing a first common basis for evaluation in this setting. Experimental results show that this simple encoding already constitutes a competitive baseline. This work opens the way to more expressive approaches to HTN planning.

（参见前文中文摘要）

---

## 全文与访问链接
> ## Full-Text & Access Links

* [查看 PDF](https://arxiv.org/pdf/2609.03938)
> * [View PDF](https://arxiv.org/pdf/2609.03938)

* [HTML 版本（实验性）](https://arxiv.org/html/2609.03938v1)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.03938v1)

* [TeX 源码](https://arxiv.org/src/2609.03938)
> * [TeX Source](https://arxiv.org/src/2609.03938)

* [DOI (DataCite)](https://doi.org/10.48550/arXiv.2609.03938)
> * [DOI (DataCite)](https://doi.org/10.48550/arXiv.2609.03938)

---

## 相关资源与工具
> ## Associated Resources & Tools

* **外部引用:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03938) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03938) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03938)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03938) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03938) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03938)

* **代码与目录:** 可通过 CatalystX、Hugging Face 和 DagsHub 等社区平台访问（实时追踪请参考源平台上的 arXivLabs 集成面板）。
> * **Code & Catalogs:** Accessible via community platforms like CatalystX, Hugging Face, and DagsHub (refer to arXivLabs integration panels on the source platform for live tracking).