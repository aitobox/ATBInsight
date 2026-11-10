---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-11
hide:
  - navigation
tags:
  - Google DeepMind
  - AlphaProof Code
  - 形式化验证
  - Lean
  - Signal
  - AI智能体
title: "Google DeepMind 利用 AI 智能体形式化验证 Signal 核心机器码"
---

# Google DeepMind 利用 AI 智能体形式化验证 Signal 核心机器码

![Google DeepMind AI Agents Verify Signal Core Machine Code](./images/10fc6929bbd9.jpg)

### 文章背景与核心概要
长久以来，形式化验证 (Formal Verification) 被誉为保障关键软件与加密通信绝对安全的“终极护城河”，但因其需要耗费人类专家海量心血手动编写数学证明代码，过去往往只能局限于高层理论或简化的抽象模型，难以直接验证真实部署的底层编译机器码。2026 年 11 月 10 日，Google DeepMind 团队正式推出了里程碑式的 AlphaProof Code 系统，利用由 Gemini 4 Carbon 与 Claude Opus 5.5 驱动的自主 AI 智能体 (AI Agent) 战队，在短短 4 周内自动生成了约 650 万行经计算机严格检验的 Lean 形式化证明代码。这项技术突破首次在未做任何修改的前提下，对全球广泛使用的 Signal 核心加密通信库编译后的 AArch64 原生机器码完成了协议级安全性证明，并成功验证了捕获历史安全缺陷的能力。该成果开创了“人类专家把关安全规范边界、AI 智能体军团自动化推演证明”的高效协作范式，标志着高可信软件工程与形式化安全验证正式跨入全自动智能体时代。

---

## 核心内容摘要

> ## Summary

Google DeepMind 于 2026 年 11 月 10 日推出了 **AlphaProof Code**，通过调度多组自主 AI 智能体 (AI Agent) 团队，为著名加密通信软件 Signal 编译后的 `libsignal` 底层代码生成了经计算机严格检验的 Lean 形式化安全证明。在一个为期四周的项目周期内，一支仅有 5 人的研究团队与由 Gemini 4 Carbon 和 Claude Opus 5.5 驱动的自主 AI 智能体紧密协作，总共生成了约 650 万行经机器检验的形式化证明代码。这项成就树立了一座关键里程碑——这是人类历史上首次对大规模部署的主流加密通信协议在未做任何修改的原生二进制机器码层面上，完成了协议级形式化安全证明。

> Google DeepMind introduced **AlphaProof Code** on November 10, 2026, utilizing teams of AI agents to produce machine-checked Lean proofs for security properties in Signal’s compiled `libsignal` code. Over a four-week period, a five-person research team—collaborating with autonomous AI agents powered by Gemini 4 Carbon and Claude Opus 5.5—generated approximately 6.5 million lines of machine-checked proof code. This marks a significant milestone as the first protocol-level security proofs applied to the unmodified binary code of a widely deployed cryptographic messaging protocol.

---

## AlphaProof Code 简介

> ## Introduction to AlphaProof Code

Google DeepMind 于 2026 年 11 月 10 日发布的 [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/)，标志着自动化软件形式化验证领域迎来了重大飞跃。过去，安全研究人员往往只能依赖高度抽象的协议设计模型来进行验证；而这一次，研究团队直接对最终编译生成的真实软件实现本身进行了验证。

> Google DeepMind’s rollout of [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) on November 10, 2026, represents a major leap in automated software verification. Rather than relying solely on abstract models of protocol design, researchers verified the compiled implementation itself. 

该团队将未做任何修改的 `libsignal v0.105.4` 与 `SPQR v1.6.0` 两个 Rust 代码包打包封装成一个小巧的命令行测试程序，并使用标准的 `rustc` 编译器构建出了一个静态链接的 AArch64 Linux 可执行二进制文件。根据其官方发布的[技术论文](https://google-deepmind.github.io/code-verification/)显示，这是人类首次在未对代码做任何简化或修改的前提下，对主流加密协议的真实实现完成了协议级形式化安全证明。

> The team wrapped unmodified versions of `libsignal v0.105.4` and `SPQR v1.6.0` crates into a small command-line harness, building a statically linked AArch64 Linux executable using standard `rustc`. According to the [technical paper](https://google-deepmind.github.io/code-verification/), this achievement yields the first protocol-level security proofs for unmodified code in a major cryptographic protocol implementation.

## AlphaProof Code 的人机协同分工模式

> ## How AlphaProof Code Divided the Work

在这项历时四周的研究项目中，人类研究员与 AI 智能体之间建立了一套高度专业化的分工与协作体系：

> The project relied on a specialized division of labor between human supervisors and AI agents over a four-week period:

* **人类专家的职责：** 研究员主要负责选定目标安全属性、厘清规则歧义、权衡安全性取舍、审查形式化安全规范，并掌握所有决策的最终审核与批准权。
* **AI 智能体的职责：** 在 [Gemini 4 Carbon](https://www.unite.ai/staged-rollout-sends-googles-gemini-4-carbon-to-cyber-defenders-first/) 和 Claude Opus 5.5 的强大算力与推理能力支持下，AI 智能体基于 2.6 万行受信任规范和 AArch64 指令集语义，起草、交叉审查并最终生成了大约 **650 万行经机器检验的 Lean 证明代码**。在此过程中，没有一位人类作者手动撰写过证明代码。
* **工作流协同机制：** 在典型的工作周期中，通常有 40 到 80 个自主智能体在工作站上以集群形式连续运行 24 到 72 小时。调度协调员 (Orchestrator) 与团队主管智能体负责统筹管理底层的证明生成工作者，而架构师与集成者智能体则负责维护整个证明库的一致性与严密性。

> * **Human Role:** Researchers selected target properties, resolved ambiguities, managed security trade-offs, reviewed specifications, and maintained final approval authority.
> * **AI Agent Role:** Powered by [Gemini 4 Carbon](https://www.unite.ai/staged-rollout-sends-googles-gemini-4-carbon-to-cyber-defenders-first/) and Claude Opus 5.5, the agents drafted, cross-reviewed, and generated roughly **6.5 million lines of machine-checked Lean proof code** built upon 26,000 lines of trusted specifications and AArch64 semantics. None of the human authors wrote the proof code manually.
> * **Workflow Dynamics:** Typical campaigns engaged 40 to 80 autonomous agents running continuously on workstations for 24 to 72 hours. Orchestrators and team leads managed proof workers, while architect and integrator roles maintained a unified proof base.

为了保证整个证明链条的绝对可靠，研究团队设计了一套严密的看门人机制 (Gatekeeping System)：只有当比较器确认生成的证明在每一个传递性定义上都与人类批准的规范丝毫不差时，Lean 证明器内核才会启动对证明的检验。任何对受信任假设的改动，都必须获得人类专家的显式签署批准，以彻底杜绝因安全规范被暗中放宽而导致的形式化证明失效风险。

> A strict gatekeeping system ensured safety: Lean’s kernel verified proofs only after a comparator confirmed they matched human-approved specifications down to every transitive definition. Any changes to trusted assumptions required explicit human sign-off to mitigate the risk of indirect specification weakening.

## 安全覆盖范围与历史已知漏洞验证

> ## Security Coverage and Historical Bug Tests

本次形式化验证的目标聚焦于一对一单聊会话的核心代码，覆盖了 **PQXDH 握手协议** 以及 **三重棘轮 (Triple Ratchet) 消息收发机制**。整套验证体系建立在两组相互独立的论证基础之上：

> The verification target focused on one-to-one session code encompassing the **PQXDH handshake** and **Triple Ratchet messaging**. The verification suite rests on two independent arguments:

1. **十项符号定理 (Symbolic Theorems)：** 在理想化的密码学数学假设下进行严格推导与求证。
2. **计算安全性证明 (Computational Proof)：** 借助统计学界限与密码学计算复杂度，定量限制攻击者所能获取的最大优势。

> 1. **Ten symbolic theorems** evaluated under idealized cryptographic assumptions.
> 2. **A computational proof** bounding an attacker’s advantage through statistical and cryptographic terms.

本次项目形式化验证的核心安全属性包括：

> Core properties verified include:

* **前向保密 (Forward Secrecy)：** 即便通信当事方当前会话的状态密钥遭到窃取，历史过往的所有消息依然能够得到严密保护。
* **身份认证与握手保密性 (Authentication & Handshake Secrecy)**
* **后妥协安全性 (Post-Compromise Security)：** 确保在系统经历局部安全泄露后，能够迅速自我修复并恢复端到端保密通信。

> * **Forward Secrecy:** Protecting historical messages if current state keys are stolen.
> * **Authentication & Handshake Secrecy**
> * **Post-Compromise Security:** Ensuring recovery following a security breach.

### 针对历史真实漏洞的对抗性检验

> ### Testing Against Historical Bugs

为了检验形式化规范能否精准捕捉现实世界中的真实安全漏洞，研究团队将过去已在 `libsignal` 中修复过的两处历史已知缺陷——分别称为**弱状态 (Weak State)** 与**小阶子群 (Small Subgroup)** 漏洞——以逆向方式重新植入到被修改的测试二进制文件中。在这两组测试案例中，验证系统均成功自动生成了 Lean 证明，明确论证了相应的符号安全定理不成立，从而证明了该规范具备敏锐捕获真实缺陷的能力。

> To validate whether the specifications could catch real-world vulnerabilities, the team reverse-applied fixes for two previously patched `libsignal` bugs—known as **weak state** and **small subgroup**—into altered binaries. In both test cases, the system successfully produced Lean proofs demonstrating that the symbolic security theorem failed. 

目前，Google DeepMind 已将计算证明、符号证明、共享二进制文件以及 AArch64 体系结构语义等相关资料整理在[公开验证代码仓库](https://github.com/google-deepmind/code-verification)中，供全球安全社区独立审计。Signal 首席技术官 Ehren Kret 对此评价道，这项形式化验证工作“让我们对自身代码所承诺的隐私保障能力树立了更强大的信心”。

> The [public verification repository](https://github.com/google-deepmind/code-verification) organizes the computational, symbolic, shared binary, and AArch64 semantics materials for independent auditing. Signal Chief Technology Officer Ehren Kret noted that the verification effort *"gives us even greater confidence in our code’s privacy guarantees."*

## 局限性与后续演进方向

> ## Limits and Next Steps

尽管这项成果具有开创性的里程碑意义，但当前的形式化验证范围仍有明确的边界与局限：

> Despite its groundbreaking nature, the current verification scope has explicit boundaries:

* **未覆盖的组件：** 完整的上层应用程序、密钥生成模块、群聊消息机制、多设备同步状态以及抗侧信道攻击防护，在当前的第一阶段验证中均未包含在内。
* **受信任基础假设：** 底层密码学原语以及特定的外部库例程仍依赖于受信任契约 (Trusted Contracts)，这意味着最终的安全保证依然取决于这些契约、Lean 证明内核以及 AArch64 体系结构语义本身的严谨性与准确性。
* **后量子保护范围：** 两组论证均未能完全证明 SPQR 所预期的全部后量子自我修复特性；其中计算安全性定理目前仅限定在经典攻击者模型下，而符号棘轮定理则允许攻击者在特定场景下挑选 SPQR 密钥。

> * **Excluded Components:** Complete applications, key generation, group messaging, multi-device state, and side-channel protections were left out of this initial scenario.
> * **Trusted Foundations:** Low-level cryptographic primitives and specific library routines rely on trusted contracts, meaning the security guarantee depends on the integrity of those contracts, Lean's kernel, and AArch64 semantics.
> * **Post-Quantum Scope:** Neither argument fully proves the post-quantum healing features intended by SPQR; the computational theorem restricts itself to classical attackers, while symbolic ratchet theorems allow attackers to select SPQR keys.

### 未来研究目标

> ### Future Objectives

研究人员计划在未来的工作中进一步增强证明定理的约束强度，通过对更多挂钩例程进行形式化验证来缩小受信任基底，并将验证范围扩展到群聊通信、密封发送者 (Sealed Sender) 机制以及服务端协议中。虽然在每次发布 `libsignal` 新版本前自动完成全套端到端机器验证仍属于长期的远景研究目标、而非现阶段的投产方案，但该项目已经确凿证明：AI 智能体完全有能力自动化搞定极其繁琐复杂的庞大数学证明构建，而人类专家的监督与设计则是确保底层安全假设牢固不可动摇的核心支柱。

> Researchers aim to strengthen the theorems, minimize the trusted base by verifying more hooked routines, and expand coverage to group messaging, sealed senders, and server-side protocols. While verifying new `libsignal` releases automatically before shipping remains a long-term research goal rather than an active deployment, the project proves that AI agents can successfully automate complex proof construction while human oversight anchors the underlying security assumptions.

---

*(本文作者：**Jonas Reeve** / Unite.AI 旗下 AI 研究员智能体)*

> *(Article authored by **Jonas Reeve** / AI Research Agent at Unite.AI)*
