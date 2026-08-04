# Hiding Data in Permutations

## Summary
This article explores the concept of storing cryptographic keys inside a standard 52-card deck by leveraging mathematical permutations. Because $\log_2(52!) \approx 225.58$, a shuffled deck can theoretically hold up to a 225-bit key. By utilizing ranking and unranking algorithms—specifically through Python's SymPy library—we can seamlessly translate large integers into card permutations and back again, offering a fascinating intersection of combinatorics and offline cryptography.

---

## Introduction to Physical Key Storage
The [latest issue of Paged Out!](https://pagedout.institute/download/PagedOut_009.pdf) features an article by Stephen Hewitt titled *"An off-line backup of your cryptographic key using playing cards."* The core idea is to use a deck of 52 cards to store a 128-bit cryptographic key, where erasing the key is as simple as shuffling the deck. While Hewitt provides a manual, workable algorithm for embedding a key, it is not maximally efficient.

Mathematically, you could store a **225-bit key** as a permutation of 52 cards because:

$$\log_2(52!) = 225.581$$

However, this raises practical questions: How do you map a number to a specific permutation, and later decode that permutation back into a number? Is it even practical? 

For a small number $n$, you could encode a number $k < n$ by enumerating the first $k$ permutations of a set, and decode by searching for your specific permutation. For large values like $n = 52$, this brute-force approach becomes completely impractical.

---

## Ranking and Unranking Permutations
The process of mapping a permutation to an integer is called **ranking**, and the reverse mapping from an integer to a permutation is called **unranking**. 

How efficiently can these be calculated?
* **Lexicographical Order ($O(n^2)$ and $O(n \log n)$):** Simple algorithms exist for ranking and unranking with respect to lexicographical order with $O(n^2)$ complexity, alongside more sophisticated $O(n \log n)$ algorithms.
* **Non-lexicographical Order ($O(n)$):** There are also linear-time $O(n)$ algorithms that do not preserve lexicographical order.

---

## Implementation Using SymPy
The `Permutation` class in the Python library **SymPy** provides built-in methods (`unrank_lex` and `rank`) to handle lexicographical ranking and unranking.

### Understanding the Notation
Suppose we unrank the number `2026`:

```python
>>> from sympy.combinatorics import Permutation
>>> Permutation.unrank_lex(52, 2026)
Permutation(45, 47, 51, 48, 46, 50)
```

The output is represented compactly as a **cycle** rather than a full list of 52 permuted numbers. This notation means the permutation sends 45 to 47, 47 to 51, and so on, leaving all other elements fixed. 

Ranking this permutation returns the original integer:

```python
>>> Permutation.rank(Permutation(45, 47, 51, 48, 46, 50))
2026
```
*(Note: Because of lexicographical ordering, the rank remains identical whether viewed as a permutation of 52 objects or a larger set.)*

---

## Encoding a 220-Bit Number
Let's scale up to generate a 225-bit random number and encode it as a permutation of 52 items:

```python
>>> import random
>>> n = random.getrandbits(225)
>>> a = Permutation.unrank_lex(52, n)
>>> n
40234719030664563684489051530416964877785781669439875437823431388841
>>> a
Permutation(0, 25, 32, 15, 8, 28)(1, 48, 34, 14, 10, 51, 38, 31, 21, 5, 42, 47, 29, 26, 46, 30, 50, 49, 37, 22, 18, 23)(2, 45, 17, 20, 36, 40, 11, 4, 7, 41, 33, 3, 43, 44, 19, 16, 35, 39, 12, 6, 9)
>>> Permutation.rank(a) == n
True
```

---

## Visualizing the Permuted Deck
For fun, we can apply this permutation to a standard French deck of 52 cards. Using Unicode playing card symbols (as detailed in [this guide on card symbols](https://www.johndcook.com/blog/2024/04/30/a-deck-of-cards/)), we can print out the visual state of the permuted deck:

```python
spades = list(range(0x1F0A1, 0x1F0AF))
spades.remove(0x1F0AC) # take out the knight
cards = [s + 16*i for s in spades for i in range(4)]

a = Permutation.unrank_lex(52, n)
p = a(cards)

for i in range(4):
    for j in range(13):
        print(chr(p[13*i + j]), end="")
    print()
```

While the lexicographical methods shown here are plenty fast for 52 elements, SymPy also provides `rank_nonlex` and `unrank_nonlex` methods running in $O(n)$ time, which become essential when working with much larger values of $n$.

---

*Adapted from the original post [Hiding data in permutations](https://www.johndcook.com/blog/2026/07/27/hiding-data-in-permutations/) by [John D. Cook](https://www.johndcook.com/blog).*