# Inverse Factorial Improved

> **Summary:** John D. Cook revisits his previous work on computing the inverse factorial—specifically required for solving bit-length inequalities like $\lfloor\log_2(n!)\rfloor \ge b$. He outlines key improvements to his original implementation, including abandoning rounding within the function, replacing the bisection method with the globally convergent Newton's method (enabled by the convexity of $\log \Gamma$), and exposing the tolerance parameter.

---

[A couple years ago](https://www.johndcook.com/blog/2024/01/01/inverse-factorial/), I wrote about how to compute the inverse of factorial. I used that code in writing the previous post because the post required solving the equation:

$$\lfloor\log_2(n!)\rfloor \ge b$$

given $b$. That is, given a number of bits $b$, find the smallest value of $n$ such that $n! \ge 2^b$.

## What the Code Got Right

Looking back on the code in that post, there are a few changes I’d like to make. But first of all, I’d like to point out something the post does right: instead of trying to solve:

$$\Gamma(y) = x$$

it solves:

$$\log \Gamma(y) = \log x$$

That’s why the argument to `inverse_log_gamma` is `logarg`. That makes the code useful for values of $x$ that would far exceed the maximum floating point value, such as in the calculations for the previous post.

## What I’d Change

### 1. Rounding

The function `inverse_factorial` from the old post finds the closest integer solution. It would be better for it to return the solution without rounding and then let the user round the result if they want to. In my calculations in the previous post, I wanted to take the floor, not round.

### 2. Newton’s Method

The code in the previous post uses the bisection method. This method is very safe, and fast enough for my purposes, but it could be made faster. Newton’s method is faster, but it can be ill-behaved if you don’t start close enough to the solution.

It’s safe to use Newton’s method to invert $\log \Gamma$ for two reasons. 
* First, you can get a good starting point based on Stirling’s approximation. 
* Second, and more importantly, $\log \Gamma$ is convex. Newton’s method will converge from *any* starting point when applied to a convex function. A little caution is necessary because $\log \Gamma$ is not convex everywhere, but it is convex on the positive real axis.

Another difficulty with Newton’s method is that you need to supply the derivative of the function whose root you’re trying to find. But this isn’t an issue here because the derivative of $\log \Gamma$ is the digamma function, which is implemented in SciPy.

### 3. Tolerance

Finally, the previous code used the default tolerance for deciding when to stop refining the solution. The revised method lets the user specify tolerance. It provides a default value, but that default is visible in the function call, not hidden down in SciPy.

---

## Revised Code

Here is the revised implementation:

```python
from scipy.special import gammaln, digamma
from scipy.optimize import newton

def inverse_log_gamma(logarg, tol=1e-12):
    assert(logarg > 0)    
    x0 = logarg / log(logarg + 1) + 1 if logarg > 1 else 2.0
    def f(z): return gammaln(z) - logarg
    return newton(f, x0, fprime=digamma, tol=tol)

def inverse_factorial(logarg):
    g = inverse_log_gamma(logarg)
    return g - 1 
```

***

*This post, [Inverse factorial improved](https://www.johndcook.com/blog/2026/07/28/inverse-factorial-improved/), originally appeared on [John D. Cook](https://www.johndcook.com/blog).*