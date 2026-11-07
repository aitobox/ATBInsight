---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-08
hide:
  - navigation
tags:
  - Ghostty
  - Libghostty
  - 终端模拟器
  - C语言
  - ABI稳定性
title: "Libghostty 1.0 正式发布：面向终端仿真的高性能可移植 C 语言核心库"
---

# Libghostty 1.0 正式发布：面向终端仿真的高性能可移植 C 语言核心库

> # Libghostty 1.0

作者：Mitchell Hashimoto  
发布日期：2026 年 11 月 6 日

> *By Mitchell Hashimoto*  
> *Published: November 6, 2026*

---

### 文章背景与核心概要
`libghostty` 是直接从新一代极速终端仿真器 Ghostty 核心代码中抽离出的通用底层引擎。1.0 正式版的发布标志着该项目达成了里程碑式的质变：它不仅提供了完全稳定的 C 语言接口，更承诺提供长期、严谨的应用程序二进制接口 (Application Binary Interface, ABI) 兼容性。凭借轻量高效、不依赖重量级运行时的跨平台架构，它已被 JetBrains 全系列 IDE、Neovim 等头部开发工具大规模深度整合，直接服务于全球超过 1,250 万活跃用户。从资源受限的嵌入式设备到万级并发的云端会话，Libghostty 正在成为现代软件生态构建终端应用坚实可靠的“动力中枢”。

---

## 核心概述

> ## Executive Summary

`libghostty-vt` 1.0 现已正式发布。作为直接从 Ghostty 终端模拟器 (Terminal Emulator) 核心中提炼出的关键引擎，`libghostty` 是一款高度可移植、高性能的终端仿真 C 语言底层库。1.0 里程碑标志着一次至关重要的蜕变：该库及其底层 C 语言应用程序二进制接口 (Application Binary Interface, ABI) 现已全面进入稳定期，不仅享有语义化版本 (Semantic Versioning) 与严苛持续集成 (Continuous Integration, CI) 自动化测试的双重保障，更已在各大主流开发工具中落地，服务于全球超 1,250 万活跃开发者。

> `libghostty-vt` 1.0 has officially been released. Extracted directly from the core of the Ghostty terminal emulator, `libghostty` is a portable, high-performance C library for terminal emulation. This 1.0 milestone marks a critical transition: both the library and its C ABI are now fully stable, backed by semantic versioning, rigorous CI enforcement, and broad industry adoption by over 12.5 million active users across major development tools.

---

## 引言

> ## Introduction

距离最初宣布 [libghostty 即将到来](/writing/libghostty-is-coming) 刚过去一年多时间，该项目已经从最初雏形阶段的 Zig 语言模块，蜕变为一套成熟且随时可用于生产环境、支撑数百万用户日常工具的 C 语言应用编程接口 (Application Programming Interface, API)。本次 1.0 正式发布带来了一整套功能完整、极致流畅的终端模拟器，并配备了严格执行的 ABI 稳定性保障策略。

> A little over a year after the initial announcement that [libghostty is coming](/writing/libghostty-is-coming), the project has evolved from a nascent Zig module into a production-ready C API powering products used by millions. This release delivers a complete, high-performance terminal emulator with a strictly enforced ABI stability policy.

---

## 谁在使用它

> ## Who Is Already Using It

自 2022 年立项以来，`libghostty` 的应用边界早已超越了 Ghostty 终端应用本身，迅速成长为整个软件行业不可或缺的底层基石组件：

> Since its inception in 2022, `libghostty` has grown beyond the Ghostty application to become a foundational building block across the software industry:

* **JetBrains IDEs:** JetBrains 旗下全系集成开发环境 (Integrated Development Environment, IDE) 包括 IntelliJ、PyCharm、GoLand 等内部集成的终端，现已全面切换至 `libghostty` 驱动，为超过 1,250 万活跃用户提供服务。
* **Neovim:** 官方已合并一项拉取请求 (Pull Request, PR)，用 `libghostty-vt` 彻底替代了历史悠久的 `libvterm`，完美解决了困扰社区长达 10 年之久的回滚文本重排 (Scrollback Reflow) 难题。
* **KDE:** 社区开发者正在基于该库开展实验性探索，打造下一代 Konsole 终端替代方案。
* **其他广泛集成:** Vercel 的 Turborepo、`devenv`、Antithesis (用于针对终端界面应用进行模糊测试) 、Ghostel (Emacs 扩展) 、`ghostty-web` (兼容 WASM 与 Xterm.js 规范的 API) 、OrbStack，以及 `herdr`、`cmux` 等前沿智能体工具均已将它深度整合。
* **社区多语言绑定:** 社区已经为 Rust、Go、JavaScript、Swift、Python、.NET、Elixir、Dart、Java 等几乎所有主流语言开发了语言绑定 (Language Bindings)，详情由精选列表 [awesome-libghostty](https://github.com/Uzaaft/awesome-libghostty) 持续追踪收录。

> * **JetBrains IDEs:** The terminal in JetBrains IDEs (IntelliJ, PyCharm, GoLand, etc.) now runs on `libghostty`, serving over 12.5 million active users.
> * **Neovim:** An approved pull request replaces `libvterm` with `libghostty-vt`, resolving a 10-year-old scrollback reflow issue.
> * **KDE:** Developers are experimenting with a Konsole replacement built on the library.
> * **Other Integrations:** Vercel’s Turborepo, `devenv`, Antithesis (for fuzzing TUI apps), Ghostel (Emacs), `ghostty-web` (WASM/Xterm.js-compatible API), OrbStack, and new agentic tools like `herdr` and `cmux` all utilize it.
> * **Community Bindings:** Bindings are available for Rust, Go, JavaScript, Swift, Python, .NET, Elixir, Dart, Java, and more, tracked by the [awesome-libghostty](https://github.com/Uzaaft/awesome-libghostty) list.

---

## ABI 稳定性保障

> ## ABI Stability

1.0 版本的正式推出，在语义化版本体系下确立了严密的 [ABI 兼容性](https://en.wikipedia.org/wiki/Application_binary_interface) 承诺：

> The 1.0 release establishes strict [ABI compatibility](https://en.wikipedia.org/wiki/Application_binary_interface) under semantic versioning:

* **不透明句柄 (Opaque Handles) 设计:** 所有数据对象均采用不透明句柄进行抽象封装。通过枚举类型与规范的设置/获取函数 (Setters/Getters) 避免符号膨胀；即使在新版头文件链接至旧版动态库的场景下，也会安全返回 `GHOSTTY_UNSUPPORTED` 错误代码，而绝不会引发崩溃。
* **CI 自动化严格校验:** 在 Linux 平台上采用 [libabigail](https://sourceware.org/libabigail/) 对所有代码变更进行 ABI 差异检查，并在 macOS 和 WebAssembly (WASM) 平台上辅以标准基准类型清单 (Golden Type Manifests) 进行一致性验证。
* **符号版本控制 (Symbol Versioning):** 在 ELF (Executable and Linkable Format) 目标平台上全面采用导出符号版本控制机制，彻底避免动态链接运行时的符号错配问题。

> * **Opaque Handles:** All objects use opaque handles. Enums and setters/getters prevent symbol bloat, ensuring newer headers linked against older libraries return `GHOSTTY_UNSUPPORTED` rather than crashing.
> * **Automated CI Enforcement:** Changes are checked using [libabigail](https://sourceware.org/libabigail/) on Linux, alongside golden type manifests on macOS and WebAssembly.
> * **Symbol Versioning:** ELF platforms use exported symbol versioning to prevent runtime mismatches.

---

## 打包与软件分发

> ## Packaging and Distribution

1.0 版本引入了稳健完善的构建工具链、源码归档包 (Tarballs) 、依赖清单以及详细文档 (详见 `PACKAGING-LIBGHOSTTY.md`) ：

> The 1.0 release introduces robust build tooling, tarballs, dependency manifests, and documentation (found in `PACKAGING-LIBGHOSTTY.md`):

* **独立发布周期:** 提供完全独立的 tarball 压缩包，仅包含核心库构建所需的必要文件。
* **离线构建支持:** 提供带签名的源码包以及预先缓存了全部 Zig 依赖包的配套离线包，确保在没有外网的环境中也能平滑编译。
* **标准工具链友好:** 原生支持标准共享库名 (SONAME) 、C 头文件、`pkg-config`、CMake 软件包配置，以及 `--prefix`、`DESTDIR`、`lib64` 等经典 Linux 发行版打包参数。

> * **Independent Release Cycle:** Separate tarballs containing only necessary files.
> * **Offline Builds:** Includes signed source tarballs and companion dependency tarballs with all Zig packages pre-cached.
> * **Standard Tooling:** Supports standard SONAMEs, headers, `pkg-config`, CMake package configurations, `--prefix`, `DESTDIR`, and `lib64`.

---

## 依赖项与开源许可

> ## Dependencies and Licensing

* **开源许可协议:** 遵循极度宽松的 MIT 许可协议。
* **运行时开销 (Runtime Footprint):** 默认仅依赖标准 C 库 `libc`，同时完全支持无运行时依赖的独立裸机环境 (Freestanding) 编译。
* **第三方依赖:** 仅整合了极少数采用宽松协议的精品底层库——包括无需 `libc++` 即可编译的 [simdutf](https://github.com/simdutf/simdutf) 与 [Google Highway](https://github.com/google/highway)、Unicode 字形簇表 (Unicode Grapheme Table) ，以及用于解码 Kitty 图像协议的 [Wuffs](https://github.com/google/wuffs)。
* **元数据清单:** 提供完备的机器可读清单，清晰列出每个第三方依赖的精确版本号、SPDX 许可证标识以及哈希校验值 (Hash)。

> * **License:** MIT licensed.
> * **Runtime Footprint:** Requires only `libc` by default, but can compile fully freestanding.
> * **Dependencies:** Integrates minimal, permissively licensed libraries—[simdutf](https://github.com/simdutf/simdutf) and [Google Highway](https://github.com/google/highway) (both built without `libc++`), a Unicode grapheme table, and [Wuffs](https://github.com/google/wuffs) for Kitty graphics protocol decoding.
> * **Metadata:** Machine-readable manifests list every dependency's version, SPDX license, and hash.

---

## 跨平台可移植性与资源占用

> ## Portability & Resource Usage

`libghostty-vt` 在持续集成环境中跨多种操作系统与硬件架构进行了极为全面的自动化测试：

> `libghostty-vt` is extensively tested across multiple platforms and architectures in CI:

| 平台 (Platform) | 芯片架构 (Architectures) |
| :--- | :--- |
| Linux (glibc, musl) | `x86_64`, `aarch64` |
| macOS 13+ | `x86_64`, `aarch64` |
| iOS 13+ | `aarch64` |
| FreeBSD | `x86_64`, `aarch64` |
| Windows | `x86_64` |
| Android | `aarch64`, `x86_64`, `arm` |
| WebAssembly | `wasm32` (freestanding) |

*其他平台——包括裸机系统 (`riscv32`, `thumb`)、WASI、Windows ARM64、illumos 以及 32 位 x86 架构——均在持续集成环境中参与构建，但未包含端到端自动化测试。*

> *Additional platforms—including bare metal (`riscv32`, `thumb`), WASI, Windows ARM64, illumos, and 32-bit x86—are built in CI without automated testing.*

### 极致的资源使用效率

> ### Resource Efficiency

该库在运行时内部不创建任何额外线程，支持接入自定义内存分配器 (Custom Memory Allocators)，能够以极其微小的计算资源与内存开销飞速运转。举例来说，在一台仅配备 4 核 CPU 与 8 GB 内存的普通 Linux 服务器上，它可以轻松维持 10,000 个持续产生输出的活跃终端实例平稳运行。

> The library creates zero threads, allows custom memory allocators, and operates with minimal compute and memory overhead. For example, it can sustain 10,000 active, output-producing terminal instances on a 4-core, 8 GB RAM Linux server.

---

## 未来展望

> ## What's Next

随着 `libghostty-vt` 1.0 的推出，开发者借助任何主流编程语言，仅用 [约 1,500 行 C 代码](https://github.com/ghostty-org/ghostling) 即可轻而易举地搭建起一个功能完备的现代化终端。未来的研发重点将聚焦于坚守严苛的 ABI 稳定性，同时持续拓展对更多前沿终端协议与转义序列的支持。

> With `libghostty-vt` 1.0, developers can build a feature-rich terminal in [~1,500 lines of C](https://github.com/ghostty-org/ghostling) across any major programming language with minimal effort. Future development will focus on maintaining strict stability while continuously expanding support for terminal protocols.

*如需查阅官方文档、示例代码与下载安装，请访问 [lib.ghostty.org](https://lib.ghostty.org/)。*

Boo. 👻

> *Docs, examples, and downloads are available at [lib.ghostty.org](https://lib.ghostty.org/).*
>
> Boo. 👻

---

## 尾注与补充说明

> ## Footnotes

1. *作者注：本文完全由作者手工撰写，未借助任何 AI 辅助。*
2. *使用数据均为估算值；仅 JetBrains 一家在其官方年度报告中就披露了超过 [1,250 万周期性活跃用户](https://www.jetbrains.com/lp/annualreport-2026/)。*
3. *禁用单指令多数据流 (Single Instruction, Multiple Data, SIMD) 优化分支并结合自定义分配器，可使该库完全脱离操作系统环境在裸机硬件上运行。*
4. *功能特性开关 (Feature Flags) 适用于所有编译目标，可按需开启或关闭输入编码、文本搜索、内容选区以及 Kitty 图形协议等子系统。*
5. *文中“特性 (Features)”特指支持的终端协议与控制转义序列，而“性能 (Performance)”则指解析吞吐量与内存占用表现。*

> 1. *Note: This post was completely hand-written with no AI assistance.* 
> 2. *Usage numbers are estimates; JetBrains alone reports [12.5 million recurring active users](https://www.jetbrains.com/lp/annualreport-2026/).*
> 3. *Disabling SIMD paths and custom allocators allows the library to run entirely freestanding on bare-metal targets.*
> 4. *Feature flags work across all targets to toggle subsystems like input encoding, search, selection, and Kitty graphics.*
> 5. *"Features" refers to supported terminal protocols/sequences, and "performance" refers to parsing throughput and memory usage.*
