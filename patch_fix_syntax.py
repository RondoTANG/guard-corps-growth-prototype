import re

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "r") as f:
    content = f.read()

# 1. Fix the missing `});` for DOMContentLoaded
# Look at the end of the file
end_pattern = "        }\n</script></body>"
fixed_end = "        }\n    });\n</script></body>"
if end_pattern in content:
    content = content.replace(end_pattern, fixed_end)

# 2. Add the empty-selection-overlay
# The chart area starts with:
# <div class="flex-1 flex flex-col min-w-0 bg-gray-50 h-screen overflow-y-auto">
#   <!-- Top Navbar -->
#   <div class="bg-white border-b border-gray-200 h-14 flex items-center justify-between px-4 shrink-0 shadow-sm z-10 relative">
#   ...
#   <div class="p-6 pb-20 relative min-h-screen">
# We can inject the overlay right after `<div class="p-6 pb-20 relative min-h-screen">`
target_html = '<div class="p-6 pb-20 relative min-h-screen">'
overlay_html = """<div class="p-6 pb-20 relative min-h-screen">
<div id="empty-selection-overlay" class="absolute inset-0 bg-gray-50/70 backdrop-blur-[2px] z-[40] flex items-center justify-center hidden" style="min-height: 800px;">
    <div class="flex flex-col items-center justify-center bg-white border border-gray-200 rounded-lg shadow-md p-8 translate-y-[-100px]">
        <i class="fas fa-sitemap text-4xl text-blue-300 mb-4"></i>
        <h3 class="text-gray-800 font-bold mb-2">未选择对比维度</h3>
        <p class="text-gray-500 text-sm">请在左侧组织树中，勾选需要统计对比的党委或党支部</p>
    </div>
</div>
"""
if target_html in content and "id=\"empty-selection-overlay\"" not in content:
    content = content.replace(target_html, overlay_html)

# 3. Update Javascript to toggle the overlay
# Find updateChart(info) { ... if (names.length === 0) { ... }
# We want to inject the overlay toggle
search_js = """            if (names.length === 0) {
                orgOption.xAxis[0].data = [];"""
replace_js = """            const overlay = document.getElementById('empty-selection-overlay');
            if (names.length === 0) {
                if (overlay) overlay.classList.remove('hidden');
                orgOption.xAxis[0].data = [];"""
if search_js in content:
    content = content.replace(search_js, replace_js)

search_js_2 = """            orgOption.xAxis[0].data = names;"""
replace_js_2 = """            const overlay = document.getElementById('empty-selection-overlay');
            if (overlay) overlay.classList.add('hidden');
            orgOption.xAxis[0].data = names;"""
if search_js_2 in content:
    content = content.replace(search_js_2, replace_js_2)

# Write back
with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "w") as f:
    f.write(content)

