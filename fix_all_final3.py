from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. REMOVE THE GLOBAL BOTTOM BAR
global_bar = soup.find('div', class_=lambda c: c and 'absolute' in c and 'bottom-0' in c and 'left-0' in c and 'right-0' in c)
if global_bar:
    global_bar.decompose()

# 2. RESTORE AND ENHANCE TAB-TIER ROWS
tab_tier = soup.find('div', id='tab-tier')
if tab_tier:
    rows = tab_tier.find('tbody').find_all('tr')
    
    privilege_data = {
        0: [],
        1: ['解锁周边兑换商城资格'],
        2: ['专属作业优先分配权', '线下活动邀请资格'],
        3: ['直面高管圆桌会', '专属勋章', '年度盛典VVIP']
    }
    
    for i, row in enumerate(rows):
        tds = row.find_all('td')
        if len(tds) >= 5:
            # 5th TD: Exclusive privileges
            priv_td = tds[4]
            priv_td.clear()
            
            tags_html = ""
            for p in privilege_data.get(i, []):
                tags_html += f'<span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200">{p} <i class="fas fa-times ml-1 cursor-pointer text-blue-400 hover:text-blue-600"></i></span>'
            
            priv_td.append(BeautifulSoup(f'''
            <div class="flex flex-wrap gap-2 items-center">
                {tags_html}
                <button type="button" class="text-xs text-blue-600 hover:text-blue-800 border border-dashed border-blue-300 rounded px-2 py-1 flex items-center bg-white cursor-pointer relative z-20" onclick="openDrawer()"><i class="fas fa-plus mr-1"></i>添加</button>
            </div>
            ''', 'html.parser'))

# 3. FIX GLOBAL TAB (SELECT DROP-DOWNS NOT CLICKABLE)
# Adding cursor-pointer and relative z-20 to ensure it's not blocked by other elements
tab_global = soup.find('div', id='tab-global')
if tab_global:
    for select in tab_global.find_all('select'):
        select['class'] = 'border border-gray-300 rounded px-2 py-1.5 text-sm bg-white focus:border-dfred outline-none cursor-pointer relative z-20'

# 4. RE-INJECT THE DRAWER HTML & JS
# First remove any existing drawer
existing_overlay = soup.find('div', id='privilege-drawer-overlay')
if existing_overlay:
    existing_overlay.decompose()
existing_drawer = soup.find('div', id='privilege-drawer')
if existing_drawer:
    existing_drawer.decompose()

drawer_html = """
<!-- Drawer Overlay -->
<div id="privilege-drawer-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-40 hidden transition-opacity" onclick="closeDrawer()" style="display: none;"></div>

<!-- Drawer Panel -->
<div id="privilege-drawer" class="fixed inset-y-0 right-0 w-96 bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col">
    <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
        <h3 class="text-lg font-bold text-gray-900">配置特权</h3>
        <button type="button" onclick="closeDrawer()" class="text-gray-400 hover:text-gray-600 cursor-pointer relative z-20"><i class="fas fa-times text-xl"></i></button>
    </div>
    <div class="p-6 flex-1 overflow-y-auto">
        <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">选择特权类型</label>
            <select class="w-full border border-gray-300 rounded-md shadow-sm p-2 text-sm focus:border-dfred outline-none cursor-pointer">
                <option>积分/XP 倍率加成</option>
                <option selected>商城兑换折扣/资格</option>
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
        <button type="button" onclick="closeDrawer()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors cursor-pointer relative z-20">取消</button>
        <button type="button" onclick="closeDrawer(); showToast('特权已添加（Demo演示）')" class="px-4 py-2 bg-dfred text-white rounded-md text-sm font-medium hover:bg-red-700 transition-colors shadow-sm cursor-pointer relative z-20">确定添加</button>
    </div>
</div>
<script>
    function openDrawer() {
        const overlay = document.getElementById('privilege-drawer-overlay');
        const drawer = document.getElementById('privilege-drawer');
        if (overlay && drawer) {
            overlay.classList.remove('hidden');
            overlay.style.display = 'block';
            setTimeout(() => {
                drawer.classList.remove('translate-x-full');
            }, 10);
        } else {
            console.error('Drawer elements not found!');
        }
    }
    function closeDrawer() {
        const overlay = document.getElementById('privilege-drawer-overlay');
        const drawer = document.getElementById('privilege-drawer');
        if (drawer) {
            drawer.classList.add('translate-x-full');
            setTimeout(() => {
                if(overlay) {
                    overlay.classList.add('hidden');
                    overlay.style.display = 'none';
                }
            }, 300);
        }
    }
</script>
"""
soup.body.append(BeautifulSoup(drawer_html, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Final advanced fixes applied successfully.")
