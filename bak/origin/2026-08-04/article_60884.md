# You Should Probably Check on Your Smart Appliances

## Executive Summary

Data collected from the **Anubis reputation database** and **Sourceware** honeypot reveals that internet-wide scraping is far more pervasive than previously understood. 

Crucially, **80–90% of the IP addresses** triggering the honeypot do not appear on any existing threat-monitoring lists. This traffic spans 229 countries and over 21,000 Autonomous System Numbers (ASNs), indicating a massive, highly distributed global crisis. Experts suspect that the primary drivers behind this traffic are **compromised smart appliances** unwittingly funneled into residential proxy networks.

---

## Honeypot Data Analysis

Recent telemetry from Sourceware's integration with Anubis provides a stark look at incoming automated web traffic.

### Overview Statistics

| Field | Value | Share / Percentage |
| :--- | :--- | :--- |
| **Lines Read** | 2,678,193 | — |
| **Unique IPs** | 2,678,193 | 100% |
| **Flagged (in DB)** | 286,161 | 10.7% |
| **Clean (not in DB)** | 2,392,032 | **89.3%** |

---

### Flags of Flagged Addresses

| Flag Type | Unique IPs | Share of Flagged |
| :--- | :--- | :--- |
| `is_vpn` | 1,264 | 0.4% |
| `is_datacenter` | 7,918 | 2.8% |
| `is_crawler` | 46 | 0.0% |
| `is_proxy` | 2,562 | 0.9% |

---

### Threat Categories

| Category | Unique IPs | Share |
| :--- | :--- | :--- |
| **abuse** | 282,182 | 98.6% |
| **datacenter** | 7,918 | 2.8% |
| **proxy** | 2,562 | 0.9% |
| **vpn** | 1,264 | 0.4% |
| **crawler** | 46 | 0.0% |
| **tor** | 17 | 0.0% |

---

### Top Providers

> *Methodology note: "Provider" refers either to the organization associated with the IP address or the source list (e.g., public ranges from Scaleway, FireHOL, or FreeDesktop).*

| Provider | Unique IPs | Share |
| :--- | :--- | :--- |
| `netshield` | 237,945 | 83.2% |
| `bitwire` | 96,539 | 33.7% |
| `magicteamc` | 26,475 | 9.3% |
| `ipinsights` | 17,378 | 6.1% |
| `threathive` | 8,422 | 2.9% |
| `netmountains` | 6,673 | 2.3% |
| `multacom` | 2,676 | 0.9% |
| `fyvri` | 2,433 | 0.9% |
| `cbuijs` | 1,916 | 0.7% |

*(Remaining 98+ providers omitted for brevity; view the [full dataset appendix](https://xeiaso.net/notes/2026/check-your-smart-tv/full-table/) for complete records).*

---

### Geographic Distribution (Top Impacted Countries)

| Country | Total Unique IPs | Flagged IPs | Flag Rate |
| :--- | :--- | :--- | :--- |
| **Bangladesh (BD)** | 59,245 | 17,735 | 29.9% |
| **Ukraine (UA)** | 32,261 | 8,920 | 27.6% |
| **Iraq (IQ)** | 62,047 | 13,613 | 21.9% |
| **Venezuela (VE)** | 64,670 | 13,780 | 21.3% |
| **Pakistan (PK)** | 85,241 | 17,083 | 20.0% |
| **South Africa (ZA)** | 43,919 | 7,431 | 16.9% |
| **Indonesia (ID)** | 38,119 | 6,122 | 16.1% |
| **Brazil (BR)** | 270,937 | 18,282 | 6.7% |

*(Data spans 229 distinct countries globally).*

---

## How the Anubis Honeypot Works

To accurately measure the true volume of web scrapers, the [Anubis honeypot feature](https://anubis.techaro.lol/docs/admin/honeypot/overview) injects semantically invalid, hidden HTML structures into standard challenge pages. 

A typical payload looks like this:

```html
<script type="ignore">
  <a href="/.within.website/x/cmd/anubis/api/honeypot/<uuidv4>/init">Don't click me</a>
</script>
```

When poorly written scrapers parse and follow these hidden endpoints, they consume generated anti-content laced with recursive links. This traps the scraper in an isolated loop while capturing clean diagnostic telemetry about the attacker's origin.

---

## A Global Crisis Driven by Smart Appliances

Because the offending IP addresses are distributed across thousands of ASNs and hundreds of nations, analysts believe this is not merely traditional data center scraping. 

Instead, a significant volume of traffic originates from **compromised smart appliances** (such as smart TVs and IoT devices) quietly drafted into malicious proxy networks. Mitigating this threat will likely require concerted, global action—and highlights why robust web application firewalls (WAFs) like Anubis have become essential infrastructure for modern web operators.