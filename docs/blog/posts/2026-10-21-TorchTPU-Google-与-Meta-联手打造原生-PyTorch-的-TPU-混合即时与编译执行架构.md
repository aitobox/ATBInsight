---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-21
hide:
  - navigation
tags:
  - TorchTPU
  - PyTorch
  - TPU
  - Google
  - Meta
  - torch.compile
title: "TorchTPU：Google 与 Meta 联手打造原生 PyTorch 的 TPU 混合即时与编译执行架构"
---

# TorchTPU：Google 与 Meta 联手打造原生 PyTorch 的 TPU 混合即时与编译执行架构

> # TorchTPU - A Hybrid Eager/Compiled Architecture for Native PyTorch Execution on TPU

> **arXiv ID:** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]  
> **Authors:** Claudio Basile, Michael Voznesensky, Gunhyun Park, Ben Wilson, Parker Holloway, Zhanyong Wan, Vlad Belous, Manish Khanna, Paul Ganssle, Kevin Gleason, Andrew Dame, Brendan Folie, Bhavya Bahl, Haifeng Jin, Pedro Goncalves Mokarzel, Arian Arfaian, Luke Boyer, Chi Zhang, Yiling Yuan, Adam Mainz, Aditya Patel, Huangze Tang, Jay Gan, Lizzie Liang, Will Froom, Tushar Agarwal, Karlo Basioli, Theotime Combes, Emilio Cota, Minos Papadopoulos, Tudor Pipernea, Yarong Mu, Qi Zhou, Yaoshiang Ho, Aleksey Vlasenko, Alexander Brauckmann, Ziyin Huang, Jack Oh, Jerry Hsu, Tanvi Bajpai, Jialei Chen, Wenjun Gu, Chintan Shah, Chris Chan, Sayce Falk, Chris Jones, Rob Torres, Kat Ko, Lee Howes, Freya Azad, Andi Gavrilescu, Joe Pamer, Bill Jia (共 53 位作者)  
> **Submitted:** October 16, 2026  
> **DOI:** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)

### 文章背景与核心概要

长期以来，深度学习开发者在使用 Google 自研的张量处理单元 (Tensor Processing Unit, TPU) 时，往往面临着框架生态割裂的痛点——主流的 PyTorch 模型在迁移至 TPU 平台时，经常遭遇繁琐的环境适配门槛或运行时效率折损。为了彻底打破这一算力生态壁垒，Google 与 Meta 两大科技巨头展开前所未有的深度开源合作，联合推出了专为 Google TPU 量身定制的原生后端架构 **TorchTPU**。该架构创造性地融合了动态即时执行 (Eager Execution) 优化与现代 `torch.compile` 图编译加速技术，不仅让海量现成 PyTorch 模型无需任何代码改动即可在 TPU 集群上“开箱即用”极速运转，更在模型推理与分布式训练中释放出具备行业顶尖竞争力的硬件性能。这项重磅突破理顺了 PyTorch 开发者迈向 TPU 算力底座的平滑迁移之路，标志着全球顶级 AI 硬件与主流算法生态正加速走向深度的底层大融合。

---

## 核心概要

> ## Summary

**TorchTPU** 是 Google 与 Meta 联手推出的开源重大合作成果，旨在为 Google 张量处理单元 (Tensor Processing Unit, TPU) 构建一套原生且符合设计规范的 PyTorch 官方级硬件后端。通过创造性地结合动态即时执行 (Eager Execution) 优化、`torch.compile` 深度编译集成与底层原生硬件加速，该架构为大模型的实时推理与大规模训练注入了极具行业竞争力的顶尖性能，同时大幅简化了现有 PyTorch 模型的开箱即用运行与 TPU 迁移流程。

> **TorchTPU** is an open-source collaboration between Google and Meta designed to introduce a native, principled PyTorch backend for Google Tensor Processing Units (TPUs). By combining eager execution optimizations, `torch.compile` integration, and native hardware acceleration, the architecture delivers industry-competitive performance for both model inference and training while streamlining out-of-the-box model execution and TPU migration.

---

## 论文详细信息

> ## Paper Information

* **arXiv 编号 (arXiv ID)：** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]
* **DOI 标识 (DOI)：** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)
* **提交时间 (Submitted On)：** 2026 年 10 月 16 日
* **主要学科 (Primary Subject)：** 人工智能 (`cs.AI`)
* **论文篇幅 (Length)：** 23 页，包含 5 幅插图
* **论文作者 (Authors)：** Claudio Basile, Michael Voznesensky, Gunhyun Park, Ben Wilson, Parker Holloway, Zhanyong Wan, Vlad Belous, Manish Khanna, Paul Ganssle, Kevin Gleason, Andrew Dame, Brendan Folie, Bhavya Bahl, Haifeng Jin, Pedro Goncalves Mokarzel, Arian Arfaian, Luke Boyer, Chi Zhang, Yiling Yuan, Adam Mainz, Aditya Patel, Huangze Tang, Jay Gan, Lizzie Liang, Will Froom, Tushar Agarwal, Karlo Basioli, Theotime Combes, Emilio Cota, Minos Papadopoulos, Tudor Pipernea, Yarong Mu, Qi Zhou, Yaoshiang Ho, Aleksey Vlasenko, Alexander Brauckmann, Ziyin Huang, Jack Oh, Jerry Hsu, Tanvi Bajpai, Jialei Chen, Wenjun Gu, Chintan Shah, Chris Chan, Sayce Falk, Chris Jones, Rob Torres, Kat Ko, Lee Howes, Freya Azad, Andi Gavrilescu, Joe Pamer, Bill Jia (共 53 位作者)

> * **arXiv ID:** [arXiv:2610.24161](https://arxiv.org/abs/2610.24161) [cs.AI]
> * **DOI:** [10.48550/arXiv.2610.24161](https://doi.org/10.48550/arXiv.2610.24161)
> * **Submitted On:** October 16, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Length:** 23 pages, 5 figures
> * **Authors:** Claudio Basile, Michael Voznesensky, Gunhyun Park, Ben Wilson, Parker Holloway, Zhanyong Wan, Vlad Belous, Manish Khanna, Paul Ganssle, Kevin Gleason, Andrew Dame, Brendan Folie, Bhavya Bahl, Haifeng Jin, Pedro Goncalves Mokarzel, Arian Arfaian, Luke Boyer, Chi Zhang, Yiling Yuan, Adam Mainz, Aditya Patel, Huangze Tang, Jay Gan, Lizzie Liang, Will Froom, Tushar Agarwal, Karlo Basioli, Theotime Combes, Emilio Cota, Minos Papadopoulos, Tudor Pipernea, Yarong Mu, Qi Zhou, Yaoshiang Ho, Aleksey Vlasenko, Alexander Brauckmann, Ziyin Huang, Jack Oh, Jerry Hsu, Tanvi Bajpai, Jialei Chen, Wenjun Gu, Chintan Shah, Chris Chan, Sayce Falk, Chris Jones, Rob Torres, Kat Ko, Lee Howes, Freya Azad, Andi Gavrilescu, Joe Pamer, Bill Jia (53 authors total)

---

## 论文摘要

> ## Abstract

> 💬 [原文引用 / Original Quote]:
> TorchTPU 是 Google 与 Meta 联手打造的开源合作成果，旨在为 Google TPU 引入一套原生且符合设计规范的 PyTorch 后端。通过融合动态即时执行优化、`torch.compile` 图编译集成与原生硬件加速能力，它不仅支持模型免修改开箱即用运行与极简 TPU 迁移，更在模型推理与训练任务中提供了具备行业顶尖竞争力的卓越性能。
>
> TorchTPU is an open-source collaboration between Google and Meta that introduces a native and principled PyTorch backend for Google TPUs. It enables seamless out-of-the-box model execution and TPU migration while delivering industry-competitive inference and training performance through eager execution optimizations, [torch.compile](http://torch.compile) integration, and native hardware acceleration.

---

## 全文与外部资源

> ## Full-Text and External Resources

* **PDF 全文访问 (PDF Access)：** [查看 PDF 论文](https://arxiv.org/pdf/2610.24161)
* **HTML 在线版本 (HTML Version)：** [arXiv HTML (实验性)](https://arxiv.org/html/2610.24161v1)
* **TeX 源码包 (TeX Source)：** [arXiv 源码归档](https://arxiv.org/src/2610.24161)
* **开源授权 (License)：** [非排他性分发协议许可](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

> * **PDF Access:** [View PDF](https://arxiv.org/pdf/2610.24161)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2610.24161v1)
> * **TeX Source:** [arXiv Source Archive](https://arxiv.org/src/2610.24161)
> * **License:** [Non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

### 引文检索与学术索引

> ### Citations and Indexes

* [Google Scholar (谷歌学术检索)](https://scholar.google.com/scholar_lookup?arxiv_id=2610.24161)
* [Semantic Scholar API (语义学人学术接口)](https://api.semanticscholar.org/arXiv:2610.24161)
* [SciX Explorer (NASA SciX 学术探索平台)](https://scixplorer.org/abs/arXiv:2610.24161)

> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.24161)
> * [Semantic Scholar API](https://api.semanticscholar.org/arXiv:2610.24161)
> * [SciX Explorer](https://scixplorer.org/abs/arXiv:2610.24161)
