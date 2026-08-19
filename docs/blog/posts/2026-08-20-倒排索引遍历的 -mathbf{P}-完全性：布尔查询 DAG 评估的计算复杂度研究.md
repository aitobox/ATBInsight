---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 信息检索
- 计算复杂度
- 布尔查询
- P-完全性
- 倒排索引
title: 倒排索引遍历的 $mathbf{P}$-完全性：布尔查询 DAG 评估的计算复杂度研究
---
### 文章背景与核心概要
现代人工智能智能体（AI Agents）越来越多地利用搜索基础架构来驱动复杂的神经符号推理工作流，这些工作流经常被编译为对文本字段进行深度嵌套的、非单调的布尔查询。然而，在处理这些结构时，倒排索引上的标准查询评估策略遇到了根本性的理论边界。本文深入探讨了在倒排索引上原生执行复杂逻辑的理论极限，将基于有向无环图（DAG）的检索语言（$\mathcal{L}_R$）形式化，并证明了其评估问题严格属于 **$\mathbf{P}$-完全（$\mathbf{P}$-Complete）**。

为了恢复算法的可解性，该论文引入了 **`ComputePN`**——一种确定性的、具稀疏感知能力的评估算法。通过创新的“正-负双重表示法”（Positive-Negative dual representation）将逻辑否定与全域物化解耦，并利用原生的 DAG 记忆化技术，`ComputePN` 将评估时间严格限制在 $O(|Q| \cdot |U_{\mathit{active}}|)$。该框架能够原生处理 $\mathbf{P}$-完全查询，而不会陷入组合树扩展瓶颈或全局扫描惩罚，从而为计算检索提供了坚实的理论基础。

---

# The $\mathbf{P}$-Completeness of Inverted Index Traversal: On the Complexity of Evaluating Boolean Query DAGs

**Authors:** Amir Aavani  
**Subjects:** Information Retrieval (`cs.IR`); Artificial Intelligence (`cs.AI`); Computational Complexity (`cs.CC`); Computation and Language (`cs.CL`); Databases (`cs.DB`)  
**Cite as:** [arXiv:2601.18747 [cs.IR]]  
**DOI:** [10.48550/arXiv.2601.18747](https://doi.org/10.48550/arXiv.2601.18747)  
**Submission History:** Submitted on 26 Jan 2026; Last revised 17 Aug 2026 (v3).

> # The $\mathbf{P}$-Completeness of Inverted Index Traversal: On the Complexity of Evaluating Boolean Query DAGs
> 
> **Authors:** Amir Aavani  
> **Subjects:** Information Retrieval (`cs.IR`); Artificial Intelligence (`cs.AI`); Computational Complexity (`cs.CC`); Computation and Language (`cs.CL`); Databases (`cs.DB`)  
> **Cite as:** [arXiv:2601.18747 [cs.IR]]  
> **DOI:** [10.48550/arXiv.2601.18747](https://doi.org/10.48550/arXiv.2601.18747)  
> **Submission History:** Submitted on 26 Jan 2026; Last revised 17 Aug 2026 (v3).

---

## Abstract Summary

Modern AI agents increasingly leverage search infrastructures to drive complex, neuro-symbolic reasoning workflows, which frequently compile into deeply nested, non-monotonic Boolean queries over text fields. However, standard query evaluation strategies over inverted indices hit fundamental theoretical boundaries when addressing these structures:

* **Stateful Iterator Models (Document-at-a-Time):** Structurally bounded by $\text{NC}^1$ formula evaluation, these suffer from a worst-case $O(2^{|Q|})$ exponential blowup in query complexity when unrolling re-convergent logic.
* **Recursive Materialization Models (Term-at-a-Time):** Incur an $\Omega(|U|)$ space complexity penalty (the Universal Scan) when dealing with logical negation over the broader document universe.

This paper establishes the theoretical limits of executing complex logic natively over an inverted index. The author formalizes a retrieval language ($\mathcal{L}_R$) based on Directed Acyclic Graphs (DAGs) and proves that its evaluation problem is strictly **$\mathbf{P}$-Complete**. 

To restore tractability, the paper introduces **`ComputePN`**, a deterministic, sparsity-aware evaluation algorithm. By decoupling logical negation from universe-scale materialization through a novel Positive-Negative dual representation and leveraging native DAG memoization, `ComputePN` strictly bounds evaluation time to $O(|Q| \cdot |U_{\mathit{active}}|)$. This framework handles $\mathbf{P}$-Complete queries natively without falling victim to combinatorial tree-expansion bottlenecks or universal scan penalties, thus providing a formal foundation for computational retrieval.

> ## Abstract Summary
> 
> Modern AI agents increasingly leverage search infrastructures to drive complex, neuro-symbolic reasoning workflows, which frequently compile into deeply nested, non-monotonic Boolean queries over text fields. However, standard query evaluation strategies over inverted indices hit fundamental theoretical boundaries when addressing these structures:
> 
> * **Stateful Iterator Models (Document-at-a-Time):** Structurally bounded by $\text{NC}^1$ formula evaluation, these suffer from a worst-case $O(2^{|Q|})$ exponential blowup in query complexity when unrolling re-convergent logic.
> * **Recursive Materialization Models (Term-at-a-Time):** Incur an $\Omega(|U|)$ space complexity penalty (the Universal Scan) when dealing with logical negation over the broader document universe.
> 
> This paper establishes the theoretical limits of executing complex logic natively over an inverted index. The author formalizes a retrieval language ($\mathcal{L}_R$) based on Directed Acyclic Graphs (DAGs) and proves that its evaluation problem is strictly **$\mathbf{P}$-Complete**. 
> 
> To restore tractability, the paper introduces **`ComputePN`**, a deterministic, sparsity-aware evaluation algorithm. By decoupling logical negation from universe-scale materialization through a novel Positive-Negative dual representation and leveraging native DAG memoization, `ComputePN` strictly bounds evaluation time to $O(|Q| \cdot |U_{\mathit{active}}|)$. This framework handles $\mathbf{P}$-Complete queries natively without falling victim to combinatorial tree-expansion bottlenecks or universal scan penalties, thus providing a formal foundation for computational retrieval.

---

## Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2601.18747) | [HTML (Experimental)](https://arxiv.org/html/2601.18747v3) | [TeX Source](https://arxiv.org/src/2601.18747)
* **External Bibliographic Tools:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.18747)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.18747)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.18747)

> ## Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2601.18747) | [HTML (Experimental)](https://arxiv.org/html/2601.18747v3) | [TeX Source](https://arxiv.org/src/2601.18747)
> * **External Bibliographic Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.18747)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.18747)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.18747)