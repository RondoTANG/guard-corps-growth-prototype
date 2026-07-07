import os
import re

directory = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型"
files_to_fix = [
    ("B端_成长数据健康度大盘.html", "成长数据大盘"),
    ("B端_等级规则与XP配置页.html", "成长规则配置"),
    ("B端_用户管理_XP干预页.html", "用户列表"),
    ("B端_系统设置_文章管理页.html", "文章管理")
]

# The active style is: class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu"

def clean_active_state(html):
    # First, find any <a> tags that have bg-[#3B82F6] and revert them to normal
    def replace_active(match):
        full_a = match.group(0)
        # Revert to standard classes
        # But we need to keep href and text
        inner_text = re.search(r'>([^<]+)</a>', full_a).group(1)
        href = re.search(r'href="([^"]+)"', full_a)
        href_val = href.group(1) if href else "#"
        return f'<a class="px-9 py-2.5 hover:text-white transition-colors" href="{href_val}">{inner_text}</a>'
        
    html = re.sub(r'<a[^>]+bg-\[#3B82F6\][^>]+>.*?</a>', replace_active, html)
    # Also clean up any other variants like bg-gray-700
    html = re.sub(r'<a[^>]+bg-gray-700[^>]+>.*?</a>', replace_active, html)
    return html

def set_active_state(html, target_text):
    # Find the link with exact target_text and set it to active
    # For user list, it might be <a ...>用户列表</a>
    def replace_target(match):
        full_a = match.group(0)
        inner_text = re.search(r'>([^<]+)</a>', full_a).group(1)
        href = re.search(r'href="([^"]+)"', full_a)
        href_val = href.group(1) if href else "#"
        if inner_text == target_text:
            return f'<a class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu" href="{href_val}">{inner_text}</a>'
        return full_a
    
    html = re.sub(r'<a class="px-9[^>]+>([^<]+)</a>', replace_target, html)
    return html

for filename, active_text in files_to_fix:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Extract sidebar
    sidebar_match = re.search(r'(<aside.*?</aside>)', html, re.DOTALL)
    if sidebar_match:
        sidebar = sidebar_match.group(1)
        sidebar = clean_active_state(sidebar)
        sidebar = set_active_state(sidebar, active_text)
        
        html = re.sub(r'<aside.*?</aside>', sidebar, html, flags=re.DOTALL)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed {filename}: highlighted '{active_text}'")
    else:
        print(f"Sidebar not found in {filename}")
