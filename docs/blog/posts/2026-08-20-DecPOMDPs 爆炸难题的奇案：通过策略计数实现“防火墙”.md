---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 多智能体系统
- DecPOMDP
- 动态规划
- 策略计数
- 不确定性管理
title: DecPOMDPs 爆炸难题的奇案：通过策略计数实现“防火墙”
---
### 文章背景与核心概要

去中心化部分可观测马尔可夫决策过程（DecPOMDPs）是处理多智能体在不确定环境下决策的通用数学框架。然而，该框架面临着严重的扩展性挑战：随着智能体数量的增加，计算复杂度呈指数级增长。虽然现有的研究通过对智能体进行分区和计数（Agent Counting）来降低模型复杂度和评估成本，但这种方法却引发了新的问题——策略空间（Policy Space）的爆炸。

本文针对这一难题，提出了一种创新的解决方案：将研究重心从“智能体计数”转向“策略计数”。通过引入“策略计数 DecPOMDPs”（policy-counted DecPOMDPs），作者成功实现了在智能体数量上的可处理性。此外，本文还提出了一种基于紧凑表示的策略计数动态规划算法，能够高效地求解此类模型，为解决大规模多智能体决策问题提供了新的理论与实践路径。

---

## 元数据与出版详情

* **arXiv 标识符:** [arXiv:2608.17749](https://arxiv.org/abs/2608.17749) [cs.AI]
* **学科分类:** 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月18日
* **作者:** Nazlı Nur Karabulut, Tanya Braun
* **备注:** 本文为已被第17届可扩展不确定性管理国际会议（SUM 2026）录用的同名论文的完整版本（含附录）。
* **DOI:** [10.48550/arXiv.2608.17749](https://doi.org/10.48550/arXiv.2608.17749)

> * **arXiv Identifier:** [arXiv:2608.17749](https://arxiv.org/abs/2608.17749) [cs.AI]
> * **Subjects:** Artificial Intelligence (`cs.AI`)
> * **Submission Date:** 18 August 2026
> * **Authors:** Nazlı Nur Karabulut, Tanya Braun
> * **Comments:** Full version including appendix of a paper accepted at the 17th International Conference on Scalable Uncertainty Management (SUM 2026) under the same name.
> * **DOI:** [10.48550/arXiv.2608.17749](https://doi.org/10.48550/arXiv.2608.17749)

---

## 摘要

去中心化部分可观测马尔可夫决策过程（DecPOMDPs）为建模不确定环境下的多智能体决策提供了一个通用框架。然而，众所周知，DecPOMDPs 在智能体数量上存在指数级复杂度。应对这种智能体数量导致的不可处理性的一种方法是观察智能体之间的对称性并进行分区，从而通过计数实现紧凑编码。然而，尽管模型复杂度和评估成本降低到了多项式级别，但策略空间的爆炸却带来了新的挑战。在本文中，我们将重心从计数智能体转向计数策略，这实际上使得所谓的“策略计数 DecPOMDPs”在智能体数量上具有了可处理性。此外，我们提出了一种利用紧凑表示的策略计数动态规划方法，以高效地求解策略计数 DecPOMDPs。

> Decentralised partially observable Markov decision processes (DecPOMDPs) provide a general framework for modelling multi-agent decision making under uncertainty. However, DecPOMDPs are known to suffer from exponential complexity in the number of agents. One way to combat this intractability in agent numbers is to look at partitions of agents that exhibit a form of symmetry among agents, allowing for a compact encoding by counting. However, a challenge arises as the policy space explodes, even though the model complexity and evaluation cost reduce to a polynomial dependence. In this paper, we redirect our focus from counting agents to counting policies, which actually enables tractability in agent numbers for so called policy-counted DecPOMDPs. Further, we present policy-counted dynamic programming using the compact representation to solve policy-counted DecPOMDPs efficiently.

---

## 访问论文

* **PDF:** [查看 PDF](https://arxiv.org/pdf/2608.17749)
* **HTML:** [HTML 版本 (实验性)](https://arxiv.org/html/2608.17749v1)
* **TeX 源码:** [arXiv 源码文件](https://arxiv.org/src/2608.17749)
* **许可协议:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>

> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.17749)
> * **HTML:** [HTML Version (Experimental)](https://arxiv.org/html/2608.17749v1)
> * **TeX Source:** [arXiv Source File](https://arxiv.org/src/2608.17749)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>

---

## 外部参考与工具

* **引用与指标:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17749) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17749) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17749)
* **交互式工具:** [alphaXiv](https://alphaxiv.org/) | [Connected Papers](https://www.connectedpapers.com/) | [Scite.ai](https://www.scite.ai/)

> * **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17749) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17749) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17749)
> * **Interactive Tools:** [alphaXiv](https://alphaxiv.org/) | [Connected Papers](https://www.connectedpapers.com/) | [Scite.ai](https://www.scite.ai/)