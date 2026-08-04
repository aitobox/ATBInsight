# Making an agile version of a Windows Runtime delegate in C++/WinRT, Part 9

## Summary
In this final installment of the series, we evaluate whether the complex handling of non-marshalable delegates is truly necessary. By comparing how major C++ implementations—**C++/WinRT**, **C++/CX**, and **WRL**—handle agile delegates, optimizations, and non-marshalable objects, we provide a comprehensive breakdown of the design trade-offs and conclude with a feature-comparison table to help developers tailor their own agile reference implementations.

---

## Introduction

Over half of the time we spent trying to make an agile version of a Windows Runtime delegate in C++/WinRT was dealing with the case of [a delegate that declares non-marshalability](https://devblogs.microsoft.com/oldnewthing/20260729-00/?p=112570). But how much does it matter?

To find out, I looked at the three major C++ implementations of the Windows Runtime: **C++/WinRT**, **C++/CX**, and **WRL**.

## Implementation Comparisons

### 1. C++/WinRT
The C++/WinRT implementation [has an optimization for `IAgileObject`](https://github.com/microsoft/cppwinrt/blob/55f1b452aca069d6ac7eaad3e05cc1058fc39d27/strings/base_delegate.h#L88), but for objects that aren’t agile, [it just goes directly to `agile_ref`](https://github.com/microsoft/cppwinrt/blob/55f1b452aca069d6ac7eaad3e05cc1058fc39d27/strings/base_delegate.h#L95) without checking for `INoMarshal`. This means that a delegate that declares non-marshability will always be rejected by C++/WinRT when used as an event handler.

### 2. C++/CX
The C++/CX implementation [lazy-creates the agile reference to the original delegate when the wrapper is used from a different apartment](https://github.com/ojdkbuild/tools_toolchain_vs2013e/blob/a6cea36c2e52a571864986ee2957fbd91d6f4ce8/VC/include/agile.h#L207). If the original delegate is non-marshalable, it means that the `CO_E_NOT_SUPPORTED` error is produced only when the wrapper is used in a way that requires a marshalable delegate.

### 3. WRL (Windows Runtime Library)
The WRL implementation does not have an optimization for `IAgileObject`, although [it mentions it as a possible optimization](https://github.com/tpn/winsdk-10/blob/9b69fd26ac0c7d0b83d378dba01080e93349c2ed/Include/10.0.16299.0/winrt/wrl/event.h#L278). It always creates the agile reference eagerly, which means that if the original delegate is non-marshalable, it cannot be added to an agile event source.

---

## Implementation Feature Comparison

| Event source | C++/WinRT | C++/CX | WRL (Single-threaded) | WRL (Multi-threaded) | Our version |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Optimize agile delegates** | Yes | Yes | N/A | No | Yes |
| **Avoid wrapping agile delegates** | Yes | No | Never wraps | No | Yes |
| **Agile reference creation** | Eager | Lazy | Never | Eager | Eager |
| **Non-marshalable delegates** | Rejected | Allowed if used non-agile-ly | Allowed (always used non-agile-ly) | Rejected | Allowed if used non-agile-ly |

---

## Conclusion

Now, maybe you think we are working too hard. (Maybe we are.) In which case you can remove support for whatever cases you feel you don’t need.

***

*Source: [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260730-00/?p=112573)*