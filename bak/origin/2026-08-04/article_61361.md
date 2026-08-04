# Tech Note: Making Your Own V–I Plots at Home

## Executive Summary
While writing the book *The Secret Life of Circuits*, the author sought authentic data for every electrical diagram rather than relying on idealized textbook approximations or hand-drawn sketches. This technical note details the methodology, hardware setup, and programming logic used to capture precise, real-world Voltage-Current (V–I) curves for diodes and transistors. By moving beyond traditional oscilloscopes to use benchtop multimeters, source measure units (SMUs), thermal management (mineral oil), and automated pulse-testing, the author reveals the nuanced realities of semiconductor behavior that often contradict standard textbook theory and manufacturer datasheets.

---

## 1. The Problem with Textbook Electronics
Most popular electronics tutorials and textbooks rely on diagrams that are either retraced from ancient literature or sketched from memory, resulting in overly idealized representations of semiconductor behavior. 

Capturing accurate parametric plots—which show the relationship between voltage and current in semiconductor devices—presents several distinct engineering hurdles:
* **Measurement extremes:** Currents can be too minute for standard oscilloscopes in some regions, yet skyrocket abruptly in others, risking component failure ("magic smoke").
* **Thermal drift:** Semiconductor junction characteristics change with temperature, including self-heating caused by currents as low as 1 mA, causing oscilloscope readings to drift constantly.

---

## 2. The DIY Lab Setup
To overcome these limitations, the author transitioned to a more robust instrumentation and cooling strategy:
* **Instruments:** An oscilloscope was replaced with a **benchtop digital multimeter (DMM)** capable of measuring microamps and microvolts, paired with a pulsed power lab supply to mitigate heating-induced drift.
* **Thermal Cooling:** The device under test (DUT) was submerged in a non-conductive liquid (**mineral oil**) to keep temperatures stable.
* **Automation via SCPI:** To avoid tedious manual logging, instruments were interfaced with a computer using **SCPI (Standard Commands for Programmable Instruments)** over Ethernet (TCP port 5025).
* **The Upgrade to an SMU:** Needing precise remote control, the author acquired a secondhand **Source Measure Unit (SMU)**—specifically a Rohde & Schwarz NGU401—which combines a power supply and multimeter with ultra-fast response times.

---

## 3. Data Streaming and Firmware Logic
Using the SMU's native data streaming mode (**FastLog**), the setup achieved sampling rates between 100 and 500k samples per second, transmitting voltage-current pairs as 4-byte binary floats over an Ethernet connection. 

* **Diode Measurement C Code:** The implementation (available [here](https://lcamtuf.coredump.cx/soft/embedded/ngu401_fastlog_diode.c)) uses FastLog at 10 ksps:
  * For low currents ($< 0.3\text{ mA}$), supply voltage remains on, averaging 2,500 data points to yield a noise-free microamp reading.
  * For higher currents, power is pulsed on for 5 ms, averaging the top 20 samples from the buffer.
* **MOSFET Measurement C Code:** For higher voltage spans (exceeding the SMU's 20 V limit by adding a floating power supply in series), the code shifts from fixed signals to **1 ms pulses at a 1% duty cycle** to prevent overheating. Continuous current sampling runs for ~2.5 seconds per set point (source code available [here](https://lcamtuf.coredump.cx/soft/embedded/ngu401_mosfet.c)).

---

## 4. Key Discoveries & Real-World Observations

### Diodes (1N4148 and BAT46)
* **Exponential Limits:** While diode V–I relationships are taught as strictly exponential, real-world data shows divergence past ~10 mA due to semiconductor substrate resistance.
* **Schottky Anomalies:** Testing small Schottky diodes like the [BAT46](https://www.vishay.com/docs/85662/bat46.pdf) yields unconventional curves that match manufacturer data sheets precisely, proving the test setup's accuracy.

### Zener Diodes (1N4731 and BZX79)
* Low-voltage Zener diodes (e.g., [1N4731](https://assets.nexperia.com/documents/data-sheet/1N4728A_SER.pdf)) exhibit less steep reverse-breakdown curves, requiring precise current matching. The breakdown "knee" sharpens noticeably past ~5 V (observed across [BZX79](https://assets.nexperia.com/documents/data-sheet/BZX79.pdf) variants).

### Transistors (BS170 and 2N7000 MOSFETs)
* **Constant-Current Region:** The [BS170](https://www.onsemi.com/download/data-sheet/pdf/mmbf170-d.pdf) acts largely as a constant-current device across its operating range, with limits dictated by $V_{GS}$.
* **Breakdown Realities:** Textbooks show transistor breakdown as a sharp, vertical drop at the rated 60 V. Real-world testing reveals a much more gradual degradation when practical $V_{GS}$ levels are applied.
* **Datasheet Discrepancies:** Comparing the [2N7000](https://ww1.microchip.com/downloads/en/DeviceDoc/2N7000-N-Channel-Enhancement-Mode-Vertical-DMOS-FET-Data-Sheet-20005695A.pdf) Microchip datasheet against real lab captures exposed major scale disagreements, whereas Fairchild/ON Semiconductor specs aligned almost perfectly with empirical results.