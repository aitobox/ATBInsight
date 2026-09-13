import os

def test_screener_skill_exists_and_synced():
    path_skills = "skills/article-screener/SKILL.md"
    path_agents = ".agents/skills/article-screener/SKILL.md"
    
    assert os.path.exists(path_skills), f"{path_skills} must exist"
    assert os.path.exists(path_agents), f"{path_agents} must exist"
    
    with open(path_skills, "r", encoding="utf-8") as f:
        content_skills = f.read()
    with open(path_agents, "r", encoding="utf-8") as f:
        content_agents = f.read()
        
    assert content_skills == content_agents, "Both SKILL.md files must remain in sync"
    
    # Persona check
    assert "Chief Editor" in content_skills
    assert "ATBInsight" in content_skills
    
    # Rejection criteria check
    assert "Strict Rejection Criteria" in content_skills
    assert "Digests / Roundups" in content_skills
    assert "Out-of-Scope Applied ML" in content_skills
    assert "Incremental Academic Fluff" in content_skills
    assert "Commercial PR" in content_skills
    assert "Political / Geopolitical" in content_skills
    
    # 4 Dimensions check
    assert "Technical Depth & Rigor" in content_skills
    assert "Core Domain Relevance" in content_skills
    assert "Engineering Value & Practical Insights" in content_skills
    assert "Originality & Thinking Quality" in content_skills
    
    # Threshold and Quota check
    assert "70" in content_skills
    assert "breakdown" in content_skills
    assert "verdict" in content_skills
    assert "Daily arXiv Quota" in content_skills
    assert "Top 3 by score" in content_skills

