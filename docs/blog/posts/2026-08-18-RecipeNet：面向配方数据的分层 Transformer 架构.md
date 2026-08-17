---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- Transformer
- 配方数据
- 材料合成
- 机器学习
- 层次化建模
title: RecipeNet：面向配方数据的分层 Transformer 架构
---
### 文章背景与核心概要
在材料合成、药物配方和工业制造等领域中，配方数据普遍存在且具有独特的复杂性：它们通常由按特定顺序排列的步骤序列构成，且每个步骤包含异构的结构化字段。传统的表格学习方法往往会将这种复杂的层次结构展平为固定的模式（schema），这严重限制了模型捕捉字段间复杂交互以及步骤间顺序依赖的能力。

为了克服这些传统方法的局限性，本文介绍了 **RecipeNet**——一种专为配方数据设计的层次化 Transformer 架构。通过堆叠的 Transformer 编码器，该模型能够同时对单个步骤内部的字段级交互以及多个步骤之间的顺序依赖关系进行有效编码。在多个配方数据集和下游任务上的实验表明，RecipeNet 的性能持续超越现有的表格模型，充分证明了层次化与序列化建模在配方表示学习中的巨大价值。

---

# RecipeNet: A Hierarchical Transformer for Recipe Data

## Summary
> Recipe data—commonly found in domains like materials synthesis, pharmaceutical formulation, and industrial manufacturing—consists of procedures represented as ordered sequences of steps with heterogeneous structured fields. Traditional tabular learning methods often flatten this complex structure into a fixed schema, restricting their ability to properly capture hierarchical field interactions and sequential dependencies. 
> 
> To overcome these limitations, **RecipeNet** introduces a hierarchical Transformer architecture. By utilizing stacked Transformer encoders, it effectively encodes both field-level interactions within individual steps and sequential dependencies across multiple steps, consistently outperforming existing tabular models across multiple recipe datasets and tasks.

---

## Paper Metadata

* **arXiv Identifier:** [arXiv:2608.14505](https://arxiv.org/abs/2608.14505) [cs.LG]
* **Subjects:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`)
* **Submission Date:** 14 August 2026
* **Conference Acceptance:** Accepted at CIKM 2026
* **DOI:** [10.48550/arXiv.2608.14505](https://doi.org/10.48550/arXiv.2608.14505)
* **Related DOI:** [10.1145/3799682.3839874](https://doi.org/10.1145/3799682.3839874)

## Authors
* Pin-Yen Huang
* Sachin Chhabra
* Prasanth Sai Gouripeddi
* Abhinav Kumar
* Baoxin Li

---

## Abstract
> Recipe data arises in domains such as materials synthesis, pharmaceutical formulation, and industrial manufacturing, where procedures are represented as ordered sequences of steps containing heterogeneous structured fields. Existing tabular learning methods typically flatten this structure into fixed-schema representations, limiting their ability to capture hierarchical field interactions and procedural dependencies. We propose RecipeNet, a hierarchical Transformer architecture that encodes field-level interactions within each step and sequential dependencies across steps through stacked Transformer encoders. Experiments on multiple recipe datasets and tasks demonstrate that RecipeNet consistently outperforms existing tabular models, highlighting the value of hierarchical and sequential modeling for recipe representation learning.

---

## Access Links & Resources

* **Full-Text Options:**
  * [View PDF](https://arxiv.org/pdf/2608.14505)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.14505v1)
  * [TeX Source](https://arxiv.org/src/2608.14505)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>
* **External Citations & Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.14505)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.14505)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.14505)