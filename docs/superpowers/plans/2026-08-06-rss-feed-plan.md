# RSS Feed Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an RSS feed for the 50 most recent articles and an RSS link icon to the site header.

**Architecture:** Use the standard `mkdocs-rss-plugin` configured in `zensical.toml` to generate `rss.xml` during the build process, and override the MkDocs Material `header.html` partial to inject an RSS icon linking to the feed.

**Tech Stack:** Python, MkDocs, MkDocs Material, HTML/Jinja2

## Global Constraints

- Must output exactly the last 50 articles.
- Must filter to only include articles in `blog/posts/`.
- Must generate output file `rss.xml`.
- Link must appear next to the theme toggle in the header action area.

---

### Task 1: Install and Configure `mkdocs-rss-plugin`

**Files:**
- Modify: `/opt/aitobox/ATBInsight/zensical.toml`

**Interfaces:**
- Consumes: Site structure
- Produces: `rss.xml` generated at build time

- [ ] **Step 1: Install the plugin in the environment**

```bash
pip install mkdocs-rss-plugin
```

- [ ] **Step 2: Add plugin configuration to `zensical.toml`**

Add the following block to `zensical.toml` under the existing plugins:

```toml
[[plugins]]
name = "rss"
length = 50
match_path = ".*blog/posts/.*"
output_path = "rss.xml"
```

- [ ] **Step 3: Test feed generation**

```bash
source /home/aitobox/miniconda3/bin/activate ATBInsight && mkdocs build
```
Verify that `site/rss.xml` is successfully generated and no build errors occur.

- [ ] **Step 4: Commit**

```bash
git add zensical.toml
git commit -m "feat: configure mkdocs-rss-plugin for latest 50 posts"
```

### Task 2: Inject RSS Icon into Header

**Files:**
- Create: `/opt/aitobox/ATBInsight/overrides/partials/header.html`

**Interfaces:**
- Consumes: MkDocs Material base `header.html`
- Produces: Overridden header with RSS link icon

- [ ] **Step 1: Create the overridden `header.html` partial**

Create `/opt/aitobox/ATBInsight/overrides/partials/header.html` with the following content, which extends the base header block to inject the icon next to the source/theme toggle:

```html
{% extends "base.html" %}

{% block header %}
  {{ super() }}
  <script>
    // A lightweight JS approach to inject the icon since overriding the precise inner block of the header 
    // can be fragile across Material versions. We inject the RSS link next to the palette toggle.
    document.addEventListener("DOMContentLoaded", function() {
      var headerAction = document.querySelector(".md-header__source") || document.querySelector(".md-header__option");
      if (!headerAction) {
         // Fallback to inserting at the end of the inner header
         headerAction = document.querySelector(".md-header__inner");
      }
      
      if (headerAction) {
        var rssLink = document.createElement("a");
        rssLink.href = "/rss.xml";
        rssLink.title = "RSS 订阅";
        rssLink.className = "md-header__button md-icon";
        rssLink.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19 7.38 20 6.18 20C5 20 4 19 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.02c8.83 0 16 7.17 16 16h-3.38c0-6.97-5.65-12.62-12.62-12.62V4.02M4 9.84c5.61 0 10.16 4.55 10.16 10.16H10.8c0-3.75-3.05-6.8-6.8-6.8V9.84Z"/></svg>';
        
        var container = document.querySelector(".md-header__inner");
        if(container) {
           var existingIcons = container.querySelectorAll(".md-header__button");
           if (existingIcons.length > 0) {
               existingIcons[0].parentNode.insertBefore(rssLink, existingIcons[0]);
           } else {
               container.appendChild(rssLink);
           }
        }
      }
    });
  </script>
{% endblock %}
```
*Note: We use a JS injection to ensure we don't break the base MkDocs Material header layout, avoiding the need to copy hundreds of lines of original `header.html` template code.*

- [ ] **Step 2: Test the visual integration**

Run `mkdocs serve` and navigate to `http://localhost:8000` to visually confirm the RSS icon appears in the top header and links to `/rss.xml`.

- [ ] **Step 3: Commit**

```bash
git add overrides/partials/header.html
git commit -m "feat: add RSS link icon to site header"
```
