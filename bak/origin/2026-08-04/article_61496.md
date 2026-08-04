# Plumbing Homebrew into the Vulnerability Ecosystem

## Summary

This document details the journey of bringing native CVE vulnerability scanning to **Homebrew**—moving from a standalone third-party gem (`brew-vulns`) to a core, built-in feature as of Homebrew 6.0.11. 

The integration required bridging the gap between Homebrew's package management model and standard vulnerability ecosystems (like OSV and CycloneDX). This involved introducing native patch-annotation APIs, building an independent advisory database, registering new Package-URL (`purl`) and OSV schema types, porting Homebrew's version-comparison logic to Python, and optimizing test coverage across thousands of formulae.

---

## 1. From Third-Party Gem to Core Feature

Back in January, [`brew-vulns`](https://nesbitt.io/2026/01/08/brew-vulns-cve-scanning-for-homebrew) was released as a gem that added CVE scanning to Homebrew by shelling out to `brew info --json=v2`, deriving source repository URLs, and querying [osv.dev](https://osv.dev). 

As of Homebrew 6.0.11, this functionality is now **built-in**, making the original gem deprecated. 

```bash
$ brew vulns
Checking 142 packages for vulnerabilities...
(18 packages skipped - no supported source URL)

openssl@3 (3.4.1)
  CVE-2024-13176 (medium) - Timing side-channel in ECDSA signature...
    Fixed in: 3.4.2

Found 1 vulnerability in 1 package

10 resolved by formula patches (not counted; pass --no-ignore-patches to include):
  glibc: CVE-2024-2961, CVE-2024-33599, CVE-2024-33600, CVE-2025-0395, ...
```

Running the tool across the entirety of `homebrew-core` (roughly 8,400 formulae) exposed several real-world edge cases:
* **Fail-Closed Range Evaluation:** OSV records with malformed `affected` ranges required stricter handling.
* **Sanitization:** Vulnerability summaries containing terminal escape sequences needed cleaning prior to output.
* **Rate Limiting & Thread Capping:** Pagination and thread pools fetching vulnerability details received hard caps to prevent unbounded API requests.
* **CI Integration:** Added a [distinct exit code](https://github.com/Homebrew/homebrew-brew-vulns/pull/79) for scan errors versus actual vulnerability findings.

---

## 2. Formula Patches and the `resolves` DSL

Hundreds of formulae in `homebrew-core` apply local patches to upstream tarballs. If a patch fixes a CVE, the installed bottle remains secure even if the upstream version falls within an advisory range.

To programmatically address this, Homebrew was updated to:
1. Expose patches in `Formula#to_hash` JSON output.
2. Introduce a `patch do` DSL with `resolves` and `type` attributes matching CycloneDX’s [`pedigree.patches`](https://cyclonedx.org/docs/1.6/json/#components_items_pedigree_patches) specification:

```ruby
patch do
  url "https://deb.debian.org/.../libquicktime_1.2.4-12.debian.tar.xz"
  sha256 "..."
  type :backport
  resolves "CVE-2016-2399", "CVE-2017-9122"
  apply "patches/CVE-2016-2399.patch", "patches/CVE-2017-9122_et_al.patch"
end
```

CVE IDs are automatically inferred from patch URLs and `apply` filenames. Any OSV result matching a `resolves` entry is now categorized as patched, excluded from exit error codes, and marked `analysis.state: resolved` in SBOM outputs.

---

## 3. Spec Registrations and the Advisory Database

To ensure external tooling could seamlessly process Homebrew's data, updates were made across multiple vulnerability ecosystems:

* **Package URL (purl) Spec:** Added the `pkg:brew` type. Because Homebrew formulae can use `@` for version-pinned variants (e.g., `openssl@3`), names are percent-encoded (e.g., `pkg:brew/openssl%403`).
* **OSV Schema Registration:** Registered [`Homebrew` and the `BREW-` prefix](https://github.com/ossf/osv-schema/pull/576) in the OSV schema registry.
* **Advisory Database:** Established [`Homebrew/advisory-database`](https://github.com/Homebrew/advisory-database) to store OSV-compliant JSON records generated automatically from `resolves` annotations via a daily GitHub Actions workflow.

---

## 4. Merging into `Homebrew/brew`

Porting the scanner natively into `Library/Homebrew/cmd/vulns.rb` required stripping external gem dependencies (`purl`, `vers`, `cvss-suite`, `sbom`, `sarif-ruby`) to comply with Homebrew's strict bundle rules:

* **Version Comparison:** The `vers` gem was replaced by a custom `Homebrew::Vulns::Semver` module implementing strict SemVer 2.0 comparison rules.
* **CVSS Scoring:** The `cvss-suite` gem was refactored into `Homebrew::Vulns::CVSS` to calculate v3.0/v3.1 base scores natively.
* **SPDX SBOM Integration:** Instead of reading current formula definitions (which might point to newer, bumped versions), the built-in command reads the **installed keg's SPDX SBOM** to guarantee accuracy against the actual installed binaries.

---

## 5. Coverage and Future Directions

The native scanner currently covers roughly 73% of `homebrew-core` via GitHub, GitLab, and Codeberg repository URLs. Expanding this coverage moving forward involves:

1. **Registry Integration:** Leveraging PyPI, npm, and other language registry URLs to build direct package purls.
2. **Repology Mapping:** Using [Repology](https://repology.org) API dumps to map lesser-hosted formulae (SourceForge, GNU mirrors, Debian archives) to distro-equivalent source packages.
3. **Ecosystem Ingestion:** Finalizing the [osv.dev ingestion pipeline](https://github.com/google/osv.dev/issues/5659) to enable direct server-side queries for `{ecosystem: "Homebrew"}`.
4. **UI Integration:** Surface vulnerability findings directly inside `formulae.brew.sh`, `brew info`, and upgrade commands so security states are transparent at install and upgrade time.