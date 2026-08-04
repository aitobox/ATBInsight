# Making an agile version of a Windows Runtime delegate in C++/WinRT (Part 8)

## Summary
In this installment, we address a subtle yet critical exception safety bug involving lambda capture evaluation order in C++. Even after precreating our custom deleter, an exception thrown during `get_context_token()` before the raw pointer is secured in a `std::unique_ptr` can still result in a reference leak. We explore multiple ways to resolve this ordering issue, including using an intermediate `unique_ptr`, leveraging copy elision via a helper lambda, and simply generating the token early.

---

## The Problem: Unspecified Lambda Capture Order

Previously, we fixed potential reference leaks caused by exceptions thrown during the custom deleter's constructor by precreating the deleter:

```cpp
if (d.try_as<::INoMarshal>()) {
    in_context_deleter del;
    void* p;
    if constexpr (std::is_reference_v<Delegate>) {
        p = winrt::detach_abi(d);
    } else {
        winrt::copy_to_abi(d, p);
    }
    return
        [p = std::unique_ptr<void, in_context_deleter>(p, std::move(del)),
        token = get_context_token()](auto&&...args) {
            if (token == get_context_token()) {
                std::remove_reference_t<Delegate> d;
                winrt::copy_from_abi(d, p.get());
                d(std::forward<decltype(args)>(args)...);
            } else {
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
            }
        };
}
```

However, **the order of construction of lambda captures in C++ is unspecified.** 

According to the C++ Standard ([expr.prim.lambda.capture]):
> *For each entity captured by copy, an unnamed non-static data member is declared in the closure type. The declaration order of these members is unspecified.*

Because the initialization order matches the declaration order, it is entirely possible for `get_context_token()` to execute *before* the `std::unique_ptr` is constructed. If `get_context_token()` throws an exception, the raw pointer `p` (and its associated reference) is leaked because it hasn't yet been safely handed over to the `std::unique_ptr`.

---

## Solution 1: Precreating the `std::unique_ptr`

To close this gap, we can instantiate the `std::unique_ptr` before we ever create the lambda:

```cpp
if (d.try_as<::INoMarshal>()) {
    in_context_deleter del;
    void* p;
    if constexpr (std::is_reference_v<Delegate>) {
        p = winrt::detach_abi(d);
    } else {
        winrt::copy_to_abi(d, p);
    }
    std::unique_ptr<void, in_context_deleter> up(p, std::move(del));
    return
        [p = std::move(up),
        token = get_context_token()](auto&&...args) {
            if (token == get_context_token()) {
                std::remove_reference_t<Delegate> d;
                winrt::copy_from_abi(d, p.get());
                d(std::forward<decltype(args)>(args)...);
            } else {
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
            }
        };
}
```

---

## Solution 2: Avoiding Temporary Overhead via Copy Elision

While Solution 1 works, introducing a temporary `std::unique_ptr` adds slight destructor overhead (checking for null when it is almost never null). We can avoid this by using copy elision directly into the lambda capture using a helper lambda:

```cpp
if (d.try_as<::INoMarshal>()) {
    auto make = [](auto&& d) {
        in_context_deleter del;
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return std::unique_ptr<void,                      
                   in_context_deleter>(p, std::move(del));
    };                                                    
    return
        [p = make(std::forward<Delegate>(d)),
        token = get_context_token()](auto&&...args) {
            if (token == get_context_token()) {
                std::remove_reference_t<Delegate> d;
                winrt::copy_from_abi(d, p.get());
                d(std::forward<decltype(args)>(args)...);
            } else {
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
            }
        };
}
```
*(For more background on this pattern, see [How do I put a non-copyable, non-movable, non-constructible object into a std::optional?](https://devblogs.microsoft.com/oldnewthing/20241115-00/?p=110527))*

---

## Solution 3: Creating the Token Early

Alternatively, an even simpler approach is to create the token early—just like we did with the deleter:

```cpp
if (d.try_as<::INoMarshal>()) {
    in_context_deleter del;
    auto token = get_context_token();
    void* p;
    if constexpr (std::is_reference_v<Delegate>) {
        p = winrt::detach_abi(d);
    } else {
        winrt::copy_to_abi(d, p);
    }
    return
        [p = std::unique_ptr<void, in_context_deleter>(p, std::move(del)),
         token](auto&&...args) {
            if (token == get_context_token()) {
                std::remove_reference_t<Delegate> d;
                winrt::copy_from_abi(d, p.get());
                d(std::forward<decltype(args)>(args)...);
            } else {
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
            }
        };
}
```

---

## Conclusion

Are we finally done? 

*Maybe.* 

Or perhaps all of this extra engineering wasn't actually worth it in the end. We will discuss that next time!

---
*Reference: [The Old New Thing — Making an agile version of a Windows Runtime delegate in C++/WinRT, part 8](https://devblogs.microsoft.com/oldnewthing/20260729-00/?p=112570)*