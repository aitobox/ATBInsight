---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 自动驾驶
- 视觉语言模型
- 模型评估
- nuScenes
- 人工智能
title: LightEMMA：视觉语言模型自动驾驶能力的纵向评估
---
### 文章背景与核心概要
近年来，视觉语言模型（VLMs）在自动驾驶领域的应用引起了广泛关注。行业内普遍存在一种假设，即随着VLM迭代升级，其驾驶性能将不断提升，并最终超越现有的最先进方法。为了系统性地检验这一假设，密歇根交通实验室等机构的研究人员推出了 LightEMMA——一个用于评估VLM自动驾驶性能的纵向评估框架。

LightEMMA 采用轻量级、统一的评估协议，在不进行特定模型微调、架构修改或提示词工程的情况下，直接评估各个模型的内在驾驶能力。基于该协议，研究团队对来自5个主要模型家族的15款模型在具有挑战性的 nuScenes 预测基准上进行了全面评估。其实验结果打破了“代际升级必然带来驾驶性能提升”的常规认知，揭示了VLM在应对复杂交通场景时的固有缺陷，为未来构建安全可靠的VLM自动驾驶系统指明了方向。

---

# LightEMMA: A Longitudinal Evaluation of Vision-Language Models for Autonomous Driving

> # LightEMMA: A Longitudinal Evaluation of Vision-Language Models for Autonomous Driving

## Summary
* **Authors:** Zhijie Qiao, Haowei Li, Zhong Cao, Henry X. Liu
* **Subjects:** Robotics (`cs.RO`), Artificial Intelligence (`cs.AI`)
* **Identifiers:** arXiv:2505.00284 [cs.RO] | DOI: [10.48550/arXiv.2505.00284](https://doi.org/10.48550/arXiv.2505.00284)
* **Submission History:** 
  * [v1] Thu, 1 May 2025
  * [v2] Sat, 13 Sep 2025
  * [v3] Wed, 2 Sep 2026 *(Current Version)*
* **Resources:** [View PDF](https://arxiv.org/pdf/2505.00284) | [HTML Version](https://arxiv.org/html/2505.00284v3) | [Source Code (GitHub)](https://github.com/michigan-traffic-lab/LightEMMA)

> ## Summary
> * **Authors:** Zhijie Qiao, Haowei Li, Zhong Cao, Henry X. Liu
> * **Subjects:** Robotics (`cs.RO`), Artificial Intelligence (`cs.AI`)
> * **Identifiers:** arXiv:2505.00284 [cs.RO] | DOI: [10.48550/arXiv.2505.00284](https://doi.org/10.48550/arXiv.2505.00284)
> * **Submission History:** 
>   * [v1] Thu, 1 May 2025
>   * [v2] Sat, 13 Sep 2025
>   * [v3] Wed, 2 Sep 2026 *(Current Version)*
> * **Resources:** [View PDF](https://arxiv.org/pdf/2505.00284) | [HTML Version](https://arxiv.org/html/2505.00284v3) | [Source Code (GitHub)](https://github.com/michigan-traffic-lab/LightEMMA)

---

## Abstract
Rapid advances in vision-language models (VLMs) have generated growing interest in their application to autonomous driving. A prevailing assumption is that successive VLM generations will continually improve driving performance and eventually outperform state-of-the-art methods. To systematically examine this assumption, we introduce **LightEMMA**, a longitudinal framework for evaluating the autonomous driving performance of VLMs. 

LightEMMA uses a lightweight, unified evaluation protocol that assesses each model's intrinsic driving capability without model-specific fine-tuning, architectural changes, or prompt engineering. Using this protocol, we evaluate 15 models from five major families on the challenging nuScenes prediction benchmark. 

Empirical findings show that, despite increased model scale and enhanced general reasoning capabilities, successive VLM generations do not consistently achieve better driving performance. Further analysis of driving scenarios reveals recurring failure modes, including overreliance on historical actions and difficulty reconciling conflicting visual cues. These findings highlight the need for domain-specific adaptation to improve the safety of VLM-based autonomous driving systems.

> ## Abstract
> Rapid advances in vision-language models (VLMs) have generated growing interest in their application to autonomous driving. A prevailing assumption is that successive VLM generations will continually improve driving performance and eventually outperform state-of-the-art methods. To systematically examine this assumption, we introduce **LightEMMA**, a longitudinal framework for evaluating the autonomous driving performance of VLMs. 
> 
> LightEMMA uses a lightweight, unified evaluation protocol that assesses each model's intrinsic driving capability without model-specific fine-tuning, architectural changes, or prompt engineering. Using this protocol, we evaluate 15 models from five major families on the challenging nuScenes prediction benchmark. 
> 
> Empirical findings show that, despite increased model scale and enhanced general reasoning capabilities, successive VLM generations do not consistently achieve better driving performance. Further analysis of driving scenarios reveals recurring failure modes, including overreliance on historical actions and difficulty reconciling conflicting visual cues. These findings highlight the need for domain-specific adaptation to improve the safety of VLM-based autonomous driving systems.

---

## Access Paper & Extra Links

* **Full-Text Access:** 
  * [View PDF](https://arxiv.org/pdf/2505.00284)
  * [HTML (experimental)](https://arxiv.org/html/2505.00284v3)
  * [TeX Source](https://arxiv.org/src/2505.00284)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="20" style="vertical-align: middle; margin-left: 4px;" />
* **Citations & References:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2505.00284)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2505.00284)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2505.00284)

> ## Access Paper & Extra Links
> 
> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2505.00284)
>   * [HTML (experimental)](https://arxiv.org/html/2505.00284v3)
>   * [TeX Source](https://arxiv.org/src/2505.00284)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="20" style="vertical-align: middle; margin-left: 4px;" />
> * **Citations & References:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2505.00284)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2505.00284)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2505.00284)