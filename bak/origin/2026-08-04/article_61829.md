# Fitting a Regular Expression to a List of Words

## Summary
When searching for a large list of words, combining them into a single regular expression can drastically improve search efficiency. While brute-force patterns (like `word1|word2|word3`) quickly become bloated, tools like Python's `trieregex` package leverage **trie data structures** to compress lists of words into optimal regular expressions by factoring out common prefixes. This optimization allows modern search tools like `ripgrep` to outperform traditional utilities by orders of magnitude.

---

## Searching with `grep` and `ripgrep`

Suppose you want to search a document for a list of words. If you are using `grep`, you can provide a file of patterns using the `-f` flag, and specify that they are literal words using `-F`:

```bash
grep -w -F -o -f icd10codes.txt notes.txt
```

Combining a large list of words into a singular regular expression can improve efficiency. Tools like `ripgrep` (`rg`) do this automatically, though excessively large lists can hit limits (e.g., *“Compiled regex exceeds size limit of 104857600 bytes”*).

---

## Beating Brute Force with Tries

Say you want to search for the strings `"bluecross"`, `"blueshield"`, and `"bluey"`. A naive, brute-force regular expression looks like this:

```regex
bluecross|blueshield|bluey
```

This approach ignores the shared prefix `"blue"`. A much more compact regular expression factors this out:

```regex
blue(shield|cross|y)
```

While finding the absolute shortest regular expression for an arbitrary list of words is a difficult problem, finding one significantly shorter than brute force is straightforward using the Python package [trieregex](https://github.com/ermanh/trieregex). 

According to the documentation:
> `trieregex` creates efficient regular expressions (regexes) by storing a list of words in a trie structure, and translating the trie into a more compact pattern.

We can test this with our `"blue"` example:

```python
import re
from trieregex import TrieRegEx as TRE

words = ['bluecross', 'blueshield', 'bluey']
tre = TRE(*words) 
print(tre.regex())
```

This outputs a pattern identical to our hand-optimized version, with the addition of `?:` to create non-capturing parentheses:

```regex
blue(?:shield|cross|y)
```

---

## Prefixes versus Suffixes

Because `trieregex` builds its trie data structure using **common prefixes**, it works wonderfully in the example above. However, the results are less impressive when dealing with common **suffixes** rather than prefixes. 

For example, running this code:

```python
words = ['javascript', 'typescript']
tre = TRE(*words) 
print(tre.regex())
```

Produces this regular expression:

```regex
(?:javascript|typescript)
```

This is no better than brute force, whereas a suffix-aware tool might ideally produce `(?:java|type)script`.

---

## Practical Performance: HCPCS Codes Example

While `ripgrep` may fail on massive lists like ICD-10 codes, smaller lists like HCPCS codes are highly compressible. In benchmarks, searching a test file yielded a massive performance boost when utilizing optimized regex compilation:

* **`grep`** (`grep -w -F -o -f hcpcs.txt notes.txt`): **73.426 seconds**
* **`ripgrep`** (`rg -w -F -o -f hcpcs.txt notes.txt`): **0.078 seconds** (three orders of magnitude faster)

You can programmatically read and compile a list of HCPCS codes into a trie regex in Python like this:

```python
tre = TRE()
with open('hcpcs.txt', 'r') as file:
    for line in file:
        tre.add(line.strip())
print(len(tre.regex()))
```

This script generates a regular expression containing **17,198 characters**. Given that the source file contains 8,725 five-character codes, the resulting regex successfully compresses the character footprint by roughly a **5-to-2 ratio**.

---

*This content was originally published by [John D. Cook](https://www.johndcook.com/blog) in [Fitting a regular expression to a list of words](https://www.johndcook.com/blog/2026/07/19/fitting-a-regex/).*