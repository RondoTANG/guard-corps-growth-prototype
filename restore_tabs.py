import re

file_path = "B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# I need to find the <div id="tab-tier" class="block">...<div id="tab-global" class="hidden">
# and replace everything in between with the correct tab-tier content.
# Then I need to find <div id="tab-global" class="hidden">...<div id="tab-task" class="hidden">
# and replace everything in between with the correct tab-global content.

# Let's just completely replace the div blocks.

tab_tier_html = """<div id="tab-tier" class="block">
                        <div class="overflow-x-auto">
                            <table class="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg">
                                <thead class="bg-gray-50">
                                    <tr>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">系统等级</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-48">前台展示段位名称</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-48">升级门槛 (近12个月XP)</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-40">基础赚分权限</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">专属高级特权说明</th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-200">
                                    <tr>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 bg-gray-50">Level 1</td>
                                        <td class="px-6 py-4 whitespace-nowrap"><input type="text" value="新秀护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                        <td class="px-6 py-4 whitespace-nowrap"><div class="flex items-center text-sm">默认 <span class="font-bold ml-1">0</span> XP</div></td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">基础赚分</td>
                                        <td class="px-6 py-4"><input type="text" value="--" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                    </tr>
                                    <tr>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 bg-gray-50">Level 2</td>
                                        <td class="px-6 py-4 whitespace-nowrap"><input type="text" value="熟练护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                        <td class="px-6 py-4 whitespace-nowrap"><div class="flex items-center gap-2"><input type="number" value="1000" class="w-24 border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"><span class="text-sm text-gray-500">XP</span></div></td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">基础赚分 x 1.1倍</td>
                                        <td class="px-6 py-4"><input type="text" value="解锁周边兑换商城资格" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                    </tr>
                                    <tr>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 bg-yellow-50 text-yellow-800">Level 3</td>
                                        <td class="px-6 py-4 whitespace-nowrap"><input type="text" value="核心护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                        <td class="px-6 py-4 whitespace-nowrap"><div class="flex items-center gap-2"><input type="number" value="5000" class="w-24 border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"><span class="text-sm text-gray-500">XP</span></div></td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">基础赚分 x 1.2倍</td>
                                        <td class="px-6 py-4"><input type="text" value="专属作业优先分配权、线下活动邀请资格" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                    </tr>
                                    <tr>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 bg-red-50 text-dfred">Level 4</td>
                                        <td class="px-6 py-4 whitespace-nowrap"><input type="text" value="大师护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                        <td class="px-6 py-4 whitespace-nowrap"><div class="flex items-center gap-2"><input type="number" value="20000" class="w-24 border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"><span class="text-sm text-gray-500">XP</span></div></td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">基础赚分 x 1.5倍</td>
                                        <td class="px-6 py-4"><input type="text" value="直面高管圆桌会、专属勋章、年度盛典VVIP" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred outline-none"></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>"""

tab_global_html = """<div id="tab-global" class="hidden">
                        <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-6 space-y-6">
                            <div>
                                <h3 class="text-base font-medium text-gray-900 border-b pb-2 mb-4">全局保级周期设定</h3>
                                <div class="grid grid-cols-2 gap-6">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1">滚动结算周期</label>
                                        <select class="w-full border-gray-300 rounded-md shadow-sm p-2 border focus:border-dfred outline-none">
                                            <option>近30天</option>
                                            <option>近90天</option>
                                            <option selected>近12个月 (滚动)</option>
                                        </select>
                                        <p class="text-xs text-gray-500 mt-1">系统将基于此周期统计总XP进行降级判断</p>
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1">保级宽限期 (缓冲期)</label>
                                        <div class="flex items-center gap-2">
                                            <input type="number" value="30" class="w-24 border-gray-300 rounded-md shadow-sm p-2 border focus:border-dfred outline-none">
                                            <span class="text-sm text-gray-600">天</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <h3 class="text-base font-medium text-gray-900 border-b pb-2 mb-4">降级软着陆规则</h3>
                                <div class="flex items-center justify-between bg-gray-50 p-4 rounded-md">
                                    <div>
                                        <div class="font-medium text-gray-800 text-sm">开启降级软着陆保护</div>
                                        <div class="text-xs text-gray-500 mt-1">开启后，高段位用户触发降级时不会直接跌至 Level 1，而是按配置的最大跌幅处理。</div>
                                    </div>
                                    <div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in">
                                        <input type="checkbox" id="global-toggle-1" checked class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer" />
                                        <label for="global-toggle-1" class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300 cursor-pointer"></label>
                                    </div>
                                </div>
                                <div class="mt-4 flex items-center gap-2">
                                    <span class="text-sm text-gray-700">单次降级最大跨度：</span>
                                    <select class="border-gray-300 rounded-md shadow-sm p-1.5 border text-sm focus:border-dfred outline-none">
                                        <option>无限制</option>
                                        <option selected>不超过 1 个段位</option>
                                        <option>不超过 2 个段位</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>"""

html = re.sub(r'<div id="tab-tier" class="block">.*?<div id="tab-global" class="hidden">', tab_tier_html + '\n                    <div id="tab-global" class="hidden">', html, flags=re.DOTALL)
html = re.sub(r'<div id="tab-global" class="hidden">.*?<div id="tab-task" class="hidden">', tab_global_html + '\n                    <div id="tab-task" class="hidden">', html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
