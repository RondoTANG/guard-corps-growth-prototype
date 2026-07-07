from bs4 import BeautifulSoup
import datetime

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main_tag = soup.find('main')
if main_tag:
    # 1. Update the Data Overview Header area
    # Find the filter bar
    filter_bar = main_tag.find('div', class_=lambda c: c and 'bg-white' in c and 'p-4' in c and 'shadow-sm' in c)
    if filter_bar:
        # Clear it and rebuild the date picker part and add T+1 text
        filter_bar.clear()
        
        filter_html = """
        <div class="flex items-center gap-4">
            <span class="text-sm font-bold text-gray-800">大盘数据总览</span>
            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded">数据更新至: 2023-10-24 (T+1)</span>
            <div class="h-4 w-px bg-gray-300"></div>
            <!-- Interactive Date Picker -->
            <div class="flex items-center gap-2">
                <div class="flex bg-gray-100 rounded p-1 text-sm border border-gray-200">
                    <button class="px-4 py-1 bg-white shadow-sm rounded text-blue-600 font-medium">本月</button>
                    <button class="px-4 py-1 text-gray-600 hover:text-gray-900">近90天</button>
                    <button class="px-4 py-1 text-gray-600 hover:text-gray-900">本年</button>
                </div>
                <div class="flex items-center border border-gray-300 rounded px-2 py-1 bg-white cursor-pointer hover:border-blue-500">
                    <i class="far fa-calendar-alt text-gray-400 mr-2"></i>
                    <span class="text-sm text-gray-600">2023-10-01 ~ 2023-10-31</span>
                    <i class="fas fa-chevron-down text-gray-400 ml-2 text-xs"></i>
                </div>
            </div>
        </div>
        <div class="flex items-center">
            <button class="bg-blue-50 text-blue-600 px-4 py-1.5 rounded text-sm hover:bg-blue-100 font-medium"><i class="fas fa-download mr-1"></i> 导出报表</button>
        </div>
        """
        filter_bar.append(BeautifulSoup(filter_html, 'html.parser'))

    # 2. Update the KPI Cards
    # Find the grid
    kpi_grid = main_tag.find('div', class_=lambda c: c and 'grid-cols-4' in c)
    if kpi_grid:
        kpi_grid['class'] = 'grid grid-cols-5 gap-4' # Change to 5 cols to fit the new cards
        kpi_grid.clear()
        
        kpis = [
            {
                'title': '累计用户总数',
                'value': '12,450',
                'trend': '<span class="text-xs text-green-500 font-medium"><i class="fas fa-arrow-up mr-1"></i>12%</span> <span class="text-xs text-gray-400">较上月新增</span>',
                'icon': 'fa-users',
                'icon_color': 'text-blue-500',
                'bg_color': 'bg-blue-50',
                'tooltip': '截止至昨日大盘的累计护卫军总人数，不受上方时间选择器影响。'
            },
            {
                'title': '新增用户数',
                'value': '1,240',
                'trend': '<span class="text-xs text-gray-400">所选时间范围内新加入用户</span>',
                'icon': 'fa-user-plus',
                'icon_color': 'text-indigo-500',
                'bg_color': 'bg-indigo-50',
                'tooltip': '在所选时间范围内，新注册或新加入护卫军体系的用户数。'
            },
            {
                'title': '活跃用户数',
                'value': '8,230',
                'trend': '<span class="text-xs text-gray-600 font-medium">活跃率 66%</span>',
                'icon': 'fa-user-check',
                'icon_color': 'text-green-500',
                'bg_color': 'bg-green-50',
                'tooltip': '在所选时间范围内，有过任意 XP 获取或核销行为的用户总数。'
            },
            {
                'title': '成功晋级人次',
                'value': '1,105',
                'trend': '<span class="text-xs text-gray-400">其中 45 人晋升至专家</span>',
                'icon': 'fa-level-up-alt',
                'icon_color': 'text-yellow-500',
                'bg_color': 'bg-yellow-50',
                'tooltip': '在所选时间范围内，触发升级条件并成功晋升更高段位的人次总和。'
            },
            {
                'title': '保级失败降级人次',
                'value': '324',
                'trend': '<span class="text-xs text-red-500 font-medium"><i class="fas fa-arrow-down mr-1"></i>15%</span> <span class="text-xs text-gray-400">较上周期增加</span>',
                'icon': 'fa-level-down-alt',
                'icon_color': 'text-red-500',
                'bg_color': 'bg-red-50',
                'tooltip': '在所选时间范围内，保级期结束且未能达到保级 XP 要求，导致段位下滑的人次总和。'
            }
        ]
        
        for kpi in kpis:
            card_html = f"""
            <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 relative group cursor-help">
                <div class="flex items-center justify-between">
                    <div class="text-sm font-medium text-gray-600 flex items-center">
                        {kpi['title']}
                        <i class="far fa-question-circle text-gray-300 ml-1 hover:text-gray-500 transition-colors"></i>
                    </div>
                    <div class="w-8 h-8 rounded-md {kpi['bg_color']} flex items-center justify-center">
                        <i class="fas {kpi['icon']} {kpi['icon_color']} text-sm"></i>
                    </div>
                </div>
                <div class="mt-2 flex items-baseline gap-2">
                    <div class="text-2xl font-bold text-gray-900">{kpi['value']}</div>
                </div>
                <div class="mt-2 flex items-center gap-2">
                    {kpi['trend']}
                </div>
                <!-- Tooltip -->
                <div class="absolute left-0 bottom-full mb-2 hidden group-hover:block w-64 bg-gray-800 text-white text-xs rounded p-2 z-50 shadow-lg">
                    {kpi['tooltip']}
                    <div class="absolute left-4 top-full w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-gray-800"></div>
                </div>
            </div>
            """
            kpi_grid.append(BeautifulSoup(card_html, 'html.parser'))

    # 3. Add Left Sidebar for Party Organization Tree
    # We need to wrap the current content of <main> inside a flex container with a new sidebar
    # Wait, <main> itself is a flex container currently.
    # Let's get the <main> parent (the body) and inject a new layout inside the main area
    
    # Actually, <main> is inside the flex body along with the global prototype sidebar.
    # We can create an inner flex layout inside <main>.
    # Get all children of <main>
    children = [child for child in main_tag.contents]
    main_tag.clear()
    
    # Create the new layout structure
    inner_layout = soup.new_tag('div', attrs={'class': 'flex-1 flex overflow-hidden bg-gray-50'})
    
    # The Tree Sidebar
    tree_sidebar_html = """
    <div class="w-64 bg-white border-r border-gray-200 flex flex-col shrink-0">
        <div class="p-4 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
            <h3 class="font-bold text-gray-800 flex items-center text-sm">
                <i class="fas fa-sitemap text-blue-600 mr-2"></i>党组织筛选
            </h3>
            <span class="bg-blue-100 text-blue-600 text-xs px-2 py-0.5 rounded-full font-medium">已选 4</span>
        </div>
        
        <div class="p-3 border-b border-gray-100">
            <div class="grid grid-cols-4 gap-2 mb-3">
                <button class="border border-gray-300 rounded text-xs py-1 hover:bg-gray-50 text-gray-700">全选</button>
                <button class="border border-gray-300 rounded text-xs py-1 hover:bg-gray-50 text-gray-700">清空</button>
                <button class="border border-gray-300 rounded text-xs py-1 hover:bg-gray-50 text-gray-700 col-span-2">仅二级党委</button>
            </div>
            <div class="relative">
                <i class="fas fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs"></i>
                <input type="text" placeholder="搜索党委/党支部" class="w-full pl-8 pr-3 py-1.5 border border-gray-300 rounded text-xs focus:border-blue-500 outline-none">
            </div>
        </div>
        
        <div class="flex-1 overflow-y-auto p-3 text-sm">
            <!-- Tree Root -->
            <div class="flex items-center mb-2 cursor-pointer">
                <div class="w-4 h-4 bg-blue-600 rounded flex items-center justify-center mr-2"><i class="fas fa-minus text-white text-[10px]"></i></div>
                <i class="fas fa-university text-gray-500 mr-2"></i>
                <span class="text-gray-800 font-medium flex-1">东风集团</span>
                <span class="text-xs bg-gray-100 text-gray-500 px-1.5 rounded">3082</span>
            </div>
            
            <!-- Child 1 -->
            <div class="pl-6 mb-2">
                <div class="flex items-center cursor-pointer">
                    <div class="w-4 h-4 bg-blue-600 rounded flex items-center justify-center mr-2"><i class="fas fa-check text-white text-[10px]"></i></div>
                    <i class="fas fa-building text-blue-500 mr-2"></i>
                    <span class="text-gray-800 flex-1 truncate">东风乘用车公司</span>
                    <span class="text-[10px] bg-blue-100 text-blue-600 px-1 rounded mr-1">二级</span>
                    <span class="text-xs bg-gray-100 text-gray-500 px-1.5 rounded">892</span>
                </div>
                
                <!-- Sub children -->
                <div class="pl-6 mt-2 space-y-2">
                    <div class="flex items-center cursor-pointer opacity-60 hover:opacity-100">
                        <div class="w-4 h-4 border border-gray-300 rounded mr-2"></div>
                        <i class="fas fa-users text-gray-400 mr-2 text-xs"></i>
                        <span class="text-gray-600 flex-1 truncate text-xs">销售部党支部</span>
                    </div>
                    <div class="flex items-center cursor-pointer opacity-60 hover:opacity-100">
                        <div class="w-4 h-4 border border-gray-300 rounded mr-2"></div>
                        <i class="fas fa-users text-gray-400 mr-2 text-xs"></i>
                        <span class="text-gray-600 flex-1 truncate text-xs">制造研发党支部</span>
                    </div>
                </div>
            </div>
            
            <!-- Child 2 -->
            <div class="pl-6 mb-2 mt-2">
                <div class="flex items-center cursor-pointer">
                    <div class="w-4 h-4 bg-blue-600 rounded flex items-center justify-center mr-2"><i class="fas fa-check text-white text-[10px]"></i></div>
                    <i class="fas fa-building text-blue-500 mr-2"></i>
                    <span class="text-gray-800 flex-1 truncate">东风日产乘用车</span>
                    <span class="text-[10px] bg-blue-100 text-blue-600 px-1 rounded mr-1">二级</span>
                    <span class="text-xs bg-gray-100 text-gray-500 px-1.5 rounded">1086</span>
                </div>
            </div>
            
            <!-- Child 3 -->
            <div class="pl-6 mb-2 mt-2">
                <div class="flex items-center cursor-pointer">
                    <div class="w-4 h-4 bg-blue-600 rounded flex items-center justify-center mr-2"><i class="fas fa-check text-white text-[10px]"></i></div>
                    <i class="fas fa-building text-blue-500 mr-2"></i>
                    <span class="text-gray-800 flex-1 truncate">东风华神汽车</span>
                    <span class="text-[10px] bg-blue-100 text-blue-600 px-1 rounded mr-1">二级</span>
                    <span class="text-xs bg-gray-100 text-gray-500 px-1.5 rounded">524</span>
                </div>
            </div>
        </div>
    </div>
    """
    
    # The right side content wrapper
    content_wrapper = soup.new_tag('div', attrs={'class': 'flex-1 flex flex-col overflow-hidden relative'})
    
    # Re-append old children to the content wrapper
    for child in children:
        content_wrapper.append(child)
        
    # Append sidebar and wrapper to inner layout
    inner_layout.append(BeautifulSoup(tree_sidebar_html, 'html.parser'))
    inner_layout.append(content_wrapper)
    
    # Append inner layout to main
    main_tag.append(inner_layout)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Dashboard rewritten with organization tree, tooltips, and correct KPI headers.")
