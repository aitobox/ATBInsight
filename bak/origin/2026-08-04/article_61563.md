# Regressive JPEGs: Exploiting Progressive Rendering

### Summary
JPEG files support a "progressive" mode that allows images to load in stages, starting with low-frequency data. By manipulating the "scans" within these files, one can force a browser to render a sequence of different images as the file downloads. This technique effectively turns a static image into a network-dependent animation, though it remains a creative hack rather than a practical format.

---

### Understanding Progressive JPEGs
Progressive JPEGs break compressed data into multiple "scans," each prefixed by a header. A typical scan header looks like this:

```text
FF DA - "start of scan" marker
00 0C - Big endian length field (12 bytes)
03    - Number of channels in scan (3)
  01  - Global id of first included channel
  00  - Huffman table index #1 (DC: 0, AC: 0)
  02  - Global id of second included channel
  10  - Huffman table index #2 (DC: 1, AC: 0)
  03  - Global id of third included channel
  10  - Huffman table index #2 (DC: 0, AC: 0)
00    - Starting DCT bin (DC)
00    - Ending DCT bin (also DC)
01    - Precision: half, no pre-existing data.
```

The file uses **YCbCr** color space. Because the human eye is less sensitive to color than luminance (Y), the chrominance channels (Cb, Cr) are often saved at lower resolutions, allowing them to be processed more efficiently.

### The Anatomy of a Load
A standard progressive JPEG fills in detail over several scans:

| Scan # | Channels | DCT Bin Range | Precision |
| :--- | :--- | :--- | :--- |
| 0 | Y Cb Cr | 0 - 0 | Half |
| 1 | Y | 1 - 5 | Quarter |
| 2-3 | Cb, Cr | 1 - 63 | Half |
| 4-5 | Y | 6 - 63 | Half/Quarter |
| 6-9 | Y Cr Cb | 0 - 63 | Full |

### Hacking the Sequence
Because each scan explicitly defines its spectral range, it is possible to construct a file where subsequent scans overwrite previous image data. By concatenating multiple images (stripping out redundant headers), you can create a file that "morphs" or switches images as it downloads.

#### The "Video" Limitation
Most decoders limit the number of scans to prevent "zip bomb" style attacks. To bypass this and create longer animations, one must minimize the data per frame. 

By using **DC-only scans** (which render at 1/16th resolution), you can fit significantly more frames into a single file before the browser gives up. Using `jpegtran`, you can generate these compliant frames:

```bash
cat > frame.scans <<EOF
# DC only scan:
0,1,2:0-0,0,0;
EOF
jpegtran -scans frame.scans -outfile out.jpg in.jpg
```

### Practicality and Fun
While this technique is essentially a "troll" format—as playback speed is entirely dependent on network latency—it demonstrates the flexibility of the JPEG specification. 

*   **View the Cat Animation:** [Click here to see the cat walk.](https://maurycyz.com/projects/bad_jpeg/cat.jpg)
*   **Related Projects:**
    *   [Merge.c Source Code](https://maurycyz.com/projects/bad_jpeg/merge.c)
    *   [Bad Apple via Partial Rendering](http://badapple.rose.systems/)