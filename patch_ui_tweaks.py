import re

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "r") as f:
    content = f.read()

# 1. Sidebar Resize Handle
sidebar_div = '<div class="w-80 bg-white border-r border-gray-200 flex flex-col shrink-0" id="org-tree-sidebar">'
new_sidebar_div = '<div class="w-80 bg-white border-r border-gray-200 flex flex-col shrink-0 relative" id="org-tree-sidebar"><div id="sidebar-resizer" class="absolute top-0 right-0 w-[3px] h-full cursor-col-resize hover:bg-blue-400 z-50 transition-colors"></div>'
content = content.replace(sidebar_div, new_sidebar_div)

# 2. Table overflow and text size
table_container_old = '<div class="bg-white border border-gray-200 rounded-md shadow-sm overflow-hidden mb-6">'
table_container_new = '<div class="bg-white border border-gray-200 rounded-md shadow-sm overflow-x-auto mb-6">'
content = content.replace(table_container_old, table_container_new)

# Table headers: change text-xs to text-[11px] maybe? the user said "font too big"
# the headers are: text-xs font-medium text-gray-500
# the cells are: text-sm text-gray-900 or text-sm text-gray-600
# Let's extract the table string and replace text-sm with text-xs
table_start = content.find('<table class="min-w-full divide-y divide-gray-200">')
table_end = content.find('</table>', table_start)
if table_start != -1 and table_end != -1:
    table_html = content[table_start:table_end]
    table_html = table_html.replace('text-sm', 'text-xs')
    table_html = table_html.replace('text-xs', 'text-[11px]') # headers and badges
    table_html = table_html.replace('min-w-full', 'min-w-max') # prevent crushing columns if container is small
    content = content[:table_start] + table_html + content[table_end:]

# 3. Add Resize JS Logic
js_resize = """
    // 2. Sidebar Resize Logic
    const sidebar = document.getElementById('org-tree-sidebar');
    const resizer = document.getElementById('sidebar-resizer');
    
    if (sidebar && resizer) {
        let isResizing = false;
        resizer.addEventListener('mousedown', (e) => {
            isResizing = true;
            document.body.style.cursor = 'col-resize';
            document.body.style.userSelect = 'none';
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!isResizing) return;
            const sidebarRect = sidebar.getBoundingClientRect();
            let newWidth = e.clientX - sidebarRect.left;
            if (newWidth < 200) newWidth = 200; // min width
            if (newWidth > 600) newWidth = 600; // max width
            sidebar.style.width = newWidth + 'px';
            
            // Resize charts
            if (orgChart) orgChart.resize();
            if (window.tierChart) window.tierChart.resize();
            if (window.conversionChart) window.conversionChart.resize();
            if (window.statusChart) window.statusChart.resize();
        });
        
        document.addEventListener('mouseup', () => {
            if (isResizing) {
                isResizing = false;
                document.body.style.cursor = '';
                document.body.style.userSelect = '';
            }
        });
    }
"""

if "// 1. Checkbox Interaction Logic" in content and "// 2. Sidebar Resize Logic" not in content:
    content = content.replace("// 1. Checkbox Interaction Logic", js_resize + "\n    // 1. Checkbox Interaction Logic")

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "w") as f:
    f.write(content)
