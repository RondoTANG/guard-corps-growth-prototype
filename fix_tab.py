import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. replace switchTab with switchConfigTab
html = html.replace("switchTab('", "switchConfigTab('")

# 2. Add switchConfigTab definition in script block
script_def = """
        function switchConfigTab(tabId) {
            // Hide all tabs
            ['tab-tier', 'tab-global', 'tab-task'].forEach(id => {
                document.getElementById(id).classList.add('hidden');
                const btn = document.getElementById('btn-' + id);
                btn.classList.remove('tab-active', 'text-dfred', 'font-bold', 'border-b-2', 'border-dfred');
                btn.classList.add('tab-inactive', 'text-gray-500');
            });
            
            // Show active tab
            document.getElementById(tabId).classList.remove('hidden');
            const activeBtn = document.getElementById('btn-' + tabId);
            activeBtn.classList.remove('tab-inactive', 'text-gray-500');
            activeBtn.classList.add('tab-active', 'text-dfred', 'font-bold', 'border-b-2', 'border-dfred');
        }

        function showToast(message) {"""

html = html.replace("function showToast(message) {", script_def)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
