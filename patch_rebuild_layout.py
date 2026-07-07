import re

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "r") as f:
    content = f.read()

# We know the top is fine until `<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>\n\n</div>`
# And the broken tree ends right before `<div class="flex-1 flex flex-col overflow-hidden relative">`
start_marker = '<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>'
end_marker = '<div class="flex-1 flex flex-col overflow-hidden relative">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    fixed_header = """<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    primary: '#1E3A8A', // 深蓝色
                    secondary: '#3B82F6', // 亮蓝色
                    dfred: '#E60012', // 东风红
                }
            }
        }
    }
</script>
<style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #E5E7EB; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #D1D5DB; }
</style>
</head>
<body class="bg-gray-50 font-sans text-gray-800">

<div class="flex h-screen overflow-hidden bg-gray-50 font-sans">
    
    <!-- Left Sidebar: Org Tree -->
    <div class="w-80 bg-white border-r border-gray-200 flex flex-col shrink-0 relative" id="org-tree-sidebar">
        <div id="sidebar-resizer" class="absolute top-0 -right-1 w-2 h-full cursor-col-resize hover:bg-blue-400 z-[100] transition-colors"></div>
        <!-- Header -->
        <div class="p-4 border-b border-gray-100 flex flex-col bg-gray-50/50">
            <div class="flex items-center justify-between mb-3">
                <h3 class="font-bold text-gray-800 flex items-center text-sm">
                    <i class="fas fa-sitemap text-blue-600 mr-2"></i>党组织筛选
                </h3>
                <span class="badge-count bg-blue-100 text-blue-600 text-xs px-2 py-0.5 rounded-full font-medium">已选 0</span>
            </div>
            
            <div class="relative mb-3">
                <i class="fas fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs"></i>
                <input class="w-full pl-8 pr-3 py-1.5 border border-gray-300 rounded text-xs focus:border-blue-500 outline-none" placeholder="搜索党委/党支部" type="text"/>
            </div>
            
            <div class="flex items-center justify-between">
                <div class="flex gap-2">
                    <button class="px-2 py-1 bg-white shadow-sm border border-gray-300 rounded text-[11px] hover:bg-gray-50 text-gray-700" id="btn-toggle-collapse">一键收起</button>
                    <button class="px-2 py-1 bg-white shadow-sm border border-gray-300 rounded text-[11px] hover:bg-gray-50 text-gray-700" id="btn-only-l2">仅二级</button>
                </div>
                <button class="text-[11px] text-gray-500 hover:text-blue-600" id="btn-clear-all"><i class="fas fa-trash-alt mr-1"></i>清空</button>
            </div>
        </div>
        
        <!-- Tree View -->
        <div class="flex-1 overflow-y-auto p-3 text-sm">
        </div>
    </div>
"""
    content = content[:start_idx] + fixed_header + content[end_idx:]
    with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "w") as f:
        f.write(content)

