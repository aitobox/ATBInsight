---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-02
hide:
- navigation
tags:
- Polkit
- systemd
- loginctl
- Linux管理
- 安全配置
title: 使用 Polkit 阻止用户运行 `loginctl enable-linger`
---
### 文章背景与核心概要
在默认情况下，systemd 允许任何用户为自己运行 `loginctl enable-linger` 命令（即启用常驻后台会话）。然而，在采用网络主目录或延迟挂载主目录（例如 NFS 文件服务器）的环境中，启用常驻会话可能会导致意外的行为以及损坏的 systemd 用户单元。本指南将介绍如何使用 **Polkit** 禁用普通用户自行管理常驻（linger）状态的权限。

通过了解 systemd 的 Polkit 策略，我们可以通过编写自定义的 `.rules` 文件来拦截 `org.freedesktop.login1.set-self-linger` 动作，从而在不影响 root 用户的前提下，彻底阻止普通用户在特定服务器环境中引发因主目录未及时挂载而导致的各类 systemd 运行故障。

---

## 使用 Polkit 阻止用户运行 `loginctl enable-linger`

> ## Using Polkit to Prevent Users from Running `loginctl enable-linger`

## 摘要

默认情况下，systemd 允许任何用户为自己运行 `loginctl enable-linger`。然而，在具有网络或延迟主目录（如 NFS 文件服务器）的环境中，常驻用户可能会导致意外行为和损坏的 systemd 用户单元。本指南介绍了如何使用 **Polkit** 禁用非 root 用户管理其自身常驻状态的能力。

> ## Summary
> By default, systemd allows any user to run `loginctl enable-linger` for themselves. However, in environments with networked or deferred home directories (such as NFS fileservers), lingering users can lead to unexpected behaviors and broken systemd user units. This guide explains how to use **Polkit** to disable the ability for non-root users to manage their own lingering status.

---

## 理解 Linger 的 Polkit 动作

针对 `loginctl` 等操作的标准 systemd 行为由位于 `/usr/share/polkit-1/actions/` 中的 Polkit 策略控制。具体来说，`org.freedesktop.login1.policy` 文件概述了相关的操作：

* `org.freedesktop.login1.set-self-linger` — 控制为自己启用或禁用常驻。
* `org.freedesktop.login1.set-user-linger` — 控制为其他用户启用或禁用常驻（通常需要管理员身份验证）。

*注意：即使你在命令行参数中显式传递了自己的用户名，`loginctl` 也会自动解析为 `set-self-linger`。不幸的是，`org.freedesktop.login1` 无法区分启用和禁用自身常驻；这两个操作共享完全相同的权限。*

> ## Understanding Polkit Actions for Linger
> 
> Standard systemd behavior for actions like `loginctl` is governed by Polkit policies located in `/usr/share/polkit-1/actions/`. Specifically, the file `org.freedesktop.login1.policy` outlines the relevant actions:
> 
> * `org.freedesktop.login1.set-self-linger` — Controls enabling or disabling lingering for yourself.
> * `org.freedesktop.login1.set-user-linger` — Controls enabling or disabling lingering for other users (which typically requires administrator authentication).
> 
> *Note: `loginctl` automatically resolves to `set-self-linger` even if you pass your own username explicitly as a command-line argument. Unfortunately, `org.freedesktop.login1` does not differentiate between enabling and disabling self-linger; both actions share the exact same permissions.*

---

## 通过 Polkit 规则禁用自身常驻（Self-Linger）

要覆盖默认行为并阻止用户启用常驻，您可以创建一个自定义的 Polkit 规则。

在 `/etc/polkit-1/rules.d/` 目录下创建一个 `.rules` 文件，并写入以下配置：

```javascript
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.login1.set-self-linger") {
        return polkit.Result.NO;
    }
});
```

> ## Disabling Self-Linger via Polkit Rules
> 
> To override the default behavior and block users from enabling linger, you can create a custom Polkit rule. 
> 
> Create a `.rules` file inside `/etc/polkit-1/rules.d/` with the following configuration:
> 
> ```javascript
> polkit.addRule(function(action, subject) {
>     if (action.id == "org.freedesktop.login1.set-self-linger") {
>         return polkit.Result.NO;
>     }
});
> ```

### 预期结果：
* 无条件返回 `polkit.Result.NO` 将拒绝所有非 root 用户使用此操作的请求。
* 尝试运行该命令的用户将收到简短的拒绝消息：
  > `Could not enable linger: Access denied` *（请注意，即使你尝试运行 `disable-linger`，loginctl 也会打印 "enable"）。*
* **Root 用户（UID 0）：** Root 用户完全绕过此限制。但是，如果你切换 (`su`) 到 root 并运行 `loginctl enable-linger`，它会为你的原始登录会话启用常驻，而不是字面上的 `root` 账户，这反映了 systemd 跟踪用户上下文的方式。

> ### What to Expect:
> * Unconditionally returning `polkit.Result.NO` rejects all non-root requests to use this action.
> * Users attempting to run the command will receive a terse rejection message: 
>   > `Could not enable linger: Access denied` *(note that loginctl prints "enable" even if you attempted to run `disable-linger`)*.
> * **Root Users (UID 0):** Root users bypass this restriction entirely. However, if you `su` to root and run `loginctl enable-linger`, it enables lingering for your original login session rather than the literal `root` account, reflecting how systemd tracks user context.

---

## 侧边栏：在初始无法访问主目录的环境中使用“Linger”的危险性

在系统早期启动期间未立即挂载主目录的环境中（例如 NFS 挂载），启用“linger”状态会埋下一个隐蔽的陷阱：

1. **过早启动：** Systemd 在系统早期启动期间为常驻用户启动用户管理器。
2. **缺少配置：** 由于此时主目录尚未挂载，新启动的用户管理器会漏掉用户定义的单元文件（如 `$HOME/.config/systemd/user/default.target.wants`）。
3. **挂载时忽略单元：** 一旦主目录最终挂载并且用户登录，用户管理器*已经处于运行状态*，并且无法注意到新可用的单元。

### 修复卡住的环境
要强制一切正确初始化，你必须通过终止用户会话从头重新启动用户管理器：

```bash
loginctl terminate-user ""
```
*（空的双引号作为安全措施是必需的，用于明确指定你当前的登录会话）。*

> ## Sidebar: The Dangers of 'Linger' with Initially Inaccessible Home Directories
> 
> In environments where home directories are not mounted immediately during early system boot (such as NFS mounts), enabling "linger" status creates a subtle trap:
> 
> 1. **Premature Startup:** Systemd launches user managers for lingering users during early system boot. 
> 2. **Missing Configuration:** Because the home directory isn't mounted yet, the newly started user manager misses user-defined unit files (like `$HOME/.config/systemd/user/default.target.wants`).
> 3. **Ignored Units on Mount:** Once the home directory eventually mounts and the user logs in, the user manager is *already running* and fails to notice newly available units.
> 
> ### Fixing Stuck Environments
> To force everything to initialize correctly, you must restart the user manager from scratch by terminating the user session:
> 
> ```bash
> loginctl terminate-user ""
> ```
> *(The empty double quotes are required as a safety measure to explicitly target your current login session).*