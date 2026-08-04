# Ratio of Metallic Ratios

> **Summary:** While the golden, silver, and bronze ratios are well-known, higher-order metallic ratios lack standard names. However, any positive real number—and by extension, constants like $\pi$—can be closely approximated by taking the ratio of two metallic ratios, a property demonstrated here using mathematical limits and Python.

---

## Defining Metallic Ratios

The golden ratio is the first and best-known of the metallic ratios, followed by the [silver ratio](https://www.johndcook.com/blog/2026/06/30/silver-kings/) and the [bronze ratio](https://www.johndcook.com/blog/2023/04/14/metallic-ratios/). The metallic ratios that follow bronze do not have standard names.

The $n$-th metallic ratio $M(n)$ is defined as the number whose continued fraction representation contains all $n$s:

$$n + \cfrac{1}{n+\cfrac{1}{n+\cfrac{1}{n+\cdots}}} = \frac{n + \sqrt{n^2 + 4}}{2}$$

When $n = 1, 2,$ and $3$, we get the gold, silver, and bronze ratios, respectively.

---

## Approximating Real Numbers

You can approximate any positive real number as a ratio of metallic ratios. To see why, note that for large $n$, $M(n)$ is approximately $n$. 

For any positive rational number $a/b$, the following limit holds:

$$\lim_{n\to\infty} \frac{M(na)}{M(nb)} = \frac{a}{b}$$

By taking $n$ large enough, you can make $\frac{M(na)}{M(nb)}$ as close to $\frac{a}{b}$ as you like. Since the rational numbers are dense in the reals, this allows you to approximate any positive real number to arbitrary precision.

---

## Finding $\pi$ via Metallic Ratios

We can search for metallic ratios whose quotient approximates $\pi$ to within $0.001$ using the following Python code:

```python
from math import pi, sqrt

M = lambda n: 0.5 * (n + sqrt(n**2 + 4))

for n in range(1, 100):
    a = round(pi * n)
    b = n
    r = M(a) / M(b)
    if abs(r - pi) < 0.001:
        print(a, b, r)
```

This snippet demonstrates that:

$$\pi \approx \frac{M(132)}{M(42)} \approx 3.1412\dots$$

### Are Smaller Numbers Possible?

Could we find smaller integers that achieve the same precision? The following script confirms that the answer is no:

```python
k = 132 + 42

# Loop over numbers whose sum is less than k
for n in range(1, k):
    for a in range(1, n):
        b = n - a
        r = M(a) / M(b)
        if abs(r - pi) < 0.001:
            print(a, b, r)
            exit()
```

---

## Related Posts

* [Pell is to silver as Fibonacci is to gold](https://www.johndcook.com/blog/2024/09/01/pell-numbers/)
* [Golden ellipse](https://www.johndcook.com/blog/2024/10/10/golden-ellipse/)
* [Derivative equals inverse](https://www.johndcook.com/blog/2026/06/29/derivative-equals-inverse/)

***

*Based on the original post [Ratio of metallic ratios](https://www.johndcook.com/blog/2026/08/04/ratio-of-metallic-ratios/) by [John D. Cook](https://www.johndcook.com/blog).*