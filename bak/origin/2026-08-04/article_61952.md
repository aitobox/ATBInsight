# Memory Safety's Hardest Problem

*Published: July 20, 2026*  
*(Adapted from a [Lobsters comment](https://lobste.rs/s/vzkmtj/forget_borrow_checkers_c3_solved_memory#c_uuhbpy) for easier reference.)*

---

## Summary

This article explores the fundamental challenge of memory safety: **type confusion via tagged unions**. Using a Zig code example, it demonstrates how taking a reference to a union variant, mutating the underlying data, and then accessing the stale reference can bypass type safety without relying on heap allocation or destructors. The author also discusses the practical impact of such bugs versus the ubiquitous buffer overflow, highlighting historical missed opportunities in systems programming language design.

---

## The Core Problem: Type Confusion

The central counterexample to memory safety—and arguably the hardest case to solve—has nothing to do with destructors or the heap. 

Consider this Zig program:

```zig
const std = @import("std");

const E = union(enum) {
    a: u128,
    b: []const u8,
};

pub fn main() void {
    const bad_addr: u128 = @intFromPtr(&main);

    var e: E = .{ .b = "hello" };
    const oh_no_pointer: *const []const u8 = switch (e) {
        .a => unreachable,
        .b => |*p| p,
    };
    e = .{ .a = (16 << 64) + bad_addr };
    const oh_no: []const u8 = oh_no_pointer.*;
    std.debug.print("{s}\n", .{oh_no});
}
```

Running this code yields:
```text
$ zig run main.zig
C 
```

Similar patterns are known to break other languages, such as [Ada's type safety guarantees](https://www.enyo.de/fw/notes/ada-type-safety.html).

### What is happening?
1. We have a tagged union (`E`) that can hold either variant `a` or variant `b`.
2. We initialize the union as one variant (`b`), and take a pointer directly to its internal data.
3. We overwrite the original union with the alternative variant (`a`).
4. We dereference the pointer. Even though the pointer is statically typed to point to variant `b`, the bytes it now references belong to variant `a`, resulting in **type confusion**.

---

## Theory vs. Practice

While theoretical edge cases like the above are fascinating, we ultimately care about memory unsafety because it leads to exploitable software. It remains unclear just how impactful union type confusion is in real-world exploitation. 

It is a happy coincidence that by far the most exploitable memory error in practice—the infamous buffer overflow—is also trivial to fix via compiler-inserted bounds checks. 

As [Walter Bright points out in *C's Biggest Mistake*](https://digitalmars.com/articles/C-biggest-mistake.html), the software industry's biggest miss regarding memory safety was failing to adopt native bounded arrays early on. One can easily imagine that if C11 had adopted a standard `char a[..]` syntax, an immense category of historical vulnerabilities might have been avoided entirely.

---

## Further Reading

* [What is Memory Safety?](https://matklad.github.io/2025/12/30/memory-safety-is.html)
* [Ada Type Safety Notes](https://www.enyo.de/fw/notes/ada-type-safety.html)
* [Walter Bright: C's Biggest Mistake](https://digitalmars.com/articles/C-biggest-mistake.html)