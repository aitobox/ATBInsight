# Counting Rooted Trees

### Summary
While combinatorial problems are often studied for their own sake, they frequently intersect with applied mathematics in unexpected ways. This post explores the surprising connection between the enumeration of unlabeled rooted trees and the design of numerical methods for solving differential equations, specifically Runge-Kutta (RK) methods.

---

### The Combinatorial Connection
Counting the number of unlabeled rooted trees with $n$ nodes, denoted as $t(n)$, is a classic problem in pure mathematics. The sequence begins:
**1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, 12486, 32973, …**

These values grow exponentially. As proven by Richard Otter in 1948, the number of trees grows asymptotically as $C \alpha^n / n^{-3/2}$, where $\alpha \approx 2.9557$.

### Application: Runge-Kutta Methods
In numerical analysis, designing an $s$-stage explicit Runge-Kutta method requires solving a system of equations derived from the Taylor expansion of the differential equation. There is a direct one-to-one correspondence between the constraints on the $n$th derivative of an RK formula and the set of rooted trees.

To design an $s$-stage method, one must satisfy the constraints for all stages up to $s$. The total number of constraints $c(s)$ is given by the cumulative sum:
$$c(s) = \sum_{i=1}^{s} t(i)$$

For example, a 4-stage RK method requires $c(4) = 1 + 1 + 2 + 4 = 8$ constraints.

### The Complexity Gap
A significant challenge arises because the number of constraints grows exponentially, while the number of available parameters in an $s$-stage RK method grows only quadratically: $s(s+1)/2$.

*   **For $s=5$:** There are 17 constraints but only 15 variables. Despite this, the system remains solvable because symmetry considerations render some equations redundant.
*   **For high-order methods:** A 10th-order RK method requires 17 stages. Designing such a method involves solving over a million equations in 153 variables—a daunting task that has nonetheless been achieved in the literature.

---

### Footnotes
1.  **Terminology:** "Unlabeled" means we do not distinguish between nodes, though we do distinguish the root.
2.  **Sequence:** See [OEIS A000081](https://oeis.org/A000081).
3.  **Growth:** The cumulative sum is dominated by the size of the final term in the sequence.
4.  **Reference:** E. Hairer, "A Runge-Kutta Method of Order 10," *J. Inst. Maths Applics* (1978) 21, 47-59.

### Related Posts
* [Solving the RK4 equations](https://www.johndcook.com/blog/2026/07/31/runge-kutta-design/)
* [Counting permutations with roots](https://www.johndcook.com/blog/2026/07/27/counting-permutations-with-roots/)
* [DNA alignment and Kings](https://www.johndcook.com/blog/2026/06/30/dna-sequence-alignment-and-kings/)

***

*Source: [Counting rooted trees](https://www.johndcook.com/blog/2026/08/01/counting-rooted-trees/) by John D. Cook.*