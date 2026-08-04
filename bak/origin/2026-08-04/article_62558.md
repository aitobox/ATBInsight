# Package Name Prefixes across Ecosystems

## Summary
Package name prefix reservation has become a critical mechanism for package registries to combat impersonation and malware (such as publishing malicious packages like `google-cloud-something`). Following the adoption of **PEP 752** on PyPI—which allows organizations to reserve package name prefixes—this analysis examines prefix distributions across seven major software registries (`pypi.org`, `crates.io`, `rubygems.org`, `hex.pm`, `hackage.haskell.org`, `npmjs.org`, and `nuget.org`). 

Data reveals that between one-third and two-thirds of packages across all registries share a first token prefix with at least four other packages. These prefixes generally fall into specific categories: open plugin conventions (e.g., `django-*`), generated SDK families (e.g., `aws-sdk-*`), language tags, and automated spam or bulk publication waves. Different registries handle these structures uniquely—from NuGet's manual verification and public reservations to Cargo’s upcoming colon-separated namespaces (`foo::bar`) and npm's scoped packages (`@scope/name`).

---

## Seven Registries Compared

Splitting package names on runs of `-`, `_`, and `.` and grouping by their first token reveals the following landscape:

| Registry | Total Packages | Prefixes with $\ge 5$ Packages | Packages with a Shared Prefix | $\ge 100$ | $\ge 500$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **pypi.org** | 912,665 | 13,934 | 41% | 427 | 66 |
| **crates.io** | 311,301 | 9,161 | 54% | 166 | 19 |
| **rubygems.org** | 209,853 | 4,214 | 46% | 132 | 18 |
| **hex.pm** | 22,373 | 382 | 32% | 12 | 1 |
| **hackage.haskell.org** | 19,345 | 521 | 41% | 9 | 0 |
| **npmjs.org (unscoped)** | 2,678,188 | 37,460 | 68% | 2,604 | 468 |
| **nuget.org** | 828,361 | 22,377 | 70% | 690 | 72 |

*(Note: npm has supported `@scope/name` since 2014; the npm row counts only the 63% of packages that remain unscoped. Multi-token prefixes like `apache-airflow-providers-` are categorized under `apache-*` in the table above).*

---

## Categories of Prefixes

### 1. Open Plugin Conventions
Plugin ecosystems where many authors publish extensions named after a host project comprise the largest category of major prefixes:
* **PyPI:** `django-*` (17,450 packages)
* **npm:** `react-*` (86,142)
* **RubyGems:** `jekyll-*` (1,658)
* **Crates.io:** `bevy-*` (1,870)
* **Hex.pm:** `phoenix_*` (245)
* **Hackage:** `servant-*` (152)

Many of these are functionally required by host tooling (e.g., Cargo runs `cargo-foo` for `cargo foo`, and ESLint resolves `eslint-plugin-foo`).

### 2. Generated SDK Families
Generated families occur when a single organization publishes hundreds of packages from an API specification:
* `aws-sdk-*` (473 crates, 481 gems, 92 PyPI)
* `google-cloud-*` (258 crates, 510 gems, 264 PyPI, 5 Hackage)
* `azure-mgmt-*` (273 crates, 124 gems, 334 PyPI)
* **Odoo Community Association (PyPI):** ~20,000 packages distributed across seven versioned prefix trees (`odoo8-addon-*` through `odoo14-addon-*` plus `odoo-addon-*`).
* **npm (scoped):** `@types/*` (11,388), `@stdlib/*` (5,555), `@fontsource/*` (2,122).

### 3. Language, Framework Tags, and Tutorials
* **Framework tags:** `python-*` (6,278), `rust-*` (1,692), `ex_*` (1,123 Hex), `node-*` (23,389 npm).
* **Tutorial residue:** `hola-*` (764 RubyGems from the *make your own gem* guide), `example-package-*` (PyPI tutorial), `guessing-game-*` (125 on Crates.io from the Rust book).
* **Assignments:** `topsis-*` on PyPI accounts for 1,999 packages embedding student roll numbers for a decision-analysis programming assignment run annually since 2020.

### 4. Bulk Publication and Spam Waves
Recent automated publishing has generated massive prefix clusters:
* `use-*` on crates.io: 820 packages (809 published in 2026 by a single account).
* `iflow-mcp-*` on PyPI: 2,505 republished Model Context Protocol servers, alongside 5,184 packages under `@iflow-mcp` on npm.
* `free.robux-*` on NuGet: 3,620 packages.

---

## Ecosystem Approaches to Namespaces

### NuGet
NuGet introduced **ID prefix reservation** in October 2017. Organizations apply via email, after which matching uploads from unauthorized users are rejected. It introduces a checkmark for verified packages in the gallery and supports subprefix delegation (e.g., delegating `Microsoft.AspNet.*`) and public reservations (where community publishers can still upload, while core packages are explicitly badged).

### Crates.io (Cargo)
Cargo's **RFC 3243** takes a decentralized approach: whoever owns the `foo` crate can publish `foo::bar` with zero application process. Of the 166 crates.io prefixes with $\ge 100$ packages, 156 have a bare crate matching the first token (though 37% of those base crates haven't been released in over 5 years). This avoids disrupting existing hyphenated names like `serde_json`.

### npm
npm's `@scope/name` design has been active since 2014, with 37% of live packages utilizing it. Among unscoped packages, flat conventions often massively outnumber scoped counterparts (e.g., `vue-*` has 23,871 packages vs. `@vue/*` at 110), primarily because tools rely on string-matching flat prefixes for configuration (e.g., `eslint-plugin-*`).

---

## Browsing and Discovery
While popular plugin ecosystems often maintain curated directory sites (e.g., Homebridge, Node-RED, Jekyll), general registry search tools return fuzzy-ranked results. NuGet’s checkmark and npm’s scope organization pages (`npmjs.com/org/babel`) remain rare examples of built-in membership UI. Third-party registry browsers or aggregated tools (like `ecosyste.ms`) offer prime opportunities to build dedicated prefix-clustering views.

## The Future: PEP 752 and PEP 755
PEP 752 establishes the rules for prefix reservations on PyPI, while its companion draft policy **PEP 755** defines who can apply and under what terms. How these policies will interact with existing open conventions (like `django-*` or `pytest-*`) remains a critical question for the Python ecosystem moving forward.

*Data and analysis scripts are available on GitHub: [github.com/andrew/package-name-prefixes](https://github.com/andrew/package-name-prefixes).*