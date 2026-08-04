# Forensic Accounting in Python

## Summary
When reverse-engineering data analyses, you often encounter situations where variables have ambiguous values, but their total sum is known. By leveraging Python's `itertools.product`, you can systematically evaluate all possible combinations to identify the correct inputs, check for data integrity, or detect violated assumptions.

---

## Introduction
I recently worked on a project that required reverse-engineering a data analysis. There was some ambiguity regarding which of several possibilities someone had chosen for multiple variables—a scenario analogous to the following example.

Suppose you have three numbers with uncertain values, along with a known (or purported) sum:
* **First number possibilities:** 31, 41, or 59
* **Second number possibilities:** 26 or 53
* **Third number possibilities:** 58, 97, 93, or 23

## The Python Solution
We can use Python's `itertools.product` to enumerate all $3 \times 2 \times 4 = 24$ possible combinations and calculate their sums:

```python
from itertools import product

# Example input representing the uncertain variables
possibilities = [(31, 41, 59), (26, 53), (58, 97, 93, 23)]

for combo in product(*possibilities):
    total = sum(combo)
    print(f"Combination {combo} sums to: {total}")
```

In this particular example, all resulting sums happen to be unique—though that may not always be the case in real-world data. 

### Applying the Results
* If you know the target sum is **187**, you can uniquely determine that the three numbers must have been **41, 53, and 93**.
* If the reported sum is **200**, you immediately know that some underlying assumption has been violated, because none of the valid combinations add up to 200.

---

## More Forensics Posts
* [Make up your own rules of probability](https://www.johndcook.com/blog/2009/09/18/make-up-your-own-rules-of-probability/)
* [Identifiable to man or machine?](https://www.johndcook.com/blog/2023/04/01/identifiable-to-man-or-machine/)
* [Metadata in photos](https://www.johndcook.com/blog/2024/02/13/photo-metadata/)
* [Changing one character in a PDF](https://www.johndcook.com/blog/2026/05/05/changing-one-character-in-a-pdf/)
* [Bits of information in age or birthday](https://www.johndcook.com/blog/2018/03/02/bits-of-information-in-age-birthday-and-birthdate/)

***

*This post, [Forensic accounting in Python](https://www.johndcook.com/blog/2026/07/21/forensic-accounting-in-python/), originally appeared on [John D. Cook](https://www.johndcook.com/blog).*