---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- LLM安全
- 智能体技能
- 供应链攻击
- 组合式攻击
- 安全扫描
title: CompoSkill：由单个扫描通过的LLM智能体技能构成的组合式技能链攻击
---
### 文章背景与核心概要

随着自主AI智能体越来越依赖市场技能来处理长视距（long-horizon）任务，现有的安全机制通常对每个技能进行孤立评估。传统的安全扫描器会对单独的软件包给出安全判定，如果所有包都通过检测，则认为整个生态系统是安全的。

在 **CompoSkill** 这项研究中，作者证明了这种“单软件包假设”在*技能组合*的情况下会彻底失效。一个技能可能很容易通过单独检查，但当它与其他通过扫描的技能结合时（通过连接的输出、能力或副作用），就会变得具有极大的危险性。因此，安全风险表现为**路径级属性**而非**node-level（节点级）属性**，这也解释了为什么传统的逐个技能扫描器无法拦截复杂的智能体威胁。

---

# CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

**arXiv:** [arXiv:2608.16246 [cs.CR]]  
**DOI:** [10.48550/arXiv.2608.16246](https://doi.org/10.48550/arXiv.2608.16246)  
**Authors:** Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang  
**Submitted:** August 17, 2026  
**Subjects:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)  

> # CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills
> 
> **arXiv:** [arXiv:2608.16246 [cs.CR]]  
> **DOI:** [10.48550/arXiv.2608.16246](https://doi.org/10.48550/arXiv.2608.16246)  
> **Authors:** Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang  
> **Submitted:** August 17, 2026  
> **Subjects:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)  

---

## 📋 Summary

随着自主AI智能体越来越依赖市场技能来处理长视距任务，现有的安全机制对每个技能进行孤立评估。安全扫描器通常对单个软件包返回安全判定，如果所有包都通过，则认为生态系统是安全的。

在 **CompoSkill** 中，作者证明了这种单软件包假设在*技能组合*下会崩溃。一个技能可以轻松通过单独检查，但当与其他通过扫描的技能结合时（通过连接的输出、能力或副作用），就会变得危险地具有恶意。因此，安全风险作为**路径级属性**而不是**节点级属性**出现，这解释了为什么传统的逐个技能扫描器无法拦截复杂的智能体威胁。

> ## 📋 Summary
> 
> As autonomous AI agents increasingly rely on marketplace skills to handle long-horizon tasks, current security mechanisms evaluate each skill in isolation. A security scanner typically returns a safety verdict for individual packages and deems the ecosystem secure if all packages pass. 
> 
> In **CompoSkill**, the authors demonstrate that this single-package assumption collapses under *skill composition*. A skill may easily pass individual inspection, yet become dangerously malicious when combined with other scanner-passing skills (through connected outputs, capabilities, or side effects). Consequently, security risks emerge as **path-level properties** rather than **node-level properties**, explaining why traditional per-skill scanners fail to intercept complex agent threats.

---

## 🔍 Key Highlights & Methodology

* **威胁模型：** 本文介绍了 *CompoSkill*，这是一个旨在建模技能组合攻击的框架，利用双攻击者系统：
  * **白盒攻击者：** 完全了解受害者的已安装技能池，直接注入显式的技能ID序列。
  * **黑盒攻击者：** 仅了解高层角色配置文件，下载该场景下的顶级市场技能，构建*技能组合图*，并搜索隐式诱饵从不显式命名目标技能标识符的高风险链。
* **CompoSkill-Bench：** 一个专门的基准测试，包含 1,140 条记录，这些记录生成自跨 **五种不同威胁** 和 **六种场景** 的长视距专业工作流，运行于 *OpenClaw* 和 *Nanobot* 等框架上。
* **评估与发现：**
  * 在白盒设置下实现了高达 **83.3%** 的风险链形成率（CFR），在黑盒设置下实现了 **80.6%**，轻松避开了标准的逐个技能扫描器。
  * 识别出一种**“桥接加成随后跳跃衰减”（"bridge-bonus-then-hop-decay"）**模式：虽然桥接技能最初可以提高攻击成功率，但如果风险链延伸超过三个技能，攻击成功率（ASR）就会下降。

> ## 🔍 Key Highlights & Methodology
> 
> * **The Threat Model:** The paper introduces *CompoSkill*, a framework designed to model skill composition attacks utilizing a dual-attacker system:
>   * **White-Box Attacker:** Fully aware of the victim's installed skill pool, directly injecting explicit skill-ID sequences.
>   * **Black-Box Attacker:** Knows only the high-level role profile, downloads top marketplace skills for the scenario, builds a *Skill Composition Graph*, and searches for high-risk chains whose implicit lures never explicitly name target skill identifiers.
> * **CompoSkill-Bench:** A specialized benchmark comprising 1,140 records generated from long-horizon professional workflows across **five distinct threats** and **six scenarios** on frameworks like *OpenClaw* and *Nanobot*.
> * **Evaluation & Findings:**
>   * Achieves risk Chain Formation Rates (CFR) up to **83.3%** in the white-box setting and **80.6%** in the black-box setting, easily evading standard per-skill scanners.
>   * Identifies a **"bridge-bonus-then-hop-decay"** pattern: while a bridge skill initially improves attack success, the Attack Success Rate (ASR) drops if the risk chain extends beyond three skills.

---

## 🔗 Links & Resources

* [查看 PDF](https://arxiv.org/pdf/2608.16246)
* [TeX 源码](https://arxiv.org/src/2608.16246)
* [HTML（实验性）](https://arxiv.org/html/2608.16246v1)

> ## 🔗 Links & Resources
> 
> * [View PDF](https://arxiv.org/pdf/2608.16246)
> * [TeX Source](https://arxiv.org/src/2608.16246)
> * [HTML (Experimental)](https://arxiv.org/html/2608.16246v1)