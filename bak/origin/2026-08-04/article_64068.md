# So You Want to Use Plants to Reduce Indoor $\text{CO}_2$

## Summary
While the idea of using houseplants to clean the air and neutralize exhaled carbon dioxide sounds appealing, physics makes it wildly impractical for a normal home. To offset the $\text{CO}_2$ produced by a single human, you would need massive energy inputs (equivalent to multiple space heaters), intense grow lighting, at least 17.6 square meters of densely packed ferns, and a system capable of harvesting and discarding roughly 4.6 kilograms of fresh plant matter every single day. Ultimately, you are much better off simply opening a window.

---

## The Dream vs. Reality

Humans make carbon dioxide. Carbon dioxide is (sometimes claimed to be) bad for cognition. But plants turn carbon dioxide back into oxygen. And plants are the one true home decoration strategy. So maybe if you get a lot of plants, you can keep carbon dioxide in check and keep your brain working?

It’s theoretically possible. It’s probably just barely possible in practice. But it won’t be easy.

## The Math of Human Exhalation

People produce roughly **1 kilogram of carbon dioxide per day**. That’s around $5.7 \times 10^{23}$ molecules, or $0.948$ moles per hour. (You may remember from high school that a [mole](https://en.wikipedia.org/wiki/Mole_(unit)) is a gigantic number made up to avoid having factors of $10^{23}$ everywhere.) Let’s keep it simple and call it **one mole per hour**.

Meanwhile, plants turn carbon dioxide into oxygen through photosynthesis—specifically, the chemical [reaction](https://en.wikipedia.org/wiki/Photosynthetic_efficiency) of:

$$\text{6 } \text{H}_2\text{O} + \text{6 }\text{CO}_2 + \text{Energy} \longrightarrow \text{C}_6\text{H}_{12}\text{O}_6 + \text{6 }\text{O}_2$$

The minimum energy physically needed to convert 1 mole of carbon dioxide into glucose and oxygen via this reaction is roughly **477 kilojoules**.

## Step-by-Step Energy Requirements

### 1. The Theoretical Lower Bound
If you had magical plants that somehow channeled all incoming energy into photosynthesis with perfect efficiency, they would need ~477 kilojoules per hour, which converts to a continuous usage of **132.5 watts**.[^1] That’s a bit more than what’s used by two incandescent light bulbs—not too bad!

### 2. The Biological Reality of Chloroplasts
Real plants don't have magic; they perform photosynthesis through a [physical process](https://en.wikipedia.org/wiki/Photosynthesis#Z_scheme) with two steps, each involving four electrons absorbing a photon. That means you need **eight photons per carbon dioxide molecule**. 

If you tune your lights for maximum efficiency, giving each photon the minimum energy necessary to excite an electron (~1.8 eV), you need pure red light with a wavelength of 680 nm. This results in a continuous usage of **386 watts**.[^2] No physical system using chloroplasts can neutralize your $\text{CO}_2$ using less than that.

### 3. Optical Losses
Your houseplants won’t be able to grab every single photon that hits them. In practice, [~30%](https://en.wikipedia.org/wiki/Photosynthetic_efficiency#:~:text=30%25,-of) of photons will reflect off the plant, pass right through it, or hit a non-chloroplast part of the plant. That bumps our requirement up to **551 watts**.[^3]

### 4. Plant Respiration
After making glucose, what happens to it? Some goes toward growing more plant (permanently sequestering carbon), but much of it is burned by the plant just to stay alive, releasing the carbon right back into the air. Assuming a standard ~40% loss due to respiration,[^4] our requirement climbs to **918 watts**.[^5]

## Living in a Tanning Booth

That still might not sound *that* bad. But consider what it's like to live in a room with **918 watts of pure red light**. 

* In terms of radiant power, that is equivalent to **~765 incandescent lightbulbs**.[^6] 
* Modern LED grow bulbs are ~50% efficient, meaning you actually need to spend **~1836 watts**. 
* Factor in the light lost to the room and the lower efficiency of using normal white light frequencies instead of pure red, and you are realistically looking at **5,000 to 10,000 watts**. 

Most of that energy is dumped into your living space as heat. Imagine **five space heaters** blasting on high, all day, every day.

## The Space Problem: Photon Flux Density

Plants can’t absorb infinite amounts of light. Chloroplasts take time to "reset" before they can absorb more photons. Your pet fern can only absorb roughly **52 watts of energy per square meter** of leaf surface area.[^7]

No matter how much light you produce, neutralizing your daily $\text{CO}_2$ output requires:

$$\frac{918 \text{ watts}}{52 \text{ W/m}^2} = 17.6 \text{ square meters of fern leaf}$$

Picture a **4.2-meter square wall** packed *solid* with ferns. If there are any gaps, stems, soil, or wall showing, it needs to be even larger. That is the absolute physical minimum.

## Where Does the Carbon Go?

If plants remove carbon from the air, they must put it somewhere. The only place it can go (other than back into the air) is into the physical structure of the plant.

* The 1 kg of $\text{CO}_2$ you produce daily contains **273 grams of elemental carbon**.
* Dry plant matter is only ~50% carbon.
* For each gram of dry plant matter, plants hold [5–10 grams of water](https://pmc.ncbi.nlm.nih.gov/articles/PMC10058729/#:~:text=Table%201,-%2E) (depending on the species).

To sequester all the carbon you make, your indoor garden must grow:

$$\begin{aligned}
& 1 \text{ kg CO}_2 \\
\times \quad & 0.273 \text{ kg carbon / kg CO}_2 \\
\times \quad & 2 \text{ kg dry plant / kg carbon} \\
\times \quad & 8.5 \text{ kg actual plant / kg dry plant} \\
\mathbf{= \quad} & \mathbf{4.6 \text{ kg of actual plant per day}}
\end{aligned}$$

That is **140 kg (308 lbs) per month**. You must prune, harvest, and discard all of this plant matter outside your home; otherwise, the carbon eventually decomposes and returns right back to your indoor air.

---

## Conclusion: How to Use Plants for $\text{CO}_2$ Reduction

1. Build an industrial indoor farm.
2. Weigh it.
3. Wait two weeks.
4. Weigh it again.
5. Divide the increase in weight by your own body mass.
6. That is the fraction of your $\text{CO}_2$ you're actually removing from the environment.
7. **Open a window.**

---

## Footnotes

[^1]: [Behold](https://www.google.com/search?q=%281+mole+%2F+hour%29+%C3%97+%28477+kJ+%2F+mole%29+to+watts) the power of [arithmetic](https://dynomight.net/arithmetic/): $(1 \text{ mole CO}_2 / \text{hour}) \times (477 \text{ kJ} / \text{mole CO}_2) = 132.5 \text{ watts}$. ↩
[^2]: Using units: $(1 \text{ mole CO}_2 / \text{hour}) \times (8 \text{ photons} / \text{CO}_2 \text{ molecule}) \times (1.8 \text{ eV} / \text{photon}) = 385.94 \text{ watts}$. Chloroplasts are thus at most ~34% ($132.5 / 385.94$) efficient at channeling light energy into photosynthesis. ↩
[^3]: This 30% loss figure comes from sunlight filtered to the 400–700 nm range. If you use pure 680 nm light with *very* densely packed plants, you might drop this loss to 10–20%. ↩
[^4]: Wikipedia cites a [35–45%](https://en.wikipedia.org/wiki/Photosynthetic_efficiency#:~:text=35%E2%80%9345%25) loss just for respiration in the leaf itself, while [this paper](https://rseco.org/book/export/html/115.html#:~:text=RGR%2E-,Figure%206%2E18) shows numbers ranging from 30% to 56% depending on species and growth rate. ↩
[^5]: This gives an overall efficiency of $132.5 / 918 \approx 14.4\%$. Accounting for the fact that real sunlight contains wavelengths outside the ideal range, Wikipedia estimates real-world leaf efficiency closer to 5.4%, aligning closely with these physical constraints. ↩
[^6]: A traditional "60-watt" incandescent bulb's rating is based on power *input*, but only ~2% is converted to visible light. Therefore, 918 watts of red light equates to roughly $918 / 60 / 0.02 = 765$ lightbulbs. Note that because human eyes [aren't very sensitive](https://dynomight.net/colors/) to 680 nm light, the perceived brightness won't feel nearly as blinding. ↩
[^7]: The saturation point of plants is typically measured at ~300 $\mu\text{mol/m}^2/\text{s}$ for shade-tolerant houseplants. At 680 nm, 300 $\mu\text{mol}$ of photons carries ~51.92 joules of energy per square meter of leaf surface per second, or **52 watts**. ↩