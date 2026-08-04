# Ubuntu 26.04 Broken Shutdown Announcements and `wall` Issue

## Summary
When performing unscheduled reboots on Ubuntu 26.04 servers, administrators discovered that **shutdown warning broadcasts** and the traditional **`wall` command** no longer notify active users. Investigation reveals these are two distinct root causes:
1. **The `wall` failure** stems from modern systemd (starting in Debian 13 / Ubuntu 25.10) being built without `/run/utmp` support due to Y2038 compliance concerns.
2. **The shutdown broadcast failure** occurs because `systemd-logind` in Ubuntu 26.04 fails to track TTY associations for SSH logins, meaning announcements never reach active terminal sessions. 

Additionally, alternative tools like `who` and `w` rely on complex fallbacks and are further impacted by AppArmor restrictions.

---

## 1. The Breakdown of `wall`
The venerable `wall` program (from the `bsdutils` package) relies entirely on the traditional `/var/run/utmp` (or `/run/utmp`) file to determine who is logged in and where. 

* **The Cause:** Starting with Debian 13 ("Trixie") and Ubuntu 25.10, systemd is built without `utmp` support, primarily due to the format's [Y2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem). 
* **The Impact:** Because `utmp` is absent, `wall` fails silently and does nothing. 
* **Workarounds:** 
  * You must write custom scripts to query active user sessions with pseudo-terminals (ptys) and broadcast messages directly.
  * A replacement project exists called [`wtmpdb`](https://github.com/thkukuk/wtmpdb), which also restores the `last` command. However, it requires manual PAM configuration, and Ubuntu 26.04's OpenSSH is currently built without `wtmpdb` support.

---

## 2. Broken Shutdown Broadcasts
Normally, running a command like:
```bash
shutdown -r +NN "<a message about the situation>"
```
triggers periodic warnings managed by `systemd`. On Ubuntu 26.04, these messages fail to broadcast to SSH users.

* **The Cause:** In Ubuntu 26.04 (featuring systemd 259.5), `systemd-logind` fails to map the TTYs used by SSH logins. Running `loginctl` or `loginctl -j` reveals a complete lack of TTY information for SSH sessions (though local console logins display correctly).
* **Comparison:** This bug is absent in older versions like Ubuntu 24.04 (systemd 255.4) and Fedora 44 (systemd 259.7 with UTMP enabled).
* **The Impact:** Because logind only transmits shutdown warnings to TTYs it actively tracks, SSH sessions receive no advance notice.

---

## 3. Quirks with `who`, `w`, and AppArmor
Interestingly, utilities like `who` (from GNU Coreutils) and `w` (from procps) may still display PTY information on Ubuntu 26.04—provided you have AppArmor disabled:

```text
$ who
cks      sshd pts/0   Jul 20 21:47 (...)
$ lsb_release -r
Release:        26.04
```

### Why do they still work (partially)?
* **GNU Coreutils `who`** attempts to query systemd via library APIs. If session TTY info is missing, it falls back to [scanning `/dev/pts`](https://github.com/coreutils/gnulib/blob/master/lib/readutmp.c#L734). *(Note: The alternative Rust-based `uutils` version suffers from [Launchpad bug #2152801](https://bugs.launchpad.net/ubuntu/+source/rust-coreutils/+bug/2152801)).*
* **Procps `w`** utilizes a similar fallback mechanism when both systemd and `utmp` fail to report TTY data. Because their fallback methods differ, `who` and `w` may occasionally report conflicting information on Ubuntu 26.04.

### The AppArmor Complication
Default AppArmor profiles in Ubuntu 26.04 block `who` from accessing `/run/systemd/sessions` (which the systemd API relies on). Amusingly, this restriction only impacts `who`; `w` bypasses this limitation entirely as it lacks a specific AppArmor profile.

***

*Original observations and discussion can be found on [Systemd, Shutdown, and Wall on Ubuntu 26.04](https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604ShutdownAndWall).*