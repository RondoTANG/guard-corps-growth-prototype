from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Add CSS for toggle switches
style_tag = soup.new_tag('style')
style_tag.string = """
/* Toggle Switch CSS */
.toggle-checkbox:checked { right: 0; border-color: #C8102E; }
.toggle-checkbox:checked + .toggle-label { background-color: #C8102E; }
.toggle-checkbox { right: 0; z-index: 1; border-color: #e5e7eb; transition: all 0.3s; }
.toggle-label { width: 2.5rem; transition: all 0.3s; }
.toggle-checkbox:not(:checked) { right: 1.25rem; }
"""
if not soup.find('style', string=lambda s: s and '.toggle-checkbox' in s):
    soup.head.append(style_tag)

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
            priv_text = priv_td.text.strip()
            priv_td.clear()
            tags_html = ""
            if priv_text and priv_text != '--':
                privileges = [p.strip() for p in priv_text.split('、')]
                for p in privileges:
                    tags_html += f'<span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200">{p} <i class="fas fa-times ml-1 cursor-pointer text-blue-400 hover:text-blue-600"></i></span>'
            
            priv_td.append(BeautifulSoup(f'''
            <div class="flex flex-wrap gap-2 items-center">
                {tags_html}
                <button class="text-xs text-blue-600 hover:text-blue-800 border border-dashed border-blue-300 rounded px-2 py-1"><i class="fas fa-plus mr-1"></i>添加</button>
            </div>
            ''', 'html.parser'))

# 3. Fix tab-global soft landing
tab_global = soup.find('div', id='tab-global')
if tab_global:
    for span in tab_global.find_all('span', class_='font-bold'):
        if '曾任大师' in span.text:
            static_box = span.find_parent('div')
            if static_box:
                static_box.replace_with(BeautifulSoup('''
                <div class="mt-4 flex flex-col space-y-3 w-full max-w-2xl">
                    <div class="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-200 hover:border-gray-300 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="text-sm text-gray-700 font-medium">规则 1:</span>
                            <span class="text-sm text-gray-600">曾达</span>
                            <select class="border border-gray-300 rounded px-2 py-1.5 text-sm bg-white focus:border-dfred outline-none">
                                <option selected>大师 (Level 4)</option>
                                <option>专家 (Level 3)</option>
                            </select>
                            <span class="text-sm text-gray-600">，清零后最低跌至</span>
                            <select class="border border-gray-300 rounded px-2 py-1.5 text-sm bg-white focus:border-dfred outline-none">
                                <option>专家 (Level 3)</option>
                                <option selected>熟练 (Level 2)</option>
                                <option>新秀 (Level 1)</option>
                            </select>
                        </div>
                        <button class="text-red-400 hover:text-red-600 px-2"><i class="fas fa-trash-alt"></i></button>
                    </div>
                    <div>
                        <button class="text-sm text-blue-600 hover:text-blue-800 border border-dashed border-blue-300 rounded-lg px-4 py-2 hover:bg-blue-50 transition-colors">
                            <i class="fas fa-plus mr-1"></i> 新增兜底规则
                        </button>
                    </div>
                </div>
                ''', 'html.parser'))
            break

# 4. Fix Bottom Bars for all 3 tabs!
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
    
    # We find the button that says '发布生效' or '独立发布'
    publish_btn = tab_div.find(lambda tag: tag.name == 'button' and ('发布生效' in tag.text or '独立发布' in tag.text))
    if publish_btn:
        # The parent flex container that holds the bottom bar
        bottom_bar = publish_btn.find_parent('div', class_=lambda c: c and 'flex' in c).find_parent('div')
        if bottom_bar:
            # Reconstruct it as sticky!
            bottom_bar['class'] = ['sticky', 'bottom-0', 'bg-white', 'border-t', 'border-gray-200', 'p-4', 'flex', 'items-center', 'justify-between', '-mx-6', '-mb-6', 'mt-8', 'z-10']
            bottom_bar.clear()
            
            new_content = f"""
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
                <button class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
                    保存当前草稿
                </button>
                <button class="px-4 py-2 bg-dfred text-white rounded-lg text-sm font-medium hover:bg-red-700 transition-colors shadow-sm" onclick="showToast('【{tab['name']}】已发布！')">
                    <i class="fas fa-paper-plane mr-1.5"></i> 独立发布【{tab['name']}】
                </button>
            </div>
            """
            bottom_bar.append(BeautifulSoup(new_content, 'html.parser'))


with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("All advanced fixes applied successfully.")
