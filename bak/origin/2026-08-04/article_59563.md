# Poppy the Training Box, Part 1: The Beginnings

## Executive Summary
Frustrated by tying up his daily driver PC (`perry`) for multi-day local LLM training runs, author Giles Thomas resurrects an old small-form-factor PC named `poppy`. Originally built in 2020 for travel and gaming, `poppy` is upgraded with a spacious new case, a high-capacity 1600W power supply, and a second-hand RTX 3090. After surviving an accidental 11-day training run, a dead CPU fan resulting in a 115°C thermal spike, and component replacements, `poppy` is successfully transformed into a dedicated, fully functional local LLM training rig.

---

## The Motivation: Why Build a Dedicated Rig?
For a while, the plan has been to put together a separate machine for local LLM training. Until now, training has been done on the daily driver desktop, `perry` (equipped with an RTX 3090). While successful—such as training a 163M-parameter GPT-2 small style LLM in JAX—this setup posed several drawbacks:

* **Sluggish Performance:** CPU and GPU heavy loads make everyday tasks sluggish.
* **No Gaming:** Tying up the PC for days rules out gaming.
* **No Parallel Experiments:** While the GPU is busy training, scoping out next steps or running other experiments is impossible.

Additionally, training runs were arbitrarily capped at two days simply because that was the maximum acceptable downtime for `perry`. Longer training runs could yield fascinating results. 

Longer-term goals include building a multi-GPU box to test large-scale cloud parallel training locally without paying high hourly cloud rental fees. Finally, the author has always wanted to build a custom water-cooling loop. 

This post covers the baseline: repurposing an old PC, installing a second-hand eBay RTX 3090, accidentally training an LLM for 11 days, and nearly cooking a CPU.

---

## Meet `poppy` (Original Build)
Before moving to Lisbon full-time, a small form-factor PC named `poppy` was built in 2020 with specific constraints:
* **Carry-on friendly:** Small enough to fit in a carry-on bag for travel between London and Portugal.
* **Portable:** Easy to move around the flat when hosting guests.
* **Gaming capable:** Powerful enough to run games like *Assassin's Creed Odyssey*.

### Original Component List
* **CPU:** AMD Ryzen 5 3600 (3.6GHz, 6-Core)
* **CPU Cooler:** Noctua NH-L9a-AM4
* **Motherboard:** Gigabyte X570 I AORUS PRO WIFI Mini ITX
* **RAM:** 32 GiB Corsair Vengeance DDR4
* **Storage:** 2x Samsung 970 Evo 500 GB NVMe SSDs
* **GPU:** Zotac GTX 1660 Super 6 GiB
* **Case:** Lian Li PC-TU100 Mini ITX
* **PSU:** Corsair SF450 450W SFF

Once `perry` became the main daily driver in Lisbon, `poppy` sat unused in the corner of the study. It was time for an upgrade.

---

## Phase 1: Moving to a New Case and PSU
Initial troubleshooting revealed `poppy` wouldn't power on, pointing to a faulty PSU. Anticipating the need to support multiple graphics cards eventually, new components were acquired:
* **PSU:** ASRock Phantom Gaming PG-1600G 1600W (capable of handling up to three RTX 3090s and a CPU).
* **Case:** Fractal Design North XL Mesh ATX Full Tower (offering plenty of space for multiple GPUs and water cooling).

After installing the old mini-ITX motherboard and new PSU into the North XL case, the system powered on successfully. The Arch Linux OS was wiped and reinstalled with a fresh configuration.

---

## The Accidental 11-Day LLM Training Run
As a burn-in test, a cut-down version of GPT-2 small was trained using a PyTorch setup:
* **Vocab Size:** 50,257
* **Context Length:** 512 (down from 1024)
* **Embedding Dimensions:** 512 (down from 768)
* **Heads / Layers:** 8 / 8 (down from 12 / 12)
* **Parameters:** ~76.9 million (requiring a ~1.5B token training run)

### Results
* **Perry (RTX 3090):** Completed the baseline run in ~9 hours drawing 368W.
* **Poppy (GTX 1660 Super):** Ran at 100% reported usage, but effectively choked at 53% utilization (67W draw), taking **267.57 hours (~11 days)**. 
* **Energy Cost:** Poppy consumed nearly 18kWh compared to Perry's 3.3kWh. *Buy an RTX 3090, save the planet!*

Despite the speed bottleneck, evaluation tests showed promising text generation and comparable loss scores to Perry's models. 

---

## Upgrading to an RTX 3090
An affordable, trustworthy RTX 3090 was sourced from Bulgaria via eBay. Upon installation, the card powered up with a vibrant, crystal-textured RGB disco display—making the mesh-sided case a welcome choice over glass.

---

## Troubleshooting: The Crispy CPU Spike
During the first full training test with the new 3090, `poppy` abruptly shut down after ten minutes. 

Investigation revealed the Noctua CPU cooler fan wasn't spinning. InfluxDB monitoring showed historical data: the CPU had been idling at a scorching **70°C+ for over a month**, culminating in an emergency thermal shutdown spike at **115°C**. 

A replacement fan (**Noctua NF-A9x14 PWM**) was ordered via Amazon next-day delivery. Upon installation, idle temperatures stabilized at a healthy 35.5°C.

---

## Final Testing and Successful Run
With cooling restored, a full-length standard LLM training run was initiated:
* **Completion Time:** ~40 hours (comparable to `perry`).
* **Tokens Seen:** 3.26 Billion
* **Train Loss / Test Loss:** ~3.530 / ~3.548 (virtually identical to Perry's benchmarks).

The model's output (*"Every effort moves you and your customers..."*) proved the rig was fully operational and ready for action.

---

## Conclusion and Next Steps
`poppy` is now a fully configured local training box featuring a single RTX 3090, a stable CPU, and ample room for expansion. 

**Next Steps:**
1. Transition to custom water cooling. 
2. Because supporting multiple GPUs will eventually require a new motherboard and CPU, water-cooling the current CPU is skipped.
3. Instead, a water block will be installed on the GPU first to build a single-component loop—and hopefully ditch the RGB lighting along the way.