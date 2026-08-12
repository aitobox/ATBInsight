import os
import re
import yaml
from src.robots.llm_robot import _chat_completion_with_fallback

POSTS_DIR = 'docs/blog/posts'
VALID_CATEGORIES = ["产品发布", "工具教程", "研究解读", "商业动态", "arXiv论文", "其他"]

def classify_article(title: str, content: str) -> str:
    # Check if article originates from or references arXiv paper
    if "arxiv" in content.lower() or "arxiv" in title.lower() or "arxiv.org" in content.lower():
        return "arXiv论文"

    system_prompt = (
        "You are an expert technical blog editor. Categorize the given article into EXACTLY ONE of the following 6 categories:\n"
        "- 产品发布 (Product releases, new versions, model releases)\n"
        "- 工具教程 (Tutorials, guides, how-to, developer tooling, code practices)\n"
        "- 研究解读 (Deep dives, benchmarks, technical research, architecture analysis, science/math paper breakdowns)\n"
        "- 商业动态 (Industry news, business analysis, tech economics, market trends)\n"
        "- arXiv论文 (Academic research papers, preprints, arXiv technical papers)\n"
        "- 其他 (General essays, book reviews, history, culture, or miscellaneous)\n\n"
        "Output ONLY the category name verbatim. Nothing else."
    )
    user_prompt = f"Title: {title}\nContent snippet:\n{content[:1500]}"
    try:
        res = _chat_completion_with_fallback([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ], temperature=0.1, timeout=15).strip()
        for cat in VALID_CATEGORIES:
            if cat in res:
                return cat
    except Exception as e:
        print(f"Classification failed for {title}: {e}")
    return "其他"

def main():
    if not os.path.exists(POSTS_DIR):
        print("No posts directory found.")
        return

    reclassified_count = 0
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
            
        if not isinstance(fm, dict):
            continue
            
        title = fm.get('title', filename.replace('.md', ''))
        current_cats = fm.get('categories') or []
        
        is_arxiv = "arxiv" in content.lower() or "arxiv" in title.lower() or "arxiv.org" in content.lower()

        # Re-classify if categories is missing, invalid, only contains "深度研报", OR if it is an arXiv paper not yet categorized as arXiv论文
        if not current_cats or current_cats == ['深度研报'] or any(c not in VALID_CATEGORIES for c in current_cats) or (is_arxiv and current_cats != ['arXiv论文']):
            cat = classify_article(title, content)
            fm['categories'] = [cat]
            reclassified_count += 1
            print(f"Categorized '{title}' -> [{cat}]")
            
            new_fm_text = yaml.dump(fm, allow_unicode=True, default_flow_style=False)
            new_content = f"---\n{new_fm_text}---\n{body}"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

    print(f"Auto-classification finished. Re-classified {reclassified_count} posts.")

if __name__ == "__main__":
    main()
