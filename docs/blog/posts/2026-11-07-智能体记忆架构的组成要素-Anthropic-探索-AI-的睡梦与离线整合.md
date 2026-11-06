---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-07
hide:
  - navigation
tags:
  - Anthropic
  - AI 智能体
  - 智能体记忆
  - 离线计算
title: "智能体记忆架构的组成要素：Anthropic 探索 AI 的睡梦与离线整合"
---

# 智能体记忆架构的组成要素：Anthropic 探索 AI 的睡梦与离线整合

> # The Components of Agent Memory

### 文章背景与核心概要
在生物神经系统中，人类依靠海马体在日间迅速编码瞬时经历，并在夜间离线睡眠中通过大脑新皮层进行记忆巩固。受此脑科学机制启发，Anthropic 深入探索了 AI 智能体 (AI Agent) 的长效记忆构建范式。通过引入“睡梦期离线计算” (Sleep-time compute / Dreaming)、结构化记忆笔记、知识 Wiki 以及分层上下文注入机制，智能体得以从低效盲目的实时状态流水账中解放出来，学会主动预测未来需求并动态纠偏。这一架构不仅帮助 Claude 破解了像通关《宝可梦》这样复杂的长周期任务，更为大语言模型突破无状态交互瓶颈、实现真正的终身持续学习指明了全新方向。

---

**概要：** 借鉴人类神经系统的记忆机制（海马体迅速捕捉眼前的即时经验，而离线睡眠则促使记忆在新皮层中完成深度巩固），Anthropic 深入探讨了 Claude 等 AI 智能体 (AI Agent) 如何管理、组织与调动长期记忆。通过引入**睡梦期计算 (Sleep-time compute，常被称为“做梦” / Dreaming)**、记忆笔记、Wiki 知识库以及上下文注入机制，大模型能够告别机械式记录冗余实时状态的初级阶段，学会精准预判未来需求、自我纠正认知偏差，从而从容应对高难度的长周期复杂任务。

> **Summary:** Drawing parallels to human neurological memory (where the hippocampus captures immediate experiences and offline sleep allows consolidation in the neocortex), Anthropic explores how AI agents like Claude can manage, organize, and utilize long-term memory. By implementing **sleep-time compute ("dreaming")**, memory notes, wikis, and context injection, models can transition from recording redundant real-time states to predicting future needs, correcting errors, and successfully tackling complex long-horizon tasks.

---

## 引言

> ## Introduction

> 💬 [哲思引用]: “生活只有向后回溯才能被理解，但生活必须向前度过。” —— Søren Kierkegaard
>
> 💬 [原文引用 / Original Quote]:
> *"Life can only be understood backward, but it must be lived forward."* — Søren Kierkegaard

为 AI 智能体设计记忆系统同样面临着类似的困局。作为人类，我们的大脑依靠海马体时刻对经历进行编码，飞速捕捉周围发生的一切；而这些经验要想真正沉淀并巩固到大脑新皮层中，主要依靠的却是在脱机睡眠或休息期间的整理。

> Designing memory for AI agents introduces a similar bind. As humans, we encode memory constantly through the hippocampus, capturing experiences quickly while consolidating them into the neocortex largely during offline sleep or rest.

智能体的记忆系统完全可以借鉴这种高效的“分工协作”模式。通过借助**睡梦期计算** (Sleep-time compute，业内常形象地称之为**“做梦” / Dreaming**)——即利用两次交互之间的空闲空档期重新梳理已有的上下文信息——智能体不仅能够从容复盘历史日志、纠正既有错误，还能自主提炼出全新的笔记与知识表征。

> Agent memory can use a similar division of labor. By leveraging **sleep-time compute** (often called ***dreaming***)—using idle time between interactions to reorganize existing context—agents can reflect on logs, fix mistakes, and produce new notes and representations.

---

## 记忆笔记

> ## Memory Notes

所谓的智能体记忆，是指 Claude 在实际交互体验中所汲取、并且能够在不同跨会话之间持续保留的知识。它本质上不同于模型内部固化的参数权重、临时的上下文学习 (In-Context Learning, ICL)，或者是会话过程中暂时的上下文压缩机制。

> Agent memory refers to the knowledge Claude gains from experience and retains between sessions, distinct from internal parameter weights, in-context learning, or temporary conversation compaction.

正如人类大脑会通过神经化学信号将某些高光经历标记为“重要”，以便在夜间离线回放一样，Claude 同样可以在会话交互日志中为显著事件打上标签，或者直接将其写入持久化的外部记忆库（例如一个专门存放记忆笔记的文件夹）。

> Just as chemical signals mark human experiences as important for offline replay, Claude can tag salient events in session logs or write them directly to a persistent memory store, such as a folder of memory notes.

<figure>
  <img alt="Diagram of a memory hierarchy between one session and the next." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa0bcfa203214d817d2b4261b7188aba8be6db5b2-3840x1754.png&amp;w=3840&amp;q=75" width="3840" height="1754" />
  <figcaption><strong>图 1:</strong> Claude 可以利用“做梦”机制重组记忆——包括纠正错误、创建笔记、构建知识表征，或精心塑造未来会话的上下文输入。 / <strong>Figure 1:</strong> Claude can use dreaming to organize memory—correcting mistakes, creating notes, building representations, or shaping future session context.</figcaption>
</figure>

### 记忆本质上是对未来需求的预判

> ### Memory as a Prediction of Future Needs

记下一条规则或一个已经验证的事实，本质上是对未来的一种笃定预测：它预测未来的智能体在后续会话中无需重新核实验证，便可以直接信赖并调用这一结论。

> Writing down a rule or a verified fact is a prediction that an agent in a future session will want to rely on it without double-checking.

在针对 **持续学习基准测试 (Continual Learning Bench, CL-Bench) 1.0** 的严苛评测中，各大模型借助跨越无状态独立会话的持久记忆目录，记录执行失败教训、构建假设理论并验证推导规则。诸如 *Claude Opus 5*、*Opus 5.5* 以及 *Sonnet 5.5* 等前沿顶级模型成功打通了这一完整的“认知闭环”，其综合表现彻底碾压了没有任何记忆留存的无状态基线模型。

> In tests on the **Continual Learning Bench (CL-Bench) 1.0**, models leveraged persistent memory directories across stateless sessions to record failures, build theories, and validate rules. Advanced models like *Claude Opus 5*, *Opus 5.5*, and *Sonnet 5.5* successfully closed this learning loop, drastically outperforming stateless baselines.

<figure>
  <img alt="CL-Bench database task, comparing memory with a stateless baseline across models." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fbb0d44c78cc431fb5e84fbf2cb17c4303bc6bd65-3840x2160.png&amp;w=3840&amp;q=75" width="3840" height="2160" />
  <figcaption><strong>图 3:</strong> CL-Bench 数据库任务评测：对比各模型在配备记忆模块与无状态基准线下的性能表现。 / <strong>Figure 3:</strong> CL-Bench database task, comparing memory with a stateless baseline across models.</figcaption>
</figure>

### 价值判断：分辨关键信息与无节制盲目记录

> ### Judging Salience vs. Indiscriminate Logging

在面对类似运行《宝可梦·红》 (*Pokémon Red*) 这类超长执行周期的任务评测时，不同模型在“究竟什么信息才值得记录”这一核心判断上，表现出了天壤之别的思维模式：

> When tested on long-horizon tasks like playing *Pokémon Red*, models exhibited vastly different approaches to what was worth remembering:

* **Claude Sonnet 3.7** 误以为所有琐碎细节都至关重要，不加筛选地在 225 个文件夹中疯狂创建了 413 份记忆文件；这直接导致其状态数据在几步之后便迅速过时失效，白白空耗了宝贵的推理与行动步数。
* **Claude Fable 5** 则维持了极为清晰精简的目录架构（通过一个顶层的 `global.md` 总览仪表盘，搭配 `locations` 地图信息与 `gameplay` 策略规则文件夹），仅保留战略层面的长远规划与摸索出的核心规律，坚决不存冗余的实时数值变化。结果，它成功斩获了 4 枚道馆徽章，而无节制记录的 Sonnet 仅勉强拿到 1 枚。

> * **Claude Sonnet 3.7** assumed everything mattered, creating 413 memory files across 225 folders indiscriminately, causing its state data to constantly go out of date and wasting execution steps.
> * **Claude Fable 5** maintained a streamlined structure (using a `global.md` dashboard, `locations`, and `gameplay` folders for strategic rules), saving only higher-level plans and discovered rules rather than redundant real-time stats. As a result, it earned four badges compared to Sonnet's one.

<figure>
  <img alt="Claude’s memory directories for Sonnet 3.7 versus Fable 5 while playing Pokémon." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5e15e10f665773050d90fafc38ab8dd76ae5368b-3840x2545.png&amp;w=3840&amp;q=75" width="3840" height="2545" />
  <figcaption><strong>图 4:</strong> Claude 运行《宝可梦》时 Sonnet 3.7 与 Fable 5 的记忆文件目录结构对比。 / <strong>Figure 4:</strong> Claude’s memory directories for Sonnet 3.7 versus Fable 5 while playing Pokémon.</figcaption>
</figure>

### 引导记忆的创建与沉淀

> ### Steering Memory Creation

实验证明，对于前沿顶尖模型而言，提供大方向的通用指导（赋予 Claude 自主判断信息重要程度的自由度），远比施加生硬死板的规矩更见效（例如强行要求模型“仅记录失败教训”，反而会直接损伤推理表现）。然而，明确的方向引导和显式的提示词工程 (Prompt Engineering) 对早期旧版模型却有立竿见影的奇效——例如在任务执行前显式提示 *Sonnet 4.6* 先通读记忆文件，直接使其基准测试得分翻了近一番。

> Providing general guidance (letting Claude judge salience freely) proved more effective for frontier models than rigid rules (such as forcing models to "record only failures," which actively degraded performance). However, steering and explicit prompting significantly helped older models—such as prompting *Sonnet 4.6* to read memory files beforehand—which nearly doubled its benchmark score.

---

## “睡梦”机制如何升华智能体记忆

> ## How Dreaming Enhances Memory

### 1. 纠正记忆偏差与认知漂移

> ### 1. Correcting Memory Errors

由于会话实时生成的笔记可能存在疏漏，或者随着动态环境的变迁而发生认知漂移，**睡梦期计算 (Dreaming)** 允许 Claude 将过往存储的笔记与最原始的会话交互实录进行对照检验，从而敏锐地捕获错误。例如，在《宝可梦》攻略月见山 (*Mt. Moon*) 复杂的洞穴迷宫环节中，一份未经修正的错误记忆曾导致 Claude 陷入永无止境的原路折返死循环；而在引入一次“睡梦”离线重构后，系统精准修正了路线空间表征，指引 Claude 成功破局继续推进剧情。

> Because in-session notes can be flawed or drift as environments change, **dreaming** allows Claude to test stored notes against original session transcripts to catch errors. For example, during the Pokémon *Mt. Moon* cave sequence, an uncorrected memory led Claude into an endless backtracking loop, whereas a dreaming pass successfully corrected the route representation, allowing Claude to progress.

<figure>
  <img alt="A corrected memory note changed the outcome in Pokémon." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd906d6ed9ac92db36631a624ad517183b07a545d-3840x2101.png&amp;w=3840&amp;q=2101" width="3840" height="2101" />
  <figcaption><strong>图 7:</strong> 一份经过纠偏的记忆笔记改变了《宝可梦》的博弈走势：引导角色重新深入洞穴探索，彻底终结了无效的原路折返循环。 / <strong>Figure 7:</strong> A corrected memory note changed the outcome in Pokémon by driving re-entry into the cave instead of looping back.</figcaption>
</figure>

### 2. 构建全新的知识表征体系（Wiki 百科）

> ### 2. Building New Memory Representations (Wikis)

Claude 还具备自主构建 **Wiki 知识库** 的强大能力——即生成由相互交织的页面链接构成的知识网络，完整测绘海量文档语料库。在针对来自 Stainless 的内部超大文档语料（涵盖 35 万个文件、约 4.2 亿 Token）的深度压力测试中，仅将“睡梦”整理轮次从 2 轮扩展至 128 轮，模型在评测问答任务中的答题准确率便直接从 13% 飙升至 48%（若进一步搭配外部搜索工具，准确率更是高达 61%）。

> Claude can construct **wikis**—interlinked collections of pages that map out large corpora. Tested on an internal document corpus from Stainless (350,000 files / ~420M tokens), scaling dreaming sessions from 2 to 128 raised performance on evaluation questions from 13% to 48% (and up to 61% when combined with a search tool).

<figure>
  <img alt="Scores on 25 questions about a corpus of documents as Claude built wikis over sequential sessions." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F336832b5015f1bfcfd7d786fae8120c533f26ecd-3136x1432.png&amp;w=3840&amp;q=75" width="3136" height="1432" />
  <figcaption><strong>图 10:</strong> 随着 Claude 在连续会话中逐步构建 Wiki，25 道文档基准问答的得分持续攀升（左右网络拓扑图生动展示了知识页面从 103 页扩展到 222 页的有机演化过程）。 / <strong>Figure 10:</strong> Scores on 25 questions as Claude built wikis over sequential sessions (left/right networks show growth from 103 to 222 pages).</figcaption>
</figure>

### 3. 将高价值笔记提升至记忆层级顶端

> ### 3. Promoting Notes Up the Hierarchy

“做梦”沉淀机制能够将最为核心关键的精华笔记筛选浮现至记忆金字塔的顶层。这使得智能体编排底座 (Agent Harness) 能够在每次全新会话启动的一瞬间，先发制人地将其预先注入到上下文窗口中（例如 *Claude Code* 内置的自动记忆头部索引机制）。确保顶层注入内容足够凝练克制，既能有效防止上下文 Token 发生急剧膨胀，又能严格保障模型对系统指令的高度遵从性。

> Dreaming floats critical notes to the top of the memory hierarchy, allowing agent harnesses to preemptively inject them into the context window at the start of every session (e.g., *Claude Code*'s auto-memory header index). Keeping this top layer concise prevents token bloat and maintains instruction adherence.

<figure>
  <img alt="The memory hierarchy with dreaming, highlighting injected context." src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc88bcc04c5d0e77db5828c9dbe72faf1c4421f8f-3840x1754.png&amp;w=3840&amp;q=75" width="3840" height="1754" />
  <figcaption><strong>图 13:</strong> 融合“睡梦”机制的记忆金字塔架构：高优记忆写入层级顶部，作为上下文自动注入到每个全新的交互会话中。 / <strong>Figure 13:</strong> Dreaming writes to the top of the memory hierarchy for injected context loaded into every session.</figcaption>
</figure>

### 4. 聚焦特定目标并查漏补缺

> ### 4. Focusing on Specific Goals and Filling Gaps

通过面向特定业务基准量身定制“睡梦”指令（例如从复杂的法律案卷摘要中提取合同关键条款），智能体能够从原先容易互相覆盖冲突的粗糙共享表格，顺利过渡到由单个智能体专属维护的高精度独立知识页面，一举实现 100% 的精准提取率。此外，额外的离线做梦轮次还能主动自愈系统中的悬空失效链接，并重构缺失页面，使整个知识图谱日趋完善。

> By tuning dreaming instructions toward specific benchmarks (such as contract extraction in legal briefs), agents can transition from flawed shared tables—where agents overwrite each other's work—to precise, single-agent dedicated pages that achieve 100% extraction accuracy. Additional dreaming passes also resolve dangling links and restructure missing pages.

---

## 结语

> ## Conclusion

设计卓越的智能体记忆体系，关键在于兼顾运行时的即时显著性捕捉与离线后台的深度计算（“做梦”）。虽然全量交互日志检索与直连记忆读写工具为系统提供了底层访问能力，但唯有“做梦”机制赋予了智能体必要的离线算力，让它得以**向后回溯**审视历史、修正认知漂移，并沉淀出高度结构化的知识表征，为未来会话的敏捷与智能全面赋能。

> Designing agent memory requires balancing real-time salience capture with offline background computation ("dreaming"). While transcript search and direct memory tools offer foundational access, dreaming provides the necessary compute to look *backward*, correct drift, and build structured representations that empower future sessions.

---

## 作者与致谢

> ## Authors & Acknowledgements

* **本文作者：** Lance Martin
* **编辑审校指导：** Caitlin Love, Tom Chivers, Rebecca Hiscott, Jake Eaton 以及 Blake Wilson
* **核心贡献者：** Barry Zhang, Theodora Chu, Daliang Li, Mahesh Murag, Jake Noble, Ravi Trivedi, Tina Vachovsky, Brad Abrams, Henry de Valence, Jeremy Fox, Matt Bell, Allen Li, Chris Gorgolewski, Eugene Yan, Artur Renault, Wei Zhang, Kevin Chen 以及 David Hershey（《Claude 畅玩宝可梦》项目）
* **配图绘制：** Monika Tuchowska

> * **Written by:** Lance Martin  
> * **Editorial Guidance:** Caitlin Love, Tom Chivers, Rebecca Hiscott, Jake Eaton, and Blake Wilson.  
> * **Contributors:** Barry Zhang, Theodora Chu, Daliang Li, Mahesh Murag, Jake Noble, Ravi Trivedi, Tina Vachovsky, Brad Abrams, Henry de Valence, Jeremy Fox, Matt Bell, Allen Li, Chris Gorgolewski, Eugene Yan, Artur Renault, Wei Zhang, Kevin Chen, and David Hershey (*Claude Plays Pokémon*).  
> * **Figures by:** Monika Tuchowska.
