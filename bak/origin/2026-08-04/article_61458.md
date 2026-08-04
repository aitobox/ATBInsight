# Visualizing Medical Code Hierarchy

> **Summary:** This post builds upon previous discussions of ICD-10 and HCPCS medical codes by using Python’s `squarify` library to generate treemaps. These visualizations display the distribution and hierarchical volume of codes based on their starting letters, highlighting the structural differences between the two coding systems.

---

## Overview

Following up on previous posts regarding ICD-10 and HCPCS codes, this article uses Python’s **squarify** library to create treemaps that visualize the distribution of codes beginning with each letter of the alphabet.

*Note: The sizes of the squares are directly proportional to the number of codes beginning with a given letter, though they do not necessarily reflect the frequency with which these codes are used in practice.*

---

## Visualizations

### HCPCS Codes
The HCPCS map omits the letters **R** and **U** because their volumes are extremely small relative to the rest of the dataset.

![HCPCS code treemap](http://localhost/proxy/JdFnOcKmcp6CtKZmY4D6sKPTp6FiF2JCcW58knZ6oLg=/aHR0cHM6Ly93d3cuam9obmRjb29rLmNvbS9IQ1BDU190cmVlbWFwLnBuZw==)

### ICD-10 Codes
Similarly, the ICD-10 map omits the letter **U** due to its minimal relative size.

![ICD-10 code treemap](http://localhost/proxy/ly5bNRs-Yzl89J5gUdA0JHUvg6R3TsX7on42MzsDeS8=/aHR0cHM6Ly93d3cuam9obmRjb29rLmNvbS9JQ0QxMF90cmVlbWFwLnBuZw==)

---

## Python Implementation

### 1. Generating the HCPCS Treemap

The script below utilizes `matplotlib` and `squarify` to render the HCPCS code distribution:

```python
import matplotlib.pyplot as plt
import squarify

# HCPCS Data
data = {
    "G": 2010,
    "J": 1232,
    "L": 940,
    "A": 862,
    "E": 671,
    "Q": 639,
    "C": 619,
    "S": 533,
    "M": 506,
    "V": 212,
    "K": 175,
    "T": 114,
    "H": 94,
    "P": 59,
    "B": 51,
  # "U": 5,
  # "R": 3,
}

labels = list(data.keys())
sizes = list(data.values())

# Labels are just the letters (no counts)
display_labels = labels

# Color map — one distinct color per box
colors = plt.cm.tab20.colors[: len(labels)]

fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(
    sizes=sizes,
    label=display_labels,
    color=colors,
    alpha=0.85,
    ax=ax,
    text_kwargs={"fontsize": 30, "weight": "bold"},
    pad=True,
)
ax.axis("off")

plt.tight_layout()
plt.savefig("treemap.png", dpi=72)
plt.show()
```

### 2. ICD-10 Data Set

The script for the ICD-10 treemap follows the exact same logic, differing only in the underlying dataset:

```python
# ICD-10 Data
data = {
    "S": 31052, 
    "T": 10090, 
    "M":  6665, 
    "V":  4086, 
    "H":  3330, 
    "O":  2437, 
    "Y":  1590, 
    "I":  1427, 
    "Z":  1411, 
    "W":  1290, 
    "C":  1226, 
    "L":  1000, 
    "E":   971, 
    "Q":   894, 
    "F":   871, 
    "K":   857, 
    "N":   836, 
    "D":   824, 
    "R":   773, 
    "G":   700, 
    "A":   573, 
    "X":   495, 
    "B":   495, 
    "P":   463, 
    "J":   360, 
  # "U":     3,
}
```

---

*The post [Visualizing Medical Code Hierarchy](https://www.johndcook.com/blog/2026/07/17/visualizing-medical-code-hierarchy/) first appeared on [John D. Cook](https://www.johndcook.com/blog).*