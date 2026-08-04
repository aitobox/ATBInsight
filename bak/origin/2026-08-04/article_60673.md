# Prometheus 3.14's (Likely) Duration Functions, Especially `step()`

## Summary
Prometheus is graduating [PromQL arithmetic expressions in time durations](https://prometheus.io/docs/prometheus/latest/feature_flags/#promql-arithmetic-expressions-in-time-durations) from experimental to standard. More excitingly, this update introduces powerful new duration functions—most notably [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step)—which expose the current range step directly within PromQL queries, streamlining ad-hoc analysis and query portability.

---

## Introduction to Duration Functions

An [exciting change](https://github.com/prometheus/prometheus/commit/352e36a7601cd720254d1a40d3cc07babce0cc82) recently landed in the development version of Prometheus, making [PromQL arithmetic expressions in time durations](https://prometheus.io/docs/prometheus/latest/feature_flags/#promql-arithmetic-expressions-in-time-durations) a standard feature rather than an experimental one. 

While duration arithmetic expressions are useful on their own, the real highlight is the addition of new PromQL functions, particularly [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step). 

> **Note:** Although [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) is currently gated behind the "experimental PromQL functions" feature flag, it will become standard alongside duration expressions.

## Understanding `step()` and Related Functions

If you are familiar with Grafana, [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) is effectively the PromQL equivalent of Grafana's [`$__interval`](https://grafana.com/docs/grafana/latest/visualizations/dashboards/variables/global-variables/#__interval) interpolation variable. 

During a range query, `step()` returns the size of the range step—information Prometheus has always possessed, but which was previously inaccessible within PromQL itself. Additionally, Prometheus has introduced:
* [`range()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#range): Returns the full size of the range duration.
* [`*_of()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#max_of) functions: Useful for further selection if the `step()` proves too small.

Because PromQL now supports arithmetic expressions in durations, you can use [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) directly inside them. This allows you to write queries like:
```promql
rate(your_metric[step()])
```
This expression automatically adjusts its duration to match whatever range step is currently active.

## Benefits for Ad-Hoc Querying

The [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) function is exceptionally handy for ad-hoc graphs built directly in the Prometheus web query interface (saving you from wrestling with Grafana Explore). 

Previously, you had to jump through increasingly elaborate hoops to determine the step value for a given time range before plugging it into [`rate()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate), `*_over_time()` aggregations, or similar functions. Now, you can simply ask for `rate(...[step()])`, and it will automatically adapt as you zoom the time scale in or out.

## Using `step()` with Grafana

In theory, you could replace various Grafana uses of [`$__interval`](https://grafana.com/docs/grafana/latest/visualizations/dashboards/variables/global-variables/#__interval) with [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step). In practice, this may not be worth the effort for existing dashboards unless you are specifically encountering issues with `$__interval`. 

However, it is worth considering for brand-new queries and dashboards. A minor advantage of using [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) inside Grafana is query portability: you can easily copy the query straight out of Grafana and paste it directly into Prometheus or another query tool and expect it to work identically.

## Getting Started Early

To use [`step()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#step) and its companion functions in current versions (such as Prometheus 3.13), you must enable the appropriate feature flags. Because these functions are slated for release in the next version of Prometheus, it is quite safe to enable the flags and start using them today—especially for ad-hoc exploration. Even if circumstances force you to revert later, it will significantly improve your workflow right now.

---

*(This post is an expanded version of [this Fediverse post](https://mastodon.social/@cks/116885770233705595).)*