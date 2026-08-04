# Negative Resistance: A Deep Dive into Electronic Quirks

## 📌 Summary
This article explores the counterintuitive concept of **negative resistance** in analog electronics. It breaks down the fundamental definitions of electrical resistance, energy, and power, before diving into the mechanics of **true negative resistance** (using active circuits like operational amplifiers) and **negative differential resistance** (NDR, demonstrated via JFET "lambda diodes" and snapback behavior). 

---

## Introduction

If you tinker with analog electronics, you might have heard that some circuits can exhibit *negative resistance*. This is usually followed by a current-to-voltage plot featuring some sort of a kinked curve and an assertion that this property might help the circuit designer in some way.

But what does it mean, exactly? The concept of negative resistance is interesting, counterintuitive, and explained on Wikipedia in a rather rambling way. If you’re up for it, I think we can do better than that.

> *Note: This article assumes familiarity with voltage, current, and the behavior of operational amplifiers. If you need a refresher, [start with this primer](https://lcamtuf.substack.com/p/primer-core-concepts-in-electronic), then read up about transistors [here](https://lcamtuf.substack.com/p/how-do-transistors-work-anyway) and signal amplification [here](https://lcamtuf.substack.com/p/the-basics-of-signal-amplification).*

---

## Defining Resistance

As a quick recap, resistance ($R$) can be understood as the opposition to the flow of steady current through some portion of the circuit. The quantity describes the relationship between the applied electromotive force — that’s voltage — and the amount of charge moving per second (that’s current).

In contrast to some other phenomena in electronic circuits, resistance is not inherently dependent on time or signal frequency. If you know the voltage ($V$) applied to a purely-resistive component, the current ($I$) flowing at that exact moment is simply:

$$I = \frac{V}{R}$$

In **resistors**, the parameter remains constant across a wide range of operating conditions. This means that if we plot $I$ in relation to $V$, we get a straight line that crosses through the center of the coordinate system. The slope of the line depends only on the component’s resistance:

[![Resistor I = V/R plots](./images/80ac9128b98c.png)](https://lcamtuf.substack.com/p/negative-resistance)
*Resistor I = V/R plots for R = 0.2, 1, and 5 Ω.*

For example, in a $5\ \Omega$ resistor (blue line), the current is $200\text{ mA}$ if the voltage across the terminals is $1\text{ V}$, rising to $1\text{ A}$ if the electromotive force increases to $5\text{ V}$.

Some other components, such as diodes and transistors, oppose the flow of current in a manner that depends on the applied voltage. We can still model their behavior using the concept of resistance, but we don’t get a constant reading. In an [earlier article](https://lcamtuf.substack.com/p/things-you-can-do-with-diodes), I provided a V-I curve for a small diode; if we take these measurements and calculate the effective $R$ by rearranging the earlier equation ($I = V / R \implies R = V / I$), we obtain the log-scale V-to-R plot shown below:

[![Apparent resistance of a small diode](./images/9c38cc2e00e9.png)](https://lcamtuf.substack.com/p/negative-resistance)
*Apparent resistance of a small diode (1N4148), log vertical scale.*

For a chosen point of the $V-I$ curve, we can also calculate so-called **differential resistance**. This parameter doesn’t tell us anything about the overall relationship between voltage and current; instead, it models the relative response to small deviations from the chosen baseline. 

For example, in the vicinity of $1.2\text{ V}$ on the plot above, the slope of the V-I curve is such that a change of $\Delta v = \pm 10\text{ mV}$ causes the current to change by $\Delta i = \pm 20\text{ mA}$. If we divide $\Delta v$ by $\Delta i$, we can say that the “local” resistance is $500\text{ m}\Omega$. Again, that number has nothing to do with the bulk resistance of the diode at $1.2\text{ V}$, but it’s a useful abstraction for modeling what happens to small signals piggybacking on top of a constant bias voltage.

In physical terms, resistance is associated with the consumption of energy. We’re making an effort to push charges through; some of the energy is absorbed by the medium and turned into heat, light, motion, or captured in chemical bonds.

To model these dynamics, we tap into the official definition of voltage — the amount of energy ($E$, in joules) expended to move a unit of electrical charge ($Q$, in coulombs):

$$E = V \cdot Q$$

Combined with the definition of current ($Q = I \cdot t$) and power ($P = E / t$), we arrive at the fundamental power equation:

$$P = V \cdot I$$

For resistive circuits, we can further substitute $I = V / R$ and get:

$$P = \frac{V^2}{R}$$

So, a resistive element consumes energy provided by the power supply at a rate proportional to the square of the applied voltage, and inversely proportional to the component’s resistance. For example, a $220\ \Omega$ resistor subjected to $10\text{ V}$ will dissipate about $455\text{ mW}$ as heat.

---

## True Negative Resistance

This brings us to an interesting question: what would it mean for a component to have a resistance of less than $0\text{ ohms}$?

Well, we can start by stating the obvious: if $R$ is negative and $I = V / R$, then the current-to-voltage plot will have a downward slope. For example, for $R = -5\ \Omega$, we’d get the following:

[![A plot of constant negative resistance](https://substackcdn.com/image/fetch/$s_!XEAb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffc0d1d9-328f-4964-968b-a01e21686cca_2346x1252.png)](https://lcamtuf.substack.com/p/negative-resistance)
*A plot of constant negative resistance.*

It would appear that if we apply a positive voltage to a “negistor”, we should get a current proportional to the voltage but with an opposite sign. The natural flow of conventional current is from the more positive side to the more negative one, but here, it must flow the other way round.

Alas, a negistor can’t exist unless it’s equipped with an external power source. Recall our power dissipation formula: $P = V^2 / R$. If $R$ is negative, so is the consumed power. This implies the component would need to extract energy from its surroundings and put it back into the circuit.

However, if we allow an external power supply, a circuit with constant negative resistance can be constructed pretty easily:

[![Negative resistance converter schematic](./images/09dee889c9e1.jpg)](https://lcamtuf.substack.com/p/negative-resistance)
*Negative resistance converter.*

Assuming $R_1$ is large enough so that both the op-amp output pin and the signal source can supply worst-case currents, the circuit acts as a textbook non-inverting amplifier. If the resistors in the divider are the same, the amplifier’s gain is $2\times$, meaning:

$$V_{\text{out}} \approx 2 \cdot V_{\text{signal}}$$

The current flowing through $R_1$ can then be calculated as:

$$I = \frac{V_{\text{signal}} - V_{\text{out}}}{R_1} = \frac{V_{\text{signal}} - 2 V_{\text{signal}}}{R_1} = -\frac{V_{\text{signal}}}{R_1}$$

In other words, the circuit behaves the same as a negative resistance ($-R_1$) placed between $V_{\text{signal}}$ and the ground, as confirmed by this empirical plot:

[![Circuit behavior plot](./images/fa90921000b2.png)](https://lcamtuf.substack.com/p/negative-resistance)
*Circuit behavior. Dashed line is the ideal behavior of -220 Ω.*

---

## Negative Differential Resistance

The arrangement discussed above has some niche uses, but most of the time, “negative resistance” refers to a different phenomenon: **negative differential resistance (NDR)** — a V-I curve that looks normal in parts, but has a section with a downward slope.

[![Simple model of differential negative resistance](./images/c482e04ff001.png)](https://lcamtuf.substack.com/p/negative-resistance)
*A simple model of differential negative resistance.*

Here, because the overall resistance remains positive, such V-I kinks can manifest **without** the need for an additional power supply. An easily constructed example is the **lambda diode** configuration using two complementary JFETs:

[![Negative differential resistance with JFETs](./images/947933a3f828.jpg)](https://lcamtuf.substack.com/p/negative-resistance)
*Negative differential resistance with JFETs.*

In this circuit, the admitted current decreases sharply in the region between $5\text{ V}$ and $9\text{ V}$. The stretch between $7$ to $8.5\text{ V}$ corresponds to a delta of about $-2\text{ mA}$ per volt:

[![Current through the J111-J175 lambda diode](./images/a17a0acad7b5.png)](https://lcamtuf.substack.com/p/negative-resistance)
*Current through the J111-J175 lambda diode.*

Another flavor of negative differential resistance arises via **horizontal snapback**, where a controlled current is supplied, but past a certain point, the voltage needed to sustain it drops sharply:

[![Negative differential resistance via horizontal snapback](./images/696f094fdd2e.png)](https://lcamtuf.substack.com/p/negative-resistance)
*Negative differential resistance via horizontal snapback.*

As it turns out, you can get that behavior out of a single bipolar transistor — a pattern we’ve explored in previous discussions on this blog!

---

> *Error code 400: daily token limit exceeded. Higher limits are available to Skippy Premium and Premium+ subscribers.*