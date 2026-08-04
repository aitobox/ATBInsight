# This Week in Package Management: 25 July 2026

Week ten of the roundup, built from the [package manager OPML feed collection](https://github.com/ecosyste-ms/package-managers-opml) and whatever I’ve posted or boosted on [Mastodon](https://mastodon.social/@andrewnez).

## 📋 Summary

This week’s package management roundup highlights crucial security updates—including the revocation of legacy RubyGems API keys following a CDN caching bug and PyPI's new 14-day restriction on modifying older releases. Major tool releases include RubyGems/Bundler 4.0.17, `uv` 0.11.31–0.32, `opam` 2.6.0-alpha1, `mise` updates focusing on secure CI runners, and Conan moving its Workspace feature out of incubation. Additionally, discussions center around EuroPython's Packaging Summit, new supply-chain security tooling like *zizmor* and *Scrutineer*, and historical dependency research datasets.

---

## 🚀 Releases

*   **[RubyGems and Bundler 4.0.17](https://blog.rubygems.org/2026/07/22/4.0.17-released.html):** Validates spec names before writing to the spec cache, escapes glob metacharacters in install paths, and resolves a series of Windows path-handling bugs in `gem open`, `bundle open`, and `MAKE`/`rake` environment variables.
*   **[uv 0.11.31 & 0.11.32](https://github.com/astral-sh/uv/releases/tag/0.11.31):** Adds support for workspace sources referencing members of different workspaces by path, centralized project environment `.venv` pointers, and new `audit.malware-check` settings. Version `0.11.32` quickly followed to enforce canonical formatting in lockfiles.
*   **[opam 2.6.0-alpha1](https://github.com/ocaml/opam/releases/tag/2.6.0-alpha1):** The first alpha of the 2.6 series updates the shell env hook to modify `PATH` in place, reads repositories in-memory via `ocaml-tar` to drastically reduce syscalls on slow filesystems, and trims disk usage by deleting build directories earlier.
*   **[pnpm 11.11–11.14](https://pnpm.io/blog/releases/11.11-11.14):** Introduces `pnpm doctor` for comprehensive installation diagnostics, `pnpm access` for registry permission management, convergence overrides, and achieves roughly 30% lower peak memory usage during cold-cache resolution.
*   **[mise 2026.7.11 – 2026.7.13](https://github.com/jdx/mise/releases/tag/v2026.7.11):** Brings consistent tool selector definitions and introduces `MISE_SAFE=1` mode to turn mise into an inert config reader for secure CI/bot environments. The `npm:` backend no longer requires Node, and several external binaries (skopeo, crane, gpg) have been replaced with built-in implementations.
*   **[Conan 2.31.0 & 2.31.1](https://github.com/conan-io/conan/releases/tag/2.31.0):** Moves the Workspace feature out of incubation, adds regex support to `replace_in_file`, and enables dynamic workspace versioning via a new `get_ref(folder)` method in `conanws.py`.
*   **[vcpkg 2026-07-24](https://github.com/microsoft/vcpkg-tool/releases/tag/2026-07-24):** Switches dependency snapshots to canonical vcpkg PURLs and embeds Git tree gitoids into its SPDX SBOMs.

**Also out:** 
[Homebrew 6.0.12](https://github.com/Homebrew/brew/releases/tag/6.0.12), [Deno 2.9.4](https://github.com/denoland/deno/releases/tag/v2.9.4), [Podman 6.0.2](https://github.com/podman-container-tools/podman/releases/tag/v6.0.2), [snapd 2.76.3](https://github.com/canonical/snapd/releases/tag/2.76.3), [Cabal 3.18.1.0](https://github.com/haskell/cabal/releases/tag/Cabal-hooks-v3.18.1.0), [pipx 1.16.2](https://github.com/pypa/pipx/releases/tag/1.16.2), [winget 1.30.70-preview](https://github.com/microsoft/winget-cli/releases/tag/v1.30.70-preview), [sbt 2.0.3](https://github.com/sbt/sbt/releases/tag/v2.0.3), [pnpm 11.15.1](https://github.com/pnpm/pnpm/releases/tag/v11.15.1), [pnpm 12.0.0-alpha.21](https://github.com/pnpm/pnpm/releases/tag/v12.0.0-alpha.21), [Renovate 43.280.4](https://github.com/renovatebot/renovate/releases/tag/43.280.4), and [Dependabot Core 0.388.0](https://github.com/dependabot/dependabot-core/releases/tag/v0.388.0).

---

## 🔒 Security

*   **[RubyGems.org API Key Disclosure](https://blog.rubygems.org/2026/07/22/security-advisory-legacy-api-key-leak.html):** Disclosed a CDN caching bug that could expose a legacy API key to another user signing in via the same edge node. Affects gem clients older than v3.2.0. All legacy keys were revoked on 23 July (scoped and OIDC keys remain unaffected).
*   **[PyPI Release Restrictions](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days):** PyPI now automatically rejects new file uploads to releases older than 14 days, mitigating the risk of compromised publishing tokens altering long-stable releases.

---

## ✍️ Articles

*   **[Securing our GitHub Actions workflows with zizmor](https://blog.packagist.com/securing-our-github-actions-workflows-with-zizmor/)** (Packagist blog): Details supply-chain hardening steps across Composer and Packagist repositories, including pinning actions to commit SHAs and cutting token permissions to read-only.
*   **[Who’s responsible for bug reports on old software versions?](https://pointieststick.com/2026/07/19/whos-responsible-for-bug-reports-on-old-software-versions/)** (Nate Graham): Argues that distributors shipping frozen software versions inherently carry the corresponding support burden.
*   **[Guix: creating a package from a binary](https://aloysberger.com/posts/guix-packaging-a-binary-as-a-guix-beginner.html)** (Aloys Berger): Walks through packaging the Caddy binary in Guix as a practical workaround to avoid building a dozen nested Go dependencies from source.

---

## 🌍 Elsewhere

*   **EuroPython 2026 Packaging Summit:** Held in Kraków last week, featuring talks on the upcoming Cyber Resilience Act obligations, three years of PyPI Trusted Publishing, and hidden compiled binary dependencies.
*   **[CHRONO-RESOLUTION](https://arxiv.org/abs/2607.15315):** A new arXiv dataset tracking historical dependency-resolution graphs across npm, PyPI, and crates.io.
*   **[Scrutineer](https://github.com/alpha-omega-security/scrutineer):** The Alpha-Omega security scanner is [now available in Homebrew](https://formulae.brew.sh/formula/scrutineer).

---

## 📦 git-pkgs

New releases tagged this week:
*   [git-pkgs v0.18.1](https://github.com/git-pkgs/git-pkgs/releases/tag/v0.18.1)
*   [enrichment v0.6.3](https://github.com/git-pkgs/enrichment/releases/tag/v0.6.3)
*   [registries v0.6.3](https://github.com/git-pkgs/registries/releases/tag/v0.6.3)
*   [vulns v0.2.1](https://github.com/git-pkgs/vulns/releases/tag/v0.2.1)
*   [purl v0.1.15](https://github.com/git-pkgs/purl/releases/tag/v0.1.15)

***

*Send links for next week to [@andrewnez@mastodon.social](https://mastodon.social/@andrewnez).*