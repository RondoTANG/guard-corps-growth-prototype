import re
with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_完整后台大盘.html", "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
with open("test.js", "w", encoding="utf-8") as f:
    f.write("\n".join(scripts))
