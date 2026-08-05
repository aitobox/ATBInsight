---
authors:
- aitoboxrobot
categories:
- 工具教程
date: '2026-08-04'
hide:
- navigation
tags:
- AI
- Linux
title: 将 TCP 连接分配给 Linux 流量控制的 'Flows'
---
# 将 TCP 连接分配给 Linux 流量控制的 'Flows'

### 背景与摘要
本文探讨了如何使用 Linux 的 `tc` (流量控制) 工具将来自单个 IP 地址的 HTTPS 流量聚合成单个“流 (flows)”。文章记录了作者为了对发出带宽实施限制而进行的网络配置实验。作者使用 `tc-flow` 替代了通常的 `tc-sfq` 来实现更精细的分组控制，详细介绍了两种配置方法：基于目标 IP 进行哈希计算分组，以及基于 /24 网络前缀进行映射分组。最后，文章指出了该方法面临的难题：难以监控验证过滤器是否按照预期正确地对流量进行了分配。

### Summary
本文探讨了使用 Linux 的 `tc` (流量控制) 实用程序将来自各个 IP 地址的 HTTPS 流量聚合成单个“流”所面临的挑战。虽然 `tc-sfq` 通常用于公平排队，但作者尝试使用 `tc-flow` 来获得对连接分组方式更精细的控制。文章详细介绍了两种具体的配置方法——按 IP 哈希以及按网络前缀映射——同时指出，要验证这些过滤器是否成功影响了流量分类是非常困难的。
> This article explores the challenge of aggregating HTTPS traffic from individual IP addresses into single "flows" using Linux's `tc` (traffic control) utility. While `tc-sfq` is typically used for fair queuing, the author experiments with `tc-flow` to gain more granular control over how connections are grouped. The post details two specific configuration approaches—hashing by IP and mapping by network prefix—while noting the difficulty in verifying whether these filters are successfully influencing traffic classification.

---

### Background
在之前限制 Web 服务器出站带宽的工作中，目标是将来自单一 IP 地址的所有 HTTPS 请求聚合成一个“流”，交由 `tc-sfq(8)` 处理。尽管 `tc-flow(8)` 正是为了这个目的而设计的，但其语法以难以驾驭而闻名。
> In previous efforts to limit outgoing bandwidth for a web server, the goal was to aggregate all HTTPS requests from a single IP address into one "flow" for `tc-sfq(8)`. Although `tc-flow(8)` is designed for this purpose, the syntax is notoriously difficult to navigate.

### Configuration Setup
下面的 class 用作受带宽限制流量的基础：
> The following class is used as the foundation for the bandwidth-limited traffic:

```bash
tc class add dev eno1 parent 1: classid 1:10 htb rate 400mbit ceil 500mbit prio 10
```

### Approach 1: Hashing by IP
为了根据目标 IP 聚合流量，我们使用了哈希过滤器。`handle` 参数对于过滤器被内核接受至关重要。
> To aggregate traffic based on the destination IP, we use a hash filter. The `handle` parameter is critical for the filter to be accepted by the kernel.

```bash
tc filter add dev eno1 protocol ip parent 1:10 handle 20 flow hash keys src,dst,proto,proto-src divisor 4096
```

*   **逻辑：** 由于 Web 服务器传出流量的源 IP、协议和源端口是恒定的，这有效地迫使流量由目标 IP 决定。
> *   **Logic:** Since the source IP, protocol, and source port are constant for a web server's outgoing traffic, this effectively forces the flow to be determined by the destination IP.
*   **注意：** 我们避免使用 `perturb` 来确保流量保持“粘性”，并使用一个较大的除数 (divisor) 以容纳大量并发连接。
> *   **Note:** We avoid `perturb` to ensure flows remain "sticky" and use a large divisor to accommodate a high volume of concurrent connections.

### Approach 2: Mapping by Network Prefix (/24)
为了更激进的聚合，可以使用 `map` 过滤器将目标 IP 按照 /24 子网进行分组：
> For more aggressive aggregation, one can group traffic by the destination's /24 subnet using a `map` filter:

```bash
tc filter add dev eno1 protocol ip parent 1:10 handle 20 flow map key dst rshift 8 divisor 4096
```

*   **逻辑：** 通过将目标 IP 右移 8 位，我们有效地隔离了前三个八位字节，从而按子网对流量进行分组。
> *   **Logic:** By right-shifting the destination IP by 8 bits, we effectively isolate the first three octets, grouping traffic by subnet.

### Integration with `tc-sfq`
为了确保排队规则与过滤器匹配，`sfq` qdisc（排队规则）必须配置为具有相匹配的流数量：
> To ensure the queueing discipline matches the filter, the `sfq` qdisc must be configured with a matching number of flows:

```bash
tc qdisc add dev eno1 parent 1:10 handle 10: sfq flows 4096 divisor 4096
```

### Challenges and Observations
首要障碍是**可观测性**。没有标准的方法来检查特定连接被分配到了哪个流，这使得很难验证过滤器是否如预期般运行。
> The primary obstacle is **observability**. There is no standard way to inspect which flow a specific connection has been assigned to, making it difficult to verify if the filters are functioning as intended. 

作者指出：
> The author notes:
*   尚不清楚过滤器应该附加到类 (`parent 1:10`) 还是直接附加到 `sfq` qdisc (`parent 10:`)。
> *   It is unclear whether the filters should be attached to the class (`parent 1:10`) or directly to the `sfq` qdisc (`parent 10:`).
*   使用 `iftop` 的初步测试表明流过滤器可能没有执行预期的聚合，尽管仍难以获得明确的证实。
> *   Initial testing with `iftop` suggests that the flow filters may not be performing the intended aggregation, though definitive confirmation remains elusive.
