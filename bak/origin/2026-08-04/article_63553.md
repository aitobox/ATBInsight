# Cryptographic Keys and Decks of Cards

## Summary
Building upon the concept of storing cryptographic keys within the permutations of a standard deck of cards, this article explores how larger keys—such as those used in Bitcoin, RSA, and post-quantum cryptography (ML-KEM)—demand significantly larger "decks." By calculating the mathematical capacity of permutations ($\lfloor\log_2(n!)\rfloor$), we discover how standard card games, casino equipment, or custom objects can be adapted to physically encode modern cryptographic secrets.

---

## Introduction

As explored in a [previous post](https://www.johndcook.com/blog/2026/07/27/hiding-data-in-permutations/), a cryptographic key can be stored in the specific order, or permutation, of a deck of cards. A standard deck of 52 cards can store **225 bits** of data because:

$$\lfloor\log_2(52!)\rfloor = 225$$

*(Where $\lfloor x \rfloor$ denotes $x$ rounded down to the nearest integer.)*

If we wish to store larger cryptographic keys, we will simply need a bigger deck of cards.

---

## Bitcoin

A standard Bitcoin private key consists of **256 bits**, which would traditionally require a deck of **58 cards**. 

Interestingly, a card game called *Zwicker* utilizes a 58-card deck (the standard 52 cards plus six jokers). Alternatively, one could use a standard 52-card deck plus 2 jokers by factoring in card **orientation**:
* 30 cards are rotationally symmetric.
* 22 cards are asymmetric, as are the two jokers.

By incorporating these 24 asymmetric orientation bits, a 54-card deck permutation (which encodes 237 bits) plus orientation yields a total capacity of **261 bits**.

---

## RSA

RSA key sizes vary, but **2048-bit** and **3072-bit** lengths are common:
* **2048-bit Key:** Requires a deck of **301 cards**. While casinos frequently use a "shoe" of 312 cards (combining six 52-card decks) for games like Blackjack or Baccarat, they use identical decks. To store an RSA key, one would need to combine six *unique* decks.
* **3072-bit Key:** Requires a deck of **422 cards**. This could be achieved by combining 8 distinguishable packs of 54 cards (52 standard cards + 2 jokers).

---

## ML-KEM

ML-KEM is a proposed quantum-resistant cryptographic standard designed to eventually replace RSA. Key sizes for ML-KEM are substantially larger; the smallest variant, **ML-KEM-512**, has a key size of 1,632 bytes (**13,056 bits**). 

Accommodating this key would require an unwieldy deck of **1,442 cards** (or combining 28 distinct packs of 52). 

This highlights one of the major trade-offs of post-quantum cryptography: significantly larger key sizes. To physically encode such keys, one would likely need to abandon traditional playing cards entirely in favor of alternative physical permutations.

---

## Verification

The following Python script can be used to mathematically verify the card-count calculations detailed above:

```python
from math import log2, factorial, floor

def capacity(cards):
    return floor(log2(factorial(cards)))

def verify(bits, cards):
    return capacity(cards) >= bits and capacity(cards-1) < bits

print(verify(237, 54))
print(verify(256, 58))
print(verify(2048, 301))
print(verify(3072, 422))
print(verify(1632*8, 1442))
```

For more details on how these specific deck sizes were derived, see the follow-up post on [computing the inverse factorial](https://www.johndcook.com/blog/2026/07/28/inverse-factorial-improved/).

---

*Adapted from [Cryptographic Keys and Decks of Cards](https://www.johndcook.com/blog/2026/07/28/keys-and-cards/) by [John D. Cook](https://www.johndcook.com/blog).*