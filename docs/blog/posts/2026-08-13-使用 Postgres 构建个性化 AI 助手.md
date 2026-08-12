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
- AI助手
- pgvector
- 长期记忆
- Supabase
title: 使用 Postgres 构建个性化 AI 助手
---
### 文章背景与核心概要
大型语言模型（LLM）擅长结构化处理非结构化文本，但在长对话中往往难以保持长期记忆和进行准确的数据检索。本指南将介绍如何通过将 LLM 与 **PostgreSQL**、**pgvector**、**pg_cron** 以及外部工具相结合，构建一个具备长期记忆保留能力的个性化 AI 助手。

利用限定范围的数据库架构（Schema）、用于自主运行的定时提示词、实时网页搜索以及 MCP 集成（如 Zapier），该助手能够保持深度上下文、追踪个人数据并自主运行——所有这一切的估计成本**每月低于 0.60 美元**。

---

<video autoplay="" class="rounded-xs m-0" loop="" muted="" playsinline=""><source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/marketing/blog/natural-db/natural-db-demo-combined.mp4" type="video/mp4"/></video>

---

## 核心架构 (Core Architecture)

助手的灵活性依赖于几个集成的构建模块：

### 1. 受控的数据库架构 (Scoped Database Control)
助手将所有结构化数据存储在名为 `memories` 的专用 Postgres 架构中。为确保系统安全性，LLM 严格在受限制的数据库角色（`memories_role`）下运行。
* **受限架构 (Scoped Schema)**：LLM 可以通过 `execute_sql` 工具在 `memories` 架构内创建表、存储数据和执行操作。
* **系统表保护 (System Table Protection)**：所有其他架构（包括 `public`）对 LLM 来说完全不可访问。

### 2. 上下文与记忆系统 (Context & Memory Systems)
三种互补的记忆类型可维持完整的对话连贯性：
* **消息历史（短期记忆）**：按时间顺序列出最近的消息，以提供即时上下文。
* **语义记忆（通过 `pgvector` 进行向量搜索）**：存储对话嵌入（Embedding），以便进行模糊概念检索（例如：“*我们上个月讨论过的那个提高生产力的东西*”）。
* **结构化记忆（SQL 数据）**：将具体事实存储在由 LLM 动态创建的表中，以便进行精确查询（例如：“*我上个季度在咖啡上花了多少钱？*”）。

### 3. 定时提示词与自主性 (Scheduled Prompts & Autonomy)
自主行为由 **`pg_cron`** 和 **`pg_net`** 驱动。定时提示词会调用与标准提示词完全相同的边缘函数（Edge Functions），从而赋予定时任务对所有系统工具的完全访问权限。

**工作流示例：**“*每周日晚上 6 点，分析我的投资组合表现并研究市场趋势*”
1. 定时任务（Cron Job）于周日晚上 6 点自动执行提示词。
2. LLM 从你的 `memories` 架构中检索持仓数据。
3. 运行网络搜索以获取相关的市场新闻和竞争对手更新。
4. 将搜索结果结构化并保存回数据库中。
5. 通过 Zapier MCP 发送个性化电子邮件报告。
6. 后续查询可以无缝引用这些历史数据。

### 4. 网页搜索集成 (Web Search Integration)
该系统利用内置的 LLM 网页搜索工具来访问实时信息和当前事件：

```sql
-- 从网页搜索结果自动生成
CREATE TABLE research_findings (
  topic TEXT,
  source_url TEXT,
  key_insights TEXT[],
  credibility_score INTEGER,
  search_date TIMESTAMPTZ DEFAULT NOW()
);
```

### 5. Zapier MCP 集成 (Zapier MCP Integration)
通过与 Zapier 的模型上下文协议（MCP）集成，你的助手可以：
* 读取和发送邮件 (Gmail)
* 管理日历事件
* 更新电子表格
* 发送通知 (Slack, Discord, SMS)
* 创建任务 (Trello, Asana, Notion)
* 控制智能家居设备

### 6. 输入/输出集成 (Input/Output Integration)
默认接口使用 **Telegram 机器人**，通过 Supabase 边缘函数的 Webhook 进行通信。这可以轻松替换为 Web UI、语音接口或自定义应用程序。

### 7. 自我演进的系统提示词 (Self-Evolving System Prompt)
助手维护两个不同的行为层：
* **基础行为 (Base Behavior)**：核心功能（数据库操作、日程安排、网页搜索）通过恒定的系统提示词保持一致。
* **个性化行为 (Personalized Behavior)**：通信风格和偏好根据用户反馈动态演进，并安全地存储在带有完整版本历史的 `public.system_prompts` 表中。

---

## 实际应用场景 (Practical Use Cases)

### 1. 跑步追踪
* **提示词**：“*帮我追踪每天的跑步情况，每天早上一条提醒，包含前一天跑步的详细信息。*”
* **工作原理**：LLM 创建用于记录指标和天气条件的 `runs` 表，设置每日定时任务，并通过 Telegram 协调日常打卡。

### 2. 个人食谱与膳食规划
* **提示词**：“*帮我记录三餐，并根据我厨房里现有的食材推荐食谱。*”
* **工作原理**：LLM 生成 `recipes`、`ingredients`、`meal_history` 和 `meal_ratings` 表，利用每日定时提示词将可用食材与饮食习惯进行交叉比对。

### 3. 公司反馈分析
* **提示词**：“*通过每天分析支持工单来帮我追踪客户反馈，并每周给我提供总结。*”
* **工作原理**：助手每天通过 MCP 获取工单，分析用户情感，将调查结果存储在 `feedback` 表中，并主动发送警报。

### 4. 基于兴趣的文章书签
* **提示词**：“*帮我追踪关于 AI 和气候变化的有趣文章，并提醒我那些还没读过的重要文章。*”
* **工作原理**：助手每天在网上搜索相关文章，存储其元数据和阅读状态，并提供个性化的阅读建议。

---

## 实施指南 (Implementation Guide)

### 前置条件 (Prerequisites)
* Supabase 账户（免费层即可）
* OpenAI API 密钥
* Telegram 机器人令牌 (Bot Token)
* Zapier 账户（可选）

---

### 选项 A：使用 Supabase CLI（推荐）
如果你更喜欢命令行，可以跳过手动 SQL 设置，使用 Supabase CLI 立即部署：

1. **克隆仓库**：
   ```bash
   git clone https://github.com/supabase-community/natural-db.git
   cd natural-db
   ```

2. **登录并关联项目**：
   在 [Supabase 仪表盘](https://supabase.com/dashboard) 上创建一个新项目，然后运行：
   ```bash
   supabase login
   supabase link --project-ref <YOUR-PROJECT-ID>
   ```

3. **推送数据库架构**：
   ```bash
   supabase db push
   ```

4. **部署边缘函数**：
   ```bash
   supabase functions deploy --no-verify-jwt
   ```
   *(完成这些步骤后，请直接转到**步骤 3：Telegram 机器人**)*。

---

### 选项 B：手动设置

#### 步骤 1：数据库设置
在 Supabase SQL 编辑器中运行 [GitHub 迁移文件](https://github.com/supabase-community/natural-db/blob/main/supabase/migrations/20250623120000_create_initial_schema.sql) 中的迁移脚本。该脚本将：
* 启用所需的扩展，如 `pgvector` 和 `pg_cron`。
* 创建 `memories` 架构。
* 设置具有受限架构权限的 `memories_role`。
* 配置 Cron 定时调度功能。

#### 步骤 2：边缘函数 (Edge Functions)
在你的 Supabase 仪表盘中创建以下三个函数：
* **`natural-db`**：处理核心逻辑、数据库查询、调度和工具执行的核心 AI 大脑 ([文件](https://github.com/supabase-community/natural-db/tree/main/supabase/functions/natural-db))。
* **`telegram-input`**：用于入站消息、用户验证和时区的 Webhook 处理器 ([文件](https://github.com/supabase-community/natural-db/blob/main/supabase/functions/telegram-input/index.ts))。
* **`telegram-outgoing`**：响应格式化程序和投递处理器 ([文件](https://github.com/supabase-community/natural-db/blob/main/supabase/functions/telegram-outgoing/index.ts))。

#### 步骤 3：Telegram 机器人
1. 使用 [@BotFather](https://t.me/botfather) 创建一个机器人。
2. 配置你的 Webhook URL：
   ```text
   https://api.telegram.org/bot[TOKEN]/setWebhook?url=https://[PROJECT].supabase.co/functions/v1/telegram-input
   ```

#### 步骤 4：环境变量
在 Supabase 项目设置 → 边缘函数 (Project Settings → Edge Functions) 中配置以下密钥：

**必需变量：**
* `OPENAI_API_KEY`：你的 OpenAI API 密钥。
* `TELEGRAM_BOT_TOKEN`：来自 @BotFather 的机器人令牌。
* `ALLOWED_USERNAMES`：逗号分隔的授权 Telegram 用户名列表。
* `TELEGRAM_WEBHOOK_SECRET`：用于验证传入 Webhook 的秘密令牌。

**可选变量：**
* `OPENAI_MODEL`：OpenAI 模型选择（默认为 `gpt-4.1-mini`）。
* `ZAPIER_MCP_URL`：用于 Zapier 集成的 MCP 服务器端点。

#### 步骤 5：测试集成
使用以下命令测试你的机器人：
* *“将我的杂货预算存为每月 400 美元”*
* *“今天天气怎么样？”*（触发网页搜索）
* *“提醒我每周一早上 7 点锻炼”*
* *“当我讨论爱好时表现得更热情一点”*（更新个性配置）

---

## 成本考量 (Cost Considerations)

基于每天 10 条消息（每月约 300 条消息）的估计每月运营成本：

* **Supabase**：免费层（500MB 数据库，5GB 带宽）— **$0.00 / 月**
* **OpenAI (GPT-4.1-mini)**：
  * 输入（约 1200 token/条消息）：$0.144
  * 输出（约 800 token/条消息）：$0.384
  * **小计**：**$0.53 / 月**
* **Telegram Bot API**：免费 — **$0.00 / 月**
* **Zapier**：免费层（300 次任务/月）— **$0.00 / 月**
* **向量嵌入 (`text-embedding-3-small`)**：约 300 条消息 — **$0.0072 / 月**

**估计每月总成本：约 $0.54**

---

## 结论 (Conclusion)

本项目展示了模块化组件——其中 LLM 只是拼图的一部分——如何构建出远超各部分总和的系统。如需了解更多架构灵感，请查看 [Geoffrey Litt 的这篇精彩文章](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs)。

准备好构建你自己的助手了吗？访问 [GitHub 仓库](https://github.com/supabase-community/natural-db) 开始使用，贡献改进，或分享你的自定义用例！