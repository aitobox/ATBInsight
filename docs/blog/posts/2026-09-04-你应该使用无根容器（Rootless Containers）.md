---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-04
hide:
- navigation
tags:
- Docker
- Podman
- 容器安全
- 无根容器
- Linux
title: 你应该使用无根容器（Rootless Containers）
---
### 文章背景与核心概要
传统的 Docker 安装严重依赖于客户端-服务器架构，其中后台守护进程以 root 权限运行。这种设计引入了严重的安全风险，特别是当用户为了图方便将自己加入 `docker` 组时，会无意中为未经身份验证的 root 提权攻击敞开大门。为了缓解这些风险，开发者应当转向无根容器（Rootless Containers）替代方案，例如**无根 Docker（Rootless Docker）**或者更好、完全无守护进程并在常规用户权限下运行的 **Podman**。

本文深入剖析了传统 Docker 架构背后的安全隐患，并通过实际示例展示了普通用户将自己加入 `docker` 组后如何轻易绕过系统权限限制。同时，文章对比了不同操作系统（如 macOS、Windows 与 Linux/WSL）上的风险差异，并介绍了转向 Podman 等无根容器带来的优势、使用中的注意事项（如镜像源指定、持久化重启及 API 交互）以及最终的实践建议。

---

## 你应该使用无根容器（Rootless Containers）

> ## You Should Be Using Rootless Containers

## 摘要

传统的 Docker 安装依赖于客户端-服务器架构，其中的后台守护进程以 root 权限运行。这种设计引入了严重的安全性风险，尤其是当用户为了方便而将自己加入 `docker` 组时，会无意中为未经身份验证的 root 提权攻击打开大门。为了缓解这些风险，开发人员应该过渡到无根容器替代方案，例如 **Rootless Docker**，或者最好是完全无守护进程并在普通用户权限下运行的 **Podman**。

> ## Summary
> Traditional Docker installations rely on a client-server architecture where a background daemon runs with root privileges. This design introduces severe security risks, particularly when users add themselves to the `docker` group for convenience, inadvertently opening the door to unauthenticated root escalation attacks. To mitigate these risks, developers should transition to rootless container alternatives like **Rootless Docker** or, preferably, **Podman**, which operates entirely daemonless and under regular user permissions.

---

## Docker 的问题所在

> ## The Problem with Docker

Docker 的安全挑战源于其初创时期的架构选择。在标准安装中，Docker 守护进程作为 `root` 用户在后台运行，通过 Docker 套接字（socket）响应来自 `docker-cli` 等客户端的请求。

> The security challenges with Docker stem from architectural choices made at its inception. On a standard installation, the Docker daemon runs in the background as the `root` user, serving requests from clients like `docker-cli` via the Docker socket. 

由于守护进程具有 root 权限，任何获取其访问权限的攻击者或配置错误的脚本，都可以在宿主机系统上以完整的 root 权限执行代码。

> Because the daemon runs with root privileges, any attacker—or misconfigured script—that gains access to it can execute code with full root permissions on the host system.

虽然默认的 Docker 安装通过严格限制 `docker` 命令只能由 `root` 用户使用（需要 `sudo`）来缓解这一问题，但用户为了图方便，经常会将自己加入 `docker` 组来放宽这些权限。正如以下示例所示，这会造成一个重大的安全隐患：

> While a default Docker installation mitigates this by restricting the `docker` command strictly to the `root` user (requiring `sudo`), users frequently relax these permissions for convenience by adding themselves to the `docker` group. As demonstrated below, this creates a major security hazard:

```bash
# As a regular user, the following command fails
$ ls /etc/sudoers.d/
ls: cannot open directory '/etc/sudoers.d/': Permission denied

# But with Docker, we can bypass restrictions instantly without a password! 
$ docker run -v /:/host alpine:latest ls /host/etc/sudoers.d/
90-cloud-init-users
README
```

在此示例中，`docker run` 将宿主机的整个文件系统挂载到了 Alpine Linux 容器内的 `/host` 目录下。由于该容器是通过 root 级别的 Docker 守护进程运行的，它完全绕过了用户权限限制，从而允许潜在的攻击者读取、修改或窃取敏感的系统文件。

> In this example, `docker run` mounts the host's entire filesystem under `/host` within an Alpine Linux container. Because the container runs via the root-level Docker daemon, it bypasses user restrictions completely, allowing potential attackers to read, modify, or exfiltrate sensitive system files.

### macOS 和 Windows 上的 Docker 怎么样？

> ### What About Docker on macOS and Windows?

Docker 无法在 macOS 或 Windows 上原生运行。相反，Docker Desktop 等产品通过虚拟化工具（如 QEMU 或 Hyper-V）使用轻量级 Linux 虚拟机（VM）。这产生了一个额外的隔离层，大大降低了对宿主机的直接风险。

> Docker does not natively run on macOS or Windows. Instead, products like Docker Desktop utilize a lightweight Linux virtual machine (VM) via virtualization tools (such as QEMU or Hyper-V). This creates an additional layer of separation, considerably reducing direct risks to the host. 

然而，**WSL (Windows Subsystem for Linux)** 是一个特例。由于 WSL 与操作系统深度集成，并在宿主机上直接运行 Linux 内核，因此它带来的风险更接近传统的 Linux 系统。

> However, **WSL (Windows Subsystem for Linux)** is a special case. Because WSL integrates tightly with the OS and runs the Linux kernel directly on the host, it carries risks closer to those of a traditional Linux system.

---

## 替代方案：无根容器

> ## The Alternative: Rootless Containers

为了消除 root 守护进程带来的漏洞，开发者可以采用无根容器平台。两个主要的选项包括：

> To eliminate root-daemon vulnerabilities, developers can adopt rootless container platforms. Two primary options include:

1. **Rootless 模式下的 Docker**：标准 Docker 的变体，其中守护进程作为用户级服务运行。（该设置需要对标准安装文件进行一些“拼凑式”的手动重新配置）。
2. **Podman**：一个完全无守护进程的容器平台，不需要任何后台服务。

> 1. **Docker in Rootless Mode**: A variation of standard Docker where the daemon runs as a user-level service. (The setup requires a slightly "hacky" manual reconfiguration of standard installation files).
> 2. **Podman**: A fully daemonless container platform that requires no background services.

切换到 Podman 非常直接。通过输入 `podman` 代替 `docker`（或者创建一个别名如 `alias docker=podman`），你的标准工作流可以保持基本不变，但所有容器都会在你的标准用户账号下安全执行，且没有进行 root 提权的途径。

> Switching to Podman is straightforward. By typing `podman` instead of `docker` (or by creating an alias like `alias docker=podman`), your standard workflows remain largely unchanged, but all containers execute safely under your standard user account with no path for root escalation.

---

## Podman 的代价（注意事项）

> ## The Catch with Podman

虽然 Podman 提供了更高的安全性，但放弃 Docker 也会带来一些取舍：

> While Podman offers superior security, transitioning away from Docker comes with a few trade-offs:

* **镜像仓库（Image Registries）：** 与默认使用 Docker Hub 的 Docker 不同，Podman 在未指定镜像来源时可能会失败。最佳实践是使用完全限定的镜像路径：
  ```bash
  podman pull docker.io/library/postgres
  ```
* **重启后的持久性：** 在没有后台守护进程的情况下，Podman 无法在系统重启后自动重启容器。为了维持 7x24 小时的服务，你必须使用诸如 `podman quadlet` 之类的命令与 `systemd` 进行集成。
* **API 交互：** 如果应用程序需要 Docker 兼容的 API 来与容器进行交互，你必须通过以下命令手动启动一个可选的用户级 API 服务：
  ```bash
  podman system service
  ```

> * **Image Registries:** Unlike Docker, which defaults to Docker Hub, Podman may fail if an image origin isn't specified. It is best practice to use fully qualified image paths:
>   ```bash
>   podman pull docker.io/library/postgres
>   ```
> * **Persistence After Reboots:** Without a background daemon, Podman cannot automatically restart containers after a system reboot. To maintain 24/7 services, you must integrate with `systemd` using commands like `podman quadlet`.
> * **API Interactions:** If applications require a Docker-compatible API to interact with containers, you must manually launch an optional user-level API service via:
>   ```bash
>   podman system service
>   ```

---

## 结论

> ## Conclusion

采用无根容器可以显著增强你的系统，以抵御提权漏洞。尽管像 **Podman** 和 **Podman Compose** 这样的工具需要进行微小的工作流调整——例如处理完全限定的镜像名称或为持久化服务配置 `systemd`——但其带来的安全效益远超这些不便之处。

> Adopting rootless containers significantly hardens your system against privilege-escalation vulnerabilities. While tools like **Podman** and **Podman Compose** require minor workflow adjustments—such as handling fully qualified image names or configuring `systemd` for persistent services—the security benefits heavily outweigh the inconvenience. 

如果你选择继续使用标准的 Docker，至关重要的是要在充分理解其固有的提权风险的前提下进行。然而，对于大多数开发和生产环境而言，转向无根（Rootless）设置才是推荐的前进方向。

> If you choose to stick with standard Docker, it is crucial to do so with a full understanding of the inherent root-escalation risks. For most development and production environments, however, moving to a rootless setup is the recommended path forward.