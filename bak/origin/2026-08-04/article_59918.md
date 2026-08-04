# The Case of the Mysterious Changes to Integers When There Shouldn’t Have Been Any Code Generation Effect

## Summary
During a routine refactoring to migrate from the legacy `NDIS_STRING_CONST` macro to the type-safe `RTL_CONSTANT_STRING`, a developer noticed unexpected differences in the compiled binary. Specifically, four functions exhibited integer constants that decreased by exactly one, despite the macro changes having identical semantic outcomes. Furthermore, one of these modified functions resided in a completely untouched source file. This investigation explores how a seemingly unrelated line deletion caused source-level line numbers to shift, which in turn propagated into debugging metadata and was even carried across source files via Link-Time Code Generation (LTCG).

---

## The Mystery: Binary Changes Without Functional Changes

A colleague made a code change that *should* have had zero effect on the generated binary: migrating from [the `NDIS_STRING_CONST` macro](https://github.com/tpn/winsdk-10/blob/9b69fd26ac0c7d0b83d378dba01080e93349c2ed/Include/10.0.16299.0/km/ndis.h#L1153) to [the more type-safe `RTL_CONSTANT_STRING` macro](https://github.com/tpn/winsdk-10/blob/9b69fd26ac0c7d0b83d378dba01080e93349c2ed/Include/10.0.14393.0/shared/ntdef.h#L2037). 

However, looking at the resulting binary revealed that **four functions had changed**. Even stranger, three of those functions were in a modified source file, while the fourth was in a source file that wasn't touched at all!

### Disassembled Comparison

| Before | After |
| :--- | :--- |
| **`contoso!EvtWdfWidgetContextCleanup`** | |
| `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [rsp+20h], rcx`<br>`mov r9d, 62Bh`<br>`mov r8d, 52467443h`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov rdx, rbx`<br>`mov rax, [rax+670h]`<br>`call __guard_dispatch_call` | `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [rsp+20h], rcx`<br>`mov r9d, 62Ah` *(Decreased by 1)*<br>`mov r8d, 52467443h`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov rdx, rbx`<br>`mov rax, [rax+670h]`<br>`call __guard_dispatch_call` |
| **`contoso!Function2`** | |
| `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [rsp+20h], rcx`<br>`mov r9d, 616h`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov r8d, 52467443h`<br>`mov rdx, rdi`<br>`mov rax, [rax+668h]`<br>`call __guard_dispatch_call` | `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [rsp+20h], rcx`<br>`mov r9d, 615h` *(Decreased by 1)*<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov r8d, 52467443h`<br>`mov rdx, rdi`<br>`mov rax, [rax+668h]`<br>`call __guard_dispatch_call` |
| **`contoso!Function3`** | |
| `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [r11-20h], rcx`<br>`xor r8d, r8d`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov r9d, 35Dh`<br>`mov rax, [rax+0DB0h]`<br>`call __guard_dispatch_call` | `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov [r11-20h], rcx`<br>`xor r8d, r8d`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov r9d, 35Ch` *(Decreased by 1)*<br>`mov rax, [rax+0DB0h]`<br>`call __guard_dispatch_call` |
| **`contoso!Function4`** | |
| `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov rdx, [rbp+8]`<br>`mov r9d, 377h`<br>`mov [rsp+20h], rcx`<br>`mov r8d, 49507443h`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov rax, [rax+0DB8h]`<br>`call __guard_dispatch_call` | `mov rax, [contoso!WdfFunctions_01031]`<br>`lea rcx, [??_C@__0DK@MPBCIIPN@...]`<br>`mov rdx, [rbp+8]`<br>`mov r9d, 376h` *(Decreased by 1)*<br>`mov [rsp+20h], rcx`<br>`mov r8d, 49507443h`<br>`mov rcx, [contoso!WdfDriverGlobals]`<br>`mov rax, [rax+0DB8h]`<br>`call __guard_dispatch_call` |

In every single case, a single integer embedded in the instructions changed to a value precisely *one smaller*.

---

## Evaluating LLM Explanations

When asked to explain the discrepancy, an LLM suggested that the changes were related to **Control Flow Guard (CFG)** metadata. 

However, this hypothesis fails on two fronts:
1. **Register Purpose:** For a guard dispatch call, the only parameter CFG cares about is the `rax` register (which holds the target function pointer being checked). All other registers contain parameters destined for the called function. Because the mutations occurred in `r9d`, they are entirely unrelated to CFG validation.
2. **Data vs. Code:** CFG metadata is not stored inside the executable code text section; rather, it is stored as a [separate data block inside the binary](https://devblogs.microsoft.com/oldnewthing/20251029-00/?p=111738).

---

## Tracking Down the Source

Let's examine `EvtWdfWidgetContextCleanup`:

```cpp
void EvtWdfWidgetContextCleanup(_In_ WDFOBJECT Object)
{
    auto widgetContext = GetContextFromWidgetHandle(Object);
    if (widgetContext->NeedsDereference)
    {
        widgetContext->NeedsDereference = FALSE;
        WdfObjectDereferenceWithTag(Object, CONTOSO_WIDGET_TAG);
    }
}
```

The compiler attributes the change directly to `WdfObjectDereferenceWithTag`. Looking at the [WDF header definitions](https://github.com/microsoft/Windows-Driver-Frameworks/blob/b6191d9543441329154da32f7ab9bdd97228dd3c/src/publicinc/wdf/kmdf/1.31/wdfobject.h), this is defined as a macro:

```cpp
#define WdfObjectDereferenceWithTag(Handle, Tag) \
        WdfObjectDereferenceActual(Handle, Tag, __LINE__, __FILE__)
```

Which wraps [an inline function](https://github.com/microsoft/Windows-Driver-Frameworks/blob/b6191d9543441329154da32f7ab9bdd97228dd3c/src/publicinc/wdf/kmdf/1.31/wdfobject.h#L701-L715) accepting `__LINE__` and `__FILE__` parameters:

```cpp
_IRQL_requires_max_(DISPATCH_LEVEL)
VOID
FORCEINLINE
WdfObjectReferenceActual(
    _In_ WDFOBJECT Handle,
    _In_opt_ PVOID Tag,
    _In_ LONG Line,
    _In_z_ PCCH File
    )
{
    ((PFN_WDFOBJECTREFERENCEACTUAL) WdfFunctions[WdfObjectReferenceActualTableIndex])
        (WdfDriverGlobals, Handle, Tag, Line, File);
}
```

*(Note: [`WdfFunctions` expands to `WdfFunctions_01031`](https://github.com/microsoft/Windows-Driver-Frameworks/blob/b6191d9543441329154da32f7ab9bdd97228dd3c/src/publicinc/umdf/1.31/wdf.h#L60), ensuring version mismatches result in linker errors rather than runtime undefined behavior.)*

Mapping this back to the compiled assembly output:

```assembly
    mov rax, [contoso!WdfFunctions_01031]   ; WdfFunctions
    lea rcx, [??_C@__0DK@MPBCIIPN@...]      ; Address of the File string
    mov [rsp+20h], rcx                      ; File parameter
    mov r9d, 62Bh                           ; Line parameter
    mov r8d, 52467443h                      ; Tag parameter
    mov rcx, [contoso!WdfDriverGlobals]     ; WdfDriverGlobals parameter
    mov rdx, rbx                            ; Handle parameter
    mov rax, [rax+670h]                     ; Load function pointer
    call __guard_dispatch_call              ; Validate and call¹
```

**The mystery solved:** The modified value is the **line number** (`__LINE__`).

---

## Why Did the Line Numbers Change?

Checking the pull request history revealed that the author had removed a single unused line from the top of the source file:

```cpp
#include <strsafe.h>
#include "stringutils.h" // <-- DELETED
```

Because `stringutils.h` contained a private definition of the obsolete `NDIS_STRING_CONST` macro which was no longer required, the developer deleted the `#include` directive. 

Deleting a line from the top of the source file causes **all subsequent line numbers in that file to shift down by one**. Consequently, the line numbers passed into `WdfObjectDereferenceWithTag` decreased by 1, resulting in clean, non-functional binary alterations.

---

## Bonus Chatter: The Untouched File

Wait—what about the fourth function, which changed inside a source file that was *never touched* in the pull request?

The explanation lies in **Link-Time Code Generation (LTCG)**. The fourth function contained a call to a helper function defined inside the modified source file. During the link phase, the compiler's optimizer decided to **inline** that helper function. Because the helper function was inlined, its internal line-number macro evaluation picked up the shifted line numbers from the modified file, causing a code generation change in an entirely independent source file.

***

¹ *For more details on this mechanism, see [The other kind of control flow guard check: The combined validate and call](https://devblogs.microsoft.com/oldnewthing/20260708-00/?p=112510).*