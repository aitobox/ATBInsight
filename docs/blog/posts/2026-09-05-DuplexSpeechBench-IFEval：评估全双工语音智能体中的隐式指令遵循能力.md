---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 全双工语音智能体
- 指令遵循
- 基准测试
- 对话动态
- 语音AI
title: DuplexSpeechBench-IFEval：评估全双工语音智能体中的隐式指令遵循能力
---
### 文章背景与核心概要
现代全双工语音智能体必须在实时环境中无缝管理对话动态，例如倾听、附和（backchanneling）、打断以及让出话语权等。然而，现有的评估基准大多依赖显式的轮次管理规则，而现实世界中的语音智能体通常通过角色和人设来进行配置，这要求它们必须具备隐式推断合适行为的能力。

为了填补这一空白，作者推出了 **DuplexSpeechBench-IFEval (DSB-IFEval)**，这是一个包含 **1,038个测试用例** 的全新评估框架，跨越了八种助手角色和五种调节协议。通过对六个实时语音系统进行评估，研究揭示了它们在架构上的权衡：一些模型在处理基于人设的隐式指令时表现不佳，而另一些模型虽然能很好地适应人设，但在动态调整话语权管理策略或处理安全冲突时却力不从心。该研究为未来全双工语音交互系统的设计和优化指明了方向。

---

# DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents

**Authors:** Puneet Mathur, Dinesh Manocha  
**Submitted:** 3 September 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv:** [2609.03423](https://arxiv.org/abs/2609.03423)  

---

## 📌 Summary

现代全双工语音智能体必须在实时环境中无缝管理对话动态——例如倾听、附和、打断以及让出话语权。虽然现有的评估基准依赖于显式的轮次管理规则，但现实世界中的语音智能体通常是通过角色和人设进行配置的，这要求它们必须隐式推断出合适的行为。

> Modern full-duplex voice agents must seamlessly manage conversational dynamics—such as listening, backchanneling, interrupting, and yielding the floor—in real time. While existing evaluation benchmarks rely on explicit turn-management rules, real-world voice agents are typically configured using roles and personas, requiring them to infer appropriate behaviors implicitly. 

为了弥补这一差距，作者推出了 **DuplexSpeechBench-IFEval (DSB-IFEval)**，这是一个新颖的评估框架，包含 **1,038个测试用例**，跨越八个助手角色和五个调节协议。对六个实时语音系统的评估揭示了明显的架构权衡：一些模型难以处理隐式的人设指令，而另一些模型虽然能很好地适应人设，却无法动态调整其话语权管理策略或处理安全冲突。

> To bridge this gap, the authors introduce **DuplexSpeechBench-IFEval (DSB-IFEval)**, a novel evaluation framework comprising **1,038 test cases** spanning eight assistant roles and five conditioning protocols. Evaluating six real-time speech systems reveals distinct architectural trade-offs: some models struggle with implicit persona-based instructions, while others adapt well to personas but fail to dynamically adjust their floor-management strategies or handle safety conflicts.

---

## 📖 Abstract

全双工语音智能体必须持续决定何时倾听、附和、打断、处理语音重叠、获取话语权以及让出话语权。现有的基准测试大多通过显式的轮次管理指令来测试这些行为，而已部署的智能体通常通过角色或人设进行配置，对话行为必须从中推断得出。

> Full-duplex voice agents must continuously decide when to listen, backchannel, interrupt, handle speech overlaps, take the floor, and yield. Existing benchmarks largely test these behaviors through explicit turn-management instructions, while deployed agents are often configured through roles or personas from which the appropriate conversational behavior must be inferred. 

我们推出了 **DuplexSpeechBench-IFEval (DSB-IFEval)**，用于评估实时口语交互中的隐式指令遵循能力。DSB-IFEval 包含 1,038 个测试用例，涵盖八种不同的助手角色，并评估了用于指令遵循的五种调节协议：
1. 默认行为
2. 显式行为指令
3. 人设隐含行为
4. 组合人设-规则调节
5. 指令冲突

> We introduce **DuplexSpeechBench-IFEval (DSB-IFEval)** for evaluating implicit instruction-following in real-time spoken interaction. DSB-IFEval comprises 1,038 test cases spanning eight diverse assistant roles and evaluates five conditioning protocols for instruction-following:
> 1. Default behavior
> 2. Explicit behavioral instructions
> 3. Persona-implied behavior
> 4. Combined persona–rule conditioning
> 5. Instruction conflict

我们使用确定性的 **指令遵循得分 (IAS)** 来衡量实时话语权管理，并使用大模型评判的 **人设遵循得分 (PAS)** 来衡量符合人设的内容。

> We measure real-time floor management using a deterministic **Instruction Adherence Score (IAS)** and persona-consistent content using an LLM-judged **Persona Adherence Score (PAS)**. 

### Key Findings
* **模型依赖的敏感性：** 全双工模型（如 **F-Actor** 和 **PersonaPlex**）对对话行为是显式声明还是隐式推断非常敏感，在仅有人设调节下，遵循度分别下降了 **9.7%** 和 **4.5%**。
* **僵化的对话行为：** 诸如 **GPT-Realtime**、**MiniCPM-o** 和 **Fun-Audio-Chat** 等系统高度遵循符合人设的内容，但其话语权行为在显式指令和纯人设指令下保持静态，表现出在主动行为方面的局限性。
* **安全覆盖：** 即使系统能够可靠地遵循采用规定人设的冲突指令，它们在面对安全冲突时仍然难以超越这些人设。

> * **Model-Dependent Sensitivity:** Full-duplex models like **F-Actor** and **PersonaPlex** are sensitive to whether conversational behavior is stated explicitly or inferred, with adherence dropping by **9.7%** and **4.5%**, respectively, under persona-only conditioning.
> * **Rigid Floor Behavior:** Systems like **GPT-Realtime**, **MiniCPM-o**, and **Fun-Audio-Chat** strongly adhere to persona-consistent content, but their floor behavior remains static across explicit and persona-only instructions, showing limitations on proactive actions.
> * **Safety Overrides:** Even when systems reliably follow conflicting directives to adopt a prescribed persona, they still struggle to override those personas when faced with safety conflicts.

这些结果突显出：推断角色隐含的行为、在适当的对话时刻执行它们以及解决竞争指令，仍然是全双工语音智能体面临的公开挑战。

> These results highlight that inferring role-implied behaviors, executing them at appropriate conversational moments, and resolving competing instructions remain open challenges for full-duplex voice agents.

---

## 🔗 Links & Resources

* **Full-Text Access:** [arXiv PDF](https://arxiv.org/pdf/2609.03423) | [arXiv HTML](https://arxiv.org/html/2609.03423v1)
* **Source Code / TeX:** [TeX Source](https://arxiv.org/src/2609.03423)
* **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03423) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03423)

---
*(License: [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/))*