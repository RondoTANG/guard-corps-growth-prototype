import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the FORM VIEW entirely
new_form_view = """
    <!-- FORM VIEW (Hidden by default) -->
    <main id="form-view" class="flex-1 overflow-y-auto p-6 hidden bg-[#f4f7f9]">
        <!-- Breadcrumb -->
        <div class="text-xs text-gray-500 mb-4">
            系统设置 / 文章管理 / 文章编辑
        </div>
        
        <div class="flex gap-6">
            <!-- Left Form Area -->
            <div class="flex-1 bg-white rounded shadow-sm border border-gray-200 p-8">
                <h2 class="text-lg font-bold text-gray-800 mb-8 pb-4 border-b border-gray-100">新增文章</h2>
                
                <div class="space-y-6 max-w-3xl">
                    <!-- 1. 前端样式分类 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>前端样式分类：</label>
                        <div class="flex-1 max-w-sm">
                            <select class="w-full border border-gray-300 rounded px-3 py-2 text-sm outline-none focus:border-dfblue bg-white">
                                <option class="text-gray-400">请选择</option>
                            </select>
                        </div>
                    </div>
                    
                    <!-- 2. 标题 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>标题：</label>
                        <div class="flex-1 max-w-sm">
                            <input type="text" class="w-full border border-gray-300 rounded px-3 py-2 text-sm outline-none focus:border-dfblue">
                            <p class="text-xs text-gray-400 mt-1">标题支持中英文字符，建议在32个字符以内</p>
                        </div>
                    </div>
                    
                    <!-- 3. 归属栏目 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2">归属栏目：</label>
                        <div class="flex-1 max-w-full">
                            <input type="text" class="w-full border border-gray-300 rounded px-3 py-2 text-sm outline-none focus:border-dfblue">
                        </div>
                    </div>
                    
                    <!-- 4. 封面 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>封面：</label>
                        <div class="flex-1 max-w-sm">
                            <div class="border border-dashed border-gray-300 rounded p-6 flex flex-col items-center justify-center text-center cursor-pointer hover:border-dfblue bg-gray-50">
                                <i class="fas fa-inbox text-blue-500 text-3xl mb-2"></i>
                                <p class="text-sm text-gray-500">点击或将文件拖拽到这里上传</p>
                            </div>
                            <p class="text-xs text-gray-400 mt-2">支持JPG、PNG格式图片，最大不超过2M，建议比例2:1</p>
                        </div>
                    </div>
                    
                    <!-- 5. 正文 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>正文：</label>
                        <div class="flex-1 max-w-full border border-gray-300 rounded overflow-hidden">
                            <!-- Toolbar -->
                            <div class="bg-gray-50 border-b border-gray-300 p-2 flex flex-wrap gap-2 text-gray-600 text-sm">
                                <button class="px-2 py-1 hover:bg-gray-200 rounded">正文 <i class="fas fa-caret-down text-xs"></i></button>
                                <div class="w-px h-5 bg-gray-300 my-auto"></div>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-bold"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-italic"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-underline"></i></button>
                                <div class="w-px h-5 bg-gray-300 my-auto"></div>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded">A <i class="fas fa-caret-down text-xs"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-align-left"></i> <i class="fas fa-caret-down text-xs"></i></button>
                                <div class="w-px h-5 bg-gray-300 my-auto"></div>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded text-xs text-gray-500">默认字号</button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded text-xs text-gray-500">默认字体</button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded text-xs text-gray-500">默认行高</button>
                                <div class="w-px h-5 bg-gray-300 my-auto"></div>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-list-ul"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-list-ol"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="fas fa-link"></i></button>
                                <button class="px-2 py-1 hover:bg-gray-200 rounded"><i class="far fa-image"></i></button>
                            </div>
                            <!-- Editor Area -->
                            <textarea class="w-full h-64 p-4 outline-none resize-none text-sm" placeholder="请输入内容..."></textarea>
                        </div>
                    </div>
                    
                    <!-- 6. 排序 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2">排序：</label>
                        <div class="flex-1 max-w-sm">
                            <input type="text" class="w-24 border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-dfblue">
                            <p class="text-xs text-gray-400 mt-1">数值越大，排序越靠前</p>
                        </div>
                    </div>
                    
                    <!-- 7. 状态 -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-1"><span class="text-red-500 mr-1">*</span>状态：</label>
                        <div class="flex-1 max-w-sm flex items-center space-x-6">
                            <label class="flex items-center cursor-pointer">
                                <input type="radio" name="status" class="w-4 h-4 text-blue-500 focus:ring-blue-400" checked>
                                <span class="ml-2 text-sm text-gray-700">启用</span>
                            </label>
                            <label class="flex items-center cursor-pointer">
                                <input type="radio" name="status" class="w-4 h-4 text-blue-500 focus:ring-blue-400">
                                <span class="ml-2 text-sm text-gray-700">禁用</span>
                            </label>
                        </div>
                    </div>
                    
                    <!-- 8. 王牌护卫军联动设置 (Retained from previous requirements) -->
                    <div class="flex items-start">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-1">作者头衔联动：</label>
                        <div class="flex-1">
                            <label class="inline-flex items-center cursor-pointer group">
                                <input type="checkbox" id="aceGuardCheckbox" class="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer">
                                <span class="ml-2 text-sm text-gray-700 group-hover:text-blue-600 transition-colors">关联并入选【王牌护卫军】</span>
                            </label>
                            <p class="text-xs text-gray-400 mt-1">勾选后，若后台配置了相应的成长 XP 奖励，将在发布时自动下发。</p>
                        </div>
                    </div>
                    
                    <!-- Buttons -->
                    <div class="flex justify-center pt-8 space-x-4">
                        <button onclick="publishArticle()" class="px-6 py-2 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600 shadow-sm font-medium">保存</button>
                        <button onclick="showListView()" class="px-6 py-2 border border-gray-300 text-gray-600 rounded text-sm hover:border-[#1890ff] hover:text-[#1890ff] bg-white">返回</button>
                    </div>
                </div>
            </div>
            
            <!-- Right Phone Preview -->
            <div class="w-80 flex-shrink-0 relative">
                <!-- Phone Frame -->
                <div class="w-full h-[600px] bg-black rounded-[40px] p-3 shadow-xl relative sticky top-6">
                    <!-- Screen -->
                    <div class="w-full h-full bg-white rounded-[30px] overflow-hidden relative">
                        <!-- StatusBar -->
                        <div class="h-6 bg-black text-white flex justify-between items-center px-4 text-[10px]">
                            <span>8:30</span>
                            <div class="flex space-x-1">
                                <i class="fas fa-signal"></i>
                                <i class="fas fa-wifi"></i>
                                <i class="fas fa-battery-full"></i>
                            </div>
                        </div>
                        
                        <!-- Screen Content Placeholder -->
                        <div class="w-full h-full bg-white relative">
                            <!-- AI Assistant Floating Icon -->
                            <div class="absolute bottom-16 right-4 w-10 h-10 bg-blue-100 rounded-full flex flex-col items-center justify-center shadow-lg border border-blue-200">
                                <div class="w-6 h-6 bg-blue-500 rounded-full flex items-center justify-center text-white text-xs mb-0.5">
                                    <i class="fas fa-robot"></i>
                                </div>
                                <span class="text-[8px] text-blue-600 scale-75 origin-top font-bold">AI助手</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
"""

html = re.sub(r'<!-- FORM VIEW \(Hidden by default\) -->.*?</main>', new_form_view, html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated form view.")
