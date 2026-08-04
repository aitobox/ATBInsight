# Unboxed: Zig

## Summary

This post is the first in a series analyzing individual package managers against a standardized set of criteria covering client design, registry architecture, governance, and threat models. 

Zig’s built-in package manager eliminates central registries in favor of source-host distribution, using content hashes as immutable package identifiers via `build.zig.zon` manifests. While this approach offers strong reproducibility and avoids central governance bottlenecks, it creates unique challenges: the bespoke Zig Object Notation (`.zon`) format requires custom cross-ecosystem parsers, Turing-complete build scripts fail the "Tuesday test" for secure installations, and the absence of a transitive override mechanism complicates security patching.

---

## Overview

Zig’s package manager has been built into the `zig` binary since [0.11 in August 2023](https://ziglang.org/download/0.11.0/release-notes.html#Package-Management), operating without a separate tool or central registry. A `build.zig.zon` file lists dependencies as URLs with content hashes, and `zig build` fetches and compiles everything together. Both the language and the tool are managed by the [Zig Software Foundation](https://ziglang.org/zsf/), a 501(c)(3) non-profit.

---

## How it Works

A Zig project typically contains two core files at its root:
1. `build.zig`: Arbitrary Zig code compiled and executed to describe targets, compile flags, and link dependencies.
2. `build.zig.zon`: Inert metadata and dependency data that can be parsed without executing code.

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

* **ZON (Zig Object Notation):** A subset of Zig’s syntax restricted to literals and anonymous structs, lacking expressions, imports, or function calls (see the [specification](https://github.com/ziglang/zig/blob/master/lib/std/zon.zig)).
* **Fingerprint:** A 64-bit integer combining a random 32-bit ID with a checksum of the package name, acting as a permanent identity independent of URLs.
* **Content Addressing:** Hashes are computed over extracted files *after* applying the `.paths` inclusion list. As the documentation notes: *"packages do not come from a `url`; they come from a `hash`. `url` is just one of many possible mirrors."*
* **Build Integration:** `zig build` compiles `build.zig` alongside every dependency's build script into a single executable, meaning transitive dependencies run in the same process rather than separate subprocesses.

---

## Categorisation

### Client

* **Resolution Algorithm:** None. Each manifest pins exact content hashes with no version ranges, aligning closest to the [explicit-dependencies bucket](https://nesbitt.io/2025/12/29/categorizing-package-manager-clients.html#resolution-algorithms) (like Nix or Guix), albeit without a content-addressed store.
* **Lockfile:** The manifest *is* the lock file (`build.zig.zon`), pinning content hashes recursively. Reproducible without a separate lockfile, akin to Go.
* **Build Hooks:** Allowed. `build.zig` executes code at build time, similar to Cargo’s `build.rs` or Swift’s `Package.swift`.
* **Tuesday Test:** [Fails](https://nesbitt.io/2026/04/15/the-tuesday-test.html). Installs can observe undeclared inputs because `build.zig` is Turing-complete.
* **Manifest Format:** Custom for metadata (`.zon`), host language for build logic (`build.zig`). Because `.zon` is bespoke, cross-ecosystem tools like [ecosyste.ms](https://ecosyste.ms) and [git-pkgs](https://github.com/git-pkgs) must implement custom parsers.

### Registry

* **Architecture:** [Source host as registry](https://nesbitt.io/2025/12/29/categorizing-package-registries.html#registry-architecture), alongside Go modules and Deno. No central index; packages are served directly as tarballs or git refs.
* **Review Model:** None. Whosoever controls the URL controls the payload.
* **Namespacing:** URL-based location, paired with a self-generated 64-bit fingerprint for identity.
* **Distribution Model:** Source-only, compiled on the client.
* **Ecosystem Scope:** Language-specific, though C/C++ libraries are frequently packaged as Zig dependencies via `zig cc`.
* **Version Retention:** Delegated entirely to the source host (e.g., GitHub releases). There is no native package yank mechanism.

---

## Governance

The [Zig Software Foundation](https://ziglang.org/zsf/) governs the language and toolchain, but package hosting and namespacing fall completely outside its remit. 

Name ownership is decentralised and enforced only by social convention around the `fingerprint` field. Abuse handling, availability, account recovery, and DMCA takedowns are deferred entirely to the source host (overwhelmingly GitHub). As Loris Cro of the ZSF stated in 2022, ["we don’t plan to create an official package index."](https://kristoff.it/blog/zig-self-hosted-now-what/)

---

## Comparisons

* **Go Modules & Deno (Pre-JSR):** Closest architectural relatives—URL-addressed source, no publish step, no central registry, and integrity verified via content hash.
* **Bazel (`http_archive`):** Uses a URL list plus a SHA-256 hash where the hash is the identity and URLs are interchangeable mirrors, evaluating a hermetic Starlark build file.
* **Missing Features:** Unlike Cargo (`[patch]`) or Go (`replace`), Zig lacks a native manifest-level dependency override mechanism. While a `--fork` CLI flag exists, it leaves no record in the committed repository, complicating reproducible builds when patching transitive dependencies.

---

## Threat Model

### Client

* **Code Execution at Install Time:** `zig build --fetch` executes no untrusted code—it downloads URLs, verifies hashes, and parses `.zon` files as pure data. However, `zig build` compiles and runs dependency build scripts (`build.zig`) with user privileges during the build phase.
* **Lockfile Guarantees:** Manifests pin SHA-256 hashes, ensuring deterministic builds post-fetch. However, there is no public transparency log (unlike Go's checksum database) to verify what a URL served the moment a hash was first recorded.
* **Dependency Confusion:** Mitigated by design, as each dependency entry maps directly to a single explicit URL.

### Registry

* **Maintainer Lifecycle:** Handled via upstream source host permissions (e.g., GitHub collaborators). Compromised source repositories or lapsed custom domains can result in supply chain takeovers, mitigated only by existing hash pins in downstream manifests.
* **Immutability:** Git tags can be force-pushed or GitHub release assets replaced; clients receive the bytes they pinned, but new consumers risk pulling modified payloads if upstream tags change.

### The Tool’s Own Supply Chain

The Zig compiler's [own manifest](https://github.com/ziglang/zig/blob/master/build.zig.zon) declares zero external dependencies. Network operations, TLS stacks, and decompressors ship as Zig source code compiled in `ReleaseSafe` mode, allowing developers to inspect and patch networking logic without rebuilding the core compiler binary.

---

## Conclusion

Zig’s approach—treating the content hash as the true package identity while treating URLs as mere mirrors—is conceptually sound, and keeping `.zon` as pure data allows safe parsing of dependency graphs. Furthermore, the compiler's zero-dependency footprint sets an exemplary supply chain standard.

However, the bespoke `.zon` format imposes parsing overhead on cross-ecosystem tooling, and Turing-complete build scripts prevent the ecosystem from passing the "Tuesday test." By offloading governance entirely to GitHub, the ecosystem inherits external dependencies on account recovery and abuse handling, while the current lack of transitive dependency overrides makes emergency security patching cumbersome for developers.