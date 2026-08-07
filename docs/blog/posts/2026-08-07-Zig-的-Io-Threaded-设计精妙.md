---
categories:
- 研究解读
date: 2026-08-07 08:39:34
hide:
- navigation
title: Zig 的 Io.Threaded 设计精妙
---
### 文章背景与核心概要

这篇文章探讨了 Zig 语言中新引入的 `std.Io.Threaded` 接口实现。它通过标准的操作系统线程和阻塞式的系统调用来实现并发操作。有别于传统的难以处理取消操作的线程模型，Zig 在 POSIX 系统上巧妙地运用了基于信号的协议（而在 Windows 系统上使用 `NtCancelSynchronousIoFile`），从而实现了对线程的安全中断。通过将这一机制整合到语言的错误处理模型中，Zig 在无需引入像 `io_uring` 这样复杂的现代异步运行时的前提下，提供了一种实现可靠取消操作的方法。

### 翻译正文

> # Zig's Io.Threaded is Neat
> 
> *August 6, 2026*
> 
> [std.Io.Threaded](https://codeberg.org/ziglang/zig/src/commit/16b42da3fd359bf5ae602aa0153e3ec1d6d14822/lib/std/Io/Threaded.zig) is one of the implementations of Zig’s new `Io` interface that enables concurrency. While it might seem like a "boring" thread-based implementation, it is remarkably elegant. It solves a long-standing challenge in systems programming—reliable cancellation of blocking syscalls—in a way that is more robust than previously thought possible.

# Zig 的 Io.Threaded 设计精妙

*2026年8月6日*

[std.Io.Threaded](https://codeberg.org/ziglang/zig/src/commit/16b42da3fd359bf5ae602aa0153e3ec1d6d14822/lib/std/Io/Threaded.zig) 是 Zig 新的 `Io` 接口的实现之一，用于支持并发。虽然它看起来像是一个“无聊”的基于线程的实现，但它其实异常优雅。它解决了一个系统编程中长期存在的难题——对阻塞式系统调用进行可靠的取消——且采用了比以往认为可能的还要稳健的方式。

---

> ## Summary
> The article explores Zig's `std.Io.Threaded`, an implementation that provides concurrency using standard OS threads and blocking syscalls. Unlike traditional threading models that struggle with cancellation, Zig uses a clever signal-based protocol on POSIX (and `NtCancelSynchronousIoFile` on Windows) to allow threads to be interrupted safely. By integrating this into the language's error-handling model, Zig provides a way to achieve reliable cancellation without the overhead or complexity of modern asynchronous runtimes like `io_uring`.

## 摘要
本文探讨了 Zig 的 `std.Io.Threaded`，这是一个使用标准操作系统线程和阻塞式系统调用来提供并发支持的实现。与在取消操作上举步维艰的传统线程模型不同，Zig 在 POSIX 上使用了一个巧妙的基于信号的协议（在 Windows 上则是 `NtCancelSynchronousIoFile`），使得线程可以被安全地中断。通过将这一机制集成到语言的错误处理模型中，Zig 提供了一种实现可靠取消的方法，而无需承担现代异步运行时（如 `io_uring`）的开销或复杂性。

---

> ## Concurrency vs. Parallelism
> Drawing from [@tedinski](https://www.tedinski.com/2018/10/16/concurrency-vs-parallelism.html), we can distinguish the two:
> * **Concurrency** is about handling asynchronous, nondeterministic events.
> * **Parallelism** is about using hardware resources to perform tasks simultaneously.
> 
> Parallelism is typically **deterministic/declarative** (e.g., Rayon in Rust), where the platform manages partitioning. Concurrency, however, **invariably involves cancellation**. When two asynchronous tasks run, one may need to actively cancel the other because it has become redundant or impossible to complete.

## 并发 (Concurrency) 与并行 (Parallelism)
借鉴 [@tedinski](https://www.tedinski.com/2018/10/16/concurrency-vs-parallelism.html) 的观点，我们可以区分两者：
* **并发** 是关于处理异步、非确定性的事件。
* **并行** 是关于使用硬件资源同时执行任务。

并行通常是**确定性/声明式的**（例如 Rust 中的 Rayon），由平台管理任务划分。然而，并发**必然涉及取消操作**。当两个异步任务运行时，其中一个可能需要主动取消另一个，因为它已变得多余或无法完成。

> ## Just Use Threads
> The primary issue with "just using threads" is the inability to cancel them when they are blocked inside a kernel syscall. While you can easily check for cancellation in a user-space loop, you are stuck once you hit a syscall like `read(fd, buffer)`. Zig’s `Io.Threaded` solves this by allowing standard OS threads to be interrupted reliably.

## “只用线程”就好？
“只用线程”的首要问题是，当线程阻塞在内核系统调用内部时无法将其取消。虽然在用户空间循环中可以很容易地检查取消标志，但一旦执行了诸如 `read(fd, buffer)` 之类的系统调用，你就会被卡住。Zig 的 `Io.Threaded` 通过允许标准操作系统线程被可靠地中断，从而解决了这个问题。

> ## SIGIO
> On POSIX, Zig uses a "cursed" but effective signal-based protocol:
> 1. The canceling thread sets a flag in shared memory.
> 2. It signals the target thread in a loop.
> 3. The target thread, upon receiving `EINTR` from a syscall, checks the flag.
> 4. If the flag is set, the thread acknowledges the cancellation and begins unwinding; otherwise, it retries the syscall.
> 
> On Windows, this is handled more directly via `NtCancelSynchronousIoFile`. In Zig, this cancellation is materialized as `error.Canceled`, treating cancellation as a specific type of error payload.

## SIGIO 信号机制
在 POSIX 系统上，Zig 使用了一种“奇葩”但有效的基于信号的协议：
1. 发起取消的线程在共享内存中设置一个标志。
2. 它在一个循环中向目标线程发送信号。
3. 目标线程从系统调用中收到 `EINTR` 错误后，会检查该标志。
4. 如果标志被设置，线程将确认取消操作并开始栈展开 (unwinding)；否则，它将重试系统调用。

在 Windows 上，这通过 `NtCancelSynchronousIoFile` 更直接地处理。在 Zig 中，这种取消被具象化为 `error.Canceled`，即将取消视作一种特定类型的错误有效载荷。

> ## Prior Art
> * **Java:** Thread interruption exists but does not support interrupting syscalls, making IO operations effectively non-interruptible.
> * **pthread_cancel:** This mechanism exists but lacks integration with language-level features like `try` and `defer`, making cleanup difficult. It also suffers from the high cost of thread creation.
> * **Zig's Approach:** Zig separates "may run concurrently" from "must run concurrently" at the interface level. By using a thread pool and precise naming (`io.async` vs `io.concurrent`), Zig provides a clear, performant, and safe model for concurrency that avoids the "twilight zone" between kernel, runtime, and language.

## 现有技术的对比
* **Java:** 存在线程中断机制，但不允许中断系统调用，这使得 IO 操作实际上无法被中断。
* **pthread_cancel:** 该机制确实存在，但缺乏与诸如 `try` 和 `defer` 等语言级别特性的整合，导致清理工作困难重重。它还受制于线程创建的高昂成本。
* **Zig 的方法:** Zig 在接口层面将“可能并发运行”与“必须并发运行”分离开来。通过使用线程池和精确的命名（`io.async` vs `io.concurrent`），Zig 提供了一个清晰、高性能且安全的并发模型，避开了内核、运行时和语言之间的“灰色地带”。
