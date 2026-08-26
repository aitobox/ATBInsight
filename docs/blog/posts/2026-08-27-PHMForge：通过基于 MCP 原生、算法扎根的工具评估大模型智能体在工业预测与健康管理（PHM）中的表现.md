---
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- PHMForge
- 模型上下文协议
- 工业智能体
- 预测与健康管理
- 大语言模型评估
title: PHMForge：通过基于 MCP 原生、算法扎根的工具评估大模型智能体在工业预测与健康管理（PHM）中的表现
---
### 文章背景与核心概要

在安全关键型的工业领域中，大语言模型（LLM）智能体正逐步通过模型上下文协议（MCP）来调用资产管理工具。然而，它们能否在该底层技术上可靠地执行预测与健康管理（PHM）任务，此前并未得到充分验证。传统的基准测试往往将协议的流利度与逻辑推理混为一谈，将工具本身的局限与智能体的故障相混淆，同时也未能区分工具的使用和工具的检索。

为了填补这一空白，本文推出了 **PHMForge**——一个专门用于评估 LLM 智能体在 PHM 任务中可靠性的全新评估环境。该框架包含了由领域专家（SME）编写的 99 个典型工业场景，覆盖旋转机械、航空发动机和锂离子电池等 8 大工业资产类别，并借助 NASA PCoE 等公开数据集提供服务。同时，PHMForge 封装了 39 个基于 MCP 原生的工具，涵盖了 C-MAPSS、ISO 10816、阿伦尼乌斯容量衰减模型及时间序列基础模型等主流 PHM 算法。

实验结果表明，在多款智能体框架和 LLM 基干模型的组合中，最优配置达到了 **80.8% 的 pass@1** 准确率，剩余的错误主要集中在任务编排和工具调用顺序上，而非模式有效性问题。更重要的是，消融实验证明，如果用基于文本的静态检索增强生成（RAG）来代替 MCP 工具的动态执行，电池剩余寿命（RUL）的预测性能将从 **100% 暴跌至 20%**，这充分凸显了算法扎根工具在预测性计算中不可替代的核心价值。

---

## 📌 摘要与核心亮点

> **PHMForge** is a novel evaluation environment designed to test the reliability of Large Language Model (LLM) agents on safety-critical *Prognostics and Health Management (PHM)* tasks. Traditional benchmarks often conflate protocol fluency with reasoning, and tool use with tool retrieval. PHMForge addresses these limitations by providing:
> * **99 SME-authored scenarios** across 8 industrial asset classes (rotating equipment, aero-engines, lithium-ion cells) using public datasets like NASA PCoE.
> * **39 MCP-native tools** wrapping standard PHM algorithms (C-MAPSS, ISO 10816, Arrhenius capacity-fade models, time-series foundation models).
> * **Deterministic evaluators, public leaderboards, and a comprehensive datasheet.**
> 
> Experimental results show that the top configuration achieves **80.8% pass@1** across frameworks and backbones, revealing that remaining errors stem primarily from orchestration and tool-sequencing rather than schema validity. Furthermore, architectural ablations demonstrate that replacing MCP tool execution with static text-based RAG causes the Remaining Useful Life (RUL) performance to collapse from **100% to 20%**, underscoring the necessity of algorithm-grounded tools for prognostic computing.

**PHMForge** 是一个新颖的评估环境，旨在测试大语言模型（LLM）智能体在安全关键型*预测与健康管理（PHM）*任务中的可靠性。传统的基准测试经常将协议流畅度与推理能力混为一谈，也将工具使用与工具检索混淆。PHMForge 通过以下方式解决了这些局限性：
* **99 个由领域专家（SME）编写的场景**，跨越 8 个工业资产类别（包括旋转机械、航空发动机、锂离子电池），并使用 NASA PCoE 等公开数据集。
* **39 个 MCP 原生工具**，封装了标准的 PHM 算法（如 C-MAPSS、ISO 10816、阿伦尼乌斯容量衰减模型、时间序列基础模型）。
* **确定性评估器、公开排行榜以及完整的数据表。**

实验结果表明，顶级配置在各个框架和基干模型中实现了 **80.8% 的 pass@1**，这表明剩余的错误主要源于任务编排和工具调用顺序，而不是模式有效性（schema validity）。此外，架构消融实验表明，用静态的基于文本的 RAG 代替 MCP 工具执行，会导致剩余寿命（RUL）性能从 **100% 崩塌至 20%**，这强调了算法扎根工具对于预测计算的必要性。

---

## 📋 元数据与出版详情

* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **Submission History:** 
  * [v1] Thu, 2 Apr 2026
  * [v2] Fri, 8 May 2026
  * [v3] Mon, 24 Aug 2026 *(This version)*
* **Full-Text Resources:** 
  * [View PDF](https://arxiv.org/pdf/2604.01532)
  * [Experimental HTML](https://arxiv.org/html/2604.01532v3)
  * [TeX Source](https://arxiv.org/src/2604.01532)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>

> **主要学科：** 人工智能 (`cs.AI`)
> **提交历史：**
> * [v1] 2026年4月2日（周四）
> * [v2] 2026年5月8日（周五）
> * [v3] 2026年8月24日（周一）*（本版本）*
> **全文资源：**
> * [查看 PDF](https://arxiv.org/pdf/2604.01532)
> * [实验性 HTML](https://arxiv.org/html/2604.01532v3)
> * [TeX 源码](https://arxiv.org/src/2604.01532)
> **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>查看许可证</span></a>

---

## 🔍 摘要

> LLM agents are beginning to invoke industrial asset-management tools through the Model Context Protocol (MCP), yet whether they can act reliably on this substrate for safety-critical *Prognostics and Health Management (PHM)* is unanswered. Prior benchmarks conflate protocol fluency with reasoning, instrumentation failures with agent failures, and tool use with tool retrieval. We introduce **PHMForge**, an evaluation environment that closes each conflation. PHMForge ships 99 SME-authored scenarios across eight industrial asset classes spanning rotating equipment, aero-engines, and lithium-ion cells, on public datasets including NASA PCoE, served through 39 MCP-native tools wrapping published PHM algorithms (C-MAPSS, ISO 10816, Arrhenius capacity-fade models, time-series foundation models). Krippendorff's $\alpha \in [0.74,\,0.82]$ on a 30-scenario stratified rotating-equipment/aero-engine sample; the battery extension is single-rater. Across three agentic frameworks and six LLM backbones, the strongest configuration reaches **80.8% pass@1**, with the residual gap concentrated in orchestration and tool-sequencing errors. Crucially, an architectural ablation shows that replacing MCP execution with text-based Retrieval-Augmented Generation (RAG) over telemetry-equivalent evidence collapses Remaining Useful Life *pass-all-3* from **100% to 20%** (5/5 vs. 1/5) on the battery class, exposing the structural limits of static retrieval for prognostic computation. Trajectory decomposition shows orchestration errors dominate failures across backbones, while schema-invalid tool calls concentrate in smaller open-weight models. Frontier LLMs are stronger at calling tools than at planning when to call them. PHMForge is open-sourced with deterministic evaluators, a public leaderboard, and a datasheet.

大语言模型（LLM）智能体正开始通过模型上下文协议（MCP）调用工业资产管理工具，然而它们是否能够在该底层技术上针对安全关键型的*预测与健康管理（PHM）*任务进行可靠操作，目前尚无定论。先前的基准测试将协议的流畅度与推理混为一谈，将仪器故障与智能体故障混淆，也将工具使用与工具检索混淆。我们推出了 **PHMForge**，这是一个能够消除上述各种混淆的评估环境。PHMForge 提供了 99 个由领域专家（SME）编写的场景，涵盖旋转机械、航空发动机和锂离子电池等八大工业资产类别，并基于 NASA PCoE 等公开数据集，通过 39 个封装了已发表 PHM 算法（C-MAPSS、ISO 10816、阿伦尼乌斯容量衰减模型、时间序列基础模型）的 MCP 原生工具进行服务。在包含 30 个分层旋转机械/航空发动机样本的测试中，Krippendorff’s $\alpha \in [0.74,\,0.82]$；电池扩展部分则采用单评分者验证。在三个智能体框架和六个 LLM 基干模型中，最强的配置达到了 **80.8% 的 pass@1**，剩余的性能差距主要集中在任务编排和工具排序错误上。至关重要的是，架构消融实验表明，在电池类别中，用基于文本的检索增强生成（RAG）替代对遥测等效证据的 MCP 执行，会导致剩余寿命（RUL）的 *pass-all-3* 指标从 **100% 暴跌至 20%**（5/5 对比 1/5），这暴露了静态检索在预测计算中的结构性局限。轨迹分解显示，编排错误在各基干模型的失败案例中占据主导地位，而架构无效的工具调用则集中在较小的开源权重模型中。前沿 LLM 在调用工具方面表现更强，但在规划何时调用工具方面能力相对较弱。PHMForge 已开源，并配有确定性评估器、公开排行榜和一个完整的数据表。