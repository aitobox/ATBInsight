---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-01
hide:
- navigation
tags:
- NTP
- 网络协议
- 计算机历史
- 操作系统
- 嵌入式开发
title: 在 NTP 诞生之前：Daytime 与 Time 协议的前世今生
---
### 文章背景与核心概要

在网络时间协议（NTP）将互联网时间同步标准化之前，早期网络依赖于更为简单、非正式的机制：**Daytime 协议（RFC 867）**和 **Time 协议（RFC 868）**。在乔恩·波斯特尔（Jon Postel）于 20世纪80年代初期的主导下，这些协议允许带宽受限的计算机通过基本的 TCP 或 UDP 请求向远程服务器查询时间。

尽管以现代标准来看它们相当原始——仅提供 1 秒的分辨率、容易受网络延迟影响，并且面临着未来“2036年危机（Y2K36）”——但这些轻量级协议为网络同步奠定了基础，并且至今仍通过美国国家标准与技术研究院（NIST）等服务运行。本文带你回顾这段互联网历史，并演示如何在 Linux 上搭建属于你自己的 Time 与 Daytime 服务器。

---

![RFC 867 Daytime Protocol](/blog/2026/rfc-867-868-time/rfc-867-daytime-protocol.png)

> In building an NTP time demo on old Macs for [VCF Midwest](https://vcfmw.org), I came across [RFC 867](https://www.rfc-editor.org/info/rfc867/) and [RFC 868](https://www.rfc-editor.org/info/rfc868/), for the 'Daytime' and 'Time' Protocols, respectively.
> 
> My first exposure to any form of network time was when I upgraded from a used PowerBook 180c to my first 'new' computer, a Power Mac G3, in 2000. With the introduction of Mac OS 8.5, Apple added a 'Network Time Server' option in the Date & Time Control Panel.
> 
> I remember dialing up the Internet via PPP, then clicking the 'Set Time Now' button, and seeing my computer's clock update. I didn't think much of it at the time, but this was way more than setting my wristwatch using the 'Time and Temperature' phone line, which was previously the most precise time source I could access regularly.

在为 [VCF Midwest](https://vcfmw.org) 的老款 Mac 制作 NTP 时间演示程序时，我偶然发现了 [RFC 867](https://www.rfc-editor.org/info/rfc867/) 和 [RFC 868](https://www.rfc-editor.org/info/rfc868/)，它们分别对应“Daytime（白昼）”和“Time（时间）”协议。

我第一次接触任何形式的网络时间，是在 2000 年从一台二手的 PowerBook 180c 升级到我的第一台“新”电脑 Power Mac G3 的时候。随着 Mac OS 8.5 的推出，苹果在“日期与时间”控制面板中增加了一个“网络时间服务器”选项。

我记得当时是通过 PPP 拨号上网，然后点击“立即设置时间”按钮，看着电脑的时钟更新。当时我并没有多想，但这比用“报时与气温”电话专线来对表要高级得多——那曾是我以前能定期接触到的最精确的时间源。

## Time 协议 (RFC 868)

> Prior to NTP ([RFC 1059](https://www.rfc-editor.org/info/rfc1059/) in 1988), requesting time from a remote server was remarkably straightforward. With the Time Protocol (RFC 868), a request consisted of just two steps:
> 
> 1. Open a connection to the server on port 37 (TCP connect, or send an empty UDP datagram).
> 2. Receive the time as a 32-bit binary number.
> 
> That's it! In the mid-80s, this was an extremely efficient method of time transfer. Network bytes were precious, and you didn't need a complex routine to handle the 32-bit time.

在 NTP（1988 年的 [RFC 1059](https://www.rfc-editor.org/info/rfc1059/)）出现之前，从远程服务器请求时间是非常直接的。通过 Time 协议 (RFC 868)，一个请求仅包含两个步骤：

1. 打开到服务器 37 端口的连接（建立 TCP 连接，或发送一个空的 UDP 数据报）。
2. 接收作为一个 32 位二进制数的当前时间。

就是这样！在 80 年代中期，这是一种极其高效的时间传输方法。当时的网络字节弥足珍贵，处理 32 位时间也无需编写复杂的常规代码。

### Time 协议的局限性

> Routing requests through the Internet with multiple non-deterministic hops exposed several drawbacks to this simplistic approach:
> 
> * **Low Resolution:** The 32-bit number represented "seconds since 00:00 (midnight) 1 January 1900 GMT," meaning the *best* timing resolution you could ever get was 1 second (whereas NTP provides 64-bit resolution scaling past microseconds).
> * **No Delay Compensation:** There is no timestamping of the actual request or response, so there is no way to account for network delays or average them out over time.
> * **The Y2K36 Bug:** The 32-bit integer value will run out on February 7, 2036, causing a 'Y2K36' bug similar to the [Unix Y2K38 Epochalypse](https://en.wikipedia.org/wiki/Year_2038_problem). (NTP shares this issue but introduced [Eras](https://www.ntp.org/reflib/y2k/) to manage it.)
> 
> When introduced in 1983, however, it was simply a convenient way for a network computer to fetch time from a server with a stable clock (since many early computers lacked real-time clocks). Critical services like distributed databases didn't rely on it yet, primarily because sub-second timing resolution wasn't yet commonplace.

通过充满多个非确定性跳数的互联网路由请求，暴露出这种简单方法的好几个缺点：

* **低分辨率：** 这个 32 位数字代表“自 1900 年 1 月 1 日 00:00（午夜）GMT 以来的秒数”，这意味着你所能获得的*最佳*时间分辨率只有 1 秒（而 NTP 提供了可精确到微秒以上的 64 位分辨率）。
* **无延迟补偿：** 实际的请求或响应没有时间戳记录，因此无法计算网络延迟或在一段时间内取平均值。
* **Y2K36 漏洞：** 32 位整数值将在 2036 年 2 月 7 日耗尽，从而引发类似于 [Unix 2038年危机（Y2K38 Epochalypse）](https://en.wikipedia.org/wiki/Year_2038_problem)的“Y2K36”漏洞。（NTP 也存在这个问题，但它引入了[纪元（Eras）](https://www.ntp.org/reflib/y2k/)机制来进行管理。）

然而，在 1983 年刚推出时，它只是网络计算机从具有稳定时钟的服务器获取时间的一种便捷方式（因为许多早期计算机缺乏实时时钟）。像分布式数据库这样关键的服务当时还不依赖它，主要是因为亚秒级的时间分辨率在当时尚未普及。

## Daytime 协议 (RFC 867)

> The Daytime protocol (RFC 867) is succinct yet ambiguous. It defines a protocol where an entire day and timestamp are returned in human-readable output:
> 
> ```fallback
> Tuesday, February 22, 1982 17:37:43-PST
> ```
> 
> The ambiguity stems from the format, which was left entirely to the implementor:
> 
> ```fallback
> There is no specific syntax for the daytime.  It is recommended that
> it be limited to the ASCII printing characters, space, carriage
> return, and line feed.  The daytime should be just one line.
> 
>     One popular syntax is:
> 
>        Weekday, Month Day, Year Time-Zone
> 
>        Example:
> 
>           Tuesday, February 22, 1982 17:37:43-PST
> ```
> 
> It immediately follows this by suggesting the alternative `dd mmm yy hh:mm:ss zzz`, which was famously used for SMTP!

Daytime 协议 (RFC 867) 既简洁又模棱两可。它定义了一种协议，返回人类可读格式的完整日期和时间戳：

```fallback
Tuesday, February 22, 1982 17:37:43-PST
```

这种歧义源于它的格式完全由实现者自行决定：

```fallback
There is no specific syntax for the daytime.  It is recommended that
it be limited to the ASCII printing characters, space, carriage
return, and line feed.  The daytime should be just one line.

    One popular syntax is:

        Weekday, Month Day, Year Time-Zone

        Example:

           Tuesday, February 22, 1982 17:37:43-PST
```

紧接着，它还建议了另一种替代格式 `dd mmm yy hh:mm:ss zzz`，而这正是 SMTP 臭名昭著的格式！

### NIST 的现代实现

> Fun fact: [NIST still runs RFC 867/868 Daytime services](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/internet-time-service-its#daytime-protocol-rfc-867) on `time.nist.gov`!
> 
> ```fallback
> $ nc time.nist.gov 13
> 
> 61281 26-08-29 23:31:43 50 0 0 771.1 UTC(NIST) *
> ```
> 
> This utilizes a customized response matching neither of the original RFC formats:
> 
> ```fallback
> JJJJJ YR-MO-DA HH:MM:SS TT L H msADV UTC(NIST) OTM
> ```
> 
> Where `JJJJJ` is the [Modified Julian Date](https://en.wikipedia.org/wiki/Julian_day), and OTM is an 'on-time marker' indicating when the time should be correct upon receipt. Historically, this derived from older [telephone time systems](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts)^[Apparently NIST's [ACTS dial-up time service](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts#software) is still used 200-300 times per day!] which were in some ways more deterministic. It remains one of the stranger [time formats](http://www.leapsecond.com/java/gpsclock.htm) around.
> 
> Both the Time and Daytime Protocols were shepherded by [Jon Postel](https://en.wikipedia.org/wiki/Jon_Postel)—often called the "God of the Internet"—who also gave us SMTP, IANA, and [Postel's law](https://en.wikipedia.org/wiki/Robustness_principle). 

趣事：[NIST 至今仍在 `time.nist.gov` 上运行 RFC 867/868 Daytime 服务](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/internet-time-service-its#daytime-protocol-rfc-867)！

```fallback
$ nc time.nist.gov 13

61281 26-08-29 23:31:43 50 0 0 771.1 UTC(NIST) *
```

这里使用了既不匹配任何原始 RFC 格式的自定义响应：

```fallback
JJJJJ YR-MO-DA HH:MM:SS TT L H msADV UTC(NIST) OTM
```

其中 `JJJJJ` 是[简化儒略日（Modified Julian Date）](https://en.wikipedia.org/wiki/Julian_day)，而 OTM 是一个“准时标记（on-time marker）”，指示接收时时间应当准确的时刻。历史上，这源自更早的[电话授时系统](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts)^[显然，NIST 的 [ACTS 拨号授时服务](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts#software)现在每天仍然被使用 200-300 次！]，这些系统在某些方面更具确定性。它至今仍然是周围最奇特的时间格式之一。

Time 和 Daytime 协议均由[乔恩·波斯特尔（Jon Postel）](https://en.wikipedia.org/wiki/Jon_Postel)（通常被称为“互联网之神”）主导，他还为我们带来了 SMTP、IANA 以及[波斯特尔定律（Postel's law）](https://en.wikipedia.org/wiki/Robustness_principle)。

---

## 运行你自己的 Time 与 Daytime 服务器

> After learning about Time and Daytime, I decided to add some easter eggs to my booth at VCF Midwest by hosting Time/Daytime services on ports 37 and 13.
> 
> Running your *own* server on Linux is straightforward using [`xinetd`](https://linux.die.net/man/8/xinetd). The following instructions are tailored for Pi OS / Debian, but apply similarly to other distributions:
> 
> ```bash
> # Install and enable xinetd
> sudo apt install xinetd
> sudo systemctl enable xinetd
> 
> # Edit time and daytime configurations
> sudo nano /etc/xinetd.d/time
>   -> service time tcp set disable to "no"
>   -> service time udp set disable to "no"
> 
> sudo nano /etc/xinetd.d/daytime
>   -> service daytime tcp set disable to "no"
>   -> service daytime udp set disable to "no"
> 
> # Restart xinetd
> sudo systemctl restart xinetd
> ```
> 
> Ensure ports 37 and 13 are open on your firewall, then test from another machine on the network:
> 
> ```mysql
> # Time
> $ nc 10.0.37.60 37 | xxd -g 1
> 00000000: ee 3f 24 b3                                      .?$.
> 
> # Verify the Time value by passing it into `date`:
> $ date -r $(( 0xee3f24c8 - 2208988800 ))
> Sun Aug 30 16:53:12 CDT 2026
> 
> # Daytime
> $ nc -v 10.0.37.60 13
> Connection to 10.0.37.60 port 13 [tcp/daytime] succeeded!
> 30 AUG 2026 16:49:26 CDT
> ```
> 
> *(Note: The `2208988800` offset in the `date` command accounts for the difference in seconds between the 1900 Time/NTP epoch and the 1970 [UNIX time](https://en.wikipedia.org/wiki/Unix_time) epoch).*
> 
> If you happen to be at VCF Midwest—especially if you've brought a vintage computer equipped with network capabilities—I'd be more than happy to hand you a proper Time or Daytime stamp!

在了解了 Time 和 Daytime 协议后，我决定在 VCF Midwest 的展位上通过在 37 和 13 端口托管 Time/Daytime 服务来添加一些彩蛋。

使用 [`xinetd`](https://linux.die.net/man/8/xinetd) 在 Linux 上运行你*自己的*服务器非常简单。以下说明专为 Pi OS / Debian 量身定制，但也同样适用于其他发行版：

```bash
# 安装并启用 xinetd
sudo apt install xinetd
sudo systemctl enable xinetd

# 编辑 time 和 daytime 配置
sudo nano /etc/xinetd.d/time
  -> service time tcp set disable to "no"
  -> service time udp set disable to "no"

sudo nano /etc/xinetd.d/daytime
  -> service daytime tcp set disable to "no"
  -> service daytime udp set disable to "no"

# 重启 xinetd
sudo systemctl restart xinetd
```

确保防火墙上的 37 和 13 端口已打开，然后从网络上的另一台机器进行测试：

```mysql
# Time 协议测试
$ nc 10.0.37.60 37 | xxd -g 1
00000000: ee 3f 24 b3                                      .?$.

# 通过将时间值传入 `date` 来验证时间：
$ date -r $(( 0xee3f24c8 - 2208988800 ))
Sun Aug 30 16:53:12 CDT 2026

# Daytime 协议测试
$ nc -v 10.0.37.60 13
Connection to 10.0.37.60 port 13 [tcp/daytime] succeeded!
30 AUG 2026 16:49:26 CDT
```

*（注意：`date` 命令中的 `2208988800` 偏移量计算的是 1900 年 Time/NTP 纪元与 1970 年 [UNIX 时间](https://en.wikipedia.org/wiki/Unix_time)纪元之间的秒数差。）*

如果你恰好在 VCF Midwest 现场——尤其是如果你带了一台配备网络功能的老式电脑——我很乐意为你提供一个标准的 Time 或 Daytime 时间戳！

---

## 延伸阅读

> * [NIST was 5 μs off UTC after last week's power cut](/blog/2025/nist-was-5-%CE%BCs-utc-after-last-weeks-power-cut/)
> * [Raspberry Pi Pico Mini Rack GPS Clock](/blog/2026/pico-gps-clock-mini-rack/)
> * [Using GPS for the most accurate time possible on a Mac](/blog/2025/using-gps-most-accurate-time-possible-on-mac/)

* [NIST 在上周断电后，其 UTC 时间偏差了 5 微秒](/blog/2025/nist-was-5-%CE%BCs-utc-after-last-weeks-power-cut/)
* [树莓派 Pico 迷你机架 GPS 时钟](/blog/2026/pico-gps-clock-mini-rack/)
* [在 Mac 上利用 GPS 实现极致精准的时间同步](/blog/2025/using-gps-most-accurate-time-possible-on-mac/)