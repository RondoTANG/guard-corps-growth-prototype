import re

file_path = 'B端_等级规则与XP配置页.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
content = content.replace('XP 产出阀门', 'XP 发放规则及上限')
content = content.replace('降级软着陆规则', '降级跌幅限制规则')
content = content.replace('开启降级软着陆保护', '开启最大降幅限制保护')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated terms in B端_等级规则与XP配置页.html")
