# Cursed Circuits #6: Reverse Avalanche Oscillator

## Summary
In this edition of *Cursed Circuits*, we explore a uniquely baffling oscillator built using an upside-down NPN transistor with a floating base. Despite defying conventional circuit logic, this setup successfully blinks an LED by exploiting the reverse avalanche breakdown and negative differential resistance of a heavily doped semiconductor junction—a hidden quirk of transistor behavior rarely found in textbooks.

---

## Introduction

Last year, I published an article titled *“It’s hard to build an oscillator.”* 

The title alluded to the fact that while there’s no shortage of oscillator circuits on the internet, many use unusual parts, require weird supply voltages, or barely function (if at all).

However, sometimes *bad* rises to an art form. Here is probably the most puzzling bad oscillator you can assemble today with the parts you already have at hand:

[![Reverse avalanche oscillator](./images/c8230a21d801.jpg)](./images/c8230a21d801.jpg)  
*Reverse avalanche oscillator. Other small NPN transistors should also work.*

---

## How It Works

At first glance, *nothing here makes sense*. The transistor is upside down, and its base terminal is completely disconnected. Yet, the circuit works: hook it to a 14–20 V power supply and watch the LED blink.

Connecting an oscilloscope across the capacitor reveals a repeating cycle: the capacitor charges up to about 10 V, then rapidly dumps its charge all the way down to 9.1 V:

[![Capacitor charge state with a 14 V supply](./images/e9604691b629.png)](./images/e9604691b629.png)  
*Capacitor charge state with a 14 V supply (5.8 Hz oscillation). By author.*

It is clear that the capacitor charges via the 1 kΩ resistor from the positive supply rail, and that energy is dumped into the LED through the upside-down NPN transistor. But why?

---

## Semiconductor Junctions & Breakdown

A conventional diode consists of a *p-n* junction formed from two distinct types of semiconducting materials, creating a non-conductive **depletion layer** at their boundary. 

* **Forward bias:** A small positive voltage applied to the *p*-side disrupts the depletion layer, allowing charge carriers to cross.
* **Reverse bias:** The depletion region remains impassable. However, if the applied reverse voltage is high enough, the electrostatic field accelerates charges violently enough to knock electrons into the conduction band via an **avalanche effect**, making the junction conductive again:

[![Breakdown in a 1N4148 diode](./images/2e172fa278cd.png)](./images/2e172fa278cd.png)  
*Breakdown in a 1N4148 diode. By author.*

An NPN transistor is essentially an *n-p-n* structure resembling two conjoined diodes. No matter how it is oriented, one diode is always reverse-biased. 

When oriented normally (collector positive), the breakdown voltage for a 2N2222 transistor is around 50 V. But flipped upside down, the emitter-collector threshold drops to just over 8 V. This occurs because the emitter area is more heavily doped ($n^{++}$), forming a thinner depletion region that is much easier to disrupt.

---

## The Secret: The V-I Curve

An ordinary reverse-biased diode still won't oscillate on its own, because it will eventually find a stable equilibrium where the charging current equals the discharging current. 

This circuit works because of the unique V-I characteristics of a reverse-biased NPN transistor with a floating base:

[![V-I plot for 2N2222 at IB = 0](./images/99c9bed6c2ab.png)](./images/99c9bed6c2ab.png)  
*V-I plot for 2N2222 at $I_B = 0$. Dashed line: what we’d expect of a diode.*

1. The $n^{++}-p-n$ structure remains non-conductive until roughly 8.2 V.
2. Once this "hump" is cleared, the conduction path opens up dynamically. At 5 mA we need ~8 V, but at 25 mA we only need 7 V.

This curve completely rules out a stable equilibrium. The capacitor charges until it hits the hump; a small discharge current then begins, but the resistor (~6 mA supply) pushes past it. This forces the capacitor onto the vertical portion of the curve where current skyrockets. 

Eventually, the capacitor voltage drops too low to sustain the current—and because of the negative slope of the curve, that lower voltage is *even less able* to sustain smaller currents. The transistor cuts off sharply, and the cycle repeats.

Old-timers might recognize that this behavior mimics a **neon lamp**, which requires a higher striking voltage to ionize gas, but a much lower voltage to maintain it once lit.

---

## Conclusion

To be clear: **everything about this oscillator is terrible!** It requires a high supply voltage, suffers from poor efficiency, demands a beefy capacitor, and exhibits abysmal duty cycle and frequency stability. 

However, it serves as a brilliant reminder that semiconductors are complex beasts, utilizing parts of the V-I curve that textbooks rarely show.

---

*I write about electronics, [the foundations of mathematics](https://lcamtuf.substack.com/p/monkeys-typewriters-and-busy-beavers), [the history of technology](https://lcamtuf.substack.com/p/a-brief-history-of-counting-stuff), and other geek interests. If you enjoyed this, please [subscribe](https://lcamtuf.substack.com/subscribe?).*