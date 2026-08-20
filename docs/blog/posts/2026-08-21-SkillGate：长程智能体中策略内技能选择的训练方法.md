---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- AI智能体
- 强化学习
- 技能选择
- 策略优化
title: SkillGate：长程智能体中策略内技能选择的训练方法
---
### 文章背景与核心概要

现代 AI 智能体框架日益倾向于将程序化知识封装为“技能”（即智能体按需读取的指令文件）。然而，随着智能体在长程任务中面临成千上万种可选技能，如何在任务执行过程中确定“读取哪项技能”成为了一个关键决策，但目前尚缺乏有效的训练信号来指导这一过程。

本文指出，标准的基于结果奖励的强化学习（RL）存在结构性缺陷，作者将其定义为“选择器信用匮乏”（selector credit starvation）。在长程序列中，由于奖励是基于整个序列的，技能命名标记（skill-naming tokens）获得的损失权重极小，且随着轨迹延长，其获得的信用往往方向错误。

为了解决这一问题，作者提出了 **SkillGate** 机制。该机制将标记支持划分为两个不相交的信用通道：一是仅针对执行标记的“结果信用”，二是专门针对技能命名标记的“动作局部优势”。通过这种方式，模型能够独立地奖励正确的技能选择。实验表明，在 16 种候选技能的基准测试中，SkillGate 将 9B 策略的成功率从 40.8% 提升至 53.2%，显著优于基准模型。

---

## 📄 摘要

> Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. 
>
> 智能体框架日益倾向于将程序化知识封装为技能：即智能体按需读取的指令文件，而公共库中现在已经包含了数千种此类技能。因此，读取哪种技能已成为策略在任务执行过程中自行做出的决策，但目前尚无现有的信号对其进行训练。

> We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name **selector credit starvation**: under a broadcast, sequence-level advantage, the few tokens that name the chosen skill carry a vanishing share of the loss, and the credit they inherit is increasingly wrong-signed as trajectories lengthen. A correct choice is punished whenever the execution after it fails, even though the choice itself is among the most valuable decisions in the trajectory. Auditing a completed run's own training artifacts confirms all three properties, each worsening monotonically with horizon. 
>
> 我们证明，默认的补救措施——即在候选列表上进行基于结果奖励的强化学习——无法实现这一目标，原因在于我们识别并命名为“选择器信用匮乏”的结构性缺陷：在广播式的序列级优势下，少数命名所选技能的标记所承担的损失份额微乎其微，且随着轨迹的延长，它们所继承的信用往往方向错误。即使某项选择是轨迹中最有价值的决策之一，只要后续执行失败，该正确选择就会受到惩罚。对已完成运行的训练产物进行审计，证实了这三个特性，且每一个特性都会随着时间跨度的增加而单调恶化。

> **SkillGate** removes the failure by construction: it partitions the token support into two disjoint credit channels, outcome credit reaching only execution tokens, and a separate action-local advantage reaching exactly the skill-naming tokens, positive only when a trajectory's single read is the correct one. On five agentic benchmarks under a 16-candidate slate, SkillGate lifts a 9B policy from 40.8% to 53.2% trial success, well ahead of the identical budget spent on outcome reward alone, while cutting exposure to misleading candidates by two thirds and reading fewer skills.
>
> **SkillGate** 通过架构设计消除了这一缺陷：它将标记支持划分为两个不相交的信用通道，结果信用仅到达执行标记，而独立的动作局部优势则专门到达技能命名标记，且仅在轨迹中单次读取为正确时才为正值。在 16 种候选技能的五个智能体基准测试中，SkillGate 将 9B 策略的试验成功率从 40.8% 提升至 53.2%，远超仅使用结果奖励的同等预算方案，同时将对误导性候选对象的暴露减少了三分之二，并减少了技能读取次数。

---

## 🔗 额外资源与产物

* **代码仓库：** [GitHub - DeepExperience/SkillGate](https://github.com/DeepExperience/SkillGate)
* **预训练模型：** [Hugging Face - simonlqy/SkillGate-9B](https://huggingface.co/simonlqy/SkillGate-9B)
* **数据集/主题：** 计算机科学 > 人工智能 (`cs.AI`)
* **DOI：** [10.48550/arXiv.2608.18852](https://doi.org/10.48550/arXiv.2608.18852)

---
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">