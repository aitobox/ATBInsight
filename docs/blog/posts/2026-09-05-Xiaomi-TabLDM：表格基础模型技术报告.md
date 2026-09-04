---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 表格数据
- 基础模型
- 上下文学习
- 合成数据
- 混合专家模型
title: Xiaomi-TabLDM：表格基础模型技术报告
---
### 文章背景与核心概要
表格数据（Tabular Data）长期以来一直是工业界和学术界预测任务的核心，但传统的机器学习模型往往需要针对每个具体任务进行繁琐的微调。为了突破这一瓶颈，小米团队推出了 Xiaomi-TabLDM，这是一个专为分类和回归任务设计的表格大模型，能够通过上下文学习（In-context Learning）实现卓越的预测准确率，而无需针对特定任务进行微调。

该模型的核心技术创新在于完全使用由结构因果模型（SCMs）生成的合成数据进行预训练，并结合了三阶段训练策略、双流特征分组、轻量级注意力残差以及稀疏混合专家模型（MoE）。这不仅赋予了模型强大的特征交互与专家特化能力，还实现了极高的计算效率。实验表明，Xiaomi-TabLDM 在多个主流基准测试（如 OpenML-CTR23、TALENT、TabArena 和 BCCO）中名列前茅，在大幅减少训练和推理时间的同时，展现出了顶尖的预测性能。此外，论文还引入了推理时计算扩展（Test-Time Scaling），进一步提升了模型的预测上限。

---

# Xiaomi-TabLDM: A Tabular Foundation Model Technical Report

**Authors:** Xiaomi-TabLDM Team (Penghui Wang, Wei Liu, Hong Wang, Chengyue Huang, Yuxi Sun, Zirui Wang, Hongming Huang, Quan Wang, Chunxiao Liu, Erli Meng, Bin Wang)  
**Submitted:** September 3, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv:** [2609.03880](https://arxiv.org/abs/2609.03880) | **DOI:** [10.48550/arXiv.2609.03880](https://doi.org/10.48550/arXiv.2609.03880)

---

## 执行摘要

**Xiaomi-TabLDM** 是一个专为分类和回归任务设计的表格大规模数据基础模型，支持通过上下文学习实现卓越的预测准确率，且无需针对特定任务进行微调。通过完全在结构因果模型（SCMs）生成的合成数据上进行预训练，该模型提供了更强的上下文利用率和极具效率的容量扩展能力。

技术报告的核心亮点包括：
* **顶级性能与效率：** 在 OpenML-CTR23 上排名第一，并在 TALENT、TabArena 和 BCCO 回归基准测试中排名第二。它在消耗显著较少资源的同时实现了极具竞争力的预测性能（例如，在 TabArena 回归任务中，它获得了第二高的 Elo 评分，且训练时间比排名第一的 TabFM **减少了 82%**，预测时间**减少了 68%**）。
* **先进的合成数据预训练与架构：** 利用多样化且规模扩大的合成表格数据、三阶段训练策略、双流特征分组、轻量级注意力残差以及稀疏混合专家模型（MoE），以捕获复杂的特征交互。
* **推理时扩展：** 引入了推理时计算扩展（Test-Time Scaling），在推理阶段进一步提升预测性能。

> **Executive Summary**
> 
> **Xiaomi-TabLDM** is a tabular large data foundation model designed for both classification and regression tasks via in-context learning. It achieves superior prediction accuracy without requiring task-specific fine-tuning. By pretraining exclusively on synthetic data generated from structural causal models (SCMs), the model offers enhanced context utilization and highly efficient capacity scaling. 
> 
> Key highlights of the technical report include:
> * **Top-Tier Performance & Efficiency:** Ranks 1st on OpenML-CTR23 and 2nd for regression across TALENT, TabArena, and BCCO benchmarks. It achieves competitive predictive performance while using significantly fewer resources (e.g., on TabArena regression, it achieves the second-highest Elo with **82% less training time** and **68% less prediction time** than the top-ranked TabFM).
> * **Advanced Synthetic Pretraining & Architecture:** Leverages a diverse, expanded scale of synthetic tabular data, a three-stage training strategy, dual-stream feature grouping, lightweight Attention Residuals, and a sparse Mixture-of-Experts (MoE) to capture complex feature interactions.
> * **Test-Time Scaling:** Introduces test-time compute scaling to further boost predictive performance during inference.

---

## 摘要

我们推出了 **Xiaomi-TabLDM**，这是一个用于分类和回归的表格大尺度基础模型，支持通过上下文 learning（上下文学习）实现卓越的预测准确率，而无需任务特定的微调。我们的模型完全在由结构因果模型（SCMs）生成的合成数据上进行预训练，从而实现了更灵活的上下文利用和更高效的容量扩展。

1. **全新的性能标准：** 在各项基准测试中表现出强劲的回归性能：Xiaomi-TabLDM 在 OpenML-CTR23 上排名第 1，在 TALENT、TabArena 和 BCCO 的回归任务中排名第 2，这表明其在四个互补的基准测试套件中均表现出持续强劲的回归性能。优异的性能-效率权衡：Xiaomi-TabLDM 将强大的预测性能与大大降低的计算成本结合在一起。例如，在 TabArena 回归任务上，它取得了第二高的 Elo 评分，同时与排名第一的 TabFM 相比，训练时间减少了 82%，预测时间减少了 68%。
2. **大规模合成数据预训练：** Xiaomi-TabLDM 扩大了用于预训练的合成表格数据的覆盖范围和多样性。我们还采用了三阶段训练策略，并结合了双流特征分组、轻量级注意力残差和稀疏混合专家模型，使 Xiaomi-TabLDM 能够在各种表格任务中学习更丰富的特征交互和专家特化。
3. **推理时扩展：** Xiaomi-TabLDM 通过推理时计算扩展进一步扩展了表格预测能力，在推理时分配额外的计算资源可以持续改善基模型的预测性能。

> **Abstract**
> 
> We introduce **Xiaomi-TabLDM**, a tabular large data foundation model for classification and regression via in-context learning, which delivers superior prediction accuracy without requiring task-specific fine-tuning. Pretrained exclusively on synthetic data generated from structural causal models (SCMs), our model enables more flexible context utilization and more efficient capacity scaling.
> 
> 1. **A New Performance Standard:** Strong regression performance across benchmarks: Xiaomi-TabLDM ranks 1st on OpenML-CTR23 and 2nd on regression across TALENT, TabArena, and BCCO, demonstrating consistently strong regression performance across four complementary benchmark suites. Favorable performance–efficiency trade-off: Xiaomi-TabLDM combines strong predictive performance with substantially lower computational cost. For example, on TabArena regression, it achieves the second-highest Elo while using 82% less training time and 68% less prediction time than the top-ranked TabFM.
> 2. **Large-Scale Synthetic Pretraining:** Xiaomi-TabLDM expands the coverage and diversity of synthetic tabular data used for pretraining. We also adopt a three-stage training strategy together with dual-stream feature grouping, lightweight Attention Residual, and sparse Mixture-of-Experts, enabling Xiaomi-TabLDM to learn richer feature interactions and expert specialization across diverse tabular tasks.
> 3. **Test-Time Scaling:** Xiaomi-TabLDM further extends tabular prediction through test-time compute scaling, where allocating additional computation at inference time consistently improves predictive performance over the base model.

---

## 附加资源与链接

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.03880) | [HTML 版本（实验性）](https://arxiv.org/html/2609.03880v1) | [TeX 源码](https://arxiv.org/src/2609.03880)
* **外部引用：** [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03880) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03880) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03880)
* **相关代码与工具：** 可通过 [Hugging Face](https://huggingface.co/huggingface) 和 [CatalyzeX Code Finder](https://www.catalyzex.com) 等平台获取。

> **Additional Resources & Links**
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.03880) | [HTML Version (Experimental)](https://arxiv.org/html/2609.03880v1) | [TeX Source](https://arxiv.org/src/2609.03880)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03880) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03880) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03880)
> * **Associated Code & Tools:** Available via platforms like [Hugging Face](https://huggingface.co/huggingface) and [CatalyzeX Code Finder](https://www.catalyzex.com).