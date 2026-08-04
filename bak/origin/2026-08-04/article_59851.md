# An Unusual Cause for DHCP Exhaustion: The "Screaming" Host

### Summary
A malfunctioning device on a network can inadvertently trigger a total DHCP service outage by responding to ICMP Echo requests for every IP address. Because the ISC DHCP server performs a "ping check" before assigning dynamic leases, a host that answers all pings causes the server to perceive the entire IP pool as occupied, effectively blocking all new dynamic address assignments.

---

### The Mechanism of Failure
The ISC DHCP server (`dhcpd`) includes a built-in safety mechanism designed to prevent IP address conflicts. Before offering a dynamic IP to a client, the server sends an ICMP Echo request (ping) to that address. If the server receives a reply, it assumes the IP is already in use and marks it as "abandoned."

When a device on the network is misconfigured to respond to pings for *every* IP address—a behavior often referred to as a "screaming" host—the DHCP server concludes that every available address in its pool is already taken. Consequently, the server stops issuing new leases, leading to a complete network-wide DHCP failure.

### Identifying the Symptoms
If your ISC DHCP server is suffering from this issue, you will typically see the following error patterns in your logs:

```text
dhcpd[1656384]: Reclaiming abandoned lease 172.17.101.132.
[...]
dhcpd[1656384]: ICMP Echo reply while lease 172.17.101.132 valid.
dhcpd[1656384]: Abandoning IP address 172.17.101.132: pinged before offer
```

### Troubleshooting and Resolution
Tracking down a "screaming" host can be difficult, as it may not be immediately obvious which device is responding to the pings. 

*   **Check ARP Tables:** In the case described, the rogue device used its actual MAC address to answer the pings. This caused the DHCP server's ARP table to be flooded with the same MAC address associated with various IP addresses, providing a clear trail.
*   **Switch Diagnostics:** If the MAC address isn't immediately obvious, you may need to inspect switch ARP tables or port-level traffic statistics to identify the source of the anomalous ICMP responses.
*   **Network Isolation:** As a last resort, administrators may need to systematically disconnect segments of the network to isolate the offending device, though this is highly disruptive.

### Why Port Isolation Didn't Help
Even in networks utilizing **Port Isolation** (or Private VLANs), this issue can persist. Because the DHCP server must maintain connectivity with the entire network to function, its ARP requests and ICMP probes are permitted to traverse the switch fabric. The rogue device, by virtue of being on the network, can intercept these probes and respond, regardless of the isolation settings intended to prevent client-to-client communication.

***

*Source: [Original post by cks on the Fediverse](https://mastodon.social/@cks/116891615025664130)*