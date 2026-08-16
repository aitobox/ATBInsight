---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- Transformer
- QKV
- KV缓存
- 模型优化
- 边缘计算
title: Transformer 需要三个投影吗？QKV 变体的系统性研究
---
### 文章背景与核心概要

在当前的深度学习架构中，Transformer 模型已成为自然语言处理和计算机视觉领域的基石。然而，标准的自注意力机制（Self-Attention）需要为查询（Queries, $Q$）、键（Keys, $K$）和值（Values, $V$）分别计算三个独立的线性投影，这在边缘设备和端侧部署（On-device Deployment）中带来了显著的内存开销和计算瓶颈。为了解决这一问题，本文系统性地探讨了 Transformer 是否真的需要这三个独立的投影，或者是否可以通过共享或省略部分投影来提升内存效率。

研究人员对三种投影共享约束进行了系统性评估：$Q$-$K=V$（共享键值）、$Q=K$-$V$（共享查询键）以及 $Q=K=V$（单投影）。通过在合成任务、视觉数据集以及大语言模型（LLM）上的广泛实验，该研究表明，优化的投影共享（特别是 $Q$-$K=V$ 方案）能够在极小的性能损失下实现显著的内存节省。结合现有的多查询注意力（MQA）技术时，最高可实现 96.9% 的 KV 缓存缩减，为资源受限环境下的高效大模型部署开辟了新途径。

---

## Executive Summary / 执行摘要

This paper investigates whether Transformers actually require three separate projections for Queries ($Q$), Keys ($K$), and Values ($V$), or if some of these projections can be shared or omitted to improve memory efficiency—particularly for edge and on-device deployment. 

> 本文研究了 Transformer 是否真的需要为查询（$Q$）、键（$K$）和值（$V$）设置三个独立的投影，或者是否可以共享或省略其中部分投影来提升内存效率——特别是针对边缘设备和端侧部署。

The authors systematically study three projection-sharing constraints:
1. **$Q$-$K=V$**: Shared Key-Value
2. **$Q=K$-$V$**: Shared Query-Key
3. **$Q=K=V$**: Single Projection

> 作者系统地研究了三种投影共享约束：
> 1. **$Q$-$K=V$**：共享键值
> 2. **$Q=K$-$V$**：共享查询键
> 3. **$Q=K=V$**：单投影

Through extensive experiments across synthetic tasks, vision datasets, and large language models (LLMs), the study demonstrates that optimized projection sharing (especially $Q$-$K=V$) achieves significant memory savings (up to 96.9% KV cache reduction when combined with MQA) with minimal performance degradation.

> 通过对合成任务、视觉数据集和大语言模型（LLM）的大量实验，该研究表明，优化的投影共享（特别是 $Q$-$K=V$）能够在性能退化极小的情况下实现显著的内存节省（与 MQA 结合时，KV 缓存缩减高达 96.9%）。

---

## Key Highlights & Findings / 核心亮点与发现

* **Performance Parity**: Transformers utilizing projection sharing perform on par with—and occasionally better than—standard QKV transformers.
> * **性能相当**：采用投影共享的 Transformer 其性能与标准 QKV Transformer 相当，甚至在某些情况下表现更好。
* **Language Modeling Efficiency**: In LLM evaluations (300M and 1.2B parameter models trained on 10B tokens), the **$Q$-$K=V$** variant achieves a **50% KV cache reduction** with only a **3.1% degradation in perplexity**.
> * **语言建模效率**：在大语言模型评估中（在 10B 词元上训练的 300M 和 1.2B 参数模型），**$Q$-$K=V$** 变体实现了 **50% 的 KV 缓存缩减**，而困惑度（Perplexity）仅退化了 **3.1%**。
* **Compatibility with Head Sharing**: Projection sharing is fully complementary to existing head-sharing techniques like Grouped-Query Attention (GQA) and Multi-Query Attention (MQA):
  * **$Q$-$K=V$ + GQA-4**: Yields an **87.5% cache reduction**.
  * **$Q$-$K=V$ + MQA**: Yields a **96.9% cache reduction**.
> * **与头共享技术的兼容性**：投影共享与现有的头共享技术（如分组查询注意力 GQA 和多查询注意力 MQA）完全互补：
>   * **$Q$-$K=V$ + GQA-4**：实现 **87.5% 的缓存缩减**。
>   * **$Q$-$K=V$ + MQA**：实现 **96.9% 的缓存缩减**。
* **Why it Works**: The $Q$-$K=V$ approach preserves model quality because keys and values naturally occupy similar representational spaces, and attention operates in a low-rank regime. Conversely, $Q=K$-$V$ disrupts attention directionality, requiring auxiliary adjustments like 2D positional encodings.
> * **有效的原因**：$Q$-$K=V$ 方法之所以能保持模型质量，是因为键和值天然占据相似的表征空间，且注意力机制运行在低秩区间。相反，$Q=K$-$V$ 会破坏注意力的方向性，需要诸如 2D 位置编码等辅助调整。

---

## Paper Metadata / 论文元数据

* **Authors:** Ali Kayyam, Anusha Madan Gopal, M Anthony Lewis
* **Subjects:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Performance (`cs.PF`)
* **Venue:** Accepted at ICML 2026 (PMLR vol. 306)
* **arXiv ID:** [arXiv:2606.04032](https://arxiv.org/abs/2606.04032)
* **Code Repository:** [GitHub - Do-Transformers-Need-3-Projections](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections)

> * **作者：** Ali Kayyam, Anusha Madan Gopal, M Anthony Lewis
> * **研究领域：** 机器学习（`cs.LG`）、人工智能（`cs.AI`）、计算与语言（`cs.CL`）、性能（`cs.PF`）
> * **会议收录：** 已被 ICML 2026 接受（PMLR vol. 306）
> * **arXiv ID：** [arXiv:2606.04032](https://arxiv.org/abs/2606.04032)
> * **代码仓库：** [GitHub - Do-Transformers-Need-3-Projections](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections)