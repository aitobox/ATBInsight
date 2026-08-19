---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- LLM Agent
- 操作系统
- 安全沙箱
- 信息流控制
- 访问控制
title: Agent libOS：面向受能力控制的自进化大模型智能体的运行时底层架构
---
### 文章背景与核心概要

随着大语言模型（LLM）智能体在多任务中持续运行、获取记忆、激活技能、合成工具、派生子进程、挂载远程资源并提交检查点，其在部署后的操作面（action surface）显著扩大。这种演进带来了严重的权限提升和数据外泄风险，特别是当系统可见性被错误地视为操作权限时更是如此。为了解决这一根本痛点，本文提出了 **Agent libOS**——一个专为智能体设计的原生库操作系统底层架构。

Agent libOS 通过解耦三个基本层面来确保系统安全：1）**操作准入（Operation Admission）**：将进程身份、任务权限上限、类型化能力、人工/策略审批、预算与具体原语相结合；2）**信息流准入（Information-Flow Admission）**：传播标签与不可变源引用、解析主机注册的接收端（sinks），并对条件式高敏感度出站实施精准的一次性人工释放；3）**持久化因果证据（Durable Causal Evidence）**：严格记录意图、结果、计费和因果链接用于审计，绝不隐式授予任何权限。

通过严格强制这些边界，Agent libOS 确保了智能体模型可见的操作面可以自由演进，而不会隐式扩大底层资源权限或信息流动的范围。论文通过源码绑定的评测验证了其有效性，为构建安全、可控且具备自进化能力的智能体系统奠定了坚实的运行时基础。

---

## Agent libOS: A Runtime Substrate for Capability-Controlled Self-Evolving LLM Agents

## Summary

As large language model (LLM) agents persist across tasks, acquire memory, activate skills, synthesize tools, fork child processes, attach remote resources, and commit checkpoints, their post-deployment action surface significantly expands. This evolution introduces severe authority-escalation and data-exfiltration risks, particularly when system visibility is mistakenly treated as permission. 

**Agent libOS** is an agent-native library operating system substrate designed to solve this problem by decoupling three fundamental planes:
1. **Operation Admission:** Merges process identity, Task Authority ceilings, typed capabilities, human/policy approvals, budgets, and concrete primitives.
2. **Information-Flow Admission:** Propagates labels and immutable source references, resolves host-registered sinks, and enforces precise one-shot human release for conditional high-sensitivity egress.
3. **Durable Causal Evidence:** Records intent, outcomes, accounting, and causal links strictly for auditing without ever implicitly granting authority.

By enforcing these boundaries, Agent libOS ensures that an agent's model-visible action surface can freely evolve without implicitly expanding underlying resource authority or information flow.

> As large language model (LLM) agents persist across tasks, acquire memory, activate skills, synthesize tools, fork child processes, attach remote resources, and commit checkpoints, their post-deployment action surface significantly expands. This evolution introduces severe authority-escalation and data-exfiltration risks, particularly when system visibility is mistakenly treated as permission. 
> 
> **Agent libOS** is an agent-native library operating system substrate designed to solve this problem by decoupling three fundamental planes:
> 1. **Operation Admission:** Merges process identity, Task Authority ceilings, typed capabilities, human/policy approvals, budgets, and concrete primitives.
> 2. **Information-Flow Admission:** Propagates labels and immutable source references, resolves host-registered sinks, and enforces precise one-shot human release for conditional high-sensitivity egress.
> 3. **Durable Causal Evidence:** Records intent, outcomes, accounting, and causal links strictly for auditing without ever implicitly granting authority.
> 
> By enforcing these boundaries, Agent libOS ensures that an agent's model-visible action surface can freely evolve without implicitly expanding underlying resource authority or information flow.

---

## Paper Metadata / 论文元数据

* **arXiv ID:** [arXiv:2606.03895](https://arxiv.org/abs/2606.03895) [cs.OS]
* **Authors / 作者:** Yingqi Zhang
* **Submitted / 提交时间:** June 2, 2026 (Last revised August 18, 2026)
* **Primary Subject / 主题:** Operating Systems (`cs.OS`)
* **Secondary Subjects / 次要主题:** Artificial Intelligence (`cs.AI`), Cryptography and Security (`cs.CR`)
* **ACM Classes / ACM 分类:** D.4.6; D.4.7; I.2.11
* **Project Page / 项目主页:** [GitHub Repository](https://github.com/yingqi-z20/Agent-libOS)

> * **arXiv ID:** [arXiv:2606.03895](https://arxiv.org/abs/2606.03895) [cs.OS]
> * **Authors:** Yingqi Zhang
> * **Submitted:** June 2, 2026 (Last revised August 18, 2026)
> * **Primary Subject:** Operating Systems (`cs.OS`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Cryptography and Security (`cs.CR`)
> * **ACM Classes:** D.4.6; D.4.7; I.2.11
> * **Project Page:** [GitHub Repository](https://github.com/yingqi-z20/Agent-libOS)

---

## Abstract / 摘要

大语言模型（LLM）智能体能够在多个任务之间持续运行、获取记忆、激活技能、合成工具、派生子进程、挂载远程资源，并将检查点提交为可重用的镜像。这些机制在部署后扩大了操作面，并且当可见性被误认为是权限时，会产生权限提升和数据外泄的风险。

我们提出了 **Agent libOS**，这是一个智能体原生的库操作系统底层架构，它将三个层面进行了分离：
* **操作准入**：结合了进程身份、任务权限上限、类型化能力、策略或人工审批、预算以及具体原语。
* **信息流准入**：传播标签和不可变源引用、解析主机注册的接收端（Sinks），并要求对条件式高敏感度出站进行精确的一次性人工释放。
* **持久化因果证据**：记录意图、结果、计费和因果链接，但绝不授予权限。

因此，模型可见的操作面可以不断演进，而无需隐式扩大资源权限或允许的信息流。

该实现提供了持久进程、对象内存、技能、系统调用中介的 JIT 工具、镜像与检查点、类型化提供程序、人工队列、预算以及持久化恢复。由提供程序支持的副作用（Effects）使用“准备-分发-结算”（prepare-dispatch-settle）协议，从而暴露出不确定性并防止盲目重放。

在基于源码的评估中，33/33 个确定性全运行时任务均通过了任务和安全评测预言机（oracles）。在 12 个规范的真实模型运行中，观察到的安全性和严格效用均为 12/12。在一项成对的 30 轮次技能投影研究中，可观测状态预言机在所有运行中均通过，每个组别中有 13/15 的运行完全正确。这些结果描述了所评估的模型/提供程序配置。*Agent libOS 无法防止提示词注入（prompt injection）、提供内核级沙箱，也无法回滚不可逆的外部影响。*

> Large language model (LLM) agents can persist across tasks, acquire memory, activate Skills, synthesize tools, fork child processes, attach remote resources, and commit checkpoints as reusable images. These mechanisms expand the action surface after deployment and create authority-escalation and data-exfiltration risks when visibility is mistaken for permission.
> 
> We present **Agent libOS**, an agent-native library OS substrate that separates three planes:
> * **Operation admission** combines process identity, Task Authority ceilings, typed Capabilities, policy or Human approval, budgets, and concrete primitives.
> * **Information-flow admission** propagates labels and immutable source references, resolves Host-registered Sinks, and requires an exact one-shot Human release for conditional high-sensitivity egress.
> * **Durable causal evidence** records intent, outcomes, accounting, and causal links but never grants authority. 
> 
> Thus, the model-visible action surface may evolve without implicitly expanding resource authority or permitted information flows.
> 
> The implementation provides persistent processes, Object Memory, Skills, syscall-mediated JIT Tools, images and checkpoints, typed providers, Human queues, budgets, and durable recovery. Provider-backed effects use a prepare-dispatch-settle protocol that exposes ambiguity and prevents blind replay. 
> 
> In source-bound evaluation, 33/33 deterministic full-runtime tasks pass both task and safety oracles. Across 12 canonical real-model runs, observed safety and strict utility are 12/12. In a paired 30-run Skill projection study, the observable-state oracle passes in all runs, with 13/15 fully correct runs in each arm. These results describe the evaluated model/provider configuration. *Agent libOS does not prevent prompt injection, provide kernel-grade sandboxing, or roll back irreversible external effects.*

---

## Full-Text and Resources / 全文与资源

* **PDF:** [查看 PDF](https://arxiv.org/pdf/2606.03895)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2606.03895v3)
* **TeX 源码:** [源码文件](https://arxiv.org/src/2606.03895)
* **许可协议:** [非独占分发许可](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2606.03895)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2606.03895v3)
> * **TeX Source:** [Source Files](https://arxiv.org/src/2606.03895)
> * **License:** [Non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)