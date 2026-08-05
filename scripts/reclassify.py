import os
import re
import yaml

POSTS_DIR = 'docs/blog/posts'
ZENSICAL_TOML = 'zensical.toml'

file_to_cat = {
  "2026-08-04-累积和的渐近估计.md": "研究解读",
  "2026-08-04-金属比例的比率.md": "研究解读",
  "2026-08-04-智能体就是单子（但不是那种单子） ).md": "研究解读",
  "2026-08-04-引入 GPT‑Live：ChatGPT 语音功能的新时代.md": "产品发布",
  "2026-08-04-使用 Rust 重写 Bun.md": "工具教程",
  "2026-08-04-训练盒子 Poppy 第一部分：起步.md": "工具教程",
  "2026-08-04-主机战争已经失败.md": "商业动态",
  "2026-08-04-服务器上的 BMC 与一个令人意外的 USB 网络设备.md": "研究解读",
  "2026-08-04-多元论：后政治.md": "其他",
  "2026-08-04-诅咒电路6：反向雪崩振荡器.md": "研究解读",
  "2026-08-04-全新 GPT-5.6 家族：Luna、Terra 与 Sol.md": "产品发布",
  "2026-08-04-就是今天，OpenAI 搞砸了 ChatGPT Mac 应用.md": "商业动态",
  "2026-08-04-开箱：Zig.md": "工具教程",
  "2026-08-04-解决了detect_mismatch错误但问题依然存在.md": "工具教程",
  "2026-08-04-毫无悬念，潜在篡位者 Fidji Simo 离开 OpenAI.md": "商业动态",
  "2026-08-04-推出Muse_Spark_1.1.md": "产品发布",
  "2026-08-04-困局：当创作上的僵化成为累赘.md": "商业动态",
  "2026-08-04-约翰·特努斯应扭转苹果在广告泥潭中的滑坡.md": "商业动态",
  "2026-08-04-一种罕见的 DHCP 耗尽原因：“尖叫”的主机.md": "研究解读",
  "2026-08-04-点积：分量与几何定义.md": "研究解读",
  "2026-08-04-Apache_IfModule指令的常见陷阱.md": "工具教程",
  "2026-08-04-“机器人的权利”与 AI 奴役幻想.md": "其他",
  "2026-08-04-为不理解你的代码库辩护.md": "其他",
  "2026-08-04-在 SQLite 中首选 STRICT 表.md": "工具教程",
  "2026-08-04-本周包管理生态回顾：2026年7月11日.md": "工具教程",
  "2026-08-04-AI 2040 与智能狂热.md": "商业动态",
  "2026-08-04-阅读清单—2026年7月11日.md": "其他",
  "2026-08-04-吉尔布雷斯猜想的新进展.md": "研究解读",
  "2026-08-04-Benedict Evans 评全新 ChatGPT “超级应用”.md": "商业动态",
  "2026-08-04-围绕“ChatGPT Classic”的困惑.md": "商业动态",
  "2026-08-04-法律的可预测性有多高？.md": "其他",
  "2026-08-04-OpenAI泡沫.md": "商业动态",
  "2026-08-04-xai-org_grok-build现已开源.md": "产品发布",
  "2026-08-04-Mermaid转Unicode框线艺术_grok-mermaid.md": "工具教程",
  "2026-08-04-带回终端机：实体媒体的愿景.md": "其他",
  "2026-08-04-早期研究版Unix的exec命令行参数大小限制.md": "研究解读",
  "2026-08-04-小工具评测：Thermal Master DV2 - 红外线观鸟望远镜 ★★★★½.md": "其他",
  "2026-08-04-关于控制面板扩展中指针截断的推测.md": "研究解读",
  "2026-08-04-Inkling：我们的开放权重模型.md": "产品发布",
  "2026-08-04-中国几乎已经追平：美国不会“赢得”AI战，而是应该这么做.md": "商业动态",
  "2026-08-04-谁在害怕中国模型？.md": "商业动态",
  "2026-08-04-我与理性主义者社区的决裂.md": "其他",
  "2026-08-04-Ubuntu26.04关机公告和wall命令失效问题.md": "工具教程",
  "2026-08-04-每周更新513：用Claude武装家庭网络.md": "工具教程",
  "2026-08-04-熟练制作文档.md": "工具教程",
  "2026-08-04-阅读清单：2026年7月25日.md": "其他",
  "2026-08-04-在RTX3090上对Qwen3.6_35BMoE进行基准测试.md": "研究解读",
  "2026-08-04-那些年我们终于找到的缺失防火墙规则.md": "工具教程",
  "2026-08-04-将TCP连接分配给Linux流量控制的Flows.md": "工具教程",
  "2026-08-04-Pluralistic：疯狂的亿万富翁及其综合征 (2026年7月16日).md": "其他",
  "2026-08-04-政治记者总是错的吗？.md": "其他",
  "2026-08-04-为什么 OpenAI 的 GPT-2 权重能击败我的？第二部分：错误修复.md": "研究解读",
  "2026-08-04-为什么所有人都在试图制造固态电池？.md": "研究解读",
  "2026-08-04-Pluralistic：监视定价能想到的最愚蠢的借口（2026年7月30日）.md": "其他",
  "2026-08-04-所以你想用植物来降低室内二氧化碳.md": "其他",
  "2026-08-04-寻找AppleUpgrade的陷阱.md": "研究解读",
  "2026-08-04-买那个电视流媒体棒之前请先读读这篇文章.md": "其他",
  "2026-08-04-为什么 OpenAI 的 GPT-2 权重能击败我的？第3部分：测试过度训练.md": "研究解读",
  "2026-08-04-商业智能泔水：企业采用 AI 是如何滋生职场平庸的.md": "商业动态",
  "2026-08-04-LLM 聊天补全服务器 0.1a0.md": "产品发布"
}

def main():
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
        
        fm = yaml.safe_load(fm_text)
        if not fm: continue
        
        new_cat = file_to_cat.get(filename, "其他")
        fm['categories'] = [new_cat]
        
        new_fm_text = yaml.dump(fm, allow_unicode=True, default_flow_style=False)
        new_content = f"---\n{new_fm_text}---\n{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    print("Updated categories.")
    
    # Update zensical.toml nav
    with open(ZENSICAL_TOML, 'r', encoding='utf-8') as f:
        config = f.read()
    
    old_nav = '''nav = [
  {"首页" = "index.md"},
  {"深度研报" = "blog/category/深度研报.md"},
  {"标签浏览" = "tags.md"}
]'''
    new_nav = '''nav = [
  {"首页" = "index.md"},
  {"产品发布" = "blog/category/产品发布.md"},
  {"工具教程" = "blog/category/工具教程.md"},
  {"研究解读" = "blog/category/研究解读.md"},
  {"商业动态" = "blog/category/商业动态.md"},
  {"其他" = "blog/category/其他.md"},
  {"标签浏览" = "tags.md"}
]'''
    
    config = config.replace(old_nav, new_nav)
    with open(ZENSICAL_TOML, 'w', encoding='utf-8') as f:
        f.write(config)

if __name__ == "__main__":
    main()
