---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-17
hide:
  - navigation
tags:
  - 大语言模型
  - KV-Cache
  - DropKV
  - 显存优化
  - Triton
title: "DropKV：解耦残差输出扰动的近最优 KV-Cache 驱逐策略"
---

# DropKV：解耦残差输出扰动的近最优 KV-Cache 驱逐策略

> # DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> **arXiv:2610.22130** [cs.AI]  
> **Authors:** Aozhong Zhang, Selcuk Gurses, Yanxia Deng, Naigang Wang, Chi-Chun Liu, Davis Wertheimer, Derrick Liu, Xin Li, Zi Yang, Felix X.-F. Ye, Penghang Yin  
> **Subjects:** Artificial Intelligence (`cs.AI`)  
> **Accepted Venue:** NeurIPS 2026  
> **Submitted:** October 15, 2026  
> **DOI / Paper:** [10.48550/arXiv.2610.22130](https://doi.org/10.48550/arXiv.2610.22130) | [arXiv:2610.22130](https://arxiv.org/abs/2610.22130)  

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 在长文本与长对话任务中的全面铺开，键值缓存 (Key-Value Cache, KV-Cache) 的显存开销随序列长度线性持续增长，成为了卡死模型高效长上下文推理的核心瓶颈。尽管近期的驱逐算法尝试超越传统的单一注意力打分规则，从全局层面最小化丢弃 Token 对最终模型输出的扰动，但该目标的求解在本质上却属于 NP-hard 组合优化难题，致使现有方案要么退化为缺乏理论背书的次优启发式策略，要么其实现架构过度繁复而无法在硬件层面高效算子化 (Kernelize) 。入选 NeurIPS 2026 的 **DropKV** 提出了一套基于“解耦残差输出扰动” (Decoupled Residual-Output Perturbation) 的原则性驱逐框架，创新性地将相互交织的联合驱逐决策拆解为各 Token 的独立打分，在避开组合计算爆炸的同时，在实证成立的锥体条件 (Cone Condition) 下给出了严密的常数因子近似理论保证。得益于深度定制的高性能融合 Triton 算子，DropKV 完全免除了在显存中实体化全量注意力矩阵的沉重负担，斩获了高达 19.8 倍的打分算子提速与 9.9% 的端到端预填充 (Prefill) 性能提升，在 RULER 和 LongBench 等前沿长文本基准测试中以最低的延迟全面刷新了性能上限。

---

## 内容概要

> ## Summary

在将大语言模型 (LLM) 扩展到处理长上下文输入的实际应用中，键值缓存 (KV-Cache) 的显存开销构成了极其严峻的系统瓶颈。尽管近期的先进驱逐策略试图超越传统的注意力得分启发式规则，通过端到端考量来最小化驱逐缓存对模型输出带来的扰动，但这类方法通常陷入了求解 NP-hard 组合优化问题的泥潭。这直接导致算法在数学层面只能妥协于次优解，或者演变为流程极其冗杂、难以在 GPU 底层实现高效算子化 (Kernelize) 的复杂方案。

> Key-value (KV) cache management presents a significant memory bottleneck when scaling Large Language Models (LLMs) to handle long-context inputs. While advanced eviction strategies attempt to minimize output perturbation by looking beyond traditional attention-score heuristics, they typically struggle with NP-hard combinatorial optimization problems. This leads to mathematical suboptimality or complex implementations that are difficult to kernelize. 

为了打破这些局限，**DropKV** 引入了一套基于**解耦残差输出扰动** (Decoupled Residual-Output Perturbation) 的原则性驱逐框架。通过将原本相互耦合的全局联合驱逐决策，解耦为针对各个 Token 的独立打分机制，DropKV 巧妙绕过了棘手的组合计算不可解性，并在经由长上下文大语言模型实证检验的锥体条件 (Cone Condition) 下，提供了可从数学上严格证明的常数因子近似保证。在高性能融合 Triton 算子的强力驱动下，DropKV 显著加快了打分评估与预填充 (Prefill) 阶段的运行速度，并在权威的 RULER 和 LongBench 基准测试中全面超越了现存的最强基线模型。

> To overcome these challenges, **DropKV** introduces a principled eviction framework based on **Decoupled Residual-Output Perturbation**. By decoupling joint eviction decisions into independent per-token scoring, DropKV bypasses combinatorial intractability and provides a provable constant-factor approximation guarantee. Backed by high-performance fused Triton kernels, DropKV significantly accelerates scoring and prefill speeds while outperforming state-of-the-art baselines on RULER and LongBench benchmarks.

---

## 论文元数据

> ## Paper Metadata

| 字段 | 详情 |
| :--- | :--- |
| **arXiv 编号** | [arXiv:2610.22130](https://arxiv.org/abs/2610.22130) [cs.AI] |
| **学科领域** | 人工智能 (`cs.AI`) |
| **入选会议** | NeurIPS 2026 |
| **提交日期** | 2026 年 10 月 15 日 |
| **DOI** | [10.48550/arXiv.2610.22130](https://doi.org/10.48550/arXiv.2610.22130) |

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [arXiv:2610.22130](https://arxiv.org/abs/2610.22130) [cs.AI] |
> | **Subject** | Artificial Intelligence (`cs.AI`) |
> | **Accepted Venue** | NeurIPS 2026 |
> | **Submission Date** | October 15, 2026 |
> | **DOI** | [10.48550/arXiv.2610.22130](https://doi.org/10.48550/arXiv.2610.22130) |

### 论文作者

> ### Authors

* Aozhong Zhang
* Selcuk Gurses
* Yanxia Deng
* Naigang Wang
* Chi-Chun Liu
* Davis Wertheimer
* Derrick Liu
* Xin Li
* Zi Yang
* Felix X.-F. Ye
* Penghang Yin

> * Aozhong Zhang
> * Selcuk Gurses
> * Yanxia Deng
> * Naigang Wang
> * Chi-Chun Liu
> * Davis Wertheimer
> * Derrick Liu
> * Xin Li
> * Zi Yang
> * Felix X.-F. Ye
> * Penghang Yin

---

## 论文摘要

> ## Abstract

由于显存占用随输入长度呈线性持续增长，键值缓存 (KV-Cache) 管理已成为将大语言模型 (LLM) 推向长上下文应用场景的核心瓶颈。虽然近期涌现的缓存驱逐策略已不再局限于传统的单一注意力打分规则，转而将 Value 矩阵表征纳入考量，但它们普遍面临着一个根本性的艰难权衡：用于最小化模型输出扰动的底层优化目标本质上属于 NP-hard 组合难题，这不仅使得算法在数学上容易退化为次优的启发式规则，更会导致相关算法逻辑极为复杂而难以在硬件底层实现深度算子化融合。

> Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trade-off: the underlying optimization for minimizing output perturbation is an NP-hard combinatorial problem, leading to mathematically suboptimal heuristics or implementations that are difficult to kernelize. 

在本项研究中，我们提出了 **DropKV**——一套基于解耦残差输出扰动 (Decoupled Residual-Output Perturbation) 的极简且严谨的缓存驱逐框架。通过将各 Token 相互牵扯的联合驱逐决策彻底解耦为各自独立的逐 Token 打分机制，DropKV 成功避开了组合爆炸带来的计算不可行性；同时在特定的锥体条件 (Cone Condition) 下，为算法赋予了具备数学证明的常数因子近似理论保证，我们还在三款主流长上下文大语言模型上通过大量实验充分验证了该条件的成立。

> In this work, we propose **DropKV**, a simple principled eviction framework based on Decoupled Residual-Output Perturbation. By decoupling the joint eviction decision into independent per-token scoring, DropKV circumvents combinatorial intractability and admits a provable constant-factor approximation guarantee under a cone condition that we empirically verify on three long-context LLMs. 

为了确保算法在工业落地中的实用性与高效率，我们基于融合 Triton 算子提供了一套高性能底层实现。该方案完全避免了在显存中显式实体化 (Materializing) 完整的注意力矩阵，从而带来了惊人的 **19.8 倍打分算子加速**，并在同等批处理条件下直接转化为最高达 **9.9% 的端到端预填充 (Prefill) 加速**。在 RULER 与 LongBench 等权威评测基准上的海量实验结果表明：在相同的 KV-Cache 显存预算约束下，DropKV 的任务准确率持续优于现存的所有前沿基线方案，不仅在全部同类驱逐算法中达成了最低的推理延迟，其整体推理速度甚至超越了传统的动态缓存基线。

> To ensure practical viability, we provide a high-performance implementation using fused Triton kernels that avoid materializing the full attention matrix, delivering a **19.8x scoring-kernel speedup** that translates to up to a **9.9% matched-batch end-to-end prefill speedup**. Extensive evaluations on the RULER and LongBench benchmarks demonstrate that DropKV consistently outperforms state-of-the-art baselines at equivalent cache budgets, achieving the lowest inference latency among eviction methods while also remaining faster than the dynamic cache baseline.

---

## 全文与资源链接

> ## Full-Text & Resource Links

* **论文获取途径：** 
  * [查看 PDF 全文](https://arxiv.org/pdf/2610.22130)
  * [HTML 网页阅读版 (实验性)](https://arxiv.org/html/2610.22130v1)
  * [TeX 源码包](https://arxiv.org/src/2610.22130)
* **开源许可协议：** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/)
* **外部学术引用与检索：**
  * [Google 学术搜索 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2610.22130)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.22130)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.22130)

> * **Access Options:** 
>   * [View PDF](https://arxiv.org/pdf/2610.22130)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2610.22130v1)
>   * [TeX Source](https://arxiv.org/src/2610.22130)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.22130)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.22130)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.22130)
