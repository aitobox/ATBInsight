# How My Desktops Wound Up with Multiple D-Bus User Session Instances

## Summary
The author shares a historical sysadmin journey explaining why their Linux machines were running redundant D-Bus session daemons. Because they use a custom window manager environment instead of a standard desktop environment or graphical login manager, they historically had to manually launch D-Bus via `dbus-launch` in their startup scripts. When systemd later introduced its own native D-Bus session management, the author's custom scripts failed to adapt, resulting in duplicate D-Bus daemons running concurrently.

---

## 1. Introduction: The Custom Desktop Problem
As discussed in previous explorations of [systemd and user D-Bus session buses](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdAndUserDBusSessionBus), some of my machines were inadvertently starting an extra D-Bus session bus daemon. After some experimentation, I've realized this is neither necessary nor proper, and I have finally stopped doing it. 

How did I end up in this situation? It is a story rooted in history.

On [my primary desktops](https://utcc.utoronto.ca/~cks/space/blog/linux/MyThreeDesktops), I have never used standard graphical login managers like `gdm` or `xdm` ([long considered a bit of heresy](https://utcc.utoronto.ca/~cks/space/blog/unix/XDMHeresy)), nor do I run a standard desktop environment. Instead, [I use my own custom window manager environment](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/MyDesktopTour). This means I am responsible for orchestrating everything required to start the X server and my session—tasks that a standard desktop environment normally handles automatically.

## 2. The Pre-Systemd Era: Manual D-Bus Startup
D-Bus predates systemd on Linux. In those early days, starting your user D-Bus session daemon was the responsibility of your desktop environment—either internally or by placing scripts into the standard `/etc/X11/xinit/xinitrc.d` directory for graphical login managers to pick up.

Because I lacked a standard desktop environment, I had to research what was normally run on session startup and replicate it inside my own shell scripts. One of those steps was running [`dbus-launch`](https://dbus.freedesktop.org/doc/dbus-launch.1.html) with the appropriate arguments. In my configuration, `dbus-launch` unconditionally started a D-Bus session daemon and set `$DBUS_SESSION_BUS_ADDRESS` to point to it.

In the pre-systemd days, this approach worked fine:
* Regular console logins didn't automatically start a D-Bus session daemon.
* The D-Bus session bus address lived in `/tmp`, meaning files could occasionally be affected by edge cases, but failures were rare enough that I rarely noticed.

## 3. The Systemd Shift and Configuration Drift
When systemd began providing [its own native D-Bus setup](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdAndUserDBusSessionBus), the official `/etc/X11/xinit/xinitrc.d` scripts were updated to detect systemd and step aside rather than spawning redundant D-Bus daemons. Standard desktop environments updated themselves similarly.

However, my custom scripts missed this memo:
1. When I logged into the console, systemd automatically set up the proper D-Bus infrastructure ([provided my session fell into the correct class](https://utcc.utoronto.ca/~cks/space/blog/linux/Systemd258UsersAndSessions)).
2. My [`xinit`](https://x.org/releases/X11R7.6/doc/man/man1/xinit.1.xhtml)-based scripts would then immediately execute `dbus-launch`, spinning up a *second* D-Bus daemon and overriding systemd's setup.

This highlights one of the major challenges of maintaining a custom desktop environment: **you are entirely responsible for keeping up with upstream changes**, and you lack access to the informal communication channels shared by mainstream desktop developers. No doubt there are other areas where my environment has drifted away from modern best practices.

## 4. A Potential Catch with the New Approach
Switching away from `dbus-launch` to rely purely on systemd is cleaner, but it introduces one notable difference between the two approaches:
* **The old approach:** Started the D-Bus session daemon with a fully initialized environment (spawned from my login shell after logging in).
* **The new approach:** Starts the daemon with whatever minimal environment it inherits directly from `systemd --user`. 

Only time will tell if this difference causes any downstream issues. 

*(You can read [the comment discussion on this topic](https://utcc.utoronto.ca/~cks/space/blog/linux/HowMyMultipleDBusInstances?showcomments#comments).)*