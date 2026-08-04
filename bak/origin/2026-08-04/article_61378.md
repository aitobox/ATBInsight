# Regular Expression Speed and Error Rates

> **Summary:** Revisiting a [previous analysis on ICD-10 diagnosis code matching](https://www.johndcook.com/blog/2019/05/05/regex_icd_codes/), this article examines the trade-offs between using regular expressions versus exhaustive list lookups. While regular expressions introduce potential false positives and negatives, they can be orders of magnitude faster and surprisingly more future-proof than strict database lookups.

---

Regular expressions usually do not exactly match *only* what you are looking for. They inherently carry risks of false positives and false negatives. However, they also offer significant advantages, and context ultimately determines whether these error rates are tolerable.

In a [previous post](https://www.johndcook.com/blog/2019/05/05/regex_icd_codes/), the following regular expression was suggested for matching ICD-10 diagnosis codes:

```regex
[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}
```

Though cryptic at first glance, it is straightforward to interpret. An ICD-10 code:
1. Begins with a capital letter, excluding `U`
2. Is followed by a digit
3. Is followed by a digit, `A`, or `B`
4. Is optionally followed by a period (`.`)
5. Is followed by up to 4 digits or capital letters (excluding `U`)

---

## Speed

Suppose you want to scan a text document for ICD-10 codes. One approach is to use the regular expression above. Another is to compare every alphanumeric sequence in the document against an exhaustive list of valid ICD-10 codes (which currently contains 74,719 codes).

Testing both approaches on an 800 KB text file yielded dramatic differences:

* **Regular Expression Search:**
  ```bash
  egrep -o '[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}' notes.txt
  ```
  *Time taken:* **18 milliseconds**

* **Exhaustive List Search:**
  ```bash
  grep -w -F -o -f icd10codes.txt notes.txt
  ```
  *Time taken:* **386 seconds** (roughly 6.5 minutes, or five orders of magnitude slower)

---

## Error Rates

### False Negatives
When originally written, the regex had a false negative rate of zero. Testing the regex against the current list of codes using:

```bash
egrep -v '[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}' icd10codes.txt
```
*(The `-v` flag reverses the search, reporting lines that **do not** match.)*

This returned three matches: **U070**, **U071**, and **U099**. Thus, only 3 out of 74,719 valid ICD-10 codes were reported as invalid. 

While codes beginning with `U` are typically reserved for provisional, emergency, or special purposes, these three have become essentially permanent. A change in the application of the ICD-10 standard introduced this discrepancy. 

Interestingly, an exhaustive list search from the past would *also* have failed on these newer codes, as would any new code not starting with `U`. In this sense, the regex is actually **more future-proof** than an exhaustive list. Presumably, a generalized regex like:

```regex
[A-Z][0-9][0-9AB]\.?[0-9A-Z]{0,4}
```

will remain valid for the foreseeable future.

### False Positives
What about false positives? That depends heavily on context. 

When searching medical notes, the false positive rate is very low: a word matching the regex in a medical record is almost certainly an ICD-10 code. However, the theoretical number of conceivable false positives is enormous. Searching a file of randomly generated alphanumeric text would yield overwhelmingly false positives [1].

The number of strings matching the generalized pattern:
```regex
[A-Z][0-9][0-9AB]\.?[0-9A-Z]{0,4}
```
is calculated as:

$$\text{26} \times \text{10} \times \text{12} \times \left(1 + 36 + 36^2 + 36^3 + 36^4\right) = 5,390,127,600$$

Out of over **5 billion** matching strings, only about 75,000 are valid ICD-10 codes. A naive theoretical calculation suggests a false positive rate of **99.9986%**. In practice, however, the real-world false positive rate is remarkably low, even if it cannot be precisely quantified *a priori*.

---

## Related Posts

* [HCPCS (“hick pics”) codes](https://www.johndcook.com/blog/2022/09/23/hcpcs-codes/)
* [NPI numbers and checksum](https://www.johndcook.com/blog/2024/06/26/npi-number/)
* [HIPAA expert determination](https://www.johndcook.com/blog/expert-hipaa-deidentification/)

---

*[1] In a stream of pure noise, you could argue that all positives are false positives because you aren't actually finding an ICD code—merely a string of characters that coincidentally matches the pattern. While pedantic, this distinction matters significantly in deidentification quality evaluations, where the goal is to locate actual Protected Health Information (PHI) rather than random character matches.*

***

*Based on an original post by [John D. Cook](https://www.johndcook.com/blog/2026/07/17/regex-speed-error/).*