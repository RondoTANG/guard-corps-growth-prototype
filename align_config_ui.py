import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Wrap the tabs in the new style
old_tabs = """            <div class="mb-6 flex items-center gap-4 border-b border-gray-200">
                <div class="flex">
                    <button onclick="switchConfigTab('tab-tier')" id="btn-tab-tier" class="pb-3 px-1 tab-active text-sm">2.1 等级门槛与特权配置</button>
                    <button onclick="switchConfigTab('tab-global')" id="btn-tab-global" class="pb-3 px-1 tab-inactive text-sm">2.2 全局周期与保护规则</button>
                    <button onclick="switchConfigTab('tab-task')" id="btn-tab-task" class="pb-3 px-1 tab-inactive text-sm">2.3 作业 XP 产出映射池</button>
                </div>
            </div>"""

new_tabs = """            <div class="bg-white p-4 rounded-md shadow-sm border border-gray-200 mb-4 flex items-center justify-between">
                <div class="flex space-x-6">
                    <button onclick="switchConfigTab('tab-tier')" id="btn-tab-tier" class="pb-2 tab-active text-sm border-b-2 border-dfred text-dfred font-bold">等级门槛与特权配置</button>
                    <button onclick="switchConfigTab('tab-global')" id="btn-tab-global" class="pb-2 tab-inactive text-sm text-gray-500 hover:text-gray-700">全局周期与保护规则</button>
                    <button onclick="switchConfigTab('tab-task')" id="btn-tab-task" class="pb-2 tab-inactive text-sm text-gray-500 hover:text-gray-700">作业 XP 产出映射池</button>
                </div>
                <div class="flex items-center gap-2 text-xs text-gray-500">
                    <i class="fas fa-info-circle text-blue-500"></i> 修改配置后，次日 00:00 生效
                </div>
            </div>"""

html = html.replace(old_tabs, new_tabs)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
