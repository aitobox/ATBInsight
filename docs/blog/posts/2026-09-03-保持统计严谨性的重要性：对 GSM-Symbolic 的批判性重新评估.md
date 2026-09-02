---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- LLM
- 评测基准
- 统计分析
- GSM-Symbolic
- 推理能力
title: 保持统计严谨性的重要性：对 GSM-Symbolic 的批判性重新评估
---
### 文章背景与核心概要
本文批判性地重新评估了 **GSM-Symbolic 基准测试**（Mirzadeh 等人，2025年）的研究结果。此前，该研究通过测试大语言模型（LLM）在 GSM8K 问题模板生成变体上的表现下降，得出“LLM 缺乏真正的推理能力”的结论。

通过对 20 个开源模型使用带有“按问题随机效应”的自举广义线性混合模型（Bootstrapped GLMM），本文作者发现：1. 只有 **8 个模型**在原始提示格式下表现出统计学上显著的性能变化；2. 与原始 GSM8K 相比，主要的 GSM-Symbolic 数据集存在**向更大整数值系统性偏移**的问题（K-S 统计量 = 0.12，$p < 0.001$）；3. 控制这一“大数效应”后，剩余案例中有一半的显著性随之消失；4. 真正表现出性能差异的模型具有特定的失效模式（如变量绑定脆弱性、算术局限性以及双任务干扰），这证明了关于 LLM 推理能力的泛化断言既在统计学上为时尚早，在机制上也具有误导性。

---

# 保持统计严谨性的重要性：对 GSM-Symbolic 的批判性重新评估 (The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic)

## 摘要 (Summary)
> This paper critically re-evaluates the findings of the **GSM-Symbolic benchmark** (Mirzadeh et al., 2025), which previously concluded that Large Language Models (LLMs) lack genuine reasoning capabilities due to performance drops on template-generated variants of GSM8K problems. 
> 
> Using bootstrapped Generalised Linear Mixed Models with per-question random effects on 20 open-weight models, the authors show that:
> 1. Only **8 models** exhibit statistically significant performance changes under the original prompt format.
> 2. The main GSM-Symbolic dataset suffers from a **systematic shift toward larger integer values** relative to the original GSM8K (K-S statistic = 0.12, $p < 0.001$).
> 3. Controlling for this **"large-number effect"** accounts for significance in half of the remaining cases.
> 4. Models that do show true performance deltas display specific failure profiles (such as variable binding fragility, arithmetic limitations, and dual-task interference), proving that blanket claims regarding LLM reasoning are both statistically premature and mechanistically misleading.

本文批判性地重新评估了 **GSM-Symbolic 基准测试**（Mirzadeh 等人，2025年）的研究结果。此前，该研究通过观察大语言模型（LLM）在 GSM8K 问题模板生成变体上的性能下降，得出模型缺乏真正推理能力的结论。

通过对 20 个开源模型应用带有“按问题随机效应”的自举广义线性混合模型（Bootstrapped GLMM），作者得出以下结论：
1. 在原始提示格式下，只有 **8 个模型**表现出统计学上显著的性能变化。
2. 与原始的 GSM8K 相比，主要的 GSM-Symbolic 数据集存在**向更大整数值发生系统性偏移**的问题（K-S 统计量 = 0.12，$p < 0.001$）。
3. 控制这一**“大数效应”**后，剩余模型中有一半的统计显著性得以消除。
4. 真正展现出性能差异的模型表现出特定的失效轮廓（例如变量绑定脆弱性、算术局限性和双任务干扰），这证明了关于 LLM 推理能力的宽泛断言既在统计上为时尚早，在机制上也具有误导性。

---

## 文档元数据 (Document Metadata)

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [arXiv:2605.28700](https://arxiv.org/abs/2605.28700) [cs.AI] |
> | **Authors** | Dominika Agnieszka Długosz, Arlindo Oliveira, Natalia Díaz-Rodríguez |
> | **Subjects** | Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`) |
> | **Publication** | Accepted to **EMNLP 2026** (Main Conference), Track: *Resources and Evaluation* |
> | **Submission History** | v1 (27 May 2026), v2 (28 May 2026), v3 (1 Sep 2026) |
> | **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2605.28700](https://arxiv.org/abs/2605.28700) [cs.AI] |
| **作者** | Dominika Agnieszka Długosz, Arlindo Oliveira, Natalia Díaz-Rodríguez |
| **研究学科** | 人工智能 (`cs.AI`)；计算与语言 (`cs.CL`) |
| **收录情况** | 已被 **EMNLP 2026**（主会）接收，赛道：*资源与评估 (Resources and Evaluation)* |
| **提交历史** | v1 (2026年5月27日), v2 (2026年5月28日), v3 (2026年9月1日) |
| **许可证** | [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

---

## 摘要 (Abstract)

> The GSM-Symbolic benchmark (Mirzadeh et al., 2025) reported consistent performance drops across 25 Large Language Models (LLMs) when tested on template-generated variants of GSM8K problems, concluding that the models lack genuine reasoning capabilities. We argue that this conclusion rests on shaky statistical ground. Re-evaluating 20 open-weight models using bootstrapped Generalised Linear Mixed Models with per-question random effects, we find that only 8 exhibit statistically significant performance changes under the original prompt format. Moreover, we identify a previously unacknowledged factor: the distribution of integers in problem texts of the main GSM-Symbolic dataset is systematically shifted towards larger values relative to the original GSM8K (K-S statistic = 0.12, $p < 0.001$), contradicting the original authors' claims. Controlling for this large-number effect accounts for significance in half of the remaining cases. Among models with statistically significant performance deltas, we identify distinct, model-specific behavioural failure profiles — including fragility of variable binding, arithmetic limitations, and dual-task interference — underscoring that blanket claims about LLM reasoning risk being both statistically premature and mechanistically misleading.

GSM-Symbolic 基准测试（Mirzadeh 等人，2025年）指出，当 25 个大语言模型（LLM）在 GSM8K 问题的模板生成变体上进行测试时，其性能均出现了持续下降，并由此得出结论：这些模型缺乏真正的推理能力。我们认为，这一结论建立在站不住脚的统计基础之上。通过使用带有“按问题随机效应”的自举广义线性混合模型（Bootstrapped GLMM）对 20 个开源模型进行重新评估，我们发现只有 8 个模型在原始提示格式下表现出统计学上显著的性能变化。此外，我们发现了一个此前未被认识到的因素：与原始的 GSM8K 相比，主要的 GSM-Symbolic 数据集中问题文本里的整数分布系统性地向更大数值发生偏移（K-S 统计量 = 0.12，$p < 0.001$），这与原作者的说法相矛盾。控制这一“大数效应”后，剩余案例中有一半的显著性得以消除。在具有统计显著性性能差异的模型中，我们识别出了独特且因模型而异的行为失效轮廓——包括变量绑定脆弱性、算术局限性以及双任务干扰——这强调了关于 LLM 推理能力的泛化断言既存在统计上为时尚早的风险，在机制上也具有误导性。

---

## 链接与资源 (Links and Resources)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2605.28700)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2605.28700v3)
>   * [TeX Source](https://arxiv.org/src/2605.28700)
> * **External Citations & Indexing:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2605.28700)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.28700)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.28700)

* **全文选项：** 
  * [查看 PDF](https://arxiv.org/pdf/2605.28700)
  * [HTML 版本（实验性）](https://arxiv.org/html/2605.28700v3)
  * [TeX 源码](https://arxiv.org/src/2605.28700)
* **外部引用与索引：** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2605.28700)
  * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2605.28700)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.28700)