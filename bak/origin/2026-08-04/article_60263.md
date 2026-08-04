# Prefer STRICT Tables in SQLite

> **Summary:** SQLite's underrated **strict tables** feature enforces rigid typing to prevent common datatype errors—such as inserting text into integer columns or using invalid types upon table creation. While they come with minor trade-offs like backward-compatibility limits and migration friction, the author argues that strict tables significantly improve data integrity and eliminate subtle bugs.

---

## Introduction

SQLite has a feature that is often underrated: [strict tables](https://sqlite.org/stricttables.html). Strict tables help enforce rigid typing, preventing mistakes like putting text into integer columns. 

To make a strict table, simply add `STRICT` to the end of its definition:

```sql
-CREATE TABLE people (name TEXT);
+CREATE TABLE people (name TEXT) STRICT;
```

---

## Advantages of Strict Tables

Broadly, strict tables help enforce rigid types, aligning SQLite with the behavior of other traditional SQL engines.

### 1. Prevents Type Mismatches on Insert/Update
By default, SQLite allows you to insert any datatype into any column (e.g., putting text into an `INTEGER` column). Strict tables reject these mismatches:

```sql
-- Non-strict tables let you put anything anywhere (works fine)
CREATE TABLE people_nonstrict (age INTEGER);
INSERT INTO people_nonstrict (age) VALUES ('garbage');

-- Strict tables throw an error, preventing data corruption
CREATE TABLE people_strict (age INTEGER) STRICT;
INSERT INTO people_strict (age) VALUES ('garbage');
-- => error: cannot store TEXT value in INTEGER column
```

This same validation applies to `UPDATE` statements. However, losslessly convertible values (like the string `'123'` being inserted into an integer column) are still accepted automatically.

### 2. Prevents Bogus Column Types on Table Creation
By default, SQLite accepts invalid or misspelled datatypes without throwing an error during table creation:

```sql
-- SQLite accepts these silently, despite being invalid types
CREATE TABLE tbl (name GARBAGE);
CREATE TABLE tbl (name DATETIME);
CREATE TABLE tbl (name JSON);
```

Appending `STRICT` forces these to error out immediately, ensuring developers only use supported types: `INT`, `INTEGER`, `REAL`, `TEXT`, `BLOB`, and `ANY`. Furthermore, strict tables require an explicit column type for every field.

### 3. Still Allows Flexibility with `ANY`
If you intentionally need a column to accept multiple types, you can use the `ANY` datatype, even inside a strict table:

```sql
CREATE TABLE tbl (value ANY) STRICT;

-- All of these remain valid:
INSERT INTO tbl (value) VALUES (123);
INSERT INTO tbl (value) VALUES ('text');
INSERT INTO tbl (value) VALUES (12.34);
INSERT INTO tbl (value) VALUES (X'8647');
```

---

## Disadvantages of Strict Tables

While strict tables are powerful, there are a few drawbacks and edge cases to keep in mind:

### 1. Cannot Convert Existing Tables to `STRICT` easily
You cannot currently `ALTER` an existing table to make it strict. Instead, you must migrate the data manually:

```sql
-- 1. Create a new strict table with the desired schema
CREATE TABLE new_people (name TEXT) STRICT;

-- 2. Copy data over (will fail if existing data violates strict types)
INSERT INTO new_people SELECT * FROM people;

-- 3. Swap the tables
DROP TABLE people;
ALTER TABLE new_people RENAME TO people;
```

### 2. The SQLite Developers Disagree
The official SQLite documentation features a guide titled [“The Advantages Of Flexible Typing”](https://sqlite.org/flextypegood.html), defending dynamic typing for use cases like key-value stores or importing messy CSV files. 

### 3. Version Compatibility (SQLite 3.37.0+)
Strict tables were introduced in [version 3.37.0](https://sqlite.org/releaselog/3_37_0.html) (November 2021). Older versions of SQLite cannot read databases containing strict tables, resulting in an error.

### 4. Performance Impact is Negligible
While strict tables perform extra validation checks during writes, real-world benchmarks show virtually no noticeable difference in execution speed or file size on disk.

---

## Conclusion

Ultimately, the benefits of strict tables far outweigh their limitations. By enforcing rigid types, developers can eliminate an entire category of subtle bugs and significantly improve data integrity from the start.