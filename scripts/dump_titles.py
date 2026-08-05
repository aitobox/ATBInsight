import os
import re
import json

POSTS_DIR = 'docs/blog/posts'
data = []

for filename in os.listdir(POSTS_DIR):
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(POSTS_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        continue
        
    title_match = re.search(r'^title:\s*(.+)$', match.group(1), re.MULTILINE)
    title = title_match.group(1).strip(" '\"") if title_match else filename
    
    data.append({"filename": filename, "title": title})

with open('post_titles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Dumped", len(data), "titles")
