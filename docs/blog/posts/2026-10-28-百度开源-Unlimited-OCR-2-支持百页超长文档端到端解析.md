---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-10-28
hide:
- navigation
tags:
- 百度
- Unlimited OCR 2
- 多模态
- 长文档解析
- 开源模型
title: 百度开源 Unlimited OCR 2：支持百页超长文档端到端解析
---
# 百度开源 Unlimited OCR 2：支持百页超长文档端到端解析

> # Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing

### 文章背景与核心概要

在海量非结构化数据处理与智能文档分析领域，传统光学字符识别 (Optical Character Recognition, OCR) 模型受制于注意力计算复杂度的二次方爆炸与显存限制，往往难以单次吞吐数十乃至上百页的长篇文档，普遍需要依赖机械的单页切分与拼接，极易割裂跨页上下文并丢失全局排版信息。2026 年 10 月，Baidu 正式开源了参数量为 3.34B 的全新多模态端到端超长文档解析模型 Unlimited OCR 2。该模型创新性地引入了稀疏参考滑动窗口注意力机制 (Sparse Reference Sliding Window Attention, SR-SWA)，将每步解码的计算与显存开销压缩为近乎恒定的常数，真正实现了在单个推理请求中对书籍、财报等数百页文档的整体结构化解析。在多页文档基准测试 MarathonDocBench 上，Unlimited OCR 2 取得了 77.1 的顶尖成绩，大幅领先业界同类模型，且采用高度宽松的 MIT 开源协议，为长文本视觉多模态技术的工程落地树立了全新标杆。

---

## 核心概述

> ## Summary

Baidu 正式开源了 **Unlimited OCR 2**，这是一款参数规模为 3.34B 的视觉语言模型 (Vision-Language Model, VLM)，专为在单次请求中端到端解析超长文档（如长篇书籍、企业财务报告以及长达数百页的技术文档）而量身打造。该模型创新性地引入了名为 **SR-SWA (稀疏参考滑动窗口注意力机制，Sparse Reference Sliding Window Attention)** 的稀疏注意力算法，使得随着文档页数增加，模型单步自回归解码的显存与计算开销能够保持近乎平直的常数水平。Unlimited OCR 2 基于极具开放性的 MIT 商业友好协议发布，在 MPDocBench 和 MarathonDocBench 等主流多页文档权威评测基准上均刷新了最佳纪录 (SOTA)。

> Baidu has released **Unlimited OCR 2**, an open-source 3.34B vision-language model designed specifically to parse extremely long documents—such as books, financial filings, and multi-hundred-page reports—in a single request. Featuring a novel sparse attention mechanism known as **SR-SWA (Sparse Reference Sliding Window Attention)**, the model keeps per-step decoding costs nearly flat as document length scales. Available under the MIT license, Unlimited OCR 2 achieves state-of-the-art results on multi-page benchmarks like MPDocBench and MarathonDocBench.

---

## 核心速览 (TL;DR)

> ## TL;DR

* **模型规模**：总参数量为 3.34B（激活参数量未公开）。最大位置编码长度达到 131,072 Token。
* **硬件要求**：支持单张 CUDA GPU 以 BF16 精度全量加载运行（Baidu 官方在单张 NVIDIA A800-80GB 上完成测试），BF16 权重文件总计约 6.7 GB。
* **综合性能**：在与 9 款主流模型的横向对比中，在多页基准测试中拔得头筹（官方自测数据）。
* **亮眼优势**：在包含数百页超长文档的基准测试 MarathonDocBench 上斩获 **77.1** 的综合高分，大幅超越位列第二的 Kimi-K3 (33.7 分)。
* **尚存短板**：在 MarathonDocBench 的标题层级结构树状编辑距离 (TEDS) 评测中得分为 **48.2**，是其各项评测中的最低细项得分。

> * **Size:** 3.34B parameters (active parameters not disclosed). Maximum position length of 131,072 tokens.
> * **Hardware Requirements:** Runs on a single CUDA GPU in BF16 (tested by Baidu on an NVIDIA A800-80GB). BF16 weights total roughly 6.7 GB.
> * **Performance:** Claims first place on multi-page benchmarks tested against 9 other models (self-reported).
> * **Highs:** Scores **77.1** overall on MarathonDocBench (hundreds of pages), significantly outperforming the next best model, Kimi-K3 (33.7).
> * **Lows:** Scores **48.2** on heading hierarchy (TEDS) on MarathonDocBench, marking its lowest sub-score.

---

## 什么是 Unlimited OCR 2？

> ## What is Unlimited OCR 2?

Unlimited OCR 2 是一款多模态视觉语言模型，能够将按顺序排列的整篇文档页面图像直接转换为具备排版结构的纯文本，涵盖复杂表格、数学公式、图表注释、各级层级标题以及自然的阅读流顺序。它是 Baidu 于 2026 年 6 月开源的 [Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) 的全新升级迭代之作。

> Unlimited OCR 2 is a vision-language model that converts ordered page images into structured text, including tables, formulas, figures, headings, and reading order. It succeeds [Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR), which was released in June 2026.

该模型的官方 [配置架构](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/config.json) 延续了类似 DeepSeek-OCR 的经典设计：前端由 SAM ViT-B 与 CLIP-L 双视觉编码器构成，负责抽取细粒度文字与高层语义特征，随后将视觉特征输入后端的 12 层混合专家模型 (Mixture of Experts, MoE) 解码器。在推理时，每个 Token 会动态路由至 64 个路由专家中的 6 个，并始终激活 2 个共享专家。在多页处理模式下，每张输入的文档图像会被极其紧凑地压缩为 273 个图像 Token。

> The model’s [configuration](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/config.json) maintains a DeepSeek-OCR style layout: a SAM ViT-B plus CLIP-L encoder feeding into a 12-layer mixture-of-experts (MoE) decoder. Each token routes to 6 of 64 experts, alongside 2 shared experts. In multi-page mode, each processed page consumes 273 image tokens.

---

## SR-SWA 机制的工作原理

> ## How Does SR-SWA Work?

在标准注意力机制中，全量注意力计算的开销与序列长度呈二次方级爆炸增长。在自回归解码阶段，每一个新生成的 Token 都必须重新扫描并计算不断膨胀的键值缓存 (Key-Value Cache, KV Cache)；以每页文档消耗 273 个图像 Token 计算，光是解析一份 100 页的长文档，在尚未生成哪怕一个输出字符之前，系统就已累积了高达 27,300 个输入 Token 的庞大显存负担。

> Full attention costs grow quadratically with sequence length. During decoding, every new token scans an increasingly large KV cache; at 273 image tokens per page, parsing a 100-page document introduces 27,300 input tokens before generating any output.

**SR-SWA (稀疏参考滑动窗口注意力机制)** 正是为了攻破这一显存与算力瓶颈而生。它将庞大的图文交叉注意力范围深度压缩进一个固定尺寸的动态工作参考集 (Working References) 中。据官方 [Model Card](https://huggingface.co/baidu/Unlimited-OCR-2) 披露，标准的工作参考集大小仅设为 512 Token，其内部结合了覆盖临近区域的 128 Token 局部滑动窗口，以及对 32 Token 特征块执行 Top-16 稀疏检索的高效挑选机制。

> **SR-SWA (Sparse Reference Sliding Window Attention)** resolves this by compressing text-visual attention into a fixed set of working references. The [model card](https://huggingface.co/baidu/Unlimited-OCR-2) cites 512 tokens as a standard reference size, pairing a 128-token local window with top-16 selection over 32-token blocks. 

得益于这一巧妙的稀疏设计，即使文档页数成倍激增，模型单步自回归解码的显存消耗与单步延迟都能保持近乎恒定的平稳状态，成功在有限的上下文窗口约束下解锁了“无限视界”的长文档解析能力（需要说明的是，前端图像编码耗时以及整体端到端推理总时间仍会随着实际页面数量线性增长）。

> This design keeps per-step latency and memory usage nearly constant as document size increases, delivering "unlimited-horizon" parsing within a finite context window (though image encoding time and total runtime still scale with page counts).

---

## 在 MPDocBench 与 MarathonDocBench 基准评测上的表现

> ## Performance on MPDocBench and MarathonDocBench

Baidu 官方在包含数十页的中等长度基准 **MPDocBench** 与涵盖数百页超长篇幅的挑战性基准 **MarathonDocBench** 上对模型展开了全方位评测。

> Baidu evaluated the model on **MPDocBench** (dozens of pages per document) and **MarathonDocBench** (hundreds of pages). 

* **MPDocBench 综合得分**：Unlimited OCR 2 斩获 **84.6** 分高居榜首，紧随其后的是 Qwen3.8-Max (78.3 分) 与 Qwen-3.8-Flash-Next (77.4 分)。
* **MarathonDocBench 综合得分**：Unlimited OCR 2 表现极为抢眼，拿下 **77.1** 的高分；相比之下，竞品模型在数百页的极端长度下均遭遇性能断崖式滑坡（如 Kimi-K3 跌至 33.7 分，Qwen3.8-Max 跌至 22.9 分）。值得一提的是，其前代模型 Unlimited-OCR 在该基准上得分为 0.0。

> * **MPDocBench Overall:** Unlimited OCR 2 scores **84.6**, followed by Qwen3.8-Max at 78.3 and Qwen-3.8-Flash-Next at 77.4.
> * **MarathonDocBench Overall:** Unlimited OCR 2 scores **77.1**, while competitors experience sharp performance drops (e.g., Kimi-K3 at 33.7 and Qwen3.8-Max falling to 22.9). Its predecessor, Unlimited-OCR, scored 0.0 on this benchmark.

### 各维度细项得分对照 (MPDocBench / MarathonDocBench)

> ### Sub-Scores (MPDocBench / MarathonDocBench)

* **纯文本识别 (Text)**：94.8 / 89.6
* **数学公式解析 (Formula)**：89.4 / 87.9
* **阅读顺序还原 (Reading Order)**：92.3 / 85.3
* **表格结构还原 (Tables)**：87.8 / 74.8
* **标题层级推导 (Heading Hierarchy)**：60.1 / 48.2

> * **Text:** 94.8 / 89.6
> * **Formula:** 89.4 / 87.9
> * **Reading Order:** 92.3 / 85.3
> * **Tables:** 87.8 / 74.8
> * **Heading Hierarchy:** 60.1 / 48.2

*（注：以上所有评测数据均来自 Baidu 官方技术报告与自测统计图表。）*

> *(Note: All benchmark figures are self-reported by Baidu and sourced from their evaluation chart.)*

---

## 与主流开源 OCR 模型的横向对比

> ## Comparison with Other Open OCR Models

| 特性对比 (Feature) | Unlimited OCR 2 | Unlimited-OCR | DeepSeek-OCR-2 | PaddleOCR-VL-1.6 |
| :--- | :--- | :--- | :--- | :--- |
| **研发机构 (Developer)** | Baidu | Baidu | DeepSeek | Baidu PaddlePaddle |
| **总参数量 (Parameters)** | 3.34B | 3.34B | 3.39B | 0.96B |
| **激活参数量 (Active Parameters)** | 未公开 | 未公开 | 未公开 | 未公开 |
| **开源许可 (License)** | MIT | MIT | Apache 2.0 | Apache 2.0 |
| **发布时间 (Release Date)** | 2026 年 10 月 ([技术报告](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/Unlimited-OCR-2.pdf)) | 2026 年 6 月 ([arXiv](https://arxiv.org/abs/2606.23050)) | 2026 年 1 月 ([arXiv](https://arxiv.org/abs/2601.20552)) | 2026 年 6 月 ([arXiv](https://arxiv.org/abs/2606.03264)) |
| **长文档处理机制 (Long-Document Mechanism)** | SR-SWA 机制，512 Token 参考集 | 多页 `infer_multi`，无 SR-SWA | 未公开 | 未公开 |
| **MPDocBench 综合得分** | 84.6 (Baidu 自测) | 61.9 (Baidu 自测) | 未汇报 | 未汇报 |
| **MarathonDocBench 综合得分** | 77.1 (Baidu 自测) | 0.0 (Baidu 自测) | 未汇报 | 未汇报 |
| **部署推理支持 (Serving Options)** | Transformers, 定制版 SGLang | Transformers, [vLLM](https://recipes.vllm.ai/baidu/Unlimited-OCR), SGLang | Transformers, [SGLang](https://cookbook.sglang.io/autoregressive/DeepSeek/DeepSeek-OCR-2) | PaddleOCR, [Transformers](https://huggingface.co/docs/transformers/model_doc/paddleocr_vl) |

> | Feature | Unlimited OCR 2 | Unlimited-OCR | DeepSeek-OCR-2 | PaddleOCR-VL-1.6 |
> | :--- | :--- | :--- | :--- | :--- |
> | **Developer** | Baidu | Baidu | DeepSeek | Baidu PaddlePaddle |
> | **Parameters** | 3.34B | 3.34B | 3.39B | 0.96B |
> | **Active Parameters** | Not disclosed | Not disclosed | Not disclosed | Not disclosed |
> | **License** | MIT | MIT | Apache 2.0 | Apache 2.0 |
> | **Release Date** | Oct 2026 ([Report](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/Unlimited-OCR-2.pdf)) | Jun 2026 ([arXiv](https://arxiv.org/abs/2606.23050)) | Jan 2026 ([arXiv](https://arxiv.org/abs/2601.20552)) | Jun 2026 ([arXiv](https://arxiv.org/abs/2606.03264)) |
> | **Long-Document Mechanism** | SR-SWA, 512-token reference set | Multi-page `infer_multi`, no SR-SWA | Not disclosed | Not disclosed |
> | **MPDocBench Overall** | 84.6 (Baidu) | 61.9 (Baidu) | Not reported | Not reported |
> | **MarathonDocBench Overall** | 77.1 (Baidu) | 0.0 (Baidu) | Not reported | Not reported |
> | **Serving Options** | Transformers, custom SGLang | Transformers, [vLLM](https://recipes.vllm.ai/baidu/Unlimited-OCR), SGLang | Transformers, [SGLang](https://cookbook.sglang.io/autoregressive/DeepSeek/DeepSeek-OCR-2) | PaddleOCR, [Transformers](https://huggingface.co/docs/transformers/model_doc/paddleocr_vl) |

---

## 如何部署与运行 Unlimited OCR 2

> ## How to Run Unlimited OCR 2

* **基于 Transformers 运行**：适合进行轻量级快速实验验证。其中的 `infer` 函数通过动态切片技术（即高达模式/gundam mode）高效处理单页文档，而 `infer_multi` 函数则支持在单次请求中一次性解析整份多页文档，从而完整保留跨页上下文连贯性。加载模型时需在配置中显式指定 `trust_remote_code=True`。
* **基于 SGLang 部署**：若要实现高性能服务化部署，目前需要使用 Baidu 官方专门提供的定制版 wheel 编译包，而非直接使用开源社区上游 SGLang。官方推荐的生产部署架构为每个滑动窗口调度 10 页文档，并复用上一个窗口末尾的 KV 缓存尾部数据，以此实现严密的显存开销控制。

> * **Transformers:** Useful for quick testing. The `infer` function handles single pages via dynamic tiling (gundam mode), while `infer_multi` parses all pages in a single request to maintain cross-page context. Loading requires setting `trust_remote_code=True`.
> * **SGLang:** Serving requires a customized wheel provided by Baidu rather than upstream SGLang. Recommended setups schedule 10 pages per window and reuse the previous window's KV tail to manage memory.

---

## 核心总结与技术要点

> ## Key Takeaways

* Unlimited OCR 2 是由 Baidu 开源的 3.34B 参数量级长文档 OCR 模型，采用商业友好的 MIT 开源许可证。
* 创新的 SR-SWA 稀疏注意力机制通过将工作参考集严格约束在 512 Token 内，成功锁定了注意力计算与显存开销的上限。
* 在面向数百页超长文档解析任务的 MarathonDocBench 评测中，该模型取得了 77.1 分的行业顶尖成绩。
* 在复杂长文档的标题层级结构还原方面仍有进一步优化空间，目前在该细项评测中得分为 48.2。
* 当前公布的所有性能评测指标均来自模型作者团队的自测报告，有待开源社区后续广泛验证。

> * Unlimited OCR 2 is a 3.34B parameter, MIT-licensed long-document OCR model developed by Baidu.
> * Its SR-SWA mechanism bounds attention overhead using a fixed 512-token reference set.
> * It achieves a leading score of 77.1 on MarathonDocBench for multi-hundred-page parsing tasks.
> * Heading hierarchy extraction remains an area for improvement, scoring 48.2 on long-form documents.
> * All evaluation metrics are currently self-reported by the authors.

---

### 核心资源与项目链接

> ### Resources & Links

* 欢迎访问官方 [Model Card](https://huggingface.co/baidu/Unlimited-OCR-2)、查阅完整 [技术报告](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/Unlimited-OCR-2.pdf)，或前往 [GitHub 代码仓库](https://github.com/baidu/Unlimited-OCR) 获取源码与权重。

> * Check out the [Model Card](https://huggingface.co/baidu/Unlimited-OCR-2), [Technical Report](https://huggingface.co/baidu/Unlimited-OCR-2/blob/main/Unlimited-OCR-2.pdf), and [GitHub Repository](https://github.com/baidu/Unlimited-OCR).
