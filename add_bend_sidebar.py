import re
import glob

# 1. Read the B-end sidebar from B端_后台总控大盘_Iframe.html
with open('B端_后台总控大盘_Iframe.html', 'r', encoding='utf-8') as f:
    iframe_html = f.read()

# Extract the <aside> containing the dark sidebar
match = re.search(r'(<aside class="w-64 bg-\[#313C48\].*?</aside>)', iframe_html, re.DOTALL)
if match:
    b_end_sidebar = match.group(1)
else:
    print("Could not find the sidebar in B端_后台总控大盘_Iframe.html")
    exit(1)

# Files to update
b_end_files = [
    'B端_等级规则与XP配置页.html',
    'B端_用户管理_XP干预页.html',
    'B端_XP资产流水明细表.html',
    'B端_成长数据健康度大盘.html'
]

for file_path in b_end_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<aside class="w-64 bg-[#313C48]' in content:
        print(f"Sidebar already exists in {file_path}")
        continue
    
    # Customize the sidebar for each file to set the active menu item
    custom_sidebar = b_end_sidebar
    
    # Un-highlight all (remove active-menu and bg-[#3B82F6])
    custom_sidebar = re.sub(r'bg-\[#3B82F6\] text-white font-bold menu-link active-menu', 'hover:text-white transition-colors menu-link', custom_sidebar)
    
    # Highlight the current one
    file_basename = file_path
    
    # We find the href that matches the file and replace its classes
    # Original unhighlighted might look like:
    # href="B端_等级规则与XP配置页.html" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link"
    
    search_str = f'href="{file_basename}" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link"'
    replace_str = f'href="{file_basename}" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu"'
    
    custom_sidebar = custom_sidebar.replace(search_str, replace_str)
    
    # Remove all remaining target="main-frame" and onclick="setActive(this)" because we are doing direct navigation now
    custom_sidebar = custom_sidebar.replace('target="main-frame"', '')
    custom_sidebar = custom_sidebar.replace('onclick="setActive(this)"', '')
    
    # Insert before <main
    new_content = re.sub(r'(<main )', f'{custom_sidebar}\n\\1', content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

