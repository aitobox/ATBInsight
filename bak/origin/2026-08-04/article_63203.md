# Permutation Roots

## Summary
This article explores the concept of square roots and higher roots of permutations, demonstrating how to compute them using Python and analyzing their existence through cycle structures. Furthermore, it delves into the probability of a random permutation possessing a $k$-th root, linking the problem to generating functions and providing a Mathematica script for exact calculations.

---

## Introduction to Permutation Roots

Let $\sigma$ be a permutation on $n$ elements. If there is a permutation $\tau$ such that applying $\tau$ twice has the same effect on the list of elements as applying $\sigma$ once, we write $\sigma = \tau^2$, and call $\tau$ a **square root** of $\sigma$.

Representing the $n$ elements as the integers $0$ through $n-1$, we can represent permutations by their action on this list. In Python, we can represent a permutation as a tuple of length $n$ and compose them using the following function:

```python
import itertools

def compose(sigma, tau):
    """Return the composition σ ∘ τ (apply τ first, then σ)."""
    return tuple(sigma[j] for j in tau)
```

## Finding Roots Computationally

We can easily construct permutations that have square roots by squaring a known permutation. Running the following code:

```python
tau = (3, 1, 4, 5, 2, 0)
sigma = compose(tau, tau)
```

We find $\sigma = (5, 1, 2, 0, 4, 3)$. By construction, $(3, 1, 4, 5, 2, 0)$ is a square root of $\sigma$, though it is not necessarily the only one.

The brute-force approach below counts the number of square roots for a given permutation:

```python
import itertools

def numroots(sigma):
    n = len(sigma)
    c = 0
    for tau in itertools.permutations(range(n)):
        if sigma == compose(tau, tau):
            c += 1
    return c

print(numroots(sigma))
print(numroots((1, 2, 3, 4, 5, 0)))
```

This code demonstrates that $\sigma$ has four square roots, while the rotation $(1, 2, 3, 4, 5, 0)$ has **no** roots.

## Existence of Roots and Cycle Structure

The `numroots` function has a runtime proportional to $n!$, making it impractical for large permutations. Fortunately, a theorem states:

> A permutation $\sigma$ has a square root if and only if the number of cycles it has of every even length is even [1].

This concept naturally extends to cubes, cube roots, and higher powers and roots.

## Probabilities of Root Existence

How common is it for permutations to have square roots, cube roots, etc.? If you pick a random permutation on $n$ elements, what is the probability that it has a $k$-th root?

While this is a difficult question in general, it is equivalent to finding the coefficient of $x^k$ in the infinite product:

$$\prod_{m=1}^\infty \exp_{\text{gcd}(m, k)} \left(\frac{x^m}{m}\right)$$

This is Theorem 4.8.3 in [1], which served as the motivation for exploring $\exp_q$ in a [previous post](https://www.johndcook.com/blog/2026/07/26/exp-q/).

### Computing Probabilities in Mathematica

Although the product is infinite, we only need to compute terms up to the power of $x$ of interest. The following Mathematica code computes the exact probability that a permutation on $n$ elements has a $k$-th root:

```mathematica
expq[x_, q_] := MittagLefflerE[q, x^q]	 
p[n_, k_] := SeriesCoefficient[	 
    Product[expq[x^m/m, GCD[m, k]], {m, 1, n}], {x, 0, n}]
```

For example, using this method reveals that the probability of a permutation of 10 elements having a square root is $\frac{29}{96}$.

---

## References

1. Herbert Wilf, *Generatingfunctionology*. Available online [here](https://www2.math.upenn.edu/~wilf/DownldGF.html).

***

*The post [Permutation roots](https://www.johndcook.com/blog/2026/07/26/permutation-roots/) first appeared on [John D. Cook](https://www.johndcook.com/blog).*