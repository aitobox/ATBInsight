# DIY Phase-Change Cooled Clothing: Making an 18°C Personal AC Vest

## Summary
Beating the summer heat with traditional air conditioning is energy-intensive and impossible to take on the go. While standard refrigerants, thermoelectric coolers, and evaporative cooling all fall short for wearable tech, **phase-change materials (PCMs)** offer a brilliant solution. By formulating a custom, low-cost **18°C "ice" mixture** using sodium sulfate, table salt, and a gelling agent, you can create DIY cooling packs that absorb body heat without freezing your skin. These packs can be frozen without electricity (just using a cool basement), packaged in heat-sealed polyethylene bags, and worn comfortably under loose clothing for hours of portable cooling.

---

## 1. The Problem with Traditional Cooling

Summer is getting hotter, and while it isn't actively dangerous everywhere yet, it is undeniably unpleasant. 

* **Vapor-Compression Refrigeration (Fridges & AC):** Uses a low boiling-point liquid that evaporates to absorb heat, then compresses and cools the vapor via a radiator to repeat the cycle. While great for buildings, the compressor, hot-side radiator, and power requirements make it impossible to fit inside a shirt.
* **Thermometric Cooling:** Replaces plumbing with semiconductor junctions, but they produce more heat than they remove, require massive radiators, draw huge amounts of power, and are expensive.
* **Evaporative Cooling:** The classic hot-day hack of water and airflow, but it fails entirely in humid climates—right when you need it most.

**The Alternative:** Instead of carrying a fridge with you, what if you could take *the cold itself* with you? 

Melting one gram of ice bottles up 333 joules of heat at a constant temperature. However, 0°C is too cold for direct skin contact, and it sits >30°C below ambient, making insulation difficult. What is needed is a cheap, safe material with a freezing point around **~20°C**—cool enough to refresh you, but easy to transport.

---

## 2. Choosing the Right Material

### Pure Glycerin
* Melting point: 17.8°C | Heat-of-fusion: ~200 J/g.
* **The Catch:** Commercial grades contain a few percent water, pushing the freezing point down significantly, and pure glycerin is difficult to purify at home.

### Sodium Sulfate (The Winner)
* A non-corrosive, non-reactive, and mild chemical.
* It forms "decahydrate" crystals (~55% water by mass) that decompose into water and sodium sulfate above 32°C, and reform crystals when cooled.
* Melting one gram absorbs 252 J of heat. 
* **The Adjustment:** 32°C is a bit too warm for personal cooling, but adding regular table salt lowers the eutectic freezing point down to **~18°C**.
* **Bonus:** This mixture can be frozen simply by leaving it in a basement or a deep hole in the ground—**no electricity required**.

---

## 3. The 18°C "Ice" Mixture Formula

| Quantity (by mass) | Ingredient |
| :--- | :--- |
| 1000 g or ml | Water |
| 320 g | Sodium sulfate (anhydrous) |
| 75 g | Table salt (NaCl) |
| 10 g *(optional)* | Polysaccharide thickener |
| 10 g *(optional)* | Borax |

### Preparation Steps
1. **Heat and Dissolve:** Heat the water, sodium sulfate, and salt until the solution is saturated (small crystals should form on the surface). Use a covered container to minimize evaporation.
2. **Add Additives:** Mix the borax and thickener as dry powders and slowly add them to the hot solution (an immersion blender works great here).
3. **Boil:** Lightly boil for ~15 minutes.
4. **Cool:** Let it cool to room temperature. It should solidify into a stable gel that won't spill.

> *Note: These measurements sit slightly above the solubility limit in hot water, leaving some residual salt, which is completely fine.*

### Role of Additives
* **The Thickener (Carboxymethyl cellulose or Xanthan gum):** Prevents decahydrate crystals from settling or forming a hard mass, avoiding separation during thermal cycling. Mix xanthan gum with another dry powder first to avoid clumping (do not use sodium sulfate, as it also clumps).
* **The Borax:** Helps with crystal nucleation and prevents mold growth. It is food-safe in the EU up to 0.4% (E285), though you can increase it to ~5% if supercooling/crystallization issues persist.
* **Water-Soluble Dye (Recommended):** Makes it easy to spot leaks and identify different batches.

---

## 4. Packaging and Wearable Design

* **The Bag Dilemma:** Standard plastic sandwich bags always leak over time. Heat-sealable polyethylene bags are much stronger, withstand pressure, and allow you to create partitioned channels so the goo doesn’t all pool at the bottom. Fix any minor leaks with hot-melt glue.
* **Making it Wearable:** Sewing the heat-sealed edges directly to a fabric strip creates an ugly but highly functional harness. Attach this strip to shoulder straps to hold the packs firmly against your chest (or back).
* **Pro-Tips for Wearing:** 
  * Wear a t-shirt underneath the packs to keep them clean.
  * Wear light-colored, loose-fitting clothes over everything to shield them from direct sunlight.

---

## 5. Test Results & Design Notes

* **Performance:** In a lab calorimeter test, the un-salted brine yielded ~171 J/g (67% of theoretical maximum). Adding the 7.5% sodium chloride reduced the heat capacity to around **90 J/g**, rendering it about 30% as effective as pure water ice, but perfectly tuned for safe, comfortable cooling.
* **Real-World Test:** Two 600g, 1cm-thick packs stayed cold for roughly **one hour** when worn. Together, they provide 108 kJ of cooling capacity and pull about 30W of heat. 
* **Cost Efficiency:** Because the raw materials cost pennies, making multiple spare packs for longer excursions is cheap and easy.

---

## 6. Related Resources & References

* **Academic Paper:** DOI [10.1109/ITHERM55368.2023.10177562](https://ieeexplore.ieee.org/document/10177562) — A reference detailing a very similar phase-change mixture.
* **Video:** [The Vapor Compression Route](https://www.youtube.com/watch?v=qv0IJM3BV9Y)
* **Video:** [Eutectic Na₂SO₄/NaCl Mixtures](https://www.youtube.com/watch?v=Nqxjfp4Gi0k)