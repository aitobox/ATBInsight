---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-20
hide:
  - navigation
tags:
  - Fedora
  - Linux内核
  - DKMS
  - ZFS
title: "Fedora 44 下 DKMS 与内核 Initramfs 镜像重建的性能陷阱与解决"
---

# Fedora 44 下 DKMS 与内核 Initramfs 镜像重建的性能陷阱与解决

> # An Issue with DKMS and Kernel Initramfs Images in Fedora 44

### 文章背景与核心概要

在 Linux 生态中，DKMS (Dynamic Kernel Module Support) 是第三方内核模块（如 ZFS 或显卡驱动）伴随内核升级自动重新编译的利器，而 Initramfs 则承载着系统引导时早期的必要驱动。然而在 Fedora 44 发行版中，默认的 DKMS 触发机制存在一项隐蔽的性能陷阱：只要执行模块卸载或安装，框架便会无差别地针对系统中“所有已安装的内核”全量重新生成 Initramfs 引导镜像。对于长期保留多个备份内核的开发者和工作站而言，一次常规的小版本更新可能会演变成长达 20 多分钟的漫长等待。本文深入剖析了这一机制背后的配置成因，并提供了一行配置覆盖的极简优化方案，帮助读者轻松解除不必要的重建负担，显著提升系统维护效率。

---

## 内容摘要

> ## Summary

在 Fedora 44 系统上通过动态内核模块支持 (Dynamic Kernel Module Support, DKMS) 更新 ZFS 文件系统 (ZFS) 时，整个更新流程变得异常迟缓，耗时竟长达 20 分钟以上。深入排查后发现，Fedora 的 DKMS 默认配置中引入了一个事务后钩子 (post-transaction hook)；只要触发 `dkms remove` 或 `dkms install` 命令，即便该模块仅面向某一个特定内核版本，系统也会强行调用 `dracut --regenerate-all --force`，为机器上安装的“每一个内核”统统重新生成一遍初始化内存盘 (Initramfs) 镜像。幸运的是，我们只需在 `/etc/dkms/framework.conf.d/` 目录下添加自定义配置并覆盖其 `post_transaction` 选项，即可轻松绕过这一繁重冗余的重建机制。

> When updating ZFS via DKMS on Fedora 44, the update process became frustratingly slow—taking upwards of twenty minutes. By investigating the issue, it was discovered that Fedora's DKMS configuration uses a post-transaction hook to regenerate *all* initramfs images across every installed kernel (`dracut --regenerate-all --force`) whenever `dkms remove` or `dkms install` is executed, even if the module is only being targeted at a single kernel version. Fortunately, this can be bypassed by overriding the `post_transaction` setting in `/etc/dkms/framework.conf.d/`.

---

## 根本成因：过于激进的 Initramfs 全量重建

> ## The Root Cause: Overzealous Initramfs Regeneration

在日常的桌面工作站环境中，作者维护着一套略显复杂的内核与 ZFS 更新流程，其中便利用了通过 [DKMS](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) 管理的 ZFS 开发分支版本。在正常预期下，系统通常只需为最近使用的两个内核编译新模块。然而，每次升级 ZFS 的 DKMS RPM 软件包时，底层都会先后执行旧模块的卸载以及新模块的安装操作，进而导致整个更新流程耗时漫长、令人苦不堪言。

> The author runs a convoluted kernel and ZFS update process on desktop systems, utilizing the development version of ZFS managed through [DKMS](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support). Normally, modules are only built for the two most recent kernels. However, updating the ZFS DKMS RPM involves both removing old modules and installing new ones, which led to agonizingly slow update times.

经过在 [Fediverse](https://mastodon.social/@cks/117445698531371721) 上的交流探讨与 [深入排查](https://mastodon.social/@cks/117445845905372687)，这一性能瓶颈的症结所在终于被彻底查明：

> Upon investigating via the [Fediverse](https://mastodon.social/@cks/117445698531371721) and [further debugging](https://mastodon.social/@cks/117445845905372687), the culprit was uncovered:

> 💬 [译文引用]:
> “在我的内核更新流程中，时间究竟都去哪儿了？答案终于水落石出：执行 `dkms remove` 会为系统中所有已安装的内核重新构建全部 Initramfs 镜像；哪怕你要卸载的模块在某些内核中根本不存在，甚至哪怕你显式加上了 `dkms remove ... -k ...` 明确限制仅为单一内核卸载，它也依然会毫不留情地全量重建一遍。
> 
> 这着实让人十分无奈。我完全不希望系统未经许可就意外重建一堆不相干的 Initramfs 镜像；更何况在我的机器上足足保留了 6 个不同版本的内核，这样一折腾下来耗费的时间可想而知。”

> 💬 [原文引用 / Original Quote]:
> The answer to where the time goes [in my kernel update process] is that 'dkms remove' rebuilds all initramfs images for all installed kernels, even if the module you're removing doesn't exist for those kernels and even if you are running 'dkms remove ... -k ...' to only remove the module for one kernel.
> 
> This is my unhappy face. I do not want random initramfs's to be rebuilt by surprise, and it also takes rather a while when you have six kernels, like I do.

*(注：`dkms install` 安装命令在执行时同样存在完全一致的激进行为)*。

> *(Note: `dkms install` exhibits the exact same behavior).*

### 为什么会发生这种情况？

> ### Why Does This Happen?

进一步深入审查 Fedora 44 的 DKMS 默认配置文件，终于找到了导致该问题的根源项。在 `/etc/dkms/framework.conf` 中，Fedora 预置了如下配置：

> Digging into Fedora 44's DKMS configuration revealed the setting responsible. Inside `/etc/dkms/framework.conf`, Fedora defines:

```ini
post_transaction="dracut --regenerate-all --force"
```

查阅 [DKMS 手册页](https://man.archlinux.org/man/dkms.8) 与 [dracut(8) 手册页](https://www.man7.org/linux/man-pages/man8/dracut.8.html) 可知，该配置指令会在系统调用诸如 `dkms install` 与 `dkms remove` 等命令后自动触发执行。它会强制将系统中**所有**已安装内核所对应的**全部** Initramfs 镜像，按顺序逐一进行串行化全量重建。

> According to [the DKMS manual page](https://man.archlinux.org/man/dkms.8) and the [dracut(8) manual page](https://www.man7.org/linux/man-pages/man8/dracut.8.html), this command runs automatically after commands like `dkms install` and `dkms remove`. It forces **all** initramfs images for **all** installed kernels to be serially regenerated, one by one.

因此，在升级 `zfs-dkms` 模块时，DKMS 会先执行旧版本的模块卸载、紧接着再执行新版本的编译安装。对于一台安装了 6 个内核的工作站而言，这相当于在一次更新中被动连续执行了整整两次 `dracut --regenerate-all` 全量生成命令，直接把一次原本轻松普通的日常维护，变成了长达 20 多分钟的漫长煎熬。

> When updating `zfs-dkms`, DKMS performs a removal of old modules followed by an installation of new ones. With six kernels installed on a work desktop, running `dracut --regenerate-all` twice turned a routine update into a 20+ minute ordeal.

---

## Fedora 如何将 DKMS 钩入内核安装流程

> ## How Fedora Hooks DKMS into Kernel Installs

与此相对的是，通过 DNF 包管理器 (DNF) 进行常规的内核安装升级时，其表现却十分正常规整。Fedora 是通过 `/usr/lib/kernel/install.d/40-dkms.install` 脚本将 DKMS 挂钩到内核安装流程中的，该脚本会调用一个官方文档中并未公开说明的 DKMS 子命令：

> Conversely, standard DNF kernel installations behave normally. Fedora hooks DKMS into kernel installs via `/usr/lib/kernel/install.d/40-dkms.install`, which executes an undocumented DKMS subcommand:

```bash
dkms kernel_postinst --kernelver "$KERNEL_VERSION"
```

这一命令会触发一种特殊形式的 `dkms autoinstall` 操作。但在 `dkms` 内部的 Shell 脚本逻辑中，专门对该子命令做了特殊处理，跳过了 `post_transaction` 钩子的执行。正因如此，当用户通过 DNF 安装新内核时，系统只会精准地针对当前这个新内核编译模块并生成对应的 Initramfs，一切都完全符合正常预期。

> This triggers a form of `dkms autoinstall`, but the internal `dkms` shell script specifically skips running the `post_transaction` command for this subcommand. Therefore, installing a new kernel via DNF only builds the module and creates the initramfs for that specific new kernel, as expected.

---

## 解决方案

> ## The Fix

由于这项机制是 Fedora 维护人员显式打入 [Fedora 的 dkms.spec 构建规范](https://src.fedoraproject.org/rpms/dkms/blob/rawhide/f/dkms.spec#_58) 中的补丁行为（最初引入于 [3.2.0 版本的提交记录](https://src.fedoraproject.org/rpms/dkms/c/11bcc820ca36ce51254d7015bdb18405d5babf3c?branch=rawhide)），因此仅仅去官方提交常规的 Bug 报告，大概率很难促使其做出改变。

> Because Fedora explicitly patches this behavior into [the Fedora dkms.spec](https://src.fedoraproject.org/rpms/dkms/blob/rawhide/f/dkms.spec#_58) (added in [the 3.2.0 commit](https://src.fedoraproject.org/rpms/dkms/c/11bcc820ca36ce51254d7015bdb18405d5babf3c?branch=rawhide)), filing a traditional bug report is unlikely to yield changes.

不过，如果读者所使用的这类特定内核模块并不需要在系统早期的内核 Initramfs 镜像中加载常驻，解决办法就非常简单优雅：我们只需在 `/etc/dkms/framework.conf.d/` 目录下创建一个自定义的覆盖配置文件，使默认配置中的 `post_transaction` 动作失效即可。

> However, since these particular kernel modules do not need to reside in the kernel initramfs image, the solution is simple: create an override file in `/etc/dkms/framework.conf.d/` to neutralize the `post_transaction` action.

将 `post_transaction` 的值配置为空或者指定为 `/bin/true`，即可阻止 DKMS 在每次执行模块卸载和安装时盲目重建所有 Initramfs 镜像，从而立竿见影地让 `dkms remove` 等命令重新恢复清爽快速的执行体验。

> Setting `post_transaction` to null or `/bin/true` will prevent DKMS from blindly touching your initramfs images on module removal and installation, instantly restoring fast execution times to commands like `dkms remove`.
