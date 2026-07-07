import re

file_path = 'B端_等级规则与XP配置页.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove the previously inserted blocks completely to reset
btn_bar_tier_re = r'    <!-- Tab 内部的保存发布按钮 -->\s*<div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">\s*<span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 10:15:30</span>.*?</button>\s*</div>'
content = re.sub(btn_bar_tier_re, '', content, flags=re.DOTALL)

btn_bar_global_re = r'    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">\s*<span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-02 16:22:05</span>.*?</button>\s*</div>'
content = re.sub(btn_bar_global_re, '', content, flags=re.DOTALL)

btn_bar_task_re = r'    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">\s*<span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 09:40:12</span>.*?</button>\s*</div>'
content = re.sub(btn_bar_task_re, '', content, flags=re.DOTALL)

# Also remove the extra </div> I added right before `<div class="hidden" id="tab-global">` and `<div class="hidden" id="tab-task">`
content = content.replace('</div>\n<div class="hidden" id="tab-global">', '<div class="hidden" id="tab-global">')
content = content.replace('</div>\n<div class="hidden" id="tab-task">', '<div class="hidden" id="tab-task">')

# Wait, the original HTML had `</div>` before `<div class="hidden" id="tab-global">` because it closed `tab-tier`!
# Let me look at my first grep before I messed it up.
# In my `head -n 250`, the original structure was:
"""
</div>
</div>
<div class="hidden" id="tab-global">
"""
# So the original DID NOT have `</div>` before `<div class="hidden" id="tab-global">` if we consider my grep?
# No, `</div>\n</div>\n<div class="hidden" id="tab-global">`! Yes it did.
# If I removed it, I might have broken the HTML! Let's be very careful.

