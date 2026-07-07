import re
import os

target_files = [
    "B端_等级规则与XP配置页.html",
    "B端_成长数据健康度大盘.html",
    "B端_XP资产流水明细表.html",
    "B端_用户管理_XP干预页.html"
]

# 1. Extract sidebar from the first file to build the Main Shell
with open(target_files[0], "r", encoding="utf-8") as f:
    base_html = f.read()

sidebar_match = re.search(r'(<!-- Sidebar -->.*?)</aside>', base_html, re.DOTALL)
if not sidebar_match:
    print("Could not find sidebar")
    exit(1)
sidebar_html = sidebar_match.group(1) + "</aside>"

# Modify sidebar links
sidebar_html = re.sub(
    r'<a href="#" class="px-9 py-2.5 hover:text-white transition-colors">用户列表</a>',
    r'<a href="B端_用户管理_XP干预页.html" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">用户列表</a>',
    sidebar_html
)
sidebar_html = re.sub(
    r'<a href="#" class="px-9 py-2.5 hover:text-white transition-colors">作业管理</a>',
    r'<a href="#" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">护卫军作业任务配置</a>',
    sidebar_html
)
sidebar_html = re.sub(
    r'<a href="#" class="px-9 py-2.5 hover:text-white transition-colors">审核管理列表</a>',
    r'<a href="#" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">审核管理列表</a>',
    sidebar_html
)
sidebar_html = re.sub(
    r'<a href="#" class="px-9 py-3 bg-\[\#3B82F6\] text-white font-bold">成长规则配置</a>',
    r'<a href="B端_等级规则与XP配置页.html" target="main-frame" onclick="setActive(this)" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu">成长规则配置</a>',
    sidebar_html
)

# We need to add "成长数据大盘" and "XP资产流水"
# Let's add them under 用户管理 or 护卫军作业管理?
# The user said: 成长规则配置, 用户列表, XP资产流水, 成长数据大盘, 护卫军作业任务配置, 审核管理列表
# Let's replace the entire "系统设置" or add them cleanly.

sidebar_html = sidebar_html.replace('<!-- 系统设置 -->', '''<!-- 核心业务导航 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                        <span class="font-bold text-gray-200">护卫军管理</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="B端_成长数据健康度大盘.html" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">成长数据大盘</a>
                        <a href="B端_等级规则与XP配置页.html" target="main-frame" onclick="setActive(this)" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu">成长规则配置</a>
                        <a href="B端_用户管理_XP干预页.html" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">用户列表</a>
                        <a href="B端_XP资产流水明细表.html" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">XP资产流水</a>
                        <a href="#" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">护卫军作业任务配置</a>
                        <a href="#" target="main-frame" onclick="setActive(this)" class="px-9 py-2.5 hover:text-white transition-colors menu-link">审核管理列表</a>
                    </div>
                </div>
<!-- 系统设置 -->''')


shell_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>东风护卫军 - 后台总控</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .style-scrollbar::-webkit-scrollbar {{ width: 6px; }}
        .style-scrollbar::-webkit-scrollbar-track {{ background: transparent; }}
        .style-scrollbar::-webkit-scrollbar-thumb {{ background-color: #4B5563; border-radius: 20px; }}
    </style>
    <script>
        function setActive(element) {{
            document.querySelectorAll('.menu-link').forEach(el => {{
                el.classList.remove('bg-[#3B82F6]', 'text-white', 'font-bold', 'active-menu');
                el.classList.add('hover:text-white');
            }});
            element.classList.remove('hover:text-white');
            element.classList.add('bg-[#3B82F6]', 'text-white', 'font-bold', 'active-menu');
        }}
    </script>
</head>
<body class="flex h-screen overflow-hidden text-gray-800 bg-gray-100">
    {sidebar_html}
    
    <main class="flex-1 h-full relative">
        <iframe name="main-frame" src="B端_等级规则与XP配置页.html" class="w-full h-full border-none"></iframe>
    </main>
</body>
</html>
"""

with open("B端_后台总控大盘_Iframe.html", "w", encoding="utf-8") as f:
    f.write(shell_html)

# 2. Strip sidebar from individual files
for file_name in target_files:
    if not os.path.exists(file_name): continue
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the sidebar
    content = re.sub(r'<!-- Sidebar -->.*?</aside>', '', content, flags=re.DOTALL)
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

print("Migration to Iframe architecture completed.")
