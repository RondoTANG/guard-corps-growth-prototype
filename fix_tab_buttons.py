import re

file_path = 'B端_等级规则与XP配置页.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the global button
global_btn_pattern = r'<div class="flex flex-col items-end">\s*<button class="bg-dfred.*?保存并发布\s*</button>\s*<span class="text-xs text-gray-400 mt-2">最后更新:.*?</span>\s*</div>'
content = re.sub(global_btn_pattern, '', content, flags=re.DOTALL)

# 2. Define the button bars
btn_bar_tier = """
    <!-- Tab 内部的保存发布按钮 -->
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 10:15:30</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('等级与特权配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('等级与特权规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""

btn_bar_task = """
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 09:40:12</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('XP发放规则配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('XP发放规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""

btn_bar_downgrade = """
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-02 16:22:05</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('降级跌幅规则草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('降级跌幅规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""

# Insert at the end of each tab div
# The tabs close with </div> directly before the next tab starts or before the parent closes.
# We can find the start of the next tab or end of parent.

# For tab-tier: find `<div id="tab-task" class="p-6 hidden">`
content = content.replace('<div id="tab-task" class="p-6 hidden">', btn_bar_tier + '\n</div>\n<div id="tab-task" class="p-6 hidden">')

# For tab-task: find `<div id="tab-downgrade" class="p-6 hidden">`
content = content.replace('<div id="tab-downgrade" class="p-6 hidden">', btn_bar_task + '\n</div>\n<div id="tab-downgrade" class="p-6 hidden">')

# For tab-downgrade: find the end of the tabs container
# The tabs container is `<div class="bg-white rounded-lg shadow-sm border border-gray-200">`
# It closes with a `</div>` before `</main>` or `<div class="fixed top-5...`. Let's look for `<div class="fixed top-5` and insert before its parent closing tag.
# Actually, the structure is:
# <div id="tab-downgrade" class="p-6 hidden"> ... </div>
# </div> (closes the bg-white container)
# <div id="editDrawer" ...>

content = content.replace('<div id="editDrawer"', btn_bar_downgrade + '\n</div>\n</div>\n<div id="editDrawer"')

# Let's fix the toast message from drawer
content = content.replace("showToast('特权配置已临时保存在页面中。正式环境需点击左上角“保存并发布”！');", "showToast('特权配置已临时保存在页面中。如需生效请在当前标签页底部点击“发布生效”。');")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated tab buttons.")
