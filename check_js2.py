import re
with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_完整后台大盘.html", "r", encoding="utf-8") as f:
    html = f.read()

match = re.search(r'<script>\s*// --- SPA Router Logic(.*?)</script>', html, re.DOTALL)
if match:
    js = match.group(1)
    with open("test2.js", "w", encoding="utf-8") as f:
        f.write(js)
