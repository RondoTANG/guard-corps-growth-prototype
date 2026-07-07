import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

header_old = """            <div class="flex items-center gap-4">
                <div class="flex bg-gray-100 rounded p-1 text-sm border border-gray-200">
                    <button class="px-3 py-1 bg-white shadow-sm rounded text-blue-600 font-medium">本月</button>
                    <button class="px-3 py-1 text-gray-600 hover:text-gray-900">近90天</button>
                    <button class="px-3 py-1 text-gray-600 hover:text-gray-900">全年</button>
                </div>
                <div class="w-8 h-8 rounded-full bg-dfred text-white flex items-center justify-center font-bold text-sm">
                    Admin
                </div>
            </div>"""

header_new = """            <div class="flex items-center">
                <div class="w-8 h-8 rounded-full bg-dfred text-white flex items-center justify-center font-bold text-sm">
                    Admin
                </div>
            </div>"""

content_old = """        <!-- Content Area -->
        <div class="flex-1 overflow-y-auto p-6 space-y-6">"""

content_new = """        <!-- Content Area -->
        <div class="flex-1 overflow-y-auto p-6 space-y-6">
            
            <!-- Global Filter Bar -->
            <div class="bg-white p-4 rounded-md shadow-sm border border-gray-200 flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <span class="text-sm font-bold text-gray-800">大盘数据总览</span>
                    <div class="h-4 w-px bg-gray-300"></div>
                    <div class="flex bg-gray-100 rounded p-1 text-sm border border-gray-200">
                        <button class="px-4 py-1 bg-white shadow-sm rounded text-blue-600 font-medium">本月</button>
                        <button class="px-4 py-1 text-gray-600 hover:text-gray-900">近90天</button>
                        <button class="px-4 py-1 text-gray-600 hover:text-gray-900">全年</button>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <button class="bg-blue-50 text-blue-600 px-4 py-1.5 rounded text-sm hover:bg-blue-100 font-medium"><i class="fas fa-download mr-1"></i> 导出报表</button>
                </div>
            </div>"""

html = html.replace(header_old, header_new)
html = html.replace(content_old, content_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
