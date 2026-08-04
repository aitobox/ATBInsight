# The Case of the Invalid Function Pointer When Shutting Down the Display Control Panel

## Summary
A recurring crash in a display control panel extension (`Contoso`) was tracked down to a **one-byte bug**: during window cleanup on `WM_DESTROY`, a 64-bit window procedure pointer was incorrectly cast to a 32-bit `LONG` instead of a `LONG_PTR`. This caused the pointer to be truncated and sign-extended into an invalid kernel-mode address space, triggering a crash inside Control Flow Guard (`ntdll!LdrpDispatchUserCallTarget`) when attempting to restore the original window procedure.

---

## 1. Analyzing the Crash Dump

The primary crash signature points to an invalid function pointer lookup in `ntdll`:

```text
ntdll!LdrpDispatchUserCallTarget+0xe:
00007fff`924acd1e mov     r11,qword ptr [r11+r10*8] ds:04007df5`0159db48=????????????????

Call Site
ntdll!LdrpDispatchUserCallTarget+0xe
user32!UserCallWinProcCheckWow+0x2bd
user32!DispatchClientMessage+0x9c
user32!__fnDWORD+0x33
ntdll!KiUserCallbackDispatcherContinue
win32u!ZwUserDestroyWindow+0x14
comctl32!_RealPropertySheet+0x36d
comctl32!_PropertySheet+0x47
Display!PropertySheetW+0x5d
Display!AdvancedSettingSheetHelper+0x3be
Display!ShowAdapterSettings+0x89
...
```

By inspecting the instruction register source, we find the invalid function pointer in `rax`:
```text
rax=ffffffff924bbde0
```

On 64-bit Windows, user-mode pointers start with `0000`, while kernel-mode pointers start with `ffff`. This pointer is clearly invalid for user mode.

---

## 2. Pinpointing the Truncation

Listing the loaded modules reveals that valid code addresses containing the lower bits in the `92xxxxxx` range belong to `ntdll` (`00007fff` base). Using `ln` (list near symbol), we can resolve the intended address:

```text
0:000> ln 7fff924bbde0
(00007fff`924bbde0)   ntdll!NtdllButtonWndProc_A   |  (00007fff`924bbdf0)   ntdll!NtdllButtonWndProc_W
```

The pointer was truncated to 32 bits (`924bbde0`) and then sign-extended back to `ffffffff924bbde0`. This strongly implies a subclassed window procedure was being restored incorrectly.

---

## 3. Investigating the Property Sheet Pages

Using internal symbols to inspect the property sheet structure (`Display!AdvancedSettingSheetHelper`), we find the associated extension modules:

```text
0:000> ?? psh
struct _PROPSHEETHEADERW_V2
   +0x028 nPages           : 4
   +0x038 phpage           : 0x00000017`85a7ec70  -> 0x000001d5`4e1aac90 _PSP
```

Dumping the `HPROPSHEETPAGE` entries reveals the modules providing the property sheet pages:
* `deskadp` (Microsoft)
* `deskmon` (Microsoft)
* `colorui` (Microsoft)
* `contoso` (Third-party plug-in)

Inspecting the `PROPSHEETPAGE` structure for the `contoso` module (`0x000001d5`4e1d26e0`):
```text
   +0x028 pfnDlgProc       : 0x00000001`800047ac contoso+0x47ac
```

---

## 4. Decompiling the Dialog Procedure

Reviewing the disassembly of the dialog's destruction sequence reveals the call to `SetWindowLongPtr`:

```text
00000001`80004716 movsxd  rbx,dword ptr [00000001`80039c50] ; Truncated 32-bit load!
...
00000001`80004733 call    [00000001`8002b4a0]               ; SetWindowLongPtr(hwnd, GWLP_WNDPROC, ...)
```

Checking the global variable at `00000001`80039c50`:
```text
0:000&gt; dp 00000001`80039c50 l1
00000001`80039c50  00007fff`924bbde0
```

The global variable stores the correct 64-bit pointer, but the `movsxd` instruction sign-extended a 32-bit read due to an incorrect cast in the C++ source code:

```cpp
// Flawed Code:
SetWindowLongPtr(GetDlgItem(m_hdlg, 0x668), GWLP_WNDPROC, (LONG)g_originalWndProc);
```
*(Casting to `LONG` instead of `LONG_PTR` causes the truncation).*

---

## 5. The Fix

By checking the x86_64 instruction encoding, we can patch the binary directly:
* **Original instruction (`movsxd`):** `48 63 1d 33 55 03 00` (`63` corresponds to `movsxd`)
* **Desired instruction (`mov` 64-bit):** `48 8b 1d 33 55 03 00` (`8b` corresponds to `mov` r64)

Applying the patch in the debugger:
```text
0:000> eb 00000001`80004717 8b
0:000> u 00000001`80004716 l1
00000001`80004716 488b1d33550300  mov     rbx,qword ptr [00000001`80039c50]
```

The one-byte modification successfully restores proper 64-bit pointer handling, eliminating the crash.