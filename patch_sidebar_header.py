import re

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "r") as f:
    content = f.read()

# 1. Update the sidebar resize handle to be wider and z-index higher
old_resizer = '<div id="sidebar-resizer" class="absolute top-0 right-0 w-[3px] h-full cursor-col-resize hover:bg-blue-400 z-50 transition-colors"></div>'
new_resizer = '<div id="sidebar-resizer" class="absolute top-0 -right-1 w-2 h-full cursor-col-resize hover:bg-blue-400 z-[100] transition-colors"></div>'
content = content.replace(old_resizer, new_resizer)

# 2. Extract and replace the sidebar header (from <div class="p-4 border-b... to the end of <div class="p-3 border-b border-gray-100">...</div>)
# We can find it using regex or string find
start_header = content.find('<div class="p-4 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">')
end_header = content.find('<div class="flex-1 overflow-y-auto p-3 text-sm">')

if start_header != -1 and end_header != -1:
    new_header_html = """<div class="p-4 border-b border-gray-100 flex flex-col bg-gray-50/50">
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
"""
    content = content[:start_header] + new_header_html + content[end_header:]

# 3. Remove the broken inline script block that I added earlier
inline_script_start = content.find('<script>\n    const btnSelectAll = document.getElementById(\'btn-select-all\');')
if inline_script_start != -1:
    inline_script_end = content.find('</script>\n<div class="flex items-center cursor-pointer org-node', inline_script_start)
    if inline_script_end != -1:
        content = content[:inline_script_start] + content[inline_script_end + 10:]

# 4. Add the button logics properly into the main script block at the bottom
# First, remove any old button logics if they exist
def remove_block(text, start_str, end_str):
    start = text.find(start_str)
    if start != -1:
        end = text.find(end_str, start)
        if end != -1:
            return text[:start] + text[end + len(end_str):]
    return text

content = remove_block(content, "const btnSelectAll = document.getElementById('btn-select-all');", "updateChart(getSelectedNames());\n        });\n    }")
# And remove btn-toggle-collapse from main block if it was there
content = remove_block(content, "const btnToggleCollapse = document.getElementById('btn-toggle-collapse');", "});\n    }")
content = remove_block(content, "if (btnToggleCollapse)", "});\n    }")

new_button_logic = """
    // Button actions
    const btnClearAll = document.getElementById('btn-clear-all');
    const btnOnlyL2 = document.getElementById('btn-only-l2');
    const btnToggleCollapse = document.getElementById('btn-toggle-collapse');

    if (btnClearAll) {
        btnClearAll.addEventListener('click', () => {
            const allBoxes = sidebar.querySelectorAll('.checkbox-box');
            allBoxes.forEach(box => setCheckboxState(box, 0));
            updateChart(getSelectedNames());
        });
    }

    if (btnToggleCollapse) {
        let isCollapsed = false;
        btnToggleCollapse.addEventListener('click', () => {
            isCollapsed = !isCollapsed;
            btnToggleCollapse.innerHTML = isCollapsed ? '一键展开' : '一键收起';
            const allContainers = sidebar.querySelectorAll('.children-container');
            const allIcons = sidebar.querySelectorAll('.toggle-icon i');
            
            allContainers.forEach(c => {
                const parentNode = c.previousElementSibling;
                if (parentNode && parseInt(parentNode.dataset.level) >= 1) {
                    if (isCollapsed) c.classList.add('hidden');
                    else c.classList.remove('hidden');
                }
            });
            allIcons.forEach(icon => {
                const pNode = icon.closest('.org-node');
                if (pNode && parseInt(pNode.dataset.level) >= 1) {
                    if (isCollapsed) {
                        icon.classList.remove('fa-chevron-down');
                        icon.classList.add('fa-chevron-right');
                    } else {
                        icon.classList.remove('fa-chevron-right');
                        icon.classList.add('fa-chevron-down');
                    }
                }
            });
        });
    }

    if (btnOnlyL2) {
        btnOnlyL2.addEventListener('click', () => {
            const allBoxes = sidebar.querySelectorAll('.checkbox-box');
            allBoxes.forEach(box => setCheckboxState(box, 0));
            
            const l2Nodes = sidebar.querySelectorAll('.org-node[data-level="2"]');
            l2Nodes.forEach(node => {
                const box = node.querySelector('.checkbox-box');
                if(getCheckboxState(box) !== 1) {
                     node.click();
                }
            });
            updateChart(getSelectedNames());
        });
    }
"""

if "function getSelectedNames()" in content:
    content = content.replace("function getSelectedNames()", new_button_logic + "\n    function getSelectedNames()")

# Write back
with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "w") as f:
    f.write(content)

