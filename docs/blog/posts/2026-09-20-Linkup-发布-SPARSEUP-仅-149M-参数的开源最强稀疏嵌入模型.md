---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-09-20
hide:
  - navigation
tags:
  - SPARSEUP
  - 稀疏嵌入
  - 向量检索
  - ModernBERT
  - 开源模型
title: "Linkup 发布 SPARSEUP：仅 149M 参数的开源最强稀疏嵌入模型"
---

# Linkup 发布 SPARSEUP：仅 149M 参数的开源最强稀疏嵌入模型

> # Linkup Research Releases SPARSEUP: A 149M-Parameter Open-Source Sparse Embedding Model

### 文章背景与核心概要
在信息检索与检索增强生成 (RAG) 领域，稠密向量模型虽然应用广泛，但在生僻专有名词匹配和可解释性上存在天然局限，而传统的稀疏模型又往往面临词表膨胀和高计算开销的挑战。为此，Linkup Research 正式发布了开源稀疏嵌入模型 (Sparse Embedding Model) —— **SPARSEUP**。该模型基于 149M 参数的 ModernBERT 架构打造，采用 Apache 2.0 许可证完全开源，在 BEIR-13 基准测试中斩获 56.4 的平均 nDCG@10 得分，成为目前 150M 参数以下公开可用的最强词表稀疏编码器。通过 Logit 平移、单位置 Top-k 截断和大小写折叠等三项精巧架构优化，SPARSEUP 巧妙破解了传统 SPLADE 模型停用词泛滥的难题，并结合 Seismic 倒排索引实现了约 380 微秒的单线程极速检索。这一成果不仅补齐了现代信息检索中轻量级稀疏范式的技术拼图，更为开发者构建高效率、强可解释性的混合检索系统提供了全新利器。

---

## 核心概述

> ## Executive Summary

Linkup Research 正式开源了基于机器学习的稀疏嵌入模型 (Sparse Embedding Model) —— **SPARSEUP**。该模型基于 149M 参数的 ModernBERT 骨干网络构建，并以宽松的 Apache 2.0 许可证公开发布。SPARSEUP 在知名的 BEIR-13 基准测试 (Benchmark) 中取得了 56.4 的平均 nDCG@10 得分，被 Linkup 定位为当前 150M 参数量级以下公开可用的最强基于词表的稀疏编码器。开发者可以通过 Hugging Face，借助 Transformers 或 Sentence Transformers 库轻松部署 SPARSEUP。该模型恰好补齐了此前 LightOn 模型套件的技术拼图，在保持极高检索效率与人类直观可读权重的特性的同时，为稠密检索 (Dense Retrieval) 和晚期交互检索 (Late-Interaction Retrieval) 提供了极具竞争力的稀疏检索替代方案。

> Linkup Research has released **SPARSEUP**, an open-source learned sparse embedding model built on a 149M-parameter ModernBERT backbone and distributed under the Apache 2.0 license. Achieving a 56.4 average nDCG@10 on BEIR-13, Linkup positions SPARSEUP as the strongest public vocabulary-based sparse encoder under 150M parameters. Deployable via Hugging Face using Transformers or Sentence Transformers, SPARSEUP bridges the gap in LightOn's recent model suite, offering a viable sparse alternative to dense and late-interaction retrieval styles while maintaining high efficiency and human-readable weights.

---

## 为什么需要稀疏模型？为什么是现在？

> ## Why a Sparse Model, and Why Now?

目前绝大多数开源检索模型都依赖于稠密表征 (Dense Representations)，即为每段文本生成一个固定维度的稠密向量。与此不同的是，稀疏模型直接在预定义的整个词表上输出权重分布，其中的每一个维度都精确对应一个真实的 Token。这种设计的精妙之处在于，生成的稀疏向量能够无缝对接到传统的倒排索引 (Inverted Indexes) 搜索引擎中；同时，由于每个激活维度都对应具体词汇，权重具备天然的人类可读性，并且在命中冷门、罕见的生僻词与专有名词时表现尤为强悍。

> Most open retrieval models rely on dense representations (one vector per text). In contrast, sparse models output weights over a vocabulary, where each dimension maps to a real token. This design allows vectors to integrate smoothly into inverted indexes while remaining human-readable and highly effective at matching rare words.

SPARSEUP 的研发直接受到了 LightOn 近期发布 [DenseOn and LateOn](https://huggingface.co/papers/2607.27178) 的启发。LightOn 当时开源了全套训练数据、训练秘方 (Recipe)、一个稠密模型以及一个晚期交互模型。而 SPARSEUP 采用相同的骨干网络家族与微调 (Fine-Tuning) 数据，恰好补全了缺失的“稀疏模型”版块，从而让开发者能够站在完全平等的基准线上，横向对比这三种主流的信息检索范式。

> The development of SPARSEUP was motivated by LightOn’s release of [DenseOn and LateOn](https://huggingface.co/papers/2607.27178), which provided open data, a training recipe, a dense model, and a late-interaction model. SPARSEUP fills the missing sparse slot by utilizing the same backbone family and fine-tuning data, allowing developers to compare all three retrieval paradigms side by side.

---

## SPARSEUP 是如何构建的

> ## How SPARSEUP is Built

SPARSEUP 的训练起点是 [LateOn-unsupervised](https://huggingface.co/lightonai/LateOn-unsupervised) 检查点，但该检查点并未包含掩码语言模型 (Masked Language Modeling, MLM) 头。Linkup 团队将 ModernBERT 原生的 MLM 预测头重新“嫁接”回模型中，并纯粹采用对比学习 (Contrastive Learning) 方法，基于 [LightOn 的微调混合数据集 (LightOn’s fine-tuning mixture)](https://huggingface.co/datasets/lightonai/embeddings-fine-tuning) 展开微调。

> Training begins from the [LateOn-unsupervised](https://huggingface.co/lightonai/LateOn-unsupervised) checkpoint, which lacked an MLM head. The Linkup team grafted ModernBERT’s original MLM head back onto the model and performed fine-tuning using [LightOn’s fine-tuning mixture](https://huggingface.co/datasets/lightonai/embeddings-fine-tuning) with contrastive learning exclusively.

* **训练策略：** 每个查询 (Query) 都从 50 个候选池中采样配对 7 个难负例 (Hard Negatives)，同时结合批次内负例 (In-batch Negatives) 共同训练。整个训练流程摒弃了复杂的交叉编码器蒸馏 (Cross-Encoder Distillation)，单张 H100 GPU 即可高效完成训练。
* **突破原生 SPLADE 的局限：** 若在该骨干网络上直接应用标准的 SPLADE 方案，会导致输出表征过于稠密，充斥着大量无意义的停用词 (Stopwords)。Linkup 通过三项核心架构调整完美化解了这一难题：
  1. **Logit 平移 (Logit shifting)：** 编码器通过计算 `log(1 + ReLU(x - 15))`，巧妙抵消了 ModernBERT MLM 原始 Logit 在初始化阶段过大从而导致对数函数饱和的问题。
  2. **逐位置 Top-k 截断 (Per-position top-k)：** 每个输入的 Token 在进入最大池化 (Max Pooling) 之前，仅保留权重最高的前 12 个词表维度。这种设计限制了每个 Token 的词汇扩展幅度，而非死板地限制最终向量的总长度。
  3. **大小写折叠 (Case folding)：** 将字节级 BPE (Byte-level BPE) 中形如 `heat`、`Heat`、`Ġheat` 和 `ĠHeat` 等同义变体统一折叠归并到单一 ID 下，并保留其中的最大权重，从而将词表输出维度从约 50k 显著压缩至约 34k。

> * **Training Strategy:** Each query is paired with 7 hard negatives sampled from a pool of 50, alongside in-batch negatives. The process excludes cross-encoder distillation and fits efficiently on a single H100 GPU.
> * **Overcoming Vanilla SPLADE Limitations:** A standard SPLADE implementation on this backbone resulted in overly dense token bags saturated with stopwords. Linkup resolved this with three core architectural adjustments:
>   1. **Logit shifting:** The encoder computes `log(1 + ReLU(x - 15))` to counteract ModernBERT MLM logits that otherwise saturate the log function at initialization.
>   2. **Per-position top-k:** Each input token retains only its 12 strongest vocabulary dimensions prior to max pooling, capping expansion per token rather than total vector size.
>   3. **Case folding:** Byte-level BPE variants like `heat`, `Heat`, `Ġheat`, and `ĠHeat` are folded onto a single ID while preserving the largest weight, reducing output dimensions from ~50k to ~34k.

在输入格式上，查询和文档分别添加 `[Q]` 与 `[D]` 前缀作为标识，检索得分通过点积 (Dot Product) 计算。在评估基准中，查询的最大长度设为 128 个 Token，文档的最大长度设为 512 个 Token。

> Queries and documents use `[Q]` and `[D]` prefixes respectively, scored via dot product. Evaluation max lengths are set to 128 tokens for queries and 512 for documents.

---

## 基准测试结果

> ## Benchmark Results

根据官方 [模型卡片 (Model Card)](https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v1) 披露的数据，在 BEIR-13 基准测试 (采用 nDCG@10 指标，且不包含 MS MARCO) 中，SPARSEUP 与其他主流稀疏编码器的对比表现如下：

> Evaluated against other sparse encoders on BEIR-13 (nDCG@10, excluding MS MARCO) per the [model card](https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v1):

| 模型 | BEIR-13 平均得分 |
| :--- | :--- |
| **SPARSEUP** | **56.4** |
| [opensearch-neural-sparse-encoding-doc-v3-gte](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte) | 54.6 |
| opensearch-neural-sparse-encoding-v1 | 52.44 |
| ModernBERT-VT | 52.4 |
| splade-v3 | 51.7 |
| [granite-embedding-30m-sparse](https://huggingface.co/ibm-granite/granite-embedding-30m-sparse) | 50.6 |
| LACONIC-1B *(10 亿参数，属于不同规模量级)* | 58.7 |

> | Model | BEIR-13 avg |
> | :--- | :--- |
> | **SPARSEUP** | **56.4** |
> | [opensearch-neural-sparse-encoding-doc-v3-gte](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte) | 54.6 |
> | opensearch-neural-sparse-encoding-v1 | 52.44 |
> | ModernBERT-VT | 52.4 |
> | splade-v3 | 51.7 |
> | [granite-embedding-30m-sparse](https://huggingface.co/ibm-granite/granite-embedding-30m-sparse) | 50.6 |
> | LACONIC-1B *(1B parameters, different size class)* | 58.7 |

### 受控对比与局限性

> ### Controlled Comparisons & Limitations

在严格控制变量 (保持骨干网络与训练数据完全相同) 的前提下，LateOn 的得分为 58.9，DenseOn 为 57.9，而 SPARSEUP 则斩获了 56.4。值得一提的是，SPARSEUP 评测时采用的是基于 Seismic 的近似检索 (而 LightOn 采用的是精确检索) 。在多跳推理数据集 HotpotQA 以及 ArguAna 和 Touché 上，SPARSEUP 的表现均超越了 DenseOn；但在 FiQA 和 DBPedia 等重度依赖语义泛化的任务上则略有落后。而在经过数据去污染 (Decontamination) 处理的 BEIR 基准上，SPARSEUP 与 DenseOn 之间的性能差距更是进一步缩小到了微弱的 0.17 分。

> When holding backbone and data constant, LateOn scores 58.9, DenseOn scores 57.9, and SPARSEUP scores 56.4. While SPARSEUP uses approximate Seismic search (compared to LightOn's exact search) and outperforms DenseOn on HotpotQA (as well as winning on ArguAna and Touché), it lags behind on semantic sets like FiQA and DBPedia. On decontaminated BEIR, the performance gap to DenseOn narrows to just 0.17 points.

---

## 速度与稀疏度

> ## Speed and Sparsity

在经典的 MS MARCO 数据集上，SPARSEUP 生成的表征中，每个查询平均包含 47 个非零词项，每个文档平均包含 190 个非零词项 (相比之下，SPLADE-v3 分别为 25 和 170) 。依托专门优化的 Seismic 倒排索引，SPARSEUP 在单线程执行环境下，仅需约 380 微秒 (µs) 即可完成单次查询检索，并取得了相对于精确检索 97% 以上的超高召回率 (Recall) 。

> On MS MARCO, SPARSEUP averages 47 non-zero terms per query and 190 per document (compared to SPLADE-v3's 25 and 170). Leveraging the Seismic inverted index, it achieves over 97% recall against exact search in approximately 380 microseconds per query in a single-threaded execution.

---

## 核心要点速览

> ## Key Takeaways

* **全面开源可用：** 拥有 149M 参数的稀疏编码器，以宽松的 Apache 2.0 许可证正式发布。
* **顶尖检索性能：** 在 BEIR-13 基准测试中取得 56.4 的 nDCG@10 评分，领跑 150M 参数以下的所有公开稀疏编码器。
* **针对性架构创新：** 凭借 15 的 Logit 平移、单 Token 仅 Top-12 扩展以及大小写折叠技术，坚固维持了高稀疏度。
* **极具竞争优势：** 在相同数据与骨干网络条件下，BEIR-13 评分仅落后 DenseOn 1.52 分，落后 LateOn 2.5 分。
* **超高运行效率：** 在 MS MARCO 上搭配 Seismic 倒排索引，单次查询延迟仅约 380 微秒，召回率高达 97% 以上。

> * **Open-Source Availability:** A 149M-parameter sparse encoder released under the Apache 2.0 license.
> * **Top-Tier Performance:** Scores 56.4 nDCG@10 on BEIR-13, leading public sparse encoders under 150M parameters.
> * **Targeted Architectural Fixes:** Relies on a logit shift of 15, top-12 expansion per token, and case folding to maintain sparsity.
> * **Competitive Edge:** Trails DenseOn by 1.52 points and LateOn by 2.5 points on BEIR-13 under identical data conditions.
> * **High Efficiency:** Delivers over 97% recall at ~380µs per query using Seismic on MS MARCO.

---

## 相关资源与链接

> ## Resources & Links

* [Hugging Face 上的模型权重 (Model Weights)](https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v1)
* [技术细节与官方博文 (Technical Details & Blog Post)](https://www.linkup.so/blog/introducing-sparseup-by-linkup)

> * [Model Weights on Hugging Face](https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v1)
> * [Technical Details & Blog Post](https://www.linkup.so/blog/introducing-sparseup-by-linkup)
