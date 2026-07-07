import os
import glob

html_files = [
    "C端_个人中心.html",
    "C端_成长中心大盘.html",
    "C端_成长值明细.html",
    "C端_作业大厅.html",
    "C端_护卫军后台功能导航页.html"
]

insert_html = '            <a href="C端_成长体系规划介绍.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-file-powerpoint w-5"></i> 规划介绍 (PRD)</a>'

search_str = '<div class="text-[10px] font-bold text-gray-400 mb-3 mt-2 px-2 tracking-wider">C端应用 (APP端)</div>'

base_dir = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/"

for f in html_files:
    filepath = os.path.join(base_dir, f)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if insert_html not in content and search_str in content:
            content = content.replace(search_str, search_str + '\n' + insert_html)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Patched {f}")
        else:
            print(f"Skipped {f} (already patched or search string not found)")
            
