---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 大语言模型
- 后训练
- 上下文对齐
- GRPO
- SFT
- DPO
title: 上下文对齐增益由预存在机制介导：GRPO、SFT与DPO的审计分析
---
### 文章背景与核心概要
大语言模型在面对与其预先记忆的知识相冲突的提示词证据时，往往会选择忽略这些证据。虽然目前广泛使用后训练方法来鼓励模型更可靠地依据证据进行生成，但一个根本性的问题依然存在：**这些性能提升究竟需要创造新的认知机制，还是仅仅强化了基础模型中已经存在的机制？**

本文通过对九种后训练技术（涵盖 **GRPO**、**SFT（监督微调）** 以及 **DPO（直接偏好优化）**）进行审计和比较，深入探讨了这一问题。研究发现，上下文对齐的增益并非源于开发新的内部能力，而是主要依赖并由基础模型中原本就内嵌的预存在机制所介导。这一发现对我们理解大语言模型在后训练阶段的内部机制演变提供了重要的实证视角。

---

# Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO

**Authors:** Prakhar Gupta, Vaibhav Gupta  
**ArXiv ID:** [arXiv:2609.00925 [cs.CL]]  
**Submitted:** September 1, 2026  
**Primary Subject:** Computation and Language (`cs.CL`)  

---

## 📌 Executive Summary

Language models often ignore prompt-provided evidence when it conflicts with their pre-existing memorized knowledge. While post-training methods are frequently used to encourage models to follow evidence more reliably, a fundamental question remains: **Do these performance gains require the creation of new cognitive machinery, or do they simply strengthen mechanisms already present in the base model?**

This paper investigates this question by auditing and comparing nine post-training techniques—spanning **GRPO**, **SFT (Supervised Fine-Tuning)**, and **DPO (Direct Preference Optimization)**—derived from a single starting checkpoint.

> ## 📌 执行摘要
> 
> 当提示词提供的证据与大语言模型预先记忆的知识发生冲突时，模型往往会忽略这些证据。尽管后训练方法经常被用于促使模型更可靠地遵循证据，但一个根本性的问题仍然存在：**这些性能增益是否需要创造全新的认知机制，还是仅仅强化了基础模型中已经存在的机制？**
> 
> 本文通过对从同一个起始检查点衍生出的九种后训练技术（涵盖 **GRPO**、**SFT（监督微调）** 和 **DPO（直接偏好优化）**）进行审计与比较，对这一问题展开了深入研究。

---

## 🔍 Key Findings & Methodology

* **GRPO Performance:** Across five tested GRPO variants, improvements in context-grounding were found to be remarkably small. For the two variants replicated across multiple random seeds, equivalence tests bounded their effectiveness *below* the gains achieved by conflict-SFT, even while their standard rewarded metrics improved.
* **SFT vs. DPO:** 
  * **Conflict-SFT** provides a moderate, stable improvement in context-grounding.
  * **DPO** drives grounding near the performance ceiling on its matched distribution.
* **Mechanistic Overlap:** Both conflict-SFT and DPO predominantly utilize the exact same causal attention-head set present in the original starting model. 
* **Intervention Experiments:**
  * Subtracting the starting model's grounding direction successfully suppresses the grounding gains of both methods.
  * Conversely, *adding* the baseline grounding direction back into the starting model recovers **35% of DPO's total gain**, using a dosage that passes all specified side-effect checks.
* **The Role of Warm Starts:** When a supervised warm start forces the correct context answer to appear more frequently during rollouts, applying the subsequent GRPO recipe yields virtually no additional grounding gains.

> ## 🔍 核心发现与方法论
> 
> * **GRPO 性能表现：** 在测试的五种 GRPO 变体中，上下文对齐的提升幅度非常小。对于在多个随机种子下进行复现的两种变体，等效性测试表明其有效性*低于*冲突 SFT（conflict-SFT）所取得的增益，尽管它们的标准奖励指标确实有所改善。
> * **SFT 与 DPO 的对比：**
>   * **冲突 SFT (Conflict-SFT)** 为上下文对齐提供了适度且稳定的改进。
>   * **DPO** 则将其在匹配分布上的对齐性能推向了接近天花板的水平。
> * **机制重合性：** 冲突 SFT 和 DPO 主要利用的都是原始起始模型中已经存在的完全相同的因果注意力头集合（causal attention-head set）。
> * **干预实验：**
>   * 减去起始模型的对齐方向可以成功抑制这两种方法的对齐增益。
>   * 相反，将基线对齐方向*重新加回*起始模型中，可以在通过所有指定的副作用检查的前提下，恢复 **DPO 总增益的 35%**。
> * **热启动的作用：** 当监督热启动强制正确的上下文答案在模型生成（rollouts）过程中更频繁地出现时，应用后续的 GRPO 配方几乎无法带来额外的对齐增益。

---

## 💡 Conclusion

The empirical evidence suggests that context-grounding gains achieved during post-training do not stem from developing novel internal capabilities. Instead, these gains largely depend on—and are mediated by—**pre-existing machinery already embedded within the starting model**.

> ## 💡 结论
> 
> 实证证据表明，后训练期间获得的上下文对齐增益并不是源于开发出新颖的内部能力。相反，这些增益很大程度上依赖于——并由——**嵌入在起始模型中的预存在机制**所介导。

---

## 🔗 Links & Resources

* **Full Text Access:** [View PDF](https://arxiv.org/pdf/2609.00925) | [HTML Version](https://arxiv.org/html/2609.00925v1) | [TeX Source](https://arxiv.org/src/2609.00925)
* **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.00925](https://doi.org/10.48550/arXiv.2609.00925)
* **License:** [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)

> ## 🔗 链接与资源
> 
> * **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.00925) | [HTML 版本](https://arxiv.org/html/2609.00925v1) | [TeX 源码](https://arxiv.org/src/2609.00925)
> * **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2609.00925](https://doi.org/10.48550/arXiv.2609.00925)
> * **许可协议：** [知识共享署名-相同方式共享 4.0 国际版](http://creativecommons.org/licenses/by-sa/4.0/)