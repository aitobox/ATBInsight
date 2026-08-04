# Assigning TCP Connections to Linux Traffic Control 'Flows'

### Summary
This article explores the challenge of aggregating HTTPS traffic from individual IP addresses into single "flows" using Linux's `tc` (traffic control) utility. While `tc-sfq` is typically used for fair queuing, the author experiments with `tc-flow` to gain more granular control over how connections are grouped. The post details two specific configuration approaches—hashing by IP and mapping by network prefix—while noting the difficulty in verifying whether these filters are successfully influencing traffic classification.

---

### Background
In previous efforts to limit outgoing bandwidth for a web server, the goal was to aggregate all HTTPS requests from a single IP address into one "flow" for `tc-sfq(8)`. Although `tc-flow(8)` is designed for this purpose, the syntax is notoriously difficult to navigate.

### Configuration Setup
The following class is used as the foundation for the bandwidth-limited traffic:

```bash
tc class add dev eno1 parent 1: classid 1:10 htb rate 400mbit ceil 500mbit prio 10
```

### Approach 1: Hashing by IP
To aggregate traffic based on the destination IP, we use a hash filter. The `handle` parameter is critical for the filter to be accepted by the kernel.

```bash
tc filter add dev eno1 protocol ip parent 1:10 handle 20 flow hash keys src,dst,proto,proto-src divisor 4096
```

*   **Logic:** Since the source IP, protocol, and source port are constant for a web server's outgoing traffic, this effectively forces the flow to be determined by the destination IP.
*   **Note:** We avoid `perturb` to ensure flows remain "sticky" and use a large divisor to accommodate a high volume of concurrent connections.

### Approach 2: Mapping by Network Prefix (/24)
For more aggressive aggregation, one can group traffic by the destination's /24 subnet using a `map` filter:

```bash
tc filter add dev eno1 protocol ip parent 1:10 handle 20 flow map key dst rshift 8 divisor 4096
```

*   **Logic:** By right-shifting the destination IP by 8 bits, we effectively isolate the first three octets, grouping traffic by subnet.

### Integration with `tc-sfq`
To ensure the queueing discipline matches the filter, the `sfq` qdisc must be configured with a matching number of flows:

```bash
tc qdisc add dev eno1 parent 1:10 handle 10: sfq flows 4096 divisor 4096
```

### Challenges and Observations
The primary obstacle is **observability**. There is no standard way to inspect which flow a specific connection has been assigned to, making it difficult to verify if the filters are functioning as intended. 

The author notes:
*   It is unclear whether the filters should be attached to the class (`parent 1:10`) or directly to the `sfq` qdisc (`parent 10:`).
*   Initial testing with `iftop` suggests that the flow filters may not be performing the intended aggregation, though definitive confirmation remains elusive.