# 开箱：Zig

### 背景与摘要
本文是包管理器分析系列文章的第一篇，专门探讨 Zig 的内置包管理器。Zig 采用了一种去中心化的方式，不依赖中央注册表，而是直接基于源码托管平台和内容哈希（通过 `build.zig.zon` 文件）进行包分发。这种方法虽然保证了构建的强可重复性，但也带来了一些挑战，如自定义格式解析困难、图灵完备的构建脚本带来的安全隐患以及缺乏依赖覆盖机制等。总体而言，Zig 的包管理理念独特，但在生态系统的治理和安全补丁管理上仍有改进空间。

## Summary

本文是系列文章的第一篇，该系列根据涵盖客户端设计、注册表架构、治理和威胁模型的标准化标准，对各个包管理器进行分析。
> This post is the first in a series analyzing individual package managers against a standardized set of criteria covering client design, registry architecture, governance, and threat models. 

Zig 的内置包管理器摒弃了中央注册表，转而采用源主机分发方式，通过 `build.zig.zon` 清单将内容哈希作为不可变的包标识符。虽然这种方法提供了强大的可重复性并避免了中央治理瓶颈，但它也带来了独特的挑战：定制的 Zig 对象表示法 (`.zon`) 格式需要跨生态系统的自定义解析器，图灵完备的构建脚本无法通过安全安装的“星期二测试”，而且缺乏传递性覆盖机制使安全补丁变得复杂。
> Zig’s built-in package manager eliminates central registries in favor of source-host distribution, using content hashes as immutable package identifiers via `build.zig.zon` manifests. While this approach offers strong reproducibility and avoids central governance bottlenecks, it creates unique challenges: the bespoke Zig Object Notation (`.zon`) format requires custom cross-ecosystem parsers, Turing-complete build scripts fail the "Tuesday test" for secure installations, and the absence of a transitive override mechanism complicates security patching.

---

## Overview

自 2023 年 8 月的 [0.11 版本](https://ziglang.org/download/0.11.0/release-notes.html#Package-Management)起，Zig 的包管理器就内置在 `zig` 二进制文件中，无需单独的工具或中央注册表即可运行。`build.zig.zon` 文件将依赖项列为带有内容哈希的 URL，而 `zig build` 则将它们全部获取并编译在一起。该语言和工具均由 501(c)(3) 非营利组织 [Zig 软件基金会](https://ziglang.org/zsf/)管理。
> Zig’s package manager has been built into the `zig` binary since [0.11 in August 2023](https://ziglang.org/download/0.11.0/release-notes.html#Package-Management), operating without a separate tool or central registry. A `build.zig.zon` file lists dependencies as URLs with content hashes, and `zig build` fetches and compiles everything together. Both the language and the tool are managed by the [Zig Software Foundation](https://ziglang.org/zsf/), a 501(c)(3) non-profit.

---

## How it Works

Zig 项目通常在其根目录下包含两个核心文件：
> A Zig project typically contains two core files at its root:
1. `build.zig`: 编译和执行任意 Zig 代码，以描述目标、编译标志并链接依赖项。
> 1. `build.zig`: Arbitrary Zig code compiled and executed to describe targets, compile flags, and link dependencies.
2. `build.zig.zon`: 惰性元数据和依赖数据，无需执行代码即可解析。
> 2. `build.zig.zon`: Inert metadata and dependency data that can be parsed without executing code.

```zig
.{
    .name = .example,
    .version = "0.3.1",
    .fingerprint = 0x6a8091f57c7f07ff,
    .minimum_zig_version = "0.16.0",
    .dependencies = .{
        .known_folders = .{
            .url = "https://github.com/ziglibs/known-folders/archive/refs/tags/1.1.0.tar.gz",
            .hash = "known_folders-1.1.0-Fy-PJtnVAAC1Qq48Hf6_4er0Ku98mFvx99UUwo9-mrJd",
        },
        .tracy = .{
            .url = "git+https://github.com/wolfpld/tracy#v0.11.1",
            .hash = "N-V-__8AAKw3UgOhKDsrn8hRlOoGmVBl5x91fMi0WQwVaokf",
            .lazy = true,
        },
    },
    .paths = .{
        "build.zig",
        "build.zig.zon",
        "src",
        "LICENSE",
    },
}
```

* **ZON (Zig Object Notation):** Zig 语法的子集，仅限于字面量和匿名结构体，缺乏表达式、导入或函数调用（参见[规范](https://github.com/ziglang/zig/blob/master/lib/std/zon.zig)）。
> * **ZON (Zig Object Notation):** A subset of Zig’s syntax restricted to literals and anonymous structs, lacking expressions, imports, or function calls (see the [specification](https://github.com/ziglang/zig/blob/master/lib/std/zon.zig)).

* **Fingerprint:** 一个 64 位整数，结合了随机的 32 位 ID 和包名的校验和，作为独立于 URL 的永久身份。
> * **Fingerprint:** A 64-bit integer combining a random 32-bit ID with a checksum of the package name, acting as a permanent identity independent of URLs.

* **Content Addressing:** 在应用 `.paths` 包含列表后，对提取的文件计算哈希值。正如文档所指出的：“包不是来自 `url`；它们来自 `hash`。`url` 只是众多可能镜像中的一个。”
> * **Content Addressing:** Hashes are computed over extracted files *after* applying the `.paths` inclusion list. As the documentation notes: *"packages do not come from a `url`; they come from a `hash`. `url` is just one of many possible mirrors."*

* **Build Integration:** `zig build` 将 `build.zig` 与每个依赖项的构建脚本一起编译为一个可执行文件，这意味着传递依赖项在同一个进程中运行，而不是在单独的子进程中运行。
> * **Build Integration:** `zig build` compiles `build.zig` alongside every dependency's build script into a single executable, meaning transitive dependencies run in the same process rather than separate subprocesses.

---

## Categorisation

### Client

* **Resolution Algorithm:** 无。每个清单都固定确切的内容哈希，没有版本范围，这最接近[显式依赖模型](https://nesbitt.io/2025/12/29/categorizing-package-manager-clients.html#resolution-algorithms)（如 Nix 或 Guix），尽管没有内容寻址存储。
> * **Resolution Algorithm:** None. Each manifest pins exact content hashes with no version ranges, aligning closest to the [explicit-dependencies bucket](https://nesbitt.io/2025/12/29/categorizing-package-manager-clients.html#resolution-algorithms) (like Nix or Guix), albeit without a content-addressed store.

* **Lockfile:** 清单本身就是锁文件（`build.zig.zon`），它递归地固定内容哈希。无需单独的锁文件即可重现，类似于 Go。
> * **Lockfile:** The manifest *is* the lock file (`build.zig.zon`), pinning content hashes recursively. Reproducible without a separate lockfile, akin to Go.

* **Build Hooks:** 允许。`build.zig` 在构建时执行代码，类似于 Cargo 的 `build.rs` 或 Swift 的 `Package.swift`。
> * **Build Hooks:** Allowed. `build.zig` executes code at build time, similar to Cargo’s `build.rs` or Swift’s `Package.swift`.

* **Tuesday Test:** [未通过](https://nesbitt.io/2026/04/15/the-tuesday-test.html)。由于 `build.zig` 是图灵完备的，安装过程可能会出现未声明的输入。
> * **Tuesday Test:** [Fails](https://nesbitt.io/2026/04/15/the-tuesday-test.html). Installs can observe undeclared inputs because `build.zig` is Turing-complete.

* **Manifest Format:** 元数据采用自定义格式（`.zon`），构建逻辑采用宿主语言（`build.zig`）。由于 `.zon` 是定制的，像 [ecosyste.ms](https://ecosyste.ms) 和 [git-pkgs](https://github.com/git-pkgs) 这样的跨生态系统工具必须实现自定义解析器。
> * **Manifest Format:** Custom for metadata (`.zon`), host language for build logic (`build.zig`). Because `.zon` is bespoke, cross-ecosystem tools like [ecosyste.ms](https://ecosyste.ms) and [git-pkgs](https://github.com/git-pkgs) must implement custom parsers.

### Registry

* **Architecture:** [将源主机作为注册表](https://nesbitt.io/2025/12/29/categorizing-package-registries.html#registry-architecture)，与 Go modules 和 Deno 并列。没有中央索引；包直接作为 tarball 或 git ref 提供。
> * **Architecture:** [Source host as registry](https://nesbitt.io/2025/12/29/categorizing-package-registries.html#registry-architecture), alongside Go modules and Deno. No central index; packages are served directly as tarballs or git refs.

* **Review Model:** 无。无论谁控制了 URL，就控制了有效载荷。
> * **Review Model:** None. Whosoever controls the URL controls the payload.

* **Namespacing:** 基于 URL 的定位，并与自生成的 64 位指纹配对作为身份。
> * **Namespacing:** URL-based location, paired with a self-generated 64-bit fingerprint for identity.

* **Distribution Model:** 仅源代码，在客户端上编译。
> * **Distribution Model:** Source-only, compiled on the client.

* **Ecosystem Scope:** 语言特定，尽管 C/C++ 库经常通过 `zig cc` 打包为 Zig 依赖项。
> * **Ecosystem Scope:** Language-specific, though C/C++ libraries are frequently packaged as Zig dependencies via `zig cc`.

* **Version Retention:** 完全委托给源主机（例如，GitHub releases）。没有原生的包撤回机制。
> * **Version Retention:** Delegated entirely to the source host (e.g., GitHub releases). There is no native package yank mechanism.

---

## Governance

[Zig 软件基金会](https://ziglang.org/zsf/)负责管理语言和工具链，但包托管和命名空间完全超出了其职权范围。
> The [Zig Software Foundation](https://ziglang.org/zsf/) governs the language and toolchain, but package hosting and namespacing fall completely outside its remit. 

命名所有权是去中心化的，仅通过围绕 `fingerprint` 字段的社会约定来执行。滥用处理、可用性、账户恢复和 DMCA 删除完全推迟给源主机（绝大多数是 GitHub）。正如 ZSF 的 Loris Cro 在 2022 年所说：“[我们不打算创建官方的包索引。](https://kristoff.it/blog/zig-self-hosted-now-what/)”
> Name ownership is decentralised and enforced only by social convention around the `fingerprint` field. Abuse handling, availability, account recovery, and DMCA takedowns are deferred entirely to the source host (overwhelmingly GitHub). As Loris Cro of the ZSF stated in 2022, ["we don’t plan to create an official package index."](https://kristoff.it/blog/zig-self-hosted-now-what/)

---

## Comparisons

* **Go Modules & Deno (Pre-JSR):** 架构上最接近的亲属——URL 寻址的源、没有发布步骤、没有中央注册表，以及通过内容哈希验证的完整性。
> * **Go Modules & Deno (Pre-JSR):** Closest architectural relatives—URL-addressed source, no publish step, no central registry, and integrity verified via content hash.

* **Bazel (`http_archive`):** 使用 URL 列表加上 SHA-256 哈希，其中哈希是标识，URL 是可互换的镜像，评估一个密封的 Starlark 构建文件。
> * **Bazel (`http_archive`):** Uses a URL list plus a SHA-256 hash where the hash is the identity and URLs are interchangeable mirrors, evaluating a hermetic Starlark build file.

* **Missing Features:** 与 Cargo (`[patch]`) 或 Go (`replace`) 不同，Zig 缺乏原生的清单级依赖覆盖机制。虽然存在 `--fork` CLI 标志，但它在提交的存储库中没有留下记录，这使得在修补传递依赖项时的可重现构建变得复杂。
> * **Missing Features:** Unlike Cargo (`[patch]`) or Go (`replace`), Zig lacks a native manifest-level dependency override mechanism. While a `--fork` CLI flag exists, it leaves no record in the committed repository, complicating reproducible builds when patching transitive dependencies.

---

## Threat Model

### Client

* **Code Execution at Install Time:** `zig build --fetch` 不执行不受信任的代码——它下载 URL，验证哈希，并将 `.zon` 文件作为纯数据解析。但是，`zig build` 在构建阶段以用户权限编译和运行依赖构建脚本 (`build.zig`)。
> * **Code Execution at Install Time:** `zig build --fetch` executes no untrusted code—it downloads URLs, verifies hashes, and parses `.zon` files as pure data. However, `zig build` compiles and runs dependency build scripts (`build.zig`) with user privileges during the build phase.

* **Lockfile Guarantees:** 清单固定了 SHA-256 哈希，确保了获取后的确定性构建。但是，没有公共的透明度日志（不像 Go 的校验和数据库）来验证首次记录哈希时 URL 提供了什么内容。
> * **Lockfile Guarantees:** Manifests pin SHA-256 hashes, ensuring deterministic builds post-fetch. However, there is no public transparency log (unlike Go's checksum database) to verify what a URL served the moment a hash was first recorded.

* **Dependency Confusion:** 通过设计得到了缓解，因为每个依赖项条目直接映射到一个单一的显式 URL。
> * **Dependency Confusion:** Mitigated by design, as each dependency entry maps directly to a single explicit URL.

### Registry

* **Maintainer Lifecycle:** 通过上游源主机权限（如 GitHub 协作者）进行处理。受损的源库或过期的自定义域名可能导致供应链接管，这只能通过下游清单中现有的哈希固定来缓解。
> * **Maintainer Lifecycle:** Handled via upstream source host permissions (e.g., GitHub collaborators). Compromised source repositories or lapsed custom domains can result in supply chain takeovers, mitigated only by existing hash pins in downstream manifests.

* **Immutability:** Git 标签可以被强制推送，或者 GitHub release 资源被替换；客户端接收到他们固定的字节，但如果上游标签发生变化，新的消费者就有拉取到被修改的有效载荷的风险。
> * **Immutability:** Git tags can be force-pushed or GitHub release assets replaced; clients receive the bytes they pinned, but new consumers risk pulling modified payloads if upstream tags change.

### The Tool’s Own Supply Chain

Zig 编译器的[自身清单](https://github.com/ziglang/zig/blob/master/build.zig.zon)声明了零外部依赖。网络操作、TLS 堆栈和解压缩器均作为 Zig 源代码发布并在 `ReleaseSafe` 模式下编译，从而允许开发人员检查和修补网络逻辑而无需重新编译核心编译器二进制文件。
> The Zig compiler's [own manifest](https://github.com/ziglang/zig/blob/master/build.zig.zon) declares zero external dependencies. Network operations, TLS stacks, and decompressors ship as Zig source code compiled in `ReleaseSafe` mode, allowing developers to inspect and patch networking logic without rebuilding the core compiler binary.

---

## Conclusion

Zig 的方法——将内容哈希视为真正的包身份，而将 URL 仅视为镜像——在概念上是合理的，并且将 `.zon` 保持为纯数据允许安全地解析依赖图。此外，编译器的零依赖足迹树立了一个模范的供应链标准。
> Zig’s approach—treating the content hash as the true package identity while treating URLs as mere mirrors—is conceptually sound, and keeping `.zon` as pure data allows safe parsing of dependency graphs. Furthermore, the compiler's zero-dependency footprint sets an exemplary supply chain standard.

然而，定制的 `.zon` 格式给跨生态系统的工具带来了额外的解析开销，而图灵完备的构建脚本阻碍了生态系统通过“星期二测试”。通过将治理完全交给 GitHub，生态系统承担了依赖账户恢复和滥用处理的外部风险，同时目前缺乏传递依赖覆盖也让开发人员在进行紧急安全修补时变得十分繁琐。
> However, the bespoke `.zon` format imposes parsing overhead on cross-ecosystem tooling, and Turing-complete build scripts prevent the ecosystem from passing the "Tuesday test." By offloading governance entirely to GitHub, the ecosystem inherits external dependencies on account recovery and abuse handling, while the current lack of transitive dependency overrides makes emergency security patching cumbersome for developers.
