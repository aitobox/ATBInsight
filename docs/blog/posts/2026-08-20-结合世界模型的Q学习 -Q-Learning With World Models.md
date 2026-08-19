---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 强化学习
- 世界模型
- Q学习
- 机器人学
- 视觉语言动作模型
title: 结合世界模型的Q学习 (Q-Learning With World Models)
---
### 文章背景与核心概要
离线强化学习（RL）在样本效率方面取得了显著进展，推动了诸如视觉-语言-动作（Vision-Language-Action）模型强化学习微调等应用的落地。世界模型通过预测状态变化，为提升样本效率提供了另一条途径，但其成功大都局限于监督策略学习。传统的基于模型的强化学习方法通常直接在想象的轨迹（rollouts）上优化策略或价值函数，这容易导致复合模型偏差（compounding model bias），且难以扩展到如真实世界机器人学这样高维复杂的问题中。

为了应对这些挑战，本文作者提出了 **QWM（Q-Learning With World Models，结合世界模型的Q学习）**。这一新颖的框架在标准Q学习的基础上，利用世界模型在测试时对想象的轨迹进行搜索，从而在在线采样和评估过程中选择出高价值的动作。由于底层策略和价值函数严格基于真实转移进行训练，QWM成功避开了复合模型偏差，同时充分发挥了预测性搜索在样本效率上的优势。在具有挑战性的机器人操作基准测试（*Robomimic* 和 *LIBERO*）上的评估表明，QWM在样本效率和总体性能上均显著优于现有的强基线方法。

---

## Q-Learning With World Models

**arXiv:** [2608.17163 [cs.LG]](https://arxiv.org/abs/2608.17163)  
**Authors:** Perry Dong, Yueru Jia, Chelsea Finn, Dorsa Sadigh  
**Submitted:** August 17, 2026  
**Subjects:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`)  

---

## Summary

> Off-policy reinforcement learning (RL) has become increasingly sample-efficient, facilitating applications such as RL fine-tuning for Vision-Language-Action models. While **world models** offer additional sample-efficiency benefits by predicting state changes, their success has largely been restricted to supervised policy learning. Traditional model-based RL methods often optimize policies or value functions directly on imagined rollouts, which suffers from compounding model bias and struggles to scale to high-dimensional problems like real-world robotics.

离线强化学习（RL）的样本效率不断提高，促进了视觉-语言-动作模型强化学习微调等应用的实现。尽管**世界模型**通过预测状态变化提供了额外的样本效率优势，但其成功大都局限于监督策略学习。传统的基于模型的强化学习方法通常直接在想象的轨迹上优化策略或价值函数，这会遭受复合模型偏差的困扰，并且难以扩展到现实世界机器人学等高维问题中。

> To address these challenges, the authors propose **QWM (Q-Learning With World Models)**. This novel framework leverages world models to perform test-time search over imagined trajectories on top of standard Q-learning, selecting high-value actions during both online rollouts and evaluation. Because the underlying policy and value functions are trained strictly on real transitions, QWM successfully avoids compounding model bias while harnessing the sample-efficiency advantages of predictive search. 

为了应对这些挑战，作者提出了 **QWM（结合世界模型的Q学习）**。这一新颖的框架在标准Q学习的基础上，利用世界模型在测试时对想象的轨迹进行搜索，从而在在线采样和评估过程中选择出高价值的动作。由于底层策略和价值函数严格基于真实转移进行训练，QWM成功避开了复合模型偏差，同时利用了预测性搜索的样本效率优势。

> Evaluated on challenging robotic manipulation benchmarks (*Robomimic* and *LIBERO*), QWM significantly outperforms strong state-of-the-art baselines in both sample efficiency and overall performance.

在具有挑战性的机器人操作基准测试（*Robomimic* 和 *LIBERO*）上进行评估时，QWM在样本效率和总体性能上均显著优于强大的最先进基线方法。

---

## Abstract

> Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which is prone to compounding bias and struggles to scale to large, high-dimensional problems such as real-world robotics, a problem that worsens with task horizon and visual complexity. In this work, we instead ask whether we can leverage world models directly on top of standard Q-learning to improve performance, while remaining trained and grounded in the real, online setting. We propose QWM, a framework that leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation. Since the policy and value function are trained only on real transitions, QWM avoids compounding model bias while still gaining the sample-efficiency benefits of predictive search. On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

> 离线强化学习（RL）的样本效率日益提高，使得将视觉-语言-动作模型微调为可靠、高性能策略等应用成为可能。世界模型为提升样本效率提供了另一个抓手，因为它们预测的是状态变化而不仅仅是动作，但其成功大都局限于监督策略学习。先前的基于模型的强化学习方法通常直接在想象的轨迹上优化策略或价值函数，这容易产生复合偏差，且难以扩展到如现实世界机器人学这样的大型高维问题中（随着任务视界和视觉复杂度的增加，这一问题会更加严重）。在这项工作中，我们转而探讨是否可以直接在标准Q学习之上利用世界模型来提升性能，同时保持在真实的在线环境中进行训练和落地。我们提出了QWM，这是一个在Q学习基础之上利用世界模型在测试时对想象轨迹进行搜索的框架，以便在在线采样和评估期间选择高价值的动作。由于策略和价值函数仅基于真实转移进行训练，QWM避免了复合模型偏差，同时依然获得了预测性搜索带来的样本效率收益。在极具挑战性的操作基准测试Robomimic和LIBERO上，QWM在样本效率和性能方面均显著优于先前最先进的强大方法。

---

## Resources & Links

* **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.17163) | [HTML (Experimental)](https://arxiv.org/html/2608.17163v1) | [TeX Source](https://arxiv.org/src/2608.17163)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17163) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17163) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17163)