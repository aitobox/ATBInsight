---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-09-08
hide:
- navigation
tags:
- WebAssembly
- Anubis
- Rust
- 性能优化
- 工作量证明
title: 耗时一年：WebAssembly 终于登陆 Anubis
---
### 文章背景与核心概要

经过长达一年的研发、数百次提交、五代 Pull Request、数十项测试，并重写了部分 Anubis 的 Rust 代码、遭遇了职业生涯中的第一个编译器 Bug、以及至少三次因服务器内存耗尽而崩溃，基于 WebAssembly 的工作量证明（PoW）检查终于正式登陆 Anubis。

在即将发布的版本中，管理员将能够在阈值或机器人防护规则中启用内存硬化的工作量证明函数（特别是 **Argon2id**）。这一转变解决了浏览器端 CPU 性能平衡的问题，有效拦截了幼稚的“AI 生成的 CUDA 求解器”路径，并为客户端-服务器共享二进制文件、基于 Rust 的动态插件以及未来的客户端优化奠定了坚实的基础。

> After a year of work, hundreds of commits, five generations of pull requests, dozens of tests, rewriting part of Anubis in Rust, facing the first compiler bug of a career, and running a server out of RAM at least three times, WebAssembly-based proof-of-work checks are finally arriving in Anubis. 
>
> The next version will allow administrators to enable memory-hard proof-of-work functions (specifically **Argon2id**) in thresholds or bot rules. This transition fixes browser CPU performance balance issues, neutralizes naive "AI-generated CUDA solver" routes, and lays the groundwork for shared client-server binaries, dynamic rust-based plugins, and future client-side optimizations.

---

## 为什么一开始要使用 WebAssembly？

引入 WebAssembly 的核心驱动力是为了在截然不同的架构之间平衡性能——特别是解决手机 CPU 在应对大量网页抓取工具时吃力，同时又不给攻击者留下足够漏洞信息来绕过防御的问题。

采用 WebAssembly 意味着二进制文件运行速度更快，从而让正常用户在面对 Anubis 挑战时能够更快地完成计算并消失。

> The primary driver behind adopting WebAssembly in Anubis is balancing performance across wildly different architectures—specifically addressing the fact that phone CPUs struggle with heavy scrapers without giving attackers enough information to evade mitigation.
>
> Using WebAssembly means the binary runs faster, making Anubis challenges resolve and disappear faster for legitimate users.

### 客户端与服务端运行同一份二进制文件
这种架构的一大优势在于，客户端和服务端可以运行*完全相同的二进制文件*来求解和验证挑战（其工作原理类似于 NES 游戏机中的 CIC 芯片）。

目前，`fast` 挑战分别依赖于 JavaScript 和 Go 的独立实现，这带来了技术债务和同步开销。运行统一的 WebAssembly 二进制文件简化了这一流程，为诸如“每个客户端定制程序合成”等高级实验铺平了道路。

> A major advantage of this setup is letting clients and servers run the *exact same binary* to solve and validate challenges (functioning similarly to the CIC chip in the NES). 
>
> Currently, the `fast` challenge relies on separate implementations in JavaScript and Go, creating technical debt and synchronization overhead. Running a unified WebAssembly binary streamlines this, paving the way for advanced experiments like per-client program synthesis.

### 将 Rust 引入 Anubis
尽管 Anubis 的核心依然是用 Go 语言编写的（利用了其健壮的标准库 HTTP 服务器），但将单体架构拆分为动态插件加载器极大地提升了可维护性。在不使用 CGo 且保持来自 MacBook 的严格交叉编译规则的前提下，动态更新对于适应不断变化的攻击者行为至关重要。

由于 Rust 构建的 WebAssembly 二进制文件体积小、速度极快，因此新的 WebAssembly 组件完全采用 Rust 编写（`no-std`，`wasm32-unknown-unknown`）。

> While Anubis remains core-written in Go (leveraging its robust standard library HTTP server), fragmenting the monolith into a dynamic plugin loader drastically improves maintainability. Without allowing CGo and keeping strict cross-compilation rules from a MacBook, dynamic updates are essential to adapt to shifting threat actor behaviors. 
>
> Because Rust builds small, exceptionally fast WebAssembly binaries, the new WebAssembly components are written entirely in Rust (`no-std`, `wasm32-unknown-unknown`).

### 修复挑战难度缩放机制
历史上的 Anubis 使用字符串比较来计算前导零的*半字节（nibbles）*而不是*比特（bits）*，这意味着难度每增加 1，最坏情况下的计算量就会增加 1,024 倍。引入 WebAssembly 允许我们彻底打破这一旧制，并修复底层的缩放问题。

> Historically, Anubis used string comparisons to count leading zero *nibbles* rather than *bits*, meaning a difficulty increase of 1 made worst-case scenarios 1,024 times harder. Incorporating WebAssembly allows for a clean break and a fix to this underlying scaling issue.

---

## 通常如何添加 WebAssembly（以及 Anubis 是如何做的）

在理想情况下，代码只需编写完成，编译为 WebAssembly，然后直接在现代浏览器中执行即可。然而，Anubis 必须兼顾从现代浏览器一直到 **Chrome 75**（以及向后兼容 Chrome 66 的远期目标）的各种环境。它需要继续支持那些被遗弃的 Android 设备、智能电视，以及缺乏 WebAssembly 或现代标准运行时的受限生态系统（例如 iOS 锁定模式或 GrapheneOS Vanadium）。

> In an ideal world, code is simply written, compiled to WebAssembly, and executed on modern browsers. Anubis, however, must target environments ranging from modern browsers down to **Chrome 75** (and an aspirational fallback to Chrome 66)—retaining support for marooned Android devices, smart TVs, and restricted ecosystems (like iOS Lockdown Mode or GrapheneOS Vanadium) that lack WebAssembly or standard modern runtimes.

```
![./images/b76dc505369e.webp](./images/b76dc505369e.webp)
```

### 主机到客体（Host-to-Guest）的 WASM ABI
尽管 WebAssembly 组件模型（Component Model）通常用于处理接口定义，但由于 Go 端绑定在早期工具链上的限制（例如对结构体或诸如 `Vec<u8>` 的字节字符串的支持不足），我们不得不围绕三个共享的线性内存缓冲区，定制开发了一套 ABI：
1. **数据缓冲区（Data Buffer）：** 最多 4096 字节的挑战数据。
2. **结果缓冲区（Result Buffer）：** 计算完成后从客体中读取的 32 字节缓冲区。
3. **验证缓冲区（Verification Buffer）：** 验证期间由服务端写入的 32 字节缓冲区。

模块暴露了两个核心入口点（`anubis_work` 和 `anubis_verify`），并导入了 `anubis.anubis_update_nonce` 以向 UI 进度条报告哈希速率。

> While the WebAssembly Component Model would normally handle interface definitions, early tooling limitations in Go-side bindings (such as supporting structs or byte strings like `Vec<u8>`) required a custom-crafted ABI centered around three shared linear memory buffers:
> 1. **The Data Buffer:** Up to 4096 bytes of challenge data.
> 2. **The Result Buffer:** A 32-byte buffer read out of the guest when computation finishes.
> 3. **The Verification Buffer:** A 32-byte buffer written by the server during validation.
>
> Modules expose two core entrypoints (`anubis_work` and `anubis_verify`) and import `anubis.anubis_update_nonce` to report hash rates back to the UI progress bar.

---

## 一路走来的挑战

原本只需一周的工作量由于几个复杂的工程阻碍而延长到了一年：

> What should have taken a week expanded into a year due to several intricate engineering obstacles:

### 引入 SIMD 以提升移动端速度
由于 SIMD（单指令多数据）能够极大地加速移动设备上的哈希计算，Anubis 编译了两个版本的 WebAssembly 代码：一个带有 SIMD，另一个则没有。浏览器会通过 `wasm-feature-detect` 动态检测并分发对应的构建版本。

> Because SIMD (Single Instruction Multiple Data) drastically accelerates hashing on mobile devices, Anubis compiles two versions of the WebAssembly code: one with SIMD and one without. The browser dynamically detects and dispatches the appropriate build using `wasm-feature-detect`.

### `wasm2js` 的诞生与消亡
为了支持完全通过策略禁用 WebAssembly 的环境（例如 iOS 锁定模式），我们需要一条替代的执行路径，同时又不能用原生 JavaScript 重写工作量证明逻辑。

通过使用 Binaryen 的 `wasm2js`，我们将 WebAssembly 模块编译成了 JavaScript 解释器。尽管功能可行，但由此产生的代码体积和性能开销证实它只是一种沉重的降级回退方案。

> To support environments where WebAssembly is disabled entirely via policy (e.g., iOS Lockdown Mode), an alternative execution path was required without rewriting the proof-of-work logic in native JavaScript. 
>
> Using Binaryen's `wasm2js`, the WebAssembly modules were compiled down into JavaScript interpreters. While functional, the resulting code footprint and performance overhead confirmed it as a heavy fallback method.

### 遭遇职业生涯中的第一个编译器 Bug
在 GitHub Actions 中构建时，Ubuntu 和 Fedora 对 `wasm2js` 的打包差异暴露了一个 LLVM Bug。具体来说，LLVM 在机器指针顺序下遍历异常处理块，导致构建结果出现确定性的 29 字节漂移。

禁用 ASLR（`setarch --addr-no-randomize`）有助于隔离问题，并最终促成了 LLVM 和 `wasi-sdk` 中的修复。如今，Anubis 直接在仓库中内置了经过验证完好的 `wasm-opt` 和 `wasm2js` 二进制文件，以确保做到字节级完全可复现的构建。

> While building in GitHub Actions, discrepancies between Ubuntu and Fedora packaging of `wasm2js` exposed an LLVM bug. Specifically, LLVM was iterating over exception handling blocks in machine pointer order, causing builds to drift by 29 bytes deterministically. 
>
> Disabling ASLR (`setarch --addr-no-randomize`) helped isolate the issue, leading to a fix in LLVM and `wasi-sdk`. Today, Anubis vendors the exact known-good `wasm-opt` and `wasm2js` binaries directly in the repository to guarantee byte-for-byte reproducible builds.

### 使用 "Chromesweep" 进行自动化浏览器测试
为了在不降低开发者硬件性能的前提下测试旧版浏览器（如 Chrome 75），我们开发了一个名为 `gubal` / `chromesweep` 的测试框架。它在严格的 `NetworkPolicy` 防火墙后方的隔离 Kubernetes 微虚拟机（`Kata Containers`）中运行旧版本的 Google Chrome。

> To test older browsers (like Chrome 75) without degrading developer hardware, a testing harness called `gubal` / `chromesweep` was developed. It runs legacy versions of Google Chrome inside isolated Kubernetes microVMs (`Kata Containers`) behind strict `NetworkPolicy` firewalls.

### 为旧版 WebAssembly 编译 Rust 标准库
由于预编译的 `rust-std` 组件中混入了现代引用类型（例如 `std::sync::Once`），旧版 Chrome 浏览器在加载时抛出了编译错误。

通过传递严格的 `wasm-opt` 标志（`-mvp`, `--enable-sign-ext`, `--enable-mutable-globals`, `--enable-bulk-memory`, `--enable-nontrapping-float-to-int`），从二进制文件中剥离了不必要的较新 WebAssembly 特性，从而确保其能够在旧版浏览器运行时中成功执行。

> Older Chrome versions threw compile errors due to modern reference types slipping into standard library functions (like `std::sync::Once`) via precompiled `rust-std` components. 
>
> By passing strict `wasm-opt` flags (`-mvp`, `--enable-sign-ext`, `--enable-mutable-globals`, `--enable-bulk-memory`, `--enable-nontrapping-float-to-int`), unnecessary newer WebAssembly features are stripped from the binaries, ensuring successful execution on legacy browser runtimes.

```bash
# Chrome shipped sign-ext and mutable-globals in 74, bulk-memory and
# nontrapping-fptoint in 75, multivalue in 85 and simd in 91.
baseline_features="-mvp --enable-sign-ext --enable-mutable-globals \
--enable-bulk-memory --enable-nontrapping-float-to-int"
simd128_features="${baseline_features} --enable-multivalue --enable-simd"
```

---

## 未来改进方向

尽管功能已经完善，但仍有一些领域计划在发布后进行打磨：
* 在 `wasm2js` 回退流程中接入 `update_nonce` 存根。
* 校准挑战难度，以适应 WebAssembly 带来的卓越性能。
* 结合 IP 声誉和 TLS 指纹，扩展移动端请求分类器。
* 在运行时通过 OCI/Docker 镜像仓库实现动态挑战轮换。

> While functional, several areas remain slated for post-release refinement:
> * Wiring up `update_nonce` stubs inside the `wasm2js` fallback flow.
> * Calibrating challenge difficulties to account for high WebAssembly performance.
> * Expanding mobile request classifiers using IP reputation and TLS fingerprinting.
> * Implementing dynamic challenge rotation via OCI/Docker registries at runtime.

---

## 循此苦旅，以达天际 (Ad Astra Per Aspera)

基于 WebAssembly 的工作量证明检查在 **Anubis v1.28.0（代号 *Wuk Lamat*）** 中**默认处于关闭状态**，并计划根据实际的管理员反馈，在 v1.29.0 中将其设为默认开启。

> WebAssembly-based proof-of-work checks ship **off-by-default** in **Anubis v1.28.0 (codenamed *Wuk Lamat*)**, with plans to enable them by default in v1.29.0 based on real-world administrator feedback.