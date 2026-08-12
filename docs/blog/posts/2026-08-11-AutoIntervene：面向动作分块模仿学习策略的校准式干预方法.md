---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- 模仿学习
- 机器人学
- 人机协同
- 动作分块
- 策略校准
title: AutoIntervene：面向动作分块模仿学习策略的校准式干预方法
---
### 文章背景与核心概要
动作分块视觉运动策略（Action-chunking visuomotor policies）通过预测一连串短序列的动作而不是孤立的单步指令，显著提升了时间一致性。然而，感知误差和执行漂移常常会将机器人推向其训练演示分布之外。当这种情况发生时，策略仍会持续输出与实际观察状态不符的平滑动作块。

为了解决这一问题，作者推出了 **AutoIntervene**。这是一个在线框架，能够在部署过程中在动作分块策略和人类操作员之间进行选择性控制权交接。AutoIntervene 不依赖于手动设定的得分阈值，而是通过从成功执行任务中编译的“视觉-动作支持记忆”（结合了视觉相似性以及所提议动作与参考动作之间的一致性）来评估所提议的动作块；采用“阶段局部支持”来控制特定任务阶段中的策略到操作员的交接；利用“全局支持”来管理操作员介入恢复后控制权向策略的交回；通过从留存的专家演示中推导出的经验分位数来自动校准切换阈值；并保留针对学习器引发状态的成功干预片段，从而为未来的策略更新提供纠错监督。

真实世界双臂操作实验表明，与传统的长时手动干预策略相比，AutoIntervene 实现了更高的适应后任务成功率，并显著减少了操作员的控制时间。

---

# AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies

> **Authors:** Jinhe Tang, Weiming Zhi  
> **Subjects:** Robotics (`cs.RO`); Artificial Intelligence (`cs.AI`); Computer Vision and Pattern Recognition (`cs.CV`); Human-Computer Interaction (`cs.HC`); Machine Learning (`cs.LG`)  
> **arXiv:** [2608.07065 [cs.RO]](https://arxiv.org/abs/2608.07065) | **Submitted:** August 7, 2026  
> **Links:** [View PDF](https://arxiv.org/pdf/2608.07065) | [HTML Version](https://arxiv.org/html/2608.07065v1) | [Project Website & Videos](https://aus.bot/research/autointervene/)

---

## 📌 Summary

> Action-chunking visuomotor policies improve temporal consistency by predicting short sequences of actions instead of isolated, single-step commands. However, perception errors and execution drift often push the robot outside the distribution of its training demonstrations. When this happens, the policy continues to output smooth action chunks that mismatch the actual observed state. 

> To address this, the authors introduce **AutoIntervene**, an online framework that selectively transfers control between an action-chunking policy and a human operator during deployment. Rather than relying on manual score thresholds, AutoIntervene:
> * Evaluates proposed action chunks using a **visual-action support memory** compiled from successful task executions (blending visual similarity with consistency between proposed and reference actions).
> * Employs **phase-local support** to govern policy-to-operator handoffs within specific task phases.
> * Uses **global support** to manage the return of control back to the policy after an operator recovery.
> * Calibrates switching thresholds automatically via empirical quantiles derived from held-out expert demonstrations.
> * Retains successful intervention segments targeting learner-induced states to supply corrective supervision for future policy updates.

> Real-world bimanual manipulation experiments demonstrate that AutoIntervene achieves higher post-adaptation task success rates and requires significantly less operator-control time compared to traditional manual intervention strategies.

---

## 📋 Bibliographic & Access Information

> - **Citation:** `Tang, J., & Zhi, W. (2026). AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies. arXiv:2608.07065 [cs.RO].`
> - **DOI:** [10.48550/arXiv.2608.07065](https://doi.org/10.48550/arXiv.2608.07065)
> - **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>

---

## 🔗 External Resources & Tools

> * **Code & Media:** Accessible via [Project Website](https://aus.bot/research/autointervene/)
> * **Alternative Indices:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07065) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07065) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07065)