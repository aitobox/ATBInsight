# Release: sqlite-utils 4.1.1

### Summary
The 4.1.1 release of `sqlite-utils` introduces a critical safety fix regarding foreign key constraints during table transformations, alongside improved documentation cross-referencing between the CLI and Python API. This update was prompted by an edge case identified during an exploration of `ON DELETE` behaviors.

---

### Key Changes

#### 1. Safety Improvement for `table.transform()`
A new `TransactionError` is now raised when calling `table.transform()` under specific conditions:
* **Conditions:** An active transaction is open, `PRAGMA foreign_keys` is enabled, and the table is subject to destructive `ON DELETE` actions (`CASCADE`, `SET NULL`, or `SET DEFAULT`).
* **Reasoning:** Because `PRAGMA` settings cannot be altered within a transaction, the previous implementation risked silently triggering destructive actions when dropping the old table. 
* **Reference:** See the official documentation on [Foreign keys and transactions](https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-transform-foreign-keys-transactions) for more details and recommended workarounds. (Issue [#794](https://github.com/simonw/sqlite-utils/issues/794))

#### 2. Enhanced Documentation
The [CLI](https://sqlite-utils.datasette.io/en/stable/cli.html) and [Python API](https://sqlite-utils.datasette.io/en/stable/python-api.html) documentation have been updated to provide better discoverability. Sections now include cross-references, allowing users to easily navigate between the command-line interface and the corresponding Python library functionality. (Issue [#791](https://github.com/simonw/sqlite-utils/issues/791))

---

### Links
* **Release Notes:** [sqlite-utils 4.1.1](https://github.com/simonw/sqlite-utils/releases/tag/4.1.1)
* **Tags:** #sqlite, #sqlite-utils