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
- 大模型推理
- 架构优化
- 混合专家模型
- 键值缓存
title: 双流Transformer：将主预填充路径与额外的解码计算解耦
---
### 文章背景与核心概要
随着大语言模型（LLM）不断扩展以应对高并发请求，累积的推理成本逐渐超过了一次性的训练开销。推理过程面临着一个结构性挑战：**提示词预填充（Prompt Prefill）**是并行且受计算能力限制的（compute-bound），而**自回归解码（Autoregressive Decoding）**则是串行且受内存带宽限制的（memory-bandwidth-bound）。

传统的缩放方法（如扩展宽度或深度）会同时对这两个阶段进行统一扩展，因为在预填充和解码过程中都必须评估模型的每一层。为了克服这一局限性，作者引入了**双流 Transformer（Dual-Flow Transformer）**。该架构引入了一个专门在解码阶段激活的辅助计算流用于续写预测，从而将解码特定的计算与主提示词预填充路径及其持久化的键值（KV）缓存完全解耦。

---

## 双流 Transformer：将主预填充路径与额外的解码计算解耦

**arXiv ID:** [arXiv:2608.12385](https://arxiv.org/abs/2608.12385) [cs.AI]  
**作者:** Liming Liu, Mingze Wang, Tuo Zhao  
**提交时间:** 2026年7月31日  
**许可协议:** [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)  
**全文链接:** [查看 PDF](https://arxiv.org/pdf/2608.12385) | [HTML 版本](https://arxiv.org/html/2608.12385v1) | [TeX 源码](https://arxiv.org/src/2608.12385)

---

## 执行摘要

> As large language models (LLMs) scale to serve high volumes of requests, cumulative inference costs increasingly outweigh one-time training expenses. Inference presents a structural challenge: **prompt prefill** is parallel and compute-bound, whereas **autoregressive decoding** is sequential and memory-bandwidth-bound. 

随着大语言模型（LLM）不断扩展以应对高并发请求，累积的推理成本逐渐超过了一次性的训练开销。推理过程面临着一个结构性挑战：**提示词预填充（prompt prefill）**是并行且受计算能力限制的，而**自回归解码（autoregressive decoding）**则是串行且受内存带宽限制的。

> Traditional scaling methods (such as expanding width or depth) scale both phases uniformly because every model layer must be evaluated during both prefill and decode. To overcome this limitation, the authors introduce the **Dual-Flow Transformer**. This architecture introduces an auxiliary computational flow activated exclusively during the decode phase for continuation prediction, completely decoupling decode-specific computation from the primary prompt prefill path and its persistent Key-Value (KV) cache.

传统的缩放方法（如扩展宽度或深度）会同时对这两个阶段进行统一扩展，因为在预填充和解码过程中都必须评估模型的每一层。为了克服这一局限性，作者引入了**双流 Transformer（Dual-Flow Transformer）**。该架构引入了一个专门在解码阶段激活的辅助计算流用于续写预测，从而将解码特定的计算与主提示词预填充路径及其持久化的键值（KV）缓存完全解耦。

---

## 核心架构概念

### 1. 双流结构
> * **Primary Flow:** A complete causal language model responsible for processing the prompt and generating the persistent Key-Value (KV) cache.
> * **Auxiliary Flow:** Omitted entirely during initial prompt processing and activated only from the final prompt position onward. It introduces additional continuation-prediction computation without writing persistent state or altering the primary flow.

* **主流（Primary Flow）：** 一个完整的因果语言模型，负责处理提示词并生成持久化的键值（KV）缓存。
* **辅助流（Auxiliary Flow）：** 在初始提示词处理阶段完全被省略，仅从最后一个提示词位置开始激活。它引入了额外的续写预测计算，但不会写入持久化状态，也不会改变主流。

### 2. 权重共享与耦合
> * Both flows share major attention layers, Multi-Layer Perceptrons (MLPs), and output matrices.
> * They utilize separate token embeddings combined with lightweight coupling mechanisms.
> * Sharing model weights and the primary KV cache enables optimization opportunities, such as reusing loaded weights and cached keys/values during grouped execution.

* 两个流共享主要的注意力层、多层感知机（MLPs）和输出矩阵。
* 它们使用独立的词元嵌入（Token Embeddings），并结合了轻量级的耦合机制。
* 共享模型权重和主 KV 缓存带来了优化机会，例如在分组执行期间重用已加载的权重和缓存的键/值。

### 3. 混合专家（MoE）集成
> * In MoE configurations, separating the primary and auxiliary expert fan-outs allows independent control over:
>   * Prompt compute costs
>   * Continuation compute costs
>   * Overall predictive quality

* 在 MoE 配置中，分离主流和辅助专家的扇出（fan-outs），可以独立控制：
  * 提示词计算成本
  * 续写计算成本
  * 整体预测质量

---

## 实验见解

> * **Validation Performance:** Across matched-token comparisons, the Dual-Flow architecture achieves lower validation loss across various model architectures and data configurations.
> * **Trade-Off Analysis:** The authors evaluated two distinct regimes:
>   1. Increasing decode computation while keeping prefill expert computation fixed.
>   2. Reallocating a fixed budget of decode experts between the two flows.
> * These experiments highlight a clear prefill-decode-quality trade-off, demonstrating the practical viability and efficiency of phase-specific expert allocation in modern LLM deployments.

* **验证性能：** 在匹配词元的对比中，双流架构在各种模型架构和数据配置下都实现了更低的验证损失。
* **权衡分析：** 作者评估了两种不同的机制：
  1. 在保持预填充专家计算量不变的同时，增加解码计算量。
  2. 在两个流之间重新分配固定预算的解码专家。
* 这些实验凸显了清晰的“预填充-解码-质量”权衡关系，证明了在现代 LLM 部署中针对特定阶段进行专家分配的实际可行性与效率。

---

> *For more details, bibliographic tools, or related code repositories, refer to the official [arXiv abstract page](https://arxiv.org/abs/2608.12385).*

*有关更多详细信息、文献计量工具或相关代码仓库，请参考官方 [arXiv 摘要页面](https://arxiv.org/abs/2608.12385)。*

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>