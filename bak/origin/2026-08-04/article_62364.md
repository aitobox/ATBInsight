# When Sine of $x$ Degrees Equals Sine of $x$ Radians

> ## 📌 Summary
> Ordinarily, calculating the sine of $x$ in radians yields a very different result than in degrees. However, there are specific mathematical exceptions where $\sin(x) = \sin(x^\circ)$. This article explores the general formulas for these intersection points, presents an alternative derivation using trigonometric identities, and demonstrates how these solution families are dense in the interval $[-1, 1]$, allowing for arbitrarily close approximations to any target sine value.

---

Ordinarily, the sine of $x$ radians and the sine of $x$ degrees are very different numbers. Having your calculator in radian mode when it should be in degree mode, or vice versa, usually results in a major error.

But sometimes it doesn’t matter. A trivial example is when $x = 0$. A more interesting example is:

$$x = \frac{180\pi}{180 + \pi} \approx 3.08770208\dots$$

For that value of $x$:

$$\sin(x) = \sin(x^\circ)$$

*(Note: Following standard convention, this article uses radians by default and denotes degrees with a $^\circ$ symbol.)*

Since $x = \frac{\pi x^\circ}{180}$, we are looking to solve the equation:

$$\sin(x) = \sin\left(\frac{\pi x}{180}\right)$$

---

## Deriving the General Solutions

Two angles $A$ and $B$ have the same sine if they differ by a multiple of $2\pi$, or if they are supplementary ($A = \pi - B$), or both. In other words, $A$ and $B$ have the same sine if they are either equal $\pmod{2\pi}$ or supplementary $\pmod{2\pi}$. 

This means that $\sin(x) = \sin\left(\frac{\pi x}{180}\right)$ if and only if:

$$x = \frac{\pi x}{180} + 2\pi k$$

or

$$x = \pi - \frac{\pi x}{180} + 2\pi k$$

for some integer $k$. 

Solving these yields two general forms for all solutions:

$$x = \frac{360\pi k}{180 - \pi}$$

or

$$x = \frac{180\pi (2k + 1)}{180 + \pi}$$

---

## Alternative Solution

The derivation above is correct, but we can arrive at the same conclusion more simply using the sum-to-product identity:

$$\sin(A) - \sin(B) = 2 \cos\left(\frac{A + B}{2}\right) \sin\left(\frac{A - B}{2}\right)$$

Thus, $A$ and $B$ have the same sine if:

$$\cos\left(\frac{A + B}{2}\right) = 0 \quad \text{or} \quad \sin\left(\frac{A - B}{2}\right) = 0$$

These two possibilities directly correspond to the two families of solutions outlined above.

---

## Density of Solutions

When reduced modulo $2\pi$, both families of solutions are dense in $[0, 2\pi]$. This means that for every $y$ in $[-1, 1]$, there exists a number $x$ such that:

$$\sin(x) = \sin(x^\circ) \approx y$$

Furthermore, we can make this approximation as precise as we would like.

### Example 1

Let's set our target value to $y = 0.722$ with an approximation tolerance of $\varepsilon = 0.0001$. We want to find a value of $x$ from the first family of solutions such that:

$$\left| \sin\left(\frac{360\pi k}{180 - \pi}\right) - 0.722 \right| < 0.0001$$

The smallest integer $k$ that satisfies this is $k = 96343$. This gives:

$$x = \frac{360 \times 96343 \pi}{180 - \pi} \approx 616093.78713621\dots$$

And indeed, $\sin(x) \approx 0.72191\dots$

### Example 2

Now, let's set $y = 0.2026$ and look for a solution in the second family, using a stricter tolerance of $\varepsilon = 10^{-6}$. We search for the smallest $k$ such that:

$$\left| \sin\left(\frac{180\pi (2k + 1)}{180 + \pi}\right) - 0.2026 \right| < 10^{-6}$$

The smallest qualifying integer is $k = 741141$. Evaluating this yields:

$$\sin(4576848.310950611) = \sin(4576848.310950611^\circ) \approx 0.202600139\dots$$

---

*Source: Adapted from an article by [John D. Cook](https://www.johndcook.com/blog/2026/07/22/degrees-radians/).*