---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-02
hide:
- navigation
tags:
- Scaling Laws
- LLM Pretraining
- OpenEuroLLM
- Learning Rate
- Batch Size
title: 推导 OpenEuroLLM 模型的缩放定律：学习率、批大小与损失
---
### 文章背景与核心概要
本文研究了在以英文为主的语料库上预训练稠密大语言模型（LLM）时，学习率和批大小的缩放行为。研究人员分析了联合最优参数及其相对于模型容量和数据规模的边际演变，并引入了一个综合模型来捕捉这些动态。通过采用“预热-稳定-衰减”（Warmup-Stable-Decay）学习率计划，本研究评估了在各种超参数配置、模型规模和数据预算下进行学习率退火（annealing）的优势，同时测试了最优设置在稳定阶段和衰减阶段之间的可迁移性。

此外，该研究利用能够处理欠训练（undertraining）和过训练（overtraining）机制的高级交互模型，表征了损失对模型规模和数据集大小的依赖性。这项工作为未来的 *OpenEuroLLM* 模型奠定了基础基线和缩放方法论，并开源了相关的预训练运行数据，为大模型的高效预训练提供了宝贵的经验参考。

---

## 执行摘要 (Executive Summary)

本论文研究了在以英文为主的语料库上预训练稠密大型语言模型（LLM）时，学习率和批大小的缩放行为。研究人员分析了联合最优参数及其相对于模型容量和数据规模的边际演变，并引入了一个综合模型来捕捉这些动态。通过使用**预热-稳定-衰减（Warmup-Stable-Decay）**学习率计划，本研究在广泛的超参数配置、模型规模和数据预算范围内评估了学习率退火的优势，同时测试了最优设置在稳定阶段和衰减阶段之间的可迁移性。此外，该研究通过能够解决欠训练和过训练机制的高级交互模型，表征了损失对模型规模和数据集大小的依赖性。这项工作为未来的 *OpenEuroLLM* 模型建立了基础基线和缩放方法，并伴随开源了预训练运行数据。

> This paper investigates the scaling behavior of learning rates and batch sizes when pretraining dense large language models (LLMs) on English-dominant corpora. The researchers analyze jointly optimal parameters and their marginal evolution relative to model capacity and data scale, introducing a comprehensive model to capture these dynamics. Using a **Warmup-Stable-Decay** learning rate schedule, the study evaluates the advantages of learning rate annealing across a diverse range of hyperparameter configurations, model sizes, and data budgets, while testing the transferability of optimal settings between the stable and decay phases. Additionally, it characterizes the dependence of loss on model size and dataset volume using advanced interaction models capable of addressing both undertraining and overtraining regimes. This work establishes foundational baselines and scaling methodologies for future *OpenEuroLLM* models, accompanied by open-sourced pretraining runs.

---

## 论文元数据 (Paper Metadata)

* **arXiv 标识符:** [arXiv:2608.28308](https://arxiv.org/abs/2608.28308) [cs.LG]
* **主要学科:** 机器学习 (`cs.LG`)
* **次要学科:** 人工智能 (`cs.AI`)
* **提交历史:** 
  * [v1] 2026年8月28日（星期五）
  * [v2] 2026年8月31日（星期一）（本版本）
* **许可证:** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) *(查看许可证图标：![license icon](./images/345c7ad61f1b.png))*

> * **arXiv Identifier:** [arXiv:2608.28308](https://arxiv.org/abs/2608.28308) [cs.LG]
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subject:** Artificial Intelligence (`cs.AI`)
> * **Submission History:** 
>   * [v1] Fri, 28 Aug 2026
>   * [v2] Mon, 31 Aug 2026 (This version)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(View License Icon: ![license icon](./images/345c7ad61f1b.png))*

### 作者 (Authors)
* **Niccolò Ajroldi**
* **Diana Alexandra Onutu**
* **Haider Al-Tahan**
* **Jörg Franke**
* **Sampo Pyysalo**
* **Jenia Jitsev**
* **Aaron Klein**

---

## 摘要 (Abstract)

我们研究了在英文为主的语料库上预训练稠密大型语言模型时，学习率和批大小的缩放行为。除了缩放联合最优的学习率和批大小之外，我们还研究了它们随模型容量和数据规模的边际演变，并开发了一个能够捕捉这些关系的模型。由于我们采用了“预热-稳定-衰减”学习率计划，我们进一步研究了在广泛的超参数设置、模型和数据预算下学习率退火所带来的收益，以及最优学习率和批大小是否能够在稳定阶段和衰减阶段之间进行迁移。最后，我们表征了损失对模型容量和数据集大小的依赖性，评估了显式建模其相互作用的近期提出的缩放形式。我们发现这些方法在我们的实验中对于捕捉欠训练和过训练机制特别有效。本研究为未来 OpenEuroLLM 模型的发展确立了首个基线和缩放程序。我们开源了本研究中使用的完整预训练运行集合。

> We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling jointly optimal learning rates and batch sizes, we investigate their marginal evolution with model capacity and data scale and develop a model that captures these relationships. As we employ a Warmup-Stable-Decay learning rate schedule, we further investigate the gains from learning rate annealing over a broad range of hyperparameters settings, models and data budgets, and whether the optimal learning rate and batch size transfer between the stable and decay phases. Finally, we characterize the dependence of loss on model capacity and dataset size, evaluating recently proposed scaling forms that explicitly model their interaction. We find these approaches particularly effective at capturing both undertraining and overtraining regimes across our experiments. This study establishes a first baseline and scaling procedure for the development of future OpenEuroLLM models. We open-source the complete collection of pretraining runs used in this study.

---

## 全文与资源链接 (Full-Text & Resource Links)
* **PDF 访问:** [查看 PDF](https://arxiv.org/pdf/2608.28308)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.28308v2)
* **源代码:** [TeX 源码](https://arxiv.org/src/2608.28308)
* **外部引用与工具:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28308)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28308)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28308)

> * **PDF Access:** [View PDF](https://arxiv.org/pdf/2608.28308)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.28308v2)
> * **Source Code:** [TeX Source](https://arxiv.org/src/2608.28308)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28308)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28308)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28308)