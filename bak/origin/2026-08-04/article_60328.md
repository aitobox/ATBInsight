# Release: sqlite-utils 4.1

> **Summary:** Released shortly after version 4.0, **sqlite-utils 4.1** introduces a handful of minor yet powerful features. Highlights include the ability to generate rows for insertion directly via Python code (`--code`), explicit column type overrides for CSV/TSV imports, piped SQL queries from standard input, automatic primary key inference for upserts, and new support for managing SQLite `STRICT` tables via `transform`.

---

## What's New in 4.1

### 1. Insert and Upsert via Python Code (`--code`)
`sqlite-utils insert` and `sqlite-utils upsert` now accept a `--code` option. This allows you to provide a block of Python code (or a path to a `.py` file) defining a `rows()` function or a `rows` iterable, serving as an alternative to importing from a file ([#684](https://github.com/simonw/sqlite-utils/issues/684)).

This extends the existing pattern used in commands like `sqlite-utils convert`:
```bash
sqlite-utils convert content.db articles headline '
def convert(value):
    return value.upper()'
```

Now, you can generate new rows directly:
```bash
sqlite-utils insert data.db creatures --code '
def rows():
    yield {"id": 1, "name": "Cleo"}
    yield {"id": 2, "name": "Suna"}
' --pk id
```

### 2. Column Type Overrides (`--type`)
`sqlite-utils insert` and `sqlite-utils upsert` now support the `--type column-name type` flag to override automatically inferred column types during table creation ([#131](https://github.com/simonw/sqlite-utils/issues/131)). This is particularly useful for CSV or TSV columns (like ZIP codes) that resemble integers but need to be stored as `TEXT` to preserve leading zeros.

### 3. Dropping Indexes by Name
* Added a new `table.drop_index(name)` Python method.
* Added a `sqlite-utils drop-index` CLI command.
* Both accept `ignore=True` or `--ignore` to gracefully handle missing indexes ([#626](https://github.com/simonw/sqlite-utils/issues/626)).

### 4. Reading SQL Queries from Standard Input
The `sqlite-utils query` command can now read SQL queries directly from standard input by passing `-` in place of the query string ([#765](https://github.com/simonw/sqlite-utils/issues/765)):
```bash
echo "select * from dogs" | sqlite-utils query dogs.db -
```

### 5. Automatic Primary Key Inference for Upserts
`sqlite-utils upsert` can now automatically infer the primary key of an existing table, meaning the `--pk` flag can be safely omitted when upserting into tables that already have a defined primary key.

### 6. SQLite Strict Mode Support for Transformations
Inspired by Evan Hahn’s article [*Prefer STRICT tables in SQLite*](https://evanhahn.com/prefer-strict-tables-in-sqlite/), version 4.1 adds support for altering tables between strict and non-strict modes:
* `table.transform()` and `table.transform_sql()` now accept `strict=True` or `strict=False` ([#787](https://github.com/simonw/sqlite-utils/issues/787)).
* The `sqlite-utils transform` command now accepts `--strict` and `--no-strict` flags ([#787](https://github.com/simonw/sqlite-utils/issues/787)).

Because SQLite does not natively support an `ALTER TABLE` command to toggle strictness, `sqlite-utils` leverages its robust [transform mechanism](https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-a-table) to transparently copy and rebuild the table under the hood.

---

## Links & Resources
* **GitHub Release:** [sqlite-utils 4.1](https://github.com/simonw/sqlite-utils/releases/tag/4.1)
* **Tags:** `projects` | `python` | `sqlite` | `sqlite-utils` | `annotated-release-notes` | `ai-assisted-programming`