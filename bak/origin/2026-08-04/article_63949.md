# Solving My Problem with the Emacs Lisp Byte Compilation Checker

## Summary
When splitting up an Emacs initialization file into modular components loaded via `load-file`, third-party macros (like those from `marginalia`) cause byte-compilation checker errors because packages aren't initialized yet. While adding `package-initialize` inside `eval-when-compile` fixes the checker, it triggers annoying startup warnings. The clean, straightforward solution in Flycheck is setting a single configuration variable, though a more localized "clever" fix involving function advice is also possible.

---

## The Problem
Over on the [Fediverse](https://mastodon.social/@cks/117000332807303378), I posted a somewhat cryptic lament:

> *My GNU Emacs tiny kingdom for something that only ran at byte-compile time purely so I can pacify ELisp checker errors that only happen then (in a file that is not byte compiled otherwise), and which can't be guarded with 'eval-while-compile' because then they get run twice.*
>
> *(It's complicated. This file is load-file'd by my .emacs and needs macros from third party packages to pass type checking.)*

## Background: Modularizing `.emacs`
A while back, [I split up my `.emacs` file](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsSplittingMyInitFile). Part of this process involved moving related blocks of `use-package` configurations into separate files and pulling each one in using `load-file`. 

Inside these files, I often define helper functions within `:init` or `:config` sections. For example:

```elisp
(use-package marginalia
  :init
    (defun marginalia-annotate-variable-docstring (cand)
    "Annotate variable CAND with only its documentation string."
    (when-let* ((sym (intern-soft cand)))
      (marginalia--fields
       ((or (documentation-property sym 'variable-documentation)
            (marginalia--definition-prefix sym))
	:truncate 1.0 :face 'marginalia-documentation))))
  [...]
```

When writing Emacs Lisp, using a linter like [Flycheck or Flymake](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsFlymakeFlycheck) (I prefer Flycheck) is invaluable for catching errors early. Under the hood, this works by running the Emacs Lisp byte compiler on your file and reporting any warnings.

## The Compilation Complication
To get a modularized init file to check properly, `use-package` needs to be available during byte compilation. The standard way to handle this is:

```elisp
(eval-when-compile
  (require 'use-package))
```

However, a complication arises: `marginalia--fields` is a macro. Its syntax is different enough that it triggers a byte-compilation error if interpreted as a regular function. 

If the macro were defined at byte-compilation time, there would be no issue. But even with `use-package` available, the macro isn't pulled in because of [package initialization constraints](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsMinimalEnvForPackage). Marginalia is a third-party package stored in an ever-changing subdirectory under `~/.emacs.d/elpa/`, which isn't added to the Emacs `load-path` until package initialization runs.

### The Tempting (But Flawed) Fix
Naturally, you might think you can force package initialization during compilation just like we did with `use-package`:

```elisp
(eval-when-compile
  (package-initialize))
```

With this in place, the file passes byte-compilation checks. However, starting Emacs normally results in an annoying warning:

```text
Warning (package): Unnecessary call to 'package-initialize' in init file
```

This happens because my main `.emacs` file *also* calls `package-initialize` [(partly for historical reasons)](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsMinimalEnvForPackage). When Emacs starts, both the main file and the loaded submodule run `package-initialize`, triggering the complaint. 

At the time of [my Fediverse post](https://mastodon.social/@cks/117000332807303378), I was wishing for a variant of `eval-when-compile` that silently *does nothing* when normally interpreted, ensuring the guarded `package-initialize` only runs during byte-compile checks.

## The Solution

Since [I normally use Flycheck](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsFlymakeFlycheck), I bypassed the macro dilemma by setting:

```elisp
(setq flycheck-emacs-lisp-initialize-packages t)
```

This works for my particular setup. Flycheck's [emacs-lisp checker](https://www.flycheck.org/en/latest/languages.html#emacs-lisp) can automatically initialize packages at the start of a byte-compilation check, but it normally restricts this to files inside `user-emacs-directory` (`~/.emacs.d`). Because I keep my startup files elsewhere, forcing `flycheck-emacs-lisp-initialize-packages` to `t` makes Flycheck initialize packages universally. 

*(Note: This might have unintended side effects if you work on external Emacs Lisp projects outside your personal config, but it works fine for me since I only write ELisp for my own setup.)*

---

## Sidebar: Fixing it the "Clever" Way

Flycheck uses a helper function, `flycheck-in-user-emacs-directory-p`, to determine if a file lives under your user Emacs directory. 

The morally superior way to solve this would be to use [`advice-add`](https://utcc.utoronto.ca/~cks/space/blog/programming/EmacsChangingLispWithAdviceAdd) to make that function return `true` for files residing in my personal Emacs Lisp directory tree, leaving `flycheck-emacs-lisp-initialize-packages` at its default `auto` setting.

*(I lack the energy to write that advice code right now. While `flycheck-emacs-lisp-package-user-dir` might also be a candidate for adjustment, its exact side effects remain unclear, making me wary of tampering with it.)*