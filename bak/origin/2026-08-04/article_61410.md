# Regular Expressions for HCPCS Codes

## 📌 Summary
This article explores how to use Regular Expressions (regex) to efficiently identify Healthcare Common Procedure Coding System (HCPCS) codes and their modifiers. While exhaustive database lookups offer high precision, regex provides a lightning-fast alternative (taking milliseconds instead of seconds) for preliminary text processing and pattern matching.

---

## 🏥 Understanding HCPCS Codes

HCPCS (pronounced “hick picks”) stands for Healthcare Common Procedure Coding System. In everyday medical billing and coding context—and for the purposes of this discussion—"HCPCS" refers specifically to **HCPCS Level II**.

### Basic Code Format
The standard format for a HCPCS code is straightforward: **one letter followed by four digits**. 

* **Basic Regex:**
  ```regex
  [A-Z]\d{4}
  ```

* **Strict Regex (Excluding Unused Letters):**
  Not all alphabet letters are utilized in the coding system. A more precise pattern accounts for this:
  ```regex
  [A-CEGHJ-MP-V][0-9]\d{4}
  ```
  *(Note: While some older sources claim codes never begin with "U", there are currently a small number of active codes that do.)*

---

## ➕ Handling HCPCS Modifiers

HCPCS codes can also include **modifiers**, which provide additional information about the service or procedure. 

### Modifier Format
Modifiers consist of **two characters**: a letter followed by either a letter or a digit.
```regex
[A-Z][A-Z0-9]
```
*(Note: Certain letters like I, O, W, and Y are intentionally excluded from official modifiers to avoid confusion with numbers. There are 384 official modifiers in total.)*

### Combined Codes and Modifiers
In unstructured text, modifiers are typically appended to the base HCPCS code using a hyphen. To capture both base codes and optional modifiers in a single expression, use:

```regex
[A-CEGHJ-MP-V][0-9]\d{4}(-[A-Z][A-Z0-9])?
```

This pattern is designed to eliminate **false negatives**—meaning every legitimate HCPCS code will successfully match—though it may occasionally yield false positives.

---

## ⚡ Regex vs. Exhaustive Database Search

While you can query a complete, official list of HCPCS codes for 100% accuracy, it comes with significant performance trade-offs:

* **Regex Search:** ~20 milliseconds *(includes optional modifier handling)*
* **Exhaustive List Search:** ~46 seconds *(limited to unmodified codes)*

Maintaining an exhaustive list that accounts for every valid code-and-modifier combination is often impractical, as many combinations are medically invalid or simply never used in practice. 

---

*Source: Adapted from [John D. Cook's Blog](https://www.johndcook.com/blog).*