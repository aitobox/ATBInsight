---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-11-09
hide:
  - navigation
tags:
  - Google
  - AI 智能体
  - 代码生成
  - 软件工程
title: "Google 开源 Elephant-Goldfish 插件：专为 AI 编程智能体打造的“规范优先”设计与审查架构"
---

# Google 开源 Elephant-Goldfish 插件：专为 AI 编程智能体打造的“规范优先”设计与审查架构

> # Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding

### 文章背景与核心概要
在大语言模型 (Large Language Model, LLM) 辅助编程的时代，开发者经常遭遇“上下文崩溃”以及 AI 盲目编写代码、产生低质“垃圾代码 (AI slop)”的痛点。针对这一普遍难题，Google 正式开源了其内部数千名工程师深度使用的 Elephant-Goldfish Model (EGM) 插件。该方案确立了“规范优先 (Spec-First)”的核心机制：要求负责维护全局记忆的“大象”智能体在写代码前先撰写详尽的技术规范，随后由完全处于零上下文记忆状态的“金鱼”子智能体发动多轮严苛的无偏见交叉审查。这一插件的开源不仅将错误扼杀在方案构思阶段，更为业界构建可靠、可审计的工业级 AI 智能体 (AI Agent) 软件工程体系提供了标准范式。

---

Google 正式开源了专为 AI 编码智能体量身打造的设计与审查层——[Elephant-Goldfish Model (EGM) 插件](https://github.com/google/elephant-goldfish-model)。其核心理念十分简单直接：**强制要求智能体在动手写代码前必须先撰写详尽的技术规范，随后派出没有任何对话历史记忆的全新子智能体，对这份规范展开无死角的审视与挑刺。**

> Google has open-sourced the [Elephant-Goldfish Model (EGM) plugin](https://github.com/google/elephant-goldfish-model), a design-and-review layer tailored for AI coding agents. The core philosophy is simple: **force an agent to write a specification before it writes code, and then have fresh subagents with zero conversation history attack that spec.**

据 Google 介绍，[其内部已有数千名工程师在使用该工具](https://egm.dev/)，以便尽早发现错误的设计假设——直接在初始的 Markdown 文件中将隐患扼杀在摇篮里，而不是等到后续提交代码合并请求 (Pull Request, PR) 时才仓促返工。

> According to Google, [thousands of its engineers use it](https://egm.dev/) to catch wrong assumptions early—directly in a Markdown file rather than down the road in a pull request.

---

## 📌 内容速览

> ## 📌 Summary

* **项目定位：** 一款基于 Apache 2.0 协议开源的插件，包含 7 项核心技能、9 种审查员角色设定、6 大头脑风暴视角以及 5 个递进审查阶段 (该插件不包含任何模型权重，底层大语言模型由宿主智能体提供)。
* **核心工作流：** 负责长会话上下文的“**大象 (Elephant)**”在不编写任何代码的前提下草拟技术规范，而无状态的“**金鱼 (Goldfish)**”子智能体则对其展开严苛尖锐的多角度审查。
* **平台兼容：** 适用于任何能够派生全新独立子智能体的宿主平台 (Harness)，包括 Antigravity、Claude Code (2.1.271+)、Claude Cowork、Codex 以及 ChatGPT，直接复用开发者现有的模型额度。
* **实测性能：** 真实环境基准测试展现出稳健的执行能力 (例如 Codex 0.163.0 成功按顺序调度了 15 位原生全新上下文审查员，并在 573.13 秒内顺利通过了 2 项实测)。
* **核心结论：** 它提供了一种在真正写代码前强制执行独立审查的坚固机制；尽管其伴随着较高的 Token 消耗，且在特定宿主环境下偶尔会出现微小的上下文隔离波动。

> * **What it is:** An Apache 2.0 open-source plugin consisting of 7 skills, 9 reviewer personas, 6 brainstorm lenses, and 5 review stages (no model weights included; your agent provides the LLM).
> * **Core Workflow:** The **Elephant** (long-session context) drafts the spec without writing code, while stateless **Goldfish** subagents aggressively review it.
> * **Compatibility:** Works across harnesses that can spawn fresh subagents, including Antigravity, Claude Code (2.1.271+), Claude Cowork, Codex, and ChatGPT, leveraging your existing model quota.
> * **Performance:** Real-world benchmark tests show solid execution (e.g., Codex 0.163.0 successfully completed 15 native fresh-context reviewers in order; 2 live tests passed in 573.13s).
> * **Key Takeaway:** It offers a robust way to enforce independent reviews prior to coding, though it comes with heavy token consumption and occasional context-isolation hiccups on certain hosts.

---

## 什么是 Google 的 Elephant-Goldfish 模型插件？

> ## What is Google’s Elephant-Goldfish Model Plugin?

EGM 是一款基于 Apache 2.0 协议开源的工程化插件，内含结构化技能集、审查员角色预设以及严苛的文档交付标准。需要特别指出的是，它**绝非**一款全新的基础语言大模型。

> EGM is an Apache 2.0 plugin comprising structured skills, reviewer personas, and strict document standards. It is **not** a new foundational language model.

该插件背后的方法论源自 [Dave Rensin 的深度博文](https://medium.com/@drensin/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874)，核心围绕“大象 (具备长期记忆)”与“金鱼 (无状态的即时子智能体)”的协同机制展开。尽管 [Google 开源博客 (Google Open Source blog)](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html) 将其盛赞为遏制 AI“劣质代码 (slop)”及解决会话上下文崩溃的一剂良方，但该代码仓库的 README 中也明确注明：它[并非 Google 官方正式支持的商业化产品](https://github.com/google/elephant-goldfish-model)。

> The underlying methodology stems from [Dave Rensin’s essay](https://medium.com/@drensin/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874) regarding elephants (long-term memory) and goldfish (stateless, transient subagents). While the [Google Open Source blog](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html) promotes it as a remedy for AI "slop" and session context collapse, the repository's README notes that it is [not an officially supported Google product](https://github.com/google/elephant-goldfish-model).

---

## Elephant-Goldfish 的工作流程是如何运转的？

> ## How Does the Elephant-Goldfish Workflow Work?

整个工作流紧紧维系在两类核心角色之上：

> The workflow hinges on two primary actor types:

1. **大象 (The Elephant)：** 长期存活的主会话，负责维护整个项目的宏观背景与历次技术决策。它全权负责撰写技术规范，但**绝对不编写任何一行代码**。
2. **金鱼 (The Goldfish)：** 完全无状态的临时子智能体，*仅*审查规范草案本身及文档中明确引用的关联文件，从而杜绝先入为主的偏见，确保客观公正的审计。

> 1. **The Elephant:** A long-running session that maintains project context and historical decisions. It drafts the specification but writes **no code**.
> 2. **The Goldfish:** Stateless subagents that review *only* the draft and explicitly referenced files, ensuring an unbiased audit.

其[核心循环 (core loop)](https://github.com/google/elephant-goldfish-model/blob/main/docs/getting_started.md)主要通过三大核心斜杠指令驱动：

> The [core loop](https://github.com/google/elephant-goldfish-model/blob/main/docs/getting_started.md) operates via three primary commands:

* `/egm-brainstorm`：理清底层业务逻辑，并启动拥有 6 种视角的“金鱼机群” (涵盖 YAGNI 原则、Token 成本、用户体验 UX、系统迁移、可观测性与技术债务)，最终输出一份清晰的 `concepts_brief.md` 概念简报。
* `/egm-draft`：将上述概念简报逐节细化，转化为存放于 `docs/designs/` 目录下的正式技术设计方案。
* `/egm-review`：正式拉起多阶段的金鱼交叉审查流程。

> * `/egm-brainstorm`: Clarifies the underlying idea and runs a 6-lens Goldfish swarm (covering YAGNI, token costs, UX, migration, observability, and tech debt) to output a `concepts_brief.md`.
> * `/egm-draft`: Translates the brief into a formal design document under `docs/designs/`, section by section.
> * `/egm-review`: Executes the multi-stage Goldfish review process.

此外，系统还提供了一个 `/egm-drift-report` 指令 (官方推荐每周运行一次)，用于对比实际代码库与已审批的技术规范之间的差异，有效防止软件架构随迭代逐渐“偏航走样 (architectural drift)”。

> Additionally, a `/egm-drift-report` command (recommended weekly) compares the actual codebase against the approved specification to prevent architectural drift.

---

## 五阶段“金鱼审查”到底是如何开展的？

> ## What Happens in the 5-Stage Goldfish Review?

这套[审查技能 (review skill)](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-review/SKILL.md)会强制技术规范依次通过五个严谨且环环相扣的审查阶段：

> The [review skill](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-review/SKILL.md) forces specs through five strict, sequential stages:

1. **宏观初审 (Initial Zoom Out)：** 从顶层软件架构视角全面评估整份设计文档的合理性。
2. **理解力测试 (Comprehension Test)：** 指派一只金鱼子智能体用自己的语言复述设计方案。如果复述出现偏差，则说明文档存在歧义与表达不清之处。
3. **挑刺审查 (Critic Review)：** 调度设计、架构及代码风格等多位审查员，全力搜寻边缘用例 (Edge Cases)、潜在盲点与架构断层。
4. **阶段复查 (Intermediate Zoom Out)：** 在初步问题完成修复后，重新对整体架构的一致性进行二次校验。
5. **落地就绪度评估 (Implementation Readiness)：** 严密核对文件路径、数据结构以及函数签名等具体实现细节是否万无一失。

> 1. **Initial Zoom Out:** Evaluates the entire document from a high-level architectural perspective.
> 2. **Comprehension Test:** A Goldfish subagent paraphrases the design. If the paraphrase is flawed, the documentation is flagged as ambiguous.
> 3. **Critic Review:** Design, structural, and style reviewers actively hunt for edge cases, blind spots, and architectural gaps.
> 4. **Intermediate Zoom Out:** Re-verifies the architecture after initial fixes are applied.
> 5. **Implementation Readiness:** Validates file paths, data structures, and function signatures.

*注：每个阶段最多仅允许复审一次。审查发现的问题会被严格划分为**阻断项 (Blocker)**、**重大缺陷 (Major)** 或 **轻微修饰 (Nit)**。如果宿主环境缺乏子智能体调度工具，EGM 将直接中止运行——在同一上下文中进行的自审查绝不能被算作真正的金鱼审查。*

> *Note: Each stage permits a maximum of one re-audit. Findings are rigorously categorized as **Blocker**, **Major**, or **Nit**. If a host environment lacks subagent tooling, EGM halts—a same-context review does not qualify as a Goldfish review.*

---

## EGM 支持哪些编程智能体？

> ## Which Coding Agents Does EGM Support?

项目最初推出时[仅支持 Antigravity](https://www.helpnetsecurity.com/2026/10/26/google-elephant-goldfish-model-plugin/)，但根据最新的[宿主环境指南 (harness guide)](https://github.com/google/elephant-goldfish-model/blob/main/docs/harnesses.md)，目前支持阵营已拓展至 Antigravity CLI 与 App、Claude Code、Claude Cowork、Codex、ChatGPT、omp 以及 Muse。其中，在 Antigravity CLI、Claude Code 和 Codex 上，端到端自动化测试固件均能无障碍顺利通过。

> Initial rollouts featured [Antigravity-only support](https://www.helpnetsecurity.com/2026/10/26/google-elephant-goldfish-model-plugin/), but the current [harness guide](https://github.com/google/elephant-goldfish-model/blob/main/docs/harnesses.md) has expanded to include Antigravity CLI and App, Claude Code, Claude Cowork, Codex, ChatGPT, omp, and Muse. Automated end-to-end fixtures pass cleanly on Antigravity CLI, Claude Code, and Codex.

* **Claude Code：** 要求[版本不低于 2.1.271](https://github.com/google/elephant-goldfish-model/blob/main/docs/claude.md)。审查员被严格限制仅能使用 Read、Grep 和 Glob 工具，且本地的 `CLAUDE.md` 文件会被显式排除在上下文之外。
* **实测记录：** 详实的基准测试运行记录证明了其在工业场景中的可用性：
  * *Antigravity CLI 1.4.5：* 16 位原生审查员依次完成了所有阶段的审查任务。
  * *Codex 0.163.0：* 15 位原生审查员在 573.13 秒内完成了 2 项真实用例测试。
  * *Codex CLI (v0.1.0 ZIP)：* 仅耗时 482.30 秒便成功通过了完整的测试套件。

> * **Claude Code:** Requires [version 2.1.271 or later](https://github.com/google/elephant-goldfish-model/blob/main/docs/claude.md). Reviewers are restricted to Read, Grep, and Glob tools, with local `CLAUDE.md` files explicitly excluded from their context.
> * **Test Records:** Concrete benchmark runs showcase real-world viability:
>   * *Antigravity CLI 1.4.5:* 16 native reviewers executed all stages sequentially.
>   * *Codex 0.163.0:* 15 native reviewers completed 2 live tests in 573.13s.
>   * *Codex CLI (v0.1.0 ZIP):* Full test suite completed successfully in 482.30s.

---

## EGM 与 Spec Kit、Kiro 及 Superpowers 相比有何不同？

> ## How Does EGM Compare with Spec Kit, Kiro, and Superpowers?

| 特性 (Feature) | Google EGM | GitHub Spec Kit | Kiro Specs | Superpowers |
| :--- | :--- | :--- | :--- | :--- |
| **定位类型 (Type)** | 插件 (技能集 + 角色设定) | 工具包 + Specify CLI | 智能体 IDE/CLI/Web 功能 | 技能集插件 |
| **开源协议 (License)** | [Apache 2.0](https://github.com/google/elephant-goldfish-model/blob/main/LICENSE) | [MIT](https://github.com/github/spec-kit) | 商业闭源 ([定价方案](https://kiro.dev/pricing/)) | [MIT](https://github.com/obra/superpowers) |
| **工作流 (Workflow)** | 头脑风暴、起草规范、审查、架构漂移报告 | 架构规范宪章、细化说明、方案规划、任务拆解、编码实现、收敛校验 | 需求分析、方案设计、任务管理 | 头脑风暴、方案规划、子智能体构建、测试驱动开发 (TDD)、代码审查 |
| **规范是否由全新上下文子智能体审查？ (Spec Reviewed by Fresh-Context Subagents?)** | 是，编码前历经 5 个独立审查阶段 | 未公开 | 未公开 (*需求分析*阶段通过) | 否 (全新子智能体在编码阶段按任务逐一审查代码) |
| **宿主环境支持 (Harness Support)** | Antigravity、Claude Code、Codex、ChatGPT 等 | GitHub Copilot 及其他智能体 | 仅限 Kiro | 列出支持 16 种宿主工具 |
| **环境安装 (Setup)** | 插件直接安装 | 依赖 Python 3.11+ 与 `uv` | 注册 Kiro 账号 | 插件直接安装 |
| **使用成本 (Cost)** | 插件免费 + 宿主模型推理额度 | 工具包免费 + 宿主模型推理额度 | 需按月订阅 | 插件免费 + 宿主模型推理额度 |

虽然 Spec Kit 和 Kiro 在各个阶段之间高度依赖人工审查检查点，而 Superpowers 则主要将子智能体隔离机制应用于实际编码实现阶段，但 EGM 最具标志性的特征，是在动笔写代码之前，就对*技术规范*展开极其严苛、零上下文历史的独立审查。

> While Spec Kit and Kiro rely heavily on manual human checkpoints between phases, and Superpowers delegates subagent isolation primarily to the implementation phase, EGM's defining characteristic is its aggressive, zero-context review of *specifications* prior to writing code.

---

## 核心要点总结

> ## Key Takeaways

* **重架构而非重权重：** EGM 本质上是一套组织与流程型插件，而非底层大语言模型——它巧妙依靠“大象”起草规范，并调度“金鱼”子智能体展开全面审查。
* **强制“规范优先”：** 每一份软件设计文档在生成哪怕一行代码之前，都必须严格通过 5 个零上下文的独立审查阶段。
* **生态覆盖广泛：** 全面支持主流生态，在 Antigravity、Claude Code、Codex 以及 ChatGPT 等平台上均可顺畅运行。
* **经过验证的可靠性：** Codex 实测记录展现出完整闭环，成功端到端连续轮转了 15 位全新上下文审查员。
* **仍有改进空间：** 在某些特定命令行界面 (CLI) 下，审查员隔离机制偶尔会微量泄露宿主指令，且整体 Token 开销相对较高。

> * **Architecture over Weights:** EGM is an organizational plugin, not an LLM—relying on the "Elephant" to draft specs and "Goldfish" subagents to review them.
> * **Spec-First Enforcement:** Every design document must clear 5 zero-context review stages before any code is generated.
> * **Wide Ecosystem Reach:** Fully functional across platforms like Antigravity, Claude Code, Codex, and ChatGPT.
> * **Proven Reliability:** Codex test runs successfully cycled through 15 fresh-context reviewers end-to-end.
> * **Room for Improvement:** Reviewer isolation can occasionally leak host instructions on specific CLIs, and token overhead is substantial.

---

## 资源与社区

> ## Resources & Community

* **官方链接：** [GitHub 代码仓库](https://github.com/google/elephant-goldfish-model) | [项目官网](https://egm.dev/) | [Google 开源博客文章](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html)
* **加入社区：** [Twitter](https://x.com/intent/follow?screen_name=marktechpost) | [15 万+ 成员的 ML SubReddit 社区](https://www.reddit.com/r/machinelearningnews/) | [订阅周刊](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}}) | [Telegram 频道](https://t.me/machinelearningresearchnews)
* **商业推广与合作：** [与我们取得联系](https://promotions.marktechpost.com/)，在平台上展示您的 GitHub 仓库、Hugging Face 主页或新产品发布。

> * **Official Links:** [GitHub Repository](https://github.com/google/elephant-goldfish-model) | [Project Website](https://egm.dev/) | [Google Open Source Blog Post](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html)
> * **Join the Community:** [Twitter](https://x.com/intent/follow?screen_name=marktechpost) | [150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/) | [Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}}) | [Telegram Channel](https://t.me/machinelearningresearchnews)
> * **Promotions & Partnerships:** [Connect with us](https://promotions.marktechpost.com/) to feature your GitHub Repo, Hugging Face Page, or Product Release.

*(信息来源：[MarkTechPost](https://www.marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents/))*

> *(Source: [MarkTechPost](https://www.marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents/))*
