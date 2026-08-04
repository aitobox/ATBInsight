# Posterior Mean

### Summary
Bayesian statistics provides a rigorous, quantitative framework for updating beliefs when new data arrives. At its core, the "posterior mean"—the updated estimate of a parameter—is consistently a weighted average of your prior beliefs and the new evidence. While the definition of "precision" (the weight assigned to each source of information) changes depending on the model, the underlying logic remains a balanced compromise between prior knowledge and observed data.

---

## The Bayesian Framework
Common sense dictates that your updated beliefs should be a compromise between previous information and new data. Bayesian models formalize this intuition. By combining a **prior distribution** (your initial belief) with a **likelihood model** (the process generating the data), you can "turn the Bayesian crank" to objectively derive a **posterior distribution**.

---

## 1. Normal-Normal Model
When data $X$ follows a normal distribution with unknown mean $\mu$ and known variance $\sigma^2$, and the prior on $\mu$ is also normal with mean $\mu_0$ and variance $\sigma_0^2$, the posterior mean is:

$$\mu_{\text{post}} = \frac{\frac{\mu_0}{\sigma_0^2} + \frac{x}{\sigma^2}}{\frac{1}{\sigma_0^2} + \frac{1}{\sigma^2}}$$

By defining precision as $\tau = 1/\sigma^2$ and $\tau_0 = 1/\sigma_0^2$, this simplifies to:

$$\mu_{\text{post}} = \frac{\mu_0 \cdot \tau_0 + x \cdot \tau}{\tau_0 + \tau}$$

Here, the posterior mean is a weighted average where the weights are the **precisions** of the prior and the data.

---

## 2. Beta-Binomial Model
For a binary random variable with success probability $p$ and a Beta($a, b$) prior, observing $s$ successes and $f$ failures results in a posterior mean of:

$$p_{\text{post}} = \frac{a + s}{a + b + s + f}$$

Rewritten as a weighted average:

$$p_{\text{post}} = \frac{(a + b) \frac{a}{a+b} + (s + f) \frac{s}{s+f}}{(a + b) + (s + f)}$$

In this model, the "precision" is the **effective sample size** ($a+b$ for the prior and $s+f$ for the data).

---

## 3. Gamma-Poisson Model
If data follows a Poisson distribution with parameter $\lambda$, and $\lambda$ has a Gamma($\alpha_0, \beta_0$) prior, observing $k$ events over time $t$ yields a posterior mean of:

$$\lambda_{\text{post}} = \frac{\alpha_0 + k}{\beta_0 + t} = \frac{\beta_0 (\alpha_0 / \beta_0) + t (k / t)}{\beta_0 + t}$$

Here, the "precision" is represented by **time**. The parameter $\beta_0$ acts as an effective time, balancing the prior mean against the observed rate ($k/t$).

---

## The Common Thread
Across these examples, the posterior mean is always a weighted average of the prior mean and the data mean. The "weight" assigned to each is a measure of confidence:
* **Normal-Normal:** Precision (reciprocal of variance).
* **Beta-Binomial:** Effective sample size.
* **Gamma-Poisson:** Time.

These models are all **conjugate models** from the exponential family. In technical terms, the precision acts as the multiplicative factor on the sufficient statistic within the exponent of the posterior kernel.

---

### Further Reading
* [Does additional data always reduce posterior variance?](https://www.johndcook.com/blog/2026/07/03/does-additional-data-always-reduce-posterior-variance/)
* [Diagram of probability distribution relationships](https://www.johndcook.com/blog/distribution_chart/)
* [Bayesian statistics consulting](https://www.johndcook.com/blog/bayesian-consulting/)

***

*Note: This content is based on the post [Posterior mean](https://www.johndcook.com/blog/2026/07/12/posterior-mean/) by John D. Cook.*