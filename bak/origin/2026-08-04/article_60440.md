# Posterior Variance

## Summary
This article explores how additional data affects posterior variance across different Bayesian models, demonstrating that—contrary to common intuition—more data does not always reduce variance. While the normal-normal model always sees a decrease in variance, the beta-binomial model can experience increased variance from unexpected data, and the Poisson-gamma model exhibits unique cyclical behavior where variance increases upon observing events and decreases over time between events.

---

## Introduction
In a previous discussion on [whether additional data always reduces posterior variance](https://www.johndcook.com/blog/2026/07/03/does-additional-data-always-reduce-posterior-variance/), the short answer was: **not always**. 

Following that, a [subsequent post](https://www.johndcook.com/blog/2026/07/12/posterior-mean/) examined the posterior means for three Bayesian models. It demonstrated that the posterior mean is a weighted average of the prior mean and the new data's mean, where the weights are *precisions* (which have distinct definitions for each model).

---

## Behavior Across Bayesian Models

### 1. Beta-Binomial Model
* **Variance:** May increase when observing unexpected data (see details [here](https://www.johndcook.com/blog/2026/07/03/does-additional-data-always-reduce-posterior-variance/)).
* **Precision:** Always increases.

### 2. Normal-Normal Model
* **Variance & Precision:** Precision is the reciprocal of variance. Consequently, every new data point increases precision and strictly decreases posterior variance.

### 3. Poisson-Gamma Model (The Most Interesting Case)
Suppose data follows a Poisson distribution with parameter $\lambda$, and $\lambda$ has a $\text{gamma}(\alpha_0, \beta_0)$ prior distribution. After observing $k$ events over time $t$, the posterior distribution on $\lambda$ is $\text{gamma}(\alpha_0 + k, \beta_0 + t)$. 

Thus, the posterior variance is given by:

$$\frac{\alpha_0 + k}{(\beta_0 + t)^2}$$

Notice that the posterior variance is:
* An **increasing** function of $k$ 
* A **decreasing** function of $t$

This mathematical structure means the posterior variance **increases every time an event is observed**, and it **decreases quadratically between observations**.

---

## Simulation Illustration
To visualize this phenomenon, data was simulated from a Poisson process with parameter $\lambda$, using a $\text{gamma}(1, 1)$ prior on $\lambda$. 

![Posterior Variance Plot](./images/839e7db9c274.png)

***

*Source: Originally published as [Posterior variance](https://www.johndcook.com/blog/2026/07/12/posterior-variance/) on [John D. Cook](https://www.johndcook.com/blog).*