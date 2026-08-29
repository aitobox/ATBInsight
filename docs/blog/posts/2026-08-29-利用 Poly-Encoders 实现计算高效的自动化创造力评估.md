---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- Poly-Encoders
- 创造力评估
- 自然语言处理
- 教育技术
- BERT
title: 利用 Poly-Encoders 实现计算高效的自动化创造力评估
---
### 文章背景与核心概要

自动化创造力评估长期以来面临着资源消耗巨大与评估准确性不足之间的矛盾。传统方法往往依赖于庞大的大型语言模型（LLM），这限制了其在资源受限环境下的应用，而简单的启发式方法又难以达到人类评估的精度。

本文提出了一种基于 Poly-Encoders 的创新方法，旨在平衡评估精度与计算效率。研究者利用包含约 18,000 条人类评分的《科学创造性思维测试》数据集对 Poly-Encoder 进行了微调。实验结果表明，该方法在保持与大型语言模型相当的性能（皮尔逊相关系数高达 $r = 0.74$）的同时，显著降低了计算需求。这一成果为在消费级硬件上实现大规模、自动化的创造力评估提供了切实可行的路径，特别是在教育评估场景中具有重要的应用价值。

---

# 利用 Poly-Encoders 实现计算高效的自动化创造力评估

## 摘要

> This paper introduces a novel approach to automated creativity assessment utilizing **Poly-Encoders**, bridging the gap between high evaluation accuracy and computational efficiency. Traditionally, automated creativity assessment relied on resource-intensive Large Language Models (LLMs) or simplistic methods lacking practical accuracy. 
>
> The authors fine-tuned a Poly-Encoder—leveraging small pre-trained BERT-family encoders—on a public dataset containing approximately 18,000 human-rated question responses from the *Scientific Creative Thinking Test*. The proposed method achieved performance comparable to heavy LLMs, registering Pearson correlations of up to **$r = 0.74$ (95% CI $[0.73, 0.75]$)** with human raters. This efficiency significantly lowers computational demands, making scalable, automated creativity assessment viable on consumer-grade hardware, particularly within educational contexts.

## 论文元数据

* **arXiv ID:** [arXiv:2608.26165](https://arxiv.org/abs/2608.26165) [cs.CL]
* **作者:** Sam Grouchnikov, Phillip Gregory, Jiho Noh
* **提交日期:** 2026年7月13日
* **收录会议:** AIED 2026 (DOI: [10.1007/978-3-032-29755-6_32](https://doi.org/10.1007/978-3-032-29755-6_32))
* **主要学科:** 计算与语言 (`cs.CL`)
* **次要学科:** 人工智能 (`cs.AI`)

## 论文摘要

> Automated creativity assessment has been a long standing challenge, with traditional methods often being resource intensive or lacking practical accuracy. We introduce a novel approach by using Poly-Encoder for computationally efficient and accurate automated creativity assessment. We fine-tuned a Poly-Encoder on a public dataset from the Scientific Creative Thinking Test, comprised of approximately 18,000 human-rated question responses. Our method leverages small pre-trained BERT encoders, achieving performance comparable to fine-tuned Large Language Models while significantly reducing computational demands. Experiments with the BERT-family models and poly-code counts achieved Pearson correlations of up to $r = 0.74$, 95% CI $[0.73, 0.75]$ with human raters, matching the performance of resource intensive LLMs. This study bridges the gap between high performance and computational efficiency, potentially enabling widespread implementation of automated creativity assessment on accessible consumer-grade hardware. With some limitations, our findings suggest that Poly-Encoders are a promising alternative to LLMs for practical, scalable creativity assessment in various contexts, especially educational.

## 访问链接与资源

* **全文:** [查看 PDF](https://arxiv.org/pdf/2608.26165) | [HTML (实验性)](https://arxiv.org/html/2608.26165v1) | [TeX 源码](https://arxiv.org/src/2608.26165)
* **外部索引:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26165)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26165)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26165)