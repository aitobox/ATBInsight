---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-13
hide:
  - navigation
tags:
  - Linux
  - POSIX
  - OpenZFS
  - 操作系统
  - Rust
title: "一切皆是接口：从 mkdir 的细微 Bug 看 POSIX 标准与系统调用边界"
---

# 一切皆是接口：从 mkdir 的细微 Bug 看 POSIX 标准与系统调用边界

### 文章背景与核心概要
在类 Unix 与 Linux 操作系统中，核心基础工具 (Coreutils) 看似微不足道的实现细节，往往会直接触及系统契约的最底层。近期，Rust 编写的 `uutils mkdir` 工具被曝出一个极其隐蔽的行为差异：当底层 `mkdir(2)` 系统调用返回错误但目标目录随后确实存在时，该命令竟然判定为成功并返回退出码 0，这直接导致了知名文件系统 OpenZFS 的自动化回归测试失败。更深层次的危机在于，Unix 生态数十年来长期依赖 `mkdir` 的原子性来实现 Shell 脚本互斥锁，这一异常行为足以破坏并发环境下的排他性保障。本文借由 OpenZFS 的真实排错案例，深入探讨系统调用返回值、退出状态码、临时瞬态错误重试以及 POSIX 标准的严苛边界，揭示了“接口不仅是代码签名，更是整套行为规范”的技术真谛。

---

## 概述

> ## Summary

在由 Rust 重写的核心基础工具集 `uutils` 中，`mkdir` 命令的一个隐蔽缺陷揭示了一个深刻的系统工程命题：核心基础工具中看似无伤大雅的内部实现细节，可能会彻底打破开发者固有的技术预期与长期沉淀的经典工程模式 (例如利用 Shell 脚本进行文件锁互斥操作)。本文以 OpenZFS 测试套件的一次偶发失败为切入点，深入剖析了内部系统调用、命令退出状态码以及 POSIX 严格合规标准之间微妙而敏感的边界。

> A subtle bug in `uutils mkdir` revealed how seemingly minor implementation details in core utilities can break expectations and established patterns, such as shell script locking. By exploring an OpenZFS test suite failure, this article examines the fine line between internal system calls, exit statuses, and strict POSIX compliance.

---

## OpenZFS 与 uutils 的冲突碰撞

> ## The OpenZFS and `uutils` Conflict

最近，开源文件系统 OpenZFS 社区合并了一个非常引人注目的代码提交，用以修复其测试套件中的一处异常：[ZTS: failmode_create_continue: don't rely on mkdir(1)'s exit status](https://github.com/openzfs/zfs/commit/323d497d324c3673a235003bca641bb83d32bb85)。

> Recently, an interesting commit landed in OpenZFS to fix an issue with the test suite: [ZTS: failmode_create_continue: don't rely on mkdir(1)'s exit status](https://github.com/openzfs/zfs/commit/323d497d324c3673a235003bca641bb83d32bb85). 

为了搞清楚问题的来龙去脉，我们不妨先读一读该提交日志中的核心描述摘录：

> To understand the problem, consider this excerpt from the commit description:

> 💬 [原文引用 / Original Quote]:
> On Ubuntu 26.04, mkdir is uutils coreutils, and uutils mkdir 0.8.0 exits 0 when mkdir(2) fails but the directory exists afterwards, which is exactly the case this test creates: zfs_mkdir() creates the entry, then returns EIO from the failed zil_commit(). So the test fails on ubuntu26 with "mkdir: blocked=0 rc=0" although the kernel returned EIO. GNU mkdir exits 1, as does uutils ln for the symlink case.

*(如果你想了解 OpenZFS 底层具体发生了什么，可以在 [测试脚本源码注释](https://github.com/openzfs/zfs/blob/master/tests/zfs-tests/tests/functional/failmode/failmode_create_continue.ksh) 中查阅更详尽的技术细节。)*

> *(You can read more details about what's going on in OpenZFS in [the test script's comments](https://github.com/openzfs/zfs/blob/master/tests/zfs-tests/tests/functional/failmode/failmode_create_continue.ksh).)*

---

## 更深层的影响：Shell 脚本中的目录排他锁

> ## The Broader Impact: Shell Script Locking

事实上，`uutils mkdir(1)` 暴露出的缺陷远不止影响 OpenZFS 这一极端用例。在普遍场景下，当你执行 `mkdir fred` 时，如果 `fred` 目录起初并不存在，底层的 `mkdir(2)` 系统调用在执行中报错，但随后检查发现该目录确实已经存在了，`uutils mkdir` 就会判定为创建成功并返回状态码 `0`。而在相同的场景下，GNU Coreutils 的 `mkdir` 则会果断报错，返回非零状态码 `1`。

> The issue with `uutils mkdir(1)` was more general than just the OpenZFS edge case. Whenever you invoked `mkdir fred`, if the `fred` directory didn't initially exist, the `mkdir(2)` call reported an error, but the directory existed afterward, `uutils mkdir` would succeed and exit with status `0`. Meanwhile, GNU Coreutils `mkdir` would fail, exiting with status `1`. 

这种行为偏差意味着，如果有两个并发的 `mkdir` 进程互相竞态竞争创建同一个目录，它们很可能会双双“宣告成功”。这在工程实践中会带来极大的安全隐患，因为 [利用 mkdir 的原子创建特性历来是 Shell 脚本实现排他锁的经典手法](https://utcc.utoronto.ca/~cks/space/blog/unix/ShellScriptLocking)，尽管如今 [更佳的选择是 Linux 专用的 flock 命令](https://utcc.utoronto.ca/~cks/space/blog/linux/LockShellScriptsWithFlock)。

> This discrepancy meant that two concurrent `mkdir` invocations racing each other could both "succeed" in creating the same directory. This becomes problematic because [mkdir has been a traditional method of doing locking in shell scripts](https://utcc.utoronto.ca/~cks/space/blog/unix/ShellScriptLocking), even though [the better alternative is Linux-only `flock`](https://utcc.utoronto.ca/~cks/space/blog/linux/LockShellScriptsWithFlock).

*(注：据推测，该缺陷已在 uutils 0.11.0 版本中通过 [该 uutils 提交](https://github.com/uutils/coreutils/commit/bf423f388d543b9180db6b7283d82b301f138913) 得到修复，关闭了 [Issue #13970](https://github.com/uutils/coreutils/issues/13970)。不过，如果你无法确认当前运行环境是否已经应用了该修复，[在编写 Shell 脚本排他锁时应优先采用 flock(1)](https://utcc.utoronto.ca/~cks/space/blog/linux/LockShellScriptsWithFlock)。)*

> *(Note: I believe this was fixed in uutils 0.11.0 via [this uutils commit](https://github.com/uutils/coreutils/commit/bf423f388d543b9180db6b7283d82b301f138913), resolving [bug #13970](https://github.com/uutils/coreutils/issues/13970). However, if you are unsure whether your environment has the fix, [you should use flock(1) for shell script locking](https://utcc.utoronto.ca/~cks/space/blog/linux/LockShellScriptsWithFlock).)*

---

## 这种行为是否符合 POSIX 规范？

> ## Is This Behavior POSIX Compliant?

`mkdir(1)` 的这处边缘行为很自然地引发了一个质问：`uutils` 最初的这种行为究竟算不算符合 POSIX 规范？

> This corner of `mkdir(1)` behavior raises an obvious question: is `uutils`'s original behavior POSIX compliant? 

从一种视角来看，对于简单的 `mkdir fred` 命令行调用，POSIX 规范允许在“所有指定的目录均已成功创建”时返回退出码 `0`。有人可能会辩称，即便底层的 `mkdir(2)` 系统调用返回了错误码，那也只是命令内部的实现细节；只要该目录最终由这个 `mkdir` 命令“成功创建”了，返回 0 就是合理的。这种论点在 OpenZFS 的故障场景下颇具说服力——因为在系统调用最终返回 `EIO` 错误之前，该目录在物理存储上确实已经被 `mkdir(2)` 创建出来了。

> On one hand, with a plain `mkdir fred`, exit status `0` is permitted if "all the specified directories were created successfully." One could argue that even though the `mkdir(2)` system call reported an error, that was merely an internal implementation detail, and the directory was ultimately "created successfully" by the `mkdir` command. This argument holds significant weight in the OpenZFS scenario, where the directory was literally created by the `mkdir(2)` call before it returned an `EIO`.

但从另一种视角来看，POSIX `mkdir(1)` 工具规范明文规定其必须“执行与 [`mkdir()`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/mkdir.html) 函数等价的操作……”；而 POSIX `mkdir()` C 库函数本身有一项硬性规定：如果目标目录已经存在，则必须报错失败。

> On the other hand, the POSIX `mkdir(1)` standard is obliged to "perform actions equivalent to the [`mkdir()`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/mkdir.html) function [...]", and the POSIX `mkdir()` function is specifically required to fail if the target already exists. 

更广泛地讲，如果一个合规的 POSIX `mkdir` 程序是通过调用 POSIX 标准的 `mkdir()` 实现的，那么只要 `mkdir()` 返回了错误码，程序就必须将其认定为执行失败并退出返回非零状态码。退一步说，即便某个 `mkdir` 程序使用了其他底层替代机制，标准规范中“等价操作”的措辞也强烈暗示着：只要内核报告该目录已经存在，或者在创建目录过程中发生了任何错误，该命令都必须报告失败。

> More broadly, if a POSIX `mkdir` program operates by calling the POSIX `mkdir()`, it must consider an error return from `mkdir()` as an error and exit with a non-zero status. Even if a `mkdir` program uses an alternate mechanism, the equivalence wording strongly implies it should fail if the kernel reports that the directory already exists—or if any error occurs during directory creation.

*(考虑到行业历来将 `mkdir` 用作排他锁机制，POSIX 标准的原意毋庸置疑是：如果用户当前的这一次 `mkdir` 调用没能亲手成功创建出该目录，它就必须返回非零的错误状态码。)*

> *(Given the traditional use of `mkdir` as a locking mechanism, POSIX undoubtedly intends that if your invocation of `mkdir` did not successfully create the directory, it must exit with a non-zero status.)*

---

## 瞬态错误与重试机制

> ## Transient Errors and Retries

这里还有一个耐人寻味的边缘场景：如果底层的非 POSIX `mkdir(2)` 系统调用返回了“系统调用被中断” (`EINTR`) 或类似的潜在瞬态错误 (类似于 OpenZFS 中遇到的 `EIO` 场景) ，一个合乎 POSIX 标准的 `mkdir` 程序究竟该如何应对？

> An interesting edge case involves what a POSIX `mkdir` program should do if a non-POSIX `mkdir(2)` call reports an "interrupted system call" (`EINTR`) or a similar potentially transient error (akin to the OpenZFS `EIO` case). 

* 如果你重试执行 `mkdir(2)` 并且重试成功，那么由你的 POSIX `mkdir` 程序对外返回成功是完全站得住脚的。
* 如果你在重试时遇到了 `EEXIST` 或其他永久性错误，程序就必须报错失败。
* 那么，程序能否在报错后直接检查目标目录当前是否存在，若存在就对外谎报成功呢？在实际工程中，这种做法在语义上非常站不住脚，因为你根本无法确认这个目录究竟是“你”刚刚创建的，还是被并发的其他进程创建的；尽管这在字面上是否严格违反 POSIX 标准仍存有争议。

> * If you retry `mkdir(2)` and it succeeds, reporting success from your POSIX `mkdir` program seems defensible. 
> * If you retry and encounter `EEXIST` or another permanent error, you must fail. 
> * Can you simply check if the directory now exists and report success? Practically, that is legally murky because you cannot be certain *you* created the directory, though whether it strictly violates POSIX is debatable.

你的 `mkdir` 工具可能会通过调用底层 `mkdir(2)` 系统调用的封装库，隐式且自动地对被中断的系统调用进行重试。虽然 `EINTR` 经常给开发者带来麻烦，但 [它的存在有着不可替代的底层合理性](https://utcc.utoronto.ca/~cks/space/blog/unix/WhyEINTR)。由于 `uutils mkdir` 深度依赖 Rust 标准库 ([代码引用](https://github.com/uutils/coreutils/blob/main/src/uu/mkdir/src/mkdir.rs#L247)、[官方文档](https://doc.rust-lang.org/std/fs/struct.DirBuilder.html#method.create))，任何上层工具的实现都必须对这些底层假设保持清醒与敬畏。

> Your `mkdir` program might handle this implicitly by calling a library wrapper around the underlying `mkdir(2)` system call that automatically handles retries for interrupted system calls. While `EINTR` can be annoying, [it exists for valid reasons](https://utcc.utoronto.ca/~cks/space/blog/unix/WhyEINTR). Since `uutils mkdir` relies on the Rust standard library ([reference](https://github.com/uutils/coreutils/blob/main/src/uu/mkdir/src/mkdir.rs#L247), [documentation](https://doc.rust-lang.org/std/fs/struct.DirBuilder.html#method.create)), implementations must remain mindful of these underlying assumptions.
