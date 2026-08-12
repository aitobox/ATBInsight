---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- 大语言模型
- 注意力机制
- 分布式推理
- 长文本处理
- 键值缓存
title: 抛弃锚点：通过 Pulsar Attention 实现分布式系统的统计上下文摘要
---
### 文章背景与核心概要
在处理长序列时，大语言模型（LLM）的自注意力机制由于其二次方的计算复杂度，导致推理成本极高。传统的分布式分块方法（如 Star Attention）通过将上下文分片到不同主机来降低成本，但它们依赖于在每个主机的前端预置一个静态的、与内容无关的第一块拷贝（即锚点），这往往会损害模型的性能或效率。

为了解决这一痛点，本文引入了一种名为 **Pulsar Attention** 的新型内容感知分布式分块方法。它抛弃了传统的静态锚点，转而采用两个轻量级的内容感知组件：一个是用于稳定 softmax 的小型注意力沉淀前缀（attention-sink prefix），另一个是通过基于 Max-IDF 启发式算法构建的紧凑跨块摘要（选择包含全局稀有标记的块）。

在实验部分，通过在 Llama-3.1-8B-Instruct 模型上对 RULER 基准测试进行评估，结果表明：Pulsar Attention 在高达 128K 长度的序列上表现超越了 Star Attention，同时在大多数任务中保持了与稠密注意力基线（dense attention baselines）相竞争的性能，在特定任务上实现了高达 4.7% 的绝对性能提升，并将第一阶段（Phase 1）的单 GPU 浮点运算量（FLOPs）降低了最多 3.3 倍，且 KV 缓存占用保持不变。

---

## Summary

This paper introduces **Pulsar Attention**, a novel, content-aware distributed blockwise method designed to optimize Large Language Model (LLM) inference on long sequences. By replacing the static, content-blind anchor blocks used in traditional methods like Star Attention with a lightweight attention-sink prefix and Max-IDF-based cross-block summaries, Pulsar Attention reduces Phase 1 per-GPU FLOPs by up to 3.3× while maintaining an identical KV cache footprint. Evaluations on the RULER benchmark using Llama-3.1-8B-Instruct demonstrate that Pulsar Attention outperforms Star Attention across sequence lengths up to 128K tokens and remains competitive with dense attention baselines, achieving task-dependent absolute gains of up to 4.7%.

> 本文介绍了 **Pulsar Attention**，这是一种新颖的、具备内容感知能力的分布式分块方法，旨在优化大语言模型（LLM）在长序列上的推理。通过用轻量级的注意力沉淀前缀（attention-sink prefix）和基于 Max-IDF 的跨块摘要，替代了传统方法（如 Star Attention）中使用的静态且与内容无关的锚块，Pulsar Attention 将第一阶段的单 GPU 浮点运算量（FLOPs）降低了最多 3.3 倍，同时保持了相同的 KV 缓存占用。在使用 Llama-3.1-8B-Instruct 的 RULER 基准测试评估中表明，Pulsar Attention 在高达 128K 标记的序列长度上表现优于 Star Attention，并与稠密注意力基线保持竞争力，实现了高达 4.7% 的任务相关绝对增益。

---

## Document Metadata

| Field | Details |
| :--- | :--- |
| **Title** | Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention |
| **Authors** | Aryan Sood, Shantanu Acharya, Gaurav Kumar Nayak |
| **Primary Subject** | Computation and Language (`cs.CL`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **arXiv ID** | [`arXiv:2607.20457`](https://arxiv.org/abs/2607.20457) [cs.CL] |
| **DOI** | [10.48550/arXiv.2607.20457](https://doi.org/10.48550/arXiv.2607.20457) |
| **Submission History** | **[v1]** Thu, 14 May 2026<br>**[v2]** Fri, 7 Aug 2026 (This version) |

> ## 文档元数据
> 
| 字段 | 详情 |
| :--- | :--- |
| **标题** | Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention |
| **作者** | Aryan Sood, Shantanu Acharya, Gaurav Kumar Nayak |
| **主要学科** | 计算与语言 (`cs.CL`) |
| **次要学科** | 人工智能 (`cs.AI`) |
| **arXiv ID** | [`arXiv:2607.20457`](https://arxiv.org/abs/2607.20457) [cs.CL] |
| **DOI** | [10.48550/arXiv.2607.20457](https://doi.org/10.48550/arXiv.2607.20457) |
| **提交历史** | **[v1]** 2026年5月14日 (星期四)<br>**[v2]** 2026年8月7日 (星期五) (当前版本) |

---

## Abstract

Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention. Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host. 

We propose **Pulsar Attention**, which replaces the static anchor with two lightweight, content-aware components: 
1. A small attention-sink prefix that stabilizes softmax.
2. Compact cross-block summaries built via a Max-IDF heuristic that selects chunks containing globally rare tokens. 

This reduces the Phase 1 per-GPU FLOPs by up to **3.3×** over Star Attention while retaining an identical KV cache footprint. On RULER with Llama-3.1-8B-Instruct, Pulsar Attention outperforms Star Attention at sequence lengths up to 128K tokens and remains competitive with dense attention across most tasks, with task-dependent absolute gains of up to **4.7%** over the dense baseline.

> ## 摘要
> 
> 由于自注意力机制具有二次方的复杂度，大语言模型（LLM）在长序列上的推理计算开销非常大。诸如 Star Attention 等分布式分块方法通过在主机之间对上下文进行分片来降低这种成本，但它们依赖于在每个主机前预置第一块的静态、与内容无关的拷贝。
> 
> 我们提出了 **Pulsar Attention**，它用两个轻量级的内容感知组件替代了静态锚点：
> 1. 一个用于稳定 softmax 的小型注意力沉淀前缀（attention-sink prefix）。
> 2. 通过 Max-IDF 启发式算法构建的紧凑跨块摘要，该算法选择包含全局稀有标记的块。
> 
> 与 Star Attention 相比，这在保持相同 KV 缓存占用的同时，将第一阶段的单 GPU 浮点运算量（FLOPs）降低了最多 **3.3 倍**。在搭载 Llama-3.1-8B-Instruct 的 RULER 测试中，Pulsar Attention 在高达 128K 标记的序列长度上表现优于 Star Attention，并在大多数任务中与稠密注意力保持竞争力，相比稠密基线实现了高达 **4.7%** 的任务相关绝对增益。

---

## Full-Text & External Resources

* **PDF Version:** [View PDF](https://arxiv.org/pdf/2607.20457)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2607.20457v2)
* **TeX Source:** [Download Source](https://arxiv.org/src/2607.20457)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

### External Citations & Tools
* **Academic Databases:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.20457) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.20457) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2607.20457)
* **Code & Exploration Finders:** [CatalyzeX Code Finder](https://www.catalyzex.com) | [Hugging Face](https://huggingface.co/) | [alphaXiv](https://alphaxiv.org/)

> ## 全文与外部资源
> 
> * **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2607.20457)
> * **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2607.20457v2)
> * **TeX 源码：** [下载源码](https://arxiv.org/src/2607.20457)
> * **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> 
> ### 外部引用与工具
> * **学术数据库：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.20457) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.20457) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2607.20457)
> * **代码与探索工具：** [CatalyzeX Code Finder](https://www.catalyzex.com) | [Hugging Face](https://huggingface.co/) | [alphaXiv](https://alphaxiv.org/)