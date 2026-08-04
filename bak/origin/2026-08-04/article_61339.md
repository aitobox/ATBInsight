# Argc and Argv in Early Research Unix

## Summary
This article explores the historical origins and evolution of `argc` and `argv` in early Research Unix—dating back to an era before the C programming language even existed. It examines how the redundancy of having both an argument count (`argc`) and a NULL-terminated array (`argv[]`) was handled across different versions of Unix (from V1 through V7 and into BSD/System V), revealing how the transition from raw assembly APIs to C, and the eventual introduction of environment variables, shaped modern program execution standards.

---

## Introduction

Recently, I was peripherally involved in a Fediverse discussion about (C's) `argc` and `argv` (the arguments passed to `main()`, marking the start of a C program). Famously, `argv[]` is an array of pointers to your program's arguments [including the nominal name of the program](https://utcc.utoronto.ca/~cks/space/blog/unix/Argv0IsEasy). 

It is a long-standing tradition to terminate this array with a NULL pointer—though this isn't strictly required by the base Single Unix Standard, whose [`execve()`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/execve.html) specification is silent on the matter. 

> **Update:** [Tony Finch](https://dotat.at/) pointed out that POSIX actually *does* specifically require `argv[]` to be NULL-terminated (and mandates that the NULL not be counted in `argc`).

If you think about it, having both `argc` and a NULL-terminated `argv` is technically redundant, since you could determine one from the other. This led me to wonder: how far back do `argc` and `argv` go in Unix, and was `argv` NULL-terminated from the beginning? 

The answer is that they go all the way back to **Research Unix V1** (which predates C), and `argv[]` **was not** originally NULL-terminated.

---

## Research Unix V1: The Assembly Era

The V1 [`exec(2)`](https://www.tuhs.org/cgi-bin/utree.pl?file=V1/man/man2/exec.2) manual page is very specific about both sides of the V1 `exec()` API, which was expressed purely in assembly language terms:

* `exec()` is called with a NULL-terminated array of pointers to the zero-terminated argument strings.
* However, the invoked program receives an explicit count of the arguments (`argc`) along with an array of argument pointers, and the array is *not* listed as NULL-terminated. 

Looking at the V1 kernel source code for `sysexec` (in [`u2.s`](https://www.tuhs.org/cgi-bin/utree.pl?file=V1/u2.s)), the kernel does not appear to append a final NULL pointer or any other marker after the regular `argv[]` pointers. Consequently, early programs had to rely strictly on `argc` to know when to stop reading the array.

---

## Versions 4 and 6: The `-1` Terminator

The logic behind this split between the `exec()` API and the program API becomes clearer when examining the C code for [V4 `exec()` in `sys/ken/sys1.c`](https://www.tuhs.org/cgi-bin/utree.pl?file=V4/usr/sys/ken/sys1.c). 

`exec()` needs to count the number of arguments in order to allocate the correct size for the `argv[]` array on the new program's stack. Having calculated that count, it conveniently passes it along to the new program as `argc`. 

However, if I am reading the V4 `exec()` correctly, it adds a final `-1` right after the normal end of the `argv[]` array:

```c
while(na--) {
  suword(ap=+2, c);
  do
    subyte(c++, *cp);
  while(*cp++);
}
suword(ap+2, -1);
```

This trailing `-1` persists all the way through the [V6 `exec()` in `sys/ken/sys1.c`](https://www.tuhs.org/cgi-bin/utree.pl?file=V6/usr/sys/ken/sys1.c). (Though why it was `-1` instead of `0` remains unclear to me; the [V6 `crt0.s`](https://www.tuhs.org/cgi-bin/utree.pl?file=V6/usr/source/s4/crt0.s) doesn't seem to make any visible checks for it.)

---

## Version 7: Environment Variables and NULL Separators

Finally, in the V7 `exece()` found in [`sys/sys.1`](https://www.tuhs.org/cgi-bin/utree.pl?file=V7/usr/sys/sys/sys1.c), we finally see an actual NULL pointer at the end of `argv[]`. 

However, this functions less like a terminator and more like a **separator**. As detailed in [The addition of environment variables in V7](https://utcc.utoronto.ca/~cks/space/blog/unix/V7GaveUsEnvironmentVariables), `argv[]` was transformed into two contiguous arrays of pointers stacked on top of each other:
1. One for the program arguments.
2. One for the user environment (which also required a NULL terminator so programs knew where it ended).

Based on how the C program startup script ([`libc/csu/crt0.s`](https://www.tuhs.org/cgi-bin/utree.pl?file=V7/usr/src/libc/csu/crt0.s)) handles its loops, I believe it finds the environment by walking the `argv[]` array until it hits the separator NULL—even though the kernel continues to provide `argc` alongside the `argv[]` array.

---

## BSD and System V Evolution

Both System III and 4.2 BSD continued to include this separating NULL. 
* In **4.x BSD**, it is quite explicit, featuring an explicit copy of `0` written into the user stack. 
* In **System III**, the user stack section appears to be pre-zeroed, allowing the code to simply bump the offset. 

BSD maintained this convention at least as late as **4.3 BSD Reno** ([cf. source](https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/src/sys/kern/kern_exec.c)). Similarly, historical repositories like [ryanwoodsmall/oldsysv](https://github.com/ryanwoodsmall/oldsysv/) indicate that **System V Release 2** for the VAX also separated `argv[]` and the environment using a NULL ([`vax/os/exec.c`](https://github.com/ryanwoodsmall/oldsysv/blob/master/sysvr2-vax/src/uts/vax/os/exec.c)).

If there were Unix systems that eventually moved away from putting a separating NULL between `argv[]` and the environment (thereby dropping `argv[]`'s terminating NULL), I am unaware of them. Instead, I suspect that either early C compilers on non-Unix systems omitted the NULL at the end of their makeshift `argv` implementations, or that early ANSI C and POSIX committees simply codified the practice because it was already ubiquitous.

*(Now you know why I was looking at `exec()` in early Unix and [came to understand its `argv` size limit](https://utcc.utoronto.ca/~cks/space/blog/unix/EarlyUnixExecArgvSizeLimit).)*

---

*Based on a post from the [Author's Blog](https://utcc.utoronto.ca/~cks/space/blog/unix/EarlyUnixArgcAndArgv).*