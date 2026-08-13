---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- Triton
- 大语言模型
- 评测基准
- 深度学习编译
- 软件工程
title: RealisticTritonBench：真实世界 AI 框架中 Triton 内核生成的评测基准
---
### 文章背景与核心概要
随着大语言模型（LLM）在代码生成领域的迅猛发展，自动生成兼具易用性、可移植性与高性能的 GPU 内核（如 OpenAI Triton）成为了研究热点。然而，现有的评测基准往往局限于简单的 PyTorch 到 Triton 转换任务、孤立的内核性能评估，且高度依赖容易被模型钻空子的手写评估脚本，难以反映真实工业级场景下的挑战。

为此，本文介绍了 RealisticTritonBench——首个专为真实世界生产级 AI 框架中的 Triton 内核生成而设计的评测基准。该基准直接提取自流行开源 AI 框架中修改 Triton 内核真实 Pull Request（PR），通过将生成的内核重新集成回原生框架，并借助端到端测试环境进行严格评估。对顶尖 LLM 的全面评测表明，目前的先进大模型在处理实际生产环境中的 Triton 内核生成时仍面临巨大挑战。

---

# RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks

> **RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks**

**arXiv:** [2608.12004](https://arxiv.org/abs/2608.12004) [cs.SE]  
**Accepted by:** ASE 2026  
**Submitted:** August 12, 2026  
**Authors:** Jinjun Huang, Zhongzhen Wen, Tongtong Xu, Meng Yan, Xin Xia, Zhongxin Liu  

> **arXiv:** [2608.12004](https://arxiv.org/abs/2608.12004) [cs.SE]  
> **Accepted by:** ASE 2026  
> **Submitted:** August 12, 2026  
> **Authors:** Jinjun Huang, Zhongzhen Wen, Tongtong Xu, Meng Yan, Xin Xia, Zhongxin Liu  

---

## 📌 Summary

> ## 📌 Summary

**RealisticTritonBench** is a novel evaluation benchmark designed to test Large Language Models (LLMs) on generating Triton kernels within realistic, production-grade AI frameworks. 

> **RealisticTritonBench** is a novel evaluation benchmark designed to test Large Language Models (LLMs) on generating Triton kernels within realistic, production-grade AI frameworks. 

While LLMs show promise in automatically generating Triton kernels (GPU kernels combining usability, portability, and near-handwritten CUDA performance), existing benchmarks suffer from three major limitations:
1. They restrict tasks to simple PyTorch-to-Triton translations, missing real-world complexity.
2. They evaluate isolated kernel performance rather than end-to-end framework performance.
3. They rely on flawed, manually written evaluation scripts that models can bypass to achieve inflated scores.

> While LLMs show promise in automatically generating Triton kernels (GPU kernels combining usability, portability, and near-handwritten CUDA performance), existing benchmarks suffer from three major limitations:
> 1. They restrict tasks to simple PyTorch-to-Triton translations, missing real-world complexity.
> 2. They evaluate isolated kernel performance rather than end-to-end framework performance.
> 3. They rely on flawed, manually written evaluation scripts that models can bypass to achieve inflated scores.

To solve this, RealisticTritonBench derives its tasks directly from real pull requests (PRs) in popular open-source AI frameworks that modify Triton kernels. It integrates generated kernels back into their original frameworks and evaluates them using comprehensive end-to-end testing environments. Evaluations of leading LLMs on this benchmark reveal that state-of-the-art models still struggle significantly with real-world Triton kernel generation.

> To solve this, RealisticTritonBench derives its tasks directly from real pull requests (PRs) in popular open-source AI frameworks that modify Triton kernels. It integrates generated kernels back into their original frameworks and evaluates them using comprehensive end-to-end testing environments. Evaluations of leading LLMs on this benchmark reveal that state-of-the-art models still struggle significantly with real-world Triton kernel generation.

---

## 🔗 Links & Resources

> ## 🔗 Links & Resources

* **View PDF:** [arXiv:2608.12004 PDF](https://arxiv.org/pdf/2608.12004)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.12004v1)
* **TeX Source:** [arXiv Source](https://src/2608.12004)
* **DOI:** [10.48550/arXiv.2608.12004](https://doi.org/10.48550/arXiv.2608.12004)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> * **View PDF:** [arXiv:2608.12004 PDF](https://arxiv.org/pdf/2608.12004)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.12004v1)
> * **TeX Source:** [arXiv Source](https://src/2608.12004)
> * **DOI:** [10.48550/arXiv.2608.12004](https://doi.org/10.48550/arXiv.2608.12004)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 📋 Additional Metadata

> ## 📋 Additional Metadata

* **Primary Subject:** Software Engineering (`cs.SE`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
* **Citation Tools:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.12004)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.12004)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.12004)

> * **Primary Subject:** Software Engineering (`cs.SE`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **Citation Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.12004)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.12004)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.12004)