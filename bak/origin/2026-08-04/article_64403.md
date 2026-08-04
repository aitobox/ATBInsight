# This Week in Package Management: 1 August 2026

*Compiled from the [package manager OPML feed collection](https://github.com/ecosyste-ms/package-managers-opml) and updates posted or boosted on [Mastodon](https://mastodon.social/@andrewnez).*

---

## 📌 Summary

Week eleven of the roundup brings major ecosystem updates, security enhancements, and new tooling releases:
* **Tool & Package Releases:** Significant updates rolled out for **mise**, **Verdaccio**, **uv**, **pip**, **pixi**, **pnpm**, **Docker**, **Homebrew**, and many others. Notably, *uv* released versions up to 0.12.1 introducing semantic fixes and new policy controls, while *pnpm* dropped its first Rust-engine beta (v12.0.0-beta.0).
* **Security Improvements:** npm rolled out publish-time malware scanning with explicit `contentPolicy` declarations, GitHub Actions introduced automatic safety holds on unproven workflows, and Arch Linux officially disabled orphaned-package adoption on the AUR following targeted attacks.
* **Research & Articles:** Discussions focused on maintainer burnout and sustainability ("Open Source Must Be Fun or It Will Die"), supply-chain fragility ("Supply Soup"), and key packaging research analyzing edgeless SBOMs and Python build verifications.
* **Ecosystem News:** Highlights include EuroPython 2026 Packaging Summit notes, Composer/Packagist launching a formal sponsorship program, and Fedora 45 adopting PURL metadata.

---

## Releases

* [mise 2026.7.14–18](https://github.com/jdx/mise/releases/tag/v2026.7.18): Default shell-argument settings are now global-only, preventing untrusted local configs from influencing command execution before trust evaluation. Includes experimental task output caching (replaying logs when sources/tools are unchanged) and experimental monorepo tasks that infer Node workspace dependency edges and import `package.json` scripts as `node:<package>#<script>` tasks.
* [Verdaccio 6.9.0](https://github.com/verdaccio/verdaccio/releases/tag/v6.9.0): Requires Node.js 22 minimum and ships a dual CJS+ESM build with an `exports` field, ensuring `import { runServer } from 'verdaccio'` resolves a true ES module. The bundled `@verdaccio/config` upgrades to js-yaml 4.3.0, resolving [GHSA-52cp-r559-cp3m](https://github.com/advisories/GHSA-52cp-r559-cp3m).
* [setup-uv v9.0.0](https://github.com/astral-sh/setup-uv/releases/tag/v9.0.0): Flips the `prune-cache` default to `false` to reduce load on PyPI infrastructure, which may lead to higher GitHub Actions cache usage ([details in #967](https://github.com/astral-sh/setup-uv/pull/967)).
* **Renovate:** 
  * [43.282.0](https://github.com/renovatebot/renovate/releases/tag/43.282.0) runs the mise manager in `MISE_SAFE=1` mode ([added last week](https://nesbitt.io/2026/07/25/this-week-in-package-management)), eliminating the need for `allowedUnsafeExecutions` on untrusted branches. 
  * [43.283.0](https://github.com/renovatebot/renovate/releases/tag/43.283.0) adds a `commitTrailers` option. 
  * [44.0.0](https://github.com/renovatebot/renovate/releases/tag/44.0.0) was an [accidental major](https://github.com/renovatebot/renovate/discussions/44952) triggered by a leftover `BREAKING CHANGE` footer; 44.x is being treated as a continuation of 43.x with no breaking changes.
* **uv:** 
  * [0.11.33](https://github.com/astral-sh/uv/releases/tag/0.11.33) runs malware checks against locked tools before reusing them from cache and supports reading/writing preview lockfiles without embedded `package.metadata`. 
  * [0.12.0](https://github.com/astral-sh/uv/releases/tag/0.12.0) introduces correctness changes: `uv init` defaults to a packaged `src/` layout with `uv_build`, rejects wheels that overwrite the Python interpreter, and enforces `--require-hashes` (rejecting MD5-only hashes). 
  * [0.12.1](https://github.com/astral-sh/uv/releases/tag/0.12.1) adds per-package pre-release policies via `--prerelease-package`, supports local HTML files as flat indexes, and adds `--fix` to the preview `uv check` command.
* [pip 26.2](https://github.com/pypa/pip/releases/tag/26.2): Adds `--only-deps` to install only a requirement’s dependencies, an experimental `--use-feature=venv-isolation` flag using a standard venv for build isolation, and HTTP caching for simple-index responses based on `Cache-Control` headers. The legacy resolver (`--use-deprecated=legacy-resolver`) is officially deprecated for removal in 2027. Read Richard Si's [release write-up](https://sichard.ca/blog/2026/07/whats-new-in-pip-26.2/).
* **pixi:** 
  * [0.74.0](https://github.com/prefix-dev/pixi/releases/tag/v0.74.0) allows environments to define dependencies and solve strategies inline without separate feature blocks, adds `--offline` mode, and lets `pixi global install --git` build tools from source given only `--build-backend`. 
  * [0.75.0](https://github.com/prefix-dev/pixi/releases/tag/v0.75.0) introduces `pixi publish` to deploy opted-in workspace packages in dependency order and restricts `--offline` solves to local cache or `file://` channels.
* [pnpm 11.15–11.19](https://pnpm.io/blog/releases/11.15-11.19): `pnpm update` and `pnpm outdated` now scan GitHub Actions references in workflow files, `pnpm update` can emit changesets, `pnpm self-update` ignores project-supplied config, web-based `pnpm login` works sans-TTY, and peak resolution memory on large workspaces is drastically reduced.
* [pnpm 12.0.0-beta.0](https://github.com/pnpm/pnpm/releases/tag/v12.0.0-beta.0): The first beta of the Rust-engine rewrite now parses `frozenLockfile`, `savePrefix`, `savePeer`, and `saveCatalogName` from `pnpm-workspace.yaml` and `PNPM_CONFIG_*` rather than requiring CLI flags.
* [Maven 4.0.0-rc-6](https://github.com/apache/maven/releases/tag/maven-4.0.0-rc-6): Resolves RC-5 regressions including a globally-cached field-accessibility state, a `ConcurrentModificationException` in the v4 API, and consumer POM conversion for BOM projects.
* **Docker:** 
  * [29.7.0](https://github.com/moby/moby/releases/tag/docker-v29.7.0) adds an experimental `embedded-containerd` feature running containerd inside the daemon process, promotes the `image` mount type out of experimental, and patches [CVE-2026-17106](https://github.com/moby/go-archive/security/advisories/GHSA-hfg8-hc9c-6c3h). 
  * [29.7.1](https://github.com/moby/moby/releases/tag/docker-v29.7.1) fixes regressions with layer parent-directory entries and `CopyToContainer` absolute symlink validation.
* [Homebrew 6.0.14](https://github.com/Homebrew/brew/releases/tag/6.0.14): Attaches vulnerability data from the GitHub Advisory Database to generated formula APIs, adds a `brew advisory-match` developer command, removes subprocess forks during no-op startups, and extends Landlock sandboxing to Linux kernel 6.1 ABI 2.
* **Other Notable Releases:** [npm 12.0.2](https://github.com/npm/cli/releases/tag/v12.0.2), [Conda 26.7.0](https://github.com/conda/conda/releases/tag/26.7.0), [pipx 1.16.5](https://github.com/pypa/pipx/releases/tag/1.16.5), [sbt 2.0.4](https://github.com/sbt/sbt/releases/tag/v2.0.4), [snapd 2.77](https://github.com/canonical/snapd/releases/tag/2.77), [vcpkg 2026-07-27](https://github.com/microsoft/vcpkg-tool/releases/tag/2026-07-27), [Dependabot Core 0.389.0](https://github.com/dependabot/dependabot-core/releases/tag/v0.389.0), [cabal-install 3.18.1.0](https://github.com/haskell/cabal/releases/tag/cabal-install-v3.18.1.0), [winget 1.30.80-preview](https://github.com/microsoft/winget-cli/releases/tag/v1.30.80-preview), [Yarn 4.18.0](https://github.com/yarnpkg/berry/releases/tag/%40yarnpkg%2Fcli%2F4.18.0), [Gradle 9.7.0-RC2](https://github.com/gradle/gradle/releases/tag/v9.7.0-RC2), [APT 3.3.2](https://salsa.debian.org/apt-team/apt/-/tags/3.3.2), [Mamba 2.9.0.rc0](https://github.com/mamba-org/mamba/releases/tag/2.9.0.rc0), [Podman 6.1.0-rc1](https://github.com/podman-container-tools/podman/releases/tag/v6.1.0-rc1), [diffoscope 326](https://diffoscope.org/news/diffoscope-326-released/).

---

## Security

* **npm Publish-Time Scanning:** [npm now scans packages at publish time](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/) before they hit the registry. Packages with legitimate security utility must declare a `contentPolicy` field in `package.json` and a root `DISCLOSURE` file, backed by 2FA or trusted publishing. Once declared, these cannot be removed in later versions.
* **GitHub Actions Workflow Protection:** [Workflows identified as potentially malicious are held](https://github.blog/changelog/2026-07-28-github-actions-holds-unproven-workflows-for-approval) until an authorized collaborator approves them via an authenticated web session.
* **AUR Orphaned-Package Adoption Disabled:** Arch Linux has [disabled orphaned package adoption on the AUR](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/DRDEU3JUSC72CB265XHXPFA3DFSLXPBP/) following malicious takeovers deploying Tor-based remote-access trojans (continuing the campaign from June's [alvr takeover](https://nesbitt.io/2026/06/13/this-week-in-package-management)). See [LWN's coverage](https://lwn.net/Articles/1086489/) for background.

---

## Articles

* [Open Source Must Be Fun or It Will Die](https://mikemcquaid.com/open-source-must-be-fun-or-it-will-die/) (Mike McQuaid): Explores maintainer enjoyment as a scarce resource, citing Homebrew's data where automated CI and tooling handle the tedious review work to keep 26 of 29 maintainers active.
* [The Package Manager for Everywhere](https://starhaven.io/blog/2026-07-27-the-package-manager-for-everywhere/) (Patrick Linnane): Analyzes Homebrew analytics, revealing that roughly 25% of traffic is on Linux (with Universal Blue accounting for 26% of non-CI Linux traffic and WSL at 3.7%).
* [You Don’t Have a Supply Chain, You Have a Supply Soup](https://opensourcesecurity.io/2026/07-supply-soup/) (Josh Bressers): Argues that standard supply chain metaphors fail because inputs to dependencies involve CI runners, developer workstations, and commit-access accounts that standard tooling fails to track.

---

## Papers

* [No Edges, No Verdict](https://arxiv.org/abs/2607.22140) (Zięba-Kozarzewski, arXiv): Analyzed 78,000 wild SBOMs, finding 52.9% declare no dependency edges at all. Treating edgeless SBOMs as degenerate drastically improved KEV-detection recall from 0.600 to 0.950.
* [No Snake Oil: Verifying Python Package Builds](https://arxiv.org/abs/2607.21888) (Dietrich et al., arXiv): Rebuilt 12,180 PyPI releases; only 15.4%–19.1% were byte-identical, but their `daleq4py` tool proved semantic equivalence for up to 78.9% of source-equivalent builds.

---

## Elsewhere

* **EuroPython 2026 Packaging Summit:** [Notes are available](https://hackmd.io/DZj3uo6eT_qyddBP0PZlDw?view) covering wheel-variant provider trust (PEPs 817/825), app lockfiles vs. library dependencies, PURL-based external build dependency metadata (PEPs 725/804), and Packaging Council elections.
* **WebAssembly Components:** Most WASI phase 2 proposals now feature OCI packages indexed on [wasm.directory](https://wasm.directory/wasi), a meta-registry slated for the Bytecode Alliance.
* **Composer & Packagist Sponsorship:** Launched a [formal sponsorship program](https://blog.packagist.com/announcing-the-composer-packagist-sponsorship-program/) to fund operations, incident response, and security features like transparency logs.
* **Renovate Config Debugger:** Sebastian Poxhofer released a [browser-based debugger](https://renovate.secustor.dev/) that steps through Renovate configuration parsing, migration, and validation.
* **GitHub Actions Self-Repository Actions:** Workflows can now reference local actions via `uses: $/path/to/action` [without checking out the repo](https://github.blog/changelog/2026-07-30-reference-same-repository-actions-with-self-repository-syntax).
* **Fedora PURL Integration:** Fedora 45 accepted a change to [Adopt PURL Metadata](https://fedoraproject.org/wiki/Changes/Adopt_PURL_Metadata), automatically adding virtual Provides like `purl(pkg:cargo/libc@0.2.186)` to language-ecosystem RPMs.

---

## git-pkgs

18 repositories were tagged this week:

* [git-pkgs v0.18.2](https://github.com/git-pkgs/git-pkgs/releases/tag/v0.18.2)
* [clone v0.1.2](https://github.com/git-pkgs/clone/releases/tag/v0.1.2) *(new)* – Go library for shallow local HTTPS Git checkouts via `git`.
* [cwe v0.1.0](https://github.com/git-pkgs/cwe/releases/tag/v0.1.0) *(new)* – Go library for looking up MITRE CWE entries by ID.
* [licenses v0.3.0](https://github.com/git-pkgs/licenses/releases/tag/v0.3.0) *(new)* – Go library and CLI for matching license text against ScanCode’s corpus offline.
* [magic v0.1.0](https://github.com/git-pkgs/magic/releases/tag/v0.1.0) *(new)* – Pure-Go content-detection library for format, MIME type, and text encoding.
* [archives v0.4.0](https://github.com/git-pkgs/archives/releases/tag/v0.4.0)
* [brief v0.9.4](https://github.com/git-pkgs/brief/releases/tag/v0.9.4)
* [capcheck v0.1.3](https://github.com/git-pkgs/capcheck/releases/tag/v0.1.3)
* [distill v0.1.1](https://github.com/git-pkgs/distill/releases/tag/v0.1.1)
* [enrichment v0.6.4](https://github.com/git-pkgs/enrichment/releases/tag/v0.6.4)
* [forge v0.7.0](https://github.com/git-pkgs/forge/releases/tag/v0.7.0)
* [manifests v0.6.1](https://github.com/git-pkgs/manifests/releases/tag/v0.6.1)
* [outline v0.1.8](https://github.com/git-pkgs/outline/releases/tag/v0.1.8)
* [pin v0.1.1](https://github.com/git-pkgs/pin/releases/tag/v0.1.1)
* [proxy v0.6.0](https://github.com/git-pkgs/proxy/releases/tag/v0.6.0)
* [registries v0.6.4](https://github.com/git-pkgs/registries/releases/tag/v0.6.4)
* [sigstore v0.1.2](https://github.com/git-pkgs/sigstore/releases/tag/v0.1.2)
* [spdx v0.2.0](https://github.com/git-pkgs/spdx/releases/tag/v0.2.0)

---

*Send links for next week to [@andrewnez@mastodon.social](https://mastodon.social/@andrewnez).*