# Sum of Low Squares

### Summary
This article explores a fascinating property of quadratic residues for primes $p \equiv 3 \pmod 4$. By summing the "low squares" (quadratic residues less than $p/2$), we derive a unique "signature" for each prime. Remarkably, this signature allows for the immediate recovery of the original prime $p$ through a simple arithmetic relationship, a phenomenon famously described as a mathematical parlor trick.

---

## Squares: High and Low
Let $p$ be an odd prime. Exactly half of the integers in the range $1 \le k < p$ are quadratic residues—numbers for which the congruence $x^2 \equiv k \pmod p$ has a solution. We refer to these as "squares."

For example, if $p = 7$, the squares are $1, 2,$ and $4$ (since $1^2=1, 3^2=9\equiv 2, 2^2=4$). The non-residues are $3, 5,$ and $6$.

We categorize these squares based on their magnitude:
*   **Low squares:** $0 \le k < p/2$
*   **High squares:** $p/2 < k < p$

## Signatures
For a prime $p > 3$ where $p \equiv 3 \pmod 4$, the **signature** of $p$ is defined as the sum of all low squares modulo $p$. 

The following Python code computes this signature:

```python
from sympy import isprime, is_quad_residue

def signature(p):
    assert(p > 3 and isprime(p) and p % 4 == 3)
    s = 0
    for k in range(1, 1 + p // 2):
        if is_quad_residue(k, p):
            s += k
    return s % p
```

## Inverse Signatures
It is a surprising result that the signature of $p$ is unique. Given a signature $s$, one can easily determine the original prime $p$. As presented by David M. Bloom [1], this property functions as a mathematical parlor trick.

Given a signature $s$, the prime $p$ can be recovered using the relationship:
$$p = \frac{16s + 1}{m}$$
where $m$ is the smallest integer in the set $\{3, 7, 11, 15\}$ such that the result is a prime number. Alternatively, $p$ is simply the largest prime factor of $16s + 1$.

### Implementation
The following functions demonstrate how to invert the signature:

```python
from sympy import factorint, isprime

def inverse_signature1(s):
    n = 16 * s + 1
    return max(factorint(n).keys())

def inverse_signature2(s):
    n = 16 * s + 1
    for m in [3, 7, 11, 15]:
        if n % m == 0 and isprime(n // m):
            return n // m
```

### Verification
We can verify this property for all primes $p < 1000$ where $p \equiv 3 \pmod 4$:

```python
for n in range(7, 1000, 4):
    if isprime(n):
        s = signature(n)
        assert(n == inverse_signature1(s))
        assert(n == inverse_signature2(s))
```

---
**Reference:**
[1] David M. Bloom. *A Quadratic Residues Parlor Trick*. Mathematics Magazine, Vol. 71, No. 3 (Jun., 1998), pp. 201–203.

*Content adapted from [John D. Cook](https://www.johndcook.com/blog/2026/07/19/sum-of-low-squares/).*