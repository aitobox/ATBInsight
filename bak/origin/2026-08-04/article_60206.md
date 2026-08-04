# This Week in Package Management: 11 July 2026

*Week eight of the package management roundup, curated from the [package manager OPML feed collection](https://github.com/ecosyste-ms/package-managers-opml) and posts/boosts on [Mastodon](https://mastodon.social/@andrewnez).*

---

## 📌 Summary

This week's roundup highlights major version releases across the ecosystem—including strict default settings in **npm 12**, security patches for **opam** and **pnpm**, and new caching and config improvements in **Rust 1.97.0**. Key discussions focus on immutable versions on Packagist, limitations of Trusted Publishing, and a proposed transparency log for PyPI by Trail of Bits.

---

## 🚀 Releases

*   **[npm 12.0.0](https://github.com/npm/cli/releases/tag/v12.0.0):** Introduces breaking changes. `allow-git` and `allow-remote` now default to `none`, requiring explicit opt-ins for git dependencies or remote tarballs. `npm shrinkwrap` has been removed, unknown `.npmrc` keys/flags now throw errors, root `preinstall` runs prior to dependency installation, and commands like `npm adduser`, `star`, and `unstar` are deprecated/removed.
*   **[pnpm 11.10 & 11.11.0](https://pnpm.io/blog/releases/11.10):** Adds an `_auth` setting for simplified CI registry credentials, alongside new commands like `pnpm prefix`, `pnpm issues`, and `pnpm access`. `allowBuilds` now supports matching via repository URLs without pinning commit hashes. *(Version 11.11.0 also includes critical security patches).*
*   **[uv 0.11.28](https://github.com/astral-sh/uv/releases/tag/0.11.28):** Hardens ZIP handling against parser differentials via `astral-async-zip`. Preceded by **0.11.27**, which brought significant resolver performance upgrades.
*   **[Go 1.26.5 & 1.27rc2](https://go.dev/doc/devel/release#go1.26.5):** A security release patching issues in `crypto/tls` and `os`, alongside general compiler and runtime fixes.
*   **[Rust 1.97.0](https://blog.rust-lang.org/2026/07/09/Rust-1.97.0/):** Stabilises `resolver.lockfile-path` in Cargo config for external lockfiles and `build.warnings` to turn warnings into errors without invalidating the build cache.
*   **[winget 1.29](https://github.com/microsoft/winget-cli/releases/tag/v1.29.280):** Introduces an experimental source priority feature for package search resolution.
*   **[Spack 1.2.1](https://github.com/spack/spack/releases/tag/v1.2.1):** Fixes installer hangs under `forkserver` and restores macOS solver performance.
*   **[CocoaPods 1.17.0](https://github.com/CocoaPods/CocoaPods/releases/tag/1.17.0):** Adds `--no-lint` to `pod repo push` and updates `ruby-macho` for mergeable libraries.
*   **[Hex 2.5.1](https://github.com/hexpm/hex/releases/tag/v2.5.1):** Adds `ignore_advisories` and `ignore_retirements` configurations to `mix.exs` and environment variables.
*   **[mise 2026.7.4 & 2026.7.5](https://github.com/jdx/mise/releases/tag/v2026.7.4):** Graduates `mise bootstrap` and `mise dotfiles` out of experimental mode and shares config trust across git worktrees.

**Other Notable Releases:** 
[Homebrew 6.0.9](https://github.com/Homebrew/brew/releases/tag/6.0.9), [RubyGems / Bundler 4.0.16](https://blog.rubygems.org/2026/07/10/4.0.16-released.html), [Cargo 0.98.0](https://github.com/rust-lang/cargo/releases/tag/0.98.0), [asdf 0.20.0](https://github.com/asdf-vm/asdf/releases/tag/v0.20.0), [Hatch 1.17.1](https://github.com/pypa/hatch/releases/tag/hatch-v1.17.1), [pixi 0.72.2](https://github.com/prefix-dev/pixi/releases/tag/v0.72.2), [Yarn 4.17.1](https://github.com/yarnpkg/berry/releases/tag/%40yarnpkg%2Fcli%2F4.17.1), [Deno 2.9.2](https://github.com/denoland/deno/releases/tag/v2.9.2), [Helm 4.2.3 / 3.21.3](https://github.com/helm/helm/releases/tag/v4.2.3), [Podman 6.0.1](https://github.com/podman-container-tools/podman/releases/tag/v6.0.1), [Nix 2.34.8](https://github.com/NixOS/nix/releases/tag/2.34.8), [Gradle 9.7.0-M3](https://github.com/gradle/gradle/releases/tag/v9.7.0-M3), [Maven 3.10.0-rc-1](https://github.com/apache/maven/releases/tag/maven-3.10.0-rc-1), [Renovate 43.258.0](https://github.com/renovatebot/renovate/releases/tag/43.258.0), and [Dependabot Core 0.385.0](https://github.com/dependabot/dependabot-core/releases/tag/v0.385.0).

---

## 🔒 Security Advisories

*   **[opam 2.5.2](https://github.com/ocaml/opam/releases/tag/2.5.2):** Fixes **CVE-2026-57825**, preventing packages from installing files arbitrarily via symlinks to external directories, bypassing user prompts.
*   **pnpm ([11.11.0 / 10.34.5](https://github.com/pnpm/pnpm/releases/tag/v11.11.0)):** Fixes two critical path traversal vulnerabilities preventing crafted lockfiles and malicious package manifests from writing outside target directories (`node_modules` and virtual stores).
*   **[ORAS 1.3.3](https://github.com/oras-project/oras/releases/tag/v1.3.3):** Updates to oras-go 2.6.2 to patch **[GHSA-fxhp-mv3v-67qp / CVE-2026-50163](https://github.com/advisories/GHSA-fxhp-mv3v-67qp)**, preventing crafted OCI artifacts from linking into host files during `oras pull`.

---

## 📝 Articles & Opinions

*   **[Immutable Versions on Packagist](https://blog.packagist.com/immutable-versions-on-packagist/)** *(Packagist Blog)*: Details the latest supply chain security upgrades for Composer. Stable versions now lock their git references, blocking retag attempts and turning deletions into soft deletes with transparency logs.
*   **[You shouldn’t trust Trusted Publishing](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing)** *(William Woodruff)*: Argues that Trusted Publishing is strictly an authentication mechanism between CI systems and registries, not an indicator of package safety.

---

## 🌐 Elsewhere in the Ecosystem

*   **PyPI Transparency Logs:** Trail of Bits published [a transparency log proposal](https://pytransparency.dev/) featuring an append-only log of served distribution files to detect index-level tampering. Includes a [draft PEP](https://github.com/trailofbits/pypi-transparency/blob/main/peps/pep-xxxx.rst) and [source code](https://github.com/trailofbits/pypi-transparency).
*   **EuroPython 2026 Packaging Summit:** The schedule for July 13 in Kraków is live, alongside [public notes](https://hackmd.io/@jezdez/europython2026-packaging-summit).
*   **Rust Foundation Maintainers Fund:** Josh Bressers hosts [a podcast discussion](https://opensourcesecurity.io/2026/2026-07-rfmf-lori-niko/) with Lori Lorusso and Niko Matsakis on maintenance funding structures.
*   **Nix Documentation Team:** The Nix Foundation is [fundraising via Open Collective](https://nixos.org/blog/announcements/2026/docs-funding-2026/) to hire dedicated contributors for user onboarding and reference materials.
*   **Git 2.55:** Highlights include `git history fixup <commit>` for streamlined commits, incremental multi-pack index repacking, and native Linux inotify monitoring.
*   **SBOM Completeness Study:** A new academic paper, [*Beyond Compliance: A Large Scale Study on the Completeness and Consistency of the GitHub SBOMs*](https://arxiv.org/abs/2607.04614) (Bhuiyan et al.), highlights language-specific gaps in auto-generated SBOM reliability.

---

## 📦 git-pkgs Releases

Six repositories were tagged this week:
*   [brief v0.9.3](https://github.com/git-pkgs/brief/releases/tag/v0.9.3)
*   [enrichment v0.6.0](https://github.com/git-pkgs/enrichment/releases/tag/v0.6.0)
*   [purl v0.1.14](https://github.com/git-pkgs/purl/releases/tag/v0.1.14)
*   [sarif v0.1.0](https://github.com/git-pkgs/sarif/releases/tag/v0.1.0)
*   [sbom v0.1.3](https://github.com/git-pkgs/sbom/releases/tag/v0.1.3)
*   [vulns v0.2.0](https://github.com/git-pkgs/vulns/releases/tag/v0.2.0)

---

*Got links or releases for next week? Send them to [@andrewnez@mastodon.social](https://mastodon.social/@andrewnez).*