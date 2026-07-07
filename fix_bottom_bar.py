from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

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
        
    # Find the bottom bar
    bar = tab_div.find('div', class_=lambda c: c and 'fixed bottom-0' in c)
    if bar:
        bar.clear()
        
        # Build the new bar content
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
            <button class="px-4 py-2 bg-dfred text-white rounded-lg text-sm font-medium hover:bg-red-700 transition-colors shadow-sm">
                <i class="fas fa-paper-plane mr-1.5"></i> 独立发布【{tab['name']}】
            </button>
        </div>
        """
        bar.append(BeautifulSoup(new_content, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Bottom bars updated.")
