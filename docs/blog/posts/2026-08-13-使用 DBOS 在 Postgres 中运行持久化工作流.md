---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- DBOS
- Postgres
- Supabase
- 工作流引擎
- 持久化
title: 使用 DBOS 在 Postgres 中运行持久化工作流
---
### 文章背景与核心概要
本文介绍了由 Postgres 发明者、图灵奖得主 Michael Stonebraker 携手斯坦福大学和麻省理工学院研究人员共同开发的轻量级、高性能持久化工作流引擎 —— **DBOS**。该引擎直接构建于 Postgres 之上，允许开发者通过 Python 或 TypeScript 中的简单装饰器，将各个工作流步骤的状态保存到数据库中，就像电子游戏里的“存档点”一样。

凭借近期与 **Supabase** 的深度集成，开发者可以极其轻松地利用现有的 Postgres 集群运行强健的工作流。这种设计彻底摆脱了外部协调器的依赖，带来了高达 **25 倍的性能提升**，并具备内置的幂等性、事务保证，以及诸如备份和图形界面等熟悉的 Postgres 原生工具支持。

---

## 什么是持久化工作流引擎？
> ## What's a Durable Workflow Engine?

让我们来看一个常见的电商场景，其中订单需要经过多个步骤：
> Let's look at a common e-commerce scenario where an order goes through multiple steps:

1. **扣除信用卡金额 (Charge Credit Card)**
2. **检查库存 (Check Inventory)**
3. **发货 (Ship Order)**

由于各种边缘情况的存在，编写一个能够应对意外的强健程序可能会异常困难：
> Writing a robust program for this can be surprisingly difficult due to edge cases:
* **延迟：** 如果你执行到第 2 步（“检查库存”）发现商品缺货，你可能需要等待 24 小时以等待新库存到货。此时该步骤需要“休眠”一天。
> * **Delays:** If you reach step 2 ("Check Inventory") and find the item is out of stock, you may need to wait 24 hours for new inventory to arrive. The step needs to "sleep" for a day.
* **崩溃：** 如果程序在第 3 步（“发货”）期间崩溃，且没有记录库存已发货的状态，你可能会不小心重复发送相同的订单。
> * **Crashes:** If your program crashes during step 3 ("Ship Order") without recording that the inventory was shipped, you might accidentally send the same order twice.

**持久化工作流引擎 (Durable Workflow Engine)** 能够完美解决这些问题。尽管目前存在诸如 [Oban](https://oban.pro/)、[Trigger.dev](https://trigger.dev/)、[Inngest](https://www.inngest.com/)、[Windmill](https://www.windmill.dev)、[Temporal](https://temporal.io/) 以及 [AWS Step Functions](https://aws.amazon.com/step-functions/) 等解决方案，但 DBOS 通过直接将状态存储在你自己的 Postgres 数据库中，提供了一种独特且深度集成的方案。
> A **Durable Workflow Engine** solves these problems. While solutions like [Oban](https://oban.pro/), [Trigger.dev](https://trigger.dev/), [Inngest](https://www.inngest.com/), [Windmill](https://www.windmill.dev), [Temporal](https://temporal.io/), and [AWS Step Functions](https://aws.amazon.com/step-functions/) exist, DBOS offers a uniquely integrated approach by storing state directly inside your own Postgres database.

---

## 什么是 DBOS？
> ## What is DBOS?

[DBOS](https://www.dbos.dev/) 是一个平台，允许你使用 [Python](https://docs.dbos.dev/python/programming-guide) 或 [TypeScript](https://docs.dbos.dev/typescript/programming-guide) 将应用逻辑编写为无服务器函数（类似于 Supabase Edge Functions）。
> [DBOS](https://www.dbos.dev/) is a platform where you can write application logic as serverless functions (similar to Supabase Edge Functions) in either [Python](https://docs.dbos.dev/python/programming-guide) or [TypeScript](https://docs.dbos.dev/typescript/programming-guide).

### 使用装饰器创建工作流
> ### Creating Workflows with Decorators

与标准的 Supabase Edge Functions 不同，DBOS 允许你通过 `DBOS.step()` 和 `DBOS.workflow()` 为函数添加装饰器。
> Unlike standard Supabase Edge Functions, DBOS allows you to add decorators to your functions using `DBOS.step()` and `DBOS.workflow()`. 

当你这样做时，DBOS 会自动将每个步骤的状态存储在 Postgres 中。如果你是个游戏玩家，可以把它想象成代码的 **“存档点”**：如果某个函数失败了，一个新的函数可以启动并从上一个检查点断点续传。
> When you do this, DBOS automatically stores the state of every step in Postgres. If you are a gamer, think of this as a **"save point"** for your code: if a function fails, a new function can spin up and pick up right where the last checkpoint left off.

### 在 Postgres 中存储函数状态
> ### Storing Function State in Postgres

当你初始化一个 DBOS 应用程序时，它会在你的 Postgres 集群中、紧邻应用数据的位置创建一个新的专用数据库。以官方的“Widget Store”示例为例：
> When you initialize a DBOS application, it creates a new dedicated database inside your Postgres cluster alongside your app data. Taking their "Widget Store" example:
1. `widget_store`：用于存储常规应用程序数据。
> 1. `widget_store`: Used for storing regular application data.
2. `widget_store_dbos_sys`：用于存储工作流状态。
> 2. `widget_store_dbos_sys`: Used for storing the workflow state.

### 工作流逻辑
> ### Workflow Logic

DBOS 工作流引擎的核心执行机制如下：
> The core execution mechanics of the DBOS workflow engine operate as follows:
1. 当工作流启动时，它会生成一个唯一 ID，并将其及其输入记录到 Postgres 的 `workflow_status` 表中，状态为 `PENDING`（挂起）。
> 1. When a workflow starts, it generates a unique ID and records it in a Postgres `workflow_status` table with a `PENDING` status, along with its inputs.
2. 每当一个步骤完成时，其输出会被记录到 Postgres 的 `operation_outputs` 表中。
> 2. Each time a step completes, its output is logged in a Postgres `operation_outputs` table.
3. 工作流结束后，`workflow_status` 表中的状态将更新为 `SUCCESS`（如果发生未捕获的异常则为 `ERROR`）。
> 3. Once the workflow finishes, its status in the `workflow_status` table updates to `SUCCESS` (or `ERROR` if an uncaught exception occurred).

### 错误逻辑与恢复
> ### Error Logic & Recovery

如果程序中断，DBOS 库会在重新启动时启动一个后台线程，从未完成工作流最后完成的状态处恢复它们：
> If a program is interrupted, the DBOS library launches a background thread on restart to resume incomplete workflows from their last completed state:
1. 它会查询 Postgres 中所有处于 `PENDING` 状态的工作流，并使用原始输入重新调用工作流函数。
> 1. It queries Postgres for all `PENDING` workflows and re-invokes the workflow function using its original inputs.
2. 随着工作流重新执行，它会在尝试执行每个步骤之前检查 Postgres。如果该步骤的输出已经存在，它将跳过执行并直接复用存储的输出。
> 2. As the workflow re-executes, it checks Postgres before attempting each step. If the step's output already exists, it skips execution and reuses the stored output.
3. 工作流将在第一个尚未将其输出存储到 Postgres 的步骤处恢复全新执行。
> 3. The workflow resumes fresh execution at the very first step whose output isn't yet stored in Postgres.

由于工作流具有确定性，它们可以可靠地重放存储的步骤输出，从而恢复到中断前的准确状态。
> Because workflows are deterministic, they can reliably replay stored step outputs to recover their exact pre-interruption state.

---

## 使用 Postgres 的优势
> ## The Benefits of Using Postgres

相比 AWS Step Functions 或 Temporal 等外部工作流引擎，DBOS 具有几个明显的优势：
> DBOS offers several distinct advantages over external workflow engines like AWS Step Functions or Temporal:

### 1. 性能
> ### 1. Performance
由于步骤转换只是局部的 Postgres 写入（约 1 毫秒），而不是向外部协调器发送异步调度（约 100 毫秒），因此 **DBOS 的速度比 AWS Step Functions 快 25 倍**。
> Because step transitions are just local Postgres writes (~1ms) rather than async dispatches to an external orchestrator (~100ms), DBOS is [25x faster than AWS Step Functions](https://www.dbos.dev/blog/dbos-vs-aws-step-functions-benchmark).

### 2. 精确一次执行（Exactly-Once Execution）
> ### 2. Exactly-Once Execution
DBOS 提供了一个特殊的 `@DBOS.Transaction` 装饰器，可以在原生 Postgres 事务中运行整个步骤，从而保证数据库事务步骤的精确一次执行。
> DBOS features a special `@DBOS.Transaction` decorator that runs an entire step inside a native Postgres transaction, guaranteeing exactly-once execution for database-transactional steps.

### 3. 幂等性
> ### 3. Idempotency
你可以为工作流分配一个幂等键，从而保证即使使用相同的键被意外多次调用，它也只会执行一次。其底层原理非常简单，就是将工作流的唯一 ID 映射到你的幂等键上。
> You can assign an idempotency key to a workflow, guaranteeing that it only executes once even if accidentally called multiple times with the same key. Under the hood, this simply maps the workflow's unique ID to your idempotency key.

### 4. 熟悉的 Postgres 工具链
> ### 4. Familiar Postgres Tooling
由于所有内容都存储在 Postgres 中，你现有的工具链——包括备份、图形界面（GUI）、命令行实用程序和监控——都可以直接开箱即用。
> Because everything lives in Postgres, your existing tooling—backups, GUIs, CLI utilities, and monitoring—just works out of the box.

---

## 快速开始
> ## Get Started

准备好尝试了吗？请查看官方集成指南：
> Ready to try it out? Check out the official integration guide:

[在 Supabase 中使用 DBOS →](https://docs.dbos.dev/integrations/supabase)
> [Use DBOS With Supabase →](https://docs.dbos.dev/integrations/supabase)