# The `--end-of-options` Flag in Git and the Argument Injection Threat

## Summary

This article explores `git --end-of-options`, a lesser-known flag introduced in Git 2.24.0 to solve an edge case in argument parsing where traditional `--` fails. It dives into the mechanics of **Argument Injection (CWE-88)**—how passing untrusted inputs (like package manager URLs or refs) directly into `exec()` allows flags like `--upload-pack` or `-oProxyCommand` to execute arbitrary commands. 

While numerous package managers have suffered from related CVEs across Git, Mercurial, and other tools, very few actually utilize `--end-of-options` due to legacy minimum Git version requirements. Finally, the article contrasts these subprocess vulnerabilities with native Git libraries (like libgit2 and gitoxide) and shares a practical implementation for Homebrew.

---

## The Origin of `--end-of-options`

While examining a package manager CVE fix, I stumbled upon a Git flag I had never seen before: `--end-of-options`. Initially suspected to be an LLM hallucination, it is officially [documented in `gitcli(7)`](https://git-scm.com/docs/gitcli), added in Git 2.24.0 (November 2019), and exists solely because Git had already repurposed `--` for another job.

In most Unix utilities, `--` marks the absolute end of option parsing (e.g., `rm -- -f` deletes a file named `-f`). However, Git repurposed `--` early on to separate **revisions** from **pathspecs**. For example:
```bash
git log main -- README.md
```
Here, `--` separates the commit reference (`main`) from the file path (`README.md`). Because `--` is already claimed, the revision position is left without a terminator. If a script executes `git log "$rev"` and `$rev` begins with a dash, Git mistakenly parses it as a command-line option.

As noted in the [original commit message](https://github.com/git/git/commit/19e8789b236dfe33667747d5523d6689bb59b5ef):
> *"But that doesn’t work for the revision parser, because `--` is already meaningful there: it separates revisions from pathspecs. So we need some other marker to separate options from revisions."*

### `--` vs. `--end-of-options`
Treating `--` and `--end-of-options` interchangeably is a frequent mistake:
* **`git clone -- "$url"`**: Works because `clone` follows standard POSIX conventions.
* **`git checkout "$ref" --`**: Marks `$ref` as a revision rather than a filename, but still allows it to be parsed as an option first.
* **Safe execution**: Safely parsing an untrusted revision requires both markers:
  ```bash
  git log --end-of-options "$rev" -- "$path"
  ```

Support for the new flag rolled out incrementally across subcommands. `git rev-parse` [received it in version 2.30.0](https://github.com/git/git/commit/3a1f91cfd9), while `git checkout` and `git reset` [did not accept it until 2.43.1](https://github.com/git/git/commit/9385174627) (February 2024).

---

## Argument Injection (CWE-88)

Git, Mercurial, and SSH all ship with options explicitly designed to run custom commands provided by the caller:
* **Git**: `--upload-pack=<cmd>` specifies the server-side binary, and `-c core.sshCommand=<cmd>` overrides connection behavior.
* **Mercurial**: `--config=alias.<subcmd>=!<shell>` redefines any subcommand as an arbitrary shell script.
* **SSH**: `-oProxyCommand=<cmd>` defines a proxy command.

These features transform into attack vectors when wrapping programs pass untrusted strings directly into argument arrays. 

This failure mode is classified under **[CWE-88 (Argument Injection)](https://cwe.mitre.org/data/definitions/88.html)**. Unlike command injection, **no shell is involved**. The wrapper builds an `argv` array and calls `exec` directly—following the exact advice of *"don't use `system()`"* guides. The array reaches Git intact, and Git parses the leading-dash argument as an option. A clear example is [CVE-2019-13139 in `docker build`](https://staaldraad.github.io/post/2019-07-16-cve-2019-13139-docker-build/), where a Go `os/exec` call processed a Git URL with a `#ref:dir` fragment that mutated into `--upload-pack=<cmd>`.

This vulnerability class was famously demonstrated across four version control systems simultaneously in August 2017:
* [CVE-2017-1000117](https://nvd.nist.gov/vuln/detail/CVE-2017-1000117) (Git)
* [CVE-2017-1000116](https://nvd.nist.gov/vuln/detail/CVE-2017-1000116) (Mercurial)
* [CVE-2017-9800](https://subversion.apache.org/security/CVE-2017-9800-advisory.txt) (Subversion)
* [CVE-2017-12836](https://nvd.nist.gov/vuln/detail/CVE-2017-12836) (CVS)

In each case, passing a hostname starting with `-oProxyCommand=` to `ssh` triggered unintended option parsing. A Phabricator [post-mortem](https://web.archive.org/web/20251216145944/https://secure.phabricator.com/T12961) noted that Subversion was the only tool to reliably prepend `--` to hostnames; Git and Mercurial relied on input validation instead, because `--` is not universally supported by every SSH implementation.

---

## Package Managers and Vulnerabilities

Package managers frequently accept Git URLs or refs from manifests, lockfiles, or transitive dependencies and pass them down to system subcommands (e.g., `gem 'foo', git: '...'` or `github:user/repo#ref` in `package.json`).

Of nineteen major package managers surveyed[^1], **seventeen fork the native `git` binary** by default. The only exceptions are:
* **Cargo**: Uses [libgit2](https://libgit2.org/) by default (with an opt-in `net.git-fetch-with-cli` setting to fork).
* **Poetry**: Switched to [dulwich](https://www.dulwich.io/) in [version 1.2.0](https://github.com/python-poetry/poetry/commit/ad1b0938) (with a `system-git-client` fallback). 
* *(Note: Nix uses libgit2 for local reads, but forks `git` for fetches because [libgit2 lacks git-credential helper support](https://github.com/NixOS/nix/blob/3aff4dc5edf30998d64eec024de186ac2d6fb5ea/src/libfetchers/git-utils.cc#L639-L641).)*

Package managers have accumulated numerous CVEs in this category, including:
* **Bundler**: [CVE-2021-43809](https://github.com/advisories/GHSA-fj7f-vq84-fh43)
* **Composer**: [CVE-2021-29472](https://github.com/composer/composer/security/advisories/GHSA-h5h8-pc6h-jvvx), [CVE-2022-24828](https://github.com/composer/composer/security/advisories/GHSA-x7cr-6qr6-2hh6)
* **Poetry**: [CVE-2022-36069](https://github.com/advisories/GHSA-9xgj-fcgf-x6mw)
* **pip**: [CVE-2023-5752](https://github.com/advisories/GHSA-mq26-g339-26xf)
* **CocoaPods**: [CVE-2022-21223](https://github.com/advisories/GHSA-g397-v4w5-4m79), [CVE-2022-24440](https://github.com/advisories/GHSA-7627-mp87-jf6q)
* **Go**: [CVE-2025-68119](https://pkg.go.dev/vuln/GO-2026-4338)

*(For deep dives, Snyk provides a [write-up on argument injection](https://snyk.io/blog/argument-injection-when-using-git-and-mercurial/), and Sonar maintains a [catalogue of dangerous options](https://sonarsource.github.io/argument-injection-vectors/).)*

Among the seventeen tools that fork Git, **exactly one uses `--end-of-options`**: Go's `cmd/go`. After adding `--` to repository URLs in June 2019, Go developers [adopted `--end-of-options` globally](https://github.com/golang/go/commit/94a1296a457387d1fd6eca1a9bcd44e89bdd9d55) in January 2026 to patch CVE-2025-68119, alongside enforcing `HGPLAIN=+strictflags` for Mercurial.

---

## Minimum Git Version Constraints

Most package managers guard against argument injection via `--` or a leading-dash validation check added reactively after a CVE disclosure (e.g., Bundler's [CVE-2021-43809 patch](https://github.com/ruby/rubygems/commit/90b1ed8b9f), cocoapods-downloader's [validation commits](https://github.com/CocoaPods/cocoapods-downloader/commit/35340f4b), and Poetry's [guard](https://github.com/python-poetry/poetry-core/commit/cc84be6)). 

The [Composer advisory for CVE-2022-24828](https://blog.packagist.com/cve-2022-24828-composer-command-injection-vulnerability/) highlights why `--end-of-options` is rarely adopted: **legacy support**. Because Composer supports older Git versions that predate the flag, patches resort to rejecting leading-dash branch names instead. 

Relying on `--end-of-options` forces maintainers to raise their minimum Git requirements:
* **Git ≥ 2.24.0** for basic subcommands.
* **Git ≥ 2.30.0** for `rev-parse`.
* **Git ≥ 2.43.1** for `checkout` and `reset`.

While older environments (like Amazon Linux 2 or Ubuntu 18.04/20.04) are gradually reaching end-of-life, enforcing these minimum versions risks dropping compatibility with long-term distribution packages.

---

## Alternative: Pure Git Libraries

Libraries like [libgit2](https://libgit2.org/), [gitoxide](https://github.com/GitoxideLabs/gitoxide), [go-git](https://github.com/go-git/go-git), [JGit](https://github.com/eclipse-jgit/jgit), and dulwich implement the Git wire protocol entirely in-process, bypassing the `argv` boundary completely. 

* **Jujutsu (`jj`)** relies on gitoxide for Git interoperability and has avoided argument-injection vulnerabilities entirely.
* **go-git** has experienced only one CVE in this class ([CVE-2025-21613](https://github.com/go-git/go-git/security/advisories/GHSA-v725-9546-7q7m)), which was isolated to the `file://` transport—the single code path forced to spawn a native `git` binary.

While bundled implementations trade subprocess issues for the burden of tracking upstream safety patches, they replace a fragile runtime check with a secure architectural boundary.

Inspired by these findings, I [opened a PR against Homebrew](https://github.com/Homebrew/brew/pull/23223) to raise its minimum Git requirement to 2.30.0, integrating `--end-of-options` into `clone`, `remote set-url`, `ls-remote`, and `rev-parse` calls while omitting `checkout` and `reset` to avoid breaking environments restricted to older Git binaries.

---

### Footnotes

1. Bundler, Cargo, CocoaPods, Composer, Conan, Go, Helm, Homebrew, Mix, Nix, npm, pip, pnpm, Poetry, Pub, SwiftPM, uv, vcpkg, and Yarn (all checked at HEAD in July 2026). [↩](#fnref:survey)