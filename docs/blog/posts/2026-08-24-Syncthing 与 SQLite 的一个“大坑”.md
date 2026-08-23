---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-24
hide:
- navigation
tags:
- Syncthing
- SQLite
- POSIX
- 数据库同步
- 系统编程
title: Syncthing 与 SQLite 的一个“大坑”
---
### 文章背景与核心概要
本文探讨了在使用 Syncthing 跨多台设备同步 SQLite 数据库时容易遇到的一个隐蔽 Bug。当应用（如运行中的 Web 服务）保持着数据库文件的打开状态时，由于 Syncthing 采用了原子 `rename`（重命名）操作来更新文件，应用会继续读取旧的、已被解除目录映射的 inode（索引节点），而无法感知到新同步进来的数据库内容，直到重启应用。

文章通过作者自身的日记应用 Epoch 在桌面端与笔记本端同步的实际经历，分析了该问题的表象，并深入剖析了 POSIX 文件系统的底层语义。核心原因在于：文件系统的 `rename` 操作仅改变目录项到文件的路径映射，而完全不会影响已经存在的打开文件描述符。理解这一点对于处理分布式文件系统与状态持久化组件的结合至关重要。

---

## The Setup / 配置环境

I use [Epoch](https://github.com/eudoxia0/epoch), a tiny Rust web app that runs as a systemd service and uses [SQLite](https://sqlite.org/) as its database, to keep a journal. 

> 我使用 [Epoch](https://github.com/eudoxia0/epoch) 来写日记。它是一个小型的 Rust Web 应用，作为 systemd 服务运行，并使用 [SQLite](https://sqlite.org/) 作为其数据库。

I regularly use both a desktop and a [laptop](/article/linux-on-the-fujitsu-lifebook-u729), using [Syncthing](https://syncthing.net/) to synchronize them—including Epoch’s database. This allows me to use the app on both devices without needing a central server. The only tradeoff is that I have to make sure the sync is finished before performing any mutations.

> 我经常同时使用台式机和[笔记本电脑](/article/linux-on-the-fujitsu-lifebook-u729)，并使用 [Syncthing](https://syncthing.net/) 在它们之间进行同步——包括 Epoch 的数据库。这使我能够在两台设备上使用该应用，而无需中心服务器。唯一的权衡是，我必须确保在执行任何写入修改之前同步已经完成。

---

## The Bug / 漏洞表现

I ran into a persistent bug: 
1. I edit today’s entry on the laptop.
2. I come home and wait for Syncthing to finish syncing.
3. I open today’s entry on the desktop, but the text is missing.

> 我遇到了一个挥之不去的 Bug：
> 1. 我在笔记本上编辑今天的条目。
> 2. 我回到家，等待 Syncthing 完成同步。
> 3. 我在台式机上打开今天的条目，但文本不见了。

It wasn't a file-locking issue preventing the sync. Opening the database with the `sqlite3` command-line tool confirmed the new text was actually there. However, the running server couldn't see it; simply restarting the server allowed Epoch to read the new text immediately.

> 这并不是阻止同步的文件锁定问题。使用 `sqlite3` 命令行工具打开数据库，证实新的文本确实已经存在了。然而，正在运行的服务端却看不到它；简单地重启服务端就能让 Epoch 立即读取到新文本。

My initial mental model was:
> The [rusqlite](https://github.com/rusqlite/rusqlite) `Connection` object points to the database file. Syncthing swaps the file’s contents from under it. Subsequent queries should automatically go to the new file.

> 我最初的心智模型是这样的：
> > [rusqlite](https://github.com/rusqlite/rusqlite) 的 `Connection` 对象指向数据库文件。Syncthing 在它眼皮底下悄悄替换了文件的内容。随后的查询应该会自动导向新文件。

---

## The Reality of POSIX Filesystems / POSIX 文件系统的现实

It turns out there is a crucial part of POSIX filesystem semantics I was missing. 

> 事实证明，我漏掉了 POSIX 文件系统语义中至关重要的一部分。

The standard way to replace a file safely (i.e., atomically) is via the [`rename`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html) system call, which Syncthing uses:

> 安全地（即原子性地）替换文件的标准方法是通过 [`rename`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html) 系统调用，这也是 Syncthing 所使用的方式：

```c
int rename(const char *old, const char *new);
```

What happens if another process already has an open file descriptor pointing to `new`? Do they see the new contents? 

> 如果另一个进程已经拥有一个指向 `new` 的打开文件描述符，会发生什么？它们能看到新的内容吗？

**No.** Those processes continue reading and writing to the old file *object*. The file is effectively orphaned because no directory path points to it anymore. Once all active file descriptors to that old file are eventually released, the file data becomes inaccessible.

> **不能。** 这些进程会继续对旧的*文件对象*进行读写。该文件实际上已经变成了“孤儿”，因为再也没有任何目录路径指向它了。一旦指向该旧文件的所有活动文件描述符最终被释放，该文件的数据就会彻底无法访问。

### A Shift in Mental Models / 心智模型的转变

I was used to thinking of filesystem operations in terms of paths mapping directly to mutable file pointers. In reality, `rename` works entirely at the level of directory entries: **it atomically mutates the mapping from pathnames to files, but leaves existing open file descriptors completely untouched.**

> 我过去习惯于从“路径直接映射到可变文件指针”的角度来思考文件系统操作。但实际上，`rename` 完全是在目录项的层面上运作的：**它原子性地改变了路径名到文件的映射，但完全不会触及现有的、已打开的文件描述符。**