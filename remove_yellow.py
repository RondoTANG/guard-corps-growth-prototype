import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove background yellow classes and adjust text color where necessary
html = html.replace(" bg-yellow-300 text-gray-700", "")
html = html.replace(" bg-yellow-300", "")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Yellow background removed.")
