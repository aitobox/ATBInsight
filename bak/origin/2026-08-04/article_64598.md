# Estimating a Cumulative Sum

### Summary
This article explores the asymptotic behavior of the cumulative sum of unlabeled rooted trees. By leveraging the known asymptotic growth of the number of trees ($t(n)$), we derive an estimate for their cumulative sum ($c(n)$). This approach demonstrates a general technique for estimating cumulative sums of rapidly increasing sequences.

---

### Introduction
In a previous discussion, I introduced two sequences:
*   **$t(n)$**: The number of unlabeled rooted trees with $n$ nodes (OEIS [A000081](https://oeis.org/A000081)).
*   **$c(n)$**: The cumulative sum of the former, defined as $c(n) = \sum_{i=1}^n t(i)$ (OEIS [A087803](https://oeis.org/A087803)).

The sequence $c(n)$ is significant in numerical analysis, specifically representing the number of constraints on an $n$-step Runge-Kutta method.

### Asymptotic Derivation
For large $n$, the number of unlabeled rooted trees is given by:
$$t(n) \sim C \frac{\alpha^n}{n^{3/2}}$$
where $C \approx 0.4399$ and $\alpha \approx 2.9557$.

To estimate $c(n)$, we assume that the cumulative sum of the asymptotic estimates provides a reliable approximation for the cumulative sum of the sequence. This is valid because the sequence grows exponentially, meaning the final terms dominate the total sum.

The derivation follows:
$$
\begin{align*} 
c(N) &= \sum_{n=1}^N t(n) \\ 
&\sim \sum_{n=1}^N C \frac{\alpha^n}{n^{3/2}}\\ 
&= C \frac{\alpha^N}{N^{3/2}} \sum_{k=0}^{N-1} \alpha^{-k}\left(1 - \frac{k}{N} \right)^{-3/2} \\ 
&\sim C \frac{\alpha^N}{N^{3/2}} \sum_{k=0}^\infty \alpha^{-k} \\ 
&= C \frac{\alpha^N}{N^{3/2}} \frac{\alpha}{\alpha-1} \\ 
&= C \frac{\alpha^{N+1}}{(\alpha-1)N^{3/2}} 
\end{align*}
$$

### Implementation and Visualization
The following Python code demonstrates the rate of convergence between the exact cumulative sum and our derived asymptotic approximation:

```python
import numpy as np
import matplotlib.pyplot as plt

# A000081 sequence data
A000081 = [0, 1, 1, 2, 4, ...] # Truncated for brevity
A087803 = np.cumsum(A000081)

def approx(n):
    C = 0.43992401257102530
    a = 2.95576528565199497
    return C * a**(n+1) * n**(-3/2) / (a - 1)

n = np.arange(len(A087803))
ratio = A087803 / approx(n)

plt.plot(n[1:], ratio[1:])
plt.axhline(1, color='r', linestyle='--')
plt.xlabel("$n$")
plt.ylabel("exact/approx")
plt.show()
```

The resulting plot confirms that as $n$ increases, the ratio of the exact value to our approximation converges toward 1, validating the accuracy of the asymptotic formula.

***

*This post first appeared on [John D. Cook](https://www.johndcook.com/blog).*