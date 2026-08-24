---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- Adam优化器
- 稳定性边缘
- 深度学习理论
- 优化算法
- 动态系统
title: 一维二次曲面上 Adam 优化器稳定性边缘（Edge-of-Stability）的可证明性
---
### 文章背景与核心概要

本文研究了 Adam 优化器在简洁的一维二次曲面设置下的“稳定性边缘”（Edge-of-Stability, EoS）现象。通过维持恒定的曲率，作者成功剥离了由优化器诱发的 EoS 背后复杂的动态机制，从而得以精确表征其在参数空间中的动态演化。

文章的主要贡献包括：在广泛的参数区间内，证明了 Adam 具有向 $2(1+\beta_1)/[\eta(1-\beta_1)]$ 这一固定稳定性阈值靠拢的恢复趋势；识别了这种趋边机制失效的特例，例如严格的亚临界周期轨道，以及在保持全过程超临界的同时收敛到最优解的特殊调谐轨迹；在没有演化损失几何（loss geometry）干扰的环境中，为 Adam 的 EoS 现象提供了具体的动力学解释，同时也明确了该现象的局限性。

---

# Provable Edge-of-Stability for Adam on a One-Dimensional Quadratic

## Summary

This paper investigates the **edge-of-stability (EoS)** phenomenon of the Adam optimizer using a clean, one-dimensional quadratic setup. By maintaining a constant curvature, the authors isolate the optimizer-induced dynamics behind EoS, allowing them to characterize the resulting parameter-space dynamics. 

Key contributions include:
* Proving that Adam exhibits a restoring tendency toward a frozen stability threshold of $2(1+\beta_1)/[\eta(1-\beta_1)]$ across broad regimes.
* Identifying exceptions where this edge-seeking mechanism breaks down, such as strictly subcritical periodic orbits and specially tuned trajectories that converge to the optimum while staying uniformly supercritical.
* Providing a concrete dynamical explanation for Adam's EoS in an environment free of evolving loss geometry, while also clarifying the limitations of the phenomenon.

---

## Paper Metadata

* **arXiv ID:** [arXiv:2608.20638](https://arxiv.org/abs/2608.20638) [cs.LG]
* **Authors:** Yiman Fong, Heng Yang
* **Submitted:** August 21, 2026
* **Primary Subject:** Machine Learning (`cs.LG`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Optimization and Control (`math.OC`)
* **DOI:** [10.48550/arXiv.2608.20638](https://doi.org/10.48550/arXiv.2608.20638)

---

## Links & Resources

* **Full-Text Access:**
  * [View PDF](https://arxiv.org/pdf/2608.20638)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.20638v1)
  * [TeX Source](https://arxiv.org/src/2608.20638)
* **External Bibliographic Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20638)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20638)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20638)

> ## Summary
> 
> This paper investigates the **edge-of-stability (EoS)** phenomenon of the Adam optimizer using a clean, one-dimensional quadratic setup. By maintaining a constant curvature, the authors isolate the optimizer-induced dynamics behind EoS, allowing them to characterize the resulting parameter-space dynamics. 
> 
> Key contributions include:
> * Proving that Adam exhibits a restoring tendency toward a frozen stability threshold of $2(1+\beta_1)/[\eta(1-\beta_1)]$ across broad regimes.
> * Identifying exceptions where this edge-seeking mechanism breaks down, such as strictly subcritical periodic orbits and specially tuned trajectories that converge to the optimum while staying uniformly supercritical.
> * Providing a concrete dynamical explanation for Adam's EoS in an environment free of evolving loss geometry, while also clarifying the limitations of the phenomenon.
> 
> ---
> 
> ## Paper Metadata
> 
> * **arXiv ID:** [arXiv:2608.20638](https://arxiv.org/abs/2608.20638) [cs.LG]
> * **Authors:** Yiman Fong, Heng Yang
> * **Submitted:** August 21, 2026
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Optimization and Control (`math.OC`)
> * **DOI:** [10.48550/arXiv.2608.20638](https://doi.org/10.48550/arXiv.2608.20638)
> 
> ---
> 
> ## Links & Resources
> 
> * **Full-Text Access:**
>   * [View PDF](https://arxiv.org/pdf/2608.20638)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.20638v1)
>   * [TeX Source](https://arxiv.org/src/2608.20638)
> * **External Bibliographic Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20638)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20638)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20638)