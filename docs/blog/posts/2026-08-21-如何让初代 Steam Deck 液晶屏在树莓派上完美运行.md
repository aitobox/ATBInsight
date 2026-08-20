---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-21
hide:
- navigation
tags:
- 树莓派
- Steam Deck
- Linux内核
- 硬件开源
- 嵌入式开发
title: 如何让初代 Steam Deck 液晶屏在树莓派上完美运行
---
### 文章背景与核心概要
初代 Steam Deck 所采用的那块性价比极高、素质出色的 7 英寸 LCD 屏幕，现在终于可以通过全新的开源 Linux 内核驱动以及由 Scandent 公司定制的树莓派扩展板（HAT）连接到树莓派上了。这一创新方案为创客们提供了一个远超官方树莓派触控显示屏的高性价比替代选择——不仅成本大幅降低，还拥有更高的分辨率、更好的亮度和高达 216 PPI 的细腻显示效果。

该项目的核心突破在于 Scandent 团队为其开发并开源了 Linux 内核驱动程序，以及将树莓派 MIPI 接口适配到 Steam Deck 专用 39 引脚接口的开源 Pi HAT 设计。虽然该公司无意将其商业化，但这一举措极大地延长了特定消费级显示面板的生命周期，为主流硬件开发者和开源爱好者摆脱“面板停产魔咒”提供了一条极具价值的康庄大道。

---

# Getting the Steam Deck LCD working on a Raspberry Pi

*Published: Aug 20, 2026*

## Summary
The affordable, high-quality 7-inch LCD panel from the original Steam Deck can now be used with a Raspberry Pi, thanks to a new open-source Linux kernel driver and custom Pi HAT designed by Scandent. This setup offers a superior alternative to the official Raspberry Pi Touch Display at a fraction of the cost, boasting higher resolution, better brightness, and a sharp 216 PPI.

---

## Introduction

初代 Steam Deck 上所使用的 [BOE TV070WXM-TV0 LCD 液晶屏](https://www.aliexpress.us/item/3256806531632512.html?gatewayAdapt=glo2usa4itemAdapt)现在售价仅为 30 美元左右。它是一块非常实用的 7 英寸触控屏，拥有 400 尼特的亮度以及 1280x800 的分辨率（像素密度高达 216 ppi，显示效果极其细腻）。

> The [BOE TV070WXM-TV0 LCD](https://www.aliexpress.us/item/3256806531632512.html?gatewayAdapt=glo2usa4itemAdapt) used in the original Steam Deck can be had for around $30. It's a serviceable 7" touchscreen with 400 nits of brightness and a resolution of 1280x800 (for a sharp 216 ppi).

<img alt="Steam Deck LCD working on a Raspberry Pi 5" height="auto" src="/blog/2026/steam-deck-lcd-pi-hat/steam-deck-lcd-pi-front-touch.jpeg" width="700"/>

这块屏幕的规格远胜于售价高出一倍、边框巨大且分辨率减半的[树莓派官方 7 英寸触控显示屏](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)！

> The specs are a lot nicer than the [Pi 7" Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/), which costs twice as much, with giant bezels and half the resolution!

## The Solution: A Custom Driver and Pi HAT

在此之前，Steam Deck 的 LCD 屏是无法直接在树莓派上运行的。不过，[Scandent](https://www.scandent.com) 的团队在其某款自研设备中急需一款标准化且具备大众化供应基础的触控屏。为了解决这个问题，他们专门为其编写了一个 [Linux 内核驱动程序](https://github.com/ScandentLLC/tv070wxm-hat/blob/master/linux-rpi-6.12.y-panel-boe-tv070wxm.patch)，并计划将其合并到主线内核中。

> Until recently, the Steam Deck LCD didn't work with a Raspberry Pi. However, the team at [Scandent](https://www.scandent.com) needed a standardized, mass-market touchscreen for one of their own devices. To solve this, they built a [Linux kernel driver](https://github.com/ScandentLLC/tv070wxm-hat/blob/master/linux-rpi-6.12.y-panel-boe-tv070wxm.patch) for it, which they intend to upstream.

除了软件层面的突破，他们还开源了一款 [Pi HAT 硬件设计](https://github.com/ScandentLLC/tv070wxm-hat/)，能够将树莓派 5 或 CM4 的 MIPI 接口[^1]适配到 Steam Deck LCD 所使用的特殊 39 引脚连接器上。

> Beyond the software, they have also open-sourced a [Pi HAT design](https://github.com/ScandentLLC/tv070wxm-hat/) that adapts the Raspberry Pi 5 or CM4's MIPI connection[^1] to the specialized 39-pin connector found on the Steam Deck LCD.

<img alt="Steam Deck LCD with a Raspberry Pi 5 mounted on its back" height="auto" src="/blog/2026/steam-deck-lcd-pi-hat/steam-deck-lcd-pi-rear.jpeg" width="700"/>

该代码仓库中包含了详细的构建说明以及 KiCAD 项目文件，方便用户自行打板制造该扩展板。Scandent 还非常慷慨地提供了用于测试的硬件原型：

> The repository includes detailed build instructions along with the KiCAD project files if you wish to fabricate your own HAT. Scandent kindly provided prototype hardware for testing:

<img alt="Steam Deck LCD working on a Raspberry Pi 5" height="auto" src="/blog/2026/steam-deck-lcd-pi-hat/steam-deck-lcd-assembly-pi-5-hat.jpg" width="700"/>

## Why This Matters for Makers

Scandent 并没有将这款 HAT 商业化的打算；他们的目标仅仅是为自家的生态系统在未来几年内锁定一款供货稳定、货源充足的触控屏。让硬件更轻易地被电子爱好者获取，同时也进一步巩固了这款特定液晶屏在市场上的生存空间。

> Scandent doesn't plan to commercialize the HAT; their goal was simply to secure a reliable, high-supply touchscreen for their ecosystem over the next few years. Making the hardware more accessible to hobbyists strengthens the market presence of this specific LCD.

许多特种液晶面板通常绑定于特定的消费电子产品。一旦这些产品停产，其使用的显示屏往往也会随之停产，迫使下游用户不得不频繁将项目迁移到新的面板上。简化硬件信号传输和内核驱动的维护，能够极大地缓解硬件开发者的这种“心病”。

> Specialized LCD panels are frequently tied to specific consumer devices. Once those devices stop production, the displays are often discontinued, forcing downstream users to constantly port their projects to new panels. Simplifying hardware signaling and kernel driver maintenance helps alleviate this headache for hardware developers.

## Real-World Performance

在树莓派 5 上对这块 Steam Deck LCD 进行实际测试后，结果表现非常出色：
* **显示效果：** 肉眼观察下几乎没有闪烁或水波纹，即使在演播室灯光下也能保持极高的亮度。
* **触控交互：** 在树莓派默认的分辨率缩放比例下，触控目标可能会显得略微偏小，但通过调整缩放比例或设计专用的 HMI/UI 界面，整个系统完全可以非常流畅地使用。

> Testing the Steam Deck LCD on a Raspberry Pi 5 revealed great results:
> * **Visuals:** Minimal flickering/waviness in person, with strong brightness even under studio lighting.
> * **Touch Interaction:** Touch targets can feel slightly small at the Pi's default resolution scaling, but adjusting the scaling or designing a custom HMI/UI makes the setup entirely usable. 

也许这会激发某位创客的灵感，从而设计出一套基于 3D 打印外壳和完整硬件堆栈的、基于 RetroPie 的开源掌上 Steam Deck！

> Perhaps this will inspire someone to design a 3D-printed enclosure and complete hardware stack for a RetroPie-based open-source Steam Deck!

---

## Footnotes

[^1]: CM5 理论上应当支持，但目前尚未经过实际测试。 

> [^1]: The CM5 should work, but has not yet been tested. 

---

## Further reading

* [Raspberry Pi Connect may control Windows soon](/blog/2026/raspberry-pi-connect-may-control-windows-soon/)
* [Build your own Dial-up ISP with a Raspberry Pi](/blog/2026/build-your-own-dial-up-isp-with-a-raspberry-pi/)
* [Raspberry Pi's new AI HAT adds 8GB of RAM for local LLMs](/blog/2026/raspberry-pi-ai-hat-2/)