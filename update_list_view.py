import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the Search Form
new_search_form = """
            <!-- Search Form -->
            <div class="flex flex-wrap items-center gap-4 mb-4">
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">文章ID：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">文章标题：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">栏目：</label>
                    <select class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>请选择栏目</option>
                        <option>备选</option>
                        <option>王牌护卫军</option>
                        <option>金点子排名</option>
                        <option>通知公告</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">创建人：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
            </div>
            
            <div class="flex flex-wrap items-center gap-4 mb-4">
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">状态：</label>
                    <select class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>请选择</option>
                        <option>启用</option>
                        <option>禁用</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">发布时间：</label>
                    <div class="flex items-center border border-gray-300 rounded px-3 py-1.5 bg-white w-64">
                        <input type="text" class="text-sm w-full outline-none text-gray-400" placeholder="开始日期">
                        <span class="text-gray-300 mx-2">→</span>
                        <input type="text" class="text-sm w-full outline-none text-gray-400" placeholder="结束日期">
                        <i class="far fa-calendar-alt text-gray-400 ml-2"></i>
                    </div>
                </div>
                <!-- 迭代新增字段 -->
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">是否开启打赏：</label>
                    <select class="border border-gray-300 rounded px-3 py-1.5 text-sm w-32 outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>全部</option>
                        <option>是</option>
                        <option>否</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">作者ID：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-32 outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
            </div>
            
            <div class="flex flex-wrap items-center justify-between mb-6">
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">作者姓名：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="showFormView()" class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm font-medium">新增文章</button>
                    <button class="px-4 py-1.5 border border-gray-300 text-gray-600 bg-gray-50 rounded text-sm hover:border-[#1890ff] hover:text-[#1890ff]">重置</button>
                    <button class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm font-medium">搜索</button>
                </div>
            </div>
"""
html = re.sub(r'<!-- Search Form -->.*?(?=<!-- Table -->)', new_search_form, html, flags=re.DOTALL)

# 2. Update Table Headers
new_thead = """
                    <thead class="bg-gray-50 text-gray-500 text-sm border-b border-gray-200">
                        <tr>
                            <th class="py-3 px-4 text-left font-normal">ID</th>
                            <th class="py-3 px-4 text-left font-normal">文章标题</th>
                            <th class="py-3 px-4 text-left font-normal">归属分类</th>
                            <th class="py-3 px-4 text-left font-normal">状态</th>
                            <th class="py-3 px-4 text-left font-normal">关联文章作者ID</th>
                            <th class="py-3 px-4 text-left font-normal">关联文章作者姓名</th>
                            <th class="py-3 px-4 text-left font-normal">是否开启打赏</th>
                            <th class="py-3 px-4 text-left font-normal">打赏积分总上限</th>
                            <th class="py-3 px-4 text-left font-normal">获得打赏积分</th>
                            <th class="py-3 px-4 text-left font-normal">创建人</th>
                            <th class="py-3 px-4 text-left font-normal">创建时间</th>
                            <th class="py-3 px-4 text-left font-normal">操作</th>
                        </tr>
                    </thead>
"""
html = re.sub(r'<thead.*?</thead>', new_thead, html, flags=re.DOTALL)

# 3. Update Table Rows with real production data + new fields
# Production data titles:
# 1272 采集类作业指引指南 (备选)
# 2947 第五十九期点评言：黄阳运 (王牌护卫军)
# 2946 金点子积分榜+反馈精选（2026年6月） (金点子排名)
# 2886 第五十八期点评官：王玉 (王牌护卫军)
# 1565 第五十七期点评官：刘敏欣 (王牌护卫军)
new_tbody = """
                    <tbody class="text-sm text-gray-700 divide-y divide-gray-100">
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-4 px-4">1272</td>
                            <td class="py-4 px-4">采集类作业指引指南</td>
                            <td class="py-4 px-4">备选</td>
                            <td class="py-4 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">否</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">梁吴悠</td>
                            <td class="py-4 px-4 text-gray-500">2026-03-30 18:53:16</td>
                            <td class="py-4 px-4 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">编辑</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-4 px-4">2947</td>
                            <td class="py-4 px-4">第五十九期点评言：黄阳运</td>
                            <td class="py-4 px-4">王牌护卫军</td>
                            <td class="py-4 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-4 px-4">11111111111</td>
                            <td class="py-4 px-4">黄阳运</td>
                            <td class="py-4 px-4">是</td>
                            <td class="py-4 px-4">10</td>
                            <td class="py-4 px-4 text-blue-500">10</td>
                            <td class="py-4 px-4">梁吴悠</td>
                            <td class="py-4 px-4 text-gray-500">2026-07-03 10:51:52</td>
                            <td class="py-4 px-4 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">编辑</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-4 px-4">2946</td>
                            <td class="py-4 px-4">金点子积分榜+反馈精选（2026年6月）</td>
                            <td class="py-4 px-4">金点子排名</td>
                            <td class="py-4 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">否</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">梁吴悠</td>
                            <td class="py-4 px-4 text-gray-500">2026-07-02 14:59:45</td>
                            <td class="py-4 px-4 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">编辑</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-4 px-4">2886</td>
                            <td class="py-4 px-4">第五十八期点评官：王玉</td>
                            <td class="py-4 px-4">王牌护卫军</td>
                            <td class="py-4 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-4 px-4">11111111111</td>
                            <td class="py-4 px-4">王玉</td>
                            <td class="py-4 px-4">是</td>
                            <td class="py-4 px-4">10</td>
                            <td class="py-4 px-4 text-blue-500">5</td>
                            <td class="py-4 px-4">梁吴悠</td>
                            <td class="py-4 px-4 text-gray-500">2026-06-26 17:39:30</td>
                            <td class="py-4 px-4 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">编辑</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-4 px-4">1564</td>
                            <td class="py-4 px-4">东风护卫军任务|提醒|开通公告</td>
                            <td class="py-4 px-4">通知公告</td>
                            <td class="py-4 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">否</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">—</td>
                            <td class="py-4 px-4">梁吴悠</td>
                            <td class="py-4 px-4 text-gray-500">2026-06-05 10:24:13</td>
                            <td class="py-4 px-4 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">编辑</a>
                                <span class="text-gray-300">|</span>
                                <a href="#" class="hover:underline">删除</a>
                            </td>
                        </tr>
                    </tbody>
"""
html = re.sub(r'<tbody.*?</tbody>', new_tbody, html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated list view to match production mock data and enumerations.")
