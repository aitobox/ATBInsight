# Making an agile version of a Windows Runtime delegate in C++/WinRT, part 7

## Summary
In this seventh installment, the series continues refining the construction of a `std::unique_ptr` with a custom deleter to prevent resource leaks in C++/WinRT. After previously solving an exception-safety issue regarding the `unique_ptr` deleter's constructor, this post addresses a potential raw pointer leak that occurs if the deleter itself throws an exception *after* the raw pointer has already been created. The solution involves instantiating the deleter prior to acquiring the raw pointer.

---

## Fixing Resource Leaks During Deleter Construction

Last time, we [fixed the problem of creating a `unique_ptr` whose deleter’s constructor might throw an exception](https://devblogs.microsoft.com/oldnewthing/20260727-00/?p=112566). But we’re not out of the woods yet.

Let’s take another look at what we currently have:

```cpp
    if (d.try_as<::INoMarshal>()) {
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return
            [p = std::unique_ptr<void, in_context_deleter>(p, {}),
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

We had originally broken the rule that the `unique_ptr(p)` constructor requires that the deleter’s default constructor not throw an exception. We fixed it by constructing the deleter explicitly as a parameter, so that the `unique_ptr` constructor can move it into the stored deleter without an exception.

### The Remaining Leak Hazard

But wait: if an exception occurs during the construction of the `in_context_deleter`, the raw pointer we created in the previous block will be leaked. It owns a reference count, but nothing cleans it up in the event of an exception.

We can fix this by creating the deleter **first**:

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

If there is an exception constructing the custom deleter, it happens *before* we initialize the raw pointer. Therefore, there is no leak of the reference owned by that raw pointer.

Okay, so are we done now?

Nope.

More next time.

---

*Source: [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260728-00/?p=112568)*