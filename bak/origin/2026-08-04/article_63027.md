# The Story of How We (Eventually) Found Our Missing Firewall Rule

## Summary
In system administration, root-cause discovery is often messy, driven as much by coincidence and intuition as by methodical debugging. This article recounts the real-world troubleshooting chain of events that led to the discovery of a missing firewall rule on a high-demand web server—highlighting how unexpected drops in metrics can act as critical diagnostic signals.

---

## 1. The Overloaded Web Server and Collateral Damage
When we first deployed [our new web server for a highly in-demand data set](https://utcc.utoronto.ca/~cks/space/blog/web/ServerBruteForceBandwidthLimit), Apache wasn't configured to handle a high volume of concurrent connections. It was immediately overwhelmed with HTTP requests, but we initially shrugged off the alerts. 

However, because this constantly tripped [our monitoring system](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019), I turned up Apache's connection limits to an absurdly high number. While this kept monitoring happy, it pushed the server's outgoing bandwidth to 1G wire rates, which I figured was acceptable. 

Shortly after, an unrelated machine began suffering severe NFS performance problems. Upon investigation, [we realized it shared the same 1G switch as the hyper-active web server](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/SometimesItIsTheNetwork), and its network traffic was being completely crowded out.

## 2. Bandwidth Limits and Quick Fixes
In a rush to stop the bleeding and restore normal NFS performance, [I hastily added some `tc`-based bandwidth limits by hand](https://utcc.utoronto.ca/~cks/space/blog/linux/TcLimitServiceBandwidth)—meaning I typed [`tc`](https://www.man7.org/linux/man-pages/man8/tc.8.html) commands directly into an active shell session. 

A few days later, [we figured out how to configure `mod_qos` limits directly within Apache](https://utcc.utoronto.ca/~cks/space/blog/web/ApacheIfModuleMistake). One of the parameters we introduced was a strict ceiling on concurrent connections from a single IP address. The effect was immediate and dramatic: 
* The Apache error log showed heavy traffic from a subset of IPs hitting the threshold.
* Our metrics system showed concurrent requests plummeting to roughly half their previous levels.

## 3. Connecting the Dots: The Missing Firewall Rule
With the immediate crisis resolved, we had to decide whether to make the [`tc`](https://www.man7.org/linux/man-pages/man8/tc.8.html)-based limits permanent (which would require writing startup scripts, as this would be our first machine using [`tc`](https://www.man7.org/linux/man-pages/man8/tc.8.html) in production) or rely entirely on `mod_qos`. 

While weighing our options, I remembered that our perimeter firewall included [a general-purpose "block brute-force things" system](https://utcc.utoronto.ca/~cks/space/blog/unix/OpenBSDPfStateBits). It made sense to extend this to HTTP and HTTPS requests targeting our new web server as an extra layer of insurance. 

Immediately after applying this change, our metrics system registered *another* major drop in concurrent Apache connections, shrinking by half yet again. 

*(The perimeter firewall operates via an explicit allowlist of IP addresses subjected to HTTP/HTTPS limits; because our new web server had a fresh IP address, it simply hadn't been added to the list until now.)*

This secondary drop was the "aha!" moment. It explained [why our main legacy web server had largely avoided being overwhelmed by this traffic](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/SurpriseChangesAreASignal): that perimeter firewall rule was the one protection the old server possessed that the new one lacked. Our main server had no [`tc`](https://www.man7.org/linux/man-pages/man8/tc.8.html) limits, and `mod_qos` had been disabled years prior.

## Afterword & Post-Script
Ultimately, we decided to keep both the Apache `mod_qos` limits and the [`tc`](https://www.man7.org/linux/man-pages/man8/tc.8.html)-based limits as a defense-in-depth measure. We want to strictly enforce bandwidth caps on this specific server, and utilizing two independent mechanisms ensures that both would have to fail simultaneously for an overflow to occur. 

We aren't yet worried enough to implement bandwidth limits directly in FreeBSD PF—partly because a misconfiguration at the firewall level carries a much higher blast radius than breaking a single host.

***

*Source: [Finding Our Missing Firewall Rule](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/FindingOurMissingFirewallRule?showcomments#comments)*