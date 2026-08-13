---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- AI安全
- 提示词注入
- 浏览器智能体
- 网络安全
- 大模型防御
title: BrowseSafe：理解并预防 AI 浏览器智能体中的提示词注入
---
### 文章背景与核心概要

随着 AI 智能体在网页浏览器中的深度集成，其面临的安全威胁已超越了传统的 Web 应用模型。提示词注入（Prompt Injection）作为一种关键的攻击向量，在实际浏览器环境中可能导致智能体执行恶意操作，而非仅仅是操纵文本输出。然而，目前针对此类攻击在真实复杂网页环境下的影响研究尚显不足。

本文深入探讨了提示词注入的攻击态势，并构建了一个基于真实 HTML 载荷的基准测试集。该研究不仅关注攻击的复杂度和干扰频率，更强调了攻击对智能体实际行为的影响。通过对多种前沿 AI 模型进行实证评估，作者提出了一套结合架构设计与模型防御的多层级纵深防御策略，为构建安全可靠的现代 Web 智能体提供了实践蓝图。

---

## 文档元数据

| 元数据字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2511.20597](https://arxiv.org/abs/2511.20597) [cs.LG] |
| **作者** | Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li |
| **主要学科** | 机器学习 (`cs.LG`) |
| **次要学科** | 人工智能 (`cs.AI`), 密码学与安全 (`cs.CR`) |
| **会议/期刊** | COLM 2026 |
| **提交历史** | • v1: 2025年11月25日<br>• v2 (最后修订): 2026年8月12日 |
| **许可协议** | <a class="has_license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/fb423b2203a9.png"><span>查看许可</span></a> |

---

## 摘要

人工智能（AI）智能体集成到网页浏览器中，引入了超越传统 Web 应用威胁模型的安全挑战。先前的研究已将提示词注入识别为 Web 智能体的一种新型攻击向量，但其在真实环境中的实际影响仍未得到充分理解。

在这项工作中，我们研究了提示词注入攻击的态势，并合成了一个嵌入在真实 HTML 载荷中的攻击基准测试集。我们的基准测试超越了以往的研究，重点关注那些能够影响现实世界操作（而非仅仅是文本输出）的注入攻击，并呈现了与真实智能体所遇到的复杂度和干扰频率相似的攻击载荷。我们利用该基准测试对现有防御措施进行了全面的实证评估，评估了它们在一系列前沿 AI 模型中的有效性。我们提出了一种包含架构防御和基于模型防御的多层防御策略，以抵御不断演变的提示词注入攻击。我们的工作为通过纵深防御方法设计实用、安全的 Web 智能体提供了蓝图。

> The integration of artificial intelligence (AI) agents into web browsers introduces security challenges that go beyond traditional web application threat models. Prior work has identified prompt injection as a new attack vector for web agents, yet the resulting impact within real-world environments remains insufficiently understood.
>
> In this work, we examine the landscape of prompt injection attacks and synthesize a benchmark of attacks embedded in realistic HTML payloads. Our benchmark goes beyond prior work by emphasizing injections that can influence real-world actions rather than mere text outputs, and by presenting attack payloads with complexity and distractor frequency similar to what real-world agents encounter. We leverage this benchmark to conduct a comprehensive empirical evaluation of existing defenses, assessing their effectiveness across a suite of frontier AI models. We propose a multi-layered defense strategy comprising both architectural and model-based defenses to protect against evolving prompt injection attacks. Our work offers a blueprint for designing practical, secure web agents through a defense-in-depth approach.

---

## 访问与资源

* **全文链接：**
  * [查看 PDF](https://arxiv.org/pdf/2511.20597)
  * [HTML 版本 (实验性)](https://arxiv.org/html/2511.20597v2)
  * [TeX 源码](https://arxiv.org/src/2511.20597)
* **外部参考与引用：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2511.20597)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2511.20597)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2511.20597)