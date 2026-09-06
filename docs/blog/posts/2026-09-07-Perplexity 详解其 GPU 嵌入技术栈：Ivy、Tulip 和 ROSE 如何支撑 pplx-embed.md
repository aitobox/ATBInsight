---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-09-07
hide:
- navigation
tags:
- Perplexity
- GPU推理
- 嵌入模型
- CUDA优化
- 系统架构
title: Perplexity 详解其 GPU 嵌入技术栈：Ivy、Tulip 和 ROSE 如何支撑 pplx-embed
---
### 文章背景与核心概要
本文详细介绍了 Perplexity 旗下支撑 **pplx-embed**（为其搜索、Computer 及 API 平台提供支持的顶尖嵌入与排序模型）的底层基础设施。与构建独立系统不同，Perplexity 直接复用了其大语言模型 (LLM) 技术栈中的预填充 (prefill) 和解码 (decode) 内核。该服务架构主要由三大核心组件构成：**Ivy**（用于 CPU 端处理的 Rust HTTP 网关）、**Tulip**（Rust gRPC 服务接口）以及用于模型执行的 **ROSE**（运行时优化服务引擎，Runtime-Optimized Serving Engine）。

通过充分利用全模型 CUDA 图（whole-model CUDA graphs）、惰性张量评估（lazy tensor evaluation）以及简单的先来先服务（FCFS）调度器，Perplexity 在避免传统 GPU 推理带来的沉重开销的同时，实现了极高的吞吐量和极低的向量搜索延迟。对于关注高性能 AI 推理基础设施、向量数据库检索优化以及大模型工程落地的技术人员而言，这一架构设计具有极高的参考价值。

---

# Perplexity 详解其 GPU 嵌入技术栈：Ivy、Tulip 和 ROSE 如何支撑 pplx-embed

> ## Summary
> Perplexity recently detailed the infrastructure behind **pplx-embed**—the state-of-the-art embedding and ranking models powering Perplexity Search, Computer, and its API Platform. Rather than building a separate system, Perplexity reuses the prefill and decode kernels from its Large Language Model (LLM) stack. The serving architecture relies on three core components: **Ivy** (a Rust HTTP gateway for CPU-side processing), **Tulip** (a Rust gRPC serving interface), and **ROSE** (Runtime-Optimized Serving Engine) for model execution. By leveraging whole-model CUDA graphs, lazy tensor evaluation, and a simple first-come-first-served scheduler, Perplexity achieves high throughput and low-latency vector search without the heavy overhead typically associated with GPU inference.

---

## 两种流量模式，一套统一引擎
AI 搜索产品的检索质量取决于两个关键因素：嵌入模型的质量，以及在整个索引上运行该模型的成本效益。Perplexity 将嵌入服务（embedding serving）划分为两大主要工作负载：
* **批量嵌入（Batch Embedding）：** 用于构建或重新索引向量数据库，此时最大化吞吐量是降低成本的关键。
* **在线嵌入（Online Embedding）：** 用于查询时（query time），要求对短文本查询进行即时嵌入。

评分（Scoring）则介于两者之间，在初始向量搜索完成后，平衡吞吐量和延迟。

与其维护一个独立的引擎，Perplexity 选择直接复用其 LLM 技术栈。由于嵌入模型本质上是小型 Transformer，批量嵌入类似于计算密集型的预填充（prefill），而在线嵌入（通常仅包含几个 Token）则类似于内存密集型的解码（decode）。

> ## Two Traffic Patterns, One Engine
> Retrieval quality in an AI search product depends on two factors: the quality of the embedding model and the cost-efficiency of running it across an index. Perplexity divides embedding serving into two main workloads:
> * **Batch Embedding:** Used when building or re-indexing vector databases, where maximizing throughput minimizes cost.
> * **Online Embedding:** Used at query time, requiring short queries to be embedded instantly.
> 
> Scoring sits in between these two, balancing both throughput and latency after the initial vector search. 
> 
> Rather than maintaining a separate engine, Perplexity leverages its LLM stack. Because embedding models are small Transformers, batch embedding resembles compute-bound prefill, while online embedding (often just a few tokens) resembles memory-bound decode.

---

## Ivy、Tulip 与 ROSE：请求生命周期
三个专用服务共同处理传入的请求：

1. **Ivy（Rust HTTP 网关）：** 负责 CPU 端的各项操作，包括 JSON 解析、分词（使用自研的 unigram 分词器）、输入模板化以及批次拆分。它将请求转换为自定义的 gRPC 协议，并跨副本对数据块进行负载均衡，以应对生产环境中多变的数据包大小。
2. **Tulip（推理服务器接口）：** 一个基于 Rust、`tokio` 和 `tonic` 构建的 gRPC 服务器。它在将工作负载分发给引擎之前，负责处理请求的调度和批处理（batching）。
3. **ROSE（运行时优化服务引擎）：** 负责管理模型推理。ROSE 主要用 Python 编写，提供自定义内核、层和模型定义，监督 CUDA 图，并向 Tulip 暴露出一个 `step()` 函数。值得注意的是，ROSE 在提供嵌入服务时并不分配 KV 缓存。

> ## Ivy, Tulip, and ROSE: The Request Lifecycle
> Three dedicated services handle incoming requests:
> 
> 1. **Ivy (Rust HTTP Gateway):** Handles CPU-side operations including JSON parsing, tokenization (using an in-house unigram tokenizer), input templating, and batch splitting. It translates requests into a custom gRPC protocol and load-balances chunks across replicas to compensate for varying production payload sizes.
> 2. **Tulip (Inference Server Interface):** A gRPC server built with Rust, `tokio`, and `tonic`. It handles request scheduling and batching before dispatching workloads to the engine.
> 3. **ROSE (Runtime-Optimized Serving Engine):** Manages model inference. Written primarily in Python, ROSE provides custom kernels, layers, and model definitions, oversees CUDA graphs, and exposes a `step()` function to Tulip. Notably, ROSE does not allocate a KV cache when serving embeddings.

---

## 为什么调度器刻意保持简单
随着请求不断涌现，Tulip 采用了一种直截了当的**先来先服务（FCFS）**调度策略。

这种简单性得到了实证数据的支持：对于具有典型序列长度的小型嵌入模型而言，稠密层（dense layers）的线性成本占据了主导地位，而注意力机制（attention）的二次方成本则退居其次。因此，延迟与**Token 数量**成正比，而不是与序列数量成正比。一旦批次填满 GPU（对于参数量在十亿以下的模型，大约为 **512 个 Token**），塞入更多的序列将无法带来进一步的效率提升。

> ## Why the Scheduler is Deliberately Simple
> Tulip uses a straightforward **first-come, first-served (FCFS)** scheduling strategy as requests accumulate. 
> 
> This simplicity is backed by empirical data: for small embedding models at typical sequence lengths, the linear cost of dense layers dominates the quadratic cost of attention. Consequently, latency scales proportionally with **token count rather than sequence count**. Once a batch saturates the GPU—roughly **512 tokens on a sub-billion-parameter model**—packing in additional sequences yields no further efficiency gains.

---

## CUDA 图与 LazyTensors
为了最大化硬件利用率，Perplexity 实现了先进的 GPU 优化技术：

* **全模型 CUDA 图（Whole-Model CUDA Graphs）：** 在处理小批次时，CPU 端的内核启动开销往往会超过实际的 GPU 执行时间。Perplexity 为所有嵌入模型捕获了全模型 CUDA 图，将数千次驱动程序调用精简为单次调用。为了绕过注意力层中动态输入的限制，Perplexity 向 **FlashInfer** 贡献了上游代码修改。
* **惰性捕获（Lazy Capture）：** 由于必须按配置捕获计算图，Token 数量被分桶（bucketed）为 64 或 256 的倍数。为了避免预先捕获数千个图而导致长达数分钟的启动延迟，Perplexity 采用了*惰性捕获*机制——先运行一次急切预热（eager warmup），然后在第二次命中时进行捕获和重放。
* **LazyTensors：** 为了消除同步瓶颈，`LazyTensor` 抽象跟踪一个页面锁定的主机缓冲区（page-locked host buffer），以及异步的 `cudaMemcpyAsync` 和一个 CUDA 事件。它不会在 `step()` 期间阻塞设备，而是返回一个 `LazyTensor`，从而允许 Rust 异步任务在 GPU 计算第 $N$ 个批次的同时，去处理第 $N+1$ 个批次。

> ## CUDA Graphs and LazyTensors
> To maximize hardware utilization, Perplexity implements advanced GPU optimizations:
> 
> * **Whole-Model CUDA Graphs:** On small batches, CPU-side kernel launching overhead can outweigh actual GPU execution time. Perplexity captures whole-model CUDA graphs for all embedding models, reducing thousands of driver calls into a single call. To bypass dynamic input limitations in attention layers, Perplexity contributed upstream changes to **FlashInfer**.
> * **Lazy Capture:** Because graphs must be captured per configuration, token counts are bucketed into multiples of 64 or 256. To avoid minutes of startup latency from pre-capturing thousands of graphs, Perplexity utilizes *lazy capture*—running an eager warmup followed by capture and replay upon the second hit.
> * **LazyTensors:** To eliminate synchronization bottlenecks, the `LazyTensor` abstraction tracks a page-locked host buffer along with an asynchronous `cudaMemcpyAsync` and a CUDA event. Instead of blocking the device during `step()`, it returns a `LazyTensor`, allowing Rust async tasks to process batch $N+1$ while the GPU computes batch $N$.

---

## 内核依然至关重要
ROSE 针对不规则输入（ragged inputs）支持多种注意力后端，包括 FlashInfer 2、FlashInfer 3 以及 FlashAttention 4。

尽管 FlashAttention 4 通常速度更快，但在超长序列长度下，FlashInfer 3 在基于 Qwen 的模型上表现更佳。后端的选择采取具体情况具体分析的策略。通过利用不规则注意力（ragged attention）变体，ROSE 在提供嵌入服务时避免了不必要的填充（padding）。

> ## Kernels Still Matter
> ROSE supports multiple attention backends for ragged inputs, including FlashInfer 2, FlashInfer 3, and FlashAttention 4. 
> 
> While FlashAttention 4 is generally faster, FlashInfer 3 outperforms it on Qwen-based models at very long sequence lengths. Backend selection is handled on a case-by-case basis. By utilizing ragged attention variants, ROSE avoids unnecessary padding when serving embeddings.

---

## 基准测试
Perplexity 使用真实的模型权重和评估派生的输入，在 BF16 精度下将自身的技术栈与 `vLLM` (v0.22.0) 进行了基准对比，确保余弦相似度散度（cosine similarity divergence）保持在 0.1% 以内。测试涵盖了四个套件：
1. **低延迟嵌入（Low-Latency Embeddings）：** 批大小为 1，Token 数分别为 128、512 和 4096。
2. **低延迟评分（Low-Latency Scoring）：** Token 数为 512，批大小分别为 5、25 和 50。
3. **高吞吐量嵌入（High-Throughput Embeddings）：** 跨 4 个并发进程的批大小为 100。
4. **高并发嵌入（High-Concurrency Embeddings）：** 1 到 16 个并发请求（包含 Ivy 分词和网络开销）。

> ## Benchmarks
> Perplexity benchmarked its stack against `vLLM` (v0.22.0) in BF16 using real model weights and evaluation-derived inputs, ensuring cosine similarity divergence remained within 0.1%. Tests covered four suites:
> 1. **Low-Latency Embeddings:** Batch size 1 at 128, 512, and 4096 tokens.
> 2. **Low-Latency Scoring:** Batch sizes 5, 25, and 50 at 512 tokens.
> 3. **High-Throughput Embeddings:** Batch size 100 across four concurrent processes.
> 4. **High-Concurrency Embeddings:** 1 to 16 concurrent requests (including Ivy tokenization and network overhead).

---

## 核心要点
* **统一内核：** Perplexity 的嵌入技术栈直接复用了其现有的 LLM 预填充和解码内核。
* **Token 决定延迟：** 延迟由 Token 数量而非序列数量驱动，大约 512 个 Token 即可使十亿参数以下的模型达到完全饱和。
* **降低开销：** 全模型 CUDA 图与惰性捕获相结合，消除了启动瓶颈，同时没有引入巨大的启动延迟。
* **异步流水线：** `LazyTensor` 实现了 CPU 批次准备与飞行中 GPU 计算之间的无缝重叠。
* **便捷易用：** 尽管 Ivy、Tulip 和 ROSE 属于内部系统，但开发者可以通过 Perplexity 公共的嵌入 API 轻松访问 `pplx-embed`。

> ## Key Takeaways
> * **Unified Kernels:** Perplexity’s embedding stack reuses its existing LLM prefill and decode kernels.
> * **Token-Bound Latency:** Latency is driven by token count rather than sequence count, with ~512 tokens fully saturating sub-1B parameter models.
> * **Overhead Reduction:** Whole-model CUDA graphs combined with lazy capture eliminate launch bottlenecks without introducing massive startup delays.
> * **Asynchronous Pipelines:** `LazyTensor` enables seamless overlap between CPU batch preparation and in-flight GPU computations.
> * **Accessibility:** While Ivy, Tulip, and ROSE are internal systems, `pplx-embed` is readily accessible via Perplexity’s public Embeddings API.

---

*Source: Perplexity Engineering, ["Fast Embeddings on GPUs"](https://www.perplexity.ai/hub/blog/fast-embeddings-on-gpus) (Sep 4, 2026)*