# Bug Reports Are Hard: Minor Details Matter Edition

## 📝 Summary
This article reflects on a recent bug-reporting experience with the GNU Emacs **Flycheck** package and language server clients like **Eglot**. Through a personal mistake in a follow-up bug report, the author realizes how easily users make assumptions about which technical details matter. This insight serves as a powerful reminder for system administrators and developers: when users omit crucial details or include irrelevant ones, they are simply guessing based on incomplete knowledge—much like professionals do when dealing with external support systems.

---

## 🚀 The Flycheck and Eglot Update
Recently, an interesting commit landed in the GNU Emacs [Flycheck](https://www.flycheck.org/) package. Flycheck shows diagnostics obtained from "checkers," including Emacs [language server clients](https://langserver.org/) like [Eglot](https://www.gnu.org/software/emacs/manual/html_node/eglot/index.html), which in turn fetch diagnostics from various language servers. 

Through [this commit](https://github.com/flycheck/flycheck/commit/108ea10caf44f18145decfdfb9d2c37e9c05fecd) ([PR here](https://github.com/flycheck/flycheck/pull/2277)), Flycheck was updated to better handle diagnostic sources that report information asynchronously. Eglot is one such source, largely because its diagnostics rely on communication with background language server processes.

## 🐛 How the Bug Report Unfolded
This update stems from [an issue I originally reported](https://github.com/flycheck/flycheck/issues/2201). When the core bug was fixed, [I reported a side effect of that fix](https://github.com/flycheck/flycheck/issues/2201#issuecomment-5137319841). 

During my initial bug report, I made sure to reproduce the issue both with and without Eglot to confirm it wasn't specific to Flycheck's Eglot integration. However, once the initial issue was resolved and a new side effect appeared, I didn't bother performing that dual check. I simply tested using Eglot because it was the most convenient option for my workflow (using a Go project with a lingering lint issue I disagree with).

## ⚠️ The Danger of Assumptions
I assumed that because the initial bug was independent of Eglot, the new problem would be as well. 

This assumption proved incorrect due to a detail revealed in [the commit](https://github.com/flycheck/flycheck/commit/108ea10caf44f18145decfdfb9d2c37e9c05fecd): **Eglot produces diagnostics asynchronously**, whereas Flycheck's conventional checkers produce them synchronously (from Flycheck's perspective). Had I known this distinction, I would have tested both environments. Instead, I operated under the false assumption that all diagnostic sources were functionally identical.

Even while knowing that bug reports are hard and that details matter, I still fell into the trap of making an assumption. The assumption seemed logical based on my knowledge at the time, but I lacked insight into the system's inner workings—and one of those hidden details made all the difference.

## 💡 Lessons for System Administrators and Support
This experience mirrors the challenges we face when users report problems in [our own systems](https://support.cs.toronto.edu/). 

As administrators, we know the inner workings of our systems, including which details matter and which do not. Our users, however, do not share this knowledge. We should never be surprised when incoming problem reports contain irrelevant noise while omitting crucial data. Users are simply guessing—just as I did. 

Furthermore, users often perform exhaustive checks on their initial reports, but as follow-up issues arise, they begin taking shortcuts to save time and effort. 

> *Let's face it: performing endless verification checks is tedious work. When those extra steps turn out to be pointless, users feel annoyed—and eventually, they stop doing work that only frustrates them.*

*Note: Applications of these lessons to the experiences system administrators face when filing bug reports with external vendors are left as an exercise to the reader. Though I now feel a bit more sympathetic toward support organizations, some behaviors remain undeniably irritating.*