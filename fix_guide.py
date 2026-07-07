import os

md_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘_开发指南.md"
html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

# Read original MD
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace wrong chart titles
md_content = md_content.replace(
    "图表【各党组织活跃与段位分布对比】的“自动”", 
    "图表【活跃与段位分布对比】的“自动”"
)
md_content = md_content.replace(
    "### 3.3 各党组织活跃与段位分布 (双Y轴图)", 
    "### 3.3 活跃与段位分布对比 (双Y轴图)"
)

# Write updated MD
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

# Update HTML's injected markdown
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

import re
# Regex to find <script type="text/markdown" id="devGuideMarkdown">...</script>
html = re.sub(
    r'(<script type="text/markdown" id="devGuideMarkdown">)(.*?)(</script>)',
    lambda m: f"{m.group(1)}\n{md_content}\n{m.group(3)}",
    html,
    flags=re.DOTALL
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed chart titles in Dev Guide!")
