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
- 鲁棒马尔可夫决策过程
- 随机博弈
- 线性时序逻辑
- 计算复杂度
title: 通过部分可观测随机博弈求解带有Omega正则目标的鲁棒POMDP
---
### 文章背景与核心概要
本文研究了具有通用 omega 正则目标（如安全性、可达性和线性时序逻辑）的鲁棒部分可观测马尔可夫决策过程（RPOMDPs）的求解问题。作者证明了对于配备有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP，该问题可以正式简化为求解具有相同目标的部分可观测随机博弈（POSG）。

更为关键的是，该论文在双向均建立了归约关系，证明了这两个框架之间的语义等价性。这种等价性为在各种 omega 正则目标下的 RPOMDPs 和 RMDPs 推导出了全新的计算复杂度上界与下界，极大地拓展了我们在不确定环境中进行形式化决策验证的理论认知。

---

# Solving Robust POMDPs with Omega-regular Objectives via Partially Observable Stochastic Games

## Executive Summary
> This paper investigates the problem of solving Robust Partially Observable Markov Decision Processes (RPOMDPs) featuring general omega-regular objectives (such as safety, reachability, and Linear Temporal Logic). The authors demonstrate that for $(s,a)$-rectangular RPOMDPs equipped with polytopic uncertainty sets, the problem can be formally reduced to solving Partially Observable Stochastic Games (POSGs) with identical objectives. Crucially, the paper establishes mutual reductions in both directions, proving the semantic equivalence between these frameworks. This equivalence yields new computational complexity upper and lower bounds for RPOMDPs and RMDPs under various omega-regular objectives.

---

## Paper Metadata
## 论文元数据

- **arXiv ID:** [2608.24986](https://arxiv.org/abs/2608.24986)
- **Primary Subject:** Artificial Intelligence (`cs.AI`)
- **Submission Date:** August 25, 2026
- **Authors:** 
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

## Abstract
## 摘要

鲁棒 POMDP（RPOMDP）将经典 POMDP 推广到了转移概率未知、仅已知属于某种不确定性集合的场景。在这项工作中，我们研究了求解具有通用 omega 正则目标的 RPOMDP 的问题，该目标涵盖了可达性、安全性以及线性时序逻辑（LTL）目标等广泛的类别。

我们证明了对于具有多面体不确定性集合的 $(s,a)$-矩形 RPOMDP，在 omega 正则目标下求解 RPOMDP 的问题可以归约为求解具有 omega 正则目标的部分可观测随机博弈（POSG）。此外，我们首次证明了双向都可以构造归约，从而确立了配备多面体不确定性集合的 $(s,a)$-矩形 RPOMDP 与 POSG 之间的语义等价性。这使我们能够推导出一系列关于在不同 omega 正则目标下求解 RPOMDP 的计算复杂度新结果，包括上界和下界。作为推论，我们也为 RMDP 导出了新的计算复杂度结果。

> Robust POMDPs (RPOMDPs) generalize classical POMDPs to the setting where exact transition probabilities are not known — rather, they are only known to belong to some uncertainty set of values. In this work, we study the problem of solving RPOMDPs with general omega-regular objectives, which subsume a broad class of objectives such as reachability, safety, and linear temporal logic (LTL) objectives. 
> 
> We show that, for $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets, the problem of solving RPOMDPs under omega-regular objectives can be reduced to solving partially observable stochastic games (POSGs) under omega-regular objectives. Moreover, we show for the first time that reductions can be constructed in both directions, establishing the semantic equivalence between $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets and POSGs. This allows us to derive a range of new computational complexity results, including both upper and lower complexity bounds, on solving RPOMDPs with different omega-regular objectives. As a corollary, we also derive new computational complexity results for RMDPs.

---

## Key Contributions
## 核心贡献

1. **语义等价性：** 通过在 omega 正则目标下的双向归约，证明了配备多面体不确定性集合的 $(s,a)$-矩形 RPOMDP 与部分可观测随机博弈（POSG）在语义上是等价的。
2. **通用目标：** 将 RPOMDP 求解的范围从简单的基于奖励的设置扩展到复杂的 omega 正则目标，涵盖了可达性、安全性和线性时序逻辑（LTL）。
3. **复杂度界限：** 推导出了在各种 omega 正则约束下求解 RPOMDP 和 RMDP 的全新计算复杂度上界和下界。

> 1. **Semantic Equivalence:** Proves that $(s,a)$-rectangular RPOMDPs with polytopic uncertainty sets are semantically equivalent to Partially Observable Stochastic Games (POSGs) via bidirectional reductions under omega-regular objectives.
> 2. **General Objectives:** Expands the scope of RPOMDP solving from simple reward-based settings to complex omega-regular objectives, subsuming reachability, safety, and Linear Temporal Logic (LTL).
> 3. **Complexity Bounds:** Derives novel upper and lower computational complexity bounds for solving RPOMDPs and RMDPs across various omega-regular constraints.

---

## Additional Resources
## 附加资源

- **获取论文：** 
  - [查看 PDF](https://arxiv.org/pdf/2608.24986)
  - [HTML 版本（实验性）](https://arxiv.org/html/2608.24986v1)
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
*License:* [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="max-height: 2em; vertical-align: middle; margin-top: 0.5em;">