import os
import re

md_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘_开发指南.md"
html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

# Append new section to MD
new_content = """
---

## 5. 核心交互规范与字段统计说明

### 5.1 左侧树容器自适应与拖拽缩放 (Resizable Sidebar)
- **拖拽伸缩**：由于党组织名称可能出现极长的情况，左侧组织架构树容器右边界需提供拖拽条（Resizer）。用户鼠标按住后可左右拖拽以调节容器宽度。
- **边界限制**：建议最小宽度限制为 `240px`，最大宽度限制为屏幕宽度的 `40%` 或 `500px`，超过部分文字允许 `ellipsis` 截断或横向滚动条。

### 5.2 核心漏斗转化指标口径
- **任务参与率** = `该段位在周期内提交过作业的用户数 / 该段位总用户数`
- **作业通过率** = `审核通过的作业数 / 该段位提交的总作业数`
*(注：前端需在相应图表的图例或提示词（Tooltip）中透出该统计公式，以降低业务理解成本。)*

### 5.3 活跃指标定义
- 大盘中提到的“活跃用户”，统一口径为：**在当前所选时间范围内，有任何 XP 获取或消耗行为的用户**（即只要有非“0”的账单流水产生即记为活跃，不含系统自动扣除）。
"""

with open(md_path, "a", encoding="utf-8") as f:
    f.write(new_content)

# Read updated MD
with open(md_path, "r", encoding="utf-8") as f:
    full_md = f.read()

# Inject into HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(
    r'(<script type="text/markdown" id="devGuideMarkdown">)(.*?)(</script>)',
    lambda m: f"{m.group(1)}\n{full_md}\n{m.group(3)}",
    html,
    flags=re.DOTALL
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Appended interactions successfully!")
