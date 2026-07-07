import re
import glob

# 1. Read the B-end sidebar from B端_后台总控大盘_Iframe.html
with open('B端_后台总控大盘_Iframe.html', 'r', encoding='utf-8') as f:
    iframe_html = f.read()

match = re.search(r'(<aside class="w-64 bg-\[#313C48\].*?</aside>)', iframe_html, re.DOTALL)
if not match:
    print("Could not find the sidebar in B端_后台总控大盘_Iframe.html")
    exit(1)
base_sidebar = match.group(1)

# 2. Remove the "护卫军管理" group completely
# We find the group that contains <span class="font-bold text-gray-200">护卫军管理</span>
# The group starts with <!-- 核心业务导航 --> (or similar) or <div class="menu-group"> and ends with </div></div>
base_sidebar = re.sub(r'<!-- 核心业务导航 -->\s*<div class="menu-group">.*?<span class="font-bold text-gray-200">护卫军管理</span>.*?</div>\s*</div>', '', base_sidebar, flags=re.DOTALL)
# Also try without the comment in case I removed it
base_sidebar = re.sub(r'<div class="menu-group">\s*<div[^>]*>\s*<span class="font-bold text-gray-200">护卫军管理</span>.*?</div>\s*</div>', '', base_sidebar, flags=re.DOTALL)

# 3. Add missing items to respective groups
# In "统计分析": add <a href="B端_成长数据健康度大盘.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link">成长数据大盘</a>
# add <a href="B端_XP资产流水明细表.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link">XP资产流水</a>
stat_link_str = '<a href="B端_成长数据健康度大盘.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link">成长数据大盘</a>\n                        <a href="B端_XP资产流水明细表.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link">XP资产流水</a>\n                        '
base_sidebar = re.sub(r'(<span class="font-bold text-gray-200">统计分析</span>.*?<div class="flex flex-col">\s*)', r'\1' + stat_link_str, base_sidebar, flags=re.DOTALL)

# In "系统设置": add <a href="#" class="px-9 py-2.5 hover:text-white transition-colors menu-link">护卫军作业任务配置</a>
# (If not already there. It's not there. Let's add it at the top of the group.)
sys_link_str = '<a href="#" class="px-9 py-2.5 hover:text-white transition-colors menu-link">护卫军作业任务配置</a>\n                        '
base_sidebar = re.sub(r'(<span class="font-bold text-gray-200">系统设置</span>.*?<div class="flex flex-col">\s*)', r'\1' + sys_link_str, base_sidebar, flags=re.DOTALL)

# Make sure all existing links to the 4 files have the correct href and class structure
base_sidebar = base_sidebar.replace('target="main-frame"', '')
base_sidebar = base_sidebar.replace('onclick="setActive(this)"', '')
# Ensure active states are cleared
base_sidebar = re.sub(r'bg-\[#3B82F6\] text-white font-bold menu-link active-menu', 'hover:text-white transition-colors menu-link', base_sidebar)

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
    
    custom_sidebar = base_sidebar
    
    # Highlight the current one
    file_basename = file_path
    search_str = f'href="{file_basename}" class="px-9 py-2.5 hover:text-white transition-colors menu-link"'
    replace_str = f'href="{file_basename}" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu"'
    custom_sidebar = custom_sidebar.replace(search_str, replace_str)
    
    # Also handle the cases where they don't have menu-link class, like in original sidebar
    search_str2 = f'href="{file_basename}" class="px-9 py-2.5 hover:text-white transition-colors"'
    custom_sidebar = custom_sidebar.replace(search_str2, replace_str)

    # Now replace the existing aside in the file
    # Find existing aside and replace it
    new_content = re.sub(r'<aside class="w-64 bg-\[#313C48\].*?</aside>', custom_sidebar, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes made to {file_path}")

