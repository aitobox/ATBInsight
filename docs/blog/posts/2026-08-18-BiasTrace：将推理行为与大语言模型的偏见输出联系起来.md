---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- 大语言模型
- 社会偏见
- 推理过程
- 偏见检测
- 模型缓解
title: BiasTrace：将推理行为与大语言模型的偏见输出联系起来
---
### 文章背景与核心概要
大语言模型（LLM）在实际应用中常常表现出社会偏见，这会在高风险场景中引发不准确和歧视性的推理结果。以往的研究主要将模型视为“黑盒”，聚焦于最终输出的测量与缓解，而对产生这些偏见结果的内部机制缺乏深入理解。本文介绍了名为 **BiasTrace** 的新型注释方案，旨在标记模型生成过程中的特定推理行为（如无根据的人口统计学假设或“过度思考”），并将其与歧视性推论直接挂钩。

通过在对偏见敏感的语境中应用 BiasTrace 框架并利用验证过的大模型裁判（LLM-as-a-judge）方法进行扩展，作者构建了一个大型标注数据集。研究表明，偏见输出往往源于隐蔽的推理行为，而非显式的偏见语言；此外，基于推理层面的注释能显著提升偏见检测的效果，并可用于有效的推理时缓解策略。该研究凸显了检查更广泛的推理模式对于理解和治理 LLM 偏见的重要价值。

---

## Summary
*BiasTrace* addresses the critical challenge of social bias in Large Language Models (LLMs) by shifting the focus from final outputs to the underlying reasoning processes. While existing research often treats models as "black boxes" that produce biased results, this paper introduces an annotation scheme designed to label specific reasoning behaviors—such as unsupported demographic assumptions or "overthinking"—that lead to discriminatory inferences. By applying this framework to bias-sensitive contexts, the authors demonstrate that biased outputs are frequently the result of subtle reasoning patterns rather than explicit language. Furthermore, the study shows that these reasoning-level annotations significantly improve bias detection and can be leveraged for effective inference-time mitigation.

> *BiasTrace* addresses the critical challenge of social bias in Large Language Models (LLMs) by shifting the focus from final outputs to the underlying reasoning processes. While existing research often treats models as "black boxes" that produce biased results, this paper introduces an annotation scheme designed to label specific reasoning behaviors—such as unsupported demographic assumptions or "overthinking"—that lead to discriminatory inferences. By applying this framework to bias-sensitive contexts, the authors demonstrate that biased outputs are frequently the result of subtle reasoning patterns rather than explicit language. Furthermore, the study shows that these reasoning-level annotations significantly improve bias detection and can be leveraged for effective inference-time mitigation.

---

## Abstract
LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. 

> LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. 

Recent advances in LLM reasoning offer a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on final answer correctness or explicitly biased language, overlooking different behaviours in reasoning that can drive biased outcomes. We introduce **BiasTrace**, an annotation scheme for labelling reasoning behaviours in model-generated traces and linking them to biased outcomes. BiasTrace captures bias-specific behaviours (e.g., unsupported demographic assumptions) as well as general reasoning patterns that may implicitly contribute to bias (e.g., overthinking). 

> Recent advances in LLM reasoning offer a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on final answer correctness or explicitly biased language, overlooking different behaviours in reasoning that can drive biased outcomes. We introduce **BiasTrace**, an annotation scheme for labelling reasoning behaviours in model-generated traces and linking them to biased outcomes. BiasTrace captures bias-specific behaviours (e.g., unsupported demographic assumptions) as well as general reasoning patterns that may implicitly contribute to bias (e.g., overthinking). 

We apply BiasTrace to reasoning traces in bias-sensitive contexts, scaled using validated LLM-as-a-judge methods, producing a large annotated dataset. Our analysis shows that biased outputs often stem from subtle reasoning behaviours rather than explicitly biased language, and that reasoning-level annotations improve bias detection. We further show that BiasTrace behaviours can be exploited for inference-time mitigation. These findings underscore the importance of examining a broader range of reasoning patterns to better understand bias in LLMs.

> We apply BiasTrace to reasoning traces in bias-sensitive contexts, scaled using validated LLM-as-a-judge methods, producing a large annotated dataset. Our analysis shows that biased outputs often stem from subtle reasoning behaviours rather than explicitly biased language, and that reasoning-level annotations improve bias detection. We further show that BiasTrace behaviours can be exploited for inference-time mitigation. These findings underscore the importance of examining a broader range of reasoning patterns to better understand bias in LLMs.

---

## Access Paper
*   **[View PDF](https://arxiv.org/pdf/2608.14161)**
*   **[HTML (Experimental)](https://arxiv.org/html/2608.14161v1)**
*   **[TeX Source](https://arxiv.org/src/2608.14161)**

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## Metadata
*   **Primary Subject:** Artificial Intelligence (cs.AI)
*   **DOI:** [https://doi.org/10.48550/arXiv.2608.14161](https://doi.org/10.48550/arXiv.2608.14161)
*   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)