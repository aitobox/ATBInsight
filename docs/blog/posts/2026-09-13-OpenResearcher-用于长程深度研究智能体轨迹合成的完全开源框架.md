---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 深度研究智能体
  - 智能体轨迹合成
  - 离线环境
  - 强化学习与SFT
  - 信息检索
title: "OpenResearcher：用于长程深度研究智能体轨迹合成的完全开源框架"
---

# OpenResearcher：用于长程深度研究智能体轨迹合成的完全开源框架

> # OpenResearcher: A Fully Open Pipeline for Long-Horizon Deep Research Trajectory Synthesis

> **arXiv:2603.20278** [cs.IR]  
> **Subjects:** Information Retrieval (cs.IR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)  
> **Authors:** Zhuofeng Li, Dongfu Jiang, Xueguang Ma, Haoxiang Zhang, Ping Nie, Yuyu Zhang, Kai Zou, Jianwen Xie, Yu Zhang, Wenhu Chen  
> **Submitted:** 17 Mar 2026; Last revised: 10 Sep 2026 (v2)  
> **Project / Code:** [GitHub - TIGER-AI-Lab/OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)

### 文章背景与核心概要

训练能够自主解决复杂科研与调研课题的“深度研究智能体” (Deep Research Agent) ，需要依赖大量交织着网页搜索、证据交叉聚合与多步逻辑推理的高质量长程轨迹数据。然而，当前业界的数据采集管线普遍深度依赖商业闭源的网页搜索 API，不仅调用费用高昂、网络响应脆弱，更因网络内容的实时变动而导致实验轨迹极难复现。

为此，TIGER-AI 实验室联合多家研究机构推出了 **OpenResearcher**，这是一个全流程开源且严格可复现的智能体轨迹合成框架。该框架创新性地将一次性语料冷启动与多轮长程轨迹合成解耦，并在包含 1500 万篇文档的纯离线语料库上，通过 `search`、`open` 与 `find` 三项基础浏览器原子操作闭环运行。借助开源教师模型 `GPT-OSS-120B`，团队合成了超过 9.7 万条研究轨迹，其中包含大量单条工具调用突破 100 次的长程复杂尾部数据。在合成数据上微调 30B-A3B 基座模型后，其在 BrowseComp-Plus 基准上的准确率大幅飙升 34 个百分点达到 54.8%，为学术界开展深度研究智能体的训练与可控评估提供了坚实基石。

---

## 📌 核心执行概要

> ## 📌 Executive Summary

训练具备深层推理与调查能力的深度研究智能体，离不开复杂且跨越长步长的决策轨迹，这些轨迹必须将检索操作、证据归纳以及多步骤推理严丝合缝地交织在一起。以往的数据收集管线重度依赖商业化的网络搜索 API，这带来了高昂的经济成本、服务不稳定以及严重的复现难题。

> Training sophisticated deep research agents requires complex, long-horizon trajectories that seamlessly interleave search operations, evidence aggregation, and multi-step reasoning. Traditionally, data collection pipelines rely heavily on proprietary web APIs, which introduces high costs, instability, and reproducibility hurdles.

为了突破这些屏障，作者团队打造了 **OpenResearcher**，这是一个完全开源且可复现的数据管线，旨在将一次性的语料构建与多轮轨迹合成彻底解耦。OpenResearcher 完全在离线环境下基于一个拥有 1500 万篇文档的海量语料库运行，仅依赖三个核心的浏览器原语操作（`search`、`open` 与 `find`）。在开源教师模型 `GPT-OSS-120B` 的驱动下，该管线成功合成了超过 97,000 条高质量轨迹——其中包括大量单条轨迹包含 100 次以上工具调用的超长程子集。在这一合成数据集上对 30B-A3B 骨干模型进行监督微调 (SFT) 后，模型在 **BrowseComp-Plus 上取得了 54.8% 的优异准确率**（相较基座模型显著提升了 34.0 个百分点），并在 BrowseComp、GAIA 和 xbench-DeepSearch 等基准上全面保持强劲的竞争力。

> To overcome these barriers, the authors introduce **OpenResearcher**, a fully open and reproducible pipeline designed to decouple corpus bootstrapping from multi-turn trajectory synthesis. Operating entirely offline over a massive 15-million-document corpus, OpenResearcher uses three core browser primitives (`search`, `open`, and `find`). Powered by the `GPT-OSS-120B` teacher model, the pipeline successfully synthesizes over 97,000 trajectories—including an extensive long-horizon subset featuring upwards of 100 tool calls per trajectory. Fine-tuning a 30B-A3B backbone model on this synthetic dataset yields a remarkable **54.8% accuracy on BrowseComp-Plus** (+34.0 point improvement over the base model), while maintaining competitive performance across benchmarks like BrowseComp, GAIA, and xbench-DeepSearch.

---

## 📖 摘要

> ## 📖 Abstract

训练深度研究智能体需要交替进行搜索、证据聚合与多步推理的长程交互轨迹。然而，现有的数据构建方案通常依赖专有的网页 API，使得大规模轨迹合成成本昂贵、稳定性差且难以复现。我们提出了 OpenResearcher，这是一个可复现的完整管线，它将单次语料冷启动与多轮交互轨迹合成解耦，并在一个包含 1500 万文档的语料库上，仅使用三个显式的浏览器原语操作（search、open 和 find）完全离线执行检索与浏览闭环。通过采用 GPT-OSS-120B 作为教师模型，我们合成了超过 9.7 万条轨迹，其中包含大量具有 100 次以上工具调用的长程尾部样例。在这些轨迹上对 30B-A3B 骨干模型进行监督微调后，其在 BrowseComp-Plus 上的准确率达到 54.8%，相较基础模型提升了 34.0 个百分点，同时在 BrowseComp、GAIA 和 xbench-DeepSearch 评测中保持高度竞争力。由于运行环境完全离线且指标完全可观测，它还支持细致的受控消融分析；我们的研究揭示了深度研究系统设计的诸多实用见解，包括数据过滤策略、智能体架构选型，以及检索命中率如何直接映射为最终答案的准确率。我们在 [GitHub 链接](https://github.com/TIGER-AI-Lab/OpenResearcher) 上完整开源了该管线、合成轨迹、模型权重与离线搜索评估环境。

> Training deep research agents requires long-horizon trajectories that interleave search, evidence aggregation, and multi-step reasoning. However, existing data collection pipelines typically rely on proprietary web APIs, making large-scale trajectory synthesis costly, unstable, and difficult to reproduce. We present OpenResearcher, a reproducible pipeline that decouples one-time corpus bootstrapping from multi-turn trajectory synthesis and executes the search-and-browse loop entirely offline using three explicit browser primitives: search, open, and find, over a 15M-document corpus. Using GPT-OSS-120B as the teacher model, we synthesize over 97K trajectories, including a substantial long-horizon tail with 100+ tool calls. Supervised fine-tuning a 30B-A3B backbone on these trajectories achieves 54.8\% accuracy on BrowseComp-Plus, a +34.0 point improvement over the base model, while remaining competitive on BrowseComp, GAIA, and xbench-DeepSearch. Because the environment is offline and fully instrumented, it also enables controlled analysis, where our study reveals practical insights into deep research pipeline design, including data filtering strategies, agent configuration choices, and how retrieval success relates to final answer accuracy. We release the pipeline, synthesized trajectories, model checkpoints, and the offline search environment at [this link](https://github.com/TIGER-AI-Lab/OpenResearcher).

---

## ⚙️ 管线核心亮点

> ## ⚙️ Key Pipeline Highlights

* **解耦式系统架构：** 将一次性语料冷启动与多轮长程轨迹生成完全剥离，确保全流程具备严格的可复现性，并显著降低了计算与环境维护开销。
* **纯离线运行环境：** 彻底摆脱对外部专有商业网页 API 的依赖，在精心构建的 **1500 万篇文档语料库** 上平稳运行，仅使用三个基本浏览器交互原语：
  1. `search`（搜索）
  2. `open`（打开）
  3. `find`（查找）
* **规模与交互复杂度：** 利用强大的 `GPT-OSS-120B` 开源教师模型产出逾 **9.7 万条合成轨迹** ，形成极具挑战性的长程分布，单任务交互深度可突破 **100 次以上的工具调用** 。
* **可控的可视化分析：** 得益于环境完全离线且仪表化可追溯，研究者能够深入探究深度研究智能体设计的最佳实践，清晰揭示数据清洗策略、智能体参数配置以及检索召回质量与最终答题准确率之间的内在联系。

> * **Decoupled Architecture:** Separates one-time corpus bootstrapping from multi-turn trajectory generation to ensure full reproducibility and lower computational overhead.
> * **Offline Execution Environment:** Operates independently of external, proprietary web APIs over a curated **15-million-document corpus** utilizing three fundamental browser primitives:
>   1. `search`
>   2. `open`
>   3. `find`
> * **Scale & Complexity:** Leverages `GPT-OSS-120B` as a teacher model to produce over **97K trajectories**, featuring a robust long-horizon distribution scaling past **100+ tool calls** per trajectory.
> * **Controlled Analysis:** The completely instrumented, offline framework permits deep investigation into optimal pipeline design, illuminating best practices for data filtering, agent configurations, and retrieval-to-accuracy correlations.

---

## 📊 性能与实验结果

> ## 📊 Performance & Results

当利用合成的研究轨迹在 **30B-A3B 骨干模型** 上实施监督微调 (Supervised Fine-Tuning, SFT) 时，系统取得了令人瞩目的效果：
* **BrowseComp-Plus：** 取得 **54.8% 的准确率**（相较基础模型实现了 **+34.0 个百分点的飞跃**）。
* **出色的泛化能力：** 在多个极具挑战性的权威基准测试中持续保持强大的竞争力，包括 **BrowseComp**、**GAIA** 以及 **xbench-DeepSearch**。

> When applying Supervised Fine-Tuning (SFT) using the synthesized trajectories on a **30B-A3B backbone model**, the system achieves:
> * **BrowseComp-Plus:** **54.8% accuracy** (a massive **+34.0 point improvement** over the baseline model).
> * **Robust Generalization:** Maintains highly competitive performance across alternative complex benchmarks including **BrowseComp**, **GAIA**, and **xbench-DeepSearch**.

---

## 🔗 相关资源与文献索引

> ## 🔗 Additional Links & Resources

* **全文阅读：** [查看 PDF](https://arxiv.org/pdf/2603.20278) | [实验性 HTML](https://arxiv.org/html/2603.20278v2) | [TeX 源码](https://arxiv.org/src/2603.20278)
* **开源代码与资产：** [GitHub - TIGER-AI-Lab/OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)
* **文献检索工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.20278) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.20278) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.20278)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2603.20278) | [Experimental HTML](https://arxiv.org/html/2603.20278v2) | [TeX Source](https://arxiv.org/src/2603.20278)
> * **Code & Artifacts:** [GitHub - TIGER-AI-Lab/OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)
> * **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.20278) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.20278) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.20278)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
