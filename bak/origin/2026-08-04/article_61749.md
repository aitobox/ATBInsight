# The Rust Coreutils (`uutils`) Are "Sticky" in Ubuntu 26.04 LTS

## Summary
Ubuntu 26.04 LTS makes the Rust-based rewrite of GNU Coreutils (`uutils`) the default system utilities. While Canonical provides a way to revert to the traditional GNU Coreutils, the migration is stubbornly complicated. Because critical meta-packages like `build-essential` explicitly depend on the Rust-based `coreutils-from-uutils` rather than a generic alternative, routine package installations and dependency resolutions will silently revert your system back to the Rust versions unless strict preventative measures are taken.

---

## Background: The Shift to Rust Coreutils

The [GNU Coreutils](https://www.gnu.org/software/coreutils/) comprise the fundamental command-line utilities of Unix and Linux environments, such as `mkdir`, `head`, `chmod`, `cp`, and `mv`. 

Recently, these utilities were rewritten in Rust as [uutils coreutils](https://uutils.org/). Canonical decided to adopt these Rust implementations as the default starting in Ubuntu 25.10 and carrying through to the 26.04 LTS release.

Although the project aims for 100% compatibility, real-world incompatibilities emerge quickly. After encountering issues in pre-release testing—and finding standard bug-reporting channels less than ideal—many system administrators prefer to opt out rather than act as mandatory beta-testers for Canonical's new default.

---

## Reverting to GNU Coreutils

Canonical makes switching back to the traditional GNU utilities possible, though not entirely straightforward. According to the [official Ubuntu migration guide](https://discourse.ubuntu.com/t/migration-to-rust-coreutils-in-25-10/59708), you can swap them out using the following command:

```bash
apt-get install coreutils-from-gnu coreutils-from-uutils- --allow-remove-essential
```

To lock in this preference, it is strongly recommended to immediately hold the package:

```bash
apt-mark hold coreutils-from-uutils
```

*(Note: You may also want to hold `coreutils-from-gnu` to prevent unintended alterations, though the core execution binaries reside in the separate `gnu-coreutils` package).*

---

## The Catch: The `build-essential` Dependency Problem

Switching back is not a "set-and-forget" operation. As highlighted in [this Fediverse post](https://mastodon.social/@cks/116930308880494105):

> **Ubuntu:** You can totally continue to use GNU Coreutils in 26.04 LTS.  
> **Also Ubuntu:** `build-essential` depends on the new Rust coreutils.

If you install `coreutils-from-gnu`, the package manager will automatically uninstall `build-essential`. Conversely, if you install `build-essential` at a later date, it will purge your GNU coreutils and forcibly reinstall `coreutils-from-uutils`. 

This creates a hidden trap during routine system maintenance or framework installations. If you aren't paying close attention to `apt-get` logs, your systems may end up running Rust coreutils despite your intentional migration.

### Why This Matters

While `build-essential` is lightweight, it is automatically pulled in by `apt-get build-dep <package>`, a common command used to gather compilation dependencies (such as when [building your own version of Emacs](https://mastodon.social/@cks/116817958595204460)). 

Checking the package details reveals an explicit, hardcoded dependency:

```text
$ apt-cache show build-essential
[...]
Depends: libc6-dev | libc-dev, gcc (>= 4:14.2), g++ (>= 4:14.2), make, dpkg-dev (>= 1.22.11), coreutils-from-uutils
```

Rather than using a flexible meta-package or an either/or condition (`coreutils-from-uutils | coreutils-from-gnu`), this is [a Canonical bodge introduced in late 2025](https://git.launchpad.net/ubuntu/+source/build-essential/commit/?id=28bd47593db15e492a66bd2531ad8caeb76f0caa) that bypasses upstream norms. Bypassing this effectively requires building a custom version of `build-essential` with corrected dependencies (for example, [using `dgit`](https://utcc.utoronto.ca/~cks/space/blog/linux/DgitOnUbuntuEarlyNotes)).

---

## Recommendations

Because other packages may harbor similar hardcoded requirements, holding the `coreutils-from-uutils` package is essential. 

With the package held, running `apt-get install` will safely abort with a conflict error rather than silently flipping your core utilities behind your back. This ensures you remain in control of your server environment.