---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-09-09
hide:
- navigation
tags:
- OpenNMC
- UPS
- APC
- 开源硬件
- homelab
title: OpenNMC：昂贵 APC 管理卡的开源替代方案
---
### 文章背景与核心概要
不间断电源（UPS）是家庭实验室（Homelab）中保障服务器安全关机和稳定供电的核心设备。然而，许多老旧的 APC 型号依赖于昂贵、停产且封闭的专有网络管理卡（NMC，如 NMC 2），而官方的替代品 NMC 3 售价高达近 500 美元。

为解决这一痛点，来自奥地利的 NetCube Systems 推出了 **OpenNMC**。这是一款支持热插拔的开源固件替代方案，内置了 Wi-Fi、蓝牙、Web 用户界面以及原生的网络 UPS 工具（NUT）服务器。本文介绍了作者对该开源网卡在实际 APC 智能 UPS 中的安装测试体验，展示了其 Web UI 界面、强大的控制功能以及彻底打破厂商专有生态限制的重大意义。

---

# OpenNMC is an open replacement for expensive APC management cards

*Published: Sep 8, 2026*

## Summary
Uninterruptible Power Supplies (UPSes) are essential for homelabs to safely shut down servers and condition power, but older APC models rely on expensive, discontinued, and locked-down proprietary Network Management Cards (NMCs) like the NMC 2—with replacements like the NMC 3 costing nearly $500. To solve this, the **OpenNMC** from NetCube Systems Austria offers a hot-pluggable, open-source firmware replacement featuring built-in Wi-Fi, Bluetooth, a Web UI, and a native Network UPS Tools (NUT) server.

> 不间断电源（UPS）通常是家庭实验室中最枯燥但却至关重要的部分。它们的主要任务之一是在断电时为服务器争取时间安全关机；另一个任务则是调理电源，确保服务器平稳运行。

> Uninterruptible Power Supplies (UPSes) are typically the most boring part of your homelab, but they're important. One of their main jobs is to give servers time to shut down safely if the power goes out. Another job is to condition your power so your servers can run smoothly.

---

![APC SmartUPS 2200XL](./blog/2026/opennmc-apc-ups-replacement-card/apc-smart-ups-2200xl-in-rack.jpg)

> 要把这两件事都做好，你需要一个智能接口。至少对于 APC 来说，有大量老旧的 UPS 都在使用网络管理卡。下图展示的是我从旧款 APC Smart-UPS 2200 XL 中拆下来的 NMC 2。

> To do both of those things *well*, you need a smart interface. And at least with APC, there are tons of older UPSes that use Network Management Cards. The one pictured below is the NMC 2, which I pulled out of my old APC Smart-UPS 2200 XL.

![APC Network Management Card 2 for SmartSlot UPS](./blog/2026/opennmc-apc-ups-replacement-card/apc-network-management-card-2-schneider-electric-smart-slot.jpg)

> 它已于 [2022年停产](https://www.se.com/us/en/product/AP9630/apc-ups-network-management-card-2/)。如果我想获得技术支持，APC 希望向我推销他们升级版的 [NMC *3*](https://www.se.com/us/en/product/AP9640/network-management-card-3-nmc3-secure-remote-ups-monitoring-and-management/)，售价将近 500 美元！

> It was [discontinued in 2022](https://www.se.com/us/en/product/AP9630/apc-ups-network-management-card-2/), and if I want support, APC wants to sell me their upgraded [NMC *3*](https://www.se.com/us/en/product/AP9640/network-management-card-3-nmc3-secure-remote-ups-monitoring-and-management/), which costs almost $500!

> 最令人恼火的是，无论是硬件还是软件，这一切全都是专有的。虽然它确实有一种可以与几乎任何系统进行集成的协议，但这些卡上的固件是完全锁死的。而且自从我开始使用 [NUT](https://networkupstools.org)（即 Network UPS Tools）以来，无论如何我都得用另一台电脑来监控 UPS。

> The most annoying part of this is it's all proprietary: the hardware *and* the software. It does have a protocol you can integrate with almost anything, but the firmware on these cards is locked down. And since I've started using [NUT](https://networkupstools.org), or Network UPS Tools, I'd have to use another computer to monitor the UPS anyway.

> 但现在不用了。我正在测试来自[奥地利 NetCube Systems](https://netcubesystems.at) 的 OpenNMC。它的固件完全开源，这意味着你对上面运行的软件拥有完全的自主权。它内置了 NUT 服务器，和 APC 的网卡一样支持热插拔，甚至在需要时还自带 Wi-Fi 功能！

> But not anymore. I'm testing the OpenNMC from [NetCube Systems Austria](https://netcubesystems.at). Its firmware is completely open source, meaning you have full ownership of the software that runs on it. It has a built-in NUT server, it's hot-pluggable just like APC's cards, and it even has Wi-Fi if you need that!

![OpenNMC Hero image](./blog/2026/opennmc-apc-ups-replacement-card/opennmc-hero.jpg)

> [OpenNMC 固件仓库](https://gitlab.com/netcube-systems-austria/opennmc)已经在 GitLab 上线，其硬件原理图也将根据开源硬件许可证发布。正如他们在 GitLab 中声明的那样：

> The [OpenNMC firmware repo](https://gitlab.com/netcube-systems-austria/opennmc) is already up on GitLab, and the hardware schematics will be released under an open-source hardware license. As stated in their GitLab:

> > 原理图、布局和前面板文件计划在清理和测试完成后发布，目标是以开源硬件的形式推出。

> > The schematic, layout, and front panel files are planned to be published once they are cleaned up and tested, with the goal of releasing them as open-source hardware.

> 我制作了一个关于这款网卡的简短视频，并发布在 Level 2 Jeff 频道上（标为“赞助”内容，因为原型机是由奥地利 NetCube Systems 寄给我的，不过在此之前我在 [Reddit 上发现这个项目](https://www.reddit.com/r/homelab/comments/1sd3swi/i_built_an_opensource_replacement_for_apc/)时就已经注册了 Crowd Supply 众筹活动）。

> I made a quick video about the card and published it on Level 2 Jeff (marked as 'sponsored' since the prototype was sent to me by NetCube Systems Austria, though I had already signed up for the Crowd Supply campaign when I [spotted the project on Reddit](https://www.reddit.com/r/homelab/comments/1sd3swi/i_built_an_opensource_replacement_for_apc/)).

## OpenNMC Installation

> ## OpenNMC 安装

> 切换到 OpenNMC 的过程非常简单。在 UPS 保持运行的状态下，我拔出了 APC NMC 2，然后插上了 OpenNMC。两者都支持热插拔。

> Swapping over to the OpenNMC was easy. With the UPS running, I pulled out the APC NMC 2, and plugged in the OpenNMC. Both are hot-pluggable.

> 我将它接入了以太网，但如果由于某种原因你无法将网线拉到 UPS 背面，它也内置了 Wi-Fi 和蓝牙功能。

> I plugged mine into Ethernet, but it also has Wi-Fi and Bluetooth built-in, if you can't get a network cable to the back of your UPS for some reason.

![OpenNMC installed in my APC UPS](./blog/2026/opennmc-apc-ups-replacement-card/opennmc-card-installed-apc-ups.jpg)

> 如果说我对硬件有什么小抱怨的话，那就是这些指示灯稍微有点亮。如果你对此介意，你可能手头已经准备好了一套 [LightDims](https://amzn.to/3SQuDfU) 遮光贴……

> If I had one complaint about the hardware, I think the LEDs are a little bright. If that bothers you, you probably already have a set of [LightDims](https://amzn.to/3SQuDfU) on hand...

> 首次设置时，你必须通过背面的 USB-C 串口连接，并配置一个管理员密码。之后，你就可以通过 Web UI 管理所有内容了。

> For first-time setup, you have to plug into the USB-C serial port on the back, and configure an admin password. After that, you can manage everything through the Web UI.

> 它终究是一个 UPS，所以没有那么复杂，但你可以在“概览”（Overview）页面上访问所有重要的统计数据：

> It's a UPS, so it's not *that* complicated, but you can access all the important stats on the Overview page:

![OpenNMC Web UI overview page](./blog/2026/opennmc-apc-ups-replacement-card/opennmc-overview.jpg)

> 它有一排按钮，可以用来触发不同的测试模式、在更换电池后运行校准，或者管理 UPS 上的负载：

> It has a row of buttons to trigger different test modes, run calibration after replacing batteries, or manage the load on the UPS:

![OpenNMC UPS Controls](./blog/2026/opennmc-apc-ups-replacement-card/opennmc-ups-controls.jpg)

> 你还可以通过内置的 NUT 服务器进行完全的管理控制。我在预发布固件上测试过这一点，当时有一个 Bug 阻止了某些客户端软件的正常运行，但当 [Crowd Supply 众筹活动](https://www.crowdsupply.com/netcube-systems-austria/opennmc)正式上线时，这个问题应该已经修复了。

> And you can allow full management via the built-in NUT server, as well. I tested that with my pre-production firmware and there was one bug preventing some client software from working, but that should be fixed by the time [the Crowd Supply campaign](https://www.crowdsupply.com/netcube-systems-austria/opennmc) is live.

> 我目前还不知道最终的预期价格（等众筹活动上线后我会更新这篇文章），但即使它的价格和 APC 自己的网卡完全一样，这也是物有所值的，因为你同时获得了内置的 NUT 支持和开源固件。

> I don't know the final expected price (I'll update this post when the campaign is live), but even if it cost exactly the same as APC's own card, that'd be worth it, because you get built-in NUT *and* open-source firmware.

---

## Further Reading
* [Popular Rockchip SBC distro in limbo after maintainer burns out](/blog/2024/popular-rockchip-sbc-distro-limbo-after-maintainer-burns-out/)
* [Framework's 10G Ethernet module exposes USB-C's complexity](/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)
* [Bambu Lab is abusing the open source social contract](/blog/2026/bambu-lab-abusing-open-source-social-contract/)