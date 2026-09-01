---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-02
hide:
- navigation
tags:
- Linux
- SSH
- PAM
- 安全配置
- 系统管理
title: 使用 PAM 阻止 SSH 登录（至少在 Linux 上）
---
### 文章背景与核心概要
在 Linux 系统管理中，管理员经常需要根据 OpenSSH 的 `sshd_config` 原生不支持的条件（例如用户的登录 Shell）来限制或阻止 SSH 登录。传统的做法可能会让人联想到使用 PAM 的 `auth`（认证）堆栈，但由于 OpenSSH 的公钥认证会完全绕过 PAM，这种方法在公钥登录时会失效。

本文深入探讨了如何利用 PAM 的 `account`（账户）堆栈来实现精准的访问控制。通过巧妙组合 `pam_succeed_if`、`pam_echo`（或 `pam_exec`）以及 `pam_deny` 等模块，管理员不仅能够根据自定义条件有效拦截未经授权的访问，还能向客户端输出定制化的拒绝原因说明。

---

## The Limitations of the PAM `auth` Stack
## PAM `auth` 堆栈的局限性

Suppose you need to block logins to a server based on criteria such as the user's login shell, as discussed in [this entry on Systemd User Services and Shells](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdUserServicesAndShell). Initially, one might assume this can be handled in either the `session` or `authentication` (`auth`) PAM stacks. However, that approach only tells half the story.

> 假设你需要根据用户的登录 Shell 等条件来阻止用户登录服务器，正如[关于 Systemd 用户服务与 Shell 的这篇博文](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdUserServicesAndShell)所讨论的那样。起初，人们可能会认为这可以在 `session` 或 `authentication` (`auth`) PAM 堆栈中处理。然而，这种方法只说对了问题的一部分。

The primary issue with using the PAM `auth` stack for SSH restrictions is that OpenSSH performs public key authentication *outside* of PAM. If a connection authenticates via public keys, `sshd` never invokes the PAM `auth` stack, rendering any `auth`-based block ineffective (a limitation that also affects [certain authentication combinations](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/OpenSSHAuthConfigLimits)). 

> 使用 PAM `auth` 堆栈进行 SSH 限制的主要问题在于，OpenSSH 在 PAM 的*外部*执行公钥认证。如果连接通过公钥进行认证，`sshd` 绝不会调用 PAM `auth` 堆栈，这导致任何基于 `auth` 的阻止措施都形同虚设（这一局限性同样会影响[某些认证组合](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/OpenSSHAuthConfigLimits)）。

The correct alternative is the **`account`** PAM stack, which is explicitly documented in [`pam.conf(5)`](https://www.man7.org/linux/man-pages/man5/pam.d.5.html) for this exact type of access control.

> 正确的替代方案是 **`account`** PAM 堆栈，[`pam.conf(5)`](https://www.man7.org/linux/man-pages/man5/pam.d.5.html) 中明确记录了该堆栈正是用于此类访问控制。

---

## Providing Feedback with `pam_echo` and `pam_exec`
## 使用 `pam_echo` 和 `pam_exec` 提供反馈

To notify users why their login was blocked, you need a mechanism that works outside of `pam_motd` (which only functions in the `session` stack). 

> 为了通知用户其登录被阻止的原因，你需要一种在 `pam_motd` 之外起作用的机制（`pam_motd` 仅在 `session` 堆栈中生效）。

### 1. Static Messages via `pam_echo`
### 1. 通过 `pam_echo` 提供静态消息

The [`pam_echo`](https://www.man7.org/linux/man-pages/man8/pam_echo.8.html) module prints messages across all PAM modes by reading from a file, supporting basic dynamic variable expansion.

> [`pam_echo`](https://www.man7.org/linux/man-pages/man8/pam_echo.8.html) 模块通过读取文件在所有 PAM 模式下打印消息，并支持基本的动态变量扩展。

### 2. Dynamic Messages via `pam_exec`
### 2. 通过 `pam_exec` 提供动态消息

If you require a dynamic message—such as tailoring output based on a user's specific shell—you can use [`pam_exec`](https://www.man7.org/linux/man-pages/man8/pam_exec.8.html) with its `stdout` option. This executes a script whose output is passed back through `sshd` to the user's SSH client. 
* While `pam_exec` runs in a minimal environment, it does provide `$PAM_USER`, allowing you to query `/etc/passwd` or construct a custom message.

> 如果你需要动态消息——例如根据用户的特定 Shell 量身定制输出——你可以将 [`pam_exec`](https://www.man7.org/linux/man-pages/man8/pam_exec.8.html) 与其 `stdout` 选项配合使用。这将执行一个脚本，其输出将通过 `sshd` 传回给用户的 SSH 客户端。
> * 尽管 `pam_exec` 在最小化环境中运行，但它确实提供了 `$PAM_USER`，允许你查询 `/etc/passwd` 或构建自定义消息。

---

## Example PAM Configuration
## PAM 配置示例

Using the conventions established in previous configurations, a working PAM stanza looks like this:

> 使用先前配置中确定的规范，一个可用的 PAM 代码段如下所示：

```text
account [success=ignore default=2] pam_succeed_if.so shell =~ /admin/shells/*
account optional  pam_echo.so file=/admin/access-denied.txt
# or
#account optional pam_exec.so stdout /admin/access-denied.sh
account requisite pam_deny.so
```

### Key Configuration Notes:
### 关键配置说明：

* **`requisite` Control Value:** We use `requisite` instead of the more common `required` so that the account PAM stack fails immediately. (For details, see [understanding the effect of PAM module results](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PAMModuleResultsEffects), keeping in mind [potential issues if used as a substack](https://utcc.utoronto.ca/~cks/space/blog/linux/PAMStackingAndStopping).)
* **Flexibility:** The [`pam_succeed_if`](https://www.man7.org/linux/man-pages/man8/pam_succeed_if.8.html) module supports a broader and more flexible set of data fields and comparisons than `sshd_config`'s native `Match` statements.
* **Scope:** If you want these restrictions to apply **only** to SSH logins rather than system-wide access, place these rules in `/etc/pam.d/sshd` instead of a global configuration file.

> * **`requisite` 控制值：** 我们使用 `requisite` 而不是更常见的 `required`，以便账户 PAM 堆栈立即失败。（有关详细信息，请参阅[理解 PAM 模块结果的影响](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PAMModuleResultsEffects)，同时请记住[如果用作子堆栈时的潜在问题](https://utcc.utoronto.ca/~cks/space/blog/linux/PAMStackingAndStopping)。）
> * **灵活性：** 相比 `sshd_config` 原生的 `Match` 语句，[`pam_succeed_if`](https://www.man7.org/linux/man-pages/man8/pam_succeed_if.8.html) 模块支持更广泛、更灵活的数据字段和比较运算。
> * **作用域：** 如果你希望这些限制**仅**适用于 SSH 登录，而不是整个系统的访问，请将这些规则放在 `/etc/pam.d/sshd` 中，而不是全局配置文件中。