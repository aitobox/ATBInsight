---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-09-18
hide:
  - navigation
tags:
  - Git
  - 对象存储
  - S3
  - Packfile
  - 底层系统
title: "重构 Packfile：在对象存储上直接运行 Git 的架构实践"
---

# 重构 Packfile：在对象存储上直接运行 Git 的架构实践

> # You Can Run Git on Object Storage If You Re-Make Packfiles

### 文章背景与核心概要
将 Git 存储服务直接构建在低成本、高弹性的云端对象存储 (例如 AWS S3 或 Tigris) 之上，是许多团队探索云原生存储架构与降低运维开销的理想方案。然而，标准 Git 的 Packfile 打包机制是为本地磁盘设计的，严重依赖微秒级的内核内存映射 `mmap` 与高并发随机寻道；一旦搬到存在数十毫秒网络往返延迟的对象存储上，性能便会迅速恶化至不可用的状态。为了彻底攻克这一难题，开发者借鉴了经典 CD-ROM 光盘中 `.bin`/`.cue` 音轨索引的分离设计，提出了一种专为对象存储定制的列式 Packfile 格式，并巧妙利用精准的 HTTP Range 范围请求与异步预取机制。这一架构突破将 S3 API 请求量削减了数个数量级，在生产级基准测试中使代码推送与克隆提速高达 14.6 倍，为现代分布式版本控制与云端底层系统架构开辟了全新路径。

---

## 核心概要

> ## Summary

构建一个以对象存储 (Object Storage) (例如 Tigris) 为底座的 Git 服务器，听起来似乎很直观：只需搭建一层文件系统转译层，让 Git 能够操作对象存储即可。然而，标准的 Git Packfile 是为本地磁盘量身设计的，高度依赖操作系统内核的 `mmap` 内存映射以及低延迟的本地文件系统极速读取。一旦将这些读取操作映射为跨越网络的对象存储往返，面对生产环境级别的大型仓库时，这种方案的扩展性便会彻底崩溃。

> Building a Git server backed by object storage (like Tigris) sounds straightforward: use a filesystem translation layer so Git can speak object storage. However, standard Git packfiles are designed for local disks and rely heavily on the kernel's `mmap` and fast, low-latency filesystem reads. When translated over network round-trips to object storage, this approach fails to scale for production-sized repositories. 

为了解决这个问题，作者从老式 CD-ROM 光盘的 `.bin`/`.cue` 索引单中汲取灵感，发明了一种专为对象存储原生打造的全新 Packfile 格式。通过构建一个带有二进制索引文件 (`objects.cue`) 的列式存储结构，索引中同时记录了精确的文件偏移量以及压缩与解压后的双重尺寸，客户端得以发起高效的 HTTP Range 范围请求。这一专属设计不仅大幅削减了访问 S3/对象存储的请求次数，更将代码推送 (push) 和克隆 (clone) 的性能最高提升了整整 14.6 倍。

> To solve this, the author invented an object-storage-native packfile format inspired by CD-ROM `.bin`/`.cue` sheets. By creating a columnar store with a binary index (`objects.cue`) containing both compressed and uncompressed sizes alongside precise file offsets, clients can execute efficient HTTP Range requests. This custom approach drastically reduced S3/object storage requests and accelerated push/clone performance by up to 14.6x.

---

## Git 到底是什么？不过是一堆可怜的零散对象！

> ## What is Git? A Miserable Little Pile of Objects!

当你提交一次代码时，Git 会把你的改动作为经过压缩的、基于内容寻址的对象 (Content-Addressed Objects) 保存在 `.git` 目录中 (本文称之为“dotgit”)。

> When you make a commit, Git stores your changes as compressed, content-addressed objects inside the `.git` directory (referred to here as "dotgit"). 

```bash
$ mkdir ~/tmp/gitexample
$ git init && git branch -m main
$ echo "Hello, blog!" >> hello.txt
$ git add .
$ git commit -sm "chore: initial commit"
```

这一操作会在底层生成一片由裸对象和具名引用构成的“对象之海”：

> This produces a sea of bare objects and named references:

<figure><figcaption>图 01: 对象的海洋与指向它们的引用命名</figcaption><pre>  .git/objects/                    refs/heads/main                                     │  ├── 1c/7a26a901..ec7966  ─────▶  commit 1c7a26a  │                                  │  ├── 8e/67afbb2e..857bd3  ─────▶    tree 8e67afb  │                                  │  hello.txt  └── 9c/c9867337..09fe26  ─────▶    blob 9cc9867                                          "Hello, blog!"   the filename is the sha1 of the bytes in the file, so the same  content is always, everywhere, the very same object</pre></figure>

读取其中的某个对象需要对其进行解压：

> Reading an object requires decompressing it:

```bash
$ file .git/objects/**/* | grep -v directory
.git/objects/1c/7a26a901724b4ce766655ac387413fb9ec7966: zlib compressed data
.git/objects/8e/67afbb2ee6bdcbb79061dfdfb93febce857bd3: zlib compressed data
.git/objects/9c/c9867337c2ebae85ba2350f901e0bcc209fe26: zlib compressed data

$ python3 -c "import sys, zlib; sys.stdout.buffer.write(zlib.decompress(sys.stdin.buffer.read()))" < .git/objects/9c/c9867337c2ebae85ba2350f901e0bcc209fe26
blob 13Hello, blog!
```

### inode 节点上限与 Packfile 打包文件

> ### The Inode Limit and Packfiles

对于像 Linux 内核这样的大型代码仓库，如果存储数以百万计的松散文件，很快就会触及文件系统的 inode 节点上限。Git 解决这一难题的武器正是 **Packfile**——将海量零散对象打包并压缩进单一文件的大包：

> For large repositories like the Linux kernel, storing millions of loose files hits inode limits. Git solves this using **packfiles**—compressed bundles that store multiple objects in a single file:

```bash
$ git count-objects -v
count: 756
size: 3500
in-pack: 448
packs: 1
size-pack: 321
prune-packable: 0
garbage: 0
size-garbage: 0
```

你可以使用 `git gc` 命令强制 Git 将松散对象打包归档。

> You can force Git to pack loose objects using `git gc`.

---

## Packfile 遭遇的网络延迟难题

> ## The Network Latency Problem with Packfiles

像 Linux 内核这样体量的仓库，包含了打包在数个吉字节 (GB) 庞大 Packfile 中的数百万个对象：

> A repository like the Linux kernel contains millions of objects bundled into multi-gigabyte packfiles:

```bash
xe@zohar:~/Code/linux.git$ git count-objects -v
count: 0
size: 0
in-pack: 11827138
packs: 1
size-pack: 3876775
prune-packable: 0
garbage: 0
size-garbage: 0
```

本地文件系统能够借助 `mmap` 进行近乎瞬时完成的内存映射磁盘读取 (耗时在微秒级别)，而跨越网络访问对象存储的往返耗时却长达数毫秒——这意味着照搬原生 Packfile 处理机制在网络上运行会慢上成千上万倍。

> While local filesystems leverage `mmap` for near-instantaneous memory-mapped disk reads (microseconds), network round-trips to object storage take milliseconds—making native packfile handling millions of times slower. 

雪上加霜的是，标准 Git Packfile 索引记录的仅仅是对象的*解压后*大小，根本不提供其压缩后的精确尺寸，导致你无法精准构造出只读取该对象字节区间的 **HTTP Range 范围请求**。

> Furthermore, standard Git packfile indices only reveal the *decompressed* size of an object, leaving you without the compressed size required to construct an accurate **HTTP Range request**.

<figure><figcaption>图 02: 1100 万个对象、一个 Packfile 与一个索引</figcaption><pre>  $ git count-objects -v          .git/objects/pack/  count:            0             └── pack-45986f41..c5786.pack   3.7 GiB  in-pack:   11827138  packs:            1             eleven million loose files would be  size-pack:  3876775             eleven million inodes. so: one file.    .idx                             .pack  ┌───────────────────────┐       ┌──────────────────────────────────────┐  │ 0002ff4c..  0x0000c   │       │███ ██ ████ █ ███████ ██ █ ████ ██████│  │ 0031ab90..  0x0a13f   │       └──────────────────────────────────────┘  │ 1c7a26a9..  0x1f3a4   │  │ ...                   │  └───────────────────────┘   each row's colour is the run of bytes its offset points at, so a  read is a seek to an offset inside one very big file</pre></figure>

<figure><figcaption>图 03: 一次范围 GET 请求：从 128 MiB 中间精准读取 366 字节</figcaption><pre>  packs/019a7f3c..bin  ┌────────────────────────────────────────────────┐  │                                   ██           │  └───────────────────────────────────▲────────────┘   0                                  │      128 MiB                                      └── 366 bytes, right here   you know where it starts and how long it is, so ask for  exactly that span and nothing else:   GET /packs/019a7f3c..bin  Range: bytes=100663296-100663661   and that is all the bucket sends back:   206 Partial Content  Content-Range: bytes 100663296-100663661/134217728  ┌────┐  │████│  366 B on the wire, not 128 MiB  └────┘</pre></figure>

---

## Packfile 2.0：对象存储狂想曲

> ## Packfiles v2: Object Storage Boogaloo

为了攻克这一瓶颈，作者受到早期复古 CD-ROM 光盘中 `.bin` 镜像与 `.cue` 索引单的启发，量身定制了一套全新的 Packfile 格式。

> To bridge the gap, the author designed a custom packfile format inspired by CD-ROM `.bin` and `.cue` sheets. 

### `.bin` 与 `.cue` 解决之道

> ### The `.bin` and `.cue` Solution

就像 CD 光盘的 cue 索引单通过精准记录各音轨位置、使播放器无需通读整张光盘就能任意寻道跳转一样，`objgit` 也将一份二进制数据文件 (`.bin`，上限通常为 128Mi) 与一份二进制编码的索引清单 (`.cue`) 成对组合。

> Just as CD cue sheets map out tracks to let players seek arbitrary points in a binary audio file without reading the whole disc, `objgit` pairs a binary data file (`.bin`, up to 128Mi) with a binary-encoded cue sheet (`.cue`).

<figure><figcaption>图 04: CD 光盘 cue sheet 与 objgit cue sheet 解决的是同一个问题</figcaption><pre>CD AUDIO DISC                                   OBJGIT PACKFILE──────────────────────────────────────────      ──────────────────────────────────────────U0008_0000002_0000147.WAV    one big file       objects.bin                  one big file┌──────────┬─────────────┬─────────────────┐    ┌──────────┬─────────────┬─────────────────┐│ track 01 │  track 02   │       ...       │    │  blob A  │   tree B    │       ...       │└──────────┴─────────────┴─────────────────┘    └──────────┴─────────────┴─────────────────┘  ▲          ▲                                    ▲          ▲  │ 00:00    │ 00:13                              │ @0       │ @142 FILE.cue     plain text, parsed top-down        objects.cue  packed records, fixed width┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐│ FILE "U0008_0000002_0000147.WAV" WAVE    │    │ HEADER                              16 B ││                                          │    │   magic  version  rec_size  record_count ││ TRACK 01 AUDIO                           │    ├──────────────────────────────────────────┤│ INDEX 01 00:00                           │    │ RECORD 0                            58 B ││ TITLE "U0008_0000002_0000147_0001"       │    │   hash 3a7f…c21        type blob         ││                                          │    │   comp zstd            size 311          ││ TRACK 02 AUDIO                           │    │   bin_offset 0         bin_length 142    ││ INDEX 01 00:13                           │    │   delta_base 0000…0000                   ││ TITLE "U0008_0000002_0000147_0002"       │    ├──────────────────────────────────────────┤└──────────────────────────────────────────┘    │ RECORD 1                            58 B │                                                └──────────────────────────────────────────┘to reach track 2 a player parses everyline above it. it already has the disc.         record N sits at 16 + N*58. one seek,                                                then one ranged GET into objects.bin.</pre></figure>

### Objgit 的列式存储格式

> ### Objgit's Columnar Format

这种全新定制格式在记录 Packfile 偏移量的同时，一并保存了对象压缩后与解压后的双重尺寸。这使得客户端可以直接向 Tigris 发起精准的 HTTP Range 请求，在后台异步下载整包文件的同时，先人一步拉取到当前所需的目标对象。

> The custom format stores both compressed and uncompressed sizes alongside packfile offsets. This enables precise HTTP Range requests to extract individual objects from Tigris while the packfile downloads asynchronously in the background.

<figure><figcaption>图 05: 线上传输中的 objects.cue：一个文件头，紧随固定宽度的记录结构</figcaption><pre>objects.cue HEADER   16 bytes, once at the top of the file┌──────────────┬─────────┬──────────┬────────────────────┐│ magic "OGCU" │ version │ rec_size │ record_count       ││          4 B │ u16 2 B │ u16  2 B │ u64            8 B │└──────────────┴─────────┴──────────┴────────────────────┘0              4         6          8                   16 objects.cue RECORD   58 bytes, repeated record_count times┌──────────────┬──────┬──────┬────────────┬────────────┬────────┬──────────────┐│ hash         │ type │ comp │ bin_offset │ bin_length │ size   │ delta_base   ││ sha1  20 B   │ u8 1B│ u8 1B│ u64   8 B  │ u32   4 B  │ u32 4B │ sha1  20 B   │└──────────────┴──────┴──────┴────────────┴────────────┴────────┴──────────────┘0              20     21     22           30           34       38            58 identity hash, delta_base   location bin_offset, bin_length   decode type, comp, size</pre></figure>

<figure><figcaption>图 06: 竞速预取：当整包后台下载进度刚到 2 MiB 时并发发起的四个范围 GET 请求</figcaption><pre>  git wants four objects out of packs/019a7f3c..bin                        A        B             C          D                       ▼        ▼             ▼          ▼              ┌────────────────────────────────────────────────┐  container   │░░░░░░█████░░░░█████░░░░░░░░░█████░░░░░░█████░░│              └────────────────────────────────────────────────┘   five requests go out at once:   A   16 MiB  │      █████                                     │  done       B   40 MiB  │               ████░                            │  cancelled  C   77 MiB  │                             █████              │  done       D  107 MiB  │                                        ███░░   │  cancelled  whole file  │████████████████████████████████████████████████│  done        four ranged GETs race the background download of the whole  file. whatever the download reaches stops needing a GET.</pre></figure>

---

## 性能基准测试

> ## Performance Benchmarks

团队在三个具有代表性的代码仓库中，对这种全新的列式 `.bin`/`.cue` 打包方案进行了基准测试：

> The new columnar `.bin`/`.cue` packfile approach was benchmarked across three repositories:

* **objgit**：一个较新的原型代码仓库。
* **Xe/x**：一个持续活跃开发了十余年的单体大仓库 (Monorepo)。
* **tigris-blog**：一个包含大量图片和不可压缩静态资源的博客仓库。

> * **objgit**: A newer prototype repository.
> * **Xe/x**: A monorepo active for over a decade.
> * **tigris-blog**: A repository containing images and incompressible assets.

### 代码推送 (Push) 测试

> ### Push Tests

<figure><figcaption>图 07: Push 操作产生的 S3 请求数对比 (格式改造前后，对数坐标)</figcaption><pre>              1         10        100       1,000     10,000              ├─────────┼─────────┼─────────┼─────────┤   objgit    old       ████████████████████████                     231    new       █████████████                                 18   Xe/x    old       ████████████████████████████████████████   9,236    new       ███████████████                               30   tigris-blog    old       ███████████████████████████████████        3,324    new       █████████████████████                        136   ██ old  git packfiles behind a filesystem shim  ██ new  .bin/.cue columnar packfiles</pre></figure>

| 仓库 | 构建版本 | 耗时 | S3 请求数 | PUT | GET | HEAD | LIST | Keys | 存储桶字节数 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| objgit | 旧版 | 8.7s | 231 | 46 | 47 | 0 | 138 | 42 | 829.27 KiB |
| objgit | 新版 | **2.2s** | **18** | 5 | 10 | 0 | 3 | 4 | 902.98 KiB |
| x | 旧版 | 3m29.4s | 9,236 | 1,087 | 2,170 | 0 | 5,979 | 1,082 | 54.96 MiB |
| x | 新版 | **14.3s** | **30** | 6 | 20 | 0 | 4 | 4 | 46.38 MiB |
| tigris-blog | 旧版 | 2m13.4s | 3,324 | 515 | 522 | 0 | 2,287 | 511 | 354.67 MiB |
| tigris-blog | 新版 | **26.5s** | **136** | 9 | 123 | 0 | 4 | 8 | 360.75 MiB |

> | Repo | Build | Wall | S3 requests | PUT | GET | HEAD | LIST | Keys | Bucket bytes |
> | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
> | objgit | old | 8.7s | 231 | 46 | 47 | 0 | 138 | 42 | 829.27 KiB |
> | objgit | new | **2.2s** | **18** | 5 | 10 | 0 | 3 | 4 | 902.98 KiB |
> | x | old | 3m29.4s | 9,236 | 1,087 | 2,170 | 0 | 5,979 | 1,082 | 54.96 MiB |
> | x | new | **14.3s** | **30** | 6 | 20 | 0 | 4 | 4 | 46.38 MiB |
> | tigris-blog | old | 2m13.4s | 3,324 | 515 | 522 | 0 | 2,287 | 511 | 354.67 MiB |
> | tigris-blog | new | **26.5s** | **136** | 9 | 123 | 0 | 4 | 8 | 360.75 MiB |

<figure><figcaption>图 08: Push 操作耗时对比 (对数坐标，右侧标注加速倍数)</figcaption><pre>              1s          10s         100s        1,000s              ├───────────┼───────────┼───────────┤   objgit    old       ███████████                              8.7s    new       ████                                     2.2s   4.0x   Xe/x    old       ████████████████████████████          3m29.4s    new       ██████████████                          14.3s  14.6x   tigris-blog    old       ██████████████████████████            2m13.4s    new       █████████████████                       26.5s   5.0x   ██ old  git packfiles behind a filesystem shim  ██ new  .bin/.cue columnar packfiles</pre></figure>

### 代码克隆 (Clone) 测试

> ### Clone Tests

<figure><figcaption>图 09: Clone 操作产生的 S3 请求数对比 (格式改造前后，对数坐标)</figcaption><pre>              1         10        100       1,000     10,000              ├─────────┼─────────┼─────────┼─────────┤   objgit    old       █████████████████████████                    323    new       ████████████                                  17   Xe/x    old       ████████████████████████████████████       6,428    new       ████████████                                  17   tigris-blog    old       ████████████████████████████████████       3,675    new       ██████████████████████                       158   ██ old  git packfiles behind a filesystem shim  ██ new  .bin/.cue columnar packfiles</pre></figure>

| 仓库 | 构建版本 | 耗时 | S3 请求数 | GET | HEAD | LIST | 线上传输字节数 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| objgit | 旧版 | 11.8s | 323 | 51 | 0 | 272 | 763.63 KiB |
| objgit | 新版 | **2.6s** | **17** | 13 | 0 | 4 | 767.96 KiB |
| x | 旧版 | 3m23.5s | 6,428 | 1,091 | 0 | 5,337 | 40.68 MiB |
| x | 新版 | **54.4s** | **17** | 13 | 0 | 4 | 42.22 MiB |
| tigris-blog | 旧版 | 2m23.6s | 3,675 | 520 | 0 | 3,155 | 350.94 MiB |
| tigris-blog | 新版 | **1m22s** | **158** | 155 | 0 | 3 | 349.04 MiB |

> | Repo | Build | Wall | S3 requests | GET | HEAD | LIST | Wire bytes |
> | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
> | objgit | old | 11.8s | 323 | 51 | 0 | 272 | 763.63 KiB |
> | objgit | new | **2.6s** | **17** | 13 | 0 | 4 | 767.96 KiB |
> | x | old | 3m23.5s | 6,428 | 1,091 | 0 | 5,337 | 40.68 MiB |
> | x | new | **54.4s** | **17** | 13 | 0 | 4 | 42.22 MiB |
> | tigris-blog | old | 2m23.6s | 3,675 | 520 | 0 | 3,155 | 350.94 MiB |
> | tigris-blog | new | **1m22s** | **158** | 155 | 0 | 3 | 349.04 MiB |

<figure><figcaption>图 10: Clone 操作耗时对比 (对数坐标，右侧标注加速倍数)</figcaption><pre>              1s          10s         100s        1,000s              ├───────────┼───────────┼───────────┤   objgit    old       ███████████                           11.8s    new       █████                                    2.6s   4.5x   Xe/x    old       ████████████████████████████          3m23.5s    new       █████████████████████                   54.4s   3.7x   tigris-blog    old       ██████████████████████████            2m23.6s    new       ███████████████████████               1m22.0s   1.8x   ██ old  git packfiles behind a filesystem shim  ██ new  .bin/.cue columnar packfiles</pre></figure>

---

## 总结与展望

> ## Conclusion

尽管 Git 原生的 Packfile 格式在本地文件系统上表现极其出色，但面对网络往返延迟时却显得力不从心甚至陷入崩溃。通过将 Packfile 大胆重构为专为对象存储优化的列式 `.bin`/`.cue` 双文件架构，不仅可以成百上千倍地削减 S3 API 调用次数，更能让代码推送和克隆操作变得如丝般敏捷轻快。

> While Git's default packfile format excels on local filesystems, it collapses under network round-trip latencies. Re-architecting packfiles into a columnar `.bin`/`.cue` structure optimized for object storage drastically cuts down S3 request counts and makes pushing and cloning fast and responsive. 

*注：类似 `objgit` 这样的项目目前仍处于实验探索阶段——身份认证、权限管控以及自动化的 Packfile 压实合并 (compaction) 机制仍在紧锣密鼓的开发中。*

> *Note: Projects like `objgit` are still experimental—authentication, authorization, and automated packfile compaction are still under development.*

*[展示 Git 存储层级演进的“渐进脑洞”表情包]*

> *[Expanding brain meme showing Git's storage layers]*

<img src="./images/7ddb287d2c5a.webp" alt="Expanding brain meme. Small brain: git stores diffs against an empty folder. Bigger brain: git stores the entire files for every version. Galaxy brain: git stores diffs against an empty folder." loading="lazy"/>
