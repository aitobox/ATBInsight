# Lobste.rs is Now Running on SQLite

## Summary
The tech community platform **Lobsters** has successfully completed its migration from MariaDB to SQLite. Following years of evaluation and initial plans for PostgreSQL, the Rails-based site now operates on a single VPS, achieving reduced CPU and memory usage, enhanced performance, and halved hosting costs.

---

## Migration Overview

The community site [Lobsters](https://lobste.rs) has been planning a migration away from MariaDB [since August 2018](https://github.com/lobsters/lobsters/issues/539#issuecomment-4959857588). While they originally targeted PostgreSQL, the team decided to [investigate SQLite](https://github.com/lobsters/lobsters/issues/539#issuecomment-2964114295) instead. 

After completing the migration over the weekend, the team considers the setup stable and envisions it as the permanent architecture for the site moving forward:

> "SQLite seems to have passed with flying colors: CPU usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the VPS cost once MariaDB VPS is taken down."

## Architecture & Database Breakdown

The Lobsters Rails application now runs on a single VPS, utilizing multiple SQLite database files tailored to specific tasks:

* **Primary Content Database:** ~3.8 GB
* **Cache Database:** ~1.1 GB
* **Queue Database:** ~218 MB
* **Rack::Attack Database:** ~555 MB (and growing), utilized by the [Rack::Attack](https://github.com/rack/rack-attack) middleware for blocking and throttling abusive requests.

## Technical Details

Comprehensive details can be found in the [Lobste.rs discussion thread](https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite) and the [SQLite migration PR](https://github.com/lobsters/lobsters/pull/1927) by Thomas Dziedzic. 

The primary pull request added 735 lines and removed 593 lines across 30 commits and 188 files, building upon foundational earlier work in pull requests [#1705](https://github.com/lobsters/lobsters/pull/1705), [#1871](https://github.com/lobsters/lobsters/pull/1871), and [#1924](https://github.com/lobsters/lobsters/pull/1924).

This serves as a compelling case study and a strong reminder of what can be accomplished using just a single server and SQLite.

---

**Tags:** [migrations](https://simonwillison.net/tags/migrations) | [ops](https://simonwillison.net/tags/ops) | [rails](https://simonwillison.net/tags/rails) | [sqlite](https://simonwillison.net/tags/sqlite) | [lobsters](https://simonwillison.net/tags/lobsters)