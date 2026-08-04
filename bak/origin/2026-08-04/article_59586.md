# BMCs and a Surprising USB Network Device on Your Server

## Executive Summary
When installing Linux on a modern server, you might notice a mysterious USB Ethernet device (e.g., `enp1s0f4u1u2c2`) automatically leasing an IP address via DHCP—even without anything plugged into the physical USB ports. This phenomenon indicates the presence of a **Baseboard Management Controller (BMC)** leveraging **Redfish** for modern, cloud-inspired server management. This article explores how modern hardware uses virtual USB networking to bridge the host server and its BMC, replacing older, cumbersome IPMI methods.

---

## The Discovery: A Phantom USB Device
Suppose you are installing an OS on a server with two physical network ports, and a third network device suddenly appears with a cryptic name like `enp1s0f4u1u2c2`. Despite nothing being physically plugged into the USB ports, your installer successfully leases an IP address (such as `169.254.3.1`). 

Congratulations—your server features a [Baseboard Management Controller (BMC)](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Baseboard_management_controller), and it likely speaks [Redfish](https://en.wikipedia.org/wiki/Redfish_(specification)), the modern, cloud-influenced successor to [IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface).

## From IPMI to Redfish: A Shift in Server Management
Administrators managing a server often need the host operating system to communicate directly with the BMC—for instance, to [query sensor information only available to the BMC](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/IPMISensorsWhyQuery) or to adjust its configuration. 

Historically, managing IPMI required [specialized kernel drivers](https://www.kernel.org/doc/html/latest/driver-api/ipmi.html), extracting data from [SMBIOS](https://en.wikipedia.org/wiki/System_Management_BIOS), and cumbersome workarounds. This experience contrasted sharply with cloud virtual machines, where host agents communicate simply via HTTP requests to a designated IP address. 

While IPMI is technically a network protocol, interacting with a BMC over IPMI from a host server differs vastly from standard networking. IPMI relies on a custom, UDP-based protocol suited for its era. In contrast, **Redfish** adopts an HTTP REST-based approach. By the time Redfish was developed, HTTP had emerged as the universal protocol for management tasks, mirroring practices already common in cloud environments. 

Consequently, the most natural way for a host to communicate with a Redfish-enabled BMC is via a direct network connection, eliminating legacy out-of-band mechanisms.

## Why a USB Ethernet Device?
Enabling a direct network connection requires a dedicated network interface tied exclusively to the BMC. While engineers could theoretically design semi-virtual PCIe Ethernet links, that approach introduces unnecessary complexity.

Instead, modern BMCs heavily rely on **"KVM over IP"** functionality. To provide virtual keyboard, mouse, and install-media storage, the BMC inherently presents virtual USB devices to the host. Leveraging this existing architecture, the most straightforward method to supply a network interface for Redfish is through a **virtual USB Ethernet device**.

> *Note:* These virtual USB devices are typically bundled onto a virtual USB hub—often accompanied by a virtual PCIe USB controller, graphics card, and bridge. A surprising amount of virtualization wizardry goes into connecting a BMC to the host system, alongside mechanisms handling tasks like [ATX server power control](https://utcc.utoronto.ca/~cks/space/blog/tech/ATXServerPowerControlHow).

## DHCP, HTTP, and Security Architecture
To allow the host to communicate with the BMC across this virtual link, the BMC hosts both:
1. **A miniature DHCP server**, assigning the host an IP address.
2. **An internal HTTP server**, serving management requests.

Depending on the hardware, this internal HTTP server may operate separately from the BMC's primary management network interface. On certain servers, for example, the internal HTTP server strictly answers Redfish requests and restricts access to the standard web-management GUI available on the dedicated management port (though that port supports Redfish requests as well). 

Ultimately, isolating these services via a dedicated internal channel represents a highly sensible security decision on the BMC's part.