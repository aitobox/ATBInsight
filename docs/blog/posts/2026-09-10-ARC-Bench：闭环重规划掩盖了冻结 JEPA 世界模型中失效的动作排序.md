---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 世界模型
- JEPA
- 机器人学
- 强化学习
- 评估基准
title: ARC-Bench：闭环重规划掩盖了冻结 JEPA 世界模型中失效的动作排序
---
### 文章背景与核心概要

无奖励的潜在世界模型通常通过根据冻结潜在空间中的距离来对候选动作进行评分（倾向于其预测的未来嵌入最接近目标嵌入的动作），从而进行动作规划。这种方法依赖于一个关键但极少被审视的假设：**潜在距离具有动作可排序性**——这意味着按潜在距离对候选动作进行排序，能够可靠地对应于按真实代价进行排序。

在该论文中，作者推出了 **ARC-Bench**，这是一个固定候选、无泄漏的评估协议，旨在衡量冻结的联合嵌入预测架构（JEPA）风格的目标是否能够准确对候选动作进行排序。对跨导航和操作控制领域的官方发布 JEPA-WM 检查点进行的审计表明，**这一核心假设在结构上严重失效**。理解这一局限性对于未来构建更加鲁棒的世界模型规划架构具有重要意义。

---

# ARC-Bench: Closed-Loop Replanning Masks Broken Action Ranking in Frozen JEPA World Models

> # ARC-Bench: Closed-Loop Replanning Masks Broken Action Ranking in Frozen JEPA World Models

**Authors:** Zhengshu Zhang, Zhiyuan Li  
**Subjects:** Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`); Robotics (`cs.RO`)  
**arXiv ID:** [2609.05461](https://arxiv.org/abs/2609.05461) | **DOI:** [10.48550/arXiv.2609.05461](https://doi.org/10.48550/arXiv.2609.05461)  
**Submission Date:** 12 August 2026  

> **Authors:** Zhengshu Zhang, Zhiyuan Li  
> **Subjects:** Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`); Robotics (`cs.RO`)  
> **arXiv ID:** [2609.05461](https://arxiv.org/abs/2609.05461) | **DOI:** [10.48550/arXiv.2609.05461](https://doi.org/10.48550/arXiv.2609.05461)  
> **Submission Date:** 12 August 2026  

---

## Executive Summary

> ## Executive Summary

无奖励的潜在世界模型通常通过根据候选动作在冻结的潜在空间中的距离来对其进行评分（偏好其预测的未来嵌入最接近目标嵌入的动作）。这种方法依赖于一个关键但极少被审核的假设：**潜在距离是可进行动作排序的**——这意味着按潜在距离对候选动作进行排序，能够可靠地与按真实代价进行排序相对应。

> Reward-free latent world models typically plan actions by scoring candidates according to their distance in a frozen latent space (preferring actions whose predicted future embeddings land closest to the goal embedding). This approach relies on a critical, yet rarely audited assumption: **that latent closeness is action-rankable**—meaning that ordering candidates by latent distance reliably correlates with ordering them by true cost. 

在这篇论文中，作者引入了 **ARC-Bench**，这是一个固定候选、无泄漏的评估协议，旨在衡量冻结的联合嵌入预测架构（JEPA）风格的目标函数能否准确对候选动作进行排序。对跨越导航和操作控制领域的官方发布 JEPA-WM 检查点进行的审核表明，**这一核心假设在结构上发生了严重失效**。

> In this paper, the authors introduce **ARC-Bench**, a fixed-candidate, no-leak evaluation protocol designed to measure whether frozen Joint-Embedding Predictive Architecture (JEPA)-style objectives can accurately rank candidate actions. Auditing official released JEPA-WM checkpoints across navigation and manipulation control domains reveals that **this core assumption fails structurally and severely**. 

---

## Key Findings & Insights

> ## Key Findings & Insights

* **动作排序的结构性失效：** 在官方的操作审核中，得分最高的候选动作几乎总是亚优的。在迷宫领域中也一致观察到了相同的排序反转现象。
* **跨骨干网络具有鲁棒性：** 受控的视觉骨干网络扩展表明，当用 ViT-L 和 ViT-G 尺寸的视频预训练 V-JEPA 1 和 V-JEPA 2 编码器替换 DINOv2 时，这种缺陷依然存在。
* **排除替代解释：** 经过彻底测试并排除了数据来源、训练不足、匹配预算的骨干网络控制以及度量循环性等琐碎的解释。
* **缺陷为何一直未被察觉（闭环重规划）：** 研究解释说，闭环重规划充当了一种掩护。当规划器的重规划频率降低时，导航和操作领域的任务成功率都会崩溃。此外，通过频繁重规划挽救的剧集表现出高度集中的严重首个规划排序失败。
* **结论：** 标准的闭环成功率系统性地高估了冻结潜在表示的实际可排序性。ARC-Bench 提供了必要的测量方法——而掩饰机制则提供了相应的解释——使得那些在不直接审核发布 JEPA-WM 动作可排序性的情况下围绕潜在空间规划器进行自适应、摊销或重规划的方法能够找到依据。

> * **Structural Failure of Action Ranking:** On official manipulation audits, the top-scored candidate is almost always suboptimal. The same ranking inversion is consistently observed in maze domains.
> * **Robust Across Backbones:** Controlled visual-backbone extensions demonstrate that this defect persists even when DINOv2 is replaced by video-pretrained V-JEPA 1 and V-JEPA 2 encoders scaled up to ViT-L and ViT-G sizes.
> * **Ruled-Out Alternatives:** Trivial explanations such as data provenance, undertraining, matched-budget backbone controls, and metric circularity were thoroughly tested and ruled out.
> * **Why the Defect Stayed Invisible (Closed-Loop Replanning):** The study explains that closed-loop replanning acts as a mask. When the planner's replanning frequency is reduced, task success collapses in both navigation and manipulation domains. Furthermore, episodes rescued by frequent replanning show a high concentration of severe first-plan ranking failures. 
> * **Conclusion:** Standard closed-loop success rates systematically overstate the actual rankability of frozen latent representations. ARC-Bench provides the necessary measurement—and the masking mechanism provides the explanation—for methods that adapt, amortize, or replan around latent-space planners without directly auditing released JEPA-WM action rankability.

---

## Links & Resources

> ## Links & Resources

* [查看 PDF (View PDF)](https://arxiv.org/pdf/2609.05461)
* [TeX 源码 (TeX Source)](https://arxiv.org/src/2609.05461)
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05461) | [谷歌学术 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05461) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.05461)

> * [View PDF](https://arxiv.org/pdf/2609.05461)
> * [TeX Source](https://arxiv.org/src/2609.05461)
> * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.05461) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.05461) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.05461)