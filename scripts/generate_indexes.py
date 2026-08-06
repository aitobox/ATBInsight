import os
import re
import yaml
from collections import defaultdict

POSTS_DIR = 'docs/blog/posts'
CATEGORY_DIR = 'docs/blog/category'
TAGS_FILE = 'docs/tags.md'

def main():
    if os.path.exists(CATEGORY_DIR):
        import shutil
        shutil.rmtree(CATEGORY_DIR)
    os.makedirs(CATEGORY_DIR)

    categories = defaultdict(list)
    tags = defaultdict(list)

    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse front matter
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if not match:
            continue
            
        fm_text = match.group(1)
        body = match.group(2)
        
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError:
            continue
            
        if not isinstance(fm, dict):
            continue
            
        title = fm.get('title', filename.replace('.md', ''))
        url = f"../posts/{filename}" # Relative to category page
        tag_url = f"blog/posts/{filename}" # Relative to tags.md (which is in docs/)
        
        for cat in fm.get('categories') or []:
            categories[cat].append((title, url))
            
        for tag in fm.get('tags') or []:
            tags[tag].append((title, tag_url))
            
        # Inject hide: [navigation] if not present
        if 'hide' not in fm or 'navigation' not in (fm.get('hide') or []):
            if 'hide' not in fm:
                fm['hide'] = []
            if not isinstance(fm['hide'], list):
                fm['hide'] = [fm['hide']]
            if 'navigation' not in fm['hide']:
                fm['hide'].append('navigation')
                
                # Rewrite front matter
                new_fm_text = yaml.dump(fm, allow_unicode=True, default_flow_style=False)
                new_content = f"---\n{new_fm_text}---\n{body}"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    # Generate category pages
    for cat, posts in categories.items():
        cat_file = os.path.join(CATEGORY_DIR, f"{cat}.md")
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntitle: {cat}\n---\n\n# {cat}\n\n")
            for title, url in posts:
                f.write(f"- [{title}]({url})\n")
                
    # Generate tags page
    with open(TAGS_FILE, 'w', encoding='utf-8') as f:
        f.write("---\ntitle: 标签浏览\n---\n\n# 标签浏览\n\n")
        # Sort tags alphabetically
        for tag in sorted(tags.keys()):
            f.write(f"## {tag}\n\n")
            for title, url in tags[tag]:
                f.write(f"- [{title}]({url})\n")
            f.write("\n")

if __name__ == "__main__":
    main()
