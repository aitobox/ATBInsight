---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-13
hide:
  - navigation
tags:
  - AWS
  - AI Agent
  - 本地模拟器
  - 自动化软件工程
title: "AWS 发布本地模拟器 AWS Emulator：由 AI 智能体全自主编写的 200+ 服务本地运行时"
---

# AWS 发布本地模拟器 AWS Emulator：由 AI 智能体全自主编写的 200+ 服务本地运行时

### 文章背景与核心概要
云计算开发长期以来面临一个显著痛点：本地联调和 CI 流水线测试往往需要连接昂贵的真实云环境，或依赖功能有限的第三方模拟工具。AWS 官方打破了这一局面，重磅发布了全新的本地模拟器 AWS Emulator，能够在离线状态下原生模拟超过 200 项 AWS 云服务 API。更为颠覆性的是，这个包含庞大代码库的工程并非由人类程序员敲出，而是由多组自主协同的 AI 智能体 (AI Agent) 全程编写、测试和打补丁修复完成。这一突破不仅为开发者提供了零账单、高保真的本地开发体验，更树立了 AI 驱动全自动化软件工程从前沿理论走向工业级落地的全新里程碑。

---

## 核心概述

> ## Summary

AWS 推出了一款功能强大的本地接口模拟器 —— **AWS Emulator**。它的核心目标是在本地完整模拟超过 200 项 AWS 云服务，开发者无需拥有真实的 AWS 账号，更不会产生任何云端服务账单费用。无论是运行在个人笔记本电脑、本地开发服务器，还是集成到 CI/CD 自动化流水线中，该工具都能无缝拦截 AWS 命令行工具 (CLI) 和软件开发工具包 (SDK) 的网络请求，为开发者带来极速、流畅的纯离线测试与调试闭环。

> AWS has introduced the **AWS Emulator**, a powerful local API emulator designed to replicate over 200 AWS services without requiring an active AWS account or incurring service fees. Operating on a laptop, a development server, or inside CI pipelines, the tool intercepts AWS CLI and SDK calls to provide a fast, offline testing loop. 

而这项发布最引人瞩目、最具颠覆性的地方在于其研发模式：**整套庞大的代码库完全由自主协同的 AI 智能体 (AI Agent) 独立编写、审查并打补丁完成。** AWS Emulator 基于 438 个 Smithy API 规范模型构建，目前已通过其严苛保真度测试套件中超过 56% 的测试用例。同时，它采用极为宽松的 CC0 协议开源，为开发者在传统的 LocalStack 和 Moto 等工具之外，提供了一个轻量高效的官方全新替代方案。

> What makes this release groundbreaking is its development process: **autonomous AI agents wrote, reviewed, and patched the entirety of its codebase.** Built from 438 Smithy API models, the emulator currently passes over 56% of its rigorous fidelity test suite, offering an efficient, CC0-licensed alternative to existing tools like LocalStack and Moto.

---

## 核心速览 (TL;DR)

> ## TL;DR

* **覆盖规模：** 基于 [438 个 AWS API 模型](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator) 构建，全面覆盖 [200+ 项云服务](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html)（每项服务对应一个独立的 Rust crate）。
* **系统要求：** 支持在 Linux x86_64/aarch64 环境下原生运行（提供 RPM 或 Debian 安装包），也可在 macOS/Windows 上通过 Docker 容器运行（内存上限限制为 2 GiB）。若从源码编译，则需要准备至少 100 GB 的可用磁盘空间。
* **测试表现：** 在 [v1.0.322 版本](https://github.com/aws/aws-emulator/releases/tag/v1.0.322) 中，已成功通过 42,857 项评分保真度测试中的 24,243 项（通过率达 56.6%）。
* **表现优异的服务：** AWS KMS 达到了 93.9% 的超高精准度（310 项测试中通过 291 项）；Amazon SQS 紧随其后，达到 89.8%。
* **目前偏弱的服务：** AWS CloudFormation 目前通过率相对落后，仅为 15.8%（2,612 项测试中仅通过 414 项）。

> * **Scale:** Built from [438 AWS API models](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator), covering [200+ services](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html) (one Rust crate per service).
> * **System Requirements:** Runs on Linux x86_64/aarch64 (RPM or Debian), or via Docker on macOS/Windows with a 2 GiB memory limit. Source builds require 100 GB of free disk space.
> * **Performance:** Passes 24,243 out of 42,857 scored fidelity tests (56.6%) in [release v1.0.322](https://github.com/aws/aws-emulator/releases/tag/v1.0.322).
> * **Top Performers:** AWS KMS achieves 93.9% accuracy (291 of 310 tests); Amazon SQS follows at 89.8%.
> * **Lowest Performers:** AWS CloudFormation trails at 15.8% (414 of 2,612 tests).

---

## 什么是 AWS Emulator？

> ## What is AWS Emulator?

[AWS Emulator](https://github.com/aws/aws-emulator) 是由 AWS 官方推出的一款无图形界面的本地常驻应用（Headless Application），能够对外提供高度逼真的 AWS API 接口端点。开发者只需配置标准的环境变量，将 AWS CLI 或 SDK 的网络请求重定向到本地地址，即可直接运行现有云应用程序，全程无需修改任何业务源代码。同时，它所创建的所有资源均存放于内存中，并在进程关闭时立即被安全清空，确保本地环境干净清爽。

> [AWS Emulator](https://github.com/aws/aws-emulator) is a headless local application provided by AWS that serves authentic AWS API endpoints. By redirecting the AWS CLI or SDKs via standard environment variables, developers can run applications locally without altering source code. All resources are stored in-memory and deleted immediately upon shutdown.

根据 [官方文档](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html) 的说明，在本地调用像 DynamoDB 这样的服务时，其行为逻辑与真实云端几乎毫无二致 —— 例如，当你发起一个表名仅有 2 个字符的 `CreateTable` 创建表请求时，模拟器能够准确返回与线上真实 AWS 环境字面完全一致的 `ValidationException` 校验异常报错信息。

> According to the [official documentation](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html), invoking services like DynamoDB locally yields authentic behavior—such as a `CreateTable` request with a 2-character name correctly returning the exact `ValidationException` text provided by live AWS services.

---

## AI 智能体是如何构建 AWS Emulator 的？

> ## How Did AI Agents Build AWS Emulator?

该项目的诞生始于向内部智能体 [Kiro](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator) 发出的一句简单提示词 (Prompt)。令人惊喜的是，Kiro 在短短约 15 分钟内便自动生成了一个功能可用的 Amazon SQS 消息队列本地模拟器。随后，AWS 团队顺水推舟，将这一全自动研发模式规模化扩展，组建了三支分工高度明确的自主 AI 智能体团队：

> The project originated from a single prompt directed to [Kiro](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator), which generated a functional Amazon SQS emulator in approximately 15 minutes. AWS then scaled the development process across three specialized teams of autonomous agents:

* **测试编写智能体 (Test Writers)：** 从公开的 [Smithy API 规范模型](https://github.com/aws/api-models-aws) 中提取衍生出各类测试用例场景，并在真实的 AWS 云端基础设施上逐一比对验证其行为。
* **缺陷捕获智能体 (Issue Finders)：** 将编写好的测试套件在本地模拟器上反复重放回放，并自动将所有偏离预期的失败用例记录为缺陷工单。
* **代码修复智能体 (Fixers)：** 自主认领单个缺陷问题，针对性编写修复逻辑并提交代码补丁 (Patch)。

> * **Test Writers:** Derive test scenarios from public [Smithy API models](https://github.com/aws/api-models-aws) and verify their behavior against real AWS infrastructure.
> * **Issue Finders:** Replay those test suites against the emulator and automatically log failures.
> * **Fixers:** Take on individual issues and submit targeted code patches.

在这里，每一个单独的代码补丁都要经历严苛的代码合入关卡 (Merge Gate)，涵盖自动构建、AI 自动化代码审查、全方位安全合规检测以及保真度基准测试。[专门的安全防护智能体还会持续执行对抗性安全审计](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html)。一线核心报告显示，每天有数百个 AI 智能体在并发运行，日均处理并修复数千个技术缺陷。所有生成的代码必须在 CodeCommit 托管的 AWS 内部流水线中顺利通过所有门禁，最终才会正式同步发布至 GitHub 开源社区。

> Every individual patch undergoes a strict merge gate covering builds, automated code reviews, security checks, and fidelity benchmarking. [Adversarial reviews are continuously executed by specialized security agents](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html). Lead reports indicate hundreds of concurrent agents resolving thousands of issues daily, with code deployed to GitHub only after clearing internal AWS pipelines managed on CodeCommit.

---

## AWS Emulator 的模拟精准度如何？

> ## How Accurate is AWS Emulator?

AWS 在每次版本发布时都会附带一份详细的 `scores.json` 评分数据。针对 [v1.0.322 版本](https://github.com/aws/aws-emulator/releases/tag/v1.0.322)（评测时间为 2026 年 11 月 11 日）的各项评估指标显示：

> AWS publishes a comprehensive `scores.json` file with each release. Evaluation metrics for [release v1.0.322](https://github.com/aws/aws-emulator/releases/tag/v1.0.322) (scored November 11, 2026) show:

* **整体测试表现：** 在 42,857 项评分测试中，共通过 24,243 项（整体通过率达 56.6%）；另有 80 项测试被跳过。
* **细粒度步骤保真度 (Step-Level Fidelity)：** 在细分的 68,007 个独立执行步骤中，共通过 49,810 步（步骤通过率达 73.2%）。
* **跨服务复杂工作流：** 6,569 组跨服务联调场景中，通过了 2,752 组（通过率为 41.9%）。
* **核心云服务支持度：** S3 的通过率达到 79.1%，DynamoDB 达到 77.3%，SNS 为 73.9%，Lambda 为 46.4%，而 EC2 则为 41.5%。

> * **Overall:** 24,243 of 42,857 scored tests passed (56.6%); 80 tests were skipped.
> * **Step-Level Fidelity:** 49,810 of 68,007 individual steps passed (73.2%).
> * **Cross-Service Workflows:** 2,752 of 6,569 passed (41.9%).
> * **Core Services:** S3 achieves 79.1%, DynamoDB 77.3%, SNS 73.9%, Lambda 46.4%, and EC2 41.5%.

根据 [保真度技术文档](https://docs.aws.amazon.com/emulator/latest/userguide/fidelity.html) 说明，控制平面 (Control-Plane) 的 API 接口与真实 AWS 服务的贴合度最高，而数据平面 (Data-Plane) 以及对 CloudFormation、Terraform 和 CDK 等基础设施即代码工具的支持程度则因具体服务而异。对于尚未实现的 API 操作，模拟器会友好且优雅地返回 HTTP 501 `NotImplemented`（未实现）状态码。完整的测试套件代码已在 [aws-emulator-evaluation-suite](https://github.com/aws/aws-emulator-evaluation-suite) 仓库中全面公开。

> Per the [fidelity documentation](https://docs.aws.amazon.com/emulator/latest/userguide/fidelity.html), control-plane APIs match AWS most closely, while data-plane, CloudFormation, Terraform, and CDK support varies by service. Unimplemented operations gracefully return an HTTP 501 `NotImplemented` status. The complete test suite is available in the [aws-emulator-evaluation-suite](https://github.com/aws/aws-emulator-evaluation-suite) repository.

---

## 如何运行 AWS Emulator？

> ## How Do You Run AWS Emulator?

根据官方项目 [README](https://github.com/aws/aws-emulator) 说明，目前主要提供四种快速部署与运行途径：

> According to the [README](https://github.com/aws/aws-emulator), there are four primary deployment paths:

1. **Linux 原生运行：** 直接下载并安装官方提供的 RPM 或 Debian 软件包，然后在终端执行 `aws-emulator` 命令。
2. **macOS / Windows 容器化运行：** 利用官方提供的 [AWS Dockerfile](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started-docker.html) 构建镜像并在容器中启动，推荐限制为 2 GiB 内存。
3. **Rust 内嵌测试模式 (Embedded Mode)：** 将模拟器作为项目的开发依赖 (dev-dependency) 直接引入，在执行单个自动化测试时按需动态拉起隔离的模拟实例。
4. **与编程智能体 (Coding Agents) 配合：** 配合 AWS CLI 2.35.0 及以上版本，执行命令 `aws agent-toolkit add-skill --skill-name aws-emulator` 将模拟器能力作为技能注入给 AI 编程助手。

> 1. **Linux:** Install the RPM or Debian package and execute `aws-emulator`.
> 2. **macOS/Windows:** Build a container utilizing the [AWS Dockerfile](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started-docker.html), subject to a 2 GiB memory cap.
> 3. **Rust Embedded Mode:** Integrate the emulator as a dev-dependency to spin up isolated instances per individual test.
> 4. **Coding Agents:** Run `aws agent-toolkit add-skill --skill-name aws-emulator` alongside AWS CLI version 2.35.0 or later.

源码编译后，模拟器默认会通过自带自签名证书的 HTTPS 协议在 `127.0.0.1:9297` 提供服务端口。从源码自行编译需要配置标准的 Rust 工具链、C 语言编译器，并且需要确保拥有至少 100 GB 的空闲磁盘空间。而在内嵌模式下首次运行 `cargo test` 时，也会产生类似的编译开销与磁盘占用。

> Source builds expose an HTTPS endpoint at `127.0.0.1:9297` secured via a self-signed certificate. Building from source requires a standard Rust toolchain, a C compiler, and at least 100 GB of available disk space. Embedded mode incurs a similar compilation footprint during the initial `cargo test` run.

---

## 与 LocalStack、Moto 和 Floci 的横向对比

> ## How Does It Compare with LocalStack, Moto, and Floci?

| 特性对比 (Feature) | AWS Emulator | LocalStack | Moto | Floci |
| :--- | :--- | :--- | :--- | :--- |
| **开源协议 (License)** | [CC0 1.0](https://github.com/aws/aws-emulator) (`vendor/` 为 Apache 2.0) | 商业授权许可 (Commercial plans) | Apache-2.0 | MIT |
| **价格成本 (Price)** | 完全免费 (Free) | 爱好者个人版 $0（仅限非商业）；基础版 $39/月；旗舰版 $89/月（年付标准） | 完全免费 (Free) | 完全免费 (Free) |
| **服务覆盖范围 (Service Coverage)** | 200+ 项服务，438 个 API 模型 | 视版本而定：30+ / 55+ / 110+ | README 未明确公开 | README 未统计总数 |
| **是否需要厂商鉴权 (Vendor Token Needed)** | 否 (No) | 是（需要 Auth Token） | 否 (No) | 未公开说明 |
| **默认网络端口 (Default Endpoint)** | HTTPS 127.0.0.1:9297 | 端口 4566 | [端口 5000](https://docs.getmoto.org/en/latest/docs/server_mode.html) | 端口 4566 |
| **进程内嵌测试模式 (In-Process Test Mode)** | 支持（Rust dev-dependency） | 未公开说明 | 支持（Python `@mock_aws` 装饰器） | 未公开说明 |
| **资源占用与开销 (Footprint)** | 官方 Docker 指南建议上限为 2 GiB | 未公开说明 | 未公开说明 | 空闲约 13 MiB，启动约 24 ms（官方自测数据） |
| **是否公开发布保真度评分 (Published Fidelity Scores)** | 是，每版本同步发布 | 未公开说明 | 未公开说明 | 未公开说明 |

---

## AWS Emulator 目前有哪些局限性？

> ## What Are AWS Emulator’s Limitations?

正如 [官方文档](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html) 中明确指出的那样，目前该模拟器仍存在以下几项关键局限：

> As outlined plainly in the [official documentation](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html):

* **不进行真实 IAM 策略鉴权 (No IAM Evaluation)：** 模拟器不会按照真实的 AWS IAM 语义去严格计算和评估身份权限与资源策略。**切勿将其用于安全审计或权限校验测试。**
* **单一区域与单账户模式 (Single Region & Account)：** 尽管它允许传入任意格式的账号与区域 ID，但在内部并不会真正实现跨模拟账户或跨区域的资源隔离。
* **验证环境覆盖范围 (Verification Scope)：** 现阶段主要针对 `us-west-2` 区域进行严格验证，全局服务则在 `us-east-1` 区域完成比对。
* **纯内存驻留与短期运行 (In-Memory & Short-Lived)：** 其底层架构专为轻量级测试打造，并未针对长期常驻部署或高并发压力测试进行优化。建议配置 `--idle-timeout` 参数以实现空闲时自动退出。
* **默认开启遥测收集 (Telemetry Enabled by Default)：** 模拟器默认会收集使用遥测数据，开发者可以通过 `--telemetry off` 启动参数、设置 `EMULATOR_TELEMETRY=off` 环境变量、修改 `config.toml` 文件或调用内嵌 API 进行手动关闭。

> * **No IAM Evaluation:** Identity and resource policies are not evaluated according to actual AWS IAM semantics. **Do not use it for security or authorization testing.**
> * **Single Region & Account:** It accepts arbitrary IDs but does not isolate resources across simulated accounts or regions.
> * **Verification Scope:** Primarily verified against `us-west-2`, with global services verified in `us-east-1`.
> * **In-Memory & Short-Lived:** It is not engineered for long-running deployments or heavy load testing. Use `--idle-timeout` to handle automatic termination.
> * **Telemetry Enabled by Default:** Can be disabled via `--telemetry off`, the `EMULATOR_TELEMETRY=off` environment variable, `config.toml`, or through the embedded API.

值得关注的是，该项目目前正保持着极其迅猛的高频迭代节奏 —— 仅仅在 2026 年 11 月短短数天之内，版本号就已从 [v1.0.265 飞速迭代到了 v1.0.322](https://github.com/aws/aws-emulator/releases)。

> The project maintains an exceptionally rapid release cadence, with versions ranging from [v1.0.265 to v1.0.322](https://github.com/aws/aws-emulator/releases) shipping across just a few days in November 2026.

---

## 核心总结与要点归纳

> ## Key Takeaways

* AWS Emulator 提供了一个完全免费、遵循宽松 CC0 开源协议的本地云服务运行环境，全面覆盖了 200 余项 AWS 云服务。
* 自主运行的 AI 智能体 (AI Agent) 独立且成功地编写了全部工程代码，而人类工程师则负责搭建严谨完备的测试框架与代码合入安全门禁。
* 模拟器一经发布便具备了扎实的工程基础，在公开的 42,857 项保真度测试中成功通过了 56.6%。
* SQS、KMS 和 S3 等核心数据存储与通信服务的模拟表现尤为出色，而 CloudFormation 和 IoT 等复杂的控制编排平面则仍处于持续完善之中。
* 它非常契合开发者加速本地单机调试与 CI 自动化流水线验证的需求，但在现阶段切勿将其用于 IAM 权限安全审计或高压力负载测试。

> * AWS Emulator provides a free, CC0-licensed local replica covering over 200 AWS services.
> * Autonomous AI agents successfully authored the entire codebase, while human engineers established robust test frameworks and merge gates.
> * The emulator launches with a solid foundation, passing 56.6% of its 42,857 published fidelity tests.
> * Core data services like SQS, KMS, and S3 perform exceptionally well, whereas complex control planes like CloudFormation and IoT are still maturing.
> * It is ideally suited for accelerated local development and CI validation loops, but should not be relied upon for IAM security evaluations or load testing.

---

*欢迎前往 [GitHub 官方仓库](https://github.com/aws/aws-emulator) 探索项目源码、查阅 [用户指南文档](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html)、检视 [保真度评测套件](https://github.com/aws/aws-emulator-evaluation-suite)，并阅读 [官方工程发布公告](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator) 获取更多技术细节。*

> *Explore the [GitHub repository](https://github.com/aws/aws-emulator), read the [User Guide](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html), review the [fidelity test suites](https://github.com/aws/aws-emulator-evaluation-suite), and learn more via the [engineering announcement post](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator).*
