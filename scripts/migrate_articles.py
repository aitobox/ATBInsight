import os
import glob
import shutil
import yaml

def generate_tags_and_categories(title, content):
    categories = ["深度研报"]
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
        
        new_filename = f"2026-08-04-{filename}"
        dest_path = os.path.join(dest_dir, new_filename)
        
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print(f"Successfully migrated {len(md_files)} articles to {dest_dir}")
    # Remove old directory
    shutil.rmtree(src_dir)

if __name__ == "__main__":
    migrate()
