---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 医疗大模型
- 自进化
- 临床交互
- 知识库
- 多模态诊断
title: MediSkill-Evo：基于过程约束的自进化技术实现有据可查的临床交互
---
### 文章背景与核心概要
在部分可观测的环境下，交互式临床智能体常常面临严峻挑战，其提供可靠医疗服务的关键在于通过有据可查且安全的交互过程得出准确的诊断结果。然而，现有的智能体很难将以往的诊疗经验转化为具有明确溯源性和可复用的过程知识。

为了克服这一瓶颈，**MediSkill-Evo** 提出了一种在*不微调*底层基础模型的前提下进行过程约束的自进化框架。该框架通过严格的验证和作用域规则，在四个类型化的记忆库中动态更新临床、过程、符号以及视觉知识。随后，**过程约束偏好栓控器（Process-Constrained Preference Harness）** 将这些经过验证的知识转化为具备证据支撑且优先级明确的可执行临床决策。

---

## 论文元数据

* **arXiv ID:** [arXiv:2608.23397](https://arxiv.org/abs/2608.23397) [cs.AI]
* **学科分类:** 人工智能 (`cs.AI`)
* **作者:** Ruoyu Wu, Shenfu Xie, Yinqian Sun, Haibo Tong, Feifei Zhao
* **提交时间:** 2026年8月24日 (最后修订: 2026年8月25日)
* **许可证:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **资源链接:** 
  * [查看 PDF](https://arxiv.org/pdf/2608.23397)
  * [TeX 源码](https://arxiv.org/src/2608.23397)
  * [GitHub 仓库（匿名）](https://anonymous.4open.science/r/mediskill-evo_anonymous-68E7)

---

## 摘要

> Interactive clinical agents operate under partial observability, so reliable care depends on reaching the correct diagnosis through evidence-grounded, safe interactions. Yet existing agents struggle to convert experience into reusable process knowledge with explicit provenance and authority. To address this gap, we introduce MediSkill-Evo, which self-evolves governed process knowledge without fine-tuning the backbone. It realizes this self-evolution by updating clinical, process, symbolic, and visual knowledge in four typed banks under type-specific validation and scope rules. The Process-Constrained Preference Harness then turns validated knowledge into action by grounding candidates in evidence and prioritizing safer decisions. We evaluate on 300 MIMIC-IV-derived FullChain encounters, 180 hard-isolation conditions covering six process obligations, and 100 multimodal NEJM image-diagnosis cases. On Qwen FullChain, MediSkill-Evo improves diagnosis accuracy by 7.81% and treatment-intent coverage by 70.67% over the bestperforming prior agent, while reducing critical failures by 43.04%. Under stress, it improves the stress-process composite by 7.77% and required-action completion by 12.41% over the best-performing agent for each metric, with stronger patient-fact, temporal-evidence, and triage-red-flag recovery and no controller-scored errors in unavailable-evidence, treatment, and triage safety checks. On multimodal NEJM diagnosis, MediSkill-Evo with optional MedSAM localization improves diagnosis accuracy by 2.56% and core score by 18.96% over the best-performing memory agent.

交互式临床智能体在部分可观测性下运行，因此可靠的护理依赖于通过有据可查、安全的交互来得出正确的诊断。然而，现有的智能体很难将经验转化为具有明确来源和权威性的可复用过程知识。为了填补这一空白，我们推出了 MediSkill-Evo，它在不微调骨干网络的情况下实现受控过程知识的自我进化。它通过在四种类型库中更新临床、过程、符号和视觉知识来实现这种自我进化，并遵循特定类型的验证和范围规则。然后，过程约束偏好栓控器通过将候选方案锚定在证据中并优先考虑更安全的决策，将经过验证的知识转化为行动。我们在 300 个源自 MIMIC-IV 的 FullChain 病例、覆盖六项过程义务的 180 种硬隔离条件以及 100 个多模态 NEJM 图像诊断案例上进行了评估。在 Qwen FullChain 上，与表现最好的先前智能体相比，MediSkill-Evo 将诊断准确率提高了 7.81%，治疗意图覆盖率提高了 70.67%，同时将严重故障减少了 43.04%。在压力下，它在各项指标上均优于表现最好的智能体，其中压力过程综合指标提升了 7.77%，必需动作完成度提升了 12.41%，并在患者事实、时间证据和分诊红旗恢复方面表现更强，在不可用证据、治疗和分诊安全检查中没有出现控制器评分错误。在多模态 NEJM 诊断中，结合可选 MedSAM 定位的 MediSkill-Evo 比表现最好的记忆智能体将诊断准确率提高了 2.56%，核心得分提高了 18.96%。

---

## 核心亮点与性能表现

* **FullChain 病例 (MIMIC-IV):** 与以往表现最好的智能体相比，诊断准确率提升了 **7.81%**，治疗意图覆盖率提升了 **70.67%**，同时将严重故障率降低了 **43.04%**。
* **压力与隔离测试 (Stress & Isolation Testing):** 压力过程综合指标提升了 **7.77%**，必需动作完成度提升了 **12.41%**；在各项关键安全检查（不可用证据、治疗和分诊）中实现了零控制器评分错误。
* **多模态 NEJM 诊断 (Multimodal NEJM Diagnosis):** 结合可选的 MedSAM 定位技术，相比领先的基线记忆智能体，诊断准确率提升了 **2.56%**，核心得分提升了 **18.96%**。