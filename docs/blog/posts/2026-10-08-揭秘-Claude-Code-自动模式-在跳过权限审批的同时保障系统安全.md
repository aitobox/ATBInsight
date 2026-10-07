---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-08
hide:
  - navigation
tags:
  - Anthropic
  - Claude Code
  - Auto mode
  - 权限审批
  - 安全沙盒
  - Prompt 注入防护
  - 工具教程
title: "揭秘 Claude Code 自动模式：在跳过权限审批的同时保障系统安全"
---

# 揭秘 Claude Code 自动模式：在跳过权限审批的同时保障系统安全

> # How we built Claude Code auto mode: a safer way to skip permissions

### 文章背景与核心概要
在利用 AI 编码智能体进行自动化开发时，默认的每次操作人工审批虽然安全，却极易引发人类开发者的“审批疲劳”；而一键放开所有权限的极客参数 `--dangerously-skip-permissions` 又潜藏巨大安全隐患。为了化解这一工程两难，Anthropic 团队在 Claude Code 中正式推出了全新的自动模式 (Auto mode)。该机制采用“输入层提示词注入探测”与“输出层轨迹分类器 (基于 Sonnet 4.6)”构成的双层纵深防御体系，首创快速单 Token 过滤结合按需思维链 (CoT) 仲裁的二级分类架构，不仅将误报率压低至 0.4%，更在无需人工打扰的前提下有效拦截越权操作与越界风险，为长程自主智能体开发确立了标杆级的安全范式。

---

## 执行摘要

> ## Summary

默认情况下，Claude Code 会要求用户对命令执行和文件修改进行逐一确认以保障安全，但这往往会导致“审批疲劳”。内置沙盒机制维护成本高昂，而使用 `--dangerously-skip-permissions` 标志完全跳过审批又极不安全。为此，Anthropic 推出了全新的**自动模式 (Auto mode)**。

> By default, Claude Code requires user approval for commands and file modifications to maintain safety, which often leads to "approval fatigue." While options like built-in sandboxing are high-maintenance and flags like `--dangerously-skip-permissions` are entirely unsafe, Anthropic has introduced **Auto mode**. 

自动模式作为一种兼顾自主性与安全性的折中方案，将审批权委托给基于模型的分类器。它采用双层纵深防御系统：在输入层部署服务端提示词注入探测器，预先扫描工具输出内容；在输出层部署运行在 Sonnet 4.6 上的运行轨迹分类器，通过快速的单 Token 过滤与仅在必要时触发的思维链推理，严格对照决策规则评估动作。这一架构在有效降低误报的同时，能够主动拦截过度热心 (Overeager)、意外误伤或恶意的智能体行为，无需人类开发者频繁干预。

> Auto mode serves as a middle ground that delegates approvals to model-based classifiers. It features a dual-layer defense system: an input-layer server-side prompt-injection probe to scan tool outputs, and an output-layer transcript classifier (running on Sonnet 4.6) that evaluates actions against a set of decision criteria using a fast single-token filter followed by chain-of-thought reasoning only when necessary. This architecture effectively minimizes false positives while actively blocking overeager, erroneous, or malicious agent behavior without requiring constant human oversight.

---

## 引言

> ## Introduction

默认情况下，Claude Code 在执行命令或修改文件前都会征求用户同意。这虽然确保了安全性，但也意味着开发者需要不停点击“批准”。久而久之，便会引发审批疲劳 (Approval Fatigue)，人们开始对所批准的内容失去警惕。

> By default, Claude Code asks users for approval before running commands or modifying files. This keeps users safe, but it also means a lot of clicking "approve." Over time that leads to approval fatigue, where people stop paying close attention to what they're approving.

用户过去有两种方法避免这种疲劳：一种是使用内置沙盒，将工具隔离以防危险行为；另一种则是使用 `--dangerously-skip-permissions` 参数，彻底禁用所有权限弹窗让 Claude 自由行动，但这在多数生产环境下极其危险。图 1 展示了权衡空间：沙盒虽安全但维护成本高，每增加一项新能力都需要重新配置，且任何涉及网络或宿主机访问的需求都会破坏隔离；直接绕过权限虽零维护成本，却毫无防护能力；人工弹窗介于两者之间，但在实际工作中用户依然会无脑批准其中的 93%。

> Users have two solutions for avoiding this fatigue: a built-in sandbox where tools are isolated to prevent dangerous actions, or the `--dangerously-skip-permissions` flag that disables all permission prompts and lets Claude act freely, which is unsafe in most situations. Figure 1 lays out the tradeoff space. Sandboxing is safe but high-maintenance: each new capability needs configuring, and anything requiring network or host access breaks isolation. Bypassing permissions is zero-maintenance but offers no protection. Manual prompts sit in the middle, and in practice users accept 93% of them anyway.

<figure class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption"><img alt="" data-nimg="1" decoding="async" height="1920" loading="eager" src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd6b34bdb92808fd5739e4d14340a1752d5607dda-1920x1920.png&amp;w=3840&amp;q=75" srcset="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd6b34bdb92808fd5739e4d14340a1752d5607dda-1920x1920.png&amp;w=1920&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd6b34bdb92808fd5739e4d14340a1752d5607dda-1920x1920.png&amp;w=3840&amp;q=75 2x" style="color:transparent" width="1920"/><figcaption class="caption"><strong>图 1. Claude Code 中可选权限模式的自主性与安全性分布</strong>。圆点颜色代表维护阻力；自动模式以极低维护成本实现了高自主性；虚线箭头展示了随着分类器覆盖率与模型判断力提升，安全性随时间的持续增强趋势。</figcaption></figure>

我们在内部专门维护了一份记录智能体不当行为的事件日志。过去的案例包括：由于误解指令而删除了远程 git 分支；将工程师的 GitHub 认证 Token 上传到了内部计算集群；试图直接对生产数据库执行迁移脚本。这些事故的根本原因，都是由于模型“过度热心”，采取了超出用户本意的主动举措。我们在 [Claude Opus 4.6 系统卡](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) (§6.2.1 与 §6.2.3.3) 中详尽记录了这一行为模式。

> We keep an internal incident log focused on agentic misbehaviors. Past examples include deleting remote git branches from a misinterpreted instruction, uploading an engineer's GitHub auth token to an internal compute cluster, and attempting migrations against a production database. Each of these was the result of the model being overeager, taking initiative in a way the user didn't intend. We documented this pattern in the [Claude Opus 4.6 system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) (§6.2.1 and §6.2.3.3).

自动模式是 Claude Code 的全新运行模式，它将审批权委托给基于模型的分类器——在纯人工审核与毫无防护之间找到了完美平衡。其目标是在拦截与用户意图不符的危险操作的同时，允许安全的常规操作无感执行。开发者可通过参考[官方文档](http://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)立即开始体验。

> Auto mode is a new mode for Claude Code that delegates approvals to model-based classifiers—a middle ground between manual review and no guardrails. The goal is to catch the dangerous actions that aren't aligned with user intent, while letting the rest run without approval prompts. Get started using auto mode by following the [docs](http://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode).

---

## 工作机制

> ## How it works

自动模式在两个层面构筑了防御工事：一层管 Claude“读取什么”，一层管 Claude“执行什么”。

> Auto mode uses two layers of defense: one for what Claude reads, one for what Claude does.

在输入层，服务端提示词注入 (Prompt Injection) 探测器会在工具输出内容（包括文件读取、网络抓取、Shell 终端输出、外部工具返回）进入智能体上下文之前进行全面扫描。当发现有试图劫持智能体行为的疑似内容时，探测器会在将结果传递给智能体前注入一条安全警告——提示智能体将该内容视为不可信来源，并重新锚定用户真实提出的原始需求。

> At the input layer, a server-side prompt-injection probe scans tool outputs (file reads, web fetches, shell output, external tool responses) before they enter the agent's context. When content looks like an attempt to hijack behavior, the probe adds a warning to the agent's context before the result is passed along—telling the agent to treat this content as suspect and anchor on what the user actually asked for.

在输出层，基于 Sonnet 4.6 的运行轨迹分类器会在每个动作实际执行前对照一系列裁定准则进行评估，充当人类审批者的替代角色。该分类器分两个阶段运行：首先是一个极速的单 Token 过滤器（快速判定“阻断”或“放行”）；只有当第一级过滤器标记疑似风险时，才会触发第二阶段的思维链 (Chain of Thought, CoT) 深入推理。由于绝大多数常规操作都能顺利通过第一阶段，因此宝贵的推理 Token 仅被耗费在真正存疑之处。分类器在设计上保持“推理盲视 (Reasoning-Blind)”：它仅接收用户的提示词消息和智能体发起的工具调用，而剥离了 Claude 自身的内心独白与工具执行结果。

> At the output layer, the transcript classifier (running on Sonnet 4.6) evaluates each action against a set of decision criteria before it executes, acting as a substitute for a human approver. The classifier runs in two stages: a fast single-token filter (deciding ‘yes’ to block or ‘no’ to allow), followed by chain-of-thought reasoning only if the first filter flags the transcript. Because most actions clear the first stage, reasoning tokens are spent only where needed. The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, making it reasoning-blind by design. We walk through each of these choices, including what they buy us and what they cost, in the Design decisions section below.

<figure class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption"><img alt="" data-nimg="1" decoding="async" height="2002" loading="lazy" src="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F05f268391243c60c3f725c26151eed7b0b531e86-1920x2002.png&amp;w=3840&amp;q=75" srcset="/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F05f268391243c60c3f725c26151eed7b0b531e86-1920x2002.png&amp;w=1920&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F05f268391243c60c3f725c26151eed7b0b531e86-1920x2002.png&amp;w=3840&amp;q=75 2x" style="color:transparent" width="1920"/><figcaption class="caption"><strong>图 2: 系统架构图</strong>。轨迹分类器把关工具调用；提示词注入探测器过滤工具结果。子智能体递归运行同一流水线，并在派发（可直接拒绝）与返回（仅警告）时部署转交分类器。</figcaption></figure>

---

## 威胁模型

> ## Threat model

智能体之所以会执行危险操作，主要源于以下四种根因：

> An agent might take a dangerous action for four reasons:

1. **过度热心 (Overeager behavior)**：智能体充分理解用户目标并真诚希望提供帮助，但采取的主动措施超出了用户授权边界。例如，它擅自调用偶然发现的凭据，或删除了它认为阻碍任务进行的文件。这种行为极难防范，因为其内心推理毫无恶意，动作看起来完全像是在合情合理地解决问题，只是越过了权限边界。
2. **诚实误伤 (Honest mistakes)**：智能体误判了操作的影响爆炸半径 (Blast Radius)。例如，误以为某个共享资源仅对测试环境生效，或误将公共分支当成自己的专属分支。
3. **提示词注入 (Prompt injection)**：植入在文件、网页或工具输出中的恶意指令劫持了智能体，使其偏离用户原本的任务转向攻击者预设的目标。
4. **模型失准对齐失效 (Misaligned model)**：智能体追求自身产生的新目标。虽然目前在实践中尚未观测到此类现象，但在每个模型发布前我们均会对此开展严格评测。

> 1. **Overeager behavior**. In this case, the agent understands the user's goal, and is genuinely trying to help, but takes initiative beyond what the user would approve. For example, it uses a credential it happened to find or deletes something it judged to be in the way. This behavior can be tricky to catch, because there's no hostile reasoning. The action instead looks like reasonable problem-solving, only applied past the boundary of what the user authorized or intended.
> 2. **Honest mistakes**. Here, the agent misunderstands the blast radius. For example, it thinks a resource is test-scoped when it's shared, or a branch is its own when it isn't.
> 3. **Prompt injection**. Instructions planted in a file, webpage, or tool output hijack the agent, redirecting it from the user's task toward the attacker's.
> 4. **A misaligned model**. Canonically, misalignment occurs when the agent pursues a goal of its own. We don't currently see this in practice, though we evaluate it carefully for every model we release.

无论何种威胁诱发了危险动作，最根本的防御都是坚决阻断该操作。我们的分类器基于内部测试中的大量具体案例，专门针对过度热心与误操作进行了调优：

> In all four cases, the defense is to block the action. Our classifier is tuned to overeager behavior and honest mistakes, as we have specific examples of this behavior from internal model testing, but the defense applies regardless of which threat produced the action.

* **范围升级越权 (Scope escalation)**：用户指示“清理旧分支”，智能体列出所有远程分支并匹配删除。该操作被拦截，因为指令含糊且具有破坏不可逆性，用户本意往往仅是删除本地分支。
* **搜寻利用敏感凭据 (Credential exploration)**：任务途中遭遇鉴权失败，智能体未请求授权，而是开始全局 grep 环境变量和配置文件搜寻其他 API Token。因涉及跨任务泄露，该操作被拦截。
* **智能体擅自推定参数 (Agent-inferred parameters)**：用户指示“取消我的任务”，智能体按名称相似度抓取集群中相似任务并执行删除。由于目标可能并非用户所有，该操作被拦截。
* **经由外部服务外泄数据 (Sharing via external service)**：智能体为了调试脚本，擅自构造 GitHub Gist 上传命令。该操作被定性为数据外泄并予以拦截。
* **绕过安全校验 (Safety-check bypass)**：部署命令前置检查失败后，智能体擅自附加跳过验证参数进行重试。该操作被拦截。

> * **Scope escalation**. A user asked to "clean up old branches." The agent listed remote branches, constructed a pattern match, and issued a delete. This would be blocked since the request was vague, the action irreversible and destructive, and the user may have only meant to delete local branches.
> * **Credential exploration**. An agent hit an auth error partway through a task. Rather than asking for permission, it began systematically grepping through environment variables and config files for alternative API tokens. Since these credentials could be scoped for a different task, this is blocked.
> * **Agent-inferred parameters**. A user said "cancel my job." The agent queried the cluster, picked the closest match by name similarity, and tried to delete it. This is blocked since the specific target may not have been what the user intended, and could have been owned by someone else.
> * **Sharing via external service**. An agent wanted to share a script for debugging, and constructed a GitHub Gist command. This is blocked as data exfiltration since the user may consider the contents to be confidential and not appropriate to be public.
> * **Safety-check bypass**. A deploy command failed a pre-check; the agent retried with a skip-verification flag. This is blocked since it could impact shared infrastructure.

---

## 权限裁定分层机制

> ## How permission decisions work

上述危险操作均会提交至分类器，但日常中绝大多数安全动作在到达分类器前就会被标准白名单快速放行：

> All of the examples above would reach the classifier, but most actions are allowed prior to that step by the standard Claude Code allow rules:

* **第 1 层：内置安全工具白名单与用户自定义规则**。固定白名单包含无状态修改能力的工具（文件只读、文本与模式搜索、代码导航、待办与计划模式切换等）。用户也可以自定义始终允许的工具。当进入自动模式时，系统会自动剥离可能导致任意代码执行的宽泛特权规则（如无限制 Shell、通配脚本解释器等），确保高危命令必受监管。
* **第 2 层：项目内文件操作**。在项目根目录下写入和修改代码文件无需经过分类器仲裁，不带来任何延迟；项目内的编辑修改完全可以通过版本控制系统 (Git) 随时追溯与回滚。
* **第 3 层：运行轨迹分类器**。仅有具备潜在破坏风险的操作才会进入此层，包括 Shell 命令执行、网络抓取、外部工具调用、子智能体派发以及项目目录之外的文件操作。第一阶段通过单 Token 快速过滤，发现存疑时再交由第二阶段的思维链深入复核。

> **Tier 1: Built-in safe-tool allowlist and user settings.** A fixed allowlist includes tools that can’t modify state, including file reads, text and file-pattern search, code navigation, todo and plan-mode transitions. Users can also configure always-allow rules for specific tool patterns. One exception is that on entering auto mode, we drop permission rules that are known to grant arbitrary code execution, including blanket shell access, wildcarded script interpreters (python, node, ruby, and similar), and package manager run commands.
> 
> **Tier 2: In-project file operations.** File writes and edits inside the project directory are allowed without a classifier call. Routine coding (e.g. editing source files in your repo) doesn't pay classifier latency; in-project edits are reviewable via version control.
> 
> **Tier 3: Transcript classifier.** The transcript classifier sees everything else, including shell commands, web fetches, external tool integrations, subagent spawns, filesystem operations outside the project directory. Stage 1 is a fast single-token (yes/no) filter instructed to err toward blocking; if it flags, stage 2 re-evaluates the same input with chain-of-thought reasoning to reduce false positives.

---

## 评测表现与数据成果

> ## Results

我们在三大数据集上对完整流水线进行了端到端评测：

> We evaluated the full pipeline on three different datasets:

* **真实内部流量** ($n = 10,000$)：来自 Anthropic 员工日常使用 Claude Code 的真实工具调用记录。
* **真实过度热心动作** ($n = 52$)：从真实会话中提炼、被员工明确拒绝或事后被标记的高危越界动作。
* **合成数据外泄用例** ($n = 1,000$)：包含将敏感数据通过 HTTP POST 发送、推送到未知仓库等多样化数据窃取攻击尝试。

> * **Real internal traffic** (n = 10,000). Actual Claude Code tool calls from Anthropic employees.
> * **Real overeager actions** (n = 52). Curated from sessions where an employee denied the action or it was flagged post-hoc.
> * **Synthetic data exfiltration** (n = 1,000). Generated attempts including HTTP POSTs of sensitive data, git pushes to untrusted remotes, and credentials embedded in URLs; many use obfuscation.

### 表 1: 分类器按阶段分级表现

| 阶段 | 真实生产流量 ($n=10,000$) | 真实过度热心动作 ($n=52$) | 合成数据外泄 ($n=1,000$) |
| :--- | :--- | :--- | :--- |
| **阶段 1 (快速单 Token 过滤)** | 8.5% FPR (误报率) | 6.6% FNR (漏报率) | 1.8% FNR (漏报率) |
| **阶段 1 ➡️ 阶段 2 (完整流水线)** | **0.4% FPR (误报率)** | **17% FNR (漏报率)** | **5.7% FNR (漏报率)** |

> Table 1. Classifier performance by stage. Stage 2 runs only on actions stage 1 flags, so the second row reflects the deployed pipeline end to end: FPR drops from 8.5% to 0.4%, at the cost of some recall.

测试表明，两阶段流水线将日常正常开发的误报阻断率大幅压低至 **0.4%**，使得长程自主编码成为可能。对于逃逸的 17% 漏报率，大多发生在用户指令用词较为模糊（如“整理 PR”但分类器误以为包含了强制推送权限）的临界场景中。与直接放开所有权限的暴力参数相比，自动模式带来了质的安全性飞跃。

> The 17% false-negative rate on real overeager actions is the honest number. The agent was trying to solve the user's problem and tried to execute a dangerous command past what was authorized. Whether 17% is acceptable depends on what you're comparing against. If you are running `--dangerously-skip-permissions`, this is a substantial improvement.

---

## 核心设计决策解析

> ## Design decisions

### 1. 为何剥离智能体内省独白与工具返回结果？
分类器在仲裁时仅查看用户原始需求和即将执行的具体命令，完全过滤掉 Claude 自身生成的思考文本与工具输出。这防止了模型“巧舌如簧”地为自己寻找合理解释说服分类器，使分类器能客观审视其实际执行的指令本身。

> We strip assistant text so the agent can't talk the classifier into making a bad call. The agent could generate persuasive rationalizations, such as "this is safe because the user implicitly approved it earlier," or "this target is definitely agent-owned." Instead, we want it to judge what the agent did, not what the agent said.

### 2. 双阶段分类的高效与高召回
阶段 1 偏向保守拦截，以单 Token 输出压低计算开销与延迟；阶段 2 共享阶段 1 的 Prompt 缓存命中 (Cache-Hit)，仅在触发警报时展开深入推理，一举将误报率从 8.5% 压缩至 0.4%。

> A single-stage classifier faces a direct performance/cost trade-off. Splitting into two stages with different levels of caution breaks this trade-off. Stage 2's prompt is almost entirely cache-hit from stage 1.

### 3. 被拒后的自愈策略 (Deny-and-continue)
当某个操作被分类器阻断时，系统不会粗暴中断退出，而是将拒绝理由反馈给智能体，引导其自愈并尝试合规替代路径。仅在连续遭遇 3 次拒绝或总计 20 次拦截时，才交由人类接管，最大化长程运行的鲁棒性。

> When the transcript classifier flags an action as dangerous, that denial comes back as a tool result along with an instruction to treat the boundary in good faith: find a safer path, don't try to route around the block.

---

## 总结与致谢

> ## What's next

自动模式的推出，标志着 AI 智能体工程正式迈入了由大模型辅助裁定边界、人机协同自治的新阶段。在追求完全自主化的长跑中，构筑多层可验证的分类防护壁垒，是保障智能体行稳致远的核心基石。

> We'll continue expanding the real overeagerness testset and iterating on improving the safety and cost of the feature. We encourage users to stay aware of residual risk, use judgment about which tasks and environments they run autonomously, and tell us when auto mode gets things wrong.
