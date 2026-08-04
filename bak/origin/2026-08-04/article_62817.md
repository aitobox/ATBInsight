# Making an Agile Version of a Windows Runtime Delegate in C++/WinRT (Part 4)

## Summary
In this fourth installment, the implementation of the context-checking wrapper delegate is optimized. Instead of performing expensive COM object comparisons—which incur internal `AddRef` and `Release` overhead—the solution is refactored to use integer-based context tokens via `CoGetContextToken()`. While this significantly speeds up future checks, the article concludes with a teaser that a subtle flaw still exists in the updated code.

---

## Optimizing Context Checks with Tokens

Previously, we constructed a wrapper delegate that verified whether the invocation context matched the captured context by directly comparing `IContextCallback` objects:

```cpp
if (d.try_as<::INoMarshal>()) {
    return [d = std::forward<Delegate>(d),
            context = winrt::capture<IContextCallback>(CoGetObjectContext)](auto&&...args) {
        if (context == winrt::capture<IContextCallback>(CoGetObjectContext)) {
            d(std::forward<decltype(args)>(args)...);
        } else {
            throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
        }
    };
}
```

While functional, this approach requires obtaining the current object context on every invocation, triggering an internal `AddRef` followed by an explicit `Release`.

### The Lightweight Approach: `CoGetContextToken`

We can avoid instantiating and comparing COM objects altogether. The `CoGetContextToken` function returns a lightweight integer that uniquely identifies a live context object, allowing us to compare integer tokens instead.

> **Note:** The context must remain live to prevent token value reuse. This operates similarly to process and thread IDs, which remain unique as long as they are active or held by a `HANDLE`.

By retaining the `IContextCallback` (returned by `CoGetObjectContext`) to keep the context alive, we can cache its associated context token for rapid subsequent validations:

```cpp
ULONG_PTR get_context_token()                       
{                                                   
    ULONG_PTR token;                                
    winrt::check_hresult(CoGetContextToken(&token));
    return token;                                   
}                                                   

if (d.try_as<::INoMarshal>()) {
    return [d = std::forward<Delegate>(d),
            context = winrt::capture<IContextCallback>(CoGetObjectContext),
            token = get_context_token()](auto&&...args) {
        if (token == get_context_token()) {
            d(std::forward<decltype(args)>(args)...);
        } else {
            throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
        }
    };
}
```

### Are We Done?

Of course not! There is a hidden flaw in the code above. We will explore and address it next time.

---

*Adapted from [The Old New Thing](https://devblogs.microsoft.com/oldnewthing).*