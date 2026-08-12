---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- Transformers
- 大语言模型
- 内部世界模型
- 河内塔
- 可解释性AI
title: Transformer 难以利用其涌现的世界模型：重探河内塔与思考的错觉
---
### 文章背景与核心概要

河内塔（Tower of Hanoi）是一个经典的规划谜题，长期以来一直在挑战各大推理模型（LRMs）。尽管当前的模型能够轻松处理标准格式，但它们在“平面到平面”（flat-to-flat）变体（即初始状态和目标状态不限于将所有圆环堆叠在单一柱子上）上面临巨大挑战。本文深入研究了小型自研 Transformer 与前沿大模型如何解决该任务，揭示了模型内部确实形成了线性可解码、几何保真的状态空间（谢尔宾斯基三角形）表征，但大模型在长链条推理过程中存在“构建了世界模型却又将其丢失”的维护失效问题。

这项研究挑战了“大模型缺乏内部逻辑推理能力”的传统认知，将其重新定义为一个动态的表征维护问题。通过将提示词阶段的表征注入回推理过程，可以部分恢复模型性能，这为未来改善大模型的长程规划和推理能力提供了全新的优化方向。

---

# Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking

**Authors:** Devin Pereira, Willem Zuidema  
**Published:** August 7, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [2608.07077](https://arxiv.org/abs/2608.07077)  
**DOI:** [10.48550/arXiv.2608.07077](https://doi.org/10.48550/arXiv.2608.07077)  

> # Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking
> 
> **Authors:** Devin Pereira, Willem Zuidema  
> **Published:** August 7, 2026  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> **arXiv ID:** [2608.07077](https://arxiv.org/abs/2608.07077)  
> **DOI:** [10.48550/arXiv.2608.07077](https://doi.org/10.48550/arXiv.2608.07077)  

---

## 📌 Summary

The **Tower of Hanoi** is a classic planning puzzle that continues to challenge Large Reasoning Models (LRMs). While current models easily handle standard formulations, they struggle significantly with the *flat-to-flat* variant (where initial and goal states are not restricted to stacking all rings on a single peg). 

This paper investigates how both small in-house Transformers and large third-party LRMs solve this task:
1. **Small Transformers:** Using interpretability techniques on models trained from scratch, the authors reveal an **emergent world model**—a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle) that causally drives problem-solving.
2. **Frontier Large Language Models:** Evaluating models like `Qwen3.6-27B` and `DeepSeek-R1-Distill-Qwen-32B` using extended chains-of-thought, the researchers found that these models encode the same Sierpinski world model near-perfectly early on, yet fail on the majority of tasks when scaling past 3 rings.

**Core Finding:** The failure of large models is **not** an absence of an internal world model, but rather a **failure to maintain it** over the course of extended reasoning. Injecting the prompt-time representation back into inference partially restores performance, reframing the perceived "collapse in reasoning" as a maintenance issue: **current LRMs build a world model, and then lose it.**

> ## 📌 Summary
> 
> The **Tower of Hanoi** is a classic planning puzzle that continues to challenge Large Reasoning Models (LRMs). While current models easily handle standard formulations, they struggle significantly with the *flat-to-flat* variant (where initial and goal states are not restricted to stacking all rings on a single peg). 
> 
> This paper investigates how both small in-house Transformers and large third-party LRMs solve this task:
> 1. **Small Transformers:** Using interpretability techniques on models trained from scratch, the authors reveal an **emergent world model**—a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle) that causally drives problem-solving.
> 2. **Frontier Large Language Models:** Evaluating models like `Qwen3.6-27B` and `DeepSeek-R1-Distill-Qwen-32B` using extended chains-of-thought, the researchers found that these models encode the same Sierpinski world model near-perfectly early on, yet fail on the majority of tasks when scaling past 3 rings.
> 
> **Core Finding:** The failure of large models is **not** an absence of an internal world model, but rather a **failure to maintain it** over the course of extended reasoning. Injecting the prompt-time representation back into inference partially restores performance, reframing the perceived "collapse in reasoning" as a maintenance issue: **current LRMs build a world model, and then lose it.**

---

## 📋 Metadata

* **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.07077) | [HTML (Experimental)](https://arxiv.org/html/2608.07077v1) | [TeX Source](https://arxiv.org/src/2608.07077)
* **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/) <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" width="16" style="vertical-align: middle; margin-left: 4px;" />
* **External Resources:** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07077)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07077)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07077)

> ## 📋 Metadata
> 
> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.07077) | [HTML (Experimental)](https://arxiv.org/html/2608.07077v1) | [TeX Source](https://arxiv.org/src/2608.07077)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/) <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" width="16" style="vertical-align: middle; margin-left: 4px;" />
> * **External Resources:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07077)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07077)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07077)