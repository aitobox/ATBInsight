---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 大模型智能体
- 安全上下文
- 密码学验证
- 形式化验证
- 供应链安全
title: CONTINUITY：面向可组合大模型智能体控制的安全上下文契约
---
### 文章背景与核心概要

随着大语言模型（LLM）智能体系统日益复杂，它们越来越多地集成了各种不同的安全机制——例如溯源追踪、授权引擎、策略强制监视器、协议适配器以及执行控制。然而，行业内存在一个关键的漏洞：**各自独立的正确安全机制，不一定能组合成端到端安全的系统**。当安全攸关的上下文跨越组件边界时，它们可能会被丢弃、放宽、重新绑定或误解。本文识别并形式化了这种失效模式，将其命名为**安全上下文不连续性（security-context discontinuity）**，并推出了 **CONTINUITY**——一个旨在实现智能体安全控制可验证组合的全新框架。

CONTINUITY 通过使用**假设-保证契约（assume-guarantee contract）**对每个独立的系统组件进行建模，从而解决了安全上下文不连续的问题。它利用一套严密的密码学原语，在组件转换过程中维护经过身份验证的安全上下文，包括签名根授权、溯源承诺、绑定角色的转换回执等。评估结果表明，在包含 2,560 个参数化攻击实例的测试中，完整配置的 CONTINUITY 在攻击条件下实现了零有害外部副作用，同时在良性任务上保持了 100% 的成功率。

---

## 1. 执行摘要 (Executive Summary)

随着大语言模型（LLM）智能体系统日益复杂，它们越来越多地集成了各种不同的安全机制——例如溯源追踪、授权引擎、策略强制监视器、协议适配器以及执行控制。然而，行业内存在一个关键的漏洞：**各自独立的正确安全机制，不一定能组合成端到端安全的系统**。

> As Large Language Model (LLM) agent systems grow more complex, they increasingly integrate disparate security mechanisms—such as provenance tracking, authorization engines, policy enforcement monitors, protocol adapters, and execution controls. However, a critical gap exists: **individually correct security mechanisms do not necessarily compose into an end-to-end secure system**.

当安全攸关的上下文跨越组件边界时，它们可能会被丢弃、放宽、重新绑定或误解。本文识别并形式化了这种失效模式，将其命名为**安全上下文不连续性（security-context discontinuity）**，并推出了 **CONTINUITY**——一个旨在实现智能体安全控制可验证组合的全新框架。

> When security-critical contexts cross component boundaries, they can be dropped, widened, rebound, or misinterpreted. This paper identifies and formalizes this failure mode as **security-context discontinuity** and introduces **CONTINUITY**, a novel framework designed to achieve verifiable composition of agent security controls.

---

## 2. 核心概念与架构 (Key Concepts & Architecture)

CONTINUITY 通过使用**假设-保证契约（assume-guarantee contract）**对每个独立的系统组件进行建模，从而解决了安全上下文不连续的问题。它利用一套严密的密码学原语，在组件转换过程中维护经过身份验证的安全上下文：

> CONTINUITY addresses security-context discontinuity by modeling each individual system component with an **assume-guarantee contract**. It maintains authenticated security context across transitions utilizing a rigorous suite of primitives:

* **签名根授权（Signed Root Grants）：** 建立初始信任根。
* **溯源承诺（Provenance Commitments）：** 追踪数据和指令的起源与演变。
* **绑定角色的转换回执（Role-Bound Transition Receipts）：** 确保权限在交接过程中与智能体角色紧密耦合。
* **有界类型释放（Bounded Typed Releases）：** 在严格的类型约束下安全地降级或暴露数据。
* **转换见证（Transformation Witnesses）：** 密码学验证中间转换是否保留了安全不变量。
* **效果绑定的执行许可（Effect-Bound Execution Permits）：** 授予执行外部操作的精确且可撤销的权限。

> * **Signed Root Grants:** Establishing initial trust roots.
> * **Provenance Commitments:** Tracking the origin and evolution of data/instructions.
> * **Role-Bound Transition Receipts:** Ensuring permissions are tightly coupled to agent roles during handoffs.
> * **Bounded Typed Releases:** Safely downgrading or exposing data under strict type constraints.
> * **Transformation Witnesses:** Cryptographically verifying that intermediate transformations preserve security invariants.
> * **Effect-Bound Execution Permits:** Granting precise, revocable authority to execute external actions.

通过这些机制，该框架将**端到端结果完整性（end-to-end consequence integrity）**形式化，要求每一个已实现的外部效果都必须有有效且当前授权见证的支持，该见证需将主体、任务、溯源、委托、策略状态、规范动作以及终结边界紧密联系在一起。

> Through these mechanisms, the framework formalizes **end-to-end consequence integrity**, requiring that every realized external effect is backed by a valid, current authorization witness linking the principal, task, provenance, delegation, policy state, canonical action, and finality boundary.

---

## 3. 评估与结果 (Evaluation & Results)

为了验证该框架，作者实现了一个参考验证器，以及一个确定性的跨层故障注入套件，涵盖了四个独特应用域中的 32 个不同故障类别。

> To validate the framework, the authors implemented a reference verifier alongside a deterministic cross-layer fault-injection suite covering 32 distinct fault classes across four unique application domains.

* **测试规模（Test Scale）：** 评估跨越了 **2,560 个参数化攻击实例**，涵盖 128 个故障域类别。
* **良性性能（Benign Performance）：** 成功完成了 **所有 700 个良性任务（100%）**，且没有中断合法操作。
* **模糊案例（Ambiguous Cases）：** 成功将 **全部 200 个模糊案例** 升级，交由人在回路（human-in-the-loop）或高级仲裁处理。
* **对抗韧性（Adversarial Resilience）：** 在攻击条件下，完整配置的 CONTINUITY 实现了 **零有害外部副作用（zero harmful external effects）**。

> * **Test Scale:** Evaluated across **2,560 parameterized attack instances** spanning 128 fault-domain classes.
> * **Benign Performance:** Successfully completed **100% of all 700 benign tasks** without interrupting legitimate operations.
> * **Ambiguous Cases:** Successfully escalated **all 200 ambiguous cases** for human-in-the-loop or high-level arbitration.
> * **Adversarial Resilience:** The full CONTINUITY configuration committed **zero harmful external effects** under attack conditions.

---

## 4. 结论 (Conclusions)

这项研究表明，确保 LLM 智能体执行的安全需要的不仅仅是健全的单独安全控制。它需要明确的、可验证的契约，在从指令到效果的整个路径中维护安全保证。

> The research demonstrates that securing LLM agent execution requires more than sound individual security controls. It demands explicit, verifiable contracts that preserve security guarantees across the complete instruction-to-effect path.

---

*有关更多详细信息，请参考 [arXiv](https://arxiv.org/abs/2609.05269) 上的完整论文，或在 [GitHub](https://github.com/zast-ai/continuity) 上探索代码工件仓库。*

> *For further details, reference the full paper on [arXiv](https://arxiv.org/abs/2609.05269) or explore the code artifact repository on [GitHub](https://github.com/zast-ai/continuity).*