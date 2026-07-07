from bs4 import BeautifulSoup
import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Remove the global bottom bar
global_bar = soup.find('div', class_=lambda c: c and 'fixed' in c and 'bottom-0' in c and 'left-64' in c)
if global_bar:
    global_bar.decompose()

# 2. Fix tab-tier editability
tab_tier = soup.find('div', id='tab-tier')
if tab_tier:
    rows = tab_tier.find('tbody').find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 5:
            # 4th TD: Basic Earn
            basic_earn_td = tds[3]
            val_text = basic_earn_td.text.strip()
            multiplier = "1.0"
            if 'x' in val_text:
                multiplier = val_text.split('x')[1].replace('倍', '').strip()
            
            basic_earn_td.clear()
            basic_earn_td.append(BeautifulSoup(f'''
            <div class="flex items-center"><span class="text-sm text-gray-500 mr-2">基础赚分 x</span><input type="number" value="{multiplier}" step="0.1" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:border-dfred outline-none"><span class="text-sm text-gray-500 ml-2">倍</span></div>
            ''', 'html.parser'))

            # 5th TD: Exclusive privileges
            priv_td = tds[4]
            # Since the text is actually inside <input value="...">
            priv_input = priv_td.find('input')
            priv_text = priv_input['value'].strip() if priv_input else priv_td.text.strip()
            
            priv_td.clear()
            tags_html = ""
            if priv_text and priv_text != '--':
                privileges = [p.strip() for p in priv_text.split('、')]
                for p in privileges:
                    tags_html += f'<span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200">{p} <i class="fas fa-times ml-1 cursor-pointer text-blue-400 hover:text-blue-600"></i></span>'
            
            priv_td.append(BeautifulSoup(f'''
            <div class="flex flex-wrap gap-2 items-center">
                {tags_html}
                <button class="text-xs text-blue-600 hover:text-blue-800 border border-dashed border-blue-300 rounded px-2 py-1" onclick="openDrawer()"><i class="fas fa-plus mr-1"></i>添加</button>
            </div>
            ''', 'html.parser'))

# 3. Add sticky bottom bars to all 3 tabs
tabs_info = [
    {
        'id': 'tab-tier',
        'name': '等级门槛与特权',
        'state': '草稿态',
        'state_color': 'bg-yellow-100 text-yellow-700',
        'action_text': '对比线上版本',
        'action_icon': 'fa-exchange-alt'
    },
    {
        'id': 'tab-global',
        'name': '全局周期与保护规则',
        'state': '已发布线上',
        'state_color': 'bg-green-100 text-green-700',
        'action_text': '查看历史版本',
        'action_icon': 'fa-history'
    },
    {
        'id': 'tab-task',
        'name': '作业 XP 产出映射',
        'state': '草稿态',
        'state_color': 'bg-yellow-100 text-yellow-700',
        'action_text': '对比线上版本',
        'action_icon': 'fa-exchange-alt'
    }
]

for tab in tabs_info:
    tab_div = soup.find('div', id=tab['id'])
    if not tab_div:
        continue
    
    # Check if we already added a sticky bottom bar, remove it just in case
    existing_bar = tab_div.find('div', class_=lambda c: c and 'sticky' in c and 'bottom-0' in c)
    if existing_bar:
        existing_bar.decompose()
        
    new_content = f"""
    <div class="sticky bottom-0 bg-white border-t border-gray-200 p-4 flex items-center justify-between -mx-6 -mb-6 mt-8 z-10 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
        <div class="flex items-center gap-4">
            <div class="flex items-center text-sm">
                <span class="px-2 py-1 {tab['state_color']} font-bold rounded text-xs mr-2">{tab['state']}</span>
                <span class="text-gray-800 font-bold mr-2">【{tab['name']}】</span>
                <span class="text-gray-400 text-xs">最后更新: 2026-07-03 14:40:22</span>
            </div>
            <div class="h-4 w-px bg-gray-300"></div>
            <a href="#" class="text-sm text-blue-600 hover:text-blue-800 transition-colors flex items-center">
                <i class="fas {tab['action_icon']} mr-1.5"></i>{tab['action_text']}
            </a>
        </div>
        <div class="flex space-x-3">
            <button class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors" onclick="showToast('草稿已保存')">
                保存当前草稿
            </button>
            <button class="px-4 py-2 bg-dfred text-white rounded-lg text-sm font-medium hover:bg-red-700 transition-colors shadow-sm" onclick="showToast('【{tab['name']}】已成功发布！')">
                <i class="fas fa-paper-plane mr-1.5"></i> 独立发布【{tab['name']}】
            </button>
        </div>
    </div>
    """
    tab_div.append(BeautifulSoup(new_content, 'html.parser'))

# 4. Inject Drawer HTML and JS at the end of body
drawer_html = """
<!-- Drawer Overlay -->
<div id="privilege-drawer-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-40 hidden transition-opacity" onclick="closeDrawer()"></div>

<!-- Drawer Panel -->
<div id="privilege-drawer" class="fixed inset-y-0 right-0 w-96 bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col">
    <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
        <h3 class="text-lg font-bold text-gray-900">配置特权</h3>
        <button onclick="closeDrawer()" class="text-gray-400 hover:text-gray-600"><i class="fas fa-times text-xl"></i></button>
    </div>
    <div class="p-6 flex-1 overflow-y-auto">
        <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">选择特权类型</label>
            <select class="w-full border border-gray-300 rounded-md shadow-sm p-2 text-sm focus:border-dfred outline-none">
                <option>积分/XP 倍率加成</option>
                <option>商城兑换折扣/资格</option>
                <option>专属身份标识</option>
                <option>专属作业优先分配权</option>
                <option>活动邀请资格</option>
                <option>其他</option>
            </select>
        </div>
        <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">特权文案展示</label>
            <input type="text" placeholder="例如：解锁周边兑换商城资格" class="w-full border border-gray-300 rounded-md shadow-sm p-2 text-sm focus:border-dfred outline-none">
        </div>
        <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">特权详细说明（可选）</label>
            <textarea rows="3" placeholder="填写特权的具体发放逻辑" class="w-full border border-gray-300 rounded-md shadow-sm p-2 text-sm focus:border-dfred outline-none"></textarea>
        </div>
    </div>
    <div class="px-6 py-4 border-t border-gray-200 flex justify-end gap-3 bg-white">
        <button onclick="closeDrawer()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">取消</button>
        <button onclick="closeDrawer(); showToast('特权已添加（Demo演示）')" class="px-4 py-2 bg-dfred text-white rounded-md text-sm font-medium hover:bg-red-700 transition-colors">确定添加</button>
    </div>
</div>
<script>
    function openDrawer() {
        document.getElementById('privilege-drawer-overlay').classList.remove('hidden');
        setTimeout(() => document.getElementById('privilege-drawer').classList.remove('translate-x-full'), 10);
    }
    function closeDrawer() {
        document.getElementById('privilege-drawer').classList.add('translate-x-full');
        setTimeout(() => document.getElementById('privilege-drawer-overlay').classList.add('hidden'), 300);
    }
</script>
"""
if not soup.find('div', id='privilege-drawer'):
    soup.body.append(BeautifulSoup(drawer_html, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Final advanced fixes applied successfully.")
