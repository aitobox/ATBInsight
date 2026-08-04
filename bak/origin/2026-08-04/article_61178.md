# Speculating on Pointer Truncation in Control Panel Extensions

### Summary
This article explores a common pitfall during the migration of legacy 32-bit Windows code to 64-bit architectures. It examines how a developer, while updating window procedure handles, likely fell victim to "partial refactoring"—fixing compiler errors by renaming constants without addressing the underlying pointer truncation caused by incorrect type casting.

---

### The Anatomy of the Bug
In a previous investigation, we identified a crash in a control panel extension caused by pointer truncation. Despite having a valid 64-bit pointer, the application discarded the top 32 bits, leading to an invalid memory access.

The root cause likely stems from a transition from 32-bit to 64-bit code.

#### 1. The Legacy 32-bit Code
Originally, the code functioned perfectly in a 32-bit environment:
```cpp
HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
SetWindowLong(hwndButton, GWL_WNDPROC, (LONG)g_originalWndProc);
```

#### 2. The Migration Error
When recompiling for 64-bit, the compiler flags `GWL_WNDPROC` as an undeclared identifier. The developer, following documentation, updates the constant to the 64-bit equivalent, `GWLP_WNDPROC`. However, they fail to update the cast:
```cpp
// The developer fixed the constant but left the (LONG) cast
SetWindowLong(hwndButton, GWLP_WNDPROC, (LONG)g_originalWndProc);
```

#### 3. The Required Fix
The renaming of these constants was intended to act as a "warning sign" for developers. To support 64-bit pointers, the cast must also be updated to `LONG_PTR`:
```cpp
SetWindowLong(hwndButton, GWLP_WNDPROC, (LONG_PTR)g_originalWndProc);
```

### Why Did This Happen?
It appears this was an isolated oversight rather than a systemic failure. The developer successfully implemented the window subclassing elsewhere in the code:

```cpp
WNDPROC g_originalWndProc;

HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
g_originalWndProc = (WNDPROC)SetWindowLong(hwndButton, GWLP_WNDPROC,
    (LONG_PTR)subclassWndProc);
```

It is highly probable that the developer addressed the compiler error by renaming the constant, got distracted, and neglected to update the associated type cast, leaving the application vulnerable to truncation.

***

*Next time: We will explore why this specific bug has persisted in the codebase for so long.*

*Source: [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260716-00/?p=112539)*