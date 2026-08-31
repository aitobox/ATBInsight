---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- Scaling Laws
- LLM
- OpenEuroLLM
- Pretraining
- Learning Rate
title: 推导 OpenEuroLLM 模型的缩放定律：学习率、批大小与损失
---
### 文章背景与核心概要
本文深入探讨了在以英文为主的语料库上预训练密集型大语言模型（LLM）时，学习率与批大小的缩放行为。除了研究联合最优配置外，作者还探讨了边际演化、跨不同超参数和数据预算的学习率退火（annealing）、训练阶段之间的超参数可迁移性，以及损失对模型容量和数据集大小的依赖性。

研究成果为未来 OpenEuroLLM 模型的发展确立了基础基准和缩放程序，并且官方开源了本研究所使用的所有预训练运行数据。这对于大模型预训练中的超参数调优和资源规划具有重要的指导意义。

---

# Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss

**arXiv ID:** [arXiv:2608.28308](https://arxiv.org/abs/2608.28308) [cs.LG]  
**Submitted:** 28 August 2026  
**Primary Subject:** Machine Learning (`cs.LG`)  
**Secondary Subjects:** Artificial Intelligence (`cs.AI`)  
**DOI:** [10.48550/arXiv.2608.28308](https://doi.org/10.48550/arXiv.2608.28308)  

---

## 📌 核心摘要 (Executive Summary)

本文研究了在以英文为主的语料库上预训练密集型大语言模型（LLM）时，学习率和批大小的缩放行为。除了探索联合最优配置外，作者还研究了边际演化、在多种超参数和数据预算下的学习率退火、训练阶段间的超参数可迁移性，以及损失对模型容量和数据集大小的依赖性。这些发现为未来 OpenEuroLLM 模型的发展建立了基础基准和缩放程序，并伴随开源了所有的预训练运行集合。

> This paper investigates the scaling behaviors of learning rates and batch sizes when pretraining dense large language models (LLMs) on English-prevalent corpora. Going beyond jointly optimal configurations, the authors explore marginal evolution, learning rate annealing across diverse hyperparameters and data budgets, hyperparameter transferability between training phases, and loss dependencies on model capacity and dataset size. The findings establish foundational baselines and scaling procedures for future OpenEuroLLM model development, accompanied by an open-sourced collection of all pretraining runs.

---

## 👥 作者 (Authors)

* Niccolò Ajroldi
* Diana Alexandra Onutu
* Haider Al-Tahan
* Jörg Franke
* Sampo Pyysalo
* Jenia Jitsev
* Aaron Klein

---

## 📖 摘要 (Abstract)

我们研究了在以英文为主的语料库上预训练密集型大语言模型时，学习率和批大小的缩放行为。除了对*联合最优*的学习率和批大小进行缩放研究外，我们还探讨了它们随模型容量和数据规模的*边际*演化，并开发了一个能够捕获这些关系的模型。由于我们采用了“预热-稳定-衰减”（Warmup-Stable-Decay）学习率调度策略，我们进一步研究了在广泛的超参数设置、模型和数据预算范围内进行学习率退火所带来的收益，以及最优学习率和批大小是否能在稳定阶段和衰减阶段之间进行*迁移*。最后，我们刻画了损失对模型容量和数据集大小的依赖关系，并评估了最近提出的显式建模其相互作用的缩放形式。我们发现这些方法在捕获我们实验中的欠训练和过训练状态时特别有效。本研究为未来 OpenEuroLLM 模型的发展奠定了首个基准和缩放程序。我们开源了本研究所使用的完整预训练运行集合。

> We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling *jointly optimal* learning rates and batch sizes, we investigate their *marginal* evolution with model capacity and data scale and develop a model that captures these relationships. As we employ a Warmup-Stable-Decay learning rate schedule, we further investigate the gains from learning rate annealing over a broad range of hyperparameters settings, models and data budgets, and whether the optimal learning rate and batch size *transfer* between the stable and decay phases. Finally, we characterize the dependence of loss on model capacity and dataset size, evaluating recently proposed scaling forms that explicitly model their interaction. We find these approaches particularly effective at capturing both undertraining and overtraining regimes across our experiments. This study establishes a first baseline and scaling procedure for the development of future OpenEuroLLM models. We open-source the complete collection of pretraining runs used in this study.

---

## 🔗 资源与全文访问 (Resources & Full-Text Access)

* **PDF:** [查看 PDF](https://arxiv.org/pdf/2608.28308)
* **TeX 源码:** [arXiv 源码文件](https://arxiv.org/src/2608.28308)
* **许可证:** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.28308)
> * **TeX Source:** [arXiv Source File](https://arxiv.org/src/2608.28308)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 🛠️ 引用与外部工具 (Citations & External Tools)

* **BibTeX 引用:** 可通过 [arXiv DOI / DataCite](https://doi.org/10.48550/arXiv.2608.28308) 获取
* **学术数据库:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28308)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28308)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28308)
* **社区与代码平台:** [Hugging Face](https://huggingface.co/huggingface), [CatalyzeX Code Finder](https://www.catalyzex.com), [alphaXiv](https://alphaxiv.org/), [DagsHub](https://dagshub.com/)

> * **BibTeX Citation:** Available via [arXiv DOI / DataCite](https://doi.org/10.48550/arXiv.2608.28308)
> * **Academic Databases:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28308)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28308)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28308)
> * **Community & Code Platforms:** [Hugging Face](https://huggingface.co/huggingface), [CatalyzeX Code Finder](https://www.catalyzex.com), [alphaXiv](https://alphaxiv.org/), [DagsHub](https://dagshub.com/)