# Locally Everywhere Does Not Imply Everywhere: The Fall of the Jacobian Conjecture

*By John D. Cook | [Original Article](https://www.johndcook.com/blog/2026/07/21/jacobian-conjecture/)*

---

## 📋 Summary
In a breakthrough development, mathematician Levent Alpöge used AI (Claude Fable 5) to discover a counterexample to the long-standing Jacobian conjecture in dimension $n = 3$. While the Inverse Function Theorem ensures the polynomial function is locally invertible everywhere, its failure to be globally injective disproves the conjecture for $n \ge 3$, leaving the case for $n = 2$ still open.

---

## 🤖 AI and the Mathematical Frontier
A couple of days ago, Levent Alpöge, a mathematician working at Anthropic, discovered a counterexample to the Jacobian conjecture using Claude Fable 5.

Curious about whether most mathematicians were trying to prove or disprove the conjecture, I asked Claude:

> *Before a counterexample to the Jacobian conjecture was found, did most mathematicians believe it was true or false?*

Claude’s response was:

> *The premise of this question isn’t quite right — no counterexample to the Jacobian conjecture has been found. It remains an open problem in mathematics: no one has proven it true, and no one has found a counterexample disproving it. … If you encountered a claim that a counterexample was found, do you have a source for that? I’d be happy to look into it, since that would actually be a major result in algebraic geometry if true.*

Of course, Claude doesn’t *know* that it solved the conjecture. It didn’t even solve the conjecture itself; it was merely an inanimate tool in the hand of a mathematician, just like a piece of chalk or a dry-erase marker.

The middle part of Claude’s response noted that mathematicians were previously divided on whether the conjecture was true. This placed it in a different category than the Riemann hypothesis (which most believe to be true) or the $P \neq NP$ conjecture (which most believe to be false).

---

## 📐 What is the Jacobian Conjecture?
The Jacobian conjecture states that a polynomial function from $\mathbb{R}^n$ to $\mathbb{R}^n$ with a constant, non-zero Jacobian determinant has a polynomial inverse. *(Note: The conjecture is more generally stated for fields of characteristic 0, where the derivatives defining the Jacobian are defined algebraically rather than through limits).*

---

## 🔍 Alpöge’s Counterexample
Alpöge formulated a counterexample: a polynomial function from $\mathbb{R}^3$ to $\mathbb{R}^3$ with a constant Jacobian determinant of $-2$. 

The function is defined as:

$$
\begin{align*}
F(x,y,z) = \bigl( \, 
& z (1+xy)^3 + y^2 (1+xy) (4+3xy), \\ 
& y + 3x(1+xy)^2 z + 3xy^2 (4+3xy), \\ 
& 2x - 3x^2 y - x^3 z \, \bigr)
\end{align*}
$$

It is a tedious but simple calculus exercise to show that the determinant equals $-2$ everywhere. 

### Why It Fails Globally
The Inverse Function Theorem states that a function is locally invertible at any point where the Jacobian determinant is non-zero. Therefore, Alpöge’s function is **locally invertible everywhere**.

However, the function maps certain distinct inputs to the same output:
* $(0, 0, -1/4)$ and $(1, -3/2, 13/2)$ both map to $(-1/4, 0, 0)$.

Because of this, the function is **not globally injective**, meaning it is not invertible. Consequently, the function lacks not only a polynomial inverse, but *any* inverse at all (even if non-polynomial functions are allowed).

---

## 🏁 Conclusion
Alpöge’s counterexample disproves the Jacobian conjecture for **$n = 3$**. 

This result can be trivially extended to all **$n > 3$** by applying Alpöge's function for three variables and the identity function for the rest. However, the conjecture remarkably remains **open for $n = 2$**.