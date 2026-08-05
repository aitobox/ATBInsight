import os
import re
import yaml
from datetime import datetime

POSTS_DIR = 'docs/blog/posts'
INDEX_FILE = 'docs/index.md'

def main():
    daily_best = {} # date -> (title, filename, length)
    
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if not match:
            continue
            
        fm_text = match.group(1)
        body = match.group(2)
        
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError:
            continue
            
        if not fm or 'date' not in fm:
            continue
            
        date_str = str(fm['date'])
        title = fm.get('title', filename.replace('.md', ''))
        body_length = len(body.strip())
        
        # Keep the longest article as the "best" one for that day
        if date_str not in daily_best or body_length > daily_best[date_str][2]:
            daily_best[date_str] = (title, filename, body_length)
            
    # Format headlines sorted by date descending
    headlines = []
    for date_str in sorted(daily_best.keys(), reverse=True):
        title, filename, _ = daily_best[date_str]
        url = f"blog/posts/{filename}"
        headlines.append(f"- **{date_str}**: [{title}]({url})")
        
    headlines_text = "\n".join(headlines)
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    # Update the link
    index_content = re.sub(
        r'\[博客动态区\]\([^)]+\)', 
        '[博客动态区](tags.md)', 
        index_content
    )
    
    # Inject 每日头条
    marker = "## 每日头条"
    if marker in index_content:
        # replace everything after marker
        base_content = index_content.split(marker)[0]
        new_content = f"{base_content}{marker}\n\n{headlines_text}\n"
    else:
        new_content = f"{index_content}\n\n{marker}\n\n{headlines_text}\n"
        
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated index.md with daily headlines ({len(daily_best)} days).")

if __name__ == "__main__":
    main()
