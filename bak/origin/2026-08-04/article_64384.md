# Making an Agile Version of a Windows Runtime Delegate in C++/WinRT (Part 10)

## Summary
In this installment of the series on agile delegates, the focus shifts to addressing a commenter's question: *Is `IContextCallback::ContextCallback` guaranteed to succeed inside a deleter, and what happens if it fails?* The article analyzes the potential causes of failure—such as unresponsiveness, apartment destruction, or low-memory conditions—and concludes that most failures are unrecoverable. Ultimately, following the precedent set by C++/CX, the implementation chooses to ignore release errors, with a promise of further improvements in the next part.

---

## Handling Failures in `IContextCallback`

In [Part 5 of this series](https://devblogs.microsoft.com/oldnewthing/20260724-00/?p=112562), a commenter asked: 

> *"Is the `ContextCallback` in the deleter guaranteed to always succeed? According to the docs it can fail. I wonder if there’s a way to move the fallible part to an earlier point so the deleter can be infallible."*

Let’s examine the first part of this question: **What if `IContextCallback::ContextCallback` fails?**

A failure indicates that COM could not switch to the destination context. If you cannot switch to the destination context, you cannot release the pointer. Furthermore, it is rarely clear what recovery strategy is even possible. Should you simply keep retrying until it works?

### The ASTA Reentrancy Dilemma

If the destination context is an Application Single-Threaded Apartment (ASTA), a failure might occur because the context is currently busy, and ASTAs disallow arbitrary reentrancy. 

* **The Retry Problem:** You cannot simply block on a retry loop. If the destination context happens to be calling into your current thread, spinning in a retry loop will deadlock because it is waiting for *you* to finish. You would have to return, let your current work finish (allowing the ASTA to resume), and only then attempt to call back into the ASTA.
* **COM Behavior:** Conventional COM calls into an ASTA face this issue, but we are using `IContextCallback`, which allows us to control whether we honor ASTA reentrancy roadblocks:

  > *"If `riid` is set to `IID_ICallbackWithNoReentrancyToApplicationSTA`, the function does not reenter an ASTA arbitrarily."*

Since we do not pass that special value, our call to `ContextCallback` is permitted to reenter an ASTA, removing one potential source of failure.

---

## Other Causes of Context-Switch Failures

What other reasons might prevent us from switching to the destination apartment?

1. **The Destination Apartment No Longer Exists:** 
   This is the most likely cause, leaving no room for recovery. Depending on how the object was managed by its creating thread, it may have been forcibly destroyed at thread termination,^[This is often combined with a `CoDisconnectObject` call to force proxies to fail all calls with `RPC_E_DISCONNECTED`, ensuring no external references linger to destroyed objects.] or it may have simply leaked. At any rate, the pointer can no longer be released.
2. **Low-Memory Conditions / Unresponsive Threads:** 
   As discussed previously regarding [cross-thread COM call failures (`RPC_E_SYS_CALL_FAILED`)](https://devblogs.microsoft.com/oldnewthing/20230216-00/?p=107836), the most common culprit is a destination thread that has stopped pumping messages. While you could technically wait and retry, in practice, a thread whose inbound message queue is full is unlikely to magically start responding soon.

---

## Conclusion and Next Steps

Ultimately, all of these failures are effectively unrecoverable—even though some are technically non-fatal (like the `CoDisconnectObject` scenario). Unfortunately, we cannot easily distinguish between these states. While `ContextCallback` returns `RPC_E_DISCONNECTED` when a destination apartment no longer exists, we don't always know how that apartment cleaned up its orphaned objects.

Following the C++/CX implementation of lazy-created agile delegates, our approach will simply **ignore errors** that occur when trying to release the original pointer.

*Can we do better? Find out next time.*

---

*Based on an article from [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260731-00/?p=112578).*