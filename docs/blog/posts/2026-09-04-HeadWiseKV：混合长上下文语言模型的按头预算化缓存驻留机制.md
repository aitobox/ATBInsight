---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- KV Cache
- 长上下文
- 大语言模型
- 内存优化
- 混合架构
title: HeadWiseKV：混合长上下文语言模型的按头预算化缓存驻留机制
---
### 文章背景与核心概要
随着大语言模型（LLM）长上下文推理的普及，不断增长的键值（KV）缓存（KV Cache）成为了主要的性能瓶颈，不仅消耗大量的 GPU 内存，还限制了生成吞吐量。尽管现代混合架构大模型（Hybrid LLMs）采用了局部、循环或线性注意力等设计，但其残余的全局注意力层（Residual Global-Attention Layers）仍然占据了极高的上下文相关缓存需求。

为了解决这一问题，本文作者提出了 **HeadWiseKV**，这是一个无需训练（training-free）的框架，旨在压缩混合模型中的残余全局 KV 缓存，同时保持其原生的局部、循环和线性路径不受影响。该技术的核心亮点包括：通过为每个物理 KV 头分配静态的多级历史窗口来实现可预测的缓存分配；提出 SeqCalib 算法，将分配挑战建模为一个受限的操作率失真问题，并采用感知深度的策略生成方法；实现分组缓存运行时（Grouped-Cache Runtime），将策略直接实体化为实际的按头 KV 驻留。实验表明，HeadWiseKV 在保持 RULER 和 LoCoMo 基准测试中接近 Full-KV 质量的同时，在 112K 上下文长度下将采样峰值设备内存减少了 **8.59%**，并将 Qwen3.6-27B 模型上成功验证的最大上下文从 **114K 延长至 161K**。

---

## # HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models

**arXiv:** [2609.02029](https://arxiv.org/abs/2609.02029) [cs.AI]  
**Submitted on:** 2 September 2026  
**Authors:** Renjie Xie, Juncheng Yang, Aoting Hu, Mingxi Zhang, Liyao Wu, Zheheng Hong, Wei Xu  

---

## 📋 摘要与核心亮点

长上下文语言模型推理在解码过程中会保留不断增长的键值（KV）缓存，这会消耗大量的 GPU 内存并降低生成吞吐量。在混合语言模型中，由于其残余的全局注意力层主导了与上下文相关的缓存需求，这一瓶颈依然存在。

为了解决这个问题，作者引入了 **HeadWiseKV**，这是一个无需训练的框架，旨在压缩混合语言模型的残余全局 KV 缓存，同时保留其原生的局部、循环和线性路径。主要亮点包括：
* **可预测的缓存分配：** 为每个物理 KV 头分配一个静态的多级历史窗口，确保在服务前缓存需求可预测。
* **SeqCalib 算法：** 将分配挑战建模为一个受限的操作率失真（operational rate–distortion）问题，利用考虑底层策略部署交互的深度感知策略生成方法。
* **分组缓存运行时：** 将策略实现为实际的按头 KV 驻留，而不是依赖于完整缓存之上的掩码（masks）。
* **性能表现：** 在 RULER 和 LoCoMo 基准测试中保持了接近 Full-KV 的质量，同时在 112K 上下文长度下将采样的峰值设备内存减少了 **8.59%**，并在 Qwen3.6-27B 上将成功验证的上下文长度从 **114K 扩展到 161K**。

> Long-context language model inference often suffers from a growing key–value (KV) cache bottleneck, consuming substantial GPU memory and limiting generation throughput. This issue persists in hybrid language models because their residual global-attention layers dictate high context-dependent cache demand. 
> 
> To address this, the authors introduce **HeadWiseKV**, a training-free framework designed to compress residual global KV caches in hybrid models while leaving their native local, recurrent, and linear paths untouched. Key highlights include:
> * **Predictable Cache Allocation:** Assigns each physical KV head a static, multilevel history window to ensure predictable cache demand prior to serving.
> * **SeqCalib Algorithm:** Frames the allocation challenge as a restricted operational rate–distortion problem, utilizing depth-aware policy generation that factors in lower-layer policy deployment interactions.
> * **Grouped-Cache Runtime:** Materializes policies as actual per-head KV residency rather than relying on masks over a full cache.
> * **Performance:** Maintains near-Full-KV quality across RULER and LoCoMo benchmarks while reducing sampled peak device memory by **8.59%** at a 112K context length and extending successful context verification from **114K to 161K** on Qwen3.6-27B.

---

## 📄 摘要原文

> 长上下文推理在解码过程中保留了一个不断增长的键值（KV）缓存，这消耗了大量的 GPU 内存并可能降低生成吞吐量。由于混合语言模型的残余全局注意力层会主导上下文相关的缓存需求，这一瓶颈在混合语言模型中依然存在。我们研究了如何在总 KV 驻留预算下分配该状态。我们引入了 HeadWiseKV，这是一个无需训练的框架，它压缩了混合语言模型的残余全局 KV 缓存，同时保留了其原生的局部、循环和线性路径。它为每个物理 KV 头分配了一个静态的多级历史窗口，使缓存需求在服务前变得可预测。我们将这种分配建模为一个受限的操作率失真问题，并提出 SeqCalib 作为 HeadWiseKV 中的核心策略生成算法。SeqCalib 按执行顺序处理各层，并将每个决策条件化于部署时使用的底层策略，从而考虑到跨深度的交互。分组缓存运行时将选定的策略实现为实际的按头 KV 驻留，而不是对完整缓存使用掩码。我们在四个混合长上下文模型上评估了下游质量，并在 Qwen3.6-27B 上研究了物理驻留和推理行为。HeadWiseKV 在所有评估的模型中保持了接近 Full-KV 的 RULER 和 LoCoMo 质量。在固定模型系统研究中，它在 112K 上下文长度下将采样的峰值设备内存减少了 8.59%，并将最大验证成功的上下文从 114K 延长至 161K。

> Long-context inference retains a growing key–value (KV) cache during decoding, which consumes substantial GPU memory and can reduce generation throughput. This bottleneck remains in hybrid language models because their residual global-attention layers can dominate context-dependent cache demand. We study how to allocate this state under an aggregate KV-residency budget. We introduce HeadWiseKV, a training-free framework that compresses the residual global KV caches of hybrid language models while preserving their native local, recurrent, and linear paths. It assigns each physical KV head a static, multilevel history window, making cache demand predictable before serving. We formulate this allocation as a restricted operational rate–distortion problem and propose SeqCalib as the core policy-generation algorithm in HeadWiseKV. SeqCalib processes layers in execution order and conditions each decision on the lower-layer policy used at deployment, thereby accounting for interactions across depth. A grouped-cache runtime materializes the selected policy as actual per-head KV residency rather than a mask over a full cache. We evaluate downstream quality across four hybrid long-context models and study physical residency and serving behavior on Qwen3.6-27B. HeadWiseKV retains near-Full-KV RULER and LoCoMo quality across the evaluated models. In the fixed-model systems study, it reduces sampled peak device memory by 8.59\% at a 112K context length and extends the largest verified successful context from 114K to 161K.

---

## 🔗 附加链接与资源

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.02029) | [HTML（实验性）](https://arxiv.org/html/2609.02029v1) | [TeX 源码](https://arxiv.org/src/2609.02029)
* **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2609.02029](https://doi.org/10.48550/arXiv.2609.02029)
* **外部引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.02029) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.02029) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.02029)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.02029) | [HTML (Experimental)](https://arxiv.org/html/2609.02029v1) | [TeX Source](https://arxiv.org/src/2609.02029)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.02029](https://doi.org/10.48550/arXiv.2609.02029)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.02029) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.02029) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.02029)