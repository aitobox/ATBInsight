# Runge-Kutta Order Versus Stages

## Summary
In Runge-Kutta methods for solving differential equations, the number of stages ($s$) typically matches the order of error ($p$) for lower-order versions ($p \le 4$). However, achieving an error order of $p \ge 5$ requires strictly more stages than the order itself—a limitation known as the **Butcher barrier**. 

---

## Stages

The number of stages in a Runge-Kutta (RK) method used to solve the first-order ordinary differential equation (ODE):

$$y' = f(t, y)$$

corresponds to the number of evaluations of the right-hand side function $f$. 

For example, the classic textbook RK4 method estimates the solution at each step via:

$$y_{n+1} = y_n + \frac{h}{6}\left( k_{n1} + 2k_{n2} + 2k_{n3} + k_{n4}\right)$$

where the intermediate stages are evaluated as:

$$\begin{aligned}
k_{n1} &= f(t_n, y_n) \\ 
k_{n2} &= f(t_n + 0.5h, y_n + 0.5hk_{n1}) \\ 
k_{n3} &= f(t_n + 0.5h, y_n + 0.5hk_{n2}) \\ 
k_{n4} &= f(t_n + h, y_n + hk_{n3})
\end{aligned}$$

This formulation requires four distinct stages—meaning four separate evaluations of $f$.

---

## Order

A differential equation solver is said to have **order $p$** if the local error (the error incurred after a single step of size $h$) is $\mathcal{O}(h^{p + 1})$. 

Consequently, after solving an ODE over a fixed time interval $T$ using $N = T/h$ steps, the accumulated global error is $\mathcal{O}(h^{p})$. 

* **Example:** If $p = 4$, cutting your step size $h$ in half will reduce your total global error at time $T$ by a factor of $2^4 = 16$.

---

## More Stages Than the Order: The Butcher Barrier

Mathematician John C. Butcher proved that any explicit Runge-Kutta method of order $p$ requires a number of stages $s$ such that $s > p$ whenever $p > 4$. 

### The Dormand-Prince Method
A prominent example of this principle is the **Dormand-Prince method**, which is an explicit RK method featuring order 5 and requiring 7 stages. 

A key innovation of this method is that a subset of its intermediate function evaluations can simultaneously form a valid 4th-order solver. This design offers several practical advantages:
* **"Free" error estimation:** After computing a step with the 5th-order method, the embedded 4th-order method is essentially evaluated for free.
* **Adaptive step-size control:** By comparing the differences between the 4th- and 5th-order solutions, the algorithm can dynamically adjust step sizes. If the solutions diverge significantly, the step size was likely too large and must be repeated; if they agree closely, the solver can proceed safely to the next step.

### Minimum Stages by Order
To construct an explicit RK method with a given order $p$, the minimum number of required stages ($s$) scales as follows:
* **Order 5:** At least 6 stages
* **Order 6:** At least 7 stages
* **Order 7:** At least 9 stages

---

*Adapted from the original article by [John D. Cook](https://www.johndcook.com/blog/2026/08/01/butcher-barrier/).*