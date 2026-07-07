import re

config_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"
new_page_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"

with open(config_path, "r", encoding="utf-8") as f:
    config_html = f.read()

# Extract sidebar from config page
match = re.search(r'(<aside.*?</aside>)', config_html, re.DOTALL)
if match:
    sidebar = match.group(1)
    # Modify sidebar to highlight "文章管理" instead of "成长规则配置"
    
    # First, unhighlight "成长规则配置"
    sidebar = sidebar.replace(
        '<a class="px-9 py-3 hover:text-white transition-colors menu-link" href="B端_等级规则与XP配置页.html">成长规则配置</a>',
        '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_等级规则与XP配置页.html">成长规则配置</a>'
    )
    # And remove any active styles if there were any (it seems menu-link had active styles maybe?)
    # Wait, in config page, it was:
    # <a class="px-9 py-3 hover:text-white transition-colors menu-link" href="B端_等级规则与XP配置页.html">成长规则配置</a>
    # with CSS for menu-link
    
    # Now highlight "文章管理"
    sidebar = sidebar.replace(
        '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_系统设置_文章管理页.html">文章管理</a>',
        '<a class="px-9 py-3 hover:text-white transition-colors menu-link bg-gray-700 font-bold border-l-4 border-dfred" href="B端_系统设置_文章管理页.html">文章管理</a>'
    )

    with open(new_page_path, "r", encoding="utf-8") as f:
        new_html = f.read()
    
    # Replace sidebar in new page
    new_html = re.sub(r'<aside.*?</aside>', sidebar, new_html, flags=re.DOTALL)
    
    with open(new_page_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Sidebar synced!")
else:
    print("Sidebar not found in config page.")
