---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-06
hide:
- navigation
tags:
- Compiler Explorer
- AWS
- 架构设计
- 开源运维
title: 2026年 Compiler Explorer 如何在 AWS 上运行
---
# 2026年 Compiler Explorer 如何在 AWS 上运行

### 文章背景与核心概要
本文深入揭秘了知名在线代码编译工具 Compiler Explorer（godbolt.org）在 2026 年的 AWS 云端架构与运维细节。系统每月处理约 520 万次编译请求，支持 93 种编程语言和超过 6000 种编译器。通过巧用 CloudFront CDN、应用负载均衡器（ALB）、Spot 竞价实例、EFS/SquashFS 存储组合以及 GitHub Actions 自动化构建，其整体月度云资源成本控制在 3600 美元左右。文章展现了一个高并发、大吞吐且高性价比的现代开源基础设施范例。

---

*本文在大语言模型协助下撰写。*

> *Written with LLM assistance.*

## 概要

> ## Summary

本文深入探讨了 **Compiler Explorer** (godbolt.org) 2026 年在 Amazon Web Services (AWS) 上的幕后运行机制。该基础设施每月跨 93 种语言和 6000 多种编译器处理约 520 万次编译，极度依赖 CloudFront CDN、应用负载均衡器（ALB）、Spot EC2 实例、EFS/SquashFS 存储以及用于夜间构建的 GitHub Actions。尽管规模庞大，在开源额度、Patreon 和商业赞助支持下，整个架构每月的运行成本仅约为 3,600 美元。

> This article provides an in-depth, behind-the-scenes look at how **Compiler Explorer** (godbolt.org) operates on Amazon Web Services (AWS) in 2026. Processing roughly 5.2 million compilations a month across over 6,000 compilers and 93 languages, the infrastructure relies heavily on a robust mix of CloudFront CDNs, Application Load Balancers, Spot EC2 instances, EFS/SquashFS storage, and GitHub Actions for nightly builds. Despite its scale, the entire setup runs for about $3,600 a month—supported by open-source credits, Patreon, and commercial sponsors.

---

> ---

## 代码如何抵达我们的服务器

> ## Getting Your Code as Far as Our Servers

用户的浏览器首先与亚马逊 CDN 服务 **CloudFront** 通信，CloudFront 托管着两个独立的分发网络：
* **`godbolt.org`**：将请求传递给我们的负载均衡器，同时处理压缩和缓存。
* **`static.ce-cdn.net`**：分发较重的静态资源，例如编译好的 JavaScript、图像以及 **Monaco**（负责语法高亮的 VS Code 编辑器组件）。

> Your browser first talks to **CloudFront**, Amazon's CDN, which manages two separate distributions:
> * **`godbolt.org`**: Passes requests to our load balancer while handling compression and caching.
> * **`static.ce-cdn.net`**: Delivers bulky static assets like compiled JavaScript, images, and **Monaco** (the VS Code editor component responsible for syntax highlighting).

位于 CloudFront 前端的是 **WAF（Web 应用防火墙）**，它设置了较高的速率限制门槛，以防止误封共用单一 NAT 地址的 C++ 培训班或课堂。

> Sitting in front of CloudFront is **WAF (Web Application Firewall)**, handling rate limiting with high thresholds to prevent blocking C++ trainers and classrooms sharing a single NAT.

---

> ---

## 单个负载均衡器背后的众多集群

> ## Rather a Lot of Fleets Behind One Load Balancer

CloudFront 后方挂载着单个 **应用负载均衡器 (ALB)**，根据 URL 路径将流量路由到特定集群：
* **生产集群：** 处理绝大部分的核心流量。
* **`/beta*` 与 `/staging*`：** 用于预部署检查和实验性测试。
* **`/winprod*`：** 运行 **MSVC** 的 Windows 实例。
* **`/aarch64prod*`：** ARM64 **Graviton** 架构机器。
* **`/gpu*`：** 配备真实 NVIDIA 显卡的高端机器。

> Behind CloudFront sits a single **Application Load Balancer (ALB)**, which routes traffic to specific clusters based on URL paths:
> * **Production fleet:** Handles the overwhelming bulk of traffic.
> * **`/beta*` & `/staging*`:** Used for pre-deploy checks and experiments.
> * **`/winprod*`:** Windows instances running **MSVC**.
> * **`/aarch64prod*`:** ARM64 **Graviton** machines.
> * **`/gpu*`:** High-end machines equipped with real NVIDIA cards.

每个集群由采用蓝/绿部署模式的 **Auto Scaling Group（自动扩缩容组）** 支持。扩缩容根据平均 CPU 负载动态进行。

> Each fleet is backed by an **Auto Scaling Group** arranged in a blue/green deployment model. Scaling is handled dynamically based on average CPU loads.

---

> ---

## 租赁他人闲置的计算资源

> ## Renting the Bits Nobody Else Wants

生产集群几乎完全运行在 **EC2 Spot 实例** 上——这是以 60–90% 的折扣销售的闲置算力，并带有两分钟的收回预警。由于有状态的数据都保存在共享文件系统、S3 或 DynamoDB 中，因此任何被回收的实例都可以自动被新实例替换。

> The production fleet runs almost entirely on **EC2 spot instances**—unused capacity sold at a 60–90% discount with a two-minute eviction warning. Because stateful data lives on shared filesystems, S3, or DynamoDB, any evicted instance is simply replaced automatically.

---

> ---

## 为什么编译器才是最难的部分

> ## Why the Compilers Are the Hard Part

Compiler Explorer 大量囤积二进制文件以防止链接失效，目前管理着跨 93 种语言的约 6,000 个编译器。

> Compiler Explorer hoards binaries to prevent link rot, currently managing around 6,000 compilers across 93 languages. 

为了规避 Amazon 弹性文件系统（**EFS**）的延迟问题，编译器被存储为压缩的只读 **SquashFS** 镜像，并通过 loopback 设备挂载。此外，引入 **CEFS**（打成约 20GB 的内容寻址镜像包，通过 **autofs** 按需挂载）后，操作系统启动时间从 50 秒缩短到了 20 秒。

> To bypass the latency of Amazon's elastic NFS (**EFS**), compilers are stored as compressed, read-only **SquashFS** images mounted via loopback devices. Furthermore, the introduction of **CEFS**—content-addressed images packed into ~20GB bundles mounted on-demand via **autofs**—reduced OS startup times from 50 seconds to 20 seconds.

---

> ---

## 每晚不停歇地构建编译器

> ## Building Compilers All Night, Every Night

nightly 构建由 94 个自动化任务处理（包括 GCC trunk、Clang trunk 和各种实验性分支）。这些任务运行在通过 `terraform-aws-github-runner` 工具按需托管在 **EC2** 上的 **GitHub Actions** runner 上。

> Nightly builds are handled by 94 automated jobs (including GCC trunk, Clang trunk, and various experimental branches). These run on **GitHub Actions** runners hosted on demand via **EC2**, utilizing the `terraform-aws-github-runner` tool.

---

> ---

## 尚未完全完工的架构组件

> ## The Bits That Are Half-Finished

**CE Router** 是一个最新研发的集群，旨在解耦传入的 HTTP 请求与编译器节点：
1. 路由器在 **DynamoDB** 中查找编译任务。
2. 将请求投递至 **SQS 队列**。
3. 编译结果通过 **API Gateway WebSockets** 实时流式返回。

> The **CE Router** is a newly developed fleet designed to decouple incoming HTTP requests from the compiler nodes:
> 1. A router looks up the compilation task in **DynamoDB**.
> 2. It drops the request onto an **SQS queue**.
> 3. Results are streamed back via **API Gateway WebSockets**.

*(注：尽管功能已完备，但生产流量目前仍处于向该管道迁移的过程中。)*

> *(Note: While functional, production traffic is still migrating to this pipeline).*

---

> ---

## 其他所有的 AWS 组件配套

> ## Everything Else: The AWS Plumbing

* **DynamoDB：** 存储数以百万计的短链接（`godbolt.org/z/...`）。
* **S3：** 存储构建好的编译器、静态资源、日志以及每日过期的编译缓存。
* **Lambda：** 驱动辅助任务，例如 *Claude Explain* 后端和 Discord CloudWatch 报警。
* **Route 53, ACM, CloudTrail, Backup, & SES：** 处理 DNS、TLS 证书、审计和备份。
* **CloudWatch, Grafana, Prometheus, & Loki：** 驱动指标监控、日志收集和公开仪表盘。

> * **DynamoDB:** Stores millions of short links (`godbolt.org/z/...`).
> * **S3:** Holds built compilers, static assets, logs, and a daily-expiring compilation cache.
> * **Lambda:** Powers odd jobs like the *Claude Explain* backend and Discord CloudWatch alerts.
> * **Route 53, ACM, CloudTrail, Backup, & SES:** Handle DNS, TLS certificates, auditing, and backups.
> * **CloudWatch, Grafana, Prometheus, & Loki:** Drive metrics, logging, and public dashboards.

所有基础设施均部署在 **`us-east-1`** 区域，以避免在全球范围内同步数 TB 编译器数据的复杂噩梦。

> All infrastructure resides in **`us-east-1`** to avoid the synchronization nightmare of managing terabytes of compilers globally.

---

> ---

## 数据一览

> ## By the Numbers

* **编译次数（7月）：** 5,238,210 次
* **编译次数（过去 12 个月）：** 7,870 万次
* **每月 AWS 成本：** ~$3,600（每次编译约 $0.0007）
* **最受欢迎的编译器：** GCC 16.1 (C++) 占据了总流量的 26%。

> * **Compilations (July):** 5,238,210
> * **Compilations (Trailing 12 Months):** 78.7 million
> * **Monthly AWS Cost:** ~$3,600 (~$0.0007 per compilation)
> * **Most Popular Compiler:** GCC 16.1 (C++) accounts for 26% of all traffic.

---

> ---

## 我依然想要解决的问题

> ## Things I’d Still Like to Fix

* 简化编译器发现与部署流水线。
* 全面推广 CE Router 架构迁移。
* 整理解开已有十年历史的 NFS 目录结构。

> * Streamlining the compiler discovery and deployment pipeline.
> * Fully rolling out the CE Router migration.
> * Untangling a decade-old NFS directory structure.

---

> ---

## 致谢

> ## Thanks

非常感谢 **Partouf (Patrick Quist)**、核心开发团队、开源贡献者、**AWS**（感谢其更新的开源资助计划），以及我们在 **Patreon**、**GitHub Sponsors** 和商业赞助上的慷慨支持者。

> A massive thank you to **Partouf (Patrick Quist)**, the core development team, open-source contributors, **AWS** (for their renewed open-source credits program), and our generous supporters on **Patreon**, **GitHub Sponsors**, and commercial backers.

---

> ---

## 免责声明

> ## Disclaimer

*本文由人类与 [LLM](https://anthropic.com) 协作完成。LLM 翻阅了基础设施仓库、获取了最新的 AWS 数据、运行了 Athena 查询并重新生成了图表。文中的观点、破折号的使用以及错误均由我个人承担。*

> *This article was a collaboration between a human and an [LLM](https://anthropic.com). The LLM dug through infrastructure repositories, fetched current AWS numbers, ran Athena queries, and regenerated graphs. The opinions, em- and en-dashes, and mistakes are all mine.*

---

> ---

## 脚注

> ## Footnotes

[^1]: 其他干扰因素包括在英国的家庭事务、密集的 C++ 会议演讲（C++Now, ACCU on Sea, CppCon, C++ Under the Sea 以及在柏林举行的 Meeting C++）、Computerphile 视频制作以及解码 PAL 视频信号。

> [^1]: Other distractions included family matters in the UK, a heavy run of C++ conference talks (C++Now, ACCU on Sea, CppCon, C++ Under the Sea, and Meeting C++ in Berlin), Computerphile videos, and decoding PAL video signals.

[^2]: Brotli 压缩技术已于 6 月在边缘节点启用。

> [^2]: Brotli compression was enabled at the edge in June.

[^3]: WAF 使用自定义的 IPv4 和 IPv6 黑名单，偶尔用于处理恶意爬虫或免费算力滥用者。

> [^3]: WAF utilizes custom IPv4 and IPv6 blocklists to occasionally manage malicious scrapers or free-compute abusers.

[^4]: Beta 环境用于长期实验；staging 用于部署前检查。

> [^4]: Beta environments handle long-term experiments; staging handles pre-deploy checks.

[^5]: GPU 实例虽然昂贵，但在 NVIDIA 的帮助下可以实现 GPU 代码的实时测试。

> [^5]: GPU instances are expensive but enable live testing of GPU code with help from NVIDIA.

[^6]: 未来的扩缩容策略将考虑队列深度（`ApproximateNumberOfMessagesVisible`），而不仅仅是 CPU 负载。

> [^6]: Future scaling policies will factor in queue depth (`ApproximateNumberOfMessagesVisible`) rather than CPU load alone.

[^7]: 已发布的编译器版本将永久保留；只有 nightly 构建版本会被替换。

> [^7]: Released compiler versions stay permanently; only nightly builds are superseded.

[^8]: 内容寻址技术允许自动垃圾回收孤立或被替换的编译器镜像。

> [^8]: Content-addressing allows automatic garbage collection of orphaned or superseded compiler images.

[^9]: API 通过将多语言编译器套件（例如用于 C、C++ 和 Fortran 的 GCC）分别计数来报告 6,157 个条目；独立名称总计为 4,291 个。

> [^9]: The API reports 6,157 entries by counting multi-language compiler suites (e.g., GCC for C, C++, and Fortran) separately; unique names total 4,291.

[^10]: 通过回环挂载的 SquashFS 镜像通过允许内核读取缓存的本地块数据，绕过了 NFS 延迟开销。

> [^10]: Loopback-mounted SquashFS images bypass NFS latency overhead by letting the kernel read cached local block data.

[^11]: 构建任务在 UTC 午夜启动，而安装发生在上午 5:30，偶尔会导致昨天的构建被部署的不匹配情况。

> [^11]: Jobs kick off at midnight UTC while installations happen at 5:30 AM, occasionally leading to a mismatch where yesterday's build is deployed.

[^12]: 构建脚本会检查上游仓库的每周提交，完全跳过未更改的分支。

> [^12]: Build scripts check upstream repositories for weekly commits, skipping unchanged branches entirely.

[^13]: 默认的自动重新编译延迟时间已逐步增加至 2000 毫秒，以减少冗余的构建触发。

> [^13]: Default auto-recompile delay was incrementally increased to 2000ms to reduce redundant build triggers.

[^14]: 由于总流量较低但固定存储成本保持不变，每次编译的成本略有上升。

> [^14]: Cost per compilation rose slightly due to lower overall volume against fixed storage costs.

[^15]: 默认编译器在总体使用中一直占据主导地位（例如 Clang++ 3.0.6 在 2014 年占据 37%；如今 GCC 16.1 占据 26%）。

> [^15]: Default compilers have always dominated usage (e.g., Clang++ 3.0.6 commanded 37% in 2014; GCC 16.1 commands 26% today).

[^16]: 编译器发现是指查询二进制文件的自我报告标识并写入 JSON 的步骤。

> [^16]: Compiler discovery is the step where binaries are queried for their self-reported identities and written to JSON.

[^17]: 升级到 Ubuntu 24.04 需要将较旧的编译器链接器 (`ld`) 符号链接到较新的 binutils，以绕过 `SHT_RELR` 重定位问题。

> [^17]: Upgrading to Ubuntu 24.04 required symlinking older compiler linkers (`ld`) to newer binutils to bypass `SHT_RELR` relocation issues.
