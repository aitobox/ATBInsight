---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-09-22
hide:
  - navigation
tags:
  - Hugging Face
  - Tokenizers
  - Rust
  - SIMD
  - 性能工程
title: "Hugging Face 发布 Tokenizers v1 重构：SIMD 位运算与零内存分配带来 3~30 倍加速"
---

# Hugging Face 发布 Tokenizers v1 重构：SIMD 位运算与零内存分配带来 3~30 倍加速

> # Tokenizers v1: Encode, Decode and Scaling, Measured

**发布时间：** 2026 年 9 月 21 日  
**作者：** Arthur Zucker, Simon Brandeis, Luc Georges, Lysandre  

> **Published:** September 21, 2026  
> **Authors:** Arthur Zucker, Simon Brandeis, Luc Georges, Lysandre  

### 文章背景与核心概要
在大语言模型 (Large Language Model, LLM) 的推理与训练过程中，分词 (Tokenization) 环节以往常被视作微不足道的开销。然而随着模型吞吐量的飞速攀升，原本不起眼的分词流程已逐渐演变成让昂贵 GPU 陷入空闲等待的关键数据瓶颈。为了彻底攻克这一难题，Hugging Face 对其基石级开源库 Tokenizers 进行了底层的全方位架构重构，正式推出即将发布的 Tokenizers v1。该版本在严格保证输出 Token ID 与原有模型完全兼容的前提下，通过引入基于 SIMD 的 Bitcannon 文本切分技术、无堆内存分配的合并循环以及线程级词缓存等前沿工程手段，实现了相比 v0.23 版本 3 到 30 倍的惊人性能飞跃，为高并发服务与海量数据预处理扫清了吞吐障碍。

---

## 概要

> ## Summary

随着机器学习模型运行越来越快、处理的工作负载越来越大，系统的数据瓶颈也在悄然发生转移。分词 (Tokenization) ——这一传统上被视作轻量级的前置步骤，在海量数据集训练、应对高并发请求或处理超长上下文输入时，很容易迅速沦为整条流水线的性能瓶颈，最终导致昂贵的 GPU 算力白白处于闲置等待状态。

> As machine learning models grow faster and handle larger workloads, data bottlenecks shift. Tokenization—traditionally a lightweight step—can quickly become a bottleneck when training on massive datasets, serving concurrent requests, or processing lengthy inputs, ultimately leaving expensive GPUs sitting idle. 

为了解决这一痛点，Hugging Face 团队针对即将发布的 **Tokenizers v1** 展开了极致的性能攻坚。新版本在完全保留输出兼容性、API 接口、词表以及合并优先权重 (Merge Ranks) 的同时，实现了大幅性能跃升 (比 v0.23 版本提速高达 3 至 30 倍) 。版本 1 带来了一场彻底的底层架构重构：

> To solve this, the Hugging Face team has heavily focused on performance for the upcoming **Tokenizers v1**. Built to be significantly faster (up to 3 to 30x faster than v0.23) while preserving output compatibility, APIs, vocabularies, and merge ranks, version 1 introduces a complete architectural refactor:

* **工作空间拆分 (Workspace Split) ：** 将核心运行时 (`tk-encode`) 与模型训练、序列化以及转换工具解耦模块化。
* **Bitcannon：** 用基于单指令多数据流 (SIMD) 驱动的位流运算取代了通用正则表达式引擎来进行文本切分。
* **零内存分配模型与合并循环重写 (No-Alloc Model & Merge-Loop Rewrite) ：** 通过由调用方持有的临时暂存缓冲区 (Scratch Buffers) 与侵入式链表 (Intrusive Linked Lists) ，彻底消除了分词过程中的堆内存分配开销。
* **词缓存 (The Word Cache) ：** 缓存先前已处理过的预分词片段 (Pre-tokens) ，以此加速重复文本段的处理。
* **原生并发 (Native Parallelism) ：** 支持跨多线程共享且线程安全的高并发编码，消除了互斥锁竞争。

> * **Workspace Split:** Modularizes the core runtime (`tk-encode`) from training, serialization, and conversion tools.
> * **Bitcannon:** Replaces general-purpose regex engines with SIMD-powered bitstream operations for text splitting.
> * **No-Alloc Model & Merge-Loop Rewrite:** Eliminates heap allocations during tokenization using caller-owned scratch buffers and intrusive linked lists.
> * **The Word Cache:** Caches previously processed pre-tokens to speed up repeated text segments.
> * **Native Parallelism:** Enables shared, thread-safe encoding without lock contention.

---

## V1 版本究竟是什么

> ## What V1 Is

版本 1 在生成与 v0.23 完全相同的 Token ID 的同时，全面榨干了所有受支持分词器家族 (包括 BPE、WordPiece 和 Unigram) 的性能极限。

> Version 1 produces the exact same token IDs as v0.23 while maximizing performance across all supported tokenizer families (including BPE, WordPiece, and Unigram). 

一条标准的分词处理流水线通常由四个阶段组成：

> A standard tokenization pipeline runs in four stages:

1. **规范化 (Normalization) ：** 对原始文本执行小写转换或应用 Unicode 规范化处理。
2. **预分词 (Pre-tokenization) ：** 将连续文本初步拆分为更小的切片 (“预分词片段/pre-tokens”) 。
3. **核心模型 (Model) ：** 将预分词片段转化为具体的 Token 并将其映射到词表中的 ID (这正是 v1 重点攻克的核心性能瓶颈) 。
4. **后处理 (Post-processing) ：** 添加特定模型所需的特殊 Token (如起始、结束标记等) 。

> 1. **Normalization:** Lowercasing or applying Unicode normalization to raw text.
> 2. **Pre-tokenization:** Splitting text into smaller chunks ("pre-tokens").
> 3. **Model:** Converting pre-tokens into tokens and mapping them to vocabulary IDs (the primary performance bottleneck addressed in v1).
> 4. **Post-processing:** Adding model-specific special tokens.

### 核心架构改进

> ### Key Architectural Improvements

| 改进项 | 功能机制 |
| :--- | :--- |
| **工作空间拆分 (Workspace split) ** | 单一 crate 拆分为工作空间：`tk-encode` 是核心必选运行时，而 `tk-serialize`、`tk-convert` 与 `tk-train` 仅在应用需要时按需链接 |
| **零内存分配模型 (No-alloc model) ** | 合并工作集常驻于调用方自持的暂存缓冲区中，执行循环全程无需调用内存分配器 |
| **Bitcannon** | 将文本切分规则转化为位流上的布尔运算，利用 SIMD 指令直接定位切分边界，而非依靠昂贵的正则引擎 |
| **重写合并循环 (Merge-loop rewrite) ** | 待合并的片段在单块预分配缓冲区内组织为侵入式双向链表，执行合并只需更新两个索引指针，无需移动数据 |
| **词缓存 (Word cache) ** | 建立从预分词字节到最终 ID 的线程本地备忘录，重复出现的单词仅需合并一次 |
| **原生并发 (Native parallelism) ** | 单个共享分词器可同时为多个线程提供编码服务；每个线程从专属子池中获取独立的暂存缓冲区与词缓存，线程之间不再竞争单一互斥锁 ([#2365](https://github.com/huggingface/tokenizers/pull/2365)) |

> | Change | What it does |
> | :--- | :--- |
> | **Workspace split** | One crate became a workspace: `tk-encode` is the required runtime, and `tk-serialize`, `tk-convert` and `tk-train` are linked only when an application needs them |
> | **No-alloc model** | The merge working set lives in a caller-owned scratch buffer; the loop never touches the allocator |
> | **Bitcannon** | The split pattern becomes Boolean operations over bitstreams, using SIMD instructions to find splits instead of a regex engine |
> | **Merge-loop rewrite** | The pieces being merged form an intrusive doubly-linked list inside one preallocated buffer, so a merge updates two indices instead of moving data |
> | **Word cache** | A thread-local memo from pre-token bytes to finished ids, so a repeated word is merged once |
> | **Native parallelism** | One shared tokenizer encodes from many threads at once; each thread draws its scratch buffer and word cache from its own sub-pool, so threads no longer queue on a single lock ([#2365](https://github.com/huggingface/tokenizers/pull/2365)) |

---

### 文本切分：用位流取代正则表达式

> ### The Split: Bitstreams Instead Of A Regex

BPE 模型传统上依赖固定的正则表达式将输入文本切分为预分词片段。不同于以往每次编码都要执行通用正则引擎，`bitcannon` 直接利用 SIMD (单指令多数据流，Single Instruction, Multiple Data) CPU 指令来编译并执行切分规则。通过并行位流处理 (类似于 *Parabix* 和 *simdjson*) ，单个寄存器操作即可并发处理 64 字节的数据，无需逐字符顺序扫描即可瞬间定位切分边界。

> BPE models traditionally use a fixed regular expression to split input text into pre-tokens. Instead of running a general-purpose regex engine on every encode, `bitcannon` compiles the splitting pattern directly using SIMD (Single Instruction, Multiple Data) CPU instructions. By processing 64 bytes per register operation through parallel bitstreams (similar to *Parabix* and *simdjson*), boundaries are found instantly without sequential character scanning.

### 词缓存机制

> ### The Word Cache

在真实世界的文本中，相同的词汇往往会反复高频出现。由于 BPE 算法具有确定性，v1 引入了线程本地缓存 (Thread-Local Cache) ，将预分词片段的字节序列直接映射到对应的 Token ID。这样一来，后续重复出现的相同词汇就能彻底跳过耗时的合并计算。

> Real-world text often contains repeated words. Because BPE is deterministic, v1 introduces a thread-local cache that maps pre-token bytes directly to their token IDs, allowing subsequent occurrences to bypass the merge process entirely.

```bash
tokbench measure prefix-sharing \
  --engine pipeline \
  --engine hf-tokenizers \
  --compare-to pipeline-no-cache \
  --corpus agentic_swe
```

### 重塑合并循环

> ### The Merge Loop

BPE 的核心合并循环迎来了彻底的重构，一举消除了运行时的动态内存分配。v1 不再为每个预分词片段临时构建优先队列并频繁申请内存，而是反复复用调用方持有的暂存缓冲区，将所有符号扁平化存储在通过索引偏移量相连的数组中，并将候选字符对紧凑打包为 64 位数值，从而实现极速且无分支预测惩罚的查表操作。

> The BPE merge loop has been overhauled to eliminate runtime memory allocations. Instead of constructing new priority queues and allocating memory for every pre-token, v1 reuses caller-owned scratch buffers, stores symbols in a flat array linked by index offsets, and packs candidate pairs into 64-bit values for fast, branchless lookups.

---

## 测试方法

> ## Method

为了确保各大引擎之间的基准测试结果真实、可靠且具备严格的可比性，测试过程遵循了以下准则：

> To ensure reliable benchmarks across engines, the following rules were enforced:

| 评估规则 | 制定原因 |
| :--- | :--- |
| **单一计时循环 (One timing loop) ** | 所有引擎均运行完全相同的循环逻辑，严禁针对特定引擎开放专用快速通道 |
| **排除词表加载耗时 (Load excluded) ** | 词表的加载时间单独计算，绝对不计入文本编码阶段 |
| **校验 ID 哈希一致性 (Id-hash verified) ** | 对输出 Token ID 计算 FNV-1a 哈希值，必须与基准结果完全一致 |
| **仅采纳共有测试单元 (Common cells only) ** | 中位数统计仅针对所有引擎都已成功运行并验证通过的测试单元 |
| **每个进程执行完整遍历 (Complete sweep per process) ** | 每次重复测试均启动全新的独立进程，并保留所有测试单元的数据 |
| **物理核心绑定 (Physical-core pinning) ** | 工作线程严格绑定到 8 个独立的物理 CPU 核心上，绝不使用同核的 SMT 超线程 |
| **独立作业运行 (Independent Jobs) ** | 通过独立的计算作业来衡量不同宿主机之间的性能波动差异 |

> | Rule | Why |
> | :--- | :--- |
> | **One timing loop** | Every engine runs the identical loop; no per-engine fast path |
> | **Load excluded** | Vocabulary load is timed separately, never inside encode |
> | **Id-hash verified** | FNV-1a over the output ids must match the baseline exactly |
> | **Common cells only** | Medians are over cells every engine ran and verified |
> | **Complete sweep per process** | Each repeat starts in a new process and retains every cell |
> | **Physical-core pinning** | Workers are pinned to eight distinct physical cores, never sibling SMT threads |
> | **Independent Jobs** | Separate Jobs measure host-to-host variation |

---

## 测试结果与综合成效

> ## Results & What This Adds Up To

在 v1 覆盖的十个模型家族中，在配备 Apple M4 Max 芯片的设备上进行文本编码时，其速度比 v0.23 版本提升了 **3 至 30 倍** (从 `t5-base` 相对温和的加速，到 `gpt2` 上的惊人飞跃) ；在 8 个并发工作线程下，扩展效率达到了线性扩展的 **76%**。

> Across the ten model families covered by v1, text encoding on an Apple M4 Max is **3 to 30 times faster** than v0.23 (ranging from conservative gains on `t5-base` to massive speedups on `gpt2`), scaling at **76% of linear** across eight workers.

---

## 如何获取与安装

> ## Getting It

你可以直接从 `crates.io` 安装该候选发布版本 (Release Candidate) ：

> You can install the release candidate directly from `crates.io`:

```bash
cargo add tokenizers --pre
```

如果你只需要文本编码功能，希望剔除会引入 C++ 依赖项的训练实现模块，可以使用如下命令：

> If you only need encoding capabilities and want to exclude the training implementation (which pulls in C++ dependencies), use:

```bash
cargo add tokenizers --pre --no-default-features --features http
```

### Rust 使用示例

> ### Rust Usage Example

```rust
use tokenizers::tokenizer::{Result, Tokenizer};

fn main() -> Result<()> {
    let tokenizer = Tokenizer::from_pretrained("deepseek-ai/DeepSeek-V4-Flash", None)?;

    let encoding = tokenizer.encode("The tokenizer is no longer the bottleneck.", false)?; 
    println!("{:?}", encoding.get_ids()); 
    // [671, 17840, 9160, 344, 1119, 5827, 270, 111127, 16] 
    println!("{:?}", encoding.get_tokens()); 
    // ["The", "Ġtoken", "izer", "Ġis", "Ġno", "Ġlonger", "Ġthe", "Ġbottleneck", "."]

    Ok(()) 
}
```

针对批量数据处理场景，可以使用 `encode_batch`：

> For batch processing, use `encode_batch`:

```rust
let encodings = tokenizer.encode_batch(documents, false)?;
```

---

## 迈向 V1 的研发演进与路线图

> ## Progress Towards V1

### 候选发布版本：已实现特性 (已在 crates.io 提供) 

> ### Release Candidate: Implemented (Available on crates.io)

* **工作空间拆分 (Workspace split) ：** 拆分为 `tk-encode`、`tk-serialize`、`tk-convert` 和 `tk-train` 四个独立模块。
* **Bitcannon：** 为 GPT-2、cl100k、o200k、Tekken 以及 DeepSeek 引入 SIMD 加速的正则表达式替代实现 ([#2201](https://github.com/huggingface/tokenizers/pull/2201), [#2317](https://github.com/huggingface/tokenizers/pull/2317))。
* **WordCache 词缓存：** 复用已处理预分词片段的 Token ID ([#2262](https://github.com/huggingface/tokenizers/pull/2262))。
* **极速查表与合并：** 实现了 FlatCache、MPHF RankStore、增量合并以及 BucketVocabStore ([#2190](https://github.com/huggingface/tokenizers/pull/2190), [#2188](https://github.com/huggingface/tokenizers/pull/2188))。
* **可复用模型内存：** 利用暂存缓冲区消除了每次调用时的堆内存分配 ([#2175](https://github.com/huggingface/tokenizers/pull/2175), [#2183](https://github.com/huggingface/tokenizers/pull/2183))。
* **流水线后处理：** 作为 `STAGE_POST` 流水线阶段独立暴露 ([#2182](https://github.com/huggingface/tokenizers/pull/2182))。
* **批处理模型调用：** 支持同时并行处理多个预分词跨度区间 ([#2304](https://github.com/huggingface/tokenizers/pull/2304))。
* **更高效的解码：** 直接向可复用缓冲区写入结果，避免生成中间临时字符串拷贝。
* **Node.js 语言绑定** ([#2281](https://github.com/huggingface/tokenizers/pull/2281))。

> * **Workspace split:** Divided into `tk-encode`, `tk-serialize`, `tk-convert`, and `tk-train`.
> * **Bitcannon:** SIMD-accelerated regex replacement for GPT-2, cl100k, o200k, Tekken, and DeepSeek ([#2201](https://github.com/huggingface/tokenizers/pull/2201), [#2317](https://github.com/huggingface/tokenizers/pull/2317)).
> * **WordCache:** Reuses token IDs of previously processed pre-tokens ([#2262](https://github.com/huggingface/tokenizers/pull/2262)).
> * **Faster lookup & merging:** Implemented FlatCache, MPHF RankStore, incremental merging, and BucketVocabStore ([#2190](https://github.com/huggingface/tokenizers/pull/2190), [#2188](https://github.com/huggingface/tokenizers/pull/2188)).
> * **Reusable model memory:** Scratch buffers eliminate per-call heap allocations ([#2175](https://github.com/huggingface/tokenizers/pull/2175), [#2183](https://github.com/huggingface/tokenizers/pull/2183)).
> * **Pipeline post-processing:** Exposed as the `STAGE_POST` pipeline stage ([#2182](https://github.com/huggingface/tokenizers/pull/2182)).
> * **Batched model calls:** Processes multiple pre-token spans simultaneously ([#2304](https://github.com/huggingface/tokenizers/pull/2304)).
> * **Faster decoding:** Direct writes to reusable buffers without intermediate string copies.
> * **Node.js bindings** ([#2281](https://github.com/huggingface/tokenizers/pull/2281)).

### 1.0.0 正式版近期规划

> ### Upcoming for 1.0.0

* 使用 `tk-encode` 统一训练阶段的校验逻辑。
* 支持可选的字符偏移量 (Offsets) 与注意力掩码 (Masks) (仅在显式请求时按需计算) 。
* 规范化器 (Normalizer) 架构重构。
* 提供更精简、支持无全局解释器锁 (free-threaded CPython) 的 Python 绑定。
* 针对 ExecuTorch 与 `llama.cpp` 提供仅支持推理的轻量级 C 与 C++ 绑定。

> * Unifying training validation using `tk-encode`.
> * Optional offsets and masks (computed only when explicitly requested).
> * Normalizer refactoring.
> * Simpler Python bindings supporting free-threaded CPython.
> * Inference-only C and C++ bindings for ExecuTorch and `llama.cpp`.

### 1.0.0 之后的未来展望

> ### After 1.0.0

* **Tok-devices 专用设备加速：** 探索基于 GPU 加速的编码与批量解码技术，让文本与 Token ID 全程驻留在计算设备端。

> * **Tok-devices:** Exploring GPU-accelerated encoding and batch decoding to keep texts and token IDs entirely on-device.
