---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- POMDP
- 鲁棒控制
- 随机博弈
- Omega-正则目标
- 计算复杂性
title: 通过部分可观测随机博弈求解具有 Omega-正则目标的鲁棒 POMDP
---
### 文章背景与核心概要

本文探讨了在存在不确定性环境下的决策问题，即鲁棒部分可观测马尔可夫决策过程（RPOMDP）。在实际应用中，系统转移概率往往无法精确获取，只能确定其处于某个不确定性集合内。研究者针对具有一般 Omega-正则目标（如安全性、可达性及线性时序逻辑 LTL）的 RPOMDP 进行了深入分析。

文章的核心贡献在于证明了对于具有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP，该问题可以形式化地归约为求解具有相同目标的部分可观测随机博弈（POSG）。作者不仅证明了这种归约的可行性，还建立了两者之间的双向语义等价性。这一发现为 RPOMDP 和 RMDP 在各种 Omega-正则目标下的计算复杂性提供了新的上限和下限，显著扩展了该领域的理论边界。

---

## 执行摘要

本文研究了具有一般 Omega-正则目标（如安全性、可达性及线性时序逻辑）的鲁棒部分可观测马尔可夫决策过程（RPOMDP）的求解问题。作者证明，对于配备多面体不确定性集合的 $(s,a)$-矩形 RPOMDP，该问题可以正式归约为求解具有相同目标的部分可观测随机博弈（POSG）。至关重要的是，本文建立了双向的相互归约，证明了这些框架之间的语义等价性。这种等价性为 RPOMDP 和 RMDP 在各种 Omega-正则目标下提供了新的计算复杂性上限和下限。

> This paper investigates the problem of solving Robust Partially Observable Markov Decision Processes (RPOMDPs) featuring general omega-regular objectives (such as safety, reachability, and Linear Temporal Logic). The authors demonstrate that for $(s,a)$-rectangular RPOMDPs equipped with polytopic uncertainty sets, the problem can be formally reduced to solving Partially Observable Stochastic Games (POSGs) with identical objectives. Crucially, the paper establishes mutual reductions in both directions, proving the semantic equivalence between these frameworks. This equivalence yields new computational complexity upper and lower bounds for RPOMDPs and RMDPs under various omega-regular objectives.

---

## 论文元数据

- **arXiv ID:** [2608.24986](https://arxiv.org/abs/2608.24986)
- **主要学科:** 人工智能 (`cs.AI`)
- **提交日期:** 2026年8月25日
- **作者:** 
  - Durgam Latha
  - Dion Reji
  - S. Akshay
  - Djordje Zikelic
  - Shankaranarayanan Krishna

> - **arXiv ID:** [2608.24986](https://arxiv.org/abs/2608.24986)
> - **Primary Subject:** Artificial Intelligence (`cs.AI`)
> - **Submission Date:** August 25, 2026
> - **Authors:** 
>   - Durgam Latha
>   - Dion Reji
>   - S. Akshay
>   - Djordje Zikelic
>   - Shankaranarayanan Krishna

---

## 摘要

鲁棒 POMDP（RPOMDP）将经典 POMDP 推广到精确转移概率未知的情境——即概率仅已知属于某个不确定性集合。在这项工作中，我们研究了求解具有一般 Omega-正则目标的 RPOMDP 问题，该目标涵盖了广泛的类别，如可达性、安全性和线性时序逻辑（LTL）目标。

我们证明，对于具有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP，在 Omega-正则目标下求解 RPOMDP 的问题可以归约为在 Omega-正则目标下求解部分可观测随机博弈（POSG）。此外，我们首次证明了可以构建双向归约，从而建立了具有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP 与 POSG 之间的语义等价性。这使我们能够推导出关于求解具有不同 Omega-正则目标的 RPOMDP 的一系列新的计算复杂性结果，包括上限和下限。作为推论，我们也推导出了 RMDP 的新计算复杂性结果。

> Robust POMDPs (RPOMDPs) generalize classical POMDPs to the setting where exact transition probabilities are not known — rather, they are only known to belong to some uncertainty set of values. In this work, we study the problem of solving RPOMDPs with general omega-regular objectives, which subsume a broad class of objectives such as reachability, safety, and linear temporal logic (LTL) objectives. 
>
> We show that, for $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets, the problem of solving RPOMDPs under omega-regular objectives can be reduced to solving partially observable stochastic games (POSGs) under omega-regular objectives. Moreover, we show for the first time that reductions can be constructed in both directions, establishing the semantic equivalence between $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets and POSGs. This allows us to derive a range of new computational complexity results, including both upper and lower complexity bounds, on solving RPOMDPs with different omega-regular objectives. As a corollary, we also derive new computational complexity results for RMDPs.

---

## 主要贡献

1. **语义等价性：** 证明了具有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP 通过 Omega-正则目标下的双向归约，与部分可观测随机博弈（POSG）在语义上是等价的。
2. **通用目标：** 将 RPOMDP 的求解范围从简单的基于奖励的设置扩展到复杂的 Omega-正则目标，涵盖了可达性、安全性和线性时序逻辑（LTL）。
3. **复杂性界限：** 推导出了在各种 Omega-正则约束下求解 RPOMDP 和 RMDP 的新颖计算复杂性上限和下限。

> 1. **Semantic Equivalence:** Proves that $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets are semantically equivalent to Partially Observable Stochastic Games (POSGs) via bidirectional reductions under omega-regular objectives.
> 2. **General Objectives:** Expands the scope of RPOMDP solving from simple reward-based settings to complex omega-regular objectives, subsuming reachability, safety, and Linear Temporal Logic (LTL).
> 3. **Complexity Bounds:** Derives novel upper and lower computational complexity bounds for solving RPOMDPs and RMDPs across various omega-regular constraints.

---

## 其他资源

- **访问论文：** 
  - [查看 PDF](https://arxiv.org/pdf/2608.24986)
  - [HTML 版本 (实验性)](https://arxiv.org/html/2608.24986v1)
  - [TeX 源码](https://arxiv.org/src/2608.24986)
- **引用与参考：** 
  - [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.24986)
  - [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.24986)
  - [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.24986)

> - **Access Paper:** 
>   - [View PDF](https://arxiv.org/pdf/2608.24986)
>   - [HTML Version (Experimental)](https://arxiv.org/html/2608.24986v1)
>   - [TeX Source](https://arxiv.org/src/2608.24986)
> - **Citations & References:** 
>   - [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.24986)
>   - [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.24986)
>   - [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.24986)

---
*许可协议：* [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="max-height: 2em; vertical-align: middle; margin-top: 0.5em;">