---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-26
hide:
  - navigation
tags:
  - Rust
  - 并发编程
  - 锁中毒
  - 系统架构
title: "废除 Lock Poisoning：Rust 并发编程的反思与演进"
---

# 废除 Lock Poisoning：Rust 并发编程的反思与演进

> # Abolish Lock Poisoning

### 文章背景与核心概要

Rust 标准库中的互斥锁 (Mutex) 设计了一项名为“锁中毒 (Lock Poisoning)”的独特机制：当持有锁的线程发生恐慌 (Panic) 时，该互斥锁会被标记为中毒状态，以防其他线程读到损坏的不完整数据。然而在十多年的工业实践中，开发者们发现这套理论上美好的设计在现实中沦为灾难——几乎没有任何代码能真正安全地恢复中毒状态，惯用的 `lock().unwrap()` 反而将单次恐慌演变为死锁、级联测试崩溃乃至无声的服务瘫痪。随着 Tokio、parking_lot 等核心生态库彻底弃用锁中毒，Rust 官方团队也在积极推进在未来的语言版本中将非中毒锁设为默认行为。

---

## 核心概要

> ## Summary

Rust 标准库中的 `std::sync::Mutex` 包含一项名为**互斥锁中毒 (Mutex Poisoning)** 的特性：一旦某个线程在持有互斥锁期间发生恐慌 (Panic)，该互斥锁就会被标记为“中毒”；此后其他线程对 `lock()` 的调用都会返回一个 `PoisonError` 错误。

> Rust’s `std::sync::Mutex` includes a feature called **mutex poisoning**, which marks a mutex as "poisoned" if a thread panics while holding the lock, causing subsequent calls to `lock()` to return a `PoisonError`. 

从理论设计的初衷来看，锁中毒旨在保护内部数据的不变量 (Invariant)，防止系统在恐慌后遗留下损坏的状态。但本文指出，这项机制在实践中其实是一个失败的尝试。在真实的软件代码库中，几乎没有任何代码能够正确处理中毒的锁；而 Rust 社区惯用的错误处理方式 (即 `lock().unwrap()`) 更是频繁引发死锁、级联测试失败乃至无声无息的生产事故。随着各大核心项目以及标准库自身越来越多地弃用中毒机制，转而投向诸如 `parking_lot` 这类非中毒替代方案，Rust 生态系统最明智的选择就是彻底移除锁中毒作为默认行为。

> While theoretically intended to protect internal data invariants from being left in a broken state, this post argues that lock poisoning is a failed experiment. In practice, codebases rarely handle poisoned locks correctly, and idiomatic error handling (`lock().unwrap()`) frequently leads to deadlocks, cascading test failures, and silent production outages. With major projects and the standard library itself increasingly abandoning poisoning in favor of non-poisoning alternatives like `parking_lot`, the Rust ecosystem would be best served by removing lock poisoning as a default behavior.

---

## 为什么反对锁中毒机制？

> ## The Case Against Poisoning

Rust 拥有一个相当奇特的特性——如果不是因为早期的历史遗留包袱，我认为这项特性放在今天绝不可能被并入这门语言：它就是互斥锁中毒。当 Rust 代码在持有 `std::sync::Mutex` 时发生恐慌，该互斥锁就会“中毒”。这意味着后续对 `lock()` 的任何调用都会返回一个 `PoisonError`。这项特性的初衷是：对象内部可能维系着一些必须得到保证的不变量，而在不恰当的时机发生恐慌可能会打破这些假设，从而使对象陷入不可预知的损坏状态。

> Rust has a curious feature that I don’t think the language would land today if it were not a legacy artifact: mutex poisoning. When some Rust code panics while holding a `std::sync::Mutex`, the mutex is *poisoned*. That means any further call to `lock()` returns a `PoisonError`. The motivation for this feature is that an object might have some internal invariants that need to be upheld, and panicking at the wrong moment might invalidate assumptions and leave an object behind in a broken state.

就我个人而言，我极其讨厌这项特性。我在它身上踩过无数次坑，却想不起有哪怕一次它真正帮到了我。目前 Rust 库团队 (libs team) 正在[热烈讨论](https://github.com/rust-lang/rust/issues/149359)是否要在下一个版本纪元 (Edition) 中将非中毒互斥锁设为默认行为，不出所料，这引发了相当一部分人站出来为这项旧特性辩护。

> Personally, I absolutely hate this feature. It has bitten me so many times, and I cannot recall a single instance where it actually helped me. The libs team is currently [discussing](https://github.com/rust-lang/rust/issues/149359) making non-poisoning locks the default in the next edition, which predictably has caused quite a few people to jump to the defense of the feature.

在这篇文章中，我想详细陈述我个人的观点：为什么中毒锁应该被彻底废除，或者至少降级为极少使用的特殊情况。

> In this post, I want to make my personal case for why poisoned locks should either be entirely removed or made the exception.

首要原因在于，在现实世界的所有代码库中，我至今还没有遇到过任何能够正确处理中毒锁的实现。相反，我见到了大量错误处理它的代码，其造成的破坏甚至远远恶劣于完全不支持中毒机制的 [parking_lot](https://docs.rs/parking_lot) 互斥锁。

> Primarily, this is because I have yet to come across code in the wild that handles a poisoned lock correctly. On the other hand, I have come across enough code that mishandles it, resulting in behavior worse than a [parking_lot](https://docs.rs/parking_lot) lock (which does not support poisoning).

[Josh Triplett](https://news.ycombinator.com/item?id=46041342) 在 Hacker News 的一条评论中直截了当地指出：
> “在标准库的整个演进历史中，我们从未见过哪怕一次有开发者尝试从锁中毒中恢复状态的报告。”

> [Josh Triplett](https://news.ycombinator.com/item?id=46041342) put it quite strongly in a Hacker News comment: 
> 💬 [原文引用 / Original Quote]:
> “In the entire history of the standard library, we have never once seen a single report of anyone attempting to recover from poison.”

当线程持有互斥锁并发生恐慌时，通常只有两种合理的应对方式：要么直接终止整个进程，要么忽略中毒标记继续执行。如果采用 `panic = "abort"`，系统会自动执行前者，锁中毒问题压根不会出现；但根据我所见过的所有现实案例，在基于栈展开 (Unwinding) 的默认模式下，社区习以为常的 `lock().unwrap()` 写法却恰恰选了最糟糕的一条路。

> When a panic happens with a lock held, there are two reasonable reactions: shut the process down, or carry on and ignore the flag. With `panic = "abort"`, you get the former, and poisoning never comes up. From all the evidence I have seen, with unwinding, the idiomatic `lock().unwrap()` picks the worst option of all.

这是因为它既不停止进程，也不允许程序正常继续运行；相反，它会将未来的每一次加锁尝试都变成一次恐慌，有时还会引发灾难性的后果。但这还远远不是该机制现存的唯一问题。下面我将列举其中的几大核心痛点，并结合真实世界中坑害过开发者的开源代码进行剖析。

> That’s because it neither stops the process nor lets it continue; instead, it turns every future lock attempt into a panic with sometimes disastrous effects. But that is not the only issue with the system today. Below, I want to share some of the core problems, referencing real-world code where people got bitten.

---

## 错误对象持有互斥锁：潜在的死锁隐患

> ## The Error Holds the Lock

锁中毒机制中有一个非常隐蔽的细节：`PoisonError` 错误对象本身必须持有锁守卫 (Guard)。这是因为如果你想要忽略中毒标记并继续访问受保护的数据，你必须从这个错误对象中提取出锁守卫。这意味着：只要错误对象还没有被释放，互斥锁就一直处于被锁定的状态！

> One subtle aspect of poisoning is that the `PoisonError` needs to hold the guard. That’s because in order to ignore the poison flag, you need to fetch the guard from the error object. Holding on to the error means holding on to the lock!

这就很容易导致那些涉及错误包装或类型转换的常规代码暗藏死锁 (Deadlock) 隐患。在一个返回 `Box<dyn Error>` 或类似类型的函数中，看起来人畜无害的 `m.lock()?` 写法，只要错误对象生命周期还在，就会一直锁住互斥锁 (参考 issue [#159930](https://github.com/rust-lang/rust/issues/159930))。

> That can cause common code that does error wrapping or error conversions to introduce a deadlock hazard. The innocent-looking `m.lock()?` in a function returning `Box<dyn Error>` or similar keeps the mutex locked for as long as the error lives ([#159930](https://github.com/rust-lang/rust/issues/159930)).

类似的问题同样会出现在 `if let` 语句中。例如在 [cc-switch](https://github.com/farion1231/cc-switch/commit/43077f5539235f0255642ec9aab558d29f3f1b33) 项目中，测试用例发生了卡死挂起，原因就在于其 `if let Ok(..) = lock() { .. } else { .. }` 逻辑的分支中试图再次获取同一个互斥锁，而此时条件表达式中未命名的临时 `PoisonError` 仍然牢牢持有锁守卫。[PC-AI](https://github.com/David-Martel/PC-AI/pull/273/changes) 的 `match` 分支中也出现过一模一样的 Bug，在 [ox-embed-server](https://github.com/anatolykoptev/ox-embed-server/issues/152) 中也能找到类似的受害者。

> This can also happen with `if let`. For instance, in [cc-switch](https://github.com/farion1231/cc-switch/commit/43077f5539235f0255642ec9aab558d29f3f1b33), a test hung because an `if let Ok(..) = lock() { .. } else { .. }` fallback locked the same mutex again while the unnamed `PoisonError` from the condition still owned the guard. [PC-AI](https://github.com/David-Martel/PC-AI/pull/273/changes) had the same bug in a `match` arm, and another case can be found in [ox-embed-server](https://github.com/anatolykoptev/ox-embed-server/issues/152).

---

## 从局部恐慌演变为全盘瘫痪

> ## Panic to Outage

更为刁钻的是，锁中毒并不会做到“快速失败 (Fail-fast)”；一旦处理失当，它会导致系统“永久失败 (Fail forever)”。最开始的恐慌仅仅发生在一个线程上的一次调用中，而且往往发生在与后续失败毫无关联的边角位置。然而在此之后，该互斥锁上后续执行的所有 `lock().unwrap()` 都会紧跟着发生恐慌。由于现代 Rust 代码普遍能够容忍并隔离单点恐慌 (例如线程池、Web 请求处理器、Tokio 异步任务、FFI 外部函数接口边界)，整个宿主进程依然存活，却彻底沦为无法处理任何业务的“僵尸服务”：

> Deviously, poisoning does not fail fast; when done wrong, it fails *forever*. The original panic happens once, on one thread, often somewhere unrelated to future failures. However, every later `lock().unwrap()` on that lock now panics as well. Because so much Rust code survives panics (thread pools, request handlers, Tokio tasks, FFI boundaries), the process stays up and becomes completely useless:

* 在 RLS (Rust Language Server) 中，一次失败的 Cargo 构建在持有 `ENV_LOCK` 环境变量锁时发生恐慌，[导致后续的所有构建运行都无法执行](https://github.com/rust-lang/rls/pull/492)；
* Mozilla 的 [application-services](https://github.com/mozilla/application-services/issues/4661) 项目在崩溃统计中发现 `PoisonError` [一路跃升至第 5 位](https://github.com/mozilla/application-services/issues/4658)，在得出从中毒处理中得不到任何实质收益的结论后，团队果断[迁移到了 parking_lot](https://github.com/mozilla/application-services/pull/4663)；
* 运行在预发布环境中的 [Neon safekeeper](https://github.com/neondatabase/neon/issues/2200) 服务在某个持有全局锁的线程恐慌后，后续的所有时间线查询全部宣告失败，而在系统日志中甚至连最初发生恐慌的原始现场都早已无处寻觅。

> * In RLS, a failed Cargo build panicked with `ENV_LOCK` held, [making any subsequent runs impossible](https://github.com/rust-lang/rls/pull/492).
> * Mozilla’s [application-services](https://github.com/mozilla/application-services/issues/4661) saw `PoisonError` [rise to rank 5](https://github.com/mozilla/application-services/issues/4658) in crash stats and [moved to parking_lot](https://github.com/mozilla/application-services/pull/4663) after concluding they gained no benefit from poison handling.
> * A [Neon safekeeper](https://github.com/neondatabase/neon/issues/2200) on staging failed every timeline lookup after a panic with a global lock held, and the original panic could not even be found in the logs.

除了线上长期运行的服务，自动化测试套件同样深受其害。单个测试用例的断言失败会让共享的静态锁中毒，进而导致其后执行的每一个测试用例都因 `PoisonError` 而连环暴毙。这种级联崩溃问题先后在 [cargo](https://github.com/rust-lang/cargo/pull/12264)、[deno](https://github.com/denoland/deno/pull/6567)、[polars](https://github.com/pola-rs/polars/pull/26627) 以及 [rustc](https://github.com/rust-lang/rust/issues/43155#issuecomment-315535095) 编译器自身中频繁出现。

> While not live services, test suites show the same general issue. One failing test poisons a shared static, and every test after it fails with `PoisonError`. This problem showed up for [cargo](https://github.com/rust-lang/cargo/pull/12264), [deno](https://github.com/denoland/deno/pull/6567), [polars](https://github.com/pola-rs/polars/pull/26627), and [rustc](https://github.com/rust-lang/rust/issues/43155#issuecomment-315535095) itself.

---

## 徒劳的中毒恢复尝试

> ## Attempt at Recovery

即便你在捕获错误后通过 `into_inner()` 提取守卫尝试恢复，互斥锁的中毒标记依然会被保留，后续的所有加锁操作仍会继续走入恢复分支。需要记住的是，在锁中毒特性落地的最初九年里，你甚至根本没有办法清除这一标记——直到 Rust 1.77 版本才正式引入了 `clear_poison` API。无法清除标记意味着：从发生单次恐慌那一刻起，各种潜在高开销的副作用将在随后的每一次访问中反复重演：

> If you recover with `into_inner()`, the flag stays set, and every later access takes the recovery path again. Remember that for the first nine years of Rust after the poisoning feature landed, you could not even clear it, as `clear_poison` only arrived in version 1.77. Not clearing the flag means that potentially expensive side effects will happen repeatedly from that point onward:

* [goose-in-a-pond](https://github.com/jarida-io/goose-in-a-pond/commit/8c7e7fed06385d3dfd2958ba86ef0bb119d56688) 在遭遇单次恐慌后，后续的每一次转录操作都会全量重建解码器状态；
* [librefang](https://github.com/librefang/librefang/commit/5edca0bfcf856324a6fc3701bf441d87ec7c9cca) 在随后的每一次访问中都会无休止地打印相同的警告日志；
* [ox-embed-server 中的连接池](https://github.com/anatolykoptev/ox-embed-server/issues/94) 在每次对象归还时都不得不直接丢弃模型。

> * [goose-in-a-pond](https://github.com/jarida-io/goose-in-a-pond/commit/8c7e7fed06385d3dfd2958ba86ef0bb119d56688) rebuilt its decoder state on every transcription after a single panic.
> * [librefang](https://github.com/librefang/librefang/commit/5edca0bfcf856324a6fc3701bf441d87ec7c9cca) logged the same warning on every access.
> * A [pool in ox-embed-server](https://github.com/anatolykoptev/ox-embed-server/issues/94) threw its model away on every return.

---

## 没人依赖锁中毒，甚至连标准库自己都不用

> ## Nobody Relies on It, Not Even `std`

那么到底有谁真正在严肃处理锁中毒呢？我实在说不上来——但可以肯定的是，标准库 (std) 自己绝对没有。在标准库自身的源码实现中，锁中毒几乎在所有地方都被直接忽略了。早在 [2015 年 3 月](https://github.com/rust-lang/rust/commit/2e8e8ab5648) (距离 Rust 1.0 正式发布还有两个月)，标准 I/O 模块就选择了直接忽略中毒，理由是“任何中毒必然源自用户代码，而这根本不是互斥锁所负责保护的范畴”。这是一个非常普遍的痛点：锁中毒错误往往与互斥锁本身真正受保护的数据毫无干系。

> So who is handling poisonings? I’m really not sure—definitely not the standard library. Almost everywhere in the standard library's own code, it is ignored. Standard I/O has done so since [March 2015](https://github.com/rust-lang/rust/commit/2e8e8ab5648) (two months before 1.0) because “any poison must have been the result of user code which the lock isn’t protecting.” This is a common issue: poisoning errors frequently have nothing to do with the actual mutex that was held.

同样的情况也出现在[恐慌输出捕获](https://github.com/rust-lang/rust/commit/72e96604c01)、[回溯信息锁 (Backtrace Lock)](https://github.com/rust-lang/rust/commit/2d2c9e44939) 以及 [WASI 环境锁](https://github.com/rust-lang/rust/commit/9530ba0fe21) 中。它们全都无一例外地绕过了锁中毒机制。毫无意外，目前官方代码库中正有一个[开放的 PR](https://github.com/rust-lang/rust/pull/148689)，旨在将 `std` 内部所有的互斥锁全面迁移至 `nonpoison` (非中毒版本)。

> The same applies to [panic output capture](https://github.com/rust-lang/rust/commit/72e96604c01), the [backtrace lock](https://github.com/rust-lang/rust/commit/2d2c9e44939), and the [WASI environment lock](https://github.com/rust-lang/rust/commit/9530ba0fe21). They all bypass poisoning, and unsurprisingly, there is an [open PR](https://github.com/rust-lang/rust/pull/148689) to move `std`'s internal mutexes to `nonpoison`.

而整个开源生态系统也大体得出了完全相同的结论：

> The ecosystem has largely come to the same conclusion:

* Tokio 自带的互斥锁完全不具备中毒特性。在内部实现中，它用一个[剥离中毒特性的适配层](https://github.com/tokio-rs/tokio/blob/master/tokio/src/loom/std/mutex.rs)将标准库锁封装了起来。该特性合并时，Carl Lerche 曾直言不讳地评价道：[“我宁愿假装锁中毒机制根本就不存在。”](https://github.com/tokio-rs/tokio/pull/2814#discussion_r485760722)；
* 在某个场景中，Eliza Weisman [必须借助 `into_inner`](https://github.com/tokio-rs/tokio/pull/2828#discussion_r492350077) 在 Drop 析构阶段解绑等待者，“否则链表中就会残留潜在的悬垂指针 (Dangling Pointer)”。我特别想强调这个案例，因为它生动揭示了锁中毒机制如何反过来阻碍了内存安全——而具有讽刺意味的是，内存安全往往是支持者鼓吹保留锁中毒机制的最大借口；
* Wasmtime、`crossbeam-channel` 以及 `tracing-subscriber` 始终对锁中毒视而不见，直接予以忽略；
* `rust-analyzer` 在任务取消导致其求解器频繁中毒后，[全面切换到了 parking_lot](https://github.com/rust-lang/rust-analyzer/pull/1359)，就像早先的 RLS 一样；
* `parking_lot` 的维护者更是[将锁中毒形容为](https://github.com/Amanieu/parking_lot/issues/324#issuecomment-1059616487)一项“严重伤害易用性与可靠性的负面反向特性 (Anti-feature)”，我对这种观点深表赞同。

> * Tokio’s own locks do not poison. Internally, it wraps the standard library lock in an [adapter that removes poison](https://github.com/tokio-rs/tokio/blob/master/tokio/src/loom/std/mutex.rs). When it landed, Carl Lerche remarked, [“I rather pretend lock poisoning isn’t a thing.”](https://github.com/tokio-rs/tokio/pull/2814#discussion_r485760722) 
> * In one case, Eliza Weisman [needed `into_inner`](https://github.com/tokio-rs/tokio/pull/2828#discussion_r492350077) to unlink a waiter during drop, or “we’ll leave the list with a potentially dangling pointer.” I want to point to this in particular because it demonstrates a case where poisoning stood in the way of memory safety—ironically, a property commonly argued as a reason to keep poisoning.
> * Wasmtime, `crossbeam-channel`, and `tracing-subscriber` always ignore lock poisoning.
> * `rust-analyzer` [switched to parking_lot](https://github.com/rust-lang/rust-analyzer/pull/1359) after cancellation poisoned its solver, much like RLS before it.
> * The `parking_lot` maintainer [described poisoning](https://github.com/Amanieu/parking_lot/issues/324#issuecomment-1059616487) as an “anti-feature that hurts usability and reliability,” a sentiment with which I strongly concur.

---

## 为什么只有 Mutex 中毒？设计维度的巨大割裂

> ## Why Only Mutex?

另一个极其刺眼的设计矛盾在于：为什么只有 `Mutex` 实现了中毒机制，而 `RefCell` 却没有？如果说为锁引入中毒机制的理由在于某些代码在临时打破不变量时发生恐慌、进而让其他代码观察到损坏状态，那么这套逻辑毫无疑问应该对单线程内部可变性 (Interior Mutability) 容器一视同仁。

> Another glaring inconsistency is why poisoning is implemented for `Mutex` but not for `RefCell`. Surely, if the case for poisoning is that some code temporarily breaks an invariant, panics, and someone else observes the broken state, this logic should apply equally to single-threaded interior mutability.

只要拿那些常被用来为锁中毒辩护的经典示例，将其中的 `Mutex` 替换为 `RefCell`，你就会遭遇[完全一模一样的问题](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=549fb7c9c0626a0ebd29bfa3a2e97ad4)。这甚至根本不需要多线程参与。而且这绝非仅仅停留在理论推演：Tokio 会自动捕获每个任务的恐慌；当与 `LocalSet` 配合使用时，任务恐慌会体现为 `JoinError`，而紧随其后的下一次 `borrow()` 依然会成功借用，进而[读取到一个空指针 (Null Pointer)](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=925975f7d49c10c0d6821cfeb00e1f60)——这与官方 Issue 追踪器中关于互斥锁的恐慌案例毫无二致。

> Take the usual example argued in favor of poisoning, replace `Mutex` with `RefCell`, and you have [exactly the same problem](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=549fb7c9c0626a0ebd29bfa3a2e97ad4). Threads are not even required. This is far from hypothetical: Tokio catches every task panic. Paired with a `LocalSet`, the panic surfaces as a `JoinError`, the next `borrow()` succeeds, and it [reads a null pointer](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=925975f7d49c10c0d6821cfeb00e1f60) just like the mutex example from the issue tracker.

考虑到异步代码中普遍存在大量的恐慌捕获逻辑——其中很多为了极致性能而被设计为 `!Send`——我根本不认为恐慌在多线程代码中被捕获的频率会显著高于单线程。然而，从来没有任何人跳出来要求让 `RefCell` 也支持中毒机制。

> Given how much panic-catching occurs in async code—much of which is `!Send` for performance reasons—I am not convinced panics are caught more frequently in multi-threaded code. Yet, nobody is asking for `RefCell` to poison.

甚至标准库在自身的各个类型设计上也自相矛盾：

> The standard library isn’t even consistent with itself:

* `LazyLock` 一旦发生恐慌便永久中毒，再也无法读取；
* `OnceLock` 发生恐慌后永远不会中毒；
* `Mutex` 发生恐慌会中毒，但却允许你手动恢复数据。

> * `LazyLock` poisons for good.
> * `OnceLock` never poisons.
> * `Mutex` poisons, but lets you recover.

更为关键的是，锁中毒机制仅仅能够追踪恐慌，而更加普遍的提前返回 (Early Return) 模式同样会引发完全相同的状态损坏问题。使用 `?` 运算符 (以及早已废弃的 `try!` 宏) 随时可能在临界区执行中途提前退出并返回错误，从而在一个并未中毒的正常互斥锁背后留下同样被破坏的不变量。

> Furthermore, poisoning only tracks panics, whereas more common early-return patterns have the exact same issue. The `?` operator (and the legacy `try!` macro) can return early from the middle of a critical section, leaving the same broken invariant behind an unpoisoned lock.

还需注意到，将中毒逻辑强行捆绑在互斥锁上完全是[历史原因造成的巧合](https://github.com/rust-lang/rust/issues/134645#issuecomment-3590942770)。如果真正有需要，完全可以提供一个显式的 `Poison<T>` 泛型包装类型，让开发者在真正需要时能够自主选择为*任何*内部可变性容器引入中毒语义。

> Note also that the coupling of poisoning to mutexes [is historical](https://github.com/rust-lang/rust/issues/134645#issuecomment-3590942770). An explicit `Poison<T>` type would instead allow developers to opt into poisoning for *any* interior mutability wrapper if they truly wanted it.

---

## 我的诉求与未来展望

> ## What I Want

就我个人而言，我由衷希望 Rust 官方团队能够尽快稳定 `std::sync::nonpoison`，并让 `std::sync::Mutex` 在默认情况下直接[解析为非中毒锁](https://github.com/rust-lang/libs-team/issues/169)。如果某些场景确实需要中毒保护，官方可以提供一个独立的 `Poison<T>` 包装容器，让那些确信自己需要 (且有能力正确处理) 该特性的开发者按需选择，并将其自由套用到任何类型上 (无论是 `RefCell` 还是 Tokio 异步线程任务)。

> Personally, I hope the Rust team stabilizes `std::sync::nonpoison` and has `std::sync::Mutex` [resolve to it by default](https://github.com/rust-lang/libs-team/issues/169). If someone genuinely wants poisoning, a separate `Poison<T>` wrapper can be provided so that anyone who believes they need it (and can handle it) can opt into it for any type, including `RefCell` or Tokio threads.

最糟糕的解决方式莫过于妥协性的反向提案：保留锁中毒机制，但将 `lock()` 改为在遇到中毒时直接发生恐慌、而不是返回 `Result`。这种做法除了能稍微理顺持有锁守卫的语义 (并略微提升代码调用的简便性) 之外，只会将系统无声无息的缓慢瘫痪永久固化为*唯一*的行为模式。这与当下大家普遍滥用 `lock().unwrap()` 的后果在本质上毫无差别，而上文罗列的大量真实案例已经充分证明：在存在 `catch_unwind` 恐慌捕获的环境中，这种设计具有极大的系统破坏性。

> The worst possible outcome would be the counter-proposal: keeping poisoning, but having `lock()` panic instead of returning a `Result`. That would only fix held-guard lock semantics (and slightly improve ergonomics), but it would cement the slow, silent outage as the *only* option. That is essentially what every `lock().unwrap()` does today, and the issues listed above provide plenty of evidence that this behavior is deeply problematic in the presence of `catch_unwind`.

文章[《为锁中毒辩护》 (In defense of lock poisoning)](https://sunshowers.io/posts/on-poisoning/) 从反方视角给出了最有力、最精彩的论辩，非常值得一读。但我坚信，现实中压倒性的客观证据所指向的是完全相反的方向——而且大多数严苛的生产级系统 (例如 Oxide) 在遭遇恐慌时都会直接选择终止进程 (Abort)，这显然是一种远比锁中毒更加健壮、更具确定性的工程实践。

> The post [In defense of lock poisoning](https://sunshowers.io/posts/on-poisoning/) is the best argument for the other side and is well worth reading. However, I believe the evidence points overwhelmingly the other way—and most production systems (such as Oxide) abort on panic anyway, which is a far more robust and reasonable behavior.
