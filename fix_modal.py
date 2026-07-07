from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

overlay = soup.find('div', id='version-modal-overlay')
if overlay:
    content = overlay.find('div', id='version-modal-content')
    if content:
        # Replace the entire content block
        content.replace_with(BeautifulSoup("""
    <div class="bg-white rounded-lg shadow-xl w-[700px] max-h-[90vh] flex flex-col transform scale-95 transition-transform" id="version-modal-content">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50 rounded-t-lg">
            <h3 class="text-lg font-bold text-gray-900 flex items-center"><i class="fas fa-cloud text-blue-600 mr-2"></i> 线上运行版本预览</h3>
            <button onclick="closeVersionModal()" class="text-gray-400 hover:text-gray-600 cursor-pointer"><i class="fas fa-times text-xl"></i></button>
        </div>
        <div class="p-6 overflow-y-auto flex-1 bg-gray-50">
            <!-- Read Only Online View -->
            <div class="bg-white border border-gray-200 rounded-lg shadow-sm p-6 relative">
                <div class="absolute top-0 right-0 bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">线上生效中 (版本号: V1.2)</div>
                <h4 class="text-sm font-bold text-gray-800 mb-4 border-l-4 border-blue-500 pl-2">【等级门槛与特权】配置快照</h4>
                
                <div class="space-y-4">
                    <div class="flex items-start justify-between border-b border-gray-100 pb-3">
                        <div>
                            <div class="text-sm font-bold text-gray-900">Level 4 大师护卫军</div>
                            <div class="text-xs text-gray-500 mt-1">门槛: 20000 XP</div>
                        </div>
                        <div class="text-right">
                            <div class="text-sm text-gray-700">赚分特权: <span class="font-bold text-gray-900">1.2 倍</span></div>
                            <div class="text-xs text-gray-500 mt-1">直面高管圆桌会、专属勋章</div>
                        </div>
                    </div>
                    <div class="flex items-start justify-between border-b border-gray-100 pb-3">
                        <div>
                            <div class="text-sm font-bold text-gray-900">Level 3 核心护卫军</div>
                            <div class="text-xs text-gray-500 mt-1">门槛: 5000 XP</div>
                        </div>
                        <div class="text-right">
                            <div class="text-sm text-gray-700">赚分特权: <span class="font-bold text-gray-900">1.0 倍</span></div>
                            <div class="text-xs text-gray-500 mt-1">无</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-4 flex items-start gap-2 text-sm text-gray-500 bg-orange-50 p-3 rounded-md border border-orange-100">
                <i class="fas fa-exclamation-triangle text-orange-500 mt-0.5"></i>
                <p>如果你选择“使用此版本覆盖草稿”，你当前<strong class="text-orange-600">未发布的修改将被全部清空并还原</strong>为上述配置。</p>
            </div>
        </div>
        <div class="px-6 py-4 border-t border-gray-200 flex justify-between items-center bg-white rounded-b-lg">
            <button onclick="closeVersionModal()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors cursor-pointer">关闭</button>
            <button onclick="closeVersionModal(); showToast('已成功将线上版本覆盖至当前草稿')" class="px-4 py-2 bg-yellow-500 text-white rounded-md text-sm font-medium hover:bg-yellow-600 transition-colors shadow-sm cursor-pointer"><i class="fas fa-undo mr-1"></i> 使用线上版本覆盖草稿</button>
        </div>
    </div>
        """, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modal simplified successfully.")
