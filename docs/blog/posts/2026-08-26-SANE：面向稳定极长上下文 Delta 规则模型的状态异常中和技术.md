---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- Delta-Rule
- RWKV-7
- 极长上下文
- 状态异常中和
- 模型稳定性
title: SANE：面向稳定极长上下文 Delta 规则模型的状态异常中和技术
---
### 文章背景与核心概要

随着大语言模型向极长上下文（Extreme-Context）方向发展，传统的 Transformer 架构面临着严重的计算与内存瓶颈。Delta-Rule 循环模型由于保持了固定大小的状态，能够实现 $O(1)$ 的推理内存开销，因而在超长文本处理领域受到了广泛关注。然而，这类模型在面对极端上下文外推时，往往容易出现不稳定的情况，限制了其能力的充分发挥。

为了解决这一技术瓶颈，本文研究团队以 RWKV-7 在长达 1 亿（100M）token 序列上的表现为切入点，深入剖析了导致模型崩溃的具体失效机制——研究发现，问题并非源于全局状态饱和，而是由于“在相对稀疏的基底上出现了局部的范数爆炸（localized norm explosion）”。基于此洞察，作者创新性地提出了 **SANE（State Anomaly Neutralization，状态异常中和）** 技术，通过在块边界（chunk boundaries）应用自适应 $\tanh$ 压缩，在保持块内并行结构的同时有效抑制了数值异常。

实验结果表明，SANE 在短上下文任务中保持了与基线模型一致的高性能，而在超越训练长度 24,000 倍以上的 100M token 前缀测试中，仍能展现出色的功能性推理能力。该研究不仅揭示了状态压缩中的“容量-稳定性权衡（Capacity-Stability Trade-off）”，也为未来构建超长上下文循环模型提供了一条稳健的全新路径。

---

## 标题：SANE：面向稳定极长上下文 Delta 规则模型的状态异常中和技术

> SANE: State Anomaly Neutralization for Stable Extreme-Context Delta-Rule Models

**作者：** Qingwen Lin, Boyan Xu, Xiao Liu, Zhifeng Hao, Ruichu Cai  
**主要学科：** 机器学习 (`cs.LG`)，兼跨人工智能 (`cs.AI`)  
**arXiv 标识符：** [arXiv:2608.22354 [cs.LG]](https://arxiv.org/abs/2608.22354)  
**提交时间：** 2026年8月23日  

---

## 总结

> Delta-Rule recurrent models maintain a fixed-size state that enables $O(1)$ inference memory, but they often suffer from instability during extreme-context extrapolation. By analyzing RWKV-7 over sequences of up to 100 million tokens, this paper identifies a specific failure mechanism: **localized norm explosion atop a relatively sparse substrate**, rather than global state saturation. 

Delta-Rule 循环模型维护一个固定大小的状态，从而实现 $O(1)$ 的推理内存，但它们在极长上下文外推过程中经常遭遇不稳定性问题。通过分析 RWKV-7 在长达 1 亿 token 序列上的表现，本文识别出了一种特定的失效机制：**在相对稀疏的基底上出现了局部范数爆炸**，而非全局状态饱和。

> To combat this, the authors introduce **State Anomaly Neutralization (SANE)**, a technique applying adaptive $\tanh$ compression at chunk boundaries while preserving intra-chunk parallel structure. 

为了克服这一问题，作者引入了**状态异常中和（State Anomaly Neutralization, SANE）**技术，该技术在块边界应用自适应 $\tanh$ 压缩，同时保留块内并行结构。

> Key findings include:
> * **Short-Context Parity:** Within a safe threshold range ($3 \le \alpha \le 5$), SANE performs identically to the baseline across 11 short-context reasoning benchmarks with no statistically significant degradation.
> * **Extreme-Context Resilience:** After a 100M-token prefix (exceeding training length by $>24,000\times$), SANE retains functional reasoning capabilities ($33.46\text{--}35.56$), whereas the baseline model encounters numerical overflow.
> * **The Capacity-Stability Trade-off:** Overly permissive thresholds ($\alpha \ge 8$) preserve numerical stability but completely eliminate reasoning capability, demonstrating that numerical stabilization alone does not guarantee functional performance.

主要研究发现包括：
* **短上下文同等性：** 在安全的阈值范围内（$3 \le \alpha \le 5$），SANE 在 11 个短上下文推理基准测试中的表现与基线模型完全一致，且没有产生统计学意义上的性能下降。
* **极长上下文鲁棒性：** 在经过 100M token 的前缀测试后（超出训练长度达 24,000 倍以上），SANE 依然保留了功能性推理能力（$33.46\text{--}35.56$），而基线模型则遇到了数值溢出。
* **容量-稳定性权衡：** 过于宽松的阈值（$\alpha \ge 8$）虽然能够保持数值稳定性，但会彻底剥夺模型的推理能力，这表明单纯的数值稳定并不能保证功能性表现。

---

## 摘要

> Delta-Rule recurrent models maintain a fixed-size state, enabling $O(1)$ inference memory but potentially becoming unstable under extreme-context extrapolation. By tracking RWKV-7 over sequences of up to 100M tokens, we empirically identify a distinct failure pattern: **localized norm explosion atop a relatively sparse substrate**, rather than global state saturation. Analysis of the recurrent update suggests that persistent decay keeps weakly updated entries small, whereas uneven injections allow a few channels to accumulate extreme values. Motivated by this diagnosis, we propose **State Anomaly Neutralization (SANE)**, which applies adaptive $\tanh$ compression at chunk boundaries while preserving the intra-chunk parallel structure. Within a safe threshold range ($3 \le \alpha \le 5$), SANE matches the baseline on 11 short-context reasoning benchmarks with no statistically significant degradation. After a 100M-token prefix, which exceeds the training length by over $24{,}000\times$, SANE retains functional reasoning ($33.46$--$35.56$) while the baseline encounters numerical overflow. In contrast, overly permissive thresholds ($\alpha \ge 8$) remain numerically stable but lose reasoning capability entirely, showing that numerical stabilization alone does not guarantee functional reasoning and revealing a capacity--stability trade-off in state compression.

> Delta-Rule recurrent models maintain a fixed-size state, enabling $O(1)$ inference memory but potentially becoming unstable under extreme-context extrapolation. By tracking RWKV-7 over sequences of up to 100M tokens, we empirically identify a distinct failure pattern: **localized norm explosion atop a relatively sparse substrate**, rather than global state saturation. Analysis of the recurrent update suggests that persistent decay keeps weakly updated entries small, whereas uneven injections allow a few channels to accumulate extreme values. Motivated by this diagnosis, we propose **State Anomaly Neutralization (SANE)**, which applies adaptive $\tanh$ compression at chunk boundaries while preserving the intra-chunk parallel structure. Within a safe threshold range ($3 \le \alpha \le 5$), SANE matches the baseline on 11 short-context reasoning benchmarks with no statistically significant degradation. After a 100M-token prefix, which exceeds the training length by over $24{,}000\times$, SANE retains functional reasoning ($33.46$--$35.56$) while the baseline encounters numerical overflow. In contrast, overly permissive thresholds ($\alpha \ge 8$) remain numerically stable but lose reasoning capability entirely, showing that numerical stabilization alone does not guarantee functional reasoning and revealing a capacity--stability trade-off in state compression.

---

## 链接与资源

> * [View PDF](https://arxiv.org/pdf/2608.22354)
> * [TeX Source](https://arxiv.org/src/2608.22354)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.22354v1)
> * [DOI Link](https://doi.org/10.48550/arXiv.2608.22354)

* [查看 PDF](https://arxiv.org/pdf/2608.22354)
* [TeX 源码](https://arxiv.org/src/2608.22354)
* [HTML 版本（实验性）](https://arxiv.org/html/2608.22354v1)
* [DOI 链接](https://doi.org/10.48550/arXiv.2608.22354)