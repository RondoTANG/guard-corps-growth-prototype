from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. FIX GLOBAL TAB "历史最高段位" (Replace static text with interactive dropdowns)
tab_global = soup.find('div', id='tab-global')
if tab_global:
    for strong in tab_global.find_all('strong', class_='text-gray-900'):
        if '曾任大师' in strong.text:
            static_box = strong.find_parent('div')
            if static_box:
                static_box.replace_with(BeautifulSoup('''
                <div class="mt-4 flex flex-col space-y-3 w-full max-w-2xl">
                    <div class="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-200 hover:border-gray-300 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="text-sm text-gray-700 font-medium">规则 1:</span>
                            <span class="text-sm text-gray-600">曾达</span>
                            <select class="border border-gray-300 rounded px-2 py-1.5 text-sm bg-white focus:border-dfred outline-none cursor-pointer">
                                <option selected>大师 (Level 4)</option>
                                <option>专家 (Level 3)</option>
                            </select>
                            <span class="text-sm text-gray-600">，清零后最低跌至</span>
                            <select class="border border-gray-300 rounded px-2 py-1.5 text-sm bg-white focus:border-dfred outline-none cursor-pointer">
                                <option>专家 (Level 3)</option>
                                <option selected>熟练 (Level 2)</option>
                                <option>新秀 (Level 1)</option>
                            </select>
                        </div>
                        <button class="text-red-400 hover:text-red-600 px-2 cursor-pointer"><i class="fas fa-trash-alt"></i></button>
                    </div>
                    <div>
                        <button class="text-sm text-blue-600 hover:text-blue-800 border border-dashed border-blue-300 rounded-lg px-4 py-2 hover:bg-blue-50 transition-colors cursor-pointer">
                            <i class="fas fa-plus mr-1"></i> 新增兜底规则
                        </button>
                    </div>
                </div>
                ''', 'html.parser'))
            break

# 2. ADD MODAL FOR "对比线上版本/查看历史版本"
# First find any links that trigger it and add onclick
for a in soup.find_all('a'):
    if a.text and ('对比线上版本' in a.text or '查看历史版本' in a.text):
        a['onclick'] = 'openVersionModal(event)'

# Inject modal HTML and JS
existing_modal = soup.find('div', id='version-modal-overlay')
if existing_modal:
    existing_modal.decompose()

modal_html = """
<!-- Version Compare Modal Overlay -->
<div id="version-modal-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-[60] hidden flex items-center justify-center transition-opacity" style="display: none;">
    <!-- Modal Content -->
    <div class="bg-white rounded-lg shadow-xl w-[800px] max-h-[90vh] flex flex-col transform scale-95 transition-transform" id="version-modal-content">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50 rounded-t-lg">
            <h3 class="text-lg font-bold text-gray-900 flex items-center"><i class="fas fa-history text-blue-600 mr-2"></i> 对比线上版本</h3>
            <button onclick="closeVersionModal()" class="text-gray-400 hover:text-gray-600 cursor-pointer"><i class="fas fa-times text-xl"></i></button>
        </div>
        <div class="p-6 overflow-y-auto flex-1 bg-gray-50">
            <!-- Mock Diff View -->
            <div class="bg-white border border-gray-200 rounded-lg shadow-sm">
                <div class="grid grid-cols-2 divide-x divide-gray-200 border-b border-gray-200 text-sm font-medium text-gray-500">
                    <div class="p-3 text-center bg-green-50 text-green-700">当前线上运行版本 (V1.2)</div>
                    <div class="p-3 text-center bg-yellow-50 text-yellow-700">当前草稿 (未发布)</div>
                </div>
                <div class="p-6">
                    <div class="mb-6">
                        <h4 class="text-sm font-bold text-gray-800 mb-3 border-l-4 border-blue-500 pl-2">Level 4 大师护卫军 - 基础赚分权限</h4>
                        <div class="grid grid-cols-2 gap-6">
                            <div class="p-3 border border-red-200 bg-red-50 rounded-md text-sm text-gray-700 line-through decoration-red-400">基础赚分 x 1.2倍</div>
                            <div class="p-3 border border-green-200 bg-green-50 rounded-md text-sm text-gray-700 font-bold text-green-800">基础赚分 x <span class="bg-green-200 px-1 rounded">1.5</span> 倍</div>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-gray-800 mb-3 border-l-4 border-blue-500 pl-2">Level 4 大师护卫军 - 特权说明</h4>
                        <div class="grid grid-cols-2 gap-6">
                            <div class="p-3 border border-gray-200 rounded-md text-sm text-gray-600">直面高管圆桌会、专属勋章</div>
                            <div class="p-3 border border-green-200 bg-green-50 rounded-md text-sm text-gray-700">直面高管圆桌会、专属勋章、<span class="bg-green-200 px-1 rounded font-bold text-green-800">+ 年度盛典VVIP</span></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-4 flex items-start gap-2 text-sm text-gray-500 bg-blue-50 p-3 rounded-md border border-blue-100">
                <i class="fas fa-info-circle text-blue-500 mt-0.5"></i>
                <p>提示：你可以选择将草稿覆盖为线上版本的状态，或者继续编辑草稿。<strong class="text-red-500">（覆盖草稿将丢失当前所有未发布的修改）</strong></p>
            </div>
        </div>
        <div class="px-6 py-4 border-t border-gray-200 flex justify-between items-center bg-white rounded-b-lg">
            <button onclick="closeVersionModal()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors cursor-pointer">关闭</button>
            <button onclick="closeVersionModal(); showToast('已成功将线上版本覆盖至当前草稿')" class="px-4 py-2 bg-yellow-500 text-white rounded-md text-sm font-medium hover:bg-yellow-600 transition-colors shadow-sm cursor-pointer"><i class="fas fa-copy mr-1"></i> 使用线上版本覆盖草稿</button>
        </div>
    </div>
</div>
<script>
    function openVersionModal(e) {
        if(e) e.preventDefault();
        const overlay = document.getElementById('version-modal-overlay');
        const content = document.getElementById('version-modal-content');
        if (overlay && content) {
            overlay.classList.remove('hidden');
            overlay.style.display = 'flex';
            setTimeout(() => {
                content.classList.remove('scale-95');
                content.classList.add('scale-100');
            }, 10);
        }
    }
    function closeVersionModal() {
        const overlay = document.getElementById('version-modal-overlay');
        const content = document.getElementById('version-modal-content');
        if (content) {
            content.classList.remove('scale-100');
            content.classList.add('scale-95');
            setTimeout(() => {
                if(overlay) {
                    overlay.classList.add('hidden');
                    overlay.style.display = 'none';
                }
            }, 200);
        }
    }
</script>
"""
soup.body.append(BeautifulSoup(modal_html, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modal and global tab fixes applied successfully.")
