---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-24
hide:
  - navigation
tags:
  - TorchTPU
  - PyTorch
  - TPU
  - 编译器
  - 深度学习加速
title: "TorchTPU：融合动态与编译图的原生 PyTorch TPU 执行架构"
---

# TorchTPU：融合动态与编译图的原生 PyTorch TPU 执行架构

> # TorchTPU: A Hybrid Eager/Compiled Architecture for Native PyTorch Execution on TPU

> **arXiv Identifier:** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **Submitted On:** 16 October 2026; Last revised: 22 October 2026 (Version v3)  
> **DOI:** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)

### 文章背景与核心概要

长期以来，PyTorch 开发者在将深度学习模型部署或迁移到 Google 张量处理器 (TPU) 硬件时，常常面临静态图编译笨重、动态图交互调试体验割裂以及性能调优门槛高等固有痛点。由 Google 与 Meta 联合打造的开源架构 **TorchTPU** 应运而生，它通过深度融合动态图 (Eager Mode) 的即时调试灵活性与 `torch.compile` 静态编译图的极致性能，首次为 Google TPU 构建了规范化、符合直觉的原生 PyTorch 后端。TorchTPU 依托底层原生硬件加速器与先进的动态执行优化机制，实现了真正意义上的“开箱即用”——开发者无需对现有 PyTorch 代码进行破坏性重构，即可无缝迁移并在 TPU 集群上高效运行。评测表明，该架构在模型训练和推理两端均展现出了极具行业竞争力的顶尖性能，不仅大幅抹平了 GPU 与 TPU 之间的生态迁移鸿沟，更重塑了下一代跨硬件深度学习编译基础设施的协作范式。

---

## 内容概要

> ## Summary

**TorchTPU** 是 Google 与 Meta 深度合作研发的开源项目，它为 Google 张量处理器 (TPU) 引入了规范化、高内聚的原生 PyTorch 后端支持。该框架通过深度融合动态图即时执行 (Eager Execution) 优化机制、`torch.compile` 编译图深度集成以及底层原生硬件加速技术，使各类深度学习模型能够实现无缝的“开箱即用”式运行和极速 TPU 迁移，同时在模型训练与推理场景下均能释放出领先业界的强劲性能。

> **TorchTPU** is an open-source collaboration between Google and Meta that introduces a native, principled PyTorch backend for Google Tensor Processing Units (TPUs). The framework facilitates seamless, out-of-the-box model execution and TPU migration while delivering industry-competitive training and inference performance. It achieves this by combining eager execution optimizations, `torch.compile` integration, and native hardware acceleration.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 论文编号：** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]
* **主要研究领域：** 人工智能 (`cs.AI`)
* **提交时间：** 2026 年 10 月 16 日
* **最新修订：** 2026 年 10 月 22 日 (第 3 版)
* **数字对象唯一标识符 (DOI) ：** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)

> * **arXiv Identifier:** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Submitted On:** 16 October 2026
> * **Last Revised:** 22 October 2026 (Version v3)
> * **DOI:** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)

---

## 论文作者

> ## Authors

Claudio Basile, Michael Voznesensky, Gunhyun Park, Ben Wilson, Parker Holloway, Zhanyong Wan, Vlad Belous, Manish Khanna, Paul Ganssle, Kevin Gleason, Andrew Dame, Brendan Folie, Bhavya Bahl, Haifeng Jin, Pedro Goncalves Mokarzel, Arian Arfaian, Luke Boyer, Chi Zhang, Yiling Yuan, Adam Mainz, Aditya Patel, Huangze Tang, Jay Gan, Lizzie Liang, Will Froom, Tushar Agarwal, Karlo Basioli, Theotime Combes, Emilio Cota, Minos Papadopoulos, Tudor Pipernea, Yarong Mu, Qi Zhou, Yaoshiang Ho, Aleksey Vlasenko, Alexander Brauckmann, Ziyin Huang, Jack Oh, Jerry Hsu, Tanvi Bajpai, Jialei Chen, Wenjun Gu, Chintan Shah, Chris Chan, Sayce Falk, Chris Jones, Rob Torres, Kat Ko, Lee Howes, Freya Azad, Andi Gavrilescu, Joe Pamer 以及 Bill Jia。

> Claudio Basile, Michael Voznesensky, Gunhyun Park, Ben Wilson, Parker Holloway, Zhanyong Wan, Vlad Belous, Manish Khanna, Paul Ganssle, Kevin Gleason, Andrew Dame, Brendan Folie, Bhavya Bahl, Haifeng Jin, Pedro Goncalves Mokarzel, Arian Arfaian, Luke Boyer, Chi Zhang, Yiling Yuan, Adam Mainz, Aditya Patel, Huangze Tang, Jay Gan, Lizzie Liang, Will Froom, Tushar Agarwal, Karlo Basioli, Theotime Combes, Emilio Cota, Minos Papadopoulos, Tudor Pipernea, Yarong Mu, Qi Zhou, Yaoshiang Ho, Aleksey Vlasenko, Alexander Brauckmann, Ziyin Huang, Jack Oh, Jerry Hsu, Tanvi Bajpai, Jialei Chen, Wenjun Gu, Chintan Shah, Chris Chan, Sayce Falk, Chris Jones, Rob Torres, Kat Ko, Lee Howes, Freya Azad, Andi Gavrilescu, Joe Pamer, and Bill Jia.

---

## 论文摘要

> ## Abstract

**TorchTPU** 是由 Google 与 Meta 携手合作打造的开源架构，首次为 Google TPU 平台引入了原生、规范且符合工程直觉的 PyTorch 执行后端。通过将动态图即时执行 (Eager Execution) 优化、[`torch.compile`](http://torch.compile) 编译图深度融合以及原生硬件加速能力集于一身，TorchTPU 真正实现了深度学习模型开箱即用的极简体验与顺畅的 TPU 生态迁移，同时在模型训练和推理评测中均展现出极具行业竞争力的卓越性能。

> 💬 [原文摘要 / Original Abstract]:  
> TorchTPU is an open-source collaboration between Google and Meta that introduces a native and principled PyTorch backend for Google TPUs. It enables seamless out-of-the-box model execution and TPU migration while delivering industry-competitive inference and training performance through eager execution optimizations, [`torch.compile`](http://torch.compile) integration, and native hardware acceleration.

---

## 全文与相关资源

> ## Full-Text & Resources

* [阅读 PDF 原文](https://arxiv.org/pdf/2610.24161)
* [HTML 网页版 (实验性功能) ](https://arxiv.org/html/2610.24161v3)
* [TeX 源代码](https://arxiv.org/src/2610.24161)
* [查看授权许可协议](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

> * [View PDF](https://arxiv.org/pdf/2610.24161)
> * [HTML Version (Experimental)](https://arxiv.org/html/2610.24161v3)
> * [TeX Source](https://arxiv.org/src/2610.24161)
> * [View License](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

### 外部引用与检索工具

> ### External Citations & Tools

* **学术指标与文献探索：** [SciX](https://scixplorer.org/abs/arXiv:2610.24161) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.24161) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.24161)
* **开源代码与可复现性：** [alphaXiv](https://alphaxiv.org/) | [CatalyzeX](https://www.catalyzex.com) | [Hugging Face](https://huggingface.co/huggingface)

> * **Metrics & Exploration:** [SciX](https://scixplorer.org/abs/arXiv:2610.24161) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.24161) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.24161)
> * **Code & Reproducibility:** [alphaXiv](https://alphaxiv.org/) | [CatalyzeX](https://www.catalyzex.com) | [Hugging Face](https://huggingface.co/huggingface)
