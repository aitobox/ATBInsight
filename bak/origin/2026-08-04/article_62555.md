# Making an Agile Version of a Windows Runtime Delegate in C++/WinRT (Part 3)

### Summary
In this installment, we address a specific edge case in C++/WinRT delegate agility: objects that implement the `INoMarshal` interface. Because `RoGetAgileReference` fails for these objects with `CO_E_NOT_SUPPORTED`, we implement a wrapper that allows these delegates to function as long as they are invoked within their original context, deferring the exception only if a cross-context call is attempted.

---

### The Problem: `INoMarshal` Objects
When an object implements `INoMarshal`, it explicitly forbids marshaling. Consequently, the `agile_ref` class—which relies on `RoGetAgileReference`—throws a `CO_E_NOT_SUPPORTED` exception upon creation. 

This is problematic because the error occurs at the *creation* of the reference, even if the delegate is only ever invoked from its original context, where marshaling wouldn't have been necessary in the first place.

### The Solution: Context-Aware Wrappers
To resolve this, we can create a wrapper that captures the original context. If the delegate is invoked from the same context, it executes normally. If it is invoked from a different context, it throws the `CO_E_NOT_SUPPORTED` error only at the moment of invocation.

#### First Implementation Attempt
The following code demonstrates how to check for `INoMarshal` and capture the `IContextCallback` to validate the context at runtime:

```cpp
// Don't use this yet - read to the end of the series

template<typename Delegate>
Delegate make_agile_delegate(Delegate const& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;
    }

    if (d.try_as<::INoMarshal>()) {                                                                
        return [d, context = winrt::capture<IContextCallback>(CoGetObjectContext)](auto&&...args) {
            if (context == winrt::capture<IContextCallback>(CoGetObjectContext)) {                 
                d(std::forward<decltype(args)>(args)...);                                          
            } else {                                                                               
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);                                    
            }                                                                                      
        };                                                                                         
    }                                                                                              

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
```

### Refinement: Supporting Universal References
To improve efficiency and allow for `std::move` semantics when dealing with rvalue references, we can update the function to use universal references:

```cpp
template<typename Delegate>
std::remove_reference_t<Delegate> make_agile_delegate(Delegate&& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;
    }

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

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
```

*Next time: We will explore an optimization to reduce the overhead of checking the context during every invocation.*