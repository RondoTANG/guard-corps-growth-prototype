import re

file_path = 'B端_等级规则与XP配置页.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

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

btn_bar_global = """
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-02 16:22:05</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('全局周期与保护规则草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('全局周期与保护规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""

btn_bar_task = """
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 09:40:12</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('作业XP产出映射配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('作业XP产出映射规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""

# Insert btn_bar_tier before <div class="hidden" id="tab-global">
content = content.replace('<div class="hidden" id="tab-global">', btn_bar_tier + '\n</div>\n<div class="hidden" id="tab-global">')

# Insert btn_bar_global before <div class="hidden" id="tab-task">
content = content.replace('<div class="hidden" id="tab-task">', btn_bar_global + '\n</div>\n<div class="hidden" id="tab-task">')

# Insert btn_bar_task before <div id="editDrawer" (or at the end of tab-task div)
# Let's find the closing of tab-task by looking for the next major div.
# tab-task contains several sections. It ends where <div id="editDrawer" begins, after two </div>s.
content = content.replace('<div class="fixed top-5', btn_bar_task + '\n</div>\n</div>\n</div>\n<div class="fixed top-5')
# Let's clean up duplicate </div> if we added too many
# Actually the easiest is to just find <div id="editDrawer" and insert before its parents.
# I'll just use a direct replace.
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated")
