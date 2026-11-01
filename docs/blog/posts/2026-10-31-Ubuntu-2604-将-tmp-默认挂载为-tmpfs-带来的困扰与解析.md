---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-31
hide:
  - navigation
tags:
  - Ubuntu
  - Linux
  - systemd
  - cgroups
  - 运维架构
title: "Ubuntu 26.04 将 /tmp 默认挂载为 tmpfs 带来的困扰与解析"
---

# Ubuntu 26.04 将 /tmp 默认挂载为 tmpfs 带来的困扰与解析

### 文章背景与核心概要

随着 Ubuntu 26.04 正式跟进上游 systemd 的默认设计，系统中的临时目录 `/tmp` 已默认被挂载为基于内存的临时文件系统 (tmpfs) 。在个人电脑与内存充裕的工作站上，这一改动不仅能显著加快临时小文件的读写吞吐，还能有效减少固态硬盘 (SSD) 的擦写磨损。然而在多用户共享的算力服务器以及自动化运行的 AI 智能体 (AI Agent) 业务场景中，程序或用户极易无意识地向 `/tmp` 倾倒动辄数十 GB 的大文件，进而引发剧烈的系统内存雪崩。更棘手的是，由于 systemd 控制组 (cgroups) 在用户会话注销 (session teardown) 时的统计漏洞，残留的 tmpfs 内存会脱离单用户资源配额 (`MemoryMax=`) 的管控，使单用户限额机制形同虚设。本文深入拆解了该机制背后的底层机理，并给出了通过屏蔽服务或设置全局 slice 限额等行之有效的工程应对方案。

---

## 内容概要

> ## Summary

本文深入探讨了 Ubuntu 26.04 将 `/tmp` 默认挂载为 `tmpfs` (基于内存的文件系统) 所引发的一系列意外问题。这一调整继承自上游 systemd 的默认行为。虽然对于物理内存 (RAM) 充裕或渴望降低固态硬盘 (SSD) 写入磨损的设备而言此举颇具优势，但在多人共享的计算服务器环境中，普通用户或大语言模型智能体 (LLM Agent) 往往会在不知情的情况下向 `/tmp` 写入庞大的文件，从而引发严重的系统内存压力。本文进一步分析了 `tmpfs` 机制下的 `/tmp` 使用量与 systemd 控制组 (cgroups) 内存记账之间的交互影响，指出了在用户会话注销清理 (session teardown) 和资源配额管控方面存在的关键隐患。

> This article explores the unexpected issues arising from Ubuntu 26.04’s default behavior of mounting `/tmp` as a `tmpfs` (in-memory filesystem), a change inherited from systemd. While beneficial for systems with abundant RAM or those seeking to reduce SSD wear, it causes significant memory pressure on shared compute servers where users or LLM agents unknowingly park massive files in `/tmp`. The post also examines how `tmpfs` `/tmp` usage interacts with systemd cgroup memory accounting, highlighting critical gaps in user session teardown and resource limits.

---

## `tmpfs /tmp` 遭遇的骨感现实

> ## The Unexpected Reality of `tmpfs /tmp`

> 💬 [原文引用 / Original Quote]:
> **理论预期：** “/tmp 目录是放小文件的地方，所以把它挂载为 tmpfs 完全合情合理。”
> 
> **现实打脸：** 我们一台计算服务器的 `/tmp` 目录里赫然堆积了整整 33 GB 的数据。想来大概没人通知过使用服务器的各位用户关于 `/tmp` 变成内存盘这回事吧。
> 
> *(更准确地说，根本没人告诉过他们所运行的程序——包括一大堆正在跑的大语言模型智能体 (LLM Agent)——关于 `/tmp` 的这个变化。)*
> 
> **Theory:** "/tmp is for small files, so that's why we can make it a tmpfs."
> 
> **Actual reality:** 33 GB parked in `/tmp` on one of our compute servers. I guess no one told the people using it about that `/tmp` thing, eh.
> 
> *(More exactly no one told the programs they're running about that `/tmp` thing. Including a bunch of LLM agents.)*

将 `/tmp` 挂载为 `tmpfs` 的配置是 Ubuntu 26.04 中的一项全新默认行为，源于其跟进并采纳了上游 systemd 的默认设定。正如 [Arch Wiki](https://wiki.archlinux.org/title/Tmpfs) 中所记录的，可以通过以下命令禁用 systemd 的这一默认行为：

> This `tmpfs` `/tmp` setup is a new default in Ubuntu 26.04, stemming from its adoption of upstream systemd defaults. As documented in [the Arch Wiki](https://wiki.archlinux.org/title/Tmpfs), this systemd behavior can be disabled with:

```bash
systemctl mask tmp.mount
```

执行该命令后需要重启系统方可生效。尽管在正在承载业务的活跃计算服务器上执行重启可能会造成中断，但通过屏蔽 (mask) 挂载服务，能够确保在后续的每次系统重启中都不会再出现该问题。

> Followed by a system reboot. While rebooting active compute servers can be disruptive, applying the mask ensures the issue will not return upon subsequent reboots.

---

## tmpfs 何时锦上添花，何时又适得其反？

> ## When `tmpfs` Helps vs. When It Hurts

将 `/tmp` 挂载为 `tmpfs` 在某些特定场景下确实非常合理且具备优势：

> A `tmpfs` `/tmp` makes reasonable sense in specific scenarios:

* 系统拥有非常充裕的物理内存 (RAM) ；
* 希望最大程度降低根文件系统所在的固态硬盘 (SSD) 写入磨损；
* 业务场景对 `/tmp` 目录有着极致的输入输出 (I/O) 读写速度需求。

> * You have abundant RAM.
> * You want to minimize SSD write wear on the root filesystem.
> * You require exceptionally fast `/tmp` I/O.

然而，在多用户共享的服务器（例如集中式计算集群）上，这种设计的短板便暴露无遗。普通用户与自动化脚本程序经常会向 `/tmp` 目录中写入数十甚至数百 GB 的庞大数据，并且一放就是好几天，不知不觉中便悄悄蚕食掉了大量极其宝贵的物理内存。

> However, on shared servers—such as compute clusters—it falls short. Users and automated applications frequently write gigabytes of data to `/tmp` and leave it there for days, silently consuming valuable RAM.

---

## 与 systemd 控制组及内存记账机制的交互影响

> ## Interaction with Systemd Cgroups and Memory Accounting

如果你通过 [systemd 对控制组实施内存配额限制](https://utcc.utoronto.ca/~cks/space/blog/linux/StrictOvercommitNoLongerUsing) ，那么挂载为 `tmpfs` 的 `/tmp` 又是如何与这些资源限制相互作用的呢？

> If you enforce [systemd memory limits on cgroups](https://utcc.utoronto.ca/~cks/space/blog/linux/StrictOvercommitNoLongerUsing), how does a `tmpfs` `/tmp` interact with those restrictions? 

### 内存记账机制的工作原理

> ### How Accounting Works

当一个文件被写入挂载为 `tmpfs` 的 `/tmp` 目录时，与当前进程关联的任何处于活跃状态的 systemd cgroup 都会应用相关的 [`MemoryMax=`](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html#MemoryMax=bytes) 限制配置（无论该配额是直接作用于用户的 `user-NNN.slice` 切片，还是细化到了粒度更小的管理单元） 。

> When a file is written to a `tmpfs` `/tmp`, any active systemd cgroup associated with the process applies relevant [`MemoryMax=`](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html#MemoryMax=bytes) settings (whether applied to `user-NNN.slice` or a narrower unit). 

这部分使用量会记录在 cgroup 内存统计接口文件 `memory.stat` 的 **`shmem`** 字段中，该字段专门用于追踪：

> This usage appears in the cgroup's memory accounting under the `memory.stat` **`shmem`** field, which tracks:

> 💬 [原文引用 / Original Quote]:
> *具有交换空间支持 (swap-backed) 的缓存文件系统数据量，**例如 tmpfs**、共享内存段 (shm segments) 以及共享匿名映射 (shared anonymous mmap()s)* —— [Linux Cgroup v2 官方文档](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#memory-interface-files)
> 
> *[The] Amount of cached filesystem data that is swap-backed, **such as tmpfs**, shm segments, shared anonymous mmap()s* — [Linux Cgroup v2 Documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#memory-interface-files)

### 会话注销拆除引发的统计漏洞

> ### The Session Teardown Problem

这种内存记账机制其实非常脆弱。当某位用户注销退出登录且后台没有任何活跃会话残留时，systemd 会在约 10 秒后彻底销毁并拆除对应的 `user-NNN.slice` 单元。

> This accounting is fragile. When a user logs out and leaves no active sessions behind, systemd tears down the `user-NNN.slice` unit roughly ten seconds later. 

一旦该 cgroup 被系统移除：

> Once the cgroup is removed:

1. 这部分内存占用不再归属于该用户的专属 slice 切片，而是转为回退累加至全局的 `user.slice`（或者如果所有用户会话均已结束，则回退归属到根 slice 之中）；
2. 针对该用户此前设定的具体 `MemoryMax=` 内存限制，将不再适用于这些依然滞留在内存中的数据；
3. 用户完全可以在注销前向 `/tmp` 塞入数十 GB 的数据默默囤积内存，而彻底脱离单用户资源配额阈值的任何约束。

> 1. The memory usage is no longer attributed to the user's specific slice, falling back instead to `user.slice` generally (or the root slice if all sessions end).
> 2. The user's specific `MemoryMax=` settings no longer apply to that lingering data. 
> 3. Users can silently hoard gigabytes of RAM in `/tmp` without being bound by per-user thresholds.

由此产生的结果是，严格的“单用户内存配额限制”根本无法与朴素开箱即用的 `tmpfs` `/tmp` 方案可靠共存。虽然像 [`PrivateTmp=disconnected`](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#PrivateTmp=) 这样的特性提供了隔离清理机制，但它们仅限于 `.service` 服务单元使用，并不能直接应用于 `.slice` 用户切片作用域中。

> As a result, strict per-user memory limits cannot reliably coexist with a straightforward `tmpfs` `/tmp`. Mechanisms like [`PrivateTmp=disconnected`](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#PrivateTmp=) offer cleanup behaviors, but they are limited to `.service` units rather than `.slice` scopes.

---

## 全局粗粒度配额带来的一线转机

> ## A Silver Lining for Broad Limits

反之，如果你选择在更宽泛的 `user.slice` 全局层级上严格施加 `MemoryMax=` 配额——特别是在拥有长期驻留用户会话的计算服务器等系统上——整套系统的行为表现就会变得可预测得多。

> Conversely, if you apply `MemoryMax=` strictly at the broader `user.slice` level—especially on systems with persistent user sessions like compute servers—the setup behaves more predictably. 

所有用户对 `/tmp` 的内存消耗都会统一汇总到 `user.slice` 的全局内存配额池中。举例来说，如果为 `user.slice` 设置了 100 GB 的硬性上限，而用户在 `/tmp` 中总共消耗了 30 GB，那么仍有 70 GB 内存可供活跃程序运行、文件系统缓存以及[其他内存开销](https://utcc.utoronto.ca/~cks/space/blog/linux/CgroupsMemoryUsageAccountingII) 正常使用。

> Everyone's `/tmp` consumption pools into `user.slice`'s global memory allocation. For instance, if `user.slice` has a 100 GB cap and users consume 30 GB in `/tmp`, 70 GB remains available for active programs, filesystem caches, and [other memory overheads](https://utcc.utoronto.ca/~cks/space/blog/linux/CgroupsMemoryUsageAccountingII).

*注：这一默认行为或许也能解释为什么在某些 26.04 系统上，[设定严苛的单用户内存限制会导致严重的性能异常](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdSlowSessionStartProblemII) 。因为即便是向 `/tmp` 写入极小的临时文件，也会沉重挤压本就紧张的单用户内存配额。*

> *Note: This default behavior may also explain why [setting aggressive per-user memory limits caused performance anomalies](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdSlowSessionStartProblemII) on certain 26.04 systems, as even temporary writes to `/tmp` heavily impacted tight allocations.*

---

*[阅读英文原文并参与讨论 (3 条评论)](https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604TmpfsTmp?showcomments#comments)*

> *[Read the original post and join the discussion (3 comments)](https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604TmpfsTmp?showcomments#comments).*
