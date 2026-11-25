---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-25
hide:
  - navigation
tags:
  - APFS
  - macOS
  - Unicode
  - 文件系统
  - 安全漏洞
title: "APFS 中的 Unicode 正规化与大小写折叠如何引发安全漏洞"
---

# APFS 中的 Unicode 正规化与大小写折叠如何引发安全漏洞

> # How Normalisation and Case Folding in APFS Led to Vulnerabilities

### 文章背景与核心概要
Unicode 的高度灵活性使得同一字符在底层可以拥有多种二进制表示，这要求现代文件系统 (如 APFS) 必须妥善处理正规化 (Normalisation) 与大小写折叠 (Case Folding) 问题。Apple 在最初推出 APFS 时曾将其简单视作无须正规化的“字节包” (Bag of Bytes)，在引发严重数据混乱后才仓促补上正规化层，但也由此带来了极其复杂的底层字符映射行为。近期曝光的安全漏洞表明，当上层应用程序依靠逐字符比对来校验路径白名单，而底层大小写不敏感的文件系统却会将 `ss` 与德文字符 `ß` 等视作完全等价时，攻击者便可趁机绕过安全防护并恶意覆写关键系统文件。

---

## 概要

> ## Summary

Unicode 的高度灵活性允许完全相同的字符拥有多种不同的编码形式，这就要求 APFS 等现代文件系统必须引入正规化 (Normalisation) 与大小写折叠 (Case Folding) 机制。起初，Apple 将 APFS 简单视作无需正规化的“字节包” (Bag of Bytes)，这导致早期版本频现严重缺陷；尽管后来补充实现了正规化与大小写不敏感的大小写折叠，却也引入了极其复杂的处理行为。近期曝光的安全漏洞充分证明，当应用程序层面的字符串比对逻辑与文件系统底层的大小写折叠 (例如将 `ss` 与 `ß` 视作等价) 存在认知脱节时，极易被恶意攻击者利用，进而绕过安全检测并覆写关键文件。

> Unicode's flexibility allows identical characters to have multiple encodings, necessitating normalisation and case folding in modern file systems like APFS. While Apple initially treated APFS as a simple "bag of bytes" lacking normalisation—leading to severe early bugs—the eventual implementation of normalisation and case-insensitive case folding introduced complex behaviors. Recent security vulnerabilities demonstrate how mismatches between application-level string comparisons and file system-level case folding (such as equating `ss` with `ß`) can be exploited to bypass security checks and overwrite critical files.

---

## 1. Unicode 之谜与文件系统正规化

> ## 1. The Unicode Enigma and File System Normalisation

Unicode 最令人困扰的特性之一，便是在视觉上完全相同的字符往往可能拥有不止一种编码表达。这不仅包括像 `é` 和 `é` 这样常见的带重音符号字符，还涵盖了在非英语语言中广泛使用的 `Å`，以及东南亚某些非拉丁语系语言中的诸多字符。

> One of the most unfortunate features of Unicode is that some identical characters have more than one encoding. These include common accented characters such as `é` and `é`, as well as some that are used extensively in non-English languages like `Å`, and many in some non-Roman languages from South-East Asia.

正因如此，搜索与字符串比对等日常基础功能都必须将这些多义编码纳入考量，文件系统中使用的文件命名同样需要对它们进行一致性处理。在经典的 HFS+ 文件系统中，Apple 采取的解决方案是执行*正规化* (Normalisation)，确保文件系统底层仅采用其中唯一的一种编码形式。

> As a result, everyday features including search and string comparison need to take those into account, and names used in file systems also need to deal with them consistently. In HFS+, the solution is to perform *normalisation*, so only one of those encodings is used by the file system. 

然而，当 Apple 最初在 iOS 上推出 APFS 时，它却并未进行正规化处理，而只是将文件名原样当作一堆“字节包” (Bag of Bytes) 直接保存，并把避免负面后果的责任完全推给了开发者，要求开发者自行调用正确的操作系统接口来规避风险。

> When Apple first released APFS for iOS, it didn’t normalise, instead just storing names in the way that they came as a ‘bag of bytes’, and leaving it to developers to ensure they used the correct operating system calls to avoid adverse consequences.

### 迈向 High Sierra 的曲折之路

> ### The Road to High Sierra

事实证明，这种做法险些酿成灾难，就连 Apple 自家的原生应用也频频遭遇[严重问题](https://eclecticlight.co/2017/07/17/apfs-ios-11-and-high-sierra-will-fix-normalisation-problems/)。等到 macOS High Sierra 发布 APFS 时，Apple 被迫做出妥协，在 APFS 中增设了正规化层以化解混乱局面。这件事情似乎让官方感到颇为尴尬，以至于虽然它在[早期开发文档](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html#//apple_ref/doc/uid/TP40016999-CH6-DontLinkElementID_17)中被详尽提及，但在[现行参考文档](https://developer.apple.com/documentation/foundation/about-apple-file-system)或 [APFS Reference](https://developer.apple.com/support/downloads/Apple-File-System-Reference.pdf) 中却对此只字未提。

> That nearly proved disastrous, and even Apple’s apps were caught out with [severe problems](https://eclecticlight.co/2017/07/17/apfs-ios-11-and-high-sierra-will-fix-normalisation-problems/). By the release of APFS in High Sierra, Apple had been forced to change, and APFS had been given a normalisation layer to rescue it from chaos. This seems to have been so embarrassing that, while it’s addressed in detail in [early documentation](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html#//apple_ref/doc/uid/TP40016999-CH6-DontLinkElementID_17), there’s no mention of this in its [current equivalent](https://developer.apple.com/documentation/foundation/about-apple-file-system) or the [APFS Reference](https://developer.apple.com/support/downloads/Apple-File-System-Reference.pdf).

尽管正规化缺陷可能导致使用困扰和数据丢失，但由于它们主要涉及带重音符号的字符，因此通常极少会对系统安全造成实质性影响。

> While normalisation problems can result in frustration and data loss, because they mainly involve accented characters, they should seldom have a significant impact on security.

---

## 2. 大小写不敏感与大小写折叠映射

> ## 2. Case Insensitivity and Case Fold Mapping

APFS 的另一大特性在于它可以支持大小写敏感 (Case-sensitive) 或大小写不敏感 (Case-insensitive) 两种模式。除了 Time Machine 备份存储卷强制要求大小写敏感外，Mac 设备通常默认倾向于使用大小写不敏感模式。由于部分应用程序无法兼容大小写敏感的环境，因此 Mac 上的绝大多数 APFS 卷都是大小写不敏感的，例如它不允许仅大小写不同的两个目录或文件共存 (比如 `myFile.txt` 和 `myfile.txt`)。

> Another peculiarity of APFS is that it can be sensitive or insensitive to case, with Macs preferring the latter, except for Time Machine backup storage which is required to be case-sensitive. As some apps can’t cope with case sensitivity, most APFS volumes in Macs are case-insensitive and don’t allow, for example, the coexistence of two directories or files with names that differ only in case, such as `myFile.txt` and `myfile.txt`.

大小写不敏感的实现依赖于[大小写折叠映射](https://www.w3.org/TR/charmod-norm/#definitionCaseFolding) (Case Fold Mapping)，用以判定哪些字符在逻辑上仅仅是大小写的差异。令人惊讶的是，这其中不仅包括 `ss`、`SS` 及其组合，还包括德文字母 `ß` 及其大写形态 `ẞ`——在规则定义中，它们均被视作同一字符的不同大小写变体。

> Case-insensitivity relies on [case fold mapping](https://www.w3.org/TR/charmod-norm/#definitionCaseFolding) to determine which characters are considered to differ only in their case. You might be surprised to learn that includes `ss`, `SS` and combinations, `ß` and its capital form `ẞ`, which are all defined as being different cases of the same character.

### 大小写折叠的实际验证

> ### Demonstrating Case Folding

想要观察大小写折叠映射是如何运作的，可以在普通的 APFS 大小写不敏感卷中尝试并列创建两个文件夹，分别命名为 `strasse` 与 `straße`。大小写不敏感的 APFS 会直接拒绝创建第二个文件夹；但如果在大小写敏感的 APFS 卷中重复此操作，你会发现它们完全能够和谐共存，就像 `this` 和 `This` 一样。

> To see case fold mapping at work, in a regular case-insensitive APFS volume try creating two folders side by side with the names `strasse` and `straße`. Case-insensitive APFS will refuse the second of those, but repeat that in a case-sensitive APFS volume, where you’ll find they can happily coexist just as `this` and `This` can.

<a href="https://eclecticlight.co/wp-content/uploads/2026/11/casefold.jpg" rel="noopener noreferrer" referrerpolicy="no-referrer" target="_blank"><img src="http://localhost/proxy/DDH_AX07NJ7Oy4_c3nLlT7dYygv5UEhOyULv7YWdFV0=/aHR0cHM6Ly9lY2xlY3RpY2xpZ2h0LmNvL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzExL2Nhc2Vmb2xkLmpwZw==" alt="" width="518" height="591" srcset="http://localhost/proxy/DDH_AX07NJ7Oy4_c3nLlT7dYygv5UEhOyULv7YWdFV0=/aHR0cHM6Ly9lY2xlY3RpY2xpZ2h0LmNvL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzExL2Nhc2Vmb2xkLmpwZw== 518w, http://localhost/proxy/TpIo3n1FJl1MDZVy0fpSVaJuyCfzIRlBCNXqpVcOGxU=/aHR0cHM6Ly9lY2xlY3RpY2xpZ2h0LmNvL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzExL2Nhc2Vmb2xkLmpwZz93PTEzMSZoPTE1MA== 131w, http://localhost/proxy/9LshnVMIX_2wrncFES2IDGpJa7IBU0Vc1ZwwvVyBLJA=/aHR0cHM6Ly9lY2xlY3RpY2xpZ2h0LmNvL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzExL2Nhc2Vmb2xkLmpwZz93PTI2MyZoPTMwMA== 263w" sizes="auto, (max-width: 518px) 100vw, 518px" loading="lazy"/></a>

在大小写不敏感的 APFS 卷中，尽管名称可能包含两种不同的 `ü` 编码变体 (`c3 bc` 或 `75 cc 88`) 以及两种不同的 `ß/ss` 编码变体 (`c3 9f` 或 `73 73`) 等，但 `müßig`、`müßig`、`müssig`、`müssig` 以及它们的大写变体都会被视为完全同一的文件名。因此，大小写不敏感的 APFS 在对文件名计算哈希 (Hash) 之前，必须同时完成正规化与大小写折叠映射。

> In a case-insensitive APFS volume, the names `müßig`, `müßig`, `müssig`, `müssig` and their variants using capitals are treated as identical despite containing two variants of the `ü` (`c3 bc` or `75 cc 88`), and two variants of the `ß/ss` (`c3 9f` or `73 73`), etc. Thus, case-insensitive APFS has to perform both normalisation and case fold mapping of names before hashing them.

尽管 `ss` 和 `ß` (及其变体) 是大小写折叠中最著名的案例，但合字 (Ligatures) 也存在类似的映射效应。例如，连字 `ﬂ` (`ef ac 82`) 会被直接映射为普通字母组合 `fl` (`66 6c`)；此外还存在许多更为晦涩隐蔽的映射情况，其中某些甚至与具体语言语境强绑定。

> Although `ss` and `ß` (and variants) are the best-known examples of case folding, there are similar effects with ligatures, where `ﬂ` (`ef ac 82`) is mapped to `fl` (`66 6c`), for example, and there are more obscure instances, some of which are language-dependent.

---

## 3. 现实环境中的安全隐患

> ## 3. Real-World Security Implications

墨菲定律终究应验了：这种字符映射行为已被证实涉及多起[安全漏洞](https://kb.cert.org/vuls/id/604762)，尽管这一风险并不局限于 APFS 或 macOS 平台。正如业界早已明知、且在 APFS 过去的九年中不断被印证的那样——仅仅执行简单逐字符比对的上层软件，根本无法预判底层文件系统究竟会如何解析和处理这些字符串。

> The inevitable happened when this behavior was reported to be involved in multiple [security vulnerabilities](https://kb.cert.org/vuls/id/604762), although not strictly confined to APFS or macOS alone. As has been known all along—and demonstrated in APFS over the last nine years—software that performs simple character-by-character string comparisons fails to anticipate how file systems handle those strings.

### 安装程序安全漏洞攻击场景

> ### The Installer Vulnerability Scenario

* 存在安全缺陷的安装程序在写入文件前，会根据受保护的路径与文件名白名单进行安全检查；
* 例如，该安装程序需要严格保护名为 `noAccess.config` 的核心配置文件不被覆盖；
* 假设某个恶意安装包中包含了一个名为 `noAcceß.config` 的拟写入文件；
* 若仅采用简单的字符串匹配，由于两者字符序列乃至字节长度均不相同，系统不会将其标记为覆盖 `noAccess.config`；
* 然而，一旦将 `noAcceß.config` 复制到大小写不敏感的 APFS 卷上，**它将直接覆盖原有的 `noAccess.config`**，进而使攻击者达成恶意篡改目的。

> * A vulnerable installer checks the files it’s going to install against a list of protected paths and files. 
> * For example, it might need to preserve a vital file named `noAccess.config`. 
> * Suppose a malicious package contained a file to be installed as `noAcceß.config`. 
> * Using simple string matching, that wouldn’t be flagged as replacing `noAccess.config` because their names differ, even in their byte lengths. 
> * However, if `noAcceß.config` is copied to a case-insensitive APFS volume, **it will replace `noAccess.config`** and could then be exploited.

这再次生动表明，正规化与大小写折叠的复杂性，是如何直接引发编程逻辑缺陷并导致严重安全疏漏的。

> This is yet another clear demonstration of how complexity in normalisation and case folding leads directly to coding errors and security oversight.

---

*非常感谢 Jim 指出这份漏洞报告。*

> *I’m very grateful to Jim for pointing out this vulnerability report.*
