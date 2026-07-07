from bs4 import BeautifulSoup
import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all the button bars and remove them. They are identified by having text like "此模块最后更新"
for div in soup.find_all('div', class_='mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center'):
    if "此模块最后更新" in div.text:
        div.extract()

# Find the three tab containers
tab_tier = soup.find('div', id='tab-tier')
tab_global = soup.find('div', id='tab-global')
tab_task = soup.find('div', id='tab-task')

btn_bar_tier = BeautifulSoup("""
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 10:15:30</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('等级与特权配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('等级与特权规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
""", 'html.parser')

btn_bar_global = BeautifulSoup("""
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-02 16:22:05</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('全局周期与保护规则草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('全局周期与保护规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
""", 'html.parser')

btn_bar_task = BeautifulSoup("""
    <div class="mt-10 pt-5 border-t border-gray-200 flex justify-end gap-3 items-center">
        <span class="text-xs text-gray-400 mr-2">此模块最后更新: 2026-07-03 09:40:12</span>
        <button class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition" onclick="showToast('作业XP产出映射配置草稿已保存')">保存草稿</button>
        <button class="bg-dfred hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium shadow-sm transition" onclick="showToast('作业XP产出映射规则已成功发布至生产环境！')">
            <i class="fas fa-paper-plane mr-1.5"></i> 发布生效
        </button>
    </div>
""", 'html.parser')

if tab_tier:
    tab_tier.append(btn_bar_tier)
if tab_global:
    tab_global.append(btn_bar_global)
if tab_task:
    tab_task.append(btn_bar_task)

# The html structure itself might be broken (tabs might not be siblings inside <div class="p-6"> anymore)
# Let's check if they are siblings.
p6_container = soup.find('div', class_='p-6')
if p6_container:
    # ensure tab_tier, tab_global, tab_task are inside p6_container
    if tab_tier.parent != p6_container:
        p6_container.append(tab_tier.extract())
    if tab_global.parent != p6_container:
        p6_container.append(tab_global.extract())
    if tab_task.parent != p6_container:
        p6_container.append(tab_task.extract())

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("BS4 Fix applied")
