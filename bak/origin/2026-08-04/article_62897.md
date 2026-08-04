# Excel Column Numbering

> **Summary:** Excel uses a unique column-labeling system (A–Z, AA–AZ, etc.) that does not rely on a standard base-26 positional numbering system because it lacks a zero. Instead, it uses **bijective base 26**. This article explores the mathematics behind this system, provides Python code to convert between column labels and numbers, and examines historical Excel column limits.

---

## The Mathematics of Column Labels

Working with wide spreadsheets often requires converting between Excel column labels and their numeric equivalents. At first glance, Excel's labeling system—A through Z, followed by AA through AZ, BA through BZ, and so on—might look like a standard base-26 numbering system using letters instead of digits. However, a closer look reveals that standard positional notation doesn't quite fit:

* If **A** corresponds to `0`, what happens at **AA**? The first **A** would represent `26`, while the second would represent `0`.
* If **Z** corresponds to `0`, the sequence would jump strangely from 25 to 0 to 27, and columns like **ZA** through **ZZ** would become identical to **A** through **Z**.

Ultimately, **no element in Excel column labeling corresponds to 0**. Consequently, these labels cannot be interpreted as a traditional positional number system.

### Bijective Base 26

This specific type of number system is known as **bijective base 26** (or more generally, bijective base $b$ for any positive integer $b$). While the concept itself is ancient, the terminology was coined relatively recently (also referred to as *k*-adic numbering). 

The defining feature of a bijective base $b$ system is that there is a **bijection** (a strict one-to-one correspondence) between the symbols and the positive integers. Unlike standard numbers where leading zeros create multiple representations for the same value (e.g., `7` vs. `07`), bijective numbering ensures every positive integer has one—and only one—unique representation.

---

## Excel Limits

Excel's maximum column capacity has expanded over the years:

* **Pre-2007:** Excel files were limited to $2^8 = 256$ columns, making the largest column label **IV**.
* **Excel 2007 and later:** The column limit was increased to $2^{14} = 16,384$ columns, making the largest column label **XFD**.

---

## Conversion Code

Converting from column labels to integers is straightforward, while the reverse requires a slightly different approach. 

Here is the Python implementation:

```python
letter_to_ordinal = lambda c: ord(c) - ord('A') + 1
ordinal_to_letter = lambda n: chr(ord('A') + n - 1)

def label_to_num(label):
    label = label.upper()
    n = 0
    for c in label:
        n = n * 26 + letter_to_ordinal(c)
    return n

def num_to_label(n):
    letters = []
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        letters.append(ordinal_to_letter(remainder + 1))
    return ''.join(reversed(letters))
```

> 🛠️ You can also test these calculations using this interactive [Online Calculator](https://www.johndcook.com/excel_labels.html).

---

## Testing and Edge Cases

The following tests verify the historical Excel column limits mentioned above:

```python
assert num_to_label(256) == "IV"
assert label_to_num("IV") == 256

assert num_to_label(2**14) == "XFD"
assert label_to_num("XFD") == 2**14
```

These conversion routines are not restricted to typical spreadsheet dimensions; they scale seamlessly to arbitrarily large integers. For instance, we can calculate the bijective base-26 representation for Avogadro's number ($6.02214076 \times 10^{23}$):

```python
avogadro = 602_214_076_000_000_000_000_000
assert label_to_num(num_to_label(avogadro)) == avogadro
print(num_to_label(avogadro))  # Output: MUAEKAUDYDXEWOSDD
```

---

## Related Posts

* [Radix conversion calculator](https://www.johndcook.com/radix_conversion.html)
* [When is floating point radix conversion exact?](https://www.johndcook.com/blog/2020/03/16/round-trip-radix-conversion/)
* [Excel, R, and Unicode](https://www.johndcook.com/blog/2019/09/07/excel-r-bom/)

***

*Source: Originally published by [John D. Cook](https://www.johndcook.com/blog) in [Excel column numbering](https://www.johndcook.com/blog/2026/07/25/excel-column-numbering/).*