# My Misunderstanding About Tabs in Python 3

## Summary
For years, the author labored under the common misconception that Python 3 strictly banned tab characters in favor of spaces. In reality, Python 3 is more nuanced: it permits either tabs or spaces, but strictly forbids inconsistently mixing them within the same file. This article explores the official indentation rules, how editor misconfigurations trigger `TabError`, and the practical realities of managing mixed-indentation codebases.

---

## Python 2 vs. Python 3: The Indentation Evolution

Python 2 was famously relaxed about mixing tabs and spaces, though it rigidly assumed that tabs were always equivalent to 8-space intervals. While this wasn't a major issue when using 8-space indents, it became problematic as the Python community shifted toward 4-space indents. This shift meant that purely tab-based indents and space-based indents often had to coexist.

Python 3 tightened these rules, leading many developers—including the author—to mistakenly assume that Python 3 dropped support for tabs entirely and required spaces-only indentation. 

* **The Reality Check:** Historical Python 2 code using tab-based indentation can generally be ported to Python 3 with only minor syntax and `#!` line updates. Python 3 definitely still accepts tabs.

---

## The Official Rules: What Python 3 Actually Prohibits

The official [Python 3 Language Reference (Section 2.1.8: Indentation)](https://docs.python.org/3/reference/lexical_analysis.html#indentation) defines the rule clearly:

> Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; a [`TabError`](https://docs.python.org/3/library/exceptions.html#TabError) is raised in that case.

In practice, this means:
* You can have spaces *after* tabs.
* You cannot intermittently use tabs at the start of some lines and the equivalent amount of spaces at the start of others (based on an 8-space tab world).
* Ultimately, **you must stick to a single indentation scheme (all tabs or all spaces) per file.**

---

## Editor Friction: Emacs and Vim

This rule usually surfaces when editing legacy codebases where an editor isn't configured correctly:

* **GNU Emacs:** This typically happens when [`indent-tabs-mode`](https://www.gnu.org/software/emacs/manual/html_node/emacs/Just-Spaces.html) is set incorrectly (perhaps due to an automation script failing to run).
* **Vi(m):** When editing a space-indented Python 3 program, hitting the `TAB` key inserts an actual tab character, creating a potential `TabError` trap. This makes Vim a bit more frustrating to use casually for Python 3 code.

---

## Fixing Indentation: Theory vs. Practice

In theory, converting files is straightforward using standard command-line tools or editor built-ins:
* **Vim:** Pass the entire file through [`expand`](https://www.man7.org/linux/man-pages/man1/expand.1.html) (using `:!`) to convert tabs to spaces, or [`unexpand`](https://www.man7.org/linux/man-pages/man1/unexpand.1.html) to go the other way.
* **GNU Emacs:** Use the built-in `untabify` and `tabify` commands.

### Why Conversion Is Rarely Practical
In reality, the author avoids wholesale conversions for a few reasons:
1. **Stubbornness and Scope:** Fixing massive, multi-file codebases is often too much labor.
2. **Version Control Noise:** Yanking code around creates massive, unhelpful diffs that muddy the git history. The ideal time for this migration would have been during the initial Python 2 to Python 3 transition, but that ship has sailed.
3. **The Vi(m) Advantage:** Keeping code tab-based has a quiet advantage—coworkers using plain `vi(m)` can make quick spot changes without accidentally triggering indentation traps.

***

*(Source: [Original blog post](https://utcc.utoronto.ca/~cks/space/blog/python/Python3TabsMisunderstanding) / [3 comments](https://utcc.utoronto.ca/~cks/space/blog/python/Python3TabsMisunderstanding?showcomments#comments))*