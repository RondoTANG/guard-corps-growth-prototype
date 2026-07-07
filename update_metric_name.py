import os
import re

md_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘_开发指南.md"
html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

# Update MD
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

md_content = md_content.replace("大盘中提到的“活跃用户”", "大盘中提到的“成长活跃用户”")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

# Update HTML's injected markdown
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(
    r'(<script type="text/markdown" id="devGuideMarkdown">)(.*?)(</script>)',
    lambda m: f"{m.group(1)}\n{md_content}\n{m.group(3)}",
    html,
    flags=re.DOTALL
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated metric name in Dev Guide!")
