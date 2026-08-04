# 服务器上的 BMC 与一个令人意外的 USB 网络设备 (BMCs and a Surprising USB Network Device on Your Server)
### 文章背景与核心概要
本文探讨了现代 Linux 服务器上经常出现的神秘“幻影”USB 网络设备现象，揭示了其背后由基板管理控制器 (BMC) 和现代 Redfish 管理协议驱动的技术原理。文章分析了从传统 IPMI 到基于 HTTP/REST 的 Redfish 的演进过程，解释了硬件厂商为何选择虚拟 USB 以太网来连接主机与 BMC。同时，这也展示了通过专用内部通道隔离管理服务在安全性方面的合理考量。

---

[当你在现代服务器上安装 Linux 时，可能会注意到一个神秘的 USB 以太网设备（例如 enp1s0f4u1u2c2）通过 DHCP 自动租用了一个 IP 地址——即使物理 USB 端口上什么也没插。这种现象表明存在一个基板管理控制器（BMC），它利用 Redfish 进行现代、受云启发的服务器管理。本文探讨了现代硬件如何利用虚拟 USB 网络连接宿主服务器与其 BMC，从而取代了较旧且笨重的 IPMI 方法。]

> When installing Linux on a modern server, you might notice a mysterious USB Ethernet device (e.g., `enp1s0f4u1u2c2`) automatically leasing an IP address via DHCP—even without anything plugged into the physical USB ports. This phenomenon indicates the presence of a **Baseboard Management Controller (BMC)** leveraging **Redfish** for modern, cloud-inspired server management. This article explores how modern hardware uses virtual USB networking to bridge the host server and its BMC, replacing older, cumbersome IPMI methods.

---

[假设你正在一台拥有两个物理网络端口的服务器上安装操作系统，突然出现了一个名称晦涩（如 enp1s0f4u1u2c2）的第三个网络设备。尽管物理 USB 端口上没有任何插入物，但你的安装程序成功租用了一个 IP 地址（例如 169.254.3.1）。]

> Suppose you are installing an OS on a server with two physical network ports, and a third network device suddenly appears with a cryptic name like `enp1s0f4u1u2c2`. Despite nothing being physically plugged into the USB ports, your installer successfully leases an IP address (such as `169.254.3.1`). 

[恭喜你——你的服务器配备了基板管理控制器（BMC），并且它很可能支持 Redfish，这是 IPMI 现代的、受云技术影响的继任者。]

> Congratulations—your server features a [Baseboard Management Controller (BMC)](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Baseboard_management_controller), and it likely speaks [Redfish](https://en.wikipedia.org/wiki/Redfish_(specification)), the modern, cloud-influenced successor to [IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface).

[管理服务器的管理员通常需要宿主操作系统与 BMC 直接通信——例如，查询仅 BMC 可用的传感器信息或调整其配置。]

> Administrators managing a server often need the host operating system to communicate directly with the BMC—for instance, to [query sensor information only available to the BMC](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/IPMISensorsWhyQuery) or to adjust its configuration. 

[从历史上看，管理 IPMI 需要专门的内核驱动程序、从 SMBIOS 中提取数据以及繁琐的变通方法。这种体验与云虚拟机形成了鲜明对比，在云虚拟机中，宿主代理只需通过对指定 IP 地址的 HTTP 请求进行通信。]

> Historically, managing IPMI required [specialized kernel drivers](https://www.kernel.org/doc/html/latest/driver-api/ipmi.html), extracting data from [SMBIOS](https://en.wikipedia.org/wiki/System_Management_BIOS), and cumbersome workarounds. This experience contrasted sharply with cloud virtual machines, where host agents communicate simply via HTTP requests to a designated IP address. 

[虽然 IPMI 技术上是一种网络协议，但从宿主服务器通过 IPMI 与 BMC 交互与标准网络大不相同。IPMI 依赖于适合其时代基于 UDP 的自定义协议。相比之下，Redfish 采用了基于 HTTP REST 的方法。在 Redfish 开发之时，HTTP 已成为管理任务的通用协议，这反映了云环境中已经普遍存在的做法。]

> While IPMI is technically a network protocol, interacting with a BMC over IPMI from a host server differs vastly from standard networking. IPMI relies on a custom, UDP-based protocol suited for its era. In contrast, **Redfish** adopts an HTTP REST-based approach. By the time Redfish was developed, HTTP had emerged as the universal protocol for management tasks, mirroring practices already common in cloud environments. 

[因此，宿主与启用 Redfish 的 BMC 通信最自然的方式是通过直接网络连接，从而消除了传统的带外机制。]

> Consequently, the most natural way for a host to communicate with a Redfish-enabled BMC is via a direct network connection, eliminating legacy out-of-band mechanisms.

[启用直接网络连接需要一个专用于 BMC 的专用网络接口。虽然工程师理论上可以设计半虚拟化的 PCIe 以太网链路，但这种方法会引入不必要的复杂性。]

> Enabling a direct network connection requires a dedicated network interface tied exclusively to the BMC. While engineers could theoretically design semi-virtual PCIe Ethernet links, that approach introduces unnecessary complexity.

[相反，现代 BMC 严重依赖“KVM over IP”功能。为了提供虚拟键盘、鼠标和安装介质存储，BMC 本身就会向宿主呈现虚拟 USB 设备。利用这种现有架构，为 Redfish 提供网络接口最直接的方法是通过虚拟 USB 以太网设备。]

> Instead, modern BMCs heavily rely on **"KVM over IP"** functionality. To provide virtual keyboard, mouse, and install-media storage, the BMC inherently presents virtual USB devices to the host. Leveraging this existing architecture, the most straightforward method to supply a network interface for Redfish is through a **virtual USB Ethernet device**.

[注意：这些虚拟 USB 设备通常捆绑在一个虚拟 USB 集线器上——通常伴随着虚拟 PCIe USB 控制器、显卡和桥接器。将 BMC 连接到宿主系统需要相当大数量的虚拟化奇招，同时还要处理诸如 ATX 服务器电源控制等任务的机制。]

> *Note:* These virtual USB devices are typically bundled onto a virtual USB hub—often accompanied by a virtual PCIe USB controller, graphics card, and bridge. A surprising amount of virtualization wizardry goes into connecting a BMC to the host system, alongside mechanisms handling tasks like [ATX server power control](https://utcc.utoronto.ca/~cks/space/blog/tech/ATXServerPowerControlHow).

[为了允许宿主通过此虚拟链路与 BMC 通信，BMC 托管了以下两者：]

> To allow the host to communicate with the BMC across this virtual link, the BMC hosts both:

[1. 一个小型 DHCP 服务器，为宿主分配 IP 地址。]

> 1. **A miniature DHCP server**, assigning the host an IP address.

[2. 一个内部 HTTP 服务器，用于处理管理请求。]

> 2. **An internal HTTP server**, serving management requests.

[根据硬件的不同，这个内部 HTTP 服务器可能独立于 BMC 的主管理网络接口运行。例如，在某些服务器上，内部 HTTP 服务器严格响应 Redfish 请求，并限制对专用管理端口上可用的标准网页管理 GUI 的访问（尽管该端口也支持 Redfish 请求）。]

> Depending on the hardware, this internal HTTP server may operate separately from the BMC's primary management network interface. On certain servers, for example, the internal HTTP server strictly answers Redfish requests and restricts access to the standard web-management GUI available on the dedicated management port (though that port supports Redfish requests as well). 

[归根结底，通过专用的内部通道隔离这些服务是 BMC 做出的一项非常明智的安全决策。]

> Ultimately, isolating these services via a dedicated internal channel represents a highly sensible security decision on the BMC's part.