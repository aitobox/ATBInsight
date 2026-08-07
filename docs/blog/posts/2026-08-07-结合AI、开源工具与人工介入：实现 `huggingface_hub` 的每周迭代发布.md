---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-07
hide:
- navigation
tags:
- Hugging Face
- GitHub Actions
- AI Agents
- Python
- CI/CD
title: 结合AI、开源工具与人工介入：实现 `huggingface_hub` 的每周迭代发布
---
### 文章背景与核心概要
本文介绍了 Hugging Face 核心 Python 客户端库 `huggingface_hub` 如何将其发布周期从原本耗时数小时、周期长达 4 到 6 周的缓慢流程，成功转型为高效的**每周发布机制**。通过将机械化的工作交由 GitHub Actions 处理，并借助开源工具与开放权重模型（如 `GLM-5.2`）来自动化起草发布说明，该团队在保持极低成本（每次发布约 0.25 美元）的同时，大幅提升了迭代频率。

文章深入探讨了技术核心：采用严格的确定性护栏（Deterministic Guardrails）校验生成的 PR 引用与真实清单，结合 OIDC 信任发布（Trusted Publishing）和可验证的运行时环境（Verifiable Runtimes），在保障发布质量的同时实现人工审核把关。这种“开源组件 + AI 辅助 + 人工介入”的模式为所有开源维护者提供了一套极具参考价值的现代化发布流水线范本。

---

## Shipping `huggingface_hub` Every Week with AI, Open Tools, and a Human in the Loop

**Authors:** Lucain Pouget (`Wauplin`), Célina Hanouti (`celinah`)  
**Published:** June 23, 2026  
**Status:** [Update on GitHub](https://github.com/huggingface/blog/blob/main/huggingface-hub-release-ci.md)

---

## 摘要

`huggingface_hub` 是 Hugging Face 生态系统的基础 Python 客户端，被 `transformers`、`datasets` 和 `diffusers` 等库广泛使用。过去，该库的发布周期长达 4 到 6 周，且需要数小时的手动劳动。如今，团队成功将其转型为**每周发布周期（weekly release cycle）**。

这一运维升级通过结合以下几点得以实现：
1. **GitHub Actions**：用于机械化工作流（版本号递增、打标签、推送）。
2. **开源工具与开放权重模型**（例如通过 HF Inference Providers 调用的 `GLM-5.2`）：用于自主起草发布说明和公告。
3. **确定性护栏**：强制执行严格的验证（将生成的 PR 引用与事实清单进行比对）。
4. **人工介入检查点**：由维护者快速审查、润色并发布最终版本和更新。

至关重要的是，整个流水线完全依赖开源工具、OIDC 信任发布以及可验证的运行时，从而将成本保持在最低水平（每次发布约 $\approx \$0.25$），并且完全可供任何开发者适配使用。

> ## Summary
> 
> `huggingface_hub` is the foundational Python client for the Hugging Face ecosystem, utilized by libraries like `transformers`, `datasets`, and `diffusers`. Previously operating on a sluggish 4-to-6-week release cadence requiring hours of manual labor, the team successfully transitioned to a **weekly release cycle**. 
> 
> This operational overhaul was achieved by combining:
> 1. **GitHub Actions** for mechanical workflows (version bumping, tagging, pushing).
> 2. **Open-Source Tools & Open-Weight Models** (such as `GLM-5.2` via HF Inference Providers) to autonomously draft release notes and announcements.
> 3. **Deterministic Guardrails** that enforce strict validation (checking generated PR references against a ground-truth manifest).
> 4. **A Human-in-the-Loop Checkpoint** where maintainers quickly review, polish, and publish the final releases and updates.
> 
> Crucially, the entire pipeline relies on open tools, OIDC Trusted Publishing, and verifiable runtimes, keeping costs minimal ($\approx \$0.25$ per release) and fully adaptable by any developer.

---

## 我们从哪里开始

旧的流程部分自动化，但绝大部分依赖手动。

* **已在 CI 中实现：** 推送标签后发布到 PyPI；在下游库中开辟测试分支并锁定候选版本（RC）。
* **每次依然需要手动处理的事项：**
  * 创建发布分支、递增版本号、提交、打标签并推送。
  * 监视下游 CI 运行情况并对失败进行分类排查。
  * 阅读数十个合并的 PR 以手写发布说明。
  * 发布稳定版本、起草 Slack 公告、社交媒体动态以及发布后的 PR。

一个 minor 级别的小版本发布很容易耗费半天集中的工作时间，甚至拖延好几天。

> ## Where We Started
> 
> The old process was partly automated, mostly manual.
> 
> * **Already in CI:** Publishing to PyPI once a tag was pushed; opening test branches in downstream libraries with the release candidate pinned.
> * **Still manual, every single time:** 
>   * Creating the release branch, bumping versions, committing, tagging, and pushing.
>   * Watching downstream CI runs and triaging failures.
>   * Reading through dozens of merged PRs to write release notes by hand.
>   * Cutting stable releases, drafting Slack announcements, social posts, and post-release PRs.
> 
> A minor release easily consumed a half-day of focused work spread over several days.

---

## 两类工作

简化流程需要将任务划分为两个截然不同的类别：
1. **机械化工作（自动化）：** 递增版本号、提交、打标签、推送、开启下游测试分支以及创建发布后 PR。
2. **认知工作（AI 辅助）：** 编写发布说明、选择亮点以及组织公告措辞。在严格的人工监督下，AI 模型能在几秒钟内将一张白纸变成一份扎实的初稿。

> ## Two Kinds of Work
> 
> Streamlining the process required separating tasks into two distinct buckets:
> 1. **Mechanical Work (Automated):** Bumping versions, committing, tagging, pushing, opening downstream test branches, and creating post-release PRs.
> 2. **Cognitive Work (AI-Assisted):** Writing release notes, selecting highlights, and phrasing announcements. An AI model turns a blank page into a solid first draft in seconds, backed by strict human supervision.

---

## 设计原则：开放组件，人人可用

为了避免厂商锁定，整个技术栈依赖于易获取的开源组件：

| 组件 | 功能 |
| :--- | :--- |
| **GitHub Actions** | 编排整个发布流程 |
| **[OpenCode](https://opencode.ai/)** | 驱动模型的 Agent 运行时 |
| **开放权重模型**（目前使用 Z.ai 的 [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)） | 起草发布说明和 Slack 公告 |
| **[HF Inference Providers](https://huggingface.co/docs/inference-providers/index)** | 提供模型服务 |
| **[PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)** | 发布软件包 |

> ## The Design Principle: Open Parts, Reusable by Anyone
> 
> To avoid vendor lock-in, the entire stack relies on accessible, open components:
> 
> | Part | What it does |
> | :--- | :--- |
> | **GitHub Actions** | Orchestrates the whole release |
> | **[OpenCode](https://opencode.ai/)** | Agent runtime that drives the model |
> | **An open-weights model** (currently [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) from Z.ai) | Drafts the release notes and Slack announcement |
> | **[HF Inference Providers](https://huggingface.co/docs/inference-providers/index)** | Serves the model |
> | **[PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)** | Publishes the package |

---

## 流水线导览

整个工作流包含在一个单独的文件中——[`.github/workflows/release.yml`](https://github.com/huggingface/huggingface_hub/blob/main/.github/workflows/release.yml)，通过 workflow dispatch 触发：

```yaml
on:
  workflow_dispatch:
    inputs:
      release_type:
        type: choice
        options:
          - minor-prerelease   # 从 main 分支切出一个 RC 版本
          - minor-release      # 将 RC 版本晋升为正式版本
          - patch-release      # 在现有发布分支上进行缺陷修复
```

### 流水线执行流程：
1. **准备（Prepare）：** 计算下一个版本号，创建或复用发布分支，更新 `__version__`，提交、打标签并推送。
2. **发布到 PyPI（Publish to PyPI）：** 构建并上传 `huggingface_hub` 及 `hf` CLI 软件包。
3. **发布说明（Release Notes）：** 对比自上次打标签以来的 commits 差异，拉取 PR 元数据，并提示模型起草一个结构化的更新日志，保存为 GitHub 的*草稿*发布（Draft Release）。
4. **下游测试分支（Downstream Test Branches）：** 在 `transformers`、`datasets`、`diffusers` 和 `sentence-transformers` 中开辟分支并锁定 RC 版本。
5. **Slack 公告（Slack Announcement）：** 生成针对团队定制的内部发布摘要。
6. **归档说明（Archive Notes）：** 将原始 AI 草稿和人工编辑后的版本上传至 Hugging Face 存储桶（Bucket）。
7. **发布后收尾与清理（Post-Release & Cleanup）：** 开启一个将 `main` 分支版本推进到下一个 `dev0` 的 PR，在包含的 PR 下留下一条“已在 vX.Y.Z 中发布”的评论，并同步 CLI 文档。

> ## A Tour of the Pipeline
> 
> The full workflow is contained in a single file—[`.github/workflows/release.yml`](https://github.com/huggingface/huggingface_hub/blob/main/.github/workflows/release.yml)—triggered via workflow dispatch:
> 
> ```yaml
> on:
>   workflow_dispatch:
>     inputs:
      release_type:
>         type: choice
>         options:
>           - minor-prerelease   # cut an RC from main
>           - minor-release      # promote the RC to final
>           - patch-release      # bugfix on an existing release branch
> ```
> 
> ### Pipeline Execution Flow:
> 1. **Prepare:** Compute the next version, create/reuse release branches, bump `__version__`, commit, tag, and push.
> 2. **Publish to PyPI:** Build and upload `huggingface_hub` and the `hf` CLI package.
> 3. **Release Notes:** Diff commits since the last tag, pull PR metadata, and prompt the model to draft a structured changelog saved as a *draft* GitHub release.
> 4. **Downstream Test Branches:** Open branches in `transformers`, `datasets`, `diffusers`, and `sentence-transformers` with the RC pinned.
> 5. **Slack Announcement:** Generate a team-tailored internal release summary.
> 6. **Archive Notes:** Upload both raw AI drafts and human-edited versions to a Hugging Face Bucket.
> 7. **Post-Release & Cleanup:** Open a PR bumping `main` to the next `dev0`, leave a "shipped in vX.Y.Z" comment on included PRs, and sync CLI docs.

---

## 信任但须核实：人工介入的核心

语言模型在起草散文方面表现卓越，但在全面性方面往往不可靠。为了防止遗漏或产生幻觉虚构 PR，该流水线将非确定性的 AI 生成与**确定性护栏（Deterministic Guardrails）**结合起来：

1. **提取真实数据（Ground Truth）：** Python 脚本获取属于该发布范围的所有 PR：
   ```python
   # 确定性处理：从该范围内的 squash-merge 提交中提取 PR 编号。
   PR_NUMBER_PATTERN = re.compile(r"\(#(\d+)\)$")

   pr_numbers = [
       int(m.group(1))
       for commit in commits_since_last_tag
       if (m := PR_NUMBER_PATTERN.search(commit.title))
   ]
   save_manifest(pr_numbers)  # 真实数据源
   ```
2. **验证输出：** 将模型的 markdown 输出与清单进行比对：
   ```python
   expected = set(load_manifest())          # 应该包含的内容
   found    = extract_pr_refs(notes_md)     # 模型实际写入的内容 (#1234 -> 1234)

   missing = expected - found               # 被悄悄漏掉的
   extra   .  = found - expected               # 属于其他发布版本的
   ```
3. **自动修复循环：** 如果存在差异，系统将提示 Agent 在继续操作前精准修复这些特定缺失或多余的 PR。

> ## Trust But Verify: The Human-in-the-Loop Core
> 
> Language models are exceptional at drafting prose but unreliable when it comes to exhaustiveness. To prevent dropped or hallucinated PRs, the pipeline pairs non-deterministic AI generation with **deterministic guardrails**:
> 
> 1. **Extract Ground Truth:** A Python script fetches all PRs belonging to the release range:
>    ```python
>    # Deterministic: extract PR numbers from squash-merge commits in the range.
>    PR_NUMBER_PATTERN = re.compile(r"\(#(\d+)\)$")
> 
>    pr_numbers = [
>        int(m.group(1))
>        for commit in commits_since_last_tag
>        if (m := PR_NUMBER_PATTERN.search(commit.title))
>    ]
>    save_manifest(pr_numbers)  # the source of truth
>    ```
> 2. **Validate Output:** Check the model's markdown output against the manifest:
>    ```python
>    expected = set(load_manifest())          # what should be there
>    found    = extract_pr_refs(notes_md)     # what the model wrote (#1234 -> 1234)
> 
>    missing = expected - found               # silently dropped
>    extra   = found - expected               # belongs to a different release
>    ```
> 3. **Auto-Fix Loop:** If discrepancies exist, the agent is prompted to fix precisely those specific missing or extra PRs before proceeding.

---

## 为模型提供依据（Grounding）

为了确保事实准确性，流水线会获取由特定 PR 修改的任何文档文件（`docs/*.md`）的统一差异（unified diffs）：

```python
def fetch_doc_diffs(pr):
    return [
        {"filename": f.filename, "status": f.status, "patch": f.patch}
        for f in pr.get_files()
        if f.filename.startswith("docs/") and f.filename.endswith(".md") and f.patch
    ]
```
这些数据会被纳入模型的上下文中，从而确保生成的代码示例与真实 API 保持精确一致。提示词通过模块化的 markdown [技能（Skills）](https://github.com/huggingface/huggingface_hub/tree/main/.opencode/skills/hf-release-notes)进行维护，并直接检入（check in）到代码仓库中。

> ## Grounding the Model
> 
> To ensure factual accuracy, the pipeline fetches the unified diffs of any documentation file (`docs/*.md`) touched by a given PR:
> 
> ```python
> def fetch_doc_diffs(pr):
>     return [
>         {"filename": f.filename, "status": f.status, "patch": f.patch}
>         for f in pr.get_files()
>         if f.filename.startswith("docs/") and f.filename.endswith(".md") and f.patch
>     ]
> ```
> This data is included in the model's context, ensuring accurate code examples matching real APIs. Prompts are maintained via modular markdown [Skills](https://github.com/huggingface/huggingface_hub/tree/main/.opencode/skills/hf-release-notes) checked directly into the repository.

---

## 人工检查点

1. 审核人员检查包含 AI 初版输出的草稿 GitHub 发布，并对语调和重点进行编辑。
2. 审核人员触发 `minor-release` 运行，将 RC 版本晋升为正式版。
3. 原始 AI 草稿和编辑后的版本并排存档，以便迭代优化未来的模型提示词。

> ## The Human Checkpoint
> 
> 1. Reviewers examine the draft GitHub release containing the AI's first pass, editing tone and emphasis.
> 2. Reviewers trigger the `minor-release` run to promote the RC to final.
> 3. Both raw AI drafts and edited versions are archived side-by-side to improve future model prompts iteratively.

---

## 开放且安全的管道

* **无 PyPI 令牌：** 通过短寿命的 OIDC 令牌和 [PEP 740](https://peps.python.org/pep-0740/) Sigstore 认证使用[信任发布（Trusted Publishing）](https://docs.pypi.org/trusted-publishers/)。
* **可验证的运行时：** OpenCode 运行时在执行前会被严格锁定并通过 SHA256 哈希进行校验：
  ```bash
  curl -fsSL https://opencode.ai/install | bash -s -- --version "${OPENCODE_VERSION}"
  echo "${OPENCODE_SHA256}  $(which opencode)" | sha256sum -c -
  ```

> ## Open and Secure Plumbing
> 
> * **No PyPI Tokens:** Uses [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) via short-lived OIDC tokens and [PEP 740](https://peps.python.org/pep-0740/) Sigstore attestations.
> * **Verified Runtime:** OpenCode runtimes are strictly pinned and checked via SHA256 hashes before execution:
>   ```bash
>   curl -fsSL https://opencode.ai/install | bash -s -- --version "${OPENCODE_VERSION}"
>   echo "${OPENCODE_SHA256}  $(which opencode)" | sha256sum -c -
>   ```

---

## 影响与收获

* **发布频率：** 迭代周期从原先的每 4–6 周缩短至**每周**。
* **成本：** 通过 Inference Providers 进行一次完整发布，成本约为 **$0.25**。
* **开发者体验：** 通过自动化的发布徽章缩短了贡献者的反馈闭环，并通过自动化的下游测试分支更早地发现集成问题。

如果您正在维护一个 Python 库，欢迎探索[公共工作流文件](https://github.com/huggingface/huggingface_hub/blob/main/.github/workflows/release.yml)，将这些模式适配到您自己的项目中！

> ## Impact & Takeaways
> 
> * **Frequency:** Cadence increased from every 4–6 weeks to **weekly**.
> * **Cost:** Around **$0.25** per full release via Inference Providers.
> * **Developer Experience:** Contributor loops shortened via automated release badges, and integration issues are caught earlier through automated downstream test branches.
> 
> If you maintain a Python library, explore the [public workflow file](https://github.com/huggingface/huggingface_hub/blob/main/.github/workflows/release.yml) to adapt these patterns for your own projects!