---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- AI安全
- 零知识证明
- 智能体
- zk-SNARKs
- 大语言模型
title: NiyamAI：一个基于零知识证明构建、具备密码学可验证护栏的意图绑定型AI智能体
---
### 文章背景与核心概要
随着大语言模型（LLM）自主智能体日益具备执行高影响力操作（如发送电子邮件、查询数据库或运行系统指令）的能力，它们也成为了提示词注入、幻觉推理以及不安全工具执行的主要攻击目标。传统的安全防御依赖于运行在攻击目标同一台机器上的软件检查（如系统提示词或策略过滤器），这天然缺乏可验证的执行证明。为此，Niyam-AI 提出了一种新颖的框架，通过零知识密码学使安全执行变得数学上可证明。

该框架的核心在于“意图合约”（Intent Contracts）、隔离的裁判模型验证以及零知识证明（zk-SNARKs）。在会话开始时，允许使用的工具和安全约束会被锁定在“意图合约”中，并通过 SHA-256 进行提交；随后，智能体的每一次工具调用都会被隔离的裁判模型拦截并验证；一旦通过验证，便会使用 EZKL 生成 zk-SNARK 证明，工具仅在通过密码学验证后才会执行。这种方法允许第三方在不泄露敏感裁判模型权重的情况下，审计安全执行情况，为AI智能体的安全性带来了突破性的保障。

---

# NiyamAI: An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs

**arXiv:** [arXiv:2608.07167 [cs.AI]](https://arxiv.org/abs/2608.07167)  
**Authors:** Aditya Katkar, Om Karkele, Kartik Mandhane, Manisha More, Yash Kashid  
**Submitted:** August 7, 2026  

> **arXiv:** [arXiv:2608.07167 [cs.AI]](https://arxiv.org/abs/2608.07167)  
> **Authors:** Aditya Katkar, Om Karkele, Kartik Mandhane, Manisha More, Yash Kashid  
> **Submitted:** August 7, 2026  

---

## 📌 Summary

自主大语言模型（LLM）智能体正日益具备执行高影响力操作的能力——例如发送电子邮件、查询数据库或运行系统指令，这使它们成为提示词注入、幻觉推理以及不安全工具执行的主要攻击目标。

> Autonomous Large Language Model (LLM) agents are increasingly capable of executing high-impact actions—such as sending emails, querying databases, or running system commands—making them prime targets for prompt injection, hallucinated reasoning, and unsafe tool execution. 

传统的安全防御依赖于运行在攻击者所针对的同一台机器上的软件检查（如系统提示词或策略过滤器），这天然缺乏可验证的执行证明。**Niyam-AI** 引入了一种新颖的框架，通过零知识密码学使安全执行变得数学上可证明：

> Traditional safety defenses rely on software checks (like system prompts or policy filters) running on the exact same machine an attacker targets, which inherently lacks verifiable execution proof. **Niyam-AI** introduces a novel framework that makes safety enforcement mathematically provable through zero-knowledge cryptography:

* **意图合约（Intent Contracts）：** 在会话开始时，允许使用的工具和安全约束被锁定在“意图合约”中，并通过 SHA-256 进行提交。
* **隔离的裁判验证（Isolated Judge Validation）：** 智能体的每一次工具调用都会被拦截，并由一个隔离的裁判模型进行验证。
* **零知识证明（Zero-Knowledge Proofs, zk-SNARKs）：** 一旦通过验证，便会使用 EZKL 生成 zk-SNARK 证明。工具*仅在*通过密码学验证后才会执行，这使得第三方能够在不暴露敏感裁判模型权重的前提下，审计安全执行情况。

> * **Intent Contracts:** At the start of a session, permitted tools and security constraints are locked into an "Intent Contract" and committed via SHA-256.
> * **Isolated Judge Validation:** Every agent tool call is intercepted and validated by an isolated Judge model.
> * **Zero-Knowledge Proofs (zk-SNARKs):** Upon passing validation, a zk-SNARK proof is generated using EZKL. Tools execute *only* after cryptographic verification, allowing third parties to audit safety enforcement without exposing sensitive Judge model weights.

---

## 📊 Evaluation & Results

通过在来自 **Agent-SafetyBench** 的 2,000 个真实世界场景上进行评估，并采用 5 折分层交叉验证，Niyam-AI 在零样本基线（NeMo Guardrails、Meta 的 Llama Prompt Guard 2 以及 OpenAI 的 GPT-OSS-Safeguard）面前展现出了显著的性能优势：

> Evaluated on 2,000 real-world scenarios from **Agent-SafetyBench** using 5-fold stratified cross-validation, Niyam-AI demonstrated significant performance advantages over zero-shot baselines (NeMo Guardrails, Meta's Llama Prompt Guard 2, and OpenAI's GPT-OSS-Safeguard):

* **性能表现：** 达到了 **88.5% 的 F1 分数**，且误报率极低，仅为 **1.1%**（自助法 95% 置信区间：[85.19%, 91.88%]，$N = 1000$）。
* **统计显著性：** 麦克尼马尔精确配对检验（McNemar's exact paired test）证实其在所有基线对比中均表现更优（所有情况下的 $p < 0.0001$）：
  * 在与 NeMo 的不一致场景对比中赢了 **390** 场（输 20 场）。
  * 在与 Prompt Guard 2 的对比中赢了 **115** 场（输 13 场）。
  * 在与 GPT-OSS-Safeguard 的对比中赢了 **384** 场（输 19 场）。
* **性能开销：** 
  * 证明生成为每个批准的操作增加 **$2260.6 \pm 218.4\text{ ms}$** 的延迟。
  * 证明验证耗时 **$53.1 \pm 11.8\text{ ms}$**。

> * **Performance:** Achieved an **F1 score of 88.5%** with a low **1.1% false-positive rate** (bootstrap 95% CI: [85.19%, 91.88%], $N = 1000$).
> * **Statistical Significance:** McNemar's exact paired test confirmed superior performance against all baselines ($p < 0.0001$ in all cases):
>   * Won **390** discordant scenarios against NeMo (vs. 20 losses).
>   * Won **115** against Prompt Guard 2 (vs. 13 losses).
>   * Won **384** against GPT-OSS-Safeguard (vs. 19 losses).
> * **Performance Overhead:** 
>   * Proof generation adds **$2260.6 \pm 218.4\text{ ms}$** per approved action.
>   * Proof verification takes **$53.1 \pm 11.8\text{ ms}$**.

---

## 🔗 Additional Resources

* [在 arXiv 上查看 PDF](https://arxiv.org/pdf/2608.07167)
* [DOI 链接](https://doi.org/10.48550/arXiv.2608.07167)
* **许可证：** [知识共享署名-非商业性使用-相同方式共享 4.0 国际版](http://creativecommons.org/licenses/by-nc-sa/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/079cd8198ba3.png"><span>view license</span></a>

> * [View PDF on arXiv](https://arxiv.org/pdf/2608.07167)
> * [DOI Link](https://doi.org/10.48550/arXiv.2608.07167)
> * **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/079cd8198ba3.png"><span>view license</span></a>