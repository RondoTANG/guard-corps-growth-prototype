import re

source_html = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_完整后台大盘.html"
target_html = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

with open(source_html, "r") as f:
    source_content = f.read()

aside_start = source_content.find('<aside class="w-64 bg-[#313C48]')
aside_end = source_content.find('</aside>') + len('</aside>')

if aside_start != -1 and aside_end != -1:
    aside_html = source_content[aside_start:aside_end]
    
    with open(target_html, "r") as f:
        target_content = f.read()
    
    inject_marker = '<div class="flex h-screen overflow-hidden bg-gray-50 font-sans">'
    
    if target_content.find(inject_marker) != -1:
        target_content = target_content.replace(
            inject_marker,
            inject_marker + "\n    " + aside_html + "\n"
        )
        with open(target_html, "w") as f:
            f.write(target_content)
        print("Successfully injected aside menu!")
    else:
        print("Error: Could not find inject marker in target HTML.")
else:
    print("Error: Could not find aside in source HTML.")

