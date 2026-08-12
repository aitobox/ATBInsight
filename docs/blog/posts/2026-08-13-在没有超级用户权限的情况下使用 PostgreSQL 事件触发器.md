---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- PostgreSQL
- 数据库安全
- 扩展开发
- Supabase
- 权限管理
title: 在没有超级用户权限的情况下使用 PostgreSQL 事件触发器
---
### 文章背景与核心概要
PostgreSQL 中的事件触发器（Event Triggers）是实现数据库自动化的强大工具，但传统上它们仅限于超级用户（superuser）使用。在托管云环境中，用户通常无法获得这种高权限。本文探讨了 `supautils` 扩展如何利用 PostgreSQL 钩子（hooks），使普通用户能够安全地创建事件触发器，同时有效防止潜在的特权升级攻击。

通过引入“特权角色（privileged role）”作为代理，并结合 `ProcessUtility_hook` 和 `fmgr_hook` 拦截机制，`supautils` 成功在权限控制与灵活性之间取得了平衡，允许开发者在无需完整超级用户权限的情况下安全地使用事件触发器。

---

## 特权角色
The core of `supautils` is the "privileged role"—a proxy that provides a safe subset of superuser capabilities to regular users. 

> `supautils` 的核心是“特权角色”（privileged role）——它是一个代理，能够向普通用户提供超级用户功能的的安全子集。

When a user with this role executes `CREATE EVENT TRIGGER`, the `ProcessUtility_hook` intercepts the statement. The extension temporarily elevates the session to superuser to perform the creation in the PostgreSQL core, then immediately downgrades the session and assigns ownership of the trigger to the original user [^1].

> 当具有该角色的用户执行 `CREATE EVENT TRIGGER` 时，`ProcessUtility_hook` 会拦截该语句。该扩展会临时将当前会话提升为超级用户，以便在 PostgreSQL 内核中完成创建，随后立即降低会话权限并将触发器的所有权分配给原始用户 [^1]。

## 特权升级问题
The privilege escalation problem
Simply allowing users to create event triggers is dangerous. Because event triggers execute with the privileges of the user performing the DDL command, a malicious user could create a trigger that elevates their own status:

> 简单地允许用户创建事件触发器是危险的。由于事件触发器是以执行 DDL 命令的用户的权限来运行的，恶意用户可能会创建一个提升自身权限的触发器：

```sql
create or replace function become_super()
    returns event_trigger
    language plpgsql as
$$
begin
    alter role malicious SUPERUSER;
end;
$$;

create event trigger bad_event_trigger on ddl_command_end
execute procedure become_super();
```
If a superuser performs any DDL command, this trigger would fire with superuser privileges, granting the malicious user permanent superuser access.

> 如果超级用户执行任何 DDL 命令，该触发器将以超级用户权限触发，从而授予恶意用户永久的超级用户访问权限。

## 跳过事件触发器
Skipping Event Triggers
To prevent this, `supautils` uses the `fmgr_hook` to intercept function execution. When a superuser or a "reserved role" (used by services like `pgbouncer`) triggers an event, the extension intercepts the event trigger function and replaces it with a "noop" (using the `version()` function). This ensures that user-defined triggers never execute when a privileged account performs DDL operations [^3].

> 为了防止这种情况，`supautils` 使用 `fmgr_hook` 来拦截函数执行。当超级用户或“保留角色”（如 `pgbouncer` 等服务使用的角色）触发事件时，该扩展会拦截事件触发器函数，并将其替换为一个“空操作（noop）”（通过使用 `version()` 函数）。这确保了当特权账户执行 DDL 操作时，用户定义的触发器永远不会执行 [^3]。

## 实战中的用户事件触发器
User Event Triggers in Action
With these safeguards, users can safely create event triggers without needing full superuser access:

> 有了这些安全保障，用户无需完整的超级用户权限即可安全地创建事件触发器：

```sql
-- Use the privileged role
set role postgres;

-- Create the event trigger
create function show_current_user()
returns event_trigger as $$
begin
  raise notice 'the event trigger is executed for %', current_user;
end;
$$ language plpgsql;

create event trigger myevtrig on ddl_command_end
execute procedure show_current_user();

-- Test the trigger
create table foo();
-- NOTICE:  the event trigger is executed for postgres
```

## Postgres 内核的未来
Future in Postgres Core
The team is actively working to bring this functionality into the PostgreSQL core, with patches currently under discussion in the community. Note that any implementation in the core will likely be more restrictive than the current `supautils` version.

> 该团队正积极致力于将此功能引入 PostgreSQL 内核中，相关补丁目前正在社区中讨论。请注意，内核中的任何实现可能都会比当前的 `supautils` 版本更加严格。

## 立即体验
Try it out
User Event Triggers are available for new projects on the Supabase platform. You can also find the source code at the [supautils GitHub repository](https://github.com/supabase/supautils/).

> Supabase 平台上的新项目现已支持用户事件触发器。您还可以在 [supautils GitHub 仓库](https://github.com/supabase/supautils/) 中找到源代码。

---

### 脚注
Footnotes
[^1]: This allows the event trigger to be altered or dropped by end users.
> [^1]: 这允许终端用户修改或删除该事件触发器。

[^2]: This is not true if you mark the event trigger function as `security definer`, then it will run with the privileges of the function owner. However, this is not standard practice, as triggers usually aim to preserve the context of the current user.
> [^2]: 如果将事件触发器函数标记为 `security definer`，则情况并非如此，此时它将以函数所有者的权限运行。然而，这并不是标准做法，因为触发器的通常目的是保留当前用户的上下文。

[^3]: These are configurable. You can read more about reserved roles [here](https://supabase.com/blog/roles-postgres-hooks).
> [^3]: 这些都是可配置的。您可以点击[此处](https://supabase.com/blog/roles-postgres-hooks)阅读更多关于保留角色的信息。