---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 大语言模型
  - 嵌入推理
  - Token压缩
  - FastE
  - 检索增强
title: "FastE：基于读出触发的 LLM 嵌入推理 Token 压缩算法"
---

# FastE：基于读出触发的 LLM 嵌入推理 Token 压缩算法

> # FastE: Readout-Triggered Token Compression for LLM Embedding Inference
>
> | 属性 (Attribute) | 详情 (Detail) |
> | :--- | :--- |
> | **arXiv 标识符 (arXiv Identifier)** | [arXiv:2609.08407](https://arxiv.org/abs/2609.08407) [cs.AI] |
> | **主分类 (Primary Subject)** | 计算机科学 > 人工智能 (`cs.AI`) |
> | **论文作者 (Authors)** | Jinsong Shu, Jinyong Wen, Baokun Wang, Zhongle Xie, Lidan Shou, Weiqiang Wang, Gang Chen |
> | **提交历史 (Submission History)** | [v1] 2026年9月8日 周二<br>[v2] 2026年9月10日 周四 (当前版本) |
> | **授权许可 (License)** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png) |

### 文章背景与核心概要
利用现代大语言模型 (Large Language Model, LLM) 生成高质量的向量嵌入已成为文本检索与多模态表征的核心基石，然而在长文本推理阶段，庞大的计算开销和显存占用极大限制了其部署扩展性。本文研究团队揭示了嵌入推理中普遍存在的“前缀深度依赖冗余”现象——即在网络较浅层剔除前缀状态对表现伤害极大，但在较深层这些前缀状态高度冗余、极具可压缩性。为此，研究团队提出了一种无需重新训练的即插即用算法 FastE，通过轻量级在线启发式准则在读出与前缀对齐时动态触发压缩，并依据注意力评分进行筛选。实验表明，FastE 能在保持 99.5% 以上检索精度的前提下减少高达 40% 的计算浮点运算量 (FLOPs) ，为大规模向量检索与索引系统提供了高实用价值的加速方案。

---

## 📌 内容概要

> ## Summary

**FastE** 是一种无需重新训练、即插即用的推理优化方法，旨在显著提升基于最终读出 (Final-Readout) 的大语言模型 (LLM) 嵌入推理计算效率。通过揭示前缀状态随网络深度递增的可压缩性——即前缀在深层网络中表现出明显的深度依赖冗余，FastE 设计了一种轻量级的在线启发式规则：采用基于批次均值读出-前缀对齐度的统一固定阈值来触发压缩，并利用读出位置对前缀状态的注意力得分对各状态进行重要性排序。

> **FastE** is a training-free, plug-and-play method designed to improve the computational efficiency of final-readout Large Language Model (LLM) embedding inference. By identifying depth-dependent prefix redundancy—where prefix states become increasingly compressible in deeper layers—FastE introduces a lightweight online heuristic. It uses a shared fixed threshold on batch-mean readout-prefix alignment to trigger compression, and ranks prefix states using attention scores received from the readout position. 

实验评估表明，FastE 在多个基准测试、模型规模以及跨模态检索任务中均能大幅降低计算成本 (例如在 NarrativeQA 数据集上使用 Qwen3-Embedding-0.6B 时，将解码器骨干计算浮点量 FLOPs 削减了 **40.11%**，同时保留了完整前向推理 **99.53%** 的 nDCG@10 检索质量) ，且全程无需任何微调或重新训练。

> Evaluations demonstrate that FastE substantially cuts computational costs (e.g., reducing decoder-backbone FLOPs by **40.11%** while retaining **99.53%** of Full Forward nDCG@10 on NarrativeQA using Qwen3-Embedding-0.6B) across multiple benchmarks, scales, and cross-modal retrieval tasks without requiring retraining.

---

## 📄 论文元数据

> ## Paper Metadata

| 属性 | 详情 |
| :--- | :--- |
| **arXiv 标识符** | [arXiv:2609.08407](https://arxiv.org/abs/2609.08407) [cs.AI] |
| **主分类** | 计算机科学 > 人工智能 (`cs.AI`) |
| **论文作者** | Jinsong Shu, Jinyong Wen, Baokun Wang, Zhongle Xie, Lidan Shou, Weiqiang Wang, Gang Chen |
| **提交历史** | [v1] 2026年9月8日 周二<br>[v2] 2026年9月10日 周四 (当前版本) |
| **授权许可** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png) |

> | Attribute | Detail |
> | :--- | :--- |
> | **arXiv Identifier** | [arXiv:2609.08407](https://arxiv.org/abs/2609.08407) [cs.AI] |
> | **Primary Subject** | Computer Science > Artificial Intelligence (`cs.AI`) |
> | **Authors** | Jinsong Shu, Jinyong Wen, Baokun Wang, Zhongle Xie, Lidan Shou, Weiqiang Wang, Gang Chen |
> | **Submission History** | [v1] Tue, 8 Sep 2026<br>[v2] Thu, 10 Sep 2026 (This version) |
> | **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png) |

---

## 📄 论文摘要

> ## Abstract

在本研究中，我们在基于最终读出机制的 LLM 嵌入模型中发现了深度依赖的前缀冗余性，该现象在包括 Qwen3-Embedding 和 Qwen3-VL-Embedding 等代表性骨干网络中普遍存在。我们发现，在浅层移除前缀状态对模型性能的破坏远大于在深层移除，这表明随着前缀与读出状态在网络中的前向传递，前缀状态变得越来越容易被压缩。为此，我们提出了 FastE，这是一种免训练、即插即用的加速方法。FastE 使用基于批次均值读出-前缀对齐度的共享固定阈值作为轻量级在线启发式标准，自适应决定何时触发压缩，并根据读出位置对前缀状态分配的注意力分数进行排序，决定在后续层中保留哪些状态。实证评估展示了 FastE 大幅削减计算开销的能力：在 NarrativeQA 基准上搭配 Qwen3-Embedding-0.6B 时，该方法降低了 40.11% 的解码器骨干网络 FLOPs，同时保留了完整前向推理 99.53% 的 nDCG@10 分数。在涵盖五个文本嵌入基准测试、两种骨干模型参数规模以及三项跨模态检索任务的评测中，无需任何重训即可通过调节最大剔除比例直接定制“质量-效率”权衡。我们相信，FastE 为检索、索引构建、聚类和多模态表征系统中的可扩展向量嵌入生成提供了切实的工程落地价值。

> In this study, we identify depth-dependent prefix redundancy in final-readout LLM embedding models, notably across representative backbones including Qwen3-Embedding and Qwen3-VL-Embedding. We find that removing prefix states is substantially more damaging in shallow layers than at greater depth, showing that prefix states become increasingly compressible as the prefix and readout states propagate through the network. To this end, we introduce FastE, a training-free, plug-and-play method. FastE uses a shared fixed threshold on batch-mean readout-prefix alignment as a lightweight online heuristic for selecting when compression occurs, and ranks prefix states by the attention scores they receive from the readout position to determine which states are retained in subsequent layers. Our evaluations demonstrate FastE's ability to substantially reduce computational costs: on NarrativeQA with Qwen3-Embedding-0.6B, it reduces decoder-backbone FLOPs by 40.11% while retaining 99.53% of Full Forward nDCG@10. Across five text embedding benchmarks, two backbone scales, and three cross-modal retrieval tasks, the quality-efficiency trade-off is directly customizable through the maximum removal ratio without retraining. We believe FastE offers practical value for scalable embedding generation in retrieval, indexing, clustering, and multimodal representation systems.

---

## 🔗 全文阅读与访问链接

> ## Full-Text & Access Links

* [查看 PDF](https://arxiv.org/pdf/2609.08407)
* [HTML 网页版 (实验性)](https://arxiv.org/html/2609.08407v2)
* [TeX 源码](https://arxiv.org/src/2609.08407)
* [DOI 链接](https://doi.org/10.48550/arXiv.2609.08407)

> * [View PDF](https://arxiv.org/pdf/2609.08407)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.08407v2)
> * [TeX Source](https://arxiv.org/src/2609.08407)
> * [DOI Link](https://doi.org/10.48550/arXiv.2609.08407)

---

## 🛠️ 外部资源与工具

> ## External Resources & Tools

* **文献书目工具：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.08407) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.08407) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.08407)
* **代码与相关数据：** 可通过 [Hugging Face](https://huggingface.co/huggingface)、[CatalyzeX](https://www.catalyzex.com) 以及 [alphaXiv](https://alphaxiv.org/) 获取。

> * **Bibliographic Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.08407) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.08407) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.08407)
> * **Code & Associated Data:** Available via [Hugging Face](https://huggingface.co/huggingface), [CatalyzeX](https://www.catalyzex.com), and [alphaXiv](https://alphaxiv.org/).
