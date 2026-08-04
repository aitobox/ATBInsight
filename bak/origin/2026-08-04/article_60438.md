# Panel Meter Calculator with Floating Point

## 📝 Summary
This project bridges a historical gap in calculator evolution by creating an electromechanical calculator powered by analog panel voltmeters. Featuring a custom CNC-milled maple enclosure, an AVR128DA28 microcontroller, and a unique 6+5 digit fixed-point arithmetic system, the device combines vintage aesthetics with modern embedded programming.

---

## 🛠️ Building the Display Panel
Unusual clocks are common in DIY electronics, but electromechanical displays on calculators are rare. To solve this, a custom display was constructed using:
* A **3 mm acrylic sheet** spray-painted blue on the back, with lettering and window cutouts processed via a **CNC mill**.
* Six generic **"SO-45" panel voltmeters** from Amazon, alongside one vintage edgewise voltmeter sourced from eBay (dedicated to floating-point representation).
* Custom faces printed on adhesive paper ([Download Template](http://lcamtuf.coredump.cx/soft/embedded/meter_calc.pdf)).
* Two **Dialight 656 series panel indicators** ([Catalog Page](https://www.dialight.com/wp-content/uploads/2021/07/Dialight_PMI_catalog_April2021.pdf)) to signal negative results and overflows.

---

## 🪵 Crafting the Enclosure and Keypad
Because the display panel is bulky, a non-standard keyboard layout was designed: ten digits and a decimal point arranged in two rows on the left, paired with a cluster of five operator keys on the right.

* **Material:** Resawn thin maple lumber stock.
* **Key Switches:** Sixteen high-end 18×18 mm **NKK JF series tactile switches** ([Catalog](https://www.nkkswitches.com/pdf/JFnonilluminated.pdf)) wired in a 4×4 grid matrix.
* **Finishing:** Custom vinyl decals for keys and CNC-machined recessed typography on the enclosure.

---

## ⚡ Circuitry and Software
Rather than attempting unpredictable analog calculations, the brains of the operation rely on an 8-bit **AVR128DA28 MCU**:
* **Power:** Directly supplied from a 5V wall wart.
* **Driving Meters:** Uses pulse-width modulation (PWM) across seven digital lines (`PD0`–`PD6`).
* **Keypad Scanning:** Handled by a 4×4 sense-drive grid (`PA0`–`PA7`).
* **Indicators:** Controlled via two lines (`PC0`, `PC1`).
* **Math Logic:** Uses custom **fixed-point (6+5 digit) arithmetic** to bypass floating-point accuracy issues ([Source Code](https://lcamtuf.coredump.cx/soft/embedded/meter_calc.c)).

### User Interface Quirks
The calculator UI handles operations intuitively despite hardware limitations:
* Pressing `+`, `×`, or `÷` twice repeats operations.
* `-` acts as a sign-change prefix (unless pressed immediately after the equals key).
* Pressing `=` twice clears the calculator state (compensating for the lack of a dedicated `C` button).

---

## 📺 Demonstration
The video below showcases the calculator successfully handling fractions, negative numbers, and overflow conditions:

> *Note: External video embed from Vimeo.*

---

## 📚 About the Author
If you enjoyed this article, check out ***The Secret Life of Circuits***—a richly illustrated, lucid introduction to electronics featuring over 420 pages of original content, 290+ color diagrams, and zero AI. 

*Interested in more articles on electronics, mathematics, and technology history? Consider subscribing to the author's [Substack](https://lcamtuf.substack.com/subscribe?).*