import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

new_editor_html = """
                    <!-- 5. 正文内容 (集成开源微信公众号排版编辑器) -->
                    <div class="flex mt-6 w-full">
                        <label class="w-32 shrink-0 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>正文内容：</label>
                        <div class="flex-1 min-w-0 border border-gray-300 rounded overflow-hidden flex flex-col relative h-[600px] bg-white">
                            <!-- 标注说明 -->
                            <div class="w-full bg-blue-50 text-blue-600 text-xs py-2 px-4 border-b border-blue-100 flex justify-between items-center z-10 shrink-0">
                                <span class="flex items-center"><i class="fas fa-info-circle mr-1.5 text-blue-500"></i> 已集成微信公众号排版组件 (基于 <a href="https://github.com/KID-1912/tiptap-appmsg-editor" target="_blank" class="font-bold underline mx-1 hover:text-blue-800 transition-colors">tiptap-appmsg-editor</a>) ，支持 135/壹伴 等第三方微信图文样式直接渲染。</span>
                            </div>
                            
                            <!-- Editor Workspace -->
                            <div class="flex flex-1 overflow-hidden w-full">
                                <!-- Left Sidebar: Style Templates -->
                                <div class="w-56 shrink-0 bg-white border-r border-gray-200 flex flex-col z-0">
                                    <div class="flex text-xs text-center border-b border-gray-200 bg-gray-50 shrink-0">
                                        <div class="flex-1 py-2.5 font-bold text-[#1890ff] border-b-2 border-[#1890ff] bg-white cursor-pointer">样式库</div>
                                        <div class="flex-1 py-2.5 text-gray-500 cursor-pointer hover:text-gray-700 transition-colors">模板库</div>
                                    </div>
                                    <div class="flex-1 overflow-y-auto p-3 space-y-3 bg-gray-50/50">
                                        <!-- Mock Style Items -->
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-all shadow-sm">标题样式一</div>
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-all shadow-sm">引言样式</div>
                                        <div class="h-24 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-all shadow-sm">图文组合排版</div>
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-all shadow-sm">分割线</div>
                                        <div class="h-20 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-all shadow-sm">底部二维码</div>
                                    </div>
                                </div>
                                
                                <!-- Right Area: Toolbar + Canvas -->
                                <div class="flex-1 min-w-0 flex flex-col z-0 bg-[#f0f2f5]">
                                    <!-- Toolbar -->
                                    <div class="bg-white border-b border-gray-200 px-3 py-2 flex flex-wrap gap-1 text-gray-600 shadow-sm items-center shrink-0 w-full">
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-500 transition-colors" title="撤销"><i class="fas fa-undo"></i></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-500 transition-colors" title="重做"><i class="fas fa-redo"></i></button>
                                        <div class="w-px h-5 bg-gray-300 mx-1"></div>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm font-bold text-gray-700 transition-colors" title="加粗">B</button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm italic text-gray-700 transition-colors" title="斜体">I</button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm underline text-gray-700 transition-colors" title="下划线">U</button>
                                        <div class="w-px h-5 bg-gray-300 mx-1"></div>
                                        <button class="w-8 h-8 flex flex-col items-center justify-center hover:bg-gray-100 rounded text-xs text-gray-700 transition-colors" title="字体颜色"><i class="fas fa-font mb-[1px]"></i><div class="w-3 h-[3px] rounded-full bg-red-500"></div></button>
                                        <button class="w-8 h-8 flex flex-col items-center justify-center hover:bg-gray-100 rounded text-xs text-gray-700 transition-colors" title="背景颜色"><i class="fas fa-fill-drip mb-[1px]"></i><div class="w-3 h-[3px] rounded-full bg-yellow-400"></div></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors" title="清除格式"><i class="fas fa-remove-format"></i></button>
                                        <div class="w-px h-5 bg-gray-300 mx-1"></div>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors"><i class="fas fa-align-left"></i></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors"><i class="fas fa-align-center"></i></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors"><i class="fas fa-align-right"></i></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors"><i class="fas fa-align-justify"></i></button>
                                        <div class="w-px h-5 bg-gray-300 mx-1"></div>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors" title="插入图片"><i class="far fa-image"></i></button>
                                        <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600 transition-colors" title="插入视频"><i class="fas fa-video"></i></button>
                                        <div class="ml-auto flex items-center space-x-2">
                                            <button class="px-3 py-1.5 hover:bg-gray-100 rounded text-xs text-gray-600 border border-gray-200 transition-colors"><i class="far fa-eye mr-1"></i> 预览</button>
                                            <button class="px-3 py-1.5 hover:bg-blue-50 rounded text-xs text-[#1890ff] border border-blue-200 transition-colors"><i class="fas fa-code mr-1"></i> 微信HTML源码</button>
                                        </div>
                                    </div>
                                    <!-- Canvas Container -->
                                    <div class="flex-1 overflow-y-auto p-6 flex justify-center w-full">
                                        <!-- Tiptap Canvas simulating WeChat width -->
                                        <div class="bg-white shadow-md border border-gray-200 w-full max-w-[375px] min-h-full p-5 outline-none relative group" contenteditable="true">
                                            <!-- Editor Title -->
                                            <h1 class="text-2xl font-bold mb-4 text-gray-300 group-focus:hidden pointer-events-none">文章标题</h1>
                                            <p class="text-gray-400 text-sm absolute top-16 left-5 group-focus:hidden pointer-events-none leading-relaxed">在这里输入正文，或者从左侧点击【公众号样式库】插入精美的排版组件。编辑器已自动限定为微信标准的 375px 宽度，所见即所得。</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
"""

# Regex substitution
html = re.sub(r'<!-- 5\. 正文内容 \(集成开源微信公众号排版编辑器\) -->.*?<!-- 6\. 排序 -->', new_editor_html + '\n                    <!-- 6. 排序 -->', html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed the editor style.")
