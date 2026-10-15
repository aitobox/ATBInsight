---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-15
hide:
  - navigation
tags:
  - SpecFit
  - MoE
  - 投机解码
  - 推理加速
title: "SpecFit 破局 MoE 离线推理：草稿 Token 成本差异化与子模优化加速"
---

# SpecFit 破局 MoE 离线推理：草稿 Token 成本差异化与子模优化加速

> # SpecFit: Not All Draft Tokens Cost the Same in Offloaded MoE Inference

> **arXiv:2610.15417** [cs.AI]  
> **Authors:** Hongliang Cao, Xiuyu Li, Siqi Wang, Ziming Wang, Jingmin Zhu, Hailong Yang  
> **Submitted:** October 11, 2026  
> **Paper:** [arXiv:2610.15417](https://arxiv.org/abs/2610.15417) | [View PDF](https://arxiv.org/pdf/2610.15417) | [Source Code](https://github.com/Chlience/SpecFit)  

### 文章背景与核心概要

混合专家模型 (Mixture-of-Experts, MoE) 凭借“按需激活”的稀疏计算特性，在大模型时代实现了参数规模与计算能效的绝佳平衡；然而，当数百亿的专家参数因显存不足而被卸载 (Offload) 到系统主机内存时，从主机内存到显存 (Host-to-Device, H2D) 的跨设备数据传输便瞬间跃升为拖慢自回归解码的核心瓶颈。虽然业界广泛采用投机解码 (Speculative Decoding) 试图通过单次前向传播同时验证多个草稿 Token (Draft Tokens) 来提速，但在 MoE 架构下，每个待验证的候选 Token 都可能唤醒完全不同的专家网络，盲目扩大草稿树不仅无法提速，反倒会迫使系统搬运海量专家权重，出现投机解码速度甚至反常落后于标准自回归解码的“加速负收益”怪象。为了破解这一困局，来自北京航空航天大学等机构的研究团队提出了 **SpecFit** 框架，首次打破了传统投机解码盲目堆砌候选接受长度的单一指标，开创性地确立了“以最大化预测吞吐量为核心”的草稿树动态剪裁准则。SpecFit 精准捕捉到各层激活专家集合并集天然具备的单调子模覆盖 (Monotone Submodular Coverage) 特性，仅针对每个候选节点带来的边际新增专家进行成本核算，并通过祖先闭包子树上的精确搜索算法，在每一个草稿层级动态决策最佳候选组合与最优终止时机。在 Qwen3-30B-A3B 等前沿开源模型上的评测表明，SpecFit 在相同专家缓存下相比主流方案 EAGLE-3 实现了最高 21.6% 的解码加速，面对原生 EAGLE-3 更是达成了最高 1.97 倍的强劲吞吐跃迁，为低显存环境下超大规模 MoE 模型的高效落地开辟了全新的工程优化范式。

---

## 内容概要

> ## Summary

在混合专家模型 (MoE) 中，网络每处理一个 Token 仅需激活所有专家中的一小部分子集。然而，当显存容量告急、不得不将庞大的专家层权重参数卸载 (Offload) 到系统主机内存时，在每次解码迭代中将专家数据从主机搬运至 GPU 显存 (H2D) 的传输开销，便无可避免地成为了卡住整个解码流程的关键瓶颈。

> Mixture-of-Experts (MoE) models activate only a subset of experts per token. However, when expert weights are offloaded to host memory, host-to-device (H2D) expert transfers become a critical bottleneck during decoding. 

投机解码虽然可以通过单次前向验证同时确认多个草稿 Token 来实现推理加速，但它也给 MoE 架构带来了前所未有的特有难题：每一个待验证的候选 Token 都可能激活一组全然不同的专家网络。这导致草稿树分支越多、规模越大，就越会强迫系统从主机内存中搬运海量的专家权重。在如此巨大的显存通信开销拖累下，传统投机解码在 MoE 卸载环境下非但没有提速，实际性能有时甚至比规规矩矩逐字生成的标准自回归解码还要*更差*。

> While speculative decoding accelerates inference by verifying multiple draft tokens in a single forward pass, it introduces a unique challenge in MoE models: each verified token activates its own distinct set of experts. Consequently, larger draft trees force massive H2D transfers. Due to this high memory transfer overhead, traditional speculative decoding can sometimes perform *worse* than standard autoregressive decoding.

为了攻克这一痛点，论文作者提出了 **SpecFit** 优化框架。该框架一改传统算法单纯追求最大化接受长度的局限，转为以“最大化预测吞吐量”为核心准则来指导草稿树的构建与裁决：

> To address this issue, the authors introduce **SpecFit**, an optimized framework designed to maximize predicted throughput rather than simply maximizing acceptance length:

* **吞吐量驱动的路径选择 (Throughput-Driven Selection) ：** SpecFit 依据草稿路径的转移概率来精确估算最终被确认的 Token 期望数量，同时综合草稿树的节点规模与各网络层激活专家的并集，精准预测整个验证周期的实际执行耗时。
* **子模优化算法 (Submodular Optimization) ：** 鉴于每一层激活专家的并集在数学上天然构成单调子模覆盖函数 (Monotone Submodular Coverage Function) ，系统在评估每一个新增节点时，能够严格且仅为其引入的“边际新增专家”核算传输开销，避免重复计费。
* **精确子树搜索 (Exact Subtree Search) ：** 通过在满足祖先闭包 (Ancestor-Closed) 约束的候选子树空间中执行精确搜索算法，SpecFit 能够高效锁定能带来最高预测吞吐量的最优子树，并在草稿生成的每个层级动态决断最佳终止时机。

> * **Throughput-Driven Selection:** SpecFit estimates the expected number of committed tokens using draft path probabilities while predicting cycle time based on node count and the per-layer union of activated experts.
> * **Submodular Optimization:** Because the per-layer union of experts forms a monotone submodular coverage function, each node is evaluated strictly on the marginal experts it adds.
> * **Exact Subtree Search:** An exact search algorithm over ancestor-closed subtrees determines the optimal subtree for the highest predicted throughput and dynamically decides when to stop drafting.

### 性能表现亮点

> ### Performance Highlights

在 Qwen3-30B-A3B 模型上，针对 CNN/DailyMail 文本摘要任务与 GSM8K 数学推理子集的基准测试中，**SpecFit** 取得了显著的推理加速成果：

> Tested on the Qwen3-30B-A3B model across CNN/DailyMail summarization and a GSM8K subset, **SpecFit** achieves significant speedups:

* 在配置相同容量专家缓存的条件下，相比前沿投机解码方案 EAGLE-3 的推理速度分别提升了 **21.6% 与 7.0%**；
* 相比未配备专用缓存的原生 EAGLE-3 基线方案，解码速度更是分别达到了后者的 **1.97 倍与 1.72 倍**。

> * **21.6% and 7.0% faster** than EAGLE-3 when using the same expert cache.
> * **1.97x and 1.72x as fast** as vanilla EAGLE-3.

---

## 论文摘要

> ## Abstract

混合专家模型 (MoE) 在推理时每个 Token 仅激活少数几位专家，但当海量专家权重被卸载 (Offload) 到系统主机内存时，从主机到设备 (H2D) 的跨设备专家传输开销便直接挤占了自回归解码的关键执行路径。投机解码虽然能在单次前向传播中同时验证多个草稿 Token ，但在 MoE 架构中，每个待验证的 Token 都会激活其独有的专家网络，导致更为庞大的草稿树必须搬运更多的专家参数。受制于这一沉重的 H2D 通信代价，投机解码尽管在每个验证周期内确实能确认数个 Token ，其实际解码效率在很多场景下甚至反常地慢于标准自回归解码。针对这一关键现象，我们提出了 SpecFit 优化框架，通过精心挑选待验证的草稿子树来最大化预测吞吐量，而非片面追求最长接受长度。SpecFit 利用草稿路径概率来估算被最终采纳的 Token 期望数量，并依据树节点总数以及子树所激活专家的每层并集规模来精准预测单轮执行周期；该专家并集在数学上天然构成单调子模覆盖函数 (Monotone Submodular Coverage Function) ，从而确保每个候选节点仅为其带来的边际新增专家支付传输成本。在满足祖先封闭特性的子树空间中，精确搜索算法能够快速返回预测吞吐量最高的最优子树；该搜索在每一级草稿生成后实时执行，可动态决断何时适时停止草稿生成，并直接交由未经修改的目标大模型完成高效验证。在 Qwen3-30B-A3B 模型针对 CNN/DailyMail 文本摘要任务与 GSM8K 数学推理子集的评测中，SpecFit 在相同专家缓存下比 EAGLE-3 的解码速度分别加快了 21.6% 与 7.0%，与原生 EAGLE-3 相比更是分别实现了高达 1.97 倍和 1.72 倍的加速。

> Mixture-of-experts (MoE) models activate only a few experts per token, but when their expert weights are offloaded to host memory, host-to-device (H2D) expert transfers enter the critical path of decoding. Speculative decoding verifies several draft tokens in one forward pass, yet in an MoE model each verified token activates its own experts, so a larger draft tree transfers more experts. Because of this H2D cost, speculative decoding commits several tokens per verification cycle yet is sometimes even slower than autoregressive decoding. Based on this observation, we propose SpecFit, which chooses the verified draft subtree to maximize predicted throughput rather than acceptance length. SpecFit estimates the expected number of committed tokens from draft path probabilities and predicts cycle time from the node count and the per-layer union of the experts the subtree activates; this union is a monotone submodular coverage function, so each node pays only for the experts it adds. An exact search over ancestor-closed subtrees returns the subtree with the highest predicted throughput; run after each draft level, the same search also decides when to stop drafting, and the unmodified target verifies the result. On CNN/DailyMail summarization and a GSM8K subset with Qwen3-30B-A3B, SpecFit decodes 21.6% and 7.0% faster than EAGLE-3 with the same expert cache and 1.97x and 1.72x as fast as vanilla EAGLE-3.

---

## 附加资源与元数据

> ## Additional Resources & Metadata

* **开源许可协议：** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **数字对象唯一标识符 (DOI) ：** [10.48550/arXiv.2610.15417](https://doi.org/10.48550/arXiv.2610.15417)
* **学术检索与工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.15417) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.15417)

> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2610.15417](https://doi.org/10.48550/arXiv.2610.15417)
> * **External Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.15417) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.15417)
