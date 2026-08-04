# Making an Agile Version of a Windows Runtime Delegate in C++/WinRT (Part 2)

## Summary
Building upon the previous implementation of agile Windows Runtime delegates, this article refines the approach by optimizing for delegates that are already agile. By checking for the `IAgileObject` marker interface, the function avoids unnecessary wrapper creation when the delegate is already thread-safe.

---

## Optimizing for Already-Agile Delegates

In many scenarios, the delegate passed to our function is already agile. To avoid the overhead of creating an unnecessary agile wrapper, we can check for the presence of the `IAgileObject` marker interface, which is implemented by all agile objects.

```cpp
template<typename Delegate>
Delegate make_agile_delegate(Delegate const& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;                    
    }                                

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
```

If the delegate declares itself as agile, it simply returns itself, serving as its own agile wrapper.

---

## What's Next?

While this optimization covers most cases, there is still another scenario that we missed. We will explore that case in the next installment.

---

## Bonus Chatter: Copy Elision Considerations

You might wonder if we could optimize pass-by-value semantics to achieve copy elision for agile delegates:

```cpp
template<typename Delegate>
Delegate make_agile_delegate(Delegate d)
{
    if (d.try_as<::IAgileObject>()) {
        return d; // copy elision?
    }

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
```

Unfortunately, this approach does not work as intended because function parameters are not eligible for copy elision.

---

*Source: [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260721-00/?p=112550)*