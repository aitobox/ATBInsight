---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-08
hide:
  - navigation
tags:
  - Anthropic
  - claude.ai
  - 性能优化
  - Web 工程
  - 性能爬坡
  - Valgrind
  - 工具教程
title: "两周提速三倍：Anthropic 团队如何利用 Claude 爬坡优化 claude.ai 核心体验"
---

### 文章背景与核心概要
随着大语言模型交互界面功能日益丰富，前端渲染延迟与卡顿往往成为影响用户体验的最大瓶颈。Anthropic 工程团队在短短两周的密集冲刺中，通过引入接近 Opus 5.5 能力水平的内部研究模型 Claude Tag，对 Web 端的 claude.ai 与 Claude 桌面端应用展开了全方位的性能重构。团队以覆盖 95% 用户日常操作的四大核心链路为突破口，由 Claude 自主定位瓶颈、构建确定性基准测试、提交优化代码并监控上线指标，人类工程师则把控战略方向与体验取舍，累计合入了 3,000 余项改进且未发生任何线上故障。冷启动输入就绪时间从 3.1 秒锐减至 0.55 秒，整体核心体验提速近 3 倍，每天为全球用户节省数万小时等待时间。这一实践生动证明：只要性能指标可被精准度量，AI 智能体就能以“爬坡算法”持续驱动工程系统的极致优化。

---

# 两周提速三倍：Anthropic 团队如何利用 Claude 爬坡优化 claude.ai 核心体验

> # How We Made claude.ai 3x Faster in Two Weeks

**作者：** Raymond Wang, Sam Attard, Issac G.  
**发布时间：** 2026 年 9 月 23 日  
**阅读时长：** 15 分钟  
**分类：** 工程实践 (Engineering)  

> **Authors:** Raymond Wang, Sam Attard, and Issac G.  
> **Published:** Sep 23, 2026  
> **Reading Time:** 15 min  
> **Category:** Engineering  

---

## 内容总结

> ## Summary

在短短两周的攻坚冲刺中，工程团队借助名为 Claude Tag 的内部研究模型，将 claude.ai 网页版与 Claude 桌面端应用的核心用户体验提速了约 **3 倍**。团队重点聚焦于占用户日常操作 95% 的四大核心旅程——启动应用程序、开启新对话、加载历史对话以及发送消息——期间累计合并了超过 3,000 项代码变更，且未引发任何一次影响用户的线上故障或代码回滚。这项实践最核心的启示在于：**只要一项指标能够被精准度量，Claude 就能对其进行针对性的爬坡优化 (Hill Climbing) 。**

> In a two-week sprint, the engineering team used an internal research model (Claude Tag) to make the core user experience of claude.ai and the Claude desktop app roughly **3x faster**. By focusing on the journeys that comprise 95% of user activity—launching the app, starting a conversation, loading an existing conversation, and sending a message—they merged over 3,000 changes without a single customer-facing incident or rollback. The core takeaway: **once Claude can measure something, it can optimize and hill-climb it.**

---

## 任务概况

> ## The Brief

今年 8 月，团队在两周的冲刺中让 claude.ai 和 Claude 桌面端的核心交互体验实现了约 3 倍的提速。此前常有用户反馈应用在交互时略显迟滞，为此，整个团队在单个 Slack 频道中高效协同，而 Claude 则作为核心成员深度参与到了频道内的每一个讨论串中。

> This August, the core user experience of claude.ai and the Claude desktop app was made roughly 3x faster in a two-week sprint. Users had noted the app felt slow, and the team coordinated everything out of a single Slack channel with Claude participating in every thread.

团队重点攻坚了四大核心操作链路 (涵盖 Web 端与桌面端的 13 项独立度量指标) ，在全新加载页面时，用户从打开页面到可以开始键入内容的时间 (Time to a typeable page) ，在 75 分位点 (P75) 下从 **3.1 秒骤降至 0.55 秒**。汇总到全局来看，这项优化每天能为用户省去数万小时的无谓等待。

> Focusing on four primary user journeys (thirteen distinct measurements across web and desktop), time to a typeable page on a fresh load dropped from **3.1 seconds to 0.55 seconds** (at the 75th percentile). In aggregate, this saves tens of thousands of user-hours of waiting every day.

团队充分利用了处于测试阶段的 **Claude Tag** (Beta) ，其背后运行着能力大体与 Opus 5.5 相当的内部研究模型。在整个过程中，Claude 负责主动搜寻性能瓶颈、搭建实验室基准测试 (Benchmark) 、交付优化代码并监控每次发布部署；而人类工程师则负责把控顶层战略目标、裁决关键的架构权衡，并最终审批每一项代码修改。

> The team leveraged **Claude Tag** (beta), running an internal research model roughly comparable to Opus 5.5. Claude discovered bottlenecks, constructed benchmarks, shipped enhancements, and monitored every deployment. Humans set the overarching goals, made key tradeoff decisions, and approved modifications.

---

## 万物皆可爬坡优化

> ## Anything Can Be Hill Climbed

为了打破标准发布周期的节奏限制实现超高速迭代，团队除监测常规的物理耗时 (Wall-clock timings) 外，还专门探索了一套确定性的实验室度量体系，用作持续集成 (Continuous Integration, CI) 流程中的防护底线：

> To iterate faster than the standard deployment cadence, the team sought deterministic lab measurements that could act as CI guardrails alongside wall-clock timings:

* **指令执行计数 (Instruction counts) ：** 在 Valgrind 工具链下搭配 `node --predictable` 运行基准测试，消除执行波动。
* **浏览器端遥测数据 (Browser telemetry) ：** 统计 React 提交次数、来自 V8 精准代码覆盖率的函数调用次数、布局与样式重新计算 (Layout/Style-recalc) 次数以及 DOM 变更节点数。

> * **Instruction counts:** Running benchmarks under Valgrind with `node --predictable`.
> * **Browser telemetry:** React commits, function call counts from V8 precise coverage, layout/style-recalc counts, and DOM mutations.

通过针对性精简高频关键路径 (例如组装对话消息树或扫描状态信息) 上的底层指令开销，热点代码的指令计数最高降低了 48%，直接转化为物理运行耗时的大幅削减。**至此，性能度量不再是被动记录的“第零步”，而是成为了驱动优化爬坡的“第一步”。**

> By reducing instruction counts on hot paths (like assembling a conversation’s message tree or scanning status lines), instruction counts dropped by up to 48%, yielding massive wall-clock speedups. **Measurement ceased to be a passive step zero; it became step one of the optimization climb.**

---

## 逐串推进：异步闭环工作流

> ## The Loop, Thread by Thread

本次冲刺通过分布在数百个并行讨论串中的持续异步闭环高效运转：

> The sprint operated as a continuous asynchronous loop across hundreds of parallel threads:

1. **问题发现 (Discovery) ：** 工程师在 Slack 中开启一个新讨论串，附上截图或录屏，指出某处交互存在卡顿；
2. **基准构建 (Benchmarking) ：** Claude 追踪交互执行链路，并在本地构建可复现的实验室基准测试；
3. **原型开发 (Prototyping) ：** Claude 提交体量合理的 Pull Request，并将所有涉及前端展示的改动置于特性开关 (Feature Flag) 之后保护；
4. **部署验证 (Deploy & Verify) ：** 部署上线后，Claude 持续监控生产环境的线上遥测数据；
5. **棘轮锁定 (Ratchet) ：** 一旦指标确认改善，便在 CI 中永久收紧该基准测试的阈值底线 (如同只能向前锁定的棘轮) ；若未达预期，则迅速回退特性开关并继续迭代排查。

> 1. **Discovery:** An engineer opens a thread highlighting a slow interaction with screenshots or recordings.
> 2. **Benchmarking:** Claude traces the flow and builds a lab benchmark.
> 3. **Prototyping:** Claude submits appropriately sized pull requests, placing user-visible changes behind feature flags.
> 4. **Deploy & Verify:** Claude monitors field data post-deployment.
> 5. **Ratchet:** If performance improves, the benchmark baseline is permanently tightened in CI; otherwise, flags are reverted and iterated upon.

---

## 横向拓展与工程防护网

> ## Scaling Horizontally and Guardrails

随着这种协作模式的横向铺开，Claude 深入挖掘出了一批隐蔽的底层顽疾——小到每次按键输入都会触发多达 6,900 次 Hook 重新渲染、低效的 CSS 选择器、静默发生的页面隐式重载，大到代码语法高亮期间潜藏的 UTF-16 字符串转换缺陷。

> As the loop scaled, Claude diagnosed deep underlying issues—from 6,900 hooks re-rendering on every keystroke, to inefficient CSS selectors, hidden reloads, and UTF-16 string conversion bugs during syntax highlighting.

为了在这种极高的推进节奏下坚守系统稳定性，团队部署了极为严密的工程安全防护机制：

> To maintain stability under this velocity, strict safety mechanisms were deployed:

* 全自动化的代码审查机制与强制性的单元测试覆盖；
* 短周期的特性开关 (累计引入近 200 个，其中半数以上在冲刺结束前便已完成验证并彻底清理) ；
* 完备的视觉与行为回归测试 (例如将轻量静态 HTML 输入框与完整的 React 渲染组件进行像素级精准比对) 。

> * Automated code reviews and mandatory unit tests.
> * Short-lived feature flags (nearly 200 introduced, over half cleaned up by sprint's end).
> * Comprehensive visual and behavioral regression testing (e.g., matching a static HTML composer to React renders down to the pixel).

---

## 人工领航与 8 毫秒帧预算

> ## Steering and the 8-Millisecond Budget

在高速迭代中，人类工程师的领航把关至关重要，主要体现在三个维度：

> Human involvement remained critical for three reasons:

* **雄心定力 (Ambition) ：** 鼓励 Claude 突破保守的技术预估 (“我们拥有重构任何组件的能力，请更大胆一些”) ；
* **审美感知 (Taste) ：** 通过屏幕截图与录屏仔细审视用户可见的交互体验权衡；
* **聚焦方向 (Direction) ：** 确保各个讨论串议题聚焦、按关键时序推进，且始终死磕高收益瓶颈。

> * **Ambition:** Pushing Claude past cautious estimates ("we have the power to do anything. please be braver").
> * **Taste:** Reviewing user-perceptible UX tradeoffs via screenshots and recordings.
> * **Direction:** Keeping threads narrow, sequence-focused, and high-impact.

这种人机协同把关的代表作，是对超长流式输出响应期间渲染帧率的极致优化。面对 **8.33 毫秒的时间预算 (对应 120 Hz 刷新率) **，Claude 重构了流式数据块 (Chunk) 的渲染逻辑以消除冗余计算，确保模型在输出长篇回答时，搭载 Apple Silicon 芯片的 MacBook 依然能保持 120 fps 的丝滑流畅度。

> This collaborative steering culminated in optimizing frame rates during long streaming responses. By targeting an **8.33 millisecond budget (120 Hz)**, Claude refactored chunk rendering to eliminate redundant work, ensuring long answers maintained smooth 120 fps rendering on Apple Silicon MacBooks.

---

## 未来展望

> ## What’s Next

如今，claude.ai 与桌面端应用在自动化性能棘轮的守护下，运行速度已提升了约 3 倍。团队未来的优化重点将放在攻坚 95 分位点 (P95) 的极端场景、超长对话链路以及边缘网络环境下的性能表现。

> Today, claude.ai and the desktop app operate roughly 3x faster, protected by automated performance ratchets. Future efforts will target the 95th percentile, longer conversations, and edge performance profiles.

*特别鸣谢贡献者：Alfred Xing, Anthony Morris, Benjamin Pasero, Chase McCoy, Joshua N., Luke Deen Taylor, Marius Schulz 与 Shelley Vohr。同时由衷感谢 Boris Cherny 鼓励团队树立更远大的技术抱负。*

> *With contributions from Alfred Xing, Anthony Morris, Benjamin Pasero, Chase McCoy, Joshua N., Luke Deen Taylor, Marius Schulz, and Shelley Vohr. Special thanks to Boris Cherny for encouraging higher ambition.*
