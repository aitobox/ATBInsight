import os
import re
import yaml

POSTS_DIR = 'docs/blog/posts'
ARCHIVE_FILE = 'docs/archive.md'

def main():
    posts = []
    
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
        
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError:
            continue
            
        if not fm or 'date' not in fm:
            continue
            
        date_str = str(fm['date'])
        title = fm.get('title', filename.replace('.md', ''))
        
        posts.append((date_str, title, filename))
        
    posts.sort(key=lambda x: x[0], reverse=True)
    
    lines = [
        "# 文章归档",
        "",
        "这里按发布日期整理了所有的历史文章，方便您按时间线回顾动态。",
        ""
    ]
    
    current_month = ""
    for date_str, title, filename in posts:
        # Extract YYYY-MM
        month = date_str[:7] if len(date_str) >= 7 else date_str
        if month != current_month:
            lines.append(f"## {month}")
            lines.append("")
            current_month = month
            
        lines.append(f"- **{date_str}**: [{title}](blog/posts/{filename})")
        
    with open(ARCHIVE_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Generated archive.md with {len(posts)} posts.")

if __name__ == "__main__":
    main()
