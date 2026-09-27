---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-09-25
hide:
  - navigation
tags:
  - Linux
  - proc 文件系统
  - systemd
  - 系统调用
  - 运维工程
  - 审计子系统
title: "Linux 程序对 proc 目录的隐秘依赖远超想象：systemd 沙盒限制与审计实战"
---
# Linux 程序对 proc 目录的隐秘依赖远超想象：systemd 沙盒限制与审计实战

> # Linux programs look at things in `/proc` more than you'd expect

### 文章背景与核心概要
在现代 Linux 系统安全加固中，systemd 提供了诸如 `ProcSubset=pid` 等沙盒化配置，试图对受限服务屏蔽除自身进程以外的 `/proc` 虚拟文件信息。然而，这种隔离策略极易引发意料之外的程序故障。通过借助 Linux 审计子系统 (Linux Audit Subsystem) 追踪系统调用，我们发现诸如 Go、Python、Rust 等语言运行时和常见系统工具在冷启动时对 `/proc` 和 `/sys` 存在着极其深入且隐蔽的访问依赖，用于并发配额检测或内存分配调优。本文深入剖析了这些依赖背后的原因，并演示了如何使用审计规则精准监控此类行为，为服务器安全沙盒构建与服务排错提供实践指引。

---

## 概要

> ## Summary

当 systemd 启用类似 `ProcSubset=pid` 的沙盒选项限制服务视图时 (该选项会隐藏除任务和进程本身之外的所有内容) ，往往会导致诸多意料之外的程序异常。通过使用 Linux 审计子系统 (Linux Audit Subsystem) ，我们可以直观地洞察到常见的 Linux 应用程序、语言运行时以及基础工具在启动之初对 `/proc` 和 `/sys` 的依赖程度究竟有多深——它们通常需要借此完成并发调优、内存管理或底层环境探测。

> When systemd restricts a service's view of `/proc` using options like `ProcSubset=pid` (which hides everything except task- and process-related information), it can cause unexpected issues. Using the Linux audit subsystem, we can discover just how heavily common Linux programs, language runtimes, and standard utilities rely on reading `/proc` and `/sys` on startup—often for concurrency tuning, memory management, or environment detection.

---

## 对 /proc 的隐秘依赖

> ## The Hidden Reliance on `/proc`

在探讨 Ubuntu 26.04 中 systemd 的 `apache2.service` 是如何 [限制 Apache](https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604ApacheRestrictions) 时，一个引人注目的配置项是 [`ProcSubset=pid`](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#ProcSubset=)。该配置会将服务在 `/proc` 目录下所能看到的内容大幅精简，除了与当前任务和进程相关的条目之外，其余信息全部对服务隐匿 (具体行为可参考 [Linux 内核文档](https://docs.kernel.org/filesystems/proc.html#mount-options) 说明) 。

> Yesterday's exploration into how Ubuntu 26.04's systemd `apache2.service` [restricted Apache](https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604ApacheRestrictions) highlighted the use of [`ProcSubset=pid`](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#ProcSubset=). This setting removes everything from a service's view of `/proc` apart from task- and process-related entries (as outlined in [the kernel documentation](https://docs.kernel.org/filesystems/proc.html#mount-options)). 

systemd 官方文档明确警告过，这项配置可能会对正在运行的程序产生影响。出于好奇，想弄清楚普通程序究竟有多频繁地查询 `/proc`，我借助 Linux 审计子系统进行了监测，而得到的答案令人印象深刻：**其频率相当可观。**

> Systemd's documentation explicitly warns that this may affect running programs. Curious to see how often regular programs query `/proc`, I used the Linux audit subsystem to find the answer: **a fair bit.**

虽然 [proc(5)](https://www.man7.org/man7/linux/man-pages/man5/proc.5.html) 以及相关手册页已经详尽阐述了系统的各项信息结构，但程序对这些文件的直接读取规模仍然十分惊人：

> While system information is broadly covered by [proc(5)](https://www.man7.org/man7/linux/man-pages/man5/proc.5.html) and related manual pages, the scale of direct file reads is surprising:

* **网络与系统负载 (Network & Uptime) ：** `ifconfig` 会检查 `/proc/net`；`ip` 命令会读取 `/proc/filesystems`；而 `uptime` 则会读取 `/proc/uptime` 和 `/proc/loadavg` (尽管 [`getloadavg(3)`](https://www.man7.org/linux/man-pages/man3/getloadavg.3.html) 似乎是直接调用了 [`sysinfo(2)`](https://man7.org/linux/man-pages/man2/sysinfo.2.html)) 。

> * **Network & Uptime:** `ifconfig` checks `/proc/net`, the `ip` command reads `/proc/filesystems`, and `uptime` reads `/proc/uptime` and `/proc/loadavg` (though [`getloadavg(3)`](https://www.man7.org/linux/man-pages/man3/getloadavg.3.html) appears to call [`sysinfo(2)`](https://man7.org/linux/man-pages/man2/sysinfo.2.html) directly).

### 语言运行时与标准工具集

> ### Runtimes and Standard Utilities

各类主流编程语言运行时与普通的可执行程序在冷启动时，都会频繁地审视 `/proc` 和 `/sys`：

> Language runtimes and ordinary binaries frequently inspect `/proc` and `/sys` upon starting:

* **Go：** 刚启动的 Go 程序会读取 `/proc/self/cgroup`、`/proc/self/mountinfo` 以及 `/sys/fs/cgroup` 中的 `cpu.max` 字段 (大概率是为了确定运行时的并发度限制) 。
* **Python：** Python 3.14.4 在执行任何用户代码之前，都会同时读取 `/proc/self/maps` 和 `/proc/sys/vm/overcommit_memory`。
* **Emacs：** GNU Emacs 31 会读取 `/proc/filesystems`、`/proc/self/cgroup` 以及各种关联的 cgroup 目录以定位 `cpu.max`。
* **Coreutils：** 令人惊讶的是，GNU Coreutils 中的基础命令 `mkdir` 和 `ls` 居然也都会读取 `/proc/filesystems`。
* **Rust：** 哪怕是一个最简单的 Rust "hello world" 二进制程序，在启动时都会读取 `/proc/self/maps`。执行 `cargo` 但不进行任何操作也会触发对 `/proc/self/cgroup`、`cpu.max` 和 `/proc/self/exe` 的读取，而空闲状态的 `rustc` 读取的文件甚至更多，包括 `/proc/sys/vm/overcommit_memory`。

> * **Go:** A newly starting Go program reads `/proc/self/cgroup`, `/proc/self/mountinfo`, and the `cpu.max` field in `/sys/fs/cgroup` (likely to determine concurrency limits).
> * **Python:** Python 3.14.4 reads both `/proc/self/maps` and `/proc/sys/vm/overcommit_memory` before executing user code.
> * **Emacs:** GNU Emacs 31 reads `/proc/filesystems`, `/proc/self/cgroup`, and various associated cgroups to locate `cpu.max`.
> * **Coreutils:** Surprisingly, GNU Coreutils `mkdir` and `ls` both read `/proc/filesystems`.
> * **Rust:** A Rust "hello world" binary reads `/proc/self/maps` on startup. Doing nothing with `cargo` triggers reads to `/proc/self/cgroup`, `cpu.max`, and `/proc/self/exe`, while an idle `rustc` reads even more, including `/proc/sys/vm/overcommit_memory`.

## 兼容性测试与潜在风险

> ## Testing and Compatibility

尽管部分程序在缺失 `/proc` 中这些内容的情况下仍能勉强运转，但进行全面彻底的测试仍然不可或缺。正如 systemd 文档中所指出的那样，`ProcSubset=pid` 是一项限制性极强的安全配置，绝不能想当然地认为它能够与任意业务代码无缝兼容。

> While some programs might function without these parts of `/proc`, thorough testing is essential. As the systemd documentation notes, `ProcSubset=pid` is a restrictive option that cannot be assumed to work gracefully with arbitrary code. 

退一步讲，即使代码在缺少这些虚拟文件条目时表面上能够“正常工作”，软件去查询 `/proc` 往往也有其充分且正当的理由。例如，如果无法获知内存过量使用 (Memory Overcommit) 这类系统关键指标，程序就不得不被迫猜测底层环境的行为模式——而这种盲目猜测往往极易出现偏差。

> Even if code technically "works" without these entries, software often consults `/proc` for valid reasons. Without visibility into metrics like memory overcommit, programs are forced to guess their behavior—guesses that may easily be wrong.

---

## 专题实战：使用审计子系统监控 /proc 与相关路径

> ## Sidebar: Using the audit system to watch `/proc` and other things

为了准确捕获这些访问动作，我使用了如下 audit 规则：

> To track these accesses, I used the following audit rules:

```text
# /proc
-a exit,always -F arch=b64 -F dir=/proc -F perm=r -F success=1 -F fsuid!=0 -F key=procaccess64
-a exit,always -F arch=b32 -F dir=/proc -F perm=r -F success=1 -F key=procaccess32

# cgroup stuff
-a exit,always -F arch=b64 -F dir=/sys/fs/cgroup -F perm=rw -F success=1 -F fsuid!=0 -F key=cgroupaccess64
```

为了有效控制日志输出量，审计规则中排除了 root 用户对 `/proc` 与 `/sys/fs/cgroup` 的访问记录——尤其是考虑到我们的服务器后台运行着大量密集的性能监控采集任务。同样地，由于预期访问量极低，针对 32 位系统的 cgroup 访问规则也一并予以略过。

> Root access to `/proc` and `/sys/fs/cgroup` was excluded to manage log volume—especially given heavy background metrics collection on our systems. 32-bit cgroup access was similarly omitted due to low expected volume.

由于内核目前并不原生支持直接针对特定 cgroup 的审计规则，如果想要单独审计某一个 systemd 服务，则需要采取其他变通方案。如果目标服务是在独立的非 root 用户或用户组下运行，我们可以把规则限制在指定的 UID 或 GID 上。此外，[`auditctl(8)`](https://www.man7.org/linux/man-pages/man8/auditctl.8.html) 工具还支持根据具体的可执行二进制路径、进程 ID (PID) 、父进程 ID (PPID) ，或者在适用情况下通过 SELinux 安全上下文属性来进行精细化过滤。

> Because cgroup-specific audit rules do not natively exist, auditing a single systemd service requires alternative approaches. If the service runs under a dedicated non-root user or group, rules can be restricted to that UID or GID. Additionally, [`auditctl(8)`](https://www.man7.org/linux/man-pages/man8/auditctl.8.html) allows filtering by specific executables, process IDs, parent process IDs, or SELinux attributes if applicable.
