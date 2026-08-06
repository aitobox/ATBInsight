---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-06
hide:
- navigation
tags:
- 二进制分发
- Python Wheels
- Homebrew Bottles
- 容器镜像
- OCI
title: Wheels、Bottles 与容器镜像：二进制分发技术的演进与现状
---
# Wheels、Bottles 与容器镜像：二进制分发技术的演进与现状

### 文章背景与核心概要
在软件工程领域，Python **Wheels**、Homebrew **Bottles** 和 OCI **容器镜像**（Container Images）是三大主流的自助式二进制包分发系统。尽管它们各自在不同的技术生态中独立演进，但底层均采用了不可变、带校验和的文件制品，并通过客户端平台标签进行匹配选择。本文深度比较了这三种分发系统在元数据管理、依赖解析、回退机制上的异同，并剖析了将 OCI 注册表作为通用存储后端以及引入统一签名（Sigstore）与 GPU 硬件标签的最新技术趋势。

---

### 概要

本文探讨了三大主流自助式二进制分发系统的融合趋势：Python **Wheels**、Homebrew **Bottles** 和 OCI **容器镜像**。虽然这些系统是独立演进以服务于不同的技术生态系统，但它们共享一个基本架构：由客户端平台标签选择的不可变、带校验和的构建制品。文章审视了这些系统如何处理元数据、依赖解析，以及利用 OCI 注册表作为各种二进制格式通用存储后端的日益增长的趋势。

> This article explores the convergence of three major self-service binary distribution systems: Python **Wheels**, Homebrew **Bottles**, and OCI **Container Images**. While these systems evolved independently to serve different ecosystems, they share a fundamental architecture: immutable, checksummed artifacts selected by client-side platform tags. The piece examines how these systems handle metadata, dependency resolution, and the growing trend of using OCI registries as a universal storage backend for diverse binary formats.

---

### 共同点与技术交集

尽管来源各异，但这三种系统共享着相同的技术基石：

> Despite their different origins, these three systems share a common technical foundation:

* **内容寻址存储：** 三者均通过 HTTP 分发不可变、带校验和的文件（zip/tar.gz）。制品一旦发布便绝不修改，更新通过发布新版本来处理。
* **客户端匹配选择：** 客户端（pip、brew 或容器运行时）负责检查宿主环境，并根据平台标签（CPU、操作系统、ABI）选择合适的制品。
* **索引与存储解耦：** 索引（列出可用文件）与存储（托管文件）互相分离。这带来了极高的架构灵活性，例如从 Bintray 迁移到 GitHub Packages，或者通过简单的 HTTP 缓存进行镜像分发。
* **元数据打包：** 每种格式都捆绑了一个元数据文档（如 `.dist-info`、`INSTALL_RECEIPT.json` 或 OCI 配置对象），用于记录构建细节和来源出处。

> * **Content-Addressed Storage:** All three distribute immutable, checksummed files (zip/tar.gz) via HTTP. Once published, artifacts are never modified; updates are handled by shipping new versions.
> * **Client-Side Selection:** The client (pip, brew, or a container runtime) is responsible for inspecting the host environment and selecting the appropriate artifact based on platform tags (CPU, OS, ABI).
> * **Decoupled Indexing:** The index (which lists available files) is separate from the storage (which hosts the files). This allows for flexible infrastructure, such as moving from Bintray to GitHub Packages or mirroring via simple HTTP caches.
> * **Metadata Packaging:** Each format bundles a metadata document (e.g., `.dist-info`, `INSTALL_RECEIPT.json`, or the OCI config object) to record build details and provenance.

### 差异与技术分歧

这些系统之间的分歧源自它们具体的集成需求：

> The divergence between these systems stems from their specific integration requirements:

* **依赖模型：** Wheels 和 bottles 是依赖图谱的一部分；pip 和 brew 在安装前会解析这些树状依赖。OCI 镜像缺乏正式的依赖模型，而是依赖于层叠的图层（stacked layers）。
* **回退机制：** 当缺少预编译的二进制文件时，pip 和 brew 可以回退到从源码构建（sdist 或 formula）。OCI 镜像不支持这一点；如果没有发布特定平台的镜像，拉取操作就会失败。
* **宿主假设：** Wheel 假设存在特定的 Python 解释器和 libc；bottle 假设存在特定的操作系统和安装前缀；镜像则仅假设存在内核，并在其图层中打包了整个用户空间（userland）。

> * **Dependency Models:** Wheels and bottles are part of a dependency graph; pip and brew resolve these trees before installation. OCI images lack a formal dependency model, relying instead on stacked layers.
> * **Fallback Mechanisms:** When a pre-compiled binary is missing, pip and brew can fall back to building from source (sdist or formula). OCI images do not support this; if an image for a specific platform is not published, the pull fails.
> * **Host Assumptions:** A wheel assumes a specific Python interpreter and libc; a bottle assumes an OS and install prefix; an image assumes only a kernel, packing the entire userland within its layers.

### 融合趋势与未来展望

软件行业正在日益标准化地将 **OCI 注册表** 作为通用的存储层。Homebrew 已经转向将 bottles 存储在 OCI 注册表中，而像 ORAS 这样的工具允许在无需修改注册表端的情况下存储任意构建制品。

> The industry is increasingly standardizing around **OCI registries** as a universal storage layer. Homebrew has already moved to storing bottles in OCI registries, and tools like ORAS allow for the storage of arbitrary artifacts without registry-side changes.

**塑造未来发展的核心趋势：**

> **Key trends shaping the future:**

* **统一追溯证明：** 三种系统都在采用 **Sigstore** 进行构建证明认证，确保构建制品可以追溯验证至其源代码。
* **“GPU 差距”难题：** 现有的标签语法不足以应对现代硬件需求。诸如 Python 的 **PEP 817**（WheelNext）等倡议正在尝试解决根据 GPU、SIMD 层级和 BLAS 库进行变体选择的需求——这一挑战在容器世界中在很大程度上也尚未解决。
* **标准化走向：** 虽然分发中“Blob”的一端正通过 OCI 实现商品化与标准化，但“索引”一端依然保持碎片化。下一阶段的设计工作可能会集中在标准化标签语法和跨生态系统平台限定符（PURL）上，以消除这些虽然不同但功能相似的系统之间的鸿沟。

> * **Unified Provenance:** All three systems are adopting **Sigstore** for build attestations, ensuring that artifacts can be verified back to their source.
> * **The "GPU Gap":** Current tag grammars are insufficient for modern hardware. Initiatives like Python’s **PEP 817** (WheelNext) are attempting to address the need for variant selection based on GPUs, SIMD levels, and BLAS libraries—a challenge that remains largely unsolved in the container world as well.
> * **Standardization:** While the "blob" side of distribution is becoming commoditized through OCI, the "index" side remains fragmented. The next phase of design work will likely focus on standardizing tag grammars and cross-ecosystem platform qualifiers (PURL) to bridge the gap between these disparate but functionally similar systems.
