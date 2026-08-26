---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- Delta-Rule
- RWKV-7
- 状态异常中和
- 极端上下文
- 模型稳定性
title: SANE：稳定极端上下文Delta规则模型的状态异常中和技术
---
### 文章背景与核心概要

Delta规则循环模型通过维护固定大小的状态来实现 $O(1)$ 的推理内存开销，但在面对极端上下文外推时，往往会出现不稳定性。本文对处理长达 1亿（100M）token 序列的 RWKV-7 模型进行了深入研究，发现不稳定性根源于“相对稀疏基底上的局部范数爆炸”，而非全局状态饱和。

为了解决这一问题，作者提出了**状态异常中和（State Anomaly Neutralization, SANE）**方法。该方法在分块（chunk）边界应用自适应 $\tanh$ 压缩，同时保留块内并行结构。在最佳阈值范围（$\alpha \in [3, 5]$）内，SANE 能够在短期上下文推理基准测试中保持强劲性能，并成功将功能推理能力延伸至 100M token 的前缀长度（超过训练长度的 $24,000$ 倍），而基线模型则会遭遇数值溢出。此外，该研究揭示了一个关键的容量与稳定性权衡：过于宽容的阈值（$\alpha \ge 8$）虽然能确保数值稳定性，但会完全牺牲推理能力。

---

## SANE: State Anomaly Neutralization for Stable Extreme-Context Delta-Rule Models

**arXiv:** [2608.22354](https://arxiv.org/abs/2608.22354) [cs.LG]  
**Authors:** Qingwen Lin, Boyan Xu, Xiao Liu, Zhifeng Hao, Ruichu Cai  
**Submitted:** August 23, 2026 (Last revised August 25, 2026)  
**Primary Subject:** Machine Learning (`cs.LG`)  

---

## 摘要

> Delta-Rule recurrent models maintain a fixed-size state, enabling $O(1)$ inference memory but potentially becoming unstable under extreme-context extrapolation. By tracking RWKV-7 over sequences of up to 100M tokens, we empirically identify a distinct failure pattern: **localized norm explosion atop a relatively sparse substrate**, rather than global state saturation. Analysis of the recurrent update suggests that persistent decay keeps weakly updated entries small, whereas uneven injections allow a few channels to accumulate extreme values. Motivated by this diagnosis, we propose **State Anomaly Neutralization (SANE)**, which applies adaptive $\tanh$ compression at chunk boundaries while preserving the intra-chunk parallel structure. Within a safe threshold range ($3 \le \alpha \le 5$), SANE matches the baseline on 11 short-context reasoning benchmarks with no statistically significant degradation. After a 100M-token prefix, which exceeds the training length by over $24{,}000\times$, SANE retains functional reasoning ($33.46$--$35.56$) while the baseline encounters numerical overflow. In contrast, overly permissive thresholds ($\alpha \ge 8$) remain numerically stable but lose reasoning capability entirely, showing that numerical stabilization alone does not guarantee functional reasoning and revealing a capacity--stability trade-off in state compression.

Delta规则循环模型维护固定大小的状态，实现 $O(1)$ 的推理内存开销，但在极端上下文外推下可能会变得不稳定。通过追踪处理长达 1亿 token 序列的 RWKV-7，我们通过实验发现了一种独特的失效模式：**相对稀疏基底上的局部范数爆炸**，而非全局状态饱和。对循环更新的分析表明，持续的衰减使更新较弱的条目保持较小，而不均衡的注入则允许少数通道累积极端值。受此诊断启发，我们提出了**状态异常中和（SANE）**，它在分块边界应用自适应 $\tanh$ 压缩，同时保留块内并行结构。在安全的阈值范围（$3 \le \alpha \le 5$）内，SANE 在 11 个短上下文推理基准上与基线相匹配，没有统计学上显著的性能退化。在经历 100M token 的前缀（超出训练长度 $24,000$ 倍以上）后，SANE 仍保留了功能推理能力（$33.46$--$35.56$），而基线则遭遇了数值溢出。相比之下，过于宽容的阈值（$\alpha \ge 8$）虽然保持了数值稳定，但完全失去了推理能力，这表明单纯的数值稳定并不能保证功能推理，并揭示了状态压缩中的容量与稳定性权衡。

---

## 提交历史

* **[v1]** Sun, 23 Aug 2026 10:41:07 UTC (3,314 KB)
* **[v2]** Tue, 25 Aug 2026 03:15:23 UTC (2,332 KB) — *This version*

---

## 访问链接与资源

* **Paper Formats:** [View PDF](https://arxiv.org/pdf/2608.22354) | [HTML (experimental)](https://arxiv.org/html/2608.22354v2) | [TeX Source](https://arxiv.org/src/2608.22354)
* **DOI:** [10.48550/arXiv.2608.22354](https://doi.org/10.48550/arXiv.2608.22354)
* **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22354) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22354) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22354)