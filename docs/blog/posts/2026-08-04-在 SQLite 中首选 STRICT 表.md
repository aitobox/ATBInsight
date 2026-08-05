---
authors:
- aitoboxrobot
categories:
- 深度研报
date: '2026-08-04'
hide:
- navigation
tags:
- AI
- SQLite
title: 在 SQLite 中首选 STRICT 表
---
# 在 SQLite 中首选 STRICT 表

**背景与摘要：**
本文主要探讨了 SQLite 中常被低估的 **strict tables (严格表)** 特性。该特性通过强制实施严格的类型约束，能够有效防止常见的类型错误，例如将文本插入整数列或在建表时使用了无效的数据类型。尽管开启该功能会带来诸如向后兼容性受限以及迁移现有数据较麻烦等微小妥协，但作者认为，严格表在大幅提升数据完整性和消除潜在 Bug 方面具有不可替代的作用。

> **Summary:** SQLite's underrated **strict tables** feature enforces rigid typing to prevent common datatype errors—such as inserting text into integer columns or using invalid types upon table creation. While they come with minor trade-offs like backward-compatibility limits and migration friction, the author argues that strict tables significantly improve data integrity and eliminate subtle bugs.

---

## 简介

SQLite 有一个经常被低估的功能：[严格表 (strict tables)](https://sqlite.org/stricttables.html)。严格表有助于强制执行严格的数据类型，从而防止犯下诸如将文本放入整数列之类的错误。

> ## Introduction
> 
> SQLite has a feature that is often underrated: [strict tables](https://sqlite.org/stricttables.html). Strict tables help enforce rigid typing, preventing mistakes like putting text into integer columns. 

要创建一个严格表，只需在其定义末尾加上 `STRICT` 即可：

> To make a strict table, simply add `STRICT` to the end of its definition:

```sql
-CREATE TABLE people (name TEXT);
+CREATE TABLE people (name TEXT) STRICT;
```

---

## 严格表的优势

广义上讲，严格表有助于强制实施严格的数据类型，使 SQLite 的行为与其他传统的 SQL 引擎保持一致。

> ## Advantages of Strict Tables
> 
> Broadly, strict tables help enforce rigid types, aligning SQLite with the behavior of other traditional SQL engines.

### 1. 防止 Insert/Update 时的类型不匹配

默认情况下，SQLite 允许你将任何数据类型插入任何列中（例如，将文本放入 `INTEGER` 列）。严格表会拒绝这些不匹配的操作：

> ### 1. Prevents Type Mismatches on Insert/Update
> By default, SQLite allows you to insert any datatype into any column (e.g., putting text into an `INTEGER` column). Strict tables reject these mismatches:

```sql
-- 非严格表允许你在任何地方放置任何内容（运行良好）
CREATE TABLE people_nonstrict (age INTEGER);
INSERT INTO people_nonstrict (age) VALUES ('garbage');

-- 严格表会抛出错误，防止数据损坏
CREATE TABLE people_strict (age INTEGER) STRICT;
INSERT INTO people_strict (age) VALUES ('garbage');
-- => 错误: 无法将 TEXT 值存储在 INTEGER 列中
```

同样的验证规则也适用于 `UPDATE` 语句。然而，对于可以无损转换的值（比如将字符串 `'123'` 插入到整数列中），依然会自动被接受。

> This same validation applies to `UPDATE` statements. However, losslessly convertible values (like the string `'123'` being inserted into an integer column) are still accepted automatically.

### 2. 防止在建表时出现虚假的列类型

默认情况下，SQLite 在建表期间会默默接受无效或拼写错误的数据类型而不会抛出错误：

> ### 2. Prevents Bogus Column Types on Table Creation
> By default, SQLite accepts invalid or misspelled datatypes without throwing an error during table creation:

```sql
-- 尽管这些是无效的类型，SQLite 依然会静默接受
CREATE TABLE tbl (name GARBAGE);
CREATE TABLE tbl (name DATETIME);
CREATE TABLE tbl (name JSON);
```

添加 `STRICT` 会强制这些操作立即报错，确保开发者只能使用受支持的类型：`INT`、`INTEGER`、`REAL`、`TEXT`、`BLOB` 以及 `ANY`。此外，严格表要求必须为每个字段明确指定列类型。

> Appending `STRICT` forces these to error out immediately, ensuring developers only use supported types: `INT`, `INTEGER`, `REAL`, `TEXT`, `BLOB`, and `ANY`. Furthermore, strict tables require an explicit column type for every field.

### 3. 仍可通过 `ANY` 保持灵活性

如果你确实有意需要某一列接受多种类型的数据，即便是在严格表内部，你也可以使用 `ANY` 数据类型：

> ### 3. Still Allows Flexibility with `ANY`
> If you intentionally need a column to accept multiple types, you can use the `ANY` datatype, even inside a strict table:

```sql
CREATE TABLE tbl (value ANY) STRICT;

-- 以下所有操作都保持有效：
INSERT INTO tbl (value) VALUES (123);
INSERT INTO tbl (value) VALUES ('text');
INSERT INTO tbl (value) VALUES (12.34);
INSERT INTO tbl (value) VALUES (X'8647');
```

---

## 严格表的劣势

虽然严格表功能强大，但仍有几个缺点和边缘情况需要铭记在心：

> ## Disadvantages of Strict Tables
> 
> While strict tables are powerful, there are a few drawbacks and edge cases to keep in mind:

### 1. 无法轻松将现有表转换为 `STRICT`

目前，你无法通过执行 `ALTER` 语句将现有的表转换为严格表。相反，你必须手动迁移数据：

> ### 1. Cannot Convert Existing Tables to `STRICT` easily
> You cannot currently `ALTER` an existing table to make it strict. Instead, you must migrate the data manually:

```sql
-- 1. 使用期望的 schema 创建一个新的严格表
CREATE TABLE new_people (name TEXT) STRICT;

-- 2. 复制数据过来（如果现有数据违反了严格类型，则会失败）
INSERT INTO new_people SELECT * FROM people;

-- 3. 替换表名
DROP TABLE people;
ALTER TABLE new_people RENAME TO people;
```

### 2. SQLite 开发者的分歧

官方 SQLite 文档中有一篇名为 [“灵活类型的优势 (The Advantages Of Flexible Typing)”](https://sqlite.org/flextypegood.html) 的指南，该指南为动态类型在键值存储或导入杂乱的 CSV 文件等使用场景中进行了辩护。

> ### 2. The SQLite Developers Disagree
> The official SQLite documentation features a guide titled [“The Advantages Of Flexible Typing”](https://sqlite.org/flextypegood.html), defending dynamic typing for use cases like key-value stores or importing messy CSV files. 

### 3. 版本兼容性 (SQLite 3.37.0+)

严格表功能是在 [3.37.0 版本](https://sqlite.org/releaselog/3_37_0.html)（2021 年 11 月）中引入的。较旧版本的 SQLite 无法读取包含严格表的数据库，这会导致错误。

> ### 3. Version Compatibility (SQLite 3.37.0+)
> Strict tables were introduced in [version 3.37.0](https://sqlite.org/releaselog/3_37_0.html) (November 2021). Older versions of SQLite cannot read databases containing strict tables, resulting in an error.

### 4. 性能影响微乎其微

虽然严格表在写入时会执行额外的验证检查，但实际的基准测试表明，无论是在执行速度还是磁盘上的文件大小方面，都几乎看不到明显的差异。

> ### 4. Performance Impact is Negligible
> While strict tables perform extra validation checks during writes, real-world benchmarks show virtually no noticeable difference in execution speed or file size on disk.

---

## 结论

归根结底，严格表带来的好处远远超过了它的局限性。通过强制实施严格的类型约束，开发者从一开始就可以消除一整类隐蔽的 Bug，并显著提高数据的完整性。

> ## Conclusion
> 
> Ultimately, the benefits of strict tables far outweigh their limitations. By enforcing rigid types, developers can eliminate an entire category of subtle bugs and significantly improve data integrity from the start.
