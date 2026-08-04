# This Week in Package Management: 18 July 2026

> **Summary:** Week nine of the package management roundup highlights major updates across ecosystems—including native changesets in `pnpm 11.13`, built-in vulnerability scanning (`brew vulns`) in Homebrew 6.0.11, critical security fixes in Docker Engine and sbt, and insightful discussions on supply chain stress, AI-driven dependency regeneration, and prompt injection attacks targeting AI coding agents via setup documentation.

---

## Releases

*   **[pnpm 11.13](https://github.com/pnpm/pnpm/releases/tag/v11.13.0)** introduces `pnpm change`, a native changesets-compatible release planner managing version bumping, dependent propagation, fixed groups, and per-package release lanes. It also adds `pnpm team` for registry and membership management, alongside a `versioning.epics` configuration tying package groups to a lead package. (Preceded by **[11.12](https://github.com/pnpm/pnpm/releases/tag/v11.12.0)**, which allows custom pnpmfile fetchers to delegate back to built-in ones portably).
*   **[Deno 2.9.3](https://github.com/denoland/deno/releases/tag/v2.9.3)** adds `deno add --no-save`, `--save-optional`, and introduces `--min-dep-age` as a shorthand alias for minimum-release-age checks.
*   **[pixi 0.73.0](https://github.com/prefix-dev/pixi/releases/tag/v0.73.0)** brings support for `{ workspace = true }` within environment `[dependencies]` tables, allowing shared versions to be declared once in `[workspace.dependencies]`.
*   **[uv 0.11.29](https://github.com/astral-sh/uv/releases/tag/0.11.29)** adds JSON output to `uv tree` and prioritizes local artifacts over URLs when installing from `pylock.toml`.
*   **[Verdaccio 6.8.0](https://github.com/verdaccio/verdaccio/releases/tag/v6.8.0)** fires notification webhooks on unpublish and single-version removal. Auth tokens are now safely decoupled from notification endpoints by restricting the object context to `name`, `groups`, and `real_groups`.
*   **[zizmor 1.27](https://docs.zizmor.sh/release-notes/#1270)** adds experimental support for auditing GitHub's new parallel steps pattern.
*   **[Rust 1.97.1](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/)** is a point release backporting an LLVM fix and disabling a previous IR change that increased miscompilation risks.
*   **[Homebrew 6.0.11](https://github.com/Homebrew/brew/releases/tag/6.0.11)** merges `brew vulns`, bringing built-in CVE scanning for installed formulae. Read more about [the work behind it](https://nesbitt.io/2026/07/17/plumbing-homebrew-into-the-vulnerability-ecosystem).

**Also out this week:** 
[npm 12.0.1](https://github.com/npm/cli/releases/tag/v12.0.1), [Athens 0.18.1](https://github.com/gomods/athens/releases/tag/v0.18.1), [vcpkg 2026-07-13](https://github.com/microsoft/vcpkg-tool/releases/tag/2026-07-13), [sbt 2.0.2](https://github.com/sbt/sbt/releases/tag/v2.0.2), [Nix 2.35.1](https://github.com/NixOS/nix/releases/tag/2.35.1), [mise 2026.7.10](https://github.com/jdx/mise/releases/tag/v2026.7.10), [pipx 1.16.0](https://github.com/pypa/pipx/releases/tag/1.16.0), [Gradle 9.7.0-RC1](https://github.com/gradle/gradle/releases/tag/v9.7.0-RC1), [Renovate 43.268.4](https://github.com/renovatebot/renovate/releases/tag/43.268.4), and [Dependabot Core 0.387.0](https://github.com/dependabot/dependabot-core/releases/tag/v0.387.0).

---

## Security

*   **[Docker Engine 29.6.2](https://github.com/moby/moby/releases/tag/docker-v29.6.2)** patches three vulnerabilities:
    *   [CVE-2026-15793](https://github.com/advisories/GHSA-hw3h-2gp9-cxpv): Git source checkout from bundle files leading to command injection.
    *   [CVE-2026-15792](https://github.com/advisories/GHSA-qx3x-mv6r-52p6): Incorrect parameters from BuildKit frontends causing a panic.
    *   [CVE-2026-15791](https://github.com/advisories/GHSA-32pv-7hq5-qhwj): LLB file operations improperly clearing `/tmp`.
*   **[sbt 1.12.14](https://github.com/sbt/sbt/releases/tag/v1.12.14)** backports the fix for [CVE-2026-26032](https://github.com/advisories/GHSA-j482-hm6j-v5jj) found in the bundled Apache Ivy `PackagerResolver`.

---

## Articles

*   **[crates.io: Development Update](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/)** (Tobias Bieniek, Rust Blog) — Highlights six months of progress, including a new Code tab on crate pages displaying exact files downloaded by `cargo`, decoupling accounts from GitHub logins, and completing the Svelte frontend migration.
*   **[Composer and Packagist Under Supply-Chain Stress](https://phpunit.expert/articles/composer-and-packagist-under-supply-chain-stress.html)** (Sebastian Bergmann) — Reviews how the PHP ecosystem navigated supply-chain pressures through 2025 and 2026, potential lessons from other registries, and infrastructure ownership.
*   **[My First Month as AI Security Engineer in Residence](https://rustfoundation.org/media/my-first-month-as-ai-security-engineer-in-residence-at-the-rust-foundation/)** (Jacob Finkelman, Rust Foundation) — Details the creation of a prioritized crate scanning database, initial runs with *Scrutineer*, and protocols for embargoing discovered bugs responsibly.

---

## Papers

*   **[Software Supply Chains are Dead: Use-Case-Oriented Regeneration](https://arxiv.org/abs/2607.13021)** (arXiv) — Examines how rising supply-chain security costs paired with cheap generative AI implementation are shifting paradigms, evaluating an agent workflow that synthesizes only the specific dependency slice an application actually calls.
*   **[Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/abs/2607.15143)** (Bagmar et al., arXiv) — Investigates package-install attacks embedded in project setup documentation. It shows how minor alterations to READMEs, requirements files, or Makefiles successfully trick AI coding agents into fetching packages from untrusted registries or installing vulnerable versions.
*   **[The Distributed Open-Source Vulnerability Ecosystem](https://arxiv.org/abs/2607.14900)** (Mandl et al., arXiv) — Models vulnerability management as a distributed pipeline, pinpointing exactly where and why vulnerability scanners diverge when analyzing identical software inventories.

---

## Elsewhere

*   **[Forgejo 16.0](https://forgejo.org/2026-07-release-v16-0/)** introduces per-repository watch options, an "Authorized Integrations" mechanism for secret-less API access, and multi-line review comments.
*   **[Ruby 4.0.6](https://www.ruby-lang.org/en/news/2026/07/14/ruby-4-0-6-released/)** arrives as a routine bugfix release.
*   **[Open Source Security: Project Lightwell](https://opensourcesecurity.io/2026/2026-07-lightwell-mo-duffy/)** (Josh Bressers) features a podcast discussion with Máirín Duffy covering Red Hat's initiative to route AI-discovered vulnerabilities directly to upstream projects.

---

*Got links for next year/week? Send them to [@andrewnez on Mastodon](https://mastodon.social/@andrewnez).*