# Solving the RK4 Design Equations

## Summary
This article explores the historical and mathematical process behind deriving the classic fourth-order Runge-Kutta (RK4) method. By examining the system of eight non-linear constraints for ten parameters, the post demonstrates how modern tools like Mathematica can effortlessly handle calculations that were once famously described by early mathematicians as "very tedious." It also touches upon alternative formulations, such as the 3/8 rule and Gill's method for constrained hardware.

---

## Introduction

While researching the Runge-Kutta method for solving differential equations, a passage from Hairer, Nørsett, and Wanner [1] caught my attention:

> *“These calculations, which are not reproduced in Kutta’s paper (they are however in Huen (1900)), are very tedious.”*

These calculations refer to a set of eight algebraic constraints that the parameters of a fourth-order Runge-Kutta method must satisfy. It made me wonder how much assistance Mathematica might have provided to Mr. Huen in his "very tedious" work had it been available back in 1900.

While I discuss the general mechanics of Runge-Kutta methods in [another post](https://www.johndcook.com/blog/2020/02/13/runge-kutta-methods/), here I want to focus strictly on a key step in their design: solving the underlying system of design equations.

---

## The RK4 Constraint Equations

The parameters of a fourth-order Runge-Kutta method must satisfy the following system of eight equations:

$$
\begin{align*} 
b_1 + b_2 + b_3 + b_4 &= 1 \\ 
b_2 c_2 + b_3 c_3 + b_4 c_4 &= \frac{1}{2} \\ 
b_2 c_2^2 + b_3 c_3^2 + b_4 c_4^2 &= \frac{1}{3} \\ 
b_3 a_{32} c_2 + b_4(a_{42} c_2 + a_{43} c_3) &= \frac{1}{6} \\ 
b_2 c_2^3 + b_3 c_3^3 + b_4 c_3^3 &= \frac{1}{4} \\ 
b_3 c_3 a_{32} c_2 + b_4 c_4(a_{42} c_2 + a_{43} c_3) &= \frac{1}{8} \\ 
b_3 a_{32} c_2^2 + b_4(a_{42} c_2^2 + a_{43} c_3^2) &= \frac{1}{12} \\ 
b_4 a_{43} a_{32} c_2 &= \frac{1}{24} 
\end{align*}
$$

The first crucial observation is that **there are 10 variables and only 8 equations**, meaning the system is underdetermined and does not have a single unique solution. What we typically think of as *the* fourth-order Runge-Kutta method is actually just *a* fourth-order Runge-Kutta method.

---

## Solving with Mathematica

To arrive at a specific solution, we can add auxiliary constraints. For instance, if we set $b_2 = b_3$ and $c_2 = c_3$, the system gains enough constraints to yield a unique solution, which Mathematica finds instantly:

```mathematica
eqs = {
    b1 + b2 + b3 + b4 == 1,
    b2*c2 + b3*c3 + b4*c4 == 1/2,
    b2*c2^2 + b3*c3^2 + b4*c4^2 == 1/3,
    b3*a32*c2 + b4*(a42*c2 + a43*c3) == 1/6,
    b2*c2^3 + b3*c3^3 + b4*c4^3 == 1/4,
    b3*c3*a32*c2 + b4*c4*(a42*c2 + a43*c3) == 1/8,
    b3*a32*c2^2 + b4*(a42*c2^2 + a43*c3^2) == 1/12,
    b4*a43*a32*c2 == 1/24,
    b2 == b3,
    c2 == c3
};

vars = {b1, b2, b3, b4, c2, c3, c4, a32, a42, a43};

solution = Solve[eqs, vars]
```

Executing this code returns the exact parameter set used for the standard RK4 method featured in nearly every introductory textbook.

### Variations and Alternative Rules

* **The 3/8 Rule:** If you retain the requirement $b_2 = b_3$ but substitute $2c_2 = c_3$ for the $c$ parameters, Mathematica outputs the coefficients for the Runge-Kutta 3/8 rule, which offers certain minor advantages.
* **Gill’s Method:** In 1951, A. Gill [2] discovered an RK4 rule optimized specifically for extremely constrained computer hardware. It is a fascinating approach featuring irrational parameters tailored to the hardware limitations of early computing.

> **Update:** For a deeper dive into the parameters and constraints governing higher-order RK methods, check out [this follow-up post](https://www.johndcook.com/blog/2026/08/01/counting-rooted-trees/).

---

## Related Posts

* [Dormand and Prince](https://www.johndcook.com/blog/2020/02/19/dormand-prince/)
* [RK4 as a fold](https://www.johndcook.com/blog/2016/06/02/ode-solver-as-a-functional-fold/)
* [Stiff differential equations](https://www.johndcook.com/blog/2020/02/02/stiff-differential-equations/)

---

## References

1. Hairer, E., Nørsett, S. P., & Wanner, G. (1987). *Solving Ordinary Differential Equations I: Nonstiff Problems*. Springer-Verlag.
2. Gill, A. (1951). A process for the step-by-step integration of differential equations in an automatic digital computing machine. *Proc. Cambridge Philos. Soc.*, vol. 27, pp. 95–108.

***

*Original post by [John D. Cook](https://www.johndcook.com/blog).*