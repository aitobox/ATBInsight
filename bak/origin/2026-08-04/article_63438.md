# Trying to Stress Apache to 10,000 Connections (With No Answer Yet)

## Summary
Inspired by a discussion on the Fediverse, an administrator investigates whether an out-of-the-box Apache build with minimal tuning can handle the legendary C10K challenge (10,000 simultaneous connections). Using a non-critical production server running Ubuntu 24.04 and the Apache event MPM, the experiment revealed unexpected challenges in generating enough traffic, while highlighting the nuance between active workers and total concurrent connections.

---

## The Experiment
Recently on the Fediverse, someone wondered if an out-of-the-box build of Apache (with minimal tuning) could handle 10,000 simultaneous HTTP requests—the classic **C10K** target that was once a major industry milestone. 

At [the University of Toronto Computing Services](https://support.cs.toronto.edu/), we happen to have [a web server that has previously hit 4,000 simultaneous requests](https://utcc.utoronto.ca/~cks/space/blog/web/ServerBruteForceBandwidthLimit), with every indication that the traffic would have climbed higher if our connection limits allowed it. Since hitting that high-water mark, [we've put an assortment of limits on the web server](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/FindingOurMissingFirewallRule) that significantly reduced traffic. However, removing those limits in the spirit of experimentation seemed like a great way to see how high our Apache setup could actually go.

*(Note: I wouldn't normally experiment with a production service, but we don't consider this particular service very important. If it falls over often enough that people start keeping their own local copies of the data instead of repeatedly downloading it from us, that's actually a feature.)*

---

## Server Configuration
The specific configuration of this web server is:
* **OS:** Ubuntu 24.04 LTS
* **Web Server:** Standard Ubuntu Apache
* **Hardware:** 16 GB of RAM
* **MPM:** [Event MPM](https://httpd.apache.org/docs/2.4/mod/event.html)

Non-standard settings applied for the test:
```apache
MaxRequestWorkers   11000
ServerLimit         768
```
*(This is far more processes than we normally need, but HTTP requests linger around for a long time on this server, and I was aiming for overkill for a quick test.)*

---

## The Unexpected Bottleneck: Reasonable Clients
Apache (re)started fine with these settings and is running smoothly. However, I can't yet confirm whether it stands up to 10,000 connections because **nobody is hammering the server**. 

Contrary to previous client behavior—where massive waves of simultaneous requests would flood in the moment they could—the number of connections now hovers around a modest 2,000 to 3,000. Sometimes it even dips lower (down to around 1,500). 

On one hand, it's great that users have stopped aggressively overloading this server. On the other hand, it's slightly inconvenient that everyone decided to be reasonable at the exact moment I actually wanted a stress test.

---

## Clarifying Workers vs. Connections
This experiment required me to correct [my previous entry](https://utcc.utoronto.ca/~cks/space/blog/web/ServerBruteForceBandwidthLimit) regarding our 4,000-connection limit. 

We were actually tracking and limiting the number of **active workers** (via `MaxRequestWorkers 4000`), rather than total connections. I had overlooked the fact that the [event MPM](https://httpd.apache.org/docs/2.4/mod/event.html) allows for significantly more simultaneous connections than active workers under the right circumstances. 

When we were previously hitting the worker limit, our metrics indicate we actually peaked at around **5,300 simultaneous connections**. Presumably, the extra 1,300 connections were sitting in a state that a worker could handle asynchronously alongside its other activity.

*(The graph I was reading previously reported active workers because that is normally what matters most. If Apache runs out of workers, it stops answering new requests entirely—including requests to [scrape its server status page](https://utcc.utoronto.ca/~cks/space/blog/web/ApacheServerStatusLimitation).)*

---

## Key Takeaway
One major lesson from this learning experience is that the question *"Can Apache handle 10,000 connections?"* is somewhat under-specified. 

At least with the [event MPM](https://httpd.apache.org/docs/2.4/mod/event.html), there is a massive difference between **10,000 active workers** and **10,000 connections**, where a significant portion of those connections do not tie up a dedicated worker. How many non-worker connections you can maintain depends heavily on what you are serving and how HTTP clients behave. Given that our server deals heavily in large file downloads, it likely skews toward a higher connection-to-worker ratio.

***

**P.S.** Looking back at [our metrics system](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019), this server usually displays only a modest gap of a few hundred connections between busy workers and total connections. However, the difference occasionally peaked at over 4,000 during Apache shutdowns and restarts (or graceful reloads).