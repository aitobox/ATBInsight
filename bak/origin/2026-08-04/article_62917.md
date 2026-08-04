# Ruff v0.16.0

## Summary
Astral released **Ruff v0.16.0** on July 23rd, introducing a massive expansion to its default rule set—jumping from 59 to 413 active rules. While this update catches critical bugs and syntax errors out of the box, unpinned dependencies may cause CI pipelines to fail. This post explores the impact of the upgrade across major Python projects like *Datasette*, *sqlite-utils*, and *LLM*, demonstrating how to automatically fix issues using CLI commands and AI coding agents.

---

## Key Highlights

* **Massive Default Expansion:** Ruff now enables 413 rules by default (up from 59), drawing from a total pool of 968 rules.
* **Catching Critical Issues:** The newly enabled rules surface serious problems automatically, including syntax errors and immediate runtime bugs, without requiring manual configuration.
* **AI-Ready Output:** Detailed error reports provide exact context, making it trivial for coding agents to resolve remaining issues.

---

## Trying Out the New Version

You can test the latest version on any Python project instantly using `uv`:

```bash
uvx ruff@latest check .
```

Running this against major projects like [Datasette](https://datasette.io/), [sqlite-utils](https://sqlite-utils.datasette.io/), and [LLM](https://llm.datasette.io/) immediately surfaced hundreds of minor issues breaching the new default rules.

---

## Upgrading Projects

Because the projects feature comprehensive test suites running against Python 3.10 through 3.14, upgrading was relatively safe. The bulk of the issues were resolved with a single command:

```bash
uvx ruff@latest check . --fix --unsafe-fixes
```

For **sqlite-utils**, this command reported:

> `Found 1618 errors (1538 fixed, 80 remaining).`

### Example Remaining Issues

Ruff provides clear, actionable explanations for each remaining violation:

```text
DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> tests/test_duplicate.py:17:10
   |
15 |     "datetime_col" TEXT)""")
16 |     # Insert one row of mock data:
17 |     dt = datetime.datetime.now()
   |          ^^^^^^^^^^^^^^^^^^^^^^^
18 |     data = {
19 |         "text_col": "Cleo",
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

BLE001 Do not catch blind exception: `Exception`
  --> tests/test_plugins.py:16:12
   |
14 |         db.execute("select * from pragma_function_list()")
15 |         return True
16 |     except Exception:
   |            ^^^^^^^^^
17 |         return False
18 |     finally:
   |

B018 Found useless attribute access. Either assign it to a variable or remove it.
  --> tests/test_update.py:46:5
   |
44 | def test_update_invalid_pk(fresh_db, pk, update_pk):
45 |     table = fresh_db["table"]
46 |     table.insert({"id1": 5, "id2": 3, "v": 1}, pk=pk).last_pk
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
47 |     with pytest.raises(NotFoundError):
48 |         table.update(update_pk, {"v": 2})
   |
```

---

## Fixing with AI Coding Agents

Given the clarity of Ruff's output, the remaining issues were easily handed off to AI coding assistants:
* **Codex** (GPT-5.6 Sol high) upgraded [LLM](https://github.com/simonw/llm/pull/1557) and [sqlite-utils](https://github.com/simonw/sqlite-utils/pull/814).
* **Claude Code** (with Opus 5) upgraded [Datasette](https://github.com/simonw/datasette/pull/2857).

---

* **Tags:** [python](https://simonwillison.net/tags/python) · [ruff](https://simonwillison.net/tags/ruff) · [astral](https://simonwillison.net/tags/astral)