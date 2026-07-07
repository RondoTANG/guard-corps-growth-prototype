import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

new_editor_html = """
                    <!-- 5. 正文内容 (集成开源微信公众号排版编辑器) -->
                    <div class="flex">
                        <label class="w-32 text-right text-sm text-gray-700 mr-4 pt-2"><span class="text-red-500 mr-1">*</span>正文内容：</label>
                        <div class="flex-1 border border-gray-300 rounded overflow-hidden flex flex-col relative h-[500px]">
                            <!-- 标注说明 -->
                            <div class="absolute top-0 left-0 w-full bg-blue-50 text-blue-600 text-xs py-1.5 px-3 border-b border-blue-100 flex justify-between items-center z-10 shadow-sm">
                                <span><i class="fas fa-info-circle mr-1"></i> 已集成微信公众号排版组件 (基于 <a href="https://github.com/KID-1912/tiptap-appmsg-editor" target="_blank" class="font-bold underline">tiptap-appmsg-editor</a>) ，支持 135/壹伴 等第三方微信样式库的直接应用与渲染。</span>
                            </div>
                            
                            <!-- Editor Workspace -->
                            <div class="flex flex-1 mt-7">
                                <!-- Left Sidebar: Style Templates -->
                                <div class="w-48 bg-white border-r border-gray-200 flex flex-col z-0">
                                    <div class="flex text-xs text-center border-b border-gray-200 bg-gray-50">
                                        <div class="flex-1 py-2 font-bold text-[#1890ff] border-b-2 border-[#1890ff] bg-white cursor-pointer">样式库</div>
                                        <div class="flex-1 py-2 text-gray-500 cursor-pointer hover:text-gray-700">模板库</div>
                                    </div>
                                    <div class="flex-1 overflow-y-auto p-2 space-y-3 bg-gray-50">
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-colors">标题样式一</div>
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-colors">引言样式</div>
                                        <div class="h-24 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-colors">图文组合排版</div>
                                        <div class="h-16 bg-white border border-dashed border-gray-300 flex items-center justify-center text-xs text-gray-400 hover:border-blue-400 hover:text-blue-500 cursor-pointer rounded transition-colors">分割线</div>
                                    </div>
                                </div>
                                
                                <!-- Right Area: Toolbar + Canvas -->
                                <div class="flex-1 flex flex-col bg-gray-100 z-0">
                                    <!-- Toolbar -->
                                    <div class="bg-white border-b border-gray-200 p-2 flex flex-wrap gap-1 text-gray-600 shadow-sm items-center">
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-500" title="撤销"><i class="fas fa-undo"></i></button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-500" title="重做"><i class="fas fa-redo"></i></button>
                                        <div class="w-px h-4 bg-gray-300 mx-1"></div>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm font-bold text-gray-700" title="加粗">B</button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm italic text-gray-700" title="斜体">I</button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm underline text-gray-700" title="下划线">U</button>
                                        <div class="w-px h-4 bg-gray-300 mx-1"></div>
                                        <button class="w-7 h-7 flex flex-col items-center justify-center hover:bg-gray-100 rounded text-xs text-gray-700" title="字体颜色"><i class="fas fa-font mb-[1px]"></i><div class="w-3 h-[2px] bg-red-500"></div></button>
                                        <button class="w-7 h-7 flex flex-col items-center justify-center hover:bg-gray-100 rounded text-xs text-gray-700" title="背景颜色"><i class="fas fa-fill-drip mb-[1px]"></i><div class="w-3 h-[2px] bg-yellow-400"></div></button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600" title="清除格式"><i class="fas fa-remove-format"></i></button>
                                        <div class="w-px h-4 bg-gray-300 mx-1"></div>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600"><i class="fas fa-align-left"></i></button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600"><i class="fas fa-align-center"></i></button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600"><i class="fas fa-align-right"></i></button>
                                        <div class="w-px h-4 bg-gray-300 mx-1"></div>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600" title="插入图片"><i class="far fa-image"></i></button>
                                        <button class="w-7 h-7 flex items-center justify-center hover:bg-gray-100 rounded text-sm text-gray-600" title="插入视频"><i class="fas fa-video"></i></button>
                                        <button class="px-3 py-1 hover:bg-blue-50 rounded text-xs text-[#1890ff] ml-auto border border-blue-200"><i class="fas fa-code mr-1"></i> 微信HTML源码</button>
                                    </div>
                                    <!-- Canvas Container -->
                                    <div class="flex-1 overflow-y-auto p-4 flex justify-center bg-gray-100">
                                        <!-- Tiptap Canvas simulating WeChat width -->
                                        <div class="bg-white shadow-sm border border-gray-200 w-full max-w-[375px] min-h-full p-4 outline-none relative group" contenteditable="true">
                                            <p class="text-gray-400 text-sm italic absolute top-4 left-4 group-focus:hidden pointer-events-none">在这里编辑正文，或者从左侧点击公众号样式库插入...</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
"""

# Replace the block from <!-- 5. 正文内容 --> to the end of its div right before <!-- 6. 排序 -->
html = re.sub(r'<!-- 5\. 正文内容 -->.*?<!-- 6\. 排序 -->', new_editor_html + '\n                    <!-- 6. 排序 -->', html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Replaced simple textarea with tiptap-appmsg-editor mockup.")
