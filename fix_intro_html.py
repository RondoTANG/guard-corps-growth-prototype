import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/C端_成长体系规划介绍.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove custom sidebar and main-content CSS
content = re.sub(r'/\* Sidebar Styles \*/.*?\.main-content \{.*?\}', '', content, flags=re.DOTALL)

# 2. Replace the sidebar HTML with the standard one
sidebar_html = """    <!-- 原型全局侧边栏 (方便切换页面) -->
    <div class="fixed left-0 top-0 w-64 h-full bg-white shadow-[4px_0_24px_rgba(0,0,0,0.05)] border-r border-gray-100 z-[100] flex flex-col">
        <div class="p-5 border-b border-gray-100 bg-gray-50/50">
            <h2 class="text-sm font-bold text-gray-800 flex items-center"><i class="fas fa-layer-group text-dfred mr-2"></i>护卫军体系原型</h2>
            <p class="text-[10px] text-gray-500 mt-1">交互与逻辑批注版</p>
        </div>
        <div class="flex-1 overflow-y-auto p-4 space-y-1">
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-2 px-2 tracking-wider">C端应用 (APP端)</div>
            <a href="C端_成长体系规划介绍.html" class="block px-3 py-2.5 rounded-lg text-xs bg-red-50 text-dfred font-bold transition flex items-center"><i class="fas fa-file-powerpoint w-5"></i> 规划介绍 (PRD)</a>
            <a href="C端_个人中心.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-user-circle w-5"></i> 个人中心 (入口)</a>
            <a href="C端_成长中心大盘.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-medal w-5"></i> 成长中心大盘</a>
            <a href="C端_成长值明细.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-list-alt w-5"></i> 成长值明细</a>
            <a href="C端_作业大厅.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-tasks w-5"></i> 作业大厅</a>
            
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-8 px-2 tracking-wider">B端管理 (PC端)</div>
            <a href="C端_护卫军后台功能导航页.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center"><i class="fas fa-desktop w-5"></i> 护卫军后台导航</a>
        </div>
    </div>"""

content = re.sub(r'<!-- Sidebar -->.*?</div>\n        </div>\n    </div>', sidebar_html, content, flags=re.DOTALL)

# 3. Replace main content wrapper
content = content.replace('<div class="main-content">', '<div class="ml-64 p-8 max-w-5xl mx-auto">')

# 4. Fix font sizes in hero
content = content.replace('text-4xl md:text-5xl font-extrabold', 'text-2xl font-bold')
content = content.replace('text-lg text-gray-600 leading-relaxed font-medium', 'text-sm text-gray-600 leading-relaxed')

# 5. Fix H2 sizes
content = content.replace('text-2xl font-bold text-gray-900', 'text-lg font-bold text-gray-900')

# 6. Fix "老兵" text
content = content.replace('不伤及老兵感情与利益', '不影响现存用户既有权益')
content = content.replace('【旧·尖兵】', '【存量用户：尖兵】')
content = content.replace('【旧·护卫队】', '【存量用户：护卫队】')
content = content.replace('【无标签但活跃】', '【存量用户：无标签且活跃】')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
