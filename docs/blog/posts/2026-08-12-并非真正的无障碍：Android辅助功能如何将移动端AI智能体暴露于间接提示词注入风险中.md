---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 移动端AI
- 提示词注入
- Android无障碍
- AI安全
- 漏洞分析
title: 并非真正的无障碍：Android辅助功能如何将移动端AI智能体暴露于间接提示词注入风险中
---
### 文章背景与核心概要
随着自主移动端AI智能体（如 *MobileRun* 和 *Mobile-Use*）的迅速发展，它们越来越依赖Android系统的辅助功能（A11y）树以及视觉截图来导航和操作移动应用程序。然而，最新的学术研究揭示了这种技术路线带来的严重安全隐患：由于这些框架会处理未经净化的辅助功能元数据和视觉输入，它们系统性地容易遭受“间接提示词注入”（Indirect Prompt Injection）攻击。

隐藏在用户界面中的对抗性提示词可以成功劫持智能体的目标、引发上下文漂移，并强制执行未经授权的设备操作。研究表明，采用不同大模型的智能体表现出不同的脆弱性（例如 *MobileRun* 的攻击成功率高达 0.822），这暴露出当前移动端智能体架构未能隔离语义上下文边界、盲目将环境文本信任为系统指令的核心缺陷。为此，作者提出了攻击分类法，并倡导实施零信任输入验证、专用安全智能体以及严格的上下文隔离机制。

---

# Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection

> # Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection

**arXiv:** [arXiv:2608.08939](https://arxiv.org/abs/2608.08939) [cs.AI]  
**DOI:** [10.48550/arXiv.2608.08939](https://doi.org/10.48550/arXiv.2608.08939)  
**Submitted on:** 9 August 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  

> **arXiv:** [arXiv:2608.08939](https://arxiv.org/abs/2608.08939) [cs.AI]  
> **DOI:** [10.48550/arXiv.2608.08939](https://doi.org/10.48550/arXiv.2608.08939)  
> **Submitted on:** 9 August 2026  
> **Primary Subject:** Artificial Intelligence (`cs.AI`)  

## Authors
* Rahul Deivasigamani  
* Sayeda Faatin Alvi  
* Derqui Andrea  
* Kaushal Punjabi  
* Stjepan Picek  

> ## Authors
> * Rahul Deivasigamani  
> * Sayeda Faatin Alvi  
> * Derqui Andrea  
> * Kaushal Punjabi  
> * Stjepan Picek  

---

## Summary

The paper investigates the security vulnerabilities introduced by autonomous mobile AI agents (such as *MobileRun* and *Mobile-Use*) that rely on Android accessibility (`A11y`) trees and visual screenshots to navigate mobile applications. 

> ## Summary
> 
> The paper investigates the security vulnerabilities introduced by autonomous mobile AI agents (such as *MobileRun* and *Mobile-Use*) that rely on Android accessibility (`A11y`) trees and visual screenshots to navigate mobile applications. 

The researchers demonstrate that because these frameworks process unsanitized accessibility metadata alongside visual inputs, they are systematically vulnerable to **indirect prompt injection**. Adversarial prompts hidden within user interfaces can successfully hijack agent goals, trigger context drift, and force unauthorized device actions. 

> The researchers demonstrate that because these frameworks process unsanitized accessibility metadata alongside visual inputs, they are systematically vulnerable to **indirect prompt injection**. Adversarial prompts hidden within user interfaces can successfully hijack agent goals, trigger context drift, and force unauthorized device actions. 

### Key Findings:
* **MobileRun** (using *Gemma4:31B*) achieved an attack success rate of **0.822**.
* **Mobile-Use** (using *Qwen3.6:35B*) reduced the success rate to **0.150**, though it still failed to completely prevent context drift and unauthorized actions.
* Current mobile agent architectures fail to isolate semantic context boundaries, inherently treating passive environmental text as trusted system instructions.

> ### Key Findings:
> * **MobileRun** (using *Gemma4:31B*) achieved an attack success rate of **0.822**.
> * **Mobile-Use** (using *Qwen3.6:35B*) reduced the success rate to **0.150**, though it still failed to completely prevent context drift and unauthorized actions.
> * Current mobile agent architectures fail to isolate semantic context boundaries, inherently treating passive environmental text as trusted system instructions.

### Proposed Solutions:
To counter these vulnerabilities, the authors outline a taxonomy of the attacks and advocate for:
1. **Zero-trust input validation**
2. **Dedicated security agents**
3. **Strict context isolation** within mobile agent architectures

> ### Proposed Solutions:
> To counter these vulnerabilities, the authors outline a taxonomy of the attacks and advocate for:
> 1. **Zero-trust input validation**
> 2. **Dedicated security agents**
> 3. **Strict context isolation** within mobile agent architectures

---

## Links & Resources
* [View PDF](https://arxiv.org/pdf/2608.08939)
* [HTML Version (Experimental)](https://arxiv.org/html/2608.08939v1)
* [TeX Source](https://arxiv.org/src/2608.08939)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08939) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08939)

> ## Links & Resources
> * [View PDF](https://arxiv.org/pdf/2608.08939)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.08939v1)
> * [TeX Source](https://arxiv.org/src/2608.08939)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.08939) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.08939)