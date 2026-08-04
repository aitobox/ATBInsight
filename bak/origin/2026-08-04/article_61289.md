# Mermaid to ASCII Art (mermaid-ascii)

### Summary
Simon Willison has expanded his suite of diagramming tools by compiling the robust [AlexanderGrooff/mermaid-ascii](https://github.com/AlexanderGrooff/mermaid-ascii) Go library into WebAssembly. This new implementation offers a more feature-rich experience compared to previous iterations, most notably adding support for colored ASCII output.

---

### Overview
Following the development of a Mermaid-to-ASCII tool based on Rust code, a more comprehensive Go-based library was identified. By utilizing Claude Fable 5 to compile this Go library into WebAssembly, the tool now provides enhanced functionality for users looking to convert Mermaid diagrams into clean, text-based representations.

### Key Features
*   **WebAssembly Powered:** Runs directly in the browser for instant, client-side rendering.
*   **Color Support:** Unlike earlier versions, this tool preserves and renders color definitions from Mermaid syntax.
*   **Advanced Customization:** Includes adjustable padding settings (X, Y, and Box) and an "ASCII only" toggle for fine-tuning the output.
*   **User-Friendly Interface:** Features convenient "Copy as text" and "Copy link to this diagram" functionality.

### Try the Tool
You can access the live tool here: **[Mermaid to ASCII art](https://tools.simonwillison.net/mermaid-ascii)**

---

**Tags:** #go #tools #webassembly #mermaid