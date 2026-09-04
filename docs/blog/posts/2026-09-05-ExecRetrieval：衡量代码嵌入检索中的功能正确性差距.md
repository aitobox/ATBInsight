---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 代码检索
- 嵌入模型
- 基准测试
- 软件工程
- EMNLP
title: ExecRetrieval：衡量代码嵌入检索中的功能正确性差距
---
### 文章背景与核心概要
基于嵌入（Embedding）的代码检索是现代编程智能体（Coding Agents）和检索增强代码生成（RAG）的核心技术。在这些应用场景中，寻找“功能正确”的代码远比单纯寻找词法相似的代码更为关键。然而，传统基准测试往往无法有效检验稠密嵌入是否具备真正分辨正确代码与“近克隆但错误”的变体的能力。

为了填补这一空白，本文作者推出了 **ExecRetrieval** 基准测试，包含 939 个 Python 任务。每个任务均配有一个经执行验证的规范实现，以及多达四个通过单次修改（Single-edit）机械突变生成的、经执行验证的错误干扰项。通过对 23 种稠密嵌入配置及 BM25 进行评估，研究揭示了一个显著的“功能正确性差距”：虽然顶级系统在更宽泛的指标上取得了高分（例如 `exec@10 = 1.00`），但其在首位排名的精准度上却大幅下滑（`exec@1 = 0.331`）。此外，在领先系统中，有 67% 至 78% 的查询里，规范解决方案的得分甚至低于至少一个与之配对的干扰项。

---

## ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval

## Summary

Embedding-based code retrieval is vital for modern coding agents and retrieval-augmented code generation, where finding *functionally correct* code is far more critical than merely finding lexically similar code. Traditional benchmarks often fail to test whether dense embeddings can genuinely discriminate between correct code and near-clone-but-incorrect variants. 

To address this gap, the authors introduce **ExecRetrieval**, a benchmark comprising 939 Python tasks. Each task is paired with an execution-verified canonical implementation and up to four execution-verified buggy distractors generated via single-edit mechanical mutations. Evaluating 23 dense embedding configurations alongside BM25, the study reveals a significant "functional-correctness gap": while top systems achieve high scores at broader metrics (e.g., `exec@10 = 1.00`), their precision falters at the top rank (`exec@1 = 0.331`). Furthermore, canonical solutions score below at least one paired distractor in 67–78% of queries for leading systems.

> Embedding-based code retrieval is vital for modern coding agents and retrieval-augmented code generation, where finding *functionally correct* code is far more critical than merely finding lexically similar code. Traditional benchmarks often fail to test whether dense embeddings can genuinely discriminate between correct code and near-clone-but-incorrect variants. 
> 
> To address this gap, the authors introduce **ExecRetrieval**, a benchmark comprising 939 Python tasks. Each task is paired with an execution-verified canonical implementation and up to four execution-verified buggy distractors generated via single-edit mechanical mutations. Evaluating 23 dense embedding configurations alongside BM25, the study reveals a significant "functional-correctness gap": while top systems achieve high scores at broader metrics (e.g., `exec@10 = 1.00`), their precision falters at the top rank (`exec@1 = 0.331`). Furthermore, canonical solutions score below at least one paired distractor in 67–78% of queries for leading systems.

---

## Paper Metadata

* **arXiv ID:** [`arXiv:2609.01865`](https://arxiv.org/abs/2609.01865) [cs.SE]
* **Authors:** Aaryan Kapoor, Md Abdullah Al Hafiz Khan
* **Primary Subject:** Software Engineering (`cs.SE`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Information Retrieval (`cs.IR`)
* **Publication:** Accepted to EMNLP 2026 (Main Conference, Camera-ready version)
* **Submitted:** September 1, 2026

> * **arXiv ID:** [`arXiv:2609.01865`](https://arxiv.org/abs/2609.01865) [cs.SE]
> * **Authors:** Aaryan Kapoor, Md Abdullah Al Hafiz Khan
> * **Primary Subject:** Software Engineering (`cs.SE`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Information Retrieval (`cs.IR`)
> * **Publication:** Accepted to EMNLP 2026 (Main Conference, Camera-ready version)
> * **Submitted:** September 1, 2026

---

## Abstract

基于嵌入的代码检索是编程智能体和检索增强代码生成的核心组件，在此类场景中，检索到正确的代码远比检索到词法相似的代码更为重要。现有的代码检索基准测试并未在搜索池中植入针对每个查询的规范实现的受控、经执行验证的单次修改变体，这使得在检索设定下，嵌入模型能否在功能上区分正确代码与近克隆但错误的代码这一问题长期悬而未决。

> Embedding-based code retrieval is a core component of coding agents and retrieval-augmented code generation, where retrieving correct code matters more than retrieving lexically similar code. Existing code-retrieval benchmarks do not plant controlled, execution-verified single-edit variants of each query's canonical implementation in the search pool, leaving the question of whether embeddings can functionally discriminate correct from near-clone-but-incorrect code unanswered in a retrieval setting. 

解决这一问题需要这样一个基准测试：其搜索池本身就包含相关的反事实样本——即与各个规范实现高度相似、经执行验证的错误变体，从而可以直接测试检索器的排序是否具备功能鉴别能力，而非仅仅停留在主题或标识符的重合度上。我们推出了 **ExecRetrieval**，包含 939 个 Python 任务，每个任务配有一个经执行验证的规范实现以及多达四个经执行验证的错误干扰项，每个干扰项都是通过进行单次定向修改的机械突变生成的。在提供商原生调用下，我们结合配对 McNemar 检验和查询级自助采样区间（Bootstrap intervals），评估了 23 种稠密嵌入配置以及 BM25。

> Resolving this requires a benchmark whose search pool itself contains the relevant counterfactuals—execution-verified buggy variants near-identical to each canonical—so that a retriever's rank ordering can be directly tested for functional discrimination rather than topical or identity overlap. We introduce **ExecRetrieval**, 939 Python tasks each paired with one execution-verified canonical implementation and up to four execution-verified buggy distractors, each generated by a mechanical mutation making a single targeted edit, and evaluate 23 dense embedding configurations plus BM25 under provider-native invocation with paired McNemar tests and query-level bootstrap intervals. 

当搜索池中存在近克隆反事实样本时，顶级的托管系统达到了 `exec@10 = 1.00`，但在首位命中率上仅为 `exec@1 = 0.331`；在四个领先系统中，排在第 1 位的未命中结果有 91.5%–99.4% 的情况是配对的错误变体；并且在领先系统的 67%–78% 的查询中，规范实现的得分低于其四个配对干扰项中的至少一个。

> With near-clone counterfactuals in the pool, the top hosted system reaches `exec@10 = 1.00` but only `exec@1 = 0.331`; rank-1 misses are paired buggy variants 91.5–99.4% of the time across the four leading systems, and the canonical scores below at least one of its four paired distractors in 67–78% of queries on the leading systems.

---

## Resources & Links

* **查看 PDF:** [arXiv:2609.01865 PDF](https://arxiv.org/pdf/2609.01865)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2609.01865v1)
* **DOI:** [10.48550/arXiv.2609.01865](https://doi.org/10.48550/arXiv.2609.01865)
* **数据集与代码资产:** 完整的数据集、执行谕示（Oracle）、嵌入矩阵、环境快照以及成对统计检验均可通过论文附录 D 中提供的链接获取。

> * **View PDF:** [arXiv:2609.01865 PDF](https://arxiv.org/pdf/2609.01865)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2609.01865v1)
> * **DOI:** [10.48550/arXiv.2609.01865](https://doi.org/10.48550/arXiv.2609.01865)
> * **Dataset & Code Artifacts:** Full dataset, execution oracle, embedding matrices, environment snapshot, and pairwise statistical tests are available via the link provided in Appendix D of the paper.