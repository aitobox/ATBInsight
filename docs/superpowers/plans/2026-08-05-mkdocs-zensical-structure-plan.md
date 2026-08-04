# Zensical Site Restructuring Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure project documentation into Zensical / MkDocs Material structure (`docs/blog/posts/`), migrate existing articles with YAML Front Matter metadata (`title`, `date`, `authors`, `categories`, `tags`), configure `mkdocs.yml`, and update `src/main.py` pipeline output logic.

**Architecture:** 
- Config: `mkdocs.yml` (Zensical / MkDocs Material with blog plugin enabled)
- Directory: `docs/index.md` (homepage), `docs/blog/posts/YYYY-MM-DD-title.md` (articles)
- Pipeline: `src/main.py` and `src/robots/llm_robot.py` for Front Matter generation and blog posts routing.

---

### Task 1: Create `mkdocs.yml` and `docs/index.md` Homepage

**Files:**
- Create: `mkdocs.yml`
- Create: `docs/index.md`
- Test: `tests/test_site_config.py`

- [ ] **Step 1: Write failing test**

```python
import os
import yaml

def test_mkdocs_config_and_index_exist():
    assert os.path.exists("mkdocs.yml")
    assert os.path.exists("docs/index.md")
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    assert config["site_name"] == "ATBInsight"
    assert "blog" in [p if isinstance(p, str) else list(p.keys())[0] for p in config.get("plugins", [])]
```

- [ ] **Step 2: Run test to verify failure**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_site_config.py -v"`
Expected: FAIL

- [ ] **Step 3: Create `mkdocs.yml` and `docs/index.md`**

Write `mkdocs.yml`:
```yaml
site_name: ATBInsight
site_url: https://aitobox.github.io/ATBInsight/
site_description: AI Insight Pipeline & Tech Blog

theme:
  name: material
  language: zh
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: 切换到暗黑模式
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: 切换到浅色模式
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.top
    - search.suggest
    - search.highlight

plugins:
  - search
  - blog:
      post_dir: docs/blog/posts
      archive: true
      categories: true
      authors: true

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.inlinehilite
  - pymdownx.arithmatex:
      generic: true
  - tables
  - attr_list
```

Write `docs/index.md`:
```markdown
# 欢迎来到 ATBInsight

ATBInsight 是一个自动化的 AI 科技资讯与技术研报平台。

最新动态请关注 [博客动态区](blog/index.md)。
```

- [ ] **Step 4: Run test to verify pass**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_site_config.py -v"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add mkdocs.yml docs/index.md tests/test_site_config.py
git commit -m "feat: add mkdocs.yml config and docs/index.md homepage"
```

---

### Task 2: Migrate Articles and Inject YAML Front Matter

**Files:**
- Script: `scripts/migrate_articles.py`
- Target Dir: `docs/blog/posts/`
- Test: `tests/test_migration.py`

- [ ] **Step 1: Write failing test**

```python
import os
import glob
import yaml

def test_migrated_articles_frontmatter():
    posts = glob.glob("docs/blog/posts/*.md")
    assert len(posts) > 0, "No migrated posts found in docs/blog/posts/"
    for p in posts[:5]:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        assert content.startswith("---")
        parts = content.split("---", 2)
        assert len(parts) >= 3
        fm = yaml.safe_load(parts[1])
        assert "title" in fm
        assert "date" in fm
        assert "authors" in fm
        assert "categories" in fm
        assert "tags" in fm
```

- [ ] **Step 2: Run test to verify failure**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_migration.py -v"`
Expected: FAIL

- [ ] **Step 3: Write migration script and execute**

Write `scripts/migrate_articles.py`:
```python
import os
import glob
import re
import shutil
import yaml

def generate_tags_and_categories(title, content):
    categories = ["技术研报"]
    tags = []
    
    # 关键字推断标签
    kw_map = {
        "AI": "AI",
        "OpenAI": "OpenAI",
        "GPT": "GPT",
        "Claude": "Claude",
        "Grok": "xAI",
        "Rust": "Rust",
        "Zig": "Zig",
        "Linux": "Linux",
        "SQLite": "SQLite",
        "电池": "硬件",
        "单子": "函数式编程",
        "振荡器": "硬件电路",
        "DHCP": "网络",
        "概率": "数学",
        "比例": "数学",
        "估计": "数学",
    }
    
    for kw, tag in kw_map.items():
        if kw.lower() in title.lower() or kw.lower() in content.lower():
            if tag not in tags:
                tags.append(tag)
                
    if not tags:
        tags = ["科技解构"]
        
    return categories, tags

def migrate():
    src_dir = "docs/insight/2026-08-04"
    dest_dir = "docs/blog/posts"
    img_src = os.path.join(src_dir, "images")
    img_dest = os.path.join(dest_dir, "images")
    
    os.makedirs(dest_dir, exist_ok=True)
    
    # 迁移图片
    if os.path.exists(img_src):
        os.makedirs(img_dest, exist_ok=True)
        for img in glob.glob(os.path.join(img_src, "*")):
            shutil.copy2(img, os.path.join(img_dest, os.path.basename(img)))
            
    # 迁移 Markdown 文件
    md_files = glob.glob(os.path.join(src_dir, "*.md"))
    for fpath in md_files:
        filename = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 提取标题
        title = filename.replace(".md", "")
        for line in content.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
                
        categories, tags = generate_tags_and_categories(title, content)
        
        front_matter = {
            "title": title,
            "date": "2026-08-04",
            "authors": ["aitoboxrobot"],
            "categories": categories,
            "tags": tags
        }
        
        fm_str = yaml.dump(front_matter, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{fm_str}---\n\n{content}"
        
        # 处理图片相对路径修复
        new_content = new_content.replace("./images/", "./images/")
        
        new_filename = f"2026-08-04-{filename}"
        dest_path = os.path.join(dest_dir, new_filename)
        
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print(f"Successfully migrated {len(md_files)} articles to {dest_dir}")

if __name__ == "__main__":
    migrate()
```

Run migration script:
`bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/migrate_articles.py"`

Clean up old `docs/insight/2026-08-04` folder.

- [ ] **Step 4: Run test to verify pass**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_migration.py -v"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add docs/blog/posts/ scripts/migrate_articles.py tests/test_migration.py
git rm -r docs/insight/2026-08-04/
git commit -m "feat: migrate insight articles to docs/blog/posts with Front Matter"
```

---

### Task 3: Update Main Pipeline (`src/main.py`) for Blog Posts Routing

**Files:**
- Modify: `src/main.py`
- Modify: `tests/test_main.py`

- [ ] **Step 1: Update `src/main.py` to route outputs to `docs/blog/posts/YYYY-MM-DD-title.md` with Front Matter**

- [ ] **Step 2: Update unit test `tests/test_main.py`**

- [ ] **Step 3: Run full pytest suite**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest -v"`
Expected: ALL PASS

- [ ] **Step 4: Commit**

```bash
git add src/main.py tests/test_main.py
git commit -m "feat: update main pipeline to output blog posts with Front Matter"
```
