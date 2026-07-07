from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main_tag = soup.find('main')
content_area = main_tag.find('div', class_=lambda c: c and 'flex-1' in c and 'overflow-y-auto' in c)

if content_area:
    # First, let's remove any empty separator we added before
    for h2 in content_area.find_all('h2', string='XP资产流水明细'):
        if h2.parent:
            h2.parent.decompose()

    table_html = """
    <!-- XP Assets Flow Table Section -->
    <div class="mt-8 mb-4">
        <h2 class="text-lg font-bold text-gray-800 border-l-4 border-dfred pl-2">XP资产流水明细</h2>
        <p class="text-sm text-gray-500 mt-1">全站 XP 发放与核销明细账本，支持多维度对账检索。</p>
    </div>

    <!-- Filter Bar -->
    <div class="bg-white p-4 rounded-md shadow-sm border border-gray-200 flex flex-wrap gap-4 mb-4">
        <div class="flex items-center gap-2">
            <span class="text-sm text-gray-600">时间范围</span>
            <input type="date" class="border border-gray-300 rounded px-2 py-1 text-sm outline-none focus:border-blue-500" value="2023-10-01">
            <span class="text-gray-400">-</span>
            <input type="date" class="border border-gray-300 rounded px-2 py-1 text-sm outline-none focus:border-blue-500" value="2023-10-31">
        </div>
        <div class="flex items-center gap-2">
            <span class="text-sm text-gray-600">用户搜索</span>
            <input type="text" placeholder="用户ID/手机号" class="border border-gray-300 rounded px-3 py-1 text-sm outline-none focus:border-blue-500 w-48">
        </div>
        <div class="flex items-center gap-2">
            <span class="text-sm text-gray-600">业务类型</span>
            <select class="border border-gray-300 rounded px-2 py-1 text-sm outline-none focus:border-blue-500">
                <option>全部类型</option>
                <option>作业产出 (+)</option>
                <option>额外奖励 (+)</option>
                <option>人工调账 (±)</option>
                <option>到期扣除 (-)</option>
                <option>违规扣减 (-)</option>
            </select>
        </div>
        <div class="flex items-center gap-2 ml-auto">
            <button class="bg-blue-600 text-white px-4 py-1.5 rounded text-sm hover:bg-blue-700 font-medium"><i class="fas fa-search mr-1"></i> 查询</button>
            <button class="bg-white border border-gray-300 text-gray-700 px-4 py-1.5 rounded text-sm hover:bg-gray-50 font-medium">重置</button>
            <button class="bg-white border border-blue-200 text-blue-600 px-4 py-1.5 rounded text-sm hover:bg-blue-50 font-medium ml-2"><i class="fas fa-download mr-1"></i> 导出</button>
        </div>
    </div>

    <!-- Data Table -->
    <div class="bg-white border border-gray-200 rounded-md shadow-sm overflow-hidden mb-6">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
                <tr>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">流水号 / 时间</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">用户信息</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">业务类型 / 详细描述</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">变动额度</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">变动后余额</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-64">特殊标记 (防刷阀门)</th>
                </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-100 text-sm">
                <tr class="hover:bg-gray-50">
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="text-gray-900 font-mono text-xs">TX_20231024_8891</div>
                        <div class="text-gray-500 text-xs mt-1">2023-10-24 14:30:22</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="flex items-center">
                            <img class="h-8 w-8 rounded-full bg-gray-200" src="https://ui-avatars.com/api/?name=张三&background=random" alt="">
                            <div class="ml-3">
                                <div class="text-gray-900 font-medium">张三 (ID:10086)</div>
                                <div class="text-gray-500 text-xs">专家护卫军</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 py-1 text-xs font-semibold rounded bg-green-100 text-green-800">作业产出</span>
                        <div class="text-gray-600 mt-1">完成原创试驾作业（知乎平台）</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <span class="text-green-600 font-bold text-lg">+100</span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">
                        1,450
                    </td>
                    <td class="px-6 py-4">
                        <span class="text-gray-400">-</span>
                    </td>
                </tr>
                <tr class="hover:bg-gray-50">
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="text-gray-900 font-mono text-xs">TX_20231024_8892</div>
                        <div class="text-gray-500 text-xs mt-1">2023-10-24 15:10:05</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="flex items-center">
                            <img class="h-8 w-8 rounded-full bg-gray-200" src="https://ui-avatars.com/api/?name=李四&background=random" alt="">
                            <div class="ml-3">
                                <div class="text-gray-900 font-medium">李四 (ID:10245)</div>
                                <div class="text-gray-500 text-xs">大师护卫军</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 py-1 text-xs font-semibold rounded bg-green-100 text-green-800">作业产出</span>
                        <div class="text-gray-600 mt-1">完成日常互动转发（微信视频号）</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <span class="text-green-600 font-bold text-lg">+10</span>
                        <span class="text-gray-400 line-through text-xs ml-1">(原应发: 20)</span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">
                        2,800
                    </td>
                    <td class="px-6 py-4">
                        <div class="bg-red-50 text-red-700 text-xs p-2 rounded border border-red-100">
                            <i class="fas fa-shield-alt mr-1"></i> 已达该项每月封顶阀门上限，超额 10 XP 被截断。
                        </div>
                    </td>
                </tr>
                <tr class="hover:bg-gray-50">
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="text-gray-900 font-mono text-xs">TX_20231025_0012</div>
                        <div class="text-gray-500 text-xs mt-1">2023-10-25 09:00:00</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="flex items-center">
                            <img class="h-8 w-8 rounded-full bg-gray-200" src="https://ui-avatars.com/api/?name=王五&background=random" alt="">
                            <div class="ml-3">
                                <div class="text-gray-900 font-medium">王五 (ID:9952)</div>
                                <div class="text-gray-500 text-xs">熟练护卫军</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 py-1 text-xs font-semibold rounded bg-gray-100 text-gray-800">到期扣除</span>
                        <div class="text-gray-600 mt-1">12个月前历史XP自动过期失效</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <span class="text-gray-600 font-bold text-lg">-150</span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">
                        350
                    </td>
                    <td class="px-6 py-4">
                        <span class="text-gray-400">-</span>
                    </td>
                </tr>
            </tbody>
        </table>
        
        <!-- Pagination -->
        <div class="bg-white px-4 py-3 border-t border-gray-200 flex items-center justify-between sm:px-6">
            <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                <div>
                    <p class="text-sm text-gray-700">
                        显示第 <span class="font-medium">1</span> 到 <span class="font-medium">3</span> 条数据，共 <span class="font-medium">24,582</span> 条
                    </p>
                </div>
                <div>
                    <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                        <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                            <span class="sr-only">上一页</span>
                            <i class="fas fa-chevron-left"></i>
                        </a>
                        <a href="#" aria-current="page" class="z-10 bg-blue-50 border-blue-500 text-blue-600 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 1 </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 2 </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 3 </a>
                        <span class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700"> ... </span>
                        <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                            <span class="sr-only">下一页</span>
                            <i class="fas fa-chevron-right"></i>
                        </a>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    """
    
    table_soup = BeautifulSoup(table_html, 'html.parser')
    content_area.append(table_soup)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Appended table successfully.")
