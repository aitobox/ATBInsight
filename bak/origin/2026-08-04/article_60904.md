# Notes on the Fourier Transform

## Summary

This document explores the transition from Fourier series—which are designed for periodic functions—to the **Fourier transform**, which handles non-periodic functions defined over the entire real line $(-\infty, \infty)$. By visualizing what happens to a Fourier series as its period $L$ approaches infinity, we observe that the discrete set of harmonic frequencies transitions into a continuous spectrum. This insight leads to the mathematical derivation of the Fourier transform and its inverse. 

The text also walks through a concrete example using an odd triangular pulse, illustrates how to interpret its magnitude and phase in the frequency domain, details the existence conditions for the transform, and highlights key operational properties (such as linearity, scaling, time-shifting, differentiation, and the convolution theorem). Finally, an appendix reviews the concept of Riemann sums in relation to the definite integral.

---

## Table of Contents
1. [Visualizing Fourier Series for Non-Repeating Functions](#visualizing-fourier-series-for-non-repeating-functions)
2. [Fourier Series with $L \rightarrow \infty$ Leading to Fourier Transform](#fourier-series-with-l-%E2%80%93%3E-%infin-leading-to-fourier-transform)
3. [Example Calculation of Fourier Transform](#example-calculation-of-fourier-transform)
4. [The Frequency Domain Representation of Functions](#the-frequency-domain-representation-of-functions)
5. [Existence Condition for the Fourier Transform](#existence-condition-for-the-fourier-transform)
6. [Some Useful Properties of Fourier Transforms](#some-useful-properties-of-fourier-transforms)
7. [Appendix A: Riemann Sum and the Definite Integral](#appendix-a-riemann-sum-and-the-definite-integral)
8. [Footnotes](#footnotes)

---

## Visualizing Fourier Series for Non-Repeating Functions

The Fourier series is a great tool for analyzing periodic functions. But what about functions that don’t repeat? [We’ve seen](https://eli.thegreenplace.net/2026/notes-on-fourier-series/) that we can compute Fourier series for a non-periodic function defined on a finite interval, as long as we don’t care about its behavior beyond that interval.

Let’s extend this idea to functions that *never* repeat; that is, non-periodic functions defined on the interval $(-\infty,\infty)$.

To motivate the subject ahead, let’s look back at the example used in the earlier [post about Fourier series](https://eli.thegreenplace.net/2026/notes-on-fourier-series/):

$$t(x)=
\begin{cases}
    x     &  0 \leq x \leq 1 \\
    2-x   &  1 < x \leq 2  \\
\end{cases}$$

With an odd extension into $[-2,0]$. In that post, to make the Fourier series work, we assumed $t(x)$ keeps repeating with a period $2L=4$ on the entire $x$ axis. Here, let’s face the reality that it does not—in fact—repeat, and observe how our Fourier series work out.

Recall that the Fourier series approximating $t(x)$ are the sine series (since it’s an odd function):

$$t(x)=\frac{8}{\pi^2}\bigg[ \sin\frac{\pi x}{2}-\frac{1}{3^2} \sin\frac{3\pi x}{2}+\frac{1}{5^2}\sin\frac{5\pi x}{2}-\cdots\bigg]$$

The following visualization is interactive (conceptually):
* **Step 1:** Set $n$ (terms in the Fourier series) to some non-zero number; already at 3, the approximation is very good. The frequency spacing is $\frac{\pi}{L}$. Note that the Fourier series repeats every $2L$, as expected.
* **Step 2:** Increase $L$ to $6$. This means our series are constructed assuming $t(x)$ has a period of $12$, not $4$. Note how the Fourier series look now—they repeat every $12$, and they don’t match $t(x)$ as well as before. As $L$ grows, the spacing between adjacent frequencies decreases.
* **Step 3:** Increase $L$ to $10$. We no longer see the repetitions. Note again that we need to add more and more coefficients to match $t(x)$ better with this larger $L$, and the spacing between adjacent frequencies grows smaller.

Increasing $L$ means our function repeats at larger and larger intervals. The logical conclusion of this progression is to ask: **what happens if the function *never* repeats, meaning $L\rightarrow\infty$?** 

While not mathematically rigorous, this visual experiment lets us make some conjectures: we’ll likely need an infinite number of coefficients for a good approximation, and moreover, the spacing between these coefficients will tend to zero.

In other words, instead of a discrete set of coefficients, we’ll end up with a continuous line, or *function*. The function produced by this process is the **Fourier transform** of $t(x)$, and the next section shows its mathematical derivation.

---

## Fourier Series with $L \rightarrow \infty$ Leading to Fourier Transform

In these notes, we’ll be using the complex exponential formulation of Fourier series:

$$f(x)=\sum_{n=-\infty}^{\infty}C_n\cdot e^{in\pi x/L}$$

With:

$$C_n=\frac{1}{2L}\int_{-L}^{L}f(x)e^{-in\pi x/L}dx$$

We’re interested in a non-periodic $f(x)$ defined on the interval $(-\infty,\infty)$. So we’ll be exploring the above equations for $L\rightarrow\infty$.

First, let’s make a slight change of notation. Instead of writing formulae in terms of the period ($2L$), we’ll be using the $n$-th harmonic angular frequency $w_n$:

$$w_n=\frac{n\pi}{L}$$

So we can slightly rewrite our series as:

$$f(x)=\sum_{n=-\infty}^{\infty}C_n\cdot e^{i w_n x}=\sum_{n=-\infty}^{\infty}C_n\cdot e^{i\cdot n \Delta w x}$$

Using $\Delta w$ as the difference between two consecutive frequencies:

$$\Delta w=w_n-w_{n-1}=\frac{n\pi}{L}-\frac{(n-1)\pi}{L}=\frac{\pi}{L}$$

Using this notation, $C_n$ is expressed as:

$$C_n=\frac{\Delta w}{2\pi}\int_{-\pi/\Delta w}^{\pi/\Delta w}f(x)e^{-i\cdot n \Delta w x}dx$$

So far there are no new insights here, just some new notation to facilitate the next step. Since $L\rightarrow \infty$, then $\Delta w\rightarrow 0$. Let’s calculate the limit of the Fourier series representation of $f(x)$ when $\Delta w\rightarrow 0$:

$$f(x)=\lim_{\Delta w\rightarrow 0}\sum_{n=-\infty}^{\infty}C_n\cdot e^{i\cdot n \Delta w x}$$

Substitute $C_n$ into this equation, changing its dummy integration variable from $x$ to $t$ to avoid confusion [1]:

$$f(x)=\lim_{\Delta w\rightarrow 0}\sum_{n=-\infty}^{\infty}\left[\frac{\Delta w}{2\pi}\int_{-\pi/\Delta w}^{\pi/\Delta w}f(t)e^{-i\cdot n \Delta w t}dt\right]\cdot e^{i\cdot n \Delta w x}$$

Reordering slightly, and replacing $n\Delta w$ by $w_n$ in the complex exponents:

$$f(x)=\frac{1}{2\pi}\lim_{\Delta w\rightarrow 0}\sum_{n=-\infty}^{\infty}\left[\int_{-\pi/\Delta w}^{\pi/\Delta w}f(t)e^{-i\cdot w_n t}dt\right]\cdot e^{i\cdot w_n x}\Delta w$$

Looking at the limit with the sum carefully, this is a Riemann sum (see Appendix A)! $w_n$ is the "sampled" version of $w$, and $\Delta w\rightarrow 0$. We can therefore replace it by an integral, changing $w_n$ to $w$ and $\Delta w$ to $dw$ [2]:

$$f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\left[\int_{-\infty}^{\infty}f(t)e^{-i\cdot wt}dt\right]\cdot e^{i\cdot w x}dw$$

The inner integral is called the **Fourier transform** of $f(x)$ and denoted [3]:

$$\boxed{\hat{f}(w)=\mathcal{F}\left[f(x)\right]=\int_{-\infty}^{\infty}f(x)e^{-i\cdot wx}dx}$$

And the full equation for $f(x)$ is then the **inverse** Fourier transform:

$$\boxed{f(x)=\mathcal{F}^{-1}\left[\hat{f}(w)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)e^{i\cdot w x}dw}$$

---

## Example Calculation of Fourier Transform

Let’s take our favorite odd triangular pulse example and calculate its Fourier transform. The function’s mathematical definition was shown earlier. Note that we’re not extending this function periodically—it is zero beyond the range $[-2,2]$. This is exactly why we need the Fourier transform here: as we’ve seen, Fourier series won’t do because the function they reconstruct eventually starts repeating.

We’re looking to find:

$$\hat{t}(w)=\int_{-\infty}^{\infty}t(x)e^{-iwx}dx$$

To calculate the integral, let’s decompose the complex exponent using Euler’s formula:

$$\hat{t}(w)=\int_{-\infty}^{\infty}t(x)\cos(wx)dx-i\int_{-\infty}^{\infty}t(x)\sin(wx)dx$$

Since our $t(x)$ is odd, [the first integral is zero](https://eli.thegreenplace.net/2025/notes-on-even-and-odd-functions/). Also, $t(x)\sin(wx)$ is even, so we can write:

$$\hat{t}(w)=-2i\int_{0}^{\infty}t(x)\sin(wx)dx$$

We’ve already calculated a very similar integral in the [post on Fourier series](https://eli.thegreenplace.net/2026/notes-on-fourier-series/), so let’s skip to the result:

$$\hat{t}(w)=-2i\cdot\frac{2\cdot \sin(w)-\sin(2w)}{w^2}$$

The only remaining difficulty is its value at $0$, which seems undefined at first (division by zero). However, note that as $w\rightarrow 0$, the numerator also tends to $0$, so we can use L’Hôpital’s rule (twice!) to find that:

$$\lim_{w\rightarrow 0} \hat{t}(w)=0$$

Therefore:

$$\hat{t}(w)=
\begin{cases}
    -2i\cdot\frac{2\cdot \sin(w)-\sin(2w)}{w^2}     &  w\neq 0 \\
    0   &  w=0  \\
\end{cases}$$

This function is complex-valued; in fact, it’s purely imaginary. A common way to visualize complex-valued functions is by plotting their magnitude and phase separately.

The magnitude of $\hat{t}(w)$ is:

$$|\hat{t}(w)|=\sqrt{\hat{t}(w)\cdot\hat{t}(w)^*}=2\left|\frac{2\cdot \sin(w)-\sin(2w)}{w^2} \right|$$

Since $\hat{t}(w)$ is purely imaginary, there are only two options for the phase:
* When the numerator is positive, we get a negative imaginary number with phase $-\pi/2$.
* When the numerator is negative, we get a positive imaginary number with phase $\pi/2$. 
* When $\hat{t}(w)=0$ (which happens at $w=0$, and whenever $w$ is a whole multiple of $\pi$), the phase is undefined.

It is common to talk about $\hat{t}(w)$ as the **frequency domain** representation of $t(x)$.

---

## The Frequency Domain Representation of Functions

When the functions we’re working with have *time* as their domain (e.g., the $x$ in $t(x)$ represents time)—which is often the case in the study of signals and systems—the Fourier transform can be seen as computing the *frequency domain* representation of the function.

Here’s the Fourier transform formula again:

$$\hat{f}(w)=\mathcal{F}\left[f(x)\right]=\int_{-\infty}^{\infty}f(x)e^{-i\cdot wx}dx$$

It takes $f(x)$—the **time domain** representation of a function—and converts it to $\hat{f}(w)$—a **frequency domain** representation. For well-behaved functions, these two representations are dual; each one describes the function completely, just in a different way.

To convert back from a frequency domain representation to the time domain, we use the inverse Fourier transform:

$$\mathcal{F}^{-1}\left[\hat{f}(w)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)e^{i\cdot w x}dw$$

While a time-domain plot ($t(x)$) shows how a signal changes over time, a frequency-domain plot ($\hat{t}(w)$) shows how the signal is distributed across all possible frequencies. Moreover, $\hat{t}(w)$ is complex-valued: the magnitude tells us how strongly a frequency contributes, while the phase tells us how that component is shifted.

The frequency domain is extremely useful in signal analysis, such as when designing filters. The Fourier transform also has a number of useful properties, but first, let’s discuss what a "well-behaved function" means.

---

## Existence Condition for the Fourier Transform

The simplest existence condition for Fourier transforms is absolute integrability (also known as Lebesgue integrability):

$$\int_{-\infty}^{\infty}|f(x)|dx<\infty$$

With this condition, $\hat{f}(w)$ exists on the entire $w$ domain, is continuous, and vanishes (tends to $0$) as $|w|\rightarrow\infty$ [4].

While this condition is sufficient, it’s not necessary; there are less well-behaved functions that also have Fourier transforms defined with some limitations. In these notes, we’re mostly interested in well-behaved functions used in real-world engineering.

Another assumption commonly made for real-world functions is that they vanish as $|x|\rightarrow\infty$. While this is not a direct outcome of absolute integrability [5], it’s a reasonable assumption in engineering because real-world signals have finite energies. 

An important outcome of this discussion is that **the Fourier transform is unsuitable for periodic functions**. Functions that repeat at intervals *are not absolutely integrable*. For periodic functions, we use Fourier series.

---

## Some Useful Properties of Fourier Transforms

### 1. Linearity
The Fourier transform is a linear operator because the integral is linear:

$$\begin{aligned}
    \mathcal{F}\left[\alpha f(x)+\beta g(x)\right]&=\int_{-\infty}^{\infty}\alpha f(x)e^{-i\cdot wx}dx+\int_{-\infty}^{\infty}\beta g(x)e^{-i\cdot wx}dx\\
    &=\alpha\int_{-\infty}^{\infty}f(x)e^{-i\cdot wx}dx+\beta\int_{-\infty}^{\infty}g(x)e^{-i\cdot wx}dx\\
    &=\alpha\mathcal{F}\left[f(x)\right]+\beta\mathcal{F}\left[g(x)\right]
\end{aligned}$$

Similarly, for the inverse Fourier transform:
$$\mathcal{F}^{-1}\left[\alpha\hat{f}(w)+\beta\hat{g}(w)\right]=
\alpha\mathcal{F}^{-1}\left[\hat{f}(w)\right]+\beta\mathcal{F}^{-1}\left[\hat{g}(w)\right]$$

### 2. Scaling
If we scale the domain of a function by a constant, its transform changes according to:

$$\mathcal{F}\left[f(ax)\right]=\frac{1}{|a|}\hat{f}\left(\frac{w}{a}\right) \quad (\text{for } a \neq 0)$$

Intuitively, if $a > 0$, $f(ax)$ means the signal is *compressed* in the time domain by a factor of $a$. The scaling property says that the frequency domain is *expanded* by the same factor.

### 3. Time Shifting
What happens if we time-shift the input signal by some constant $x_0$?

$$\mathcal{F}\left[f(x-x_0)\right]=e^{-iwx_0}\mathcal{F}\left[f(x)\right]$$

### 4. Transform of a Derivative
An extremely useful property employed in solving differential equations:

$$\mathcal{F}\left[f'(x)\right]=iw\cdot\mathcal{F}\left[f(x)\right]$$

*(Derived using integration by parts, assuming $f(x)$ vanishes at infinity).*

### 5. Transform of Convolution (The Convolution Theorem)
The convolution between two continuous functions $f(x)$ and $g(x)$ is defined as:

$$(f\ast g)(x)=\int_{-\infty}^{\infty}f(\xi)g(x-\xi)d\xi$$

Applying the Fourier transform and using Fubini's theorem to switch integration orders yields:

$$\mathcal{F}\left[(f\ast g)(x)\right]=\mathcal{F}\left[f\right]\cdot\mathcal{F}\left[g\right]$$

**Convolution in the time domain translates to multiplication in the frequency domain!**

---

## Appendix A: Riemann Sum and the Definite Integral

Suppose we want to know the area bounded between a function $f(x)$ and the $x$-axis in an interval $[a,b]$. We take a partition of the interval:

$$a=x_0<x_1<\cdots<x_{n-1}<x_n=b$$

We approximate sub-areas by rectangles where the area of each rectangle is $f(x^*_i)\cdot\Delta x$:
* $\Delta x = (b-a)/n$ is the width of one interval.
* $x^*_i$ is some value in the interval $[x_{i-1},x_i]$.

We approximate the area with a **Riemann sum**:

$$S=\sum_{i=1}^{n}f(x^*_i)\Delta x$$

If $f$ is continuous on $[a,b]$, then as $n\rightarrow \infty$:

$$S=\lim_{n\rightarrow \infty}\sum_{i=1}^{n}f(x^*_i)\Delta x=\int_{a}^{b}f(x)dx$$

This is known as the **Riemann integral**, or definite integral.

---

## Footnotes

* <a id="footnote-1" href="#footnote-reference-1">[1]</a> $C_n$ is not a function of $x$; in its definition, $x$ only serves as a dummy integration variable. When we substitute $C_n$ into the equation for $f(x)$, we must rename it to avoid variable clashes.
* <a id="footnote-2" href="#footnote-reference-2">[2]</a> Because we apply the limit, the bounds of the inner integral in square brackets become $-\infty$ to $\infty$.
* <a id="footnote-3" href="#footnote-reference-3">[3]</a> The dummy variable is changed back to $x$ for consistency. The final result is a function of $w$, not $x$.
* <a id="footnote-4" href="#footnote-reference-4">[4]</a> This vanishing behavior is known as the **Riemann-Lebesgue lemma**.
* <a id="footnote-5" href="#footnote-reference-5">[5]</a> A pathological absolutely-integrable function can have arbitrary spikes at infinity while maintaining a finite total area.