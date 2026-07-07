import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

new_search_form = """
            <!-- Search Form -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-y-4 gap-x-6 mb-6">
                <!-- Row 1 -->
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">文章ID：</label>
                    <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">文章标题：</label>
                    <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">栏目：</label>
                    <select class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>请选择栏目</option>
                        <option>备选</option>
                        <option>王牌护卫军</option>
                        <option>金点子排名</option>
                        <option>通知公告</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">创建人：</label>
                    <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                
                <!-- Row 2 -->
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">状态：</label>
                    <select class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>请选择</option>
                        <option>启用</option>
                        <option>禁用</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">是否开启打赏：</label>
                    <select class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>全部</option>
                        <option>是</option>
                        <option>否</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">作者ID：</label>
                    <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">作者姓名：</label>
                    <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue" placeholder="请填入内容">
                </div>

                <!-- Row 3 -->
                <div class="flex items-center col-span-1 md:col-span-2 lg:col-span-2">
                    <label class="text-sm text-gray-600 mr-2 w-20 text-right whitespace-nowrap">发布时间：</label>
                    <div class="flex-1 flex items-center border border-gray-300 rounded px-3 py-1.5 bg-white">
                        <input type="text" class="text-sm w-full outline-none text-gray-400 bg-transparent" placeholder="开始日期">
                        <span class="text-gray-300 mx-2">→</span>
                        <input type="text" class="text-sm w-full outline-none text-gray-400 bg-transparent" placeholder="结束日期">
                        <i class="far fa-calendar-alt text-gray-400 ml-2"></i>
                    </div>
                </div>
                
                <!-- Buttons -->
                <div class="col-span-1 md:col-span-2 lg:col-span-2 flex items-center justify-end space-x-3">
                    <button onclick="showFormView()" class="px-5 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm font-medium transition-colors">新增文章</button>
                    <button class="px-5 py-1.5 border border-gray-300 text-gray-600 bg-gray-50 rounded text-sm hover:border-[#1890ff] hover:text-[#1890ff] transition-colors">重置</button>
                    <button class="px-5 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm font-medium transition-colors">搜索</button>
                </div>
            </div>
"""

# Find the start and end of the search form section to replace
# We previously had <!-- Search Form --> down to right before <!-- Table -->
html = re.sub(r'<!-- Search Form -->.*?(?=<!-- Table -->)', new_search_form, html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated search form layout.")
