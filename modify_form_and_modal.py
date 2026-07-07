import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# The section to replace in Form View
# It currently has:
# <!-- 8. 王牌护卫军联动设置 (Retained from previous requirements) -->
# ...
# <!-- Buttons -->
# We will replace it with the new fields from Image 1.

new_author_reward_section = """
                    <!-- 8. 关联文章作者与打赏设置 -->
                    <div class="border-t border-gray-100 pt-6 mt-2 space-y-6">
                        <!-- 关联文章作者 -->
                        <div class="flex">
                            <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2">关联文章作者：</label>
                            <div class="flex-1 max-w-sm">
                                <div class="relative cursor-pointer" onclick="openUserModal()">
                                    <div class="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-white flex justify-between items-center text-gray-400 hover:border-dfblue">
                                        <span>请选择</span>
                                        <i class="fas fa-chevron-down text-xs"></i>
                                    </div>
                                </div>
                                <p class="text-xs text-gray-400 mt-2">不关联用户则默认为东风护卫军，开启打赏功能必须选择用户</p>
                            </div>
                        </div>
                        
                        <!-- 是否开启文章打赏 -->
                        <div class="flex items-center">
                            <label class="w-32 text-right text-sm text-gray-700 mr-4 font-bold text-gray-800">是否开启文章打赏：</label>
                            <div class="flex-1">
                                <label class="relative inline-flex items-center cursor-pointer">
                                    <input type="checkbox" class="sr-only peer" checked>
                                    <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-green-500"></div>
                                </label>
                            </div>
                        </div>
                        
                        <!-- 单次打赏积分上限 -->
                        <div class="flex">
                            <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>单次打赏积分上限：</label>
                            <div class="flex-1 max-w-sm">
                                <input type="text" class="w-full border border-gray-300 rounded px-3 py-2 text-sm outline-none focus:border-dfblue" placeholder="请输入上限积分，最低15积分">
                            </div>
                        </div>
                        
                        <!-- 打赏积分总上限 -->
                        <div class="flex items-center">
                            <label class="w-32 text-right text-sm text-gray-700 mr-4"><span class="text-red-500 mr-1">*</span>打赏积分总上限：</label>
                            <div class="flex-1 max-w-sm flex items-center">
                                <input type="text" class="flex-1 border border-gray-300 rounded px-3 py-2 text-sm outline-none focus:border-dfblue">
                                <label class="flex items-center ml-4 cursor-pointer">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                                    <span class="ml-2 text-sm text-gray-600">无上限</span>
                                </label>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Buttons -->
"""

# Replace the specific section
html = re.sub(r'<!-- 8\. 王牌护卫军联动设置.*?<!-- Buttons -->', new_author_reward_section, html, flags=re.DOTALL)

# Add Modal HTML at the end of the body
modal_html = """
    <!-- User Selection Modal -->
    <div id="userModal" class="fixed inset-0 bg-black bg-opacity-40 z-50 hidden flex items-center justify-center">
        <div class="bg-white rounded-lg shadow-xl w-[900px] max-h-[90vh] flex flex-col overflow-hidden">
            <!-- Header -->
            <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
                <h3 class="text-base font-bold text-gray-800">选择用户</h3>
                <button onclick="closeUserModal()" class="text-gray-400 hover:text-gray-600">
                    <i class="fas fa-times text-lg"></i>
                </button>
            </div>
            
            <!-- Body -->
            <div class="p-6 flex-1 overflow-y-auto">
                <!-- Search Form -->
                <div class="flex flex-wrap items-center gap-4 mb-6">
                    <div class="flex items-center">
                        <label class="text-sm text-gray-600 mr-2 font-bold">姓名</label>
                        <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                    </div>
                    <div class="flex items-center">
                        <label class="text-sm text-gray-600 mr-2 font-bold">手机</label>
                        <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-32 outline-none focus:border-dfblue" placeholder="请输入">
                    </div>
                    <div class="flex items-center">
                        <label class="text-sm text-gray-600 mr-2 font-bold">下属党委</label>
                        <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请输入">
                    </div>
                    <div class="flex items-center space-x-2 ml-auto">
                        <button class="px-5 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm">查询</button>
                        <button class="px-5 py-1.5 border border-gray-300 text-gray-600 bg-white rounded text-sm hover:border-[#1890ff] hover:text-[#1890ff]">重置</button>
                    </div>
                </div>
                
                <!-- Table -->
                <table class="min-w-full border-t border-gray-100 mb-4 text-center">
                    <thead class="bg-gray-100 text-gray-500 text-sm">
                        <tr>
                            <th class="py-3 px-4 font-normal">用户ID</th>
                            <th class="py-3 px-4 font-normal">手机</th>
                            <th class="py-3 px-4 font-normal">姓名</th>
                            <th class="py-3 px-4 font-normal">所在党委</th>
                            <th class="py-3 px-4 font-normal">下属党委</th>
                            <th class="py-3 px-4 font-normal">状态</th>
                            <th class="py-3 px-4 font-normal">操作</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm text-gray-600 divide-y divide-gray-100">
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">000001</td>
                            <td class="py-3 px-4">136****7322</td>
                            <td class="py-3 px-4">杨先生</td>
                            <td class="py-3 px-4">东风汽车有限公司</td>
                            <td class="py-3 px-4">数据公司</td>
                            <td class="py-3 px-4">正常</td>
                            <td class="py-3 px-4 text-[#1890ff]"><a href="#" onclick="selectUser('杨先生')" class="hover:underline">选择</a></td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">000001</td>
                            <td class="py-3 px-4">136****7322</td>
                            <td class="py-3 px-4">杨先生</td>
                            <td class="py-3 px-4">东风汽车有限公司</td>
                            <td class="py-3 px-4">数据公司</td>
                            <td class="py-3 px-4">冻结</td>
                            <td class="py-3 px-4 text-[#1890ff]"><a href="#" onclick="selectUser('杨先生')" class="hover:underline">选择</a></td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">000002</td>
                            <td class="py-3 px-4">136****7322</td>
                            <td class="py-3 px-4">张三</td>
                            <td class="py-3 px-4">东风汽车有限公司</td>
                            <td class="py-3 px-4">数据公司</td>
                            <td class="py-3 px-4">正常</td>
                            <td class="py-3 px-4 text-[#1890ff]"><a href="#" onclick="selectUser('张三')" class="hover:underline">选择</a></td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">000003</td>
                            <td class="py-3 px-4">136****7322</td>
                            <td class="py-3 px-4">李四</td>
                            <td class="py-3 px-4">东风汽车有限公司</td>
                            <td class="py-3 px-4">数据公司</td>
                            <td class="py-3 px-4">冻结</td>
                            <td class="py-3 px-4 text-[#1890ff]"><a href="#" onclick="selectUser('李四')" class="hover:underline">选择</a></td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">000004</td>
                            <td class="py-3 px-4">136****7322</td>
                            <td class="py-3 px-4">王五</td>
                            <td class="py-3 px-4">东风汽车有限公司</td>
                            <td class="py-3 px-4">数据公司</td>
                            <td class="py-3 px-4">正常</td>
                            <td class="py-3 px-4 text-[#1890ff]"><a href="#" onclick="selectUser('王五')" class="hover:underline">选择</a></td>
                        </tr>
                    </tbody>
                </table>
                
                <!-- Pagination -->
                <div class="flex items-center justify-start text-xs text-gray-500">
                    <span class="mr-4">共 200 条</span>
                    <div class="flex items-center space-x-1">
                        <button class="px-2 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">&lt;</button>
                        <button class="px-2.5 py-1 bg-[#1890ff] text-white rounded">1</button>
                        <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">2</button>
                        <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">3</button>
                        <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">4</button>
                        <span class="px-1">...</span>
                        <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">10</button>
                        <button class="px-2 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">&gt;</button>
                    </div>
                    <select class="border border-gray-300 rounded ml-4 px-2 py-1 outline-none">
                        <option>10 条/页</option>
                    </select>
                    <div class="flex items-center ml-4">
                        <span>跳至</span>
                        <input type="text" class="w-8 border border-gray-300 rounded mx-2 py-1 text-center outline-none" value="5">
                        <span>页</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- UI Description Sidebar (like in screenshot) -->
        <div class="ml-4 w-64 bg-white p-4 rounded shadow-lg text-xs text-gray-700 h-fit self-start mt-10">
            <h4 class="font-bold border-b border-gray-100 pb-2 mb-2 text-sm text-gray-800">界面逻辑说明</h4>
            <p class="font-bold mb-1">1. 【选择用户】交互说明</p>
            <p class="mb-1 text-gray-500">a) 取值：读取用户列表数据，读取身份类型为员工的数据，单选</p>
            <p class="text-gray-500">b) 查询：输入项均支持模糊查询，手机精准查询</p>
        </div>
    </div>
"""

if "id=\"userModal\"" not in html:
    html = html.replace("</body>", modal_html + "\n</body>")

# Add JS functions for the modal
js_code = """
    function openUserModal() {
        document.getElementById('userModal').classList.remove('hidden');
    }
    function closeUserModal() {
        document.getElementById('userModal').classList.add('hidden');
    }
    function selectUser(name) {
        // Update the select box display text
        const selectBox = document.querySelector('div[onclick="openUserModal()"] span');
        if (selectBox) {
            selectBox.textContent = name;
            selectBox.classList.remove('text-gray-400');
            selectBox.classList.add('text-gray-800');
        }
        closeUserModal();
    }
"""
if "function openUserModal()" not in html:
    html = html.replace("</script>", js_code + "\n</script>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated article edit page with user selection modal.")
