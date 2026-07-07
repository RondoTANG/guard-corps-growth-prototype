import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the Search Form
new_search_form = """
            <!-- Search Form -->
            <div class="flex flex-wrap items-center gap-4 mb-4">
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">文章ID：</label>
                    <input type="text" class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">文章标题：</label>
                    <input type="text" class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">栏目：</label>
                    <select class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue bg-white text-gray-600">
                        <option>一级分类</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">创建人：</label>
                    <input type="text" class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">状态：</label>
                    <select class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue bg-white text-gray-600">
                        <option>全部</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">是否开启打赏：</label>
                    <select class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue bg-white text-gray-600">
                        <option>全部</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">作者ID：</label>
                    <input type="text" class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">作者姓名：</label>
                    <input type="text" class="border border-gray-300 rounded px-2 py-1 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                </div>
            </div>
            
            <div class="flex flex-wrap items-center justify-between mb-6">
                <div class="flex items-center space-x-2">
                    <button onclick="showFormView()" class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600">新增文章</button>
                    <button class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600">查询</button>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 text-right">创建时间：</label>
                    <div class="flex items-center border border-gray-300 rounded px-3 py-1 bg-white">
                        <input type="text" class="text-sm w-24 outline-none text-gray-400" placeholder="开始时间">
                        <span class="text-gray-300 mx-1">~</span>
                        <input type="text" class="text-sm w-24 outline-none text-gray-400" placeholder="结束时间">
                        <i class="far fa-calendar-alt text-gray-400 ml-2"></i>
                    </div>
                </div>
            </div>
"""
html = re.sub(r'<!-- Search Form -->.*?(?=<!-- Table -->)', new_search_form, html, flags=re.DOTALL)

# 2. Update Table Headers
new_thead = """
                    <thead class="bg-gray-50 text-gray-500 text-sm">
                        <tr>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">ID</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">文章标题</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">栏目</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">状态</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100 bg-yellow-300 text-gray-700">关联文章作者ID</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100 bg-yellow-300 text-gray-700">关联文章作者姓名</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100 bg-yellow-300 text-gray-700">是否开启打赏</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100 bg-yellow-300 text-gray-700">打赏积分总上限</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100 bg-yellow-300 text-gray-700">获得打赏积分</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">创建人</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">创建时间</th>
                            <th class="py-3 px-2 text-center font-normal border-b border-gray-100">操作</th>
                        </tr>
                    </thead>
"""
html = re.sub(r'<thead.*?</thead>', new_thead, html, flags=re.DOTALL)

# 3. Update Table Rows
# We will just replace the tbody entirely
new_tbody = """
                    <tbody class="text-sm text-gray-700 divide-y divide-gray-100">
                        <tr class="hover:bg-blue-50 transition-colors text-center">
                            <td class="py-3 px-2">10</td>
                            <td class="py-3 px-2">周末也在加班</td>
                            <td class="py-3 px-2">学习中心-操作指引</td>
                            <td class="py-3 px-2">启用</td>
                            <td class="py-3 px-2 bg-yellow-300">11111111111</td>
                            <td class="py-3 px-2 bg-yellow-300">张三</td>
                            <td class="py-3 px-2 bg-yellow-300">是</td>
                            <td class="py-3 px-2 bg-yellow-300">10</td>
                            <td class="py-3 px-2 bg-yellow-300 text-blue-500">10</td>
                            <td class="py-3 px-2">张三</td>
                            <td class="py-3 px-2">2020-10-11 12:43:32</td>
                            <td class="py-3 px-2 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline">删除</a>
                                <a href="#" class="hover:underline text-red-500">复制</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors text-center">
                            <td class="py-3 px-2">9</td>
                            <td class="py-3 px-2">周末也在加班</td>
                            <td class="py-3 px-2">学习中心-操作指引</td>
                            <td class="py-3 px-2">禁用</td>
                            <td class="py-3 px-2 bg-yellow-300">11111111111</td>
                            <td class="py-3 px-2 bg-yellow-300">张三</td>
                            <td class="py-3 px-2 bg-yellow-300">否</td>
                            <td class="py-3 px-2 bg-yellow-300">-</td>
                            <td class="py-3 px-2 bg-yellow-300 text-blue-500">-</td>
                            <td class="py-3 px-2">梨子</td>
                            <td class="py-3 px-2">2020-10-11 12:43:32</td>
                            <td class="py-3 px-2 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline">删除</a>
                                <a href="#" class="hover:underline text-red-500">复制</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors text-center">
                            <td class="py-3 px-2">8</td>
                            <td class="py-3 px-2">周末也在加班</td>
                            <td class="py-3 px-2">学习中心-操作指引</td>
                            <td class="py-3 px-2">启用</td>
                            <td class="py-3 px-2 bg-yellow-300">11111111111</td>
                            <td class="py-3 px-2 bg-yellow-300">张三</td>
                            <td class="py-3 px-2 bg-yellow-300">是</td>
                            <td class="py-3 px-2 bg-yellow-300">10</td>
                            <td class="py-3 px-2 bg-yellow-300 text-blue-500">10</td>
                            <td class="py-3 px-2">李四</td>
                            <td class="py-3 px-2">2020-10-11 12:43:32</td>
                            <td class="py-3 px-2 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline">删除</a>
                                <a href="#" class="hover:underline text-red-500">复制</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors text-center">
                            <td class="py-3 px-2">5</td>
                            <td class="py-3 px-2">周末也在加班</td>
                            <td class="py-3 px-2">学习中心-操作指引</td>
                            <td class="py-3 px-2">禁用</td>
                            <td class="py-3 px-2 bg-yellow-300">-</td>
                            <td class="py-3 px-2 bg-yellow-300">-</td>
                            <td class="py-3 px-2 bg-yellow-300">否</td>
                            <td class="py-3 px-2 bg-yellow-300">-</td>
                            <td class="py-3 px-2 bg-yellow-300 text-blue-500">-</td>
                            <td class="py-3 px-2">Jenny</td>
                            <td class="py-3 px-2">2020-10-11 12:43:32</td>
                            <td class="py-3 px-2 space-x-1 text-[#1890ff]">
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline">删除</a>
                                <a href="#" class="hover:underline text-red-500">复制</a>
                            </td>
                        </tr>
                    </tbody>
"""
html = re.sub(r'<tbody.*?</tbody>', new_tbody, html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated list view.")
