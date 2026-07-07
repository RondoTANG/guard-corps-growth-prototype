import os

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/C端_作业详情.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

sidebar_html = """
    <!-- 原型全局侧边栏 (方便切换页面) -->
    <div class="fixed left-0 top-0 w-64 h-full bg-white shadow-[4px_0_24px_rgba(0,0,0,0.05)] border-r border-gray-100 z-[100] flex flex-col">
        <div class="p-5 border-b border-gray-100 bg-gray-50/50">
            <h2 class="text-sm font-bold text-gray-800 flex items-center"><i class="fas fa-layer-group text-dfred mr-2"></i>护卫军体系原型</h2>
            <p class="text-[10px] text-gray-500 mt-1">交互与逻辑批注版</p>
        </div>
        <div class="flex-1 overflow-y-auto p-4 space-y-1">
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-2 px-2 tracking-wider">C端应用 (APP端)</div>
            <a href="C端_成长体系规划介绍.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-file-powerpoint w-5"></i> 规划介绍 (PRD)</a>
            <a href="C端_个人中心.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-user-circle w-5"></i> 个人中心 (入口)</a>
            <a href="C端_成长中心大盘.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-medal w-5"></i> 成长中心大盘</a>
            <a href="C端_成长值明细.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-list-alt w-5"></i> 成长值明细</a>
            <a href="C端_作业大厅.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-tasks w-5"></i> 作业大厅</a>
            <a href="C端_作业详情.html" class="block px-3 py-2.5 rounded-lg text-xs bg-red-50 text-dfred font-bold transition flex items-center"><i class="fas fa-file-alt w-5"></i> 作业详情</a>
            
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-8 px-2 tracking-wider">B端管理 (PC端)</div>
            <a href="C端_护卫军后台功能导航页.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center"><i class="fas fa-desktop w-5"></i> 护卫军后台导航</a>
        </div>
    </div>

<div class="ml-64 flex gap-12 items-start w-full pl-10 pt-4">
"""

# Replace the body tag opening
content = content.replace('<body class="p-8 flex items-center justify-center min-h-screen">', '<body class="c-end-body bg-gray-50">\n' + sidebar_html)

# Add closing div for main content area before </body>
content = content.replace('</body>', '</div>\n</body>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
