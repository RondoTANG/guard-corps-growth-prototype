import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the broken tier button block + extra div
tier_bad = r'\n    <!-- Tab 内部的保存发布按钮 -->\n    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">.*?此模块最后更新: 2026-07-03 10:15:30.*?</div>\n\n</div>\n'
content = re.sub(tier_bad, '\n', content, flags=re.DOTALL)

# Remove the broken global button block + extra div
global_bad = r'\n    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">.*?此模块最后更新: 2026-07-02 16:22:05.*?</div>\n\n</div>\n'
content = re.sub(global_bad, '\n', content, flags=re.DOTALL)

# Remove the broken task button block + extra divs
task_bad = r'\n    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">.*?此模块最后更新: 2026-07-03 09:40:12.*?</div>\n</div>\n</div>\n</div>\n'
content = re.sub(task_bad, '\n', content, flags=re.DOTALL)

# Now, the file should be back to the state WITHOUT the buttons and WITHOUT the extra divs.
# Wait, let's verify if the original `</div>` tags for the tabs are intact.
# Yes, because my replace string was:
# content.replace('<div class="hidden" id="tab-global">', btn_bar_tier + '\n</div>\n<div class="hidden" id="tab-global">')
# This means the original `</div>` for `tab-tier` is still there, right before where I inserted.

# Let's cleanly inject the buttons BEFORE the closing </div> of each tab.
# We can find the closing </div> of `tab-tier` by looking for `</table>\n</div>\n</div>` 
# Actually, `tab-tier` ends with `</tbody>\n</table>\n</div>\n</div>`
# Let's insert the tier button before the LAST `</div>` of `tab-tier`.
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
content = content.replace('</table>\n</div>\n</div>\n<div class="hidden" id="tab-global">', '</table>\n</div>\n' + btn_bar_tier + '</div>\n<div class="hidden" id="tab-global">')


btn_bar_global = """
    <!-- Tab 内部的保存发布按钮 -->
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-02 16:22:05</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('全局周期与保护规则草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('全局周期与保护规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""
# `tab-global` ends before `tab-task`. It ends with `</div>\n</div>\n</div>\n<div class="hidden" id="tab-task">`
# Let's insert before the last </div>
content = re.sub(r'(</div>\n)\s*(</div>\n<div class="hidden" id="tab-task">)', r'\1' + btn_bar_global + r'\2', content)

btn_bar_task = """
    <!-- Tab 内部的保存发布按钮 -->
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 09:40:12</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('作业XP产出映射配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('作业XP产出映射规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
"""
# `tab-task` ends before `<div class="fixed top-5`. It ends with `</div>\n</div>\n</div>\n<div class="fixed top-5`
# But wait, we stripped the bad task div, so now it is `</div>\n</div>\n<div class="fixed top-5` (or similar)
# Let's just find the first `<div class="fixed top-5` and insert before it, but we need to make sure we are inside `tab-task`.
# Actually `tab-task` had `<div class="p-6 hidden" id="tab-task">`? No, `<div class="hidden" id="tab-task">`.
# It contains `<!-- 人工干预类 -->` etc, then ends.
# I'll find `<!-- 人工干预类 -->.*?</div>\n</div>\n</div>`
# Just use re.sub on the last </div> before `<div class="fixed top-5`
content = re.sub(r'(</div>\n)\s*(</div>\n\s*<div class="fixed top-5)', r'\1' + btn_bar_task + r'\2', content)

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fix applied")
