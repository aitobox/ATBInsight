# Printing Floating Point Numbers in Binary

*Source: [John D. Cook](https://www.johndcook.com/blog/2026/07/27/float-binary/)*

---

## 📌 Summary
While converting hexadecimal integers to binary is a well-known trick of translating digit-by-digit, fewer people realize you can apply the same principle to floating-point numbers. By leveraging Python's built-in `.hex()` method for floats and translating each hex character into its 4-bit binary equivalent, you can easily derive the exact binary representation of any floating-point number.

---

## 🔢 From Hexadecimal to Binary

It’s well known that you can convert the base 16 (hex) representation of an integer to the base 2 (binary) representation by simply converting each digit from hex to binary. For example:

$$\text{CAFE}_{\text{hex}} = 1100\ 1010\ 1111\ 1110_{\text{two}}$$

I imagine it’s less well known that you can do the exact same thing with floating-point numbers.

---

## 🐍 Using Python to Inspect Floats

I wanted to find the binary representation of a floating-point number using Python, and discovered that while Python has no direct function to do this, it does provide a method to show a float's hexadecimal representation. 

For example, here’s the hex representation of $\pi$:

```python
>>> import math
>>> (math.pi).hex()
'0x1.921fb54442d18p+1'
```

Curiously, the `p+k` part at the end is an exponent of $2$, not an exponent of $16$. So after we convert `1.921fb54442d18` to binary, we’ll need to multiply by $2$ (i.e., move the fractional point one space to the right).

---

## 📐 Step-by-Step Conversion

### 1. Convert Hex Digits to Binary
First, we convert `1.921fb54442d18` from hex to binary by converting each digit (`1`, `9`, `2`, etc.) individually:

$$\text{1.1001}\ 0010\ 0001\ 1111\ 1011\ 0101\ 0100\ 0100\ 0100\ 0010\ 1101\ 0001\ 1000_{\text{two}}$$

### 2. Adjust for the Exponent
Next, we shift the fractional point to account for the `p+1` part, giving us the final binary representation for $\pi$:

$$\pi = 11.001001000011111101101010100010001000010110100011000_{\text{two}}$$

---

## 🛠️ Handling Padding with Other Examples

You can use Python’s `bin()` function to convert the fractional part—interpreted as an integer—to binary, though you may need to pad the result with leading `0` bits. 

For example:

```python
>>> (1.03).hex()
'0x1.07ae147ae147bp+0'

>>> bin(0x7ae147ae147)
'0b1111010111000010100011110101110000101000111'
```

The true binary representation of $1.03_{\text{ten}}$ is:

$$1.000001111010111000010100011110101110000101000111_{\text{two}}$$

*(Note: We added a total of five zero bits to align the nibbles correctly—four for the `0` immediately after the fractional point, and one for converting the leading `7` to `0111_{\text{two}}`.)*