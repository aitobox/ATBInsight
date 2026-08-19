---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 大语言模型
- 语义表征
- 激活空间
- 真值探测
- Gemma 3
title: 人工智能语言表征中：虚假（Falsehood）与不可能（Impossibility）指向不同的方向
---
### 文章背景与核心概要
语言使我们能够描述事实上的错误状态（虚假）以及根本不可能发生的状态（不可能）。本研究探讨了现代人工智能模型在内部是否区分这两种不同类型的语义失效。

研究人员以开源模型 Gemma 3 4B IT 为对象，在一系列哲学和主题匹配的提示词上进行了探索性激活研究。核心发现揭示了模型显式文本输出与其内部神经表征之间存在着有趣的脱节：在输出层面，模型常将偶然谬误误判为矛盾；但在激活层面，模型内部保持了清晰的区分，真值探测器与不可能探测器各自指向不同的几何维度，且不可能方向与语义异常方向部分重叠但又可被区分。该研究表明，在模型的激活空间中，必然谬误并非普通谬误的极端情况，而是更贴近语义异常。

---

## 📌 Summary

Language allows us to describe both *false* states of affairs (things that are factually incorrect) and *impossible* states of affairs (things that could not possibly be the case). This study investigates whether modern AI models internally differentiate these two types of semantic failure. 

> Language allows us to describe both *false* states of affairs (things that are factually incorrect) and *impossible* states of affairs (things that could not possibly be the case). This study investigates whether modern AI models internally differentiate these two types of semantic failure. 

Using the open-weight model **Gemma 3 4B IT**, the author conducted an exploratory activation study across various philosophical and topic-matched prompts. The key findings reveal a fascinating disconnect between the model's explicit textual outputs and its internal neural representations:
* **The Output Level (Conflation):** When asked to evaluate false statements, the model frequently labels contingent falsehoods as "contradictions" (e.g., mislabeling 12 out of 15 false statements).
* **The Activation Level (Differentiation):** Internally, the model maintains a sharp distinction. 
    * A linear truth probe successfully separates impossible statements from true ones ($\text{AUC } 0.93$), but fails to separate impossible from false ones ($\text{AUC } 0.20$).
    * An impossibility probe cleanly separates necessary falsehoods from contingent falsehoods ($\text{AUC } 1.00$, peaking at layer 15 with $0.97$ balanced accuracy).
* **Geometric Relationships:** The directions for *truth* and *impossibility* are nearly orthogonal. Meanwhile, the *impossibility* direction partially overlaps with—yet remains distinguishable from—*semantic anomaly* directions (as seen in sparse autoencoder features).

> Using the open-weight model **Gemma 3 4B IT**, the author conducted an exploratory activation study across various philosophical and topic-matched prompts. The key findings reveal a fascinating disconnect between the model's explicit textual outputs and its internal neural representations:
> * **The Output Level (Conflation):** When asked to evaluate false statements, the model frequently labels contingent falsehoods as "contradictions" (e.g., mislabeling 12 out of 15 false statements).
> * **The Activation Level (Differentiation):** Internally, the model maintains a sharp distinction. 
>     * A linear truth probe successfully separates impossible statements from true ones ($\text{AUC } 0.93$), but fails to separate impossible from false ones ($\text{AUC } 0.20$).
>     * An impossibility probe cleanly separates necessary falsehoods from contingent falsehoods ($\text{AUC } 1.00$, peaking at layer 15 with $0.97$ balanced accuracy).
> * **Geometric Relationships:** The directions for *truth* and *impossibility* are nearly orthogonal. Meanwhile, the *impossibility* direction partially overlaps with—yet remains distinguishable from—*semantic anomaly* directions (as seen in sparse autoencoder features).

Ultimately, the study suggests that within the model's activation space, necessary falsehoods are not merely extreme cases of regular falsehoods, but align more closely with semantic anomalies.

> Ultimately, the study suggests that within the model's activation space, necessary falsehoods are not merely extreme cases of regular falsehoods, but align more closely with semantic anomalies.

---

## 🔗 Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.12852) | [HTML Version](https://arxiv.org/html/2608.12852v2)
* **Cite as:** `arXiv:2608.12852 [cs.CL]` — [DOI](https://doi.org/10.48550/arXiv.2608.12852)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.12852) | [HTML Version](https://arxiv.org/html/2608.12852v2)
> * **Cite as:** `arXiv:2608.12852 [cs.CL]` — [DOI](https://doi.org/10.48550/arXiv.2608.12852)