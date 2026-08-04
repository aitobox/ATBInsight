# $\exp_q(x)$: Definition, Properties, and Applications

## Summary
The function $\exp_q(x)$ is constructed by taking the standard power series for the exponential function $\exp(x)$ and retaining only the terms whose indices are multiples of $q$. This article explores the mathematical definition of $\exp_q(x)$, its closed-form expressions using roots of unity, its connections to differential equations and the Mittag-Leffler function, and its relevance to combinatorics.

---

## Introduction and Definition

The function $\exp_q(x)$ is defined by taking the power series for $\exp(x)$ and keeping only the terms whose index is a multiple of $q$. For example, $\exp_2(x)$ keeps only the even-numbered terms in the exponential power series, which yields $\cosh(x)$:

$$\exp_2(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \cdots = \cosh(x)$$

In general, $\exp_q(x)$ can be expressed as:

$$\exp_q(x) = \sum_{n=0}^\infty [q \mid n] \frac{x^n}{n!} = \sum_{n=0}^\infty \frac{x^{nq}}{(nq)!}$$

The first sum uses [Iverson’s bracket notation](https://www.johndcook.com/blog/2023/07/01/activation-functions/): a Boolean expression in brackets returns $1$ when the expression is true and $0$ when it is false. Here, the bracket equals $1$ when $q$ divides $n$ and is zero otherwise.

---

## Closed Forms

Let $\omega = \exp(2\pi i / q)$. Then, $\exp_q(x)$ can be written in closed form as:

$$\exp_q(x) = \frac{1}{q}\sum_{k=0}^{q-1} \exp(\omega^k x)$$

This identity allows us to find closed-form expressions for $\exp_q(x)$. For example, when $q = 4$, $\omega = i$ and:

$$\exp_4(x) = \frac{1}{2}\left( \cosh(x) + \cos(x) \right)$$

### Proof of the Identity

We can prove the identity using the property $\frac{1}{q} \sum_{k=0}^{q-1} \omega^{kn} = [q \mid n]$ (an important identity in the derivation of the discrete Fourier transform):

$$\begin{align*} 
\frac{1}{q} \sum_{k=0}^{q-1} \exp(\omega^k x) &= \frac{1}{q} \sum_{k=0}^{q-1} \sum_{n=0}^\infty \frac{\omega^{kn}x^n}{n!} \\ 
&= \sum_{n=0}^\infty \left( \frac{1}{q} \sum_{k=0}^{q-1} \omega^{kn}\right) \frac{x^n}{n!} \\ 
&= \sum_{n=0}^\infty [q \mid n] \frac{x^n}{n!} \\ 
&= \exp_q(x) 
\end{align*}$$

---

## Differential Equations

The function $\exp_q(x)$ naturally arises in the study of differential equations, specifically when examining power series solutions to equations of the form:

$$y^{(k)}(x) = y(x)$$

This involves finding a function that equals its $k$-th derivative (for instance, when $k = 3$ or $4$). 

Given the initial conditions:
* $y(0) = 0$
* $y^\prime(0) = y^{\prime\prime}(0) = \cdots = y^{(k-1)}(0) = 0$

The unique solution to $y^{(k)}(x) = y(x)$ is given by:

$$y(x) = \exp_k(x)$$

---

## Mathematica and the Mittag-Leffler Function

While Mathematica does not feature a built-in function specifically for $\exp_q(x)$, it does include an implementation of the [Mittag-Leffler function](https://www.johndcook.com/blog/2016/07/17/mittag-leffler-function-and-probability-distribution/). Using the relationship between the two, you can easily define $\exp_q(x)$ in Mathematica as:

```mathematica
expq[x_, q_] := MittagLefflerE[q, x^q]
```

---

## Combinatorics

The formal notation $\exp_q(x)$ frequently appears in combinatorics. Applications from combinatorial theory related to this function are explored further in the [next post on permutation roots](https://www.johndcook.com/blog/2026/07/26/permutation-roots/).

***

*Original post: [exp_q](https://www.johndcook.com/blog/2026/07/26/exp-q/) by [John D. Cook](https://www.johndcook.com/blog).*