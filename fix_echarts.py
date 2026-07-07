with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. Fix the Tooltip string
# The actual string in the file has `<` and `>` literal.
old_tooltip = '<b>统计规则：</b><br/>• <b>作业通过率</b> = 审核通过的作业数 / 该段位提交的总作业数<br/>• <b>评优率(加码)</b> = 获得加码奖励(评优)的作业数 / 审核通过的作业数'
new_tooltip = '<b>统计规则：</b><br/>• <b>任务参与率</b> = 该段位提交过作业的用户数 / 该段位总用户数<br/>• <b>作业通过率</b> = 审核通过的作业数 / 该段位提交的总作业数'
content = content.replace(old_tooltip, new_tooltip)

# Let's also fix the broken tooltip we created earlier at line 260 just in case
bad_tooltip = '<b>任务参与率</b> = 该段位提交过作业的用户数 / 该段位总用户数<br/>• <b>任务参与率</b> = 该段位审核通过的作业数 / 该段位提交的总作业数'
content = content.replace(bad_tooltip, new_tooltip.replace('<b>统计规则：</b><br/>• ', ''))

# 2. Fix the ECharts JS script at the bottom
# It looks like:
# legend: {
#   data: ['...', '...']
# }
# ...
# series: [
#   {
#     name: '...',
#     type: 'bar',
#     data: [65, 82, 91, 98]
#   },
#   {
#     name: '...',
#     type: 'bar',
#     data: [5, 12, 35, 62]
#   }
# ]

content = re.sub(r"data:\s*\['[^']*',\s*'[^']*'\]", "data: ['任务参与率', '作业通过率']", content)

# Name attributes in series
content = re.sub(r"name:\s*'[^']*',\s*type:\s*'bar',\s*itemStyle:\s*\{\s*color:\s*'#3b82f6'\s*\},", 
                 "name: '任务参与率',\n                            type: 'bar',\n                            itemStyle: { color: '#3b82f6' },", content)
content = re.sub(r"name:\s*'[^']*',\s*type:\s*'bar',\s*itemStyle:\s*\{\s*color:\s*'#f59e0b'\s*\},", 
                 "name: '作业通过率',\n                            type: 'bar',\n                            itemStyle: { color: '#f59e0b' },", content)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ECharts completely fixed.")
