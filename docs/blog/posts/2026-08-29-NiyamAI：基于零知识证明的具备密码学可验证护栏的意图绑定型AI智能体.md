---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 人工智能
- 零知识证明
- AI安全
- 大语言模型智能体
- 密码学护栏
title: NiyamAI：基于零知识证明的具备密码学可验证护栏的意图绑定型AI智能体
---
### 文章背景与核心概要
随着大语言模型（LLM）智能体在工具调用和自主执行能力上的不断提升，提示词注入、目标劫持和未授权操作等关键安全漏洞日益凸显。传统的安全护栏通常依赖于本地软件过滤器、语义分类器和策略引擎，它们与智能体运行在相同的不可信环境中，无法向外部观察者提供策略执行正确的客观证明。

为此，本文提出了 **NiyamAI**。这是一种意图绑定的运行时护栏架构，旨在为自主智能体确保具备密码学可验证性的执行完整性。通过引入不可变意图合约、确定性权限网关、神经判断器（Neural Judge）以及零知识证明（zkSNARKs），NiyamAI 能够在不泄露模型参数的前提下，以极低的性能开销为每一次工具调用生成简洁的密码学证明，从根本上保障AI智能体在既定安全边界内运行。

---

## 📌 Summary

> Autonomous Large Language Model (LLM) agents equipped with tool execution capabilities face critical security vulnerabilities such as prompt injection, goal hijacking, and unauthorized actions. Traditional guardrails rely on local software filters, semantic classifiers, and policy engines that operate within the same untrusted environment as the agent—providing no verifiable proof of correct policy execution to external observers.

具备工具执行能力的大语言模型（LLM）自主智能体面临着严峻的安全漏洞，例如提示词注入、目标劫持以及未授权操作。传统的安全护栏依赖于本地软件过滤器、语义分类器和策略引擎，这些组件与智能体运行在相同的不可信环境中，无法为外部观察者提供策略执行正确的切实证明。

> This paper introduces **NiyamAI**, an intent-bound runtime guardrail architecture that ensures cryptographically verifiable execution integrity for autonomous agents. 

本文介绍了 **NiyamAI**，这是一种意图绑定的运行时护栏架构，可为自主智能体确保具备密码学可验证性的执行完整性。

> ### Key Innovations:
> * **Immutable Intent Contracts:** At session initialization, permitted tools and operational constraints are locked into an immutable Intent Contract protected by a SHA-256 commitment.
> * **Deterministic Authority Gate & Neural Judge:** Every tool invocation is intercepted and classified by a dedicated feedforward neural Judge network ($11 \rightarrow 8 \rightarrow 2$).
> * **Zero-Knowledge Proofs (zkSNARKs):** For every authorized action, NiyamAI generates a succinct zkSNARK proof certifying correct policy evaluation under the committed contract. Actions only execute after successful proof verification.
> * **Robust Performance:** Across 2,000 AgentSafetyBench scenarios, NiyamAI achieves an **88.8% F1 score** at a 1.0% false positive rate, significantly outperforming existing baselines (Llama Prompt Guard 2, GPTOSSSafeguard, and NeMo Guardrails) with statistical significance ($p < 0.0001$).
> * **Low Overhead:** Proof generation adds only 1.7 seconds per approved action, verification takes 51 ms, and proofs are a compact 18.6 KB—verifiable by any third party without accessing model parameters.

### 核心创新点：
* **不可变意图合约（Immutable Intent Contracts）：** 在会话初始化时，允许使用的工具和操作约束会被锁定在一个由 SHA-256 承诺保护的不可变意图合约中。
* **确定性权限网关与神经判断器（Deterministic Authority Gate & Neural Judge）：** 每一个工具调用都会被拦截，并由专用的前馈神经判断网络（$11 \rightarrow 8 \rightarrow 2$）进行分类。
* **零知识证明（zkSNARKs）：** 针对每一次授权操作，NiyamAI 都会生成一个简洁的 zkSNARK 证明，以证明其在已承诺的合约下进行了正确的策略评估。只有在证明验证成功后，操作才会执行。
* **强劲的性能表现：** 在 2,000 个 AgentSafetyBench 场景测试中，NiyamAI 在误报率为 1.0% 的情况下实现了 **88.8% 的 F1 分数**，在统计学意义上显著优于现有的基准模型（Llama Prompt Guard 2、GPTOSSSafeguard 和 NeMo Guardrails），显著性水平为 $p < 0.0001$。
* **低开销：** 每个被批准的操作仅增加 1.7 秒的证明生成时间，验证仅需 51 毫秒，且证明体积紧凑（仅 18.6 KB）——任何第三方都可以在无需访问模型参数的情况下对其进行验证。

---

## 🔗 Links & Resources

> * **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.07167)
> * **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
>   <img alt="license icon" role="presentation" src="./images/079cd8198ba3.png" />
> * **Citations & References:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07167), [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07167), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07167)

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2608.07167)
* **开源许可：** [知识共享 署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
  <img alt="license icon" role="presentation" src="./images/079cd8198ba3.png" />
* **引用与参考：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07167)、[谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07167)、[Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07167)