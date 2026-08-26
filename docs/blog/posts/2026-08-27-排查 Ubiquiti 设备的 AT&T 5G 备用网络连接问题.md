---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-27
hide:
- navigation
tags:
- Ubiquiti
- UniFi
- 5G
- AT&T
- 网络排查
title: 排查 Ubiquiti 设备的 AT&T 5G 备用网络连接问题
---
### 文章背景与核心概要
为了搭建一套移动式“迷你家庭实验室（mini homelab）”，作者测试了 **UniFi 5G Backup** 作为冗余互联网解决方案。尽管该硬件设计紧凑、非常适合迷你机架，但在将其与 AT&T 商业 5G 套餐进行集成时遇到了重大阻碍。尽管该设备标榜已获得 AT&T 认证，但目前它无法连接到 5G 网络，而是默认降级为 4G LTE，导致网速受限。本文记录了调试过程以及当前 AT&T 网络对 5G RedCap 支持的局限性。

---

### 项目与硬件简介
对于我的移动机架项目，我需要一个能够故障转移到固定线路的主 5G 连接。我选择了 [UniFi 5G Backup](https://store.ui.com/us/en/products/u5g-us)，这是一款支持 PoE 供电的 5G RedCap 设备，最高速率可达 220 Mbps。

<img alt="UniFi 5G Backup getting 20 Mbps in my studio" height="auto" src="/blog/2026/unifi-u5g-backup-debugging/unifi-5g-backup-20mbps-in-studio.jpg" width="700"/>

> For my mobile rack project, I wanted a primary 5G connection that could fail over to a fixed-line connection. I selected the [UniFi 5G Backup](https://store.ui.com/us/en/products/u5g-us), a PoE-powered 5G RedCap device capable of 220 Mbps.

尽管 Ubiquiti 明确指出消费者套餐不支持 5G RedCap，但我认为我的 AT&T 企业级“AIA”套餐应该能够正常工作。然而，我遇到了三个主要问题：
1. **固件死循环：** 设备在被纳管（adoption）时陷入了更新循环，需要通过手动的 TFTP 恢复过程来解决。
2. **连接性问题：** 设备拒绝连接 5G，并回落到了 4G LTE。
3. **IMEI 不兼容：** 我的 AT&T 客户代表确认，该设备的 IMEI 目前尚不符合其“Internet Air for Business”5G 服务的接入资格。

> While Ubiquiti notes that consumer plans don't support 5G RedCap, I assumed my AT&T Enterprise "AIA" plan would work. However, I faced three major issues:
> 1. **Firmware Loops:** The device got stuck in an update loop upon adoption, requiring a manual TFTP recovery process.
> 2. **Connectivity:** The device refused to connect to 5G, falling back to 4G LTE.
> 3. **IMEI Incompatibility:** My AT&T representative confirmed that the device's IMEI is not currently eligible for their "Internet Air for Business" 5G service.

<img alt="UniFi 5G Backup showing 4G LTE AT&amp;T Connection" height="auto" src="/blog/2026/unifi-u5g-backup-debugging/unifi-5g-backup-4g-lte-att.jpg" width="700"/>

---

### 调试蜂窝网络连接
为了调查设备为什么无法与 5G 建立握手，我利用 UniFi 网络 UI 的“Debug（调试）”控制台访问了设备的 root shell。

> To investigate why the device was failing to handshake with 5G, I utilized the UniFi Network UI's "Debug" console to access the device's root shell.

使用 `mca-dump` 命令，我检查了调制解调器（modem）的状态：

> Using the `mca-dump` command, I inspected the modem's state:

```gdscript3
# mca-dump
{
        "architecture": "armv7l",
        "gateway_ip": "192.168.1.1",
        "hostname": "U5GBackup",
...
        "mbb": {
                "geo_info": {
                        ...
                        "isp": "AT&T Wireless",
                        "organization": "AT&T Enterprises, LLC"
                },
                "imei": "[redacted]",
                "radio": {
                        "5g_sa_mode": false,
                        "band": "eutran-30",
                        "ca_lte": [
                                {
                                        "band": 30,
                                        "dl_bw_mhz": 10.0,
                                        "dl_earfcn": 9820,
                                        "primary": true,
                                        "ul_bw_mhz": 10.0
                                }
                        ],
                        ...
                        "networkoperator": "AT&T",
                        ...
                        "rat": "LTE",
                        "rat_5g_uw": false,
                        "rat_caps": [
                                "5gnr-sa",
                                "lte"
                        ],
                        "rat_mode_active": "LTE",
                        ...
                        "rsrp": -95,
                        "rsrq": -12,
                        "rssi": -68,
                        "signal": 3,
                        "signal_percent": 100,
                        "snr": 13.800000190734863
        "model": "U5G-US",
        "model_display": "U5G-US",
        ...
        "uptime_str": "28m23s",
        "version": "1.4.3.360"
}
```

输出结果证实 `rat_mode_active` 设置为 `LTE`，而 `5g_sa_mode` 为 `false`。这表明本地基站要么缺乏 5G SA（独立组网）支持，要么该 SIM 卡在此特定硬件上未被授权使用 5G。

> The output confirms `rat_mode_active` is set to `LTE` and `5g_sa_mode` is `false`. This indicates that either the local tower lacks 5G SA (Standalone) support, or the SIM is not authorized for 5G on this specific hardware.

---

### 结论
将同一张 SIM 卡放入 **UniFi 5G Max** 中测试，其下载速度接近 600 Mbps，这证明了 SIM 卡和地理位置完全支持高速 5G。

> Testing the same SIM in a **UniFi 5G Max** yielded speeds of nearly 600 Mbps, confirming the SIM and location are capable of high-speed 5G.

<img alt="UniFi 5G Max getting nearly 600 Mbps downlink" height="auto" src="/blog/2026/unifi-u5g-backup-debugging/unifi-5g-max-581-mbps-down.jpg" width="700"/>

看起来就目前而言，U5G Backup 在 5G RedCap 方面主要针对 T-Mobile 的网络进行了优化。我目前正在等待我在[社区论坛帖子](https://community.ui.com/questions/U5G-Backup-IMEI-not-eligible-for-ATandT-Internet-Air-for-Business/0524bb57-d209-4c34-9949-9002c35e623b)上的进一步进展，看看 Ubiquiti 能否解决 AT&T 的认证问题。在此之前，我只能使用 4G LTE 的速度。

> It appears that for now, the U5G Backup is primarily optimized for T-Mobile's network regarding 5G RedCap. I am currently awaiting further traction on my [community forum post](https://community.ui.com/questions/U5G-Backup-IMEI-not-eligible-for-ATandT-Internet-Air-for-Business/0524bb57-d209-4c34-9949-9002c35e623b) to see if Ubiquiti can resolve the AT&T certification issues. Until then, I am limited to 4G LTE speeds.

***

*关于 TFTP 恢复的注意事项：如果遇到更新循环问题，请确保通过有线以太网连接。TFTP 恢复期间使用 WiFi 连接极易导致数据损坏。*

> *Note on TFTP Recovery: If you encounter update loops, ensure you are connected via a wired Ethernet connection. WiFi connections during TFTP recovery are prone to data corruption.*