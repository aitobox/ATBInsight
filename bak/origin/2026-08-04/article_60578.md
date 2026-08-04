# Why don’t we just make the entire stack out of guard pages?

## 📌 Summary
When discussing how compilers handle stack probes, a reader posed an intriguing question: *Why not make the entire stack out of guard pages that automatically allocate memory as needed?* While it sounds like a clever way to handle stack growth, this article explains why it is a dangerous idea—primarily due to unbounded memory allocation, unresponsiveness to termination requests, and the masking of wild pointer bugs.

---

## The Origin of the Question
In a previous discussion regarding [how compilers on different architectures perform stack probes](https://devblogs.microsoft.com/oldnewthing/20260311-00/?p=112134), a reader named Cole Tobin asked: 

> *"Why not have a page fault handler that detects the faulting address being the stack and page in the other pages?"*

Another reader, Csaba Varga, offered a sharp counter-perspective:

> *"My guess: you don’t want an invalid pointer dereference to allocate a huge chunk of stack, just because the pointer happens to be pointing where the stack might grow, eventually. You want an invalid pointer dereference to segfault most of the time."*

---

## Why an All-Guard-Page Stack Fails

### 1. Unbounded Allocation Latency
If the entire stack consisted of guard pages, a single errant memory access far below the current stack limit could trigger a massive, unintended memory allocation. 

For instance, if a program's stack is configured to default to 1 GB, a stray reference could force the kernel to allocate that entire gigabyte instantly. In a debugger, this would manifest as a single memory read operation taking several minutes to complete while the system freezes to satisfy the allocation.

### 2. Unstoppable Kernel-Mode Freezes
Worse still, because this massive allocation happens entirely in kernel mode, it strips the user of control. 
* If a program begins to balloon and consume the system's entire memory, an administrator might rush to Task Manager to kill it.
* However, the process **won't die immediately**. It will remain unresponsive, continuing to consume resources as the kernel struggles to finish processing the heavy page-fault sequence.

### 3. The Value of Bounded Work
By contrast, traditional stack growth utilizes a small, fixed number of guard pages. When a guard page is hit, the system can quickly and efficiently satisfy the fault because the amount of work required is strictly **bounded**.

---

*Source: [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260713-00/?p=112528)*