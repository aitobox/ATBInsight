---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-01
hide:
  - navigation
tags:
  - CounterSteer
  - 间接提示词注入
  - 激活导向
  - AI 智能体安全
  - Mark Russinovich
  - arXiv论文
title: "CounterSteer：利用激活导向抑制大模型智能体中的间接提示词注入攻击"
---

# CounterSteer：利用激活导向抑制大模型智能体中的间接提示词注入攻击

> # CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 深度融入各类 AI 智能体 (AI Agent) 场景，自动化处理外部网页、邮件和工具输出已成为常态，但外部不受信任内容中潜藏的“间接提示词注入攻击”却成为了巨大的安全隐患。Mark Russinovich 提出的 CounterSteer 带来了一种全新且高效的推理阶段防御方案：无需对模型进行二次微调，也不依赖额外的辅助防护模型，而是直接在预填阶段从模型残差流中识别并剔除与恶意指令相关的激活方向。这一常开型机制让攻击者无法察觉并绕过检测，在五款主流开源架构模型上将攻击成功率压制至接近于零，为智能体生态系统的安全落地提供了一套开箱即用且近乎无损的全新防御范式。

---

## 核心执行摘要

> ## Executive Summary

**CounterSteer** 是一种创新的推理阶段防御机制，专门用于化解大语言模型 (LLM) 智能体中的间接提示词注入漏洞。在模型处理输入的预填 (Prefill) 阶段，CounterSteer 能够精准锁定与“遵从恶意指令”相关的残差流 (Residual Stream) 激活方向并直接将其减去；这种做法既不需要重新微调模型、也无需部署额外的辅助审查模型或引入额外的 Token ，便能干净利落地瓦解恶意指令对智能体执行流程的劫持。

> **CounterSteer** is an innovative inference-time defense mechanism designed to mitigate indirect prompt injection vulnerabilities in Large Language Model (LLM) agents. By identifying and subtracting residual-stream directions associated with malicious instruction-following during the prefill phase, CounterSteer effectively neutralizes instructional takeovers without requiring model fine-tuning, auxiliary models, or added tokens.

---

## 论文元数据

> ## Paper Metadata

* **论文标题：** CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering
* **作者：** Mark Russinovich
* **主要学科领域：** 密码学与安全 (`cs.CR`) 
* **次要学科领域：** 人工智能 (`cs.AI`) 
* **arXiv 编号：** [arXiv:2609.36570 [cs.CR]](https://arxiv.org/abs/2609.36570)
* **提交时间：** 2026 年 9 月 29 日

> * **Title:** CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering
> * **Author:** Mark Russinovich
> * **Primary Subject:** Cryptography and Security (`cs.CR`)
> * **Secondary Subject:** Artificial Intelligence (`cs.AI`)
> * **arXiv Identifier:** [arXiv:2609.36570 [cs.CR]](https://arxiv.org/abs/2609.36570)
> * **Submitted:** September 29, 2026

---

## 论文摘要

> ## Abstract

间接提示词注入就像是给 AI 智能体设下的“特洛伊木马”陷阱：当智能体检索外部网页、文档或数据时，潜藏在其中的不受信任文本会诱导智能体将其误判为正当指令。为此，CounterSteer 提出了一套简洁明了的五步配方流程：通过构建成对的对照测试场景（两组场景唯一的差异仅在于是否听从了嵌入的指令），为每个大语言模型精准拟合出一个对应的残差流向量方向。只有当该方向成功通过预先设立的因果验证与通用能力门控检验时，才会被保留并投入使用。

> Indirect prompt injection tricks LLM agents into treating untrusted retrieved text as legitimate instructions. CounterSteer presents a streamlined, five-step recipe to fit a residual-stream direction per model using paired episodes (differing only in whether an embedded instruction is followed). This direction is retained only if it successfully passes pre-specified causal and capability gates.

在实际部署运行中，只要智能体调用工具并接收返回结果，系统就会在预填计算阶段从每一个工具结果 Token 中直接减去这一学习到的方向。由于这种神经层面的干预始终处于常开生效状态，系统中完全不存在任何可供攻击者探测或绕过的“防火墙规则”与检测开关。

> During deployment, the learned direction is subtracted from every tool-result token during the prefill phase. Because the edit is always active, there is no detection mechanism for attackers to evade.

---

## 核心发现与性能表现

> ## Key Findings & Performance

* **攻击成功率大幅降低：** 在涵盖五大厂商血统、参数量跨越 80 亿 (8B) 到 1060 亿 (106B) 的五款开源权重模型上，面对预留的测试集攻击，未防御时的攻击成功率高达 **0.21–1.00** （最高可达 100%），而开启 CounterSteer 防护后断崖式骤降至 **0.00–0.17** 。
* **AgentDojo 沦陷率大幅压制：** 在权威智能体基准测试 AgentDojo 中，智能体的沦陷率从原先的 **0.10–0.49** 锐减至 **0.006–0.079** （最低降至千分之六）。
* **出色保留正常任务效用：** 在排版归一化的良性任务效用测试中保持了 **93–100%** 的原有性能；尽管在针对经过导向干预的内容进行复杂推理时会产生一定程度的任务相关性能开销，但日常通用能力几乎毫无损伤。
* **极其坚固的防御鲁棒性：** 
  * **白盒梯度攻击抵御：** 即便攻击者完全获知已部署的干预向量并通过白盒梯度发起攻击，在 52 个测试场景中至多也仅能攻破 2 个；
  * **人类红队实战攻击免疫：** 在回放的 2,052 次人类安全红队实战攻击样本中，攻击成功率彻底归零 (0/2052) ；
  * **黑盒语义重构绕过困难：** 黑盒语义重构搜索 (Framing Searches) 在 18 个开发集测试样本中仅能侥幸绕过 3 个。

> * **Attack Success Reduction:** Across five open-weights models (ranging from 8B to 106B parameters across five vendor lineages), held-out attack success rates plummeted from an undefended **0.21–1.00** down to **0.00–0.17** when defended.
> * **AgentDojo Compromise Rate:** Decreased from **0.10–0.49** down to **0.006–0.079**.
> * **Utility Retention:** Retains **93–100%** typography-normalized benign utility, though some task-dependent costs arise when reasoning over steered content.
> * **Robustness:** 
>   * White-box gradient attacks through the deployed vector successfully compromised at most 2 out of 52 episodes.
>   * Zero out of 2,052 replayed human red-team attacks succeeded.
>   * Black-box framing searches successfully bypassed the defense in only 3 out of 18 development samples.

---

## 局限性与未来展望

> ## Limitations & Future Work

虽然 CounterSteer 几乎彻底瓦解了针对执行流程的恶意指令劫持，但在**参数操纵** (Parameter Manipulation) ——即攻击者在原本合法的工具调用中夹带自选恶意参数（例如正常调用转账功能，却篡改了转账接收人账号）——方面仅能实现部分抵御（在 18 个测试样本中成功防御了 13 个）。究其内在原因，这类决策往往是在模型真正生成并输出参数的那一瞬间才呈现出线性可读的内部表征，而非在生成前的预填检查位点即可捕获；因此，未来还需要结合额外的**参数来源溯源控制** (Argument-Provenance Controls) 机制，才能将这一安全通路彻底封堵。

> While CounterSteer largely neutralizes instructional takeovers, **parameter manipulation** (attacker-chosen arguments embedded in otherwise legitimate calls) is only partially resisted (13 out of 18). Because the decision becomes linearly readable at argument emission rather than at pre-generation inspection sites, additional **argument-provenance controls** are required to fully secure these pathways.
