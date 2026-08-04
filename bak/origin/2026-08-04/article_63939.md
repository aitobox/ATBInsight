# Getting Access to the `/tmp` of a Systemd Service with `PrivateTmp=yes`

## Summary
When troubleshooting systemd services that utilize `PrivateTmp=yes` or `DynamicUser=yes`, accessing their temporary files can be tricky because systemd isolates their `/tmp` directories. This guide explains how to locate standard private temporary directories on the host, how to use `nsenter` to access completely disconnected namespaces, and how to extract files from locked-down environments using clever shell redirection.

---

## Locating Standard Private Temporary Directories (`PrivateTmp=yes`)

When a systemd service is configured with `PrivateTmp=yes`, systemd routes its `/tmp` and `/var/tmp` directories to a dedicated path on the host rather than the standard `/tmp`. 

The path typically follows this structure:
`/tmp/systemd-private-<hex>-<service>-<jumble>/tmp`

* The large `<hex>` value remains constant across all services.
* The `<jumble>` value is randomized.

As noted in the [systemd.exec manual page](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#PrivateTmp=):
> *"If 'true', the backing storage of the private temporary directories will remain on the host's /tmp/ and /var/tmp/ directories. [...]"*

---

## Handling Disconnected Temporary Directories (`PrivateTmp=disconnected`)

You can also configure `PrivateTmp=disconnected` (a setting implicitly enabled by [`DynamicUser=yes`](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#DynamicUser=)) to give a service a completely detached `/tmp` on a new `tmpfs`. 

Because this disconnected `/tmp` is not mounted or available outside of the process's specific namespace, you must enter it explicitly using [`nsenter`](https://www.man7.org/linux/man-pages/man1/nsenter.1.html):

```bash
nsenter -t <pid> -m
```

Running this command as `root` starts a shell within that mount namespace, making the program's `/tmp` your `/tmp`. 

To inspect which processes have active namespaces, you can use [`lsns(8)`](https://www.man7.org/linux/man-pages/man8/lsns.8.html):
```bash
lsns -t mnt
```
*(Note: Distinguishing between a merely private `/tmp` and a disconnected `/tmp` via `lsns` is not always straightforward.)*

---

## Sidebar: Copying Files Out of a Namespace the Hard Way

If you are dealing with a heavily locked-down systemd service with a disconnected `/tmp`, using `nsenter` directly can trap you inside a restrictive mount namespace where everything else may be read-only. 

To bypass this restriction and extract debugging files, you can exploit the fact that standard output redirection is handled by your host shell *before* `nsenter` switches the meaning of `/tmp`:

```bash
nsenter -t <pid> -m cat /tmp/whatever > /tmp/whatever-out
```

### How it works:
1. The host shell sets up the output redirection (`> /tmp/whatever-out`) targeting the **real** host `/tmp`.
2. [`nsenter`](https://www.man7.org/linux/man-pages/man1/nsenter.1.html) runs `cat` inside the target namespace with its switched `/tmp`.
3. `cat` reads the disconnected debugging file and pipes its contents out to the host system.

> **Idea for a helper script:** An enterprising administrator could wrap this pattern into an `nscp` utility (e.g., `nscp <pid>:/tmp/whatever /tmp/out`), with potential extensions to copy files both in and out of isolated namespaces.

***

*Original commentary and source: [UTCC Blog](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdPrivateTmpWhere)*