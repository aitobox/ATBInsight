---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- 大语言模型
- 自我进化智能体
- 技能库维护
- Ratchet框架
- 算法可靠性
title: Ratchet：LLM裁判需要多高的可靠性才能淘汰一项技能？
---
### 文章背景与核心概要

随着大语言模型（LLM）智能体开始自主编写和精炼其专属的技能库，一个核心难题随之浮现：系统究竟该保留哪些技能，又该淘汰哪些技能？亚马逊科学团队（Amazon Science）在论文《Ratchet》中深入探讨了基于噪声标量性能指标做出淘汰决策时，对LLM裁判的可靠性要求。

研究表明，未经维护的智能体技能库会遭遇“技能库漂移”（library drift）——技能库无限膨胀，最终导致注入AI生成的技能其效果甚至不如不注入任何技能。为了解决这一问题，作者推出了Ratchet框架，该框架通过严格的机制修复了技能库的演进过程，显著提升了模型在困难基准测试上的表现，并为安全筛选智能体能力提供了必要的数学保证。

---

# Ratchet: How Reliable Must an LLM Judge Be to Retire a Skill?

> # Ratchet: How Reliable Must an LLM Judge Be to Retire a Skill?

**arXiv:** [2605.22148](https://arxiv.org/abs/2605.22148) [cs.AI]  
**Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He  
**Submitted:** 21 May 2026 (Last revised: 7 Aug 2026)  
**Code Repository:** [GitHub - Amazon Science: Self-Evolving Agents-Ratchet](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)

> **arXiv:** [2605.22148](https://arxiv.org/abs/2605.22148) [cs.AI]  
> **Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He  
> **Submitted:** 21 May 2026 (Last revised: 7 Aug 2026)  
> **Code Repository:** [GitHub - Amazon Science: Self-Evolving Agents-Ratchet](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)

---

## Executive Summary

> ## Executive Summary

当大语言模型（LLM）智能体编写并精炼自己的技能库时，它们面临着一个关键决策：*哪些技能应该保留，哪些应该被淘汰？* 本文研究了基于嘈杂的标量性能指标做出这一淘汰决策时，对LLM裁判的可靠性要求。

> When Large Language Model (LLM) agents write and refine their own skill libraries, they face a critical decision: *which skills should be kept, and which should be retired?* This paper investigates the reliability requirements of LLM judges tasked with making this eviction decision based on noisy scalar performance metrics. 

作者证明，未维护的智能体技能库会遭受**技能库漂移**（library drift）的困扰——技能库无限增长，直到注入AI生成的技能表现得比什么都不注入还要糟糕。为了解决这个问题，作者引入了**Ratchet**，这是一个原则性的框架，它修复了技能库的演进，提升了在困难基准上的性能，并提供了安全策划智能体能力所需的数学保证。

> The authors demonstrate that unmaintained agent skill libraries suffer from **library drift**—growing indefinitely until injecting an AI-generated skill performs worse than injecting nothing at all. To solve this, the authors introduce **Ratchet**, a principled framework that repairs skill library evolution, lifts performance on hard benchmarks, and provides the mathematical guarantees required to safely curate agent capabilities.

---

## Key Findings & Contributions

> ## Key Findings & Contributions

* **技能库漂移问题：** 审计显示，LLM编写的技能表现糟糕，与无技能基线相比仅带来了 **+0.0 个百分点 (pp)** 的提升，而人类编写的技能则带来了 **+16.2pp** 的提升。如果没有主动策划，自我演进的技能库会发生膨胀并导致性能退化。
  * **The Problem of Library Drift:** Audits reveal that LLM-written skills perform abysmally, yielding **+0.0 percentage points (pp)** improvement over a no-skill baseline, whereas human-written skills yield **+16.2pp**. Without active curation, self-evolving skill libraries bloat and degrade performance.
* **Ratchet 框架：** Ratchet 通过以下三种机制修复技能库漂移：
  1. 严格根据测得的贡献淘汰技能。
  2. 将技能库宽度限制在固定大小 $C$。
  3. 约束新技能的合成。
  * *结果：* 这种方法在困难的 MBPP+ 切片上将留存的 $pass@1$ 准确率提高了 **+0.328**。
  * **The Ratchet Framework:** Ratchet repairs library drift through three mechanisms:
    1. Evicting skills based strictly on their measured contribution.
    2. Capping the library at a fixed width $C$.
    3. Constraining new skill synthesis.
    * *Result:* This approach lifts held-out $pass@1$ accuracy by **+0.328** on a difficult MBPP+ slice.
* **LLM 裁判误差的不对称性：** 在无参考（reference-free）领域中，评分来自充当二元通道的 LLM 裁判，其两个错误方向的行为完全不同：
  * **将通过误判为失败：** 会付出样本效率的代价（可以通过运行更多试验来恢复）。
  * **将失败误判为通过：** 会直接置换淘汰统计量，这是一个任何下游纠正规则都无法挽回的错误。
  * **Asymmetry in LLM Judge Errors:** In reference-free domains, scores come from an LLM judge acting as a binary channel whose two error directions behave completely differently:
    * **Passes scored as failures:** Cost sample efficiency (which can be recovered by running more trials).
    * **Failures scored as passes:** Displace the eviction statistic directly, an error that no downstream correction rule can recover.
* **端任务警报的局限性：** 端任务得分无法作为良好的安全警报——它们的变动幅度最多只有所控制性能提升的五分之一，且不会随错误率单调扩展。
  * **Limitations of End-Task Alarms:** End-task scores make poor safety alarms—they move by at most one-fifth of the governed performance lift and do not scale monotonically with error rates.
* **理论保证：** 作者证明了裁判可靠性可认证区域的两端，通过实时的智能体循环验证了它们，并提供了一种在单次传递中评估 LLM 裁判适宜性的离线方法。
  * **Theoretical Guarantees:** The authors prove both edges of the certifiable region for judge reliability, validate them through live agent loops, and provide an offline method to evaluate an LLM judge's suitability in a single pass.

---

## Reference Links & Resources

> ## Reference Links & Resources

* [查看 PDF (View PDF)](https://arxiv.org/pdf/2605.22148)
* [arXiv HTML (实验性) (arXiv HTML (Experimental))](https://arxiv.org/html/2605.22148v3)
* [DOI 参考 (DOI Reference)](https://doi.org/10.48550/arXiv.2605.22148)
* [许可证 (CC BY-NC-SA 4.0) (License (CC BY-NC-SA 4.0))](http://creativecommons.org/licenses/by-nc-sa/4.0/)

> * [View PDF](https://arxiv.org/pdf/2605.22148)
> * [arXiv HTML (Experimental)](https://arxiv.org/html/2605.22148v3)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2605.22148)
> * [License (CC BY-NC-SA 4.0)](http://creativecommons.org/licenses/by-nc-sa/4.0/)