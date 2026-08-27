---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-28
hide:
- navigation
tags:
- Linux
- Systemd
- PAM
- 安全
- 系统管理
title: Systemd 用户服务单元与特殊 Shell 带来的意外挑战
---
### 文章背景与核心概要
在多服务器 Linux 环境中，管理员通常会通过在 `/etc/passwd` 中设置限制性 Shell（如仅打印提示信息并退出的脚本）来禁止用户直接登录特定节点（如文件服务器或计算节点）。然而，Systemd 的用户服务管理机制会绕过这一限制：即使 Shell 立即退出，Systemd 仍会在用户登录时自动启动其配置的后台服务单元。

本文探讨了这一安全隐患的成因，即 Systemd 用户管理器在 Shell 启动前便已运行，导致用户配置的后台任务在受限节点上意外执行。文章进一步提供了基于 Systemd v258+ 的 PAM 配置方案以及通过 PAM 拦截登录的替代策略，帮助管理员有效规避此类非授权负载执行风险。

---

## 问题：通过 Systemd 绕过特殊 Shell

假设你管理着一个多服务器 Linux 环境，用户可以登录通用登录服务器，但被禁止直接 SSH 到文件服务器或 SLURM 作业提交节点。传统的做法是修改 `/etc/passwd` 中的用户 Shell 为一个自定义脚本，用以告知用户限制信息并退出。

当用户配置了个人 Systemd 服务单元（通常存放在 `$HOME/.config/systemd/user` 并设置为 `WantedBy=default.target`）时，问题便出现了：

1. **自动启动：** 当用户尝试 SSH 到受限节点时，系统会在评估其 Shell 之前就启动 Systemd 用户管理器。
2. **执行：** 该管理器会自动启动用户的服务单元，这意味着用户的后台服务会在他们本不应访问的机器上运行。
3. **持久化：** 如果用户通过 `loginctl enable-linger` 启用了“用户驻留（lingering）”，他们的用户管理器和服务将持续运行，而不会在标准的十秒 `UserStopDelaySec` 窗口后终止。

虽然 `logind.conf` 中存在 `KillUserProcesses` 选项，但它仅针对 session `.scope` 单元内的进程，完全忽略了隔离的用户服务单元。

> The flaw arises when users configure per-user systemd service units (typically placed in `$HOME/.config/systemd/user` and set to start via `WantedBy=default.target`). 
>
> 1. **Automatic Startup:** When a user attempts to SSH into a restricted node, the system spawns a systemd user manager *before* evaluating their shell. 
> 2. **Execution:** This manager automatically starts their user units, meaning their background services run on a machine they aren't supposed to access.
> 3. **Persistence:** If the user has enabled "user lingering" via `loginctl enable-linger`, their user manager and services become perpetual rather than timing out after the standard ten-second `UserStopDelaySec` window.
>
> While `KillUserProcesses` exists in `logind.conf`, it only targets processes within session `.scope` units, ignoring isolated user service units entirely.

---

## 缓解策略

### 1. 现代 PAM 方法（Systemd v258+）
在 Systemd v258 及更高版本中，你可以通过配置 `pam_systemd` 并使用 `class=user-light` 参数，防止 Systemd 为受限账户启动用户管理器。

对于 Ubuntu 26.04 及兼容发行版，你可以在 PAM 会话堆栈中添加以下内容：

```text
session [success=ignore default=2] pam_succeed_if.so shell =~ /admin/shells/*
session optional  pam_systemd.so class=user-light
session [success=1 default=ignore] pam_succeed_if.so shell =~ /admin/shells/*
session optional  pam_systemd.so
```

* **优点：** 用户在管理 Shell 运行的短暂时间内仍会被置于正确的 Systemd 单元层级（如 `user-NNN.slice` 和 `session-NNN.scope`），从而确保资源限制脚本正常工作。

> In systemd v258 and later, you can prevent systemd from spinning up a user manager for restricted accounts by configuring `pam_systemd` with `class=user-light`. 
>
> For Ubuntu 26.04 and compatible distributions, you can add the following to your PAM session stack:
>
> ```text
> session [success=ignore default=2] pam_succeed_if.so shell =~ /admin/shells/*
> session optional  pam_systemd.so class=user-light
> session [success=1 default=ignore] pam_succeed_if.so shell =~ /admin/shells/*
> session optional  pam_systemd.so
> ```
>
> * **Advantage:** Users are still placed into the proper systemd unit hierarchy (such as `user-NNN.slice` and `session-NNN.scope`) for the brief duration of the administrative shell, keeping resource-limiting scripts happy.

---

### 2. 侧边栏：通过 PAM 拒绝登录
或者，你也可以在 PAM 会话堆栈中使用 `pam_succeed_if.so` 配合 `pam_deny.so` 完全阻止登录，同时使用 `pam_motd.so` 显示拒绝访问的消息：

```text
session [success=ignore default=3] pam_succeed_if.so shell =~ /admin/shells/*
session optional pam_motd.so motd=/admin/access-denied.txt
session required pam_deny.so
```

*（注意：此代码块必须放置在 `pam_systemd.so` 之前。）*

#### 缺点：
* 由于会话在打开后被立即终止，可能会在 `sshd-session` 中触发轻微的日志错误。
* 为多个管理 Shell 维护唯一的消息需要在 PAM 配置中编写重复的块。

> Alternatively, you can block logins entirely inside the PAM session stack using `pam_succeed_if.so` paired with `pam_deny.so`, while using `pam_motd.so` to display an access-denied message:
>
> ```text
> session [success=ignore default=3] pam_succeed_if.so shell =~ /admin/shells/*
> session optional pam_motd.so motd=/admin/access-denied.txt
> session required pam_deny.so
> ```
>
> *(Note: This block must be placed before `pam_systemd.so`.)*
>
> #### Drawbacks:
> * It can trigger minor logging errors in `sshd-session` because the session is abruptly terminated post-opening.
> * Maintaining unique messages for multiple administrative shells requires repetitive blocks in the PAM configuration.