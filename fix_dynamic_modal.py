from bs4 import BeautifulSoup
import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Update the onclick in each tab's bottom bar
for tab_id in ['tab-tier', 'tab-global', 'tab-task']:
    tab_div = soup.find('div', id=tab_id)
    if tab_div:
        links = tab_div.find_all('a', onclick=re.compile('openVersionModal'))
        for a in links:
            a['onclick'] = f"openVersionModal(event, '{tab_id}')"

# 2. Update the Modal HTML
modal_overlay = soup.find('div', id='version-modal-overlay')
if modal_overlay:
    modal_overlay.decompose()

new_modal_html = """
<!-- Dynamic Version Modal Overlay -->
<div id="version-modal-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-[60] hidden flex items-center justify-center transition-opacity" style="display: none;">
    <!-- Modal Content -->
    <div class="bg-white rounded-lg shadow-xl w-[700px] max-h-[90vh] flex flex-col transform scale-95 transition-transform" id="version-modal-container">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50 rounded-t-lg">
            <h3 class="text-lg font-bold text-gray-900 flex items-center"><i class="fas fa-cloud text-blue-600 mr-2"></i> <span id="modal-title-text">线上运行版本预览</span></h3>
            <button onclick="closeVersionModal()" class="text-gray-400 hover:text-gray-600 cursor-pointer"><i class="fas fa-times text-xl"></i></button>
        </div>
        <div class="p-6 overflow-y-auto flex-1 bg-gray-50" id="modal-dynamic-body">
            <!-- Content injected via JS -->
        </div>
        <div class="px-6 py-4 border-t border-gray-200 flex justify-between items-center bg-white rounded-b-lg">
            <button onclick="closeVersionModal()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors cursor-pointer">关闭</button>
            <button onclick="closeVersionModal(); showToast('已成功将线上版本覆盖至当前草稿')" class="px-4 py-2 bg-yellow-500 text-white rounded-md text-sm font-medium hover:bg-yellow-600 transition-colors shadow-sm cursor-pointer"><i class="fas fa-undo mr-1"></i> 使用线上版本覆盖草稿</button>
        </div>
    </div>
</div>

<script>
    const modalData = {
        'tab-tier': {
            title: '【等级门槛与特权】配置快照',
            content: `
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
            `
        },
        'tab-global': {
            title: '【全局周期与保护规则】配置快照',
            content: `
                <div class="bg-white border border-gray-200 rounded-lg shadow-sm p-6 relative">
                    <div class="absolute top-0 right-0 bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">线上生效中 (版本号: V1.2)</div>
                    <h4 class="text-sm font-bold text-gray-800 mb-4 border-l-4 border-blue-500 pl-2">【全局周期与保护规则】配置快照</h4>
                    <div class="space-y-4">
                        <div class="bg-gray-50 p-4 rounded-md border border-gray-200">
                            <div class="text-sm font-bold text-gray-900 mb-2">保护规则 1</div>
                            <div class="text-sm text-gray-700">曾达 <span class="font-bold">大师 (Level 4)</span>，清零后最低跌至 <span class="font-bold">专家 (Level 3)</span></div>
                        </div>
                        <div class="bg-gray-50 p-4 rounded-md border border-gray-200">
                            <div class="text-sm font-bold text-gray-900 mb-2">保护规则 2</div>
                            <div class="text-sm text-gray-700">曾达 <span class="font-bold">专家 (Level 3)</span>，清零后最低跌至 <span class="font-bold">熟练 (Level 2)</span></div>
                        </div>
                    </div>
                </div>
            `
        },
        'tab-task': {
            title: '【作业 XP 产出映射】配置快照',
            content: `
                <div class="bg-white border border-gray-200 rounded-lg shadow-sm p-6 relative">
                    <div class="absolute top-0 right-0 bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">线上生效中 (版本号: V1.2)</div>
                    <h4 class="text-sm font-bold text-gray-800 mb-4 border-l-4 border-blue-500 pl-2">【作业 XP 产出映射】配置快照</h4>
                    <div class="space-y-4">
                        <div class="flex items-center justify-between border-b border-gray-100 pb-3">
                            <div class="text-sm text-gray-900">
                                <span class="font-bold mr-2">原创</span>|<span class="mx-2 text-gray-500">微信视频号</span>|<span class="mx-2 text-gray-500">原创投稿</span>
                            </div>
                            <div class="text-sm text-gray-700 text-right">
                                单次: <span class="font-bold">150 XP</span><br>
                                <span class="text-xs text-gray-500">限制: 每月最高 500 XP</span>
                            </div>
                        </div>
                        <div class="flex items-center justify-between border-b border-gray-100 pb-3">
                            <div class="text-sm text-gray-900">
                                <span class="font-bold mr-2">转发</span>|<span class="mx-2 text-gray-500">朋友圈</span>|<span class="mx-2 text-gray-500">转发文章</span>
                            </div>
                            <div class="text-sm text-gray-700 text-right">
                                单次: <span class="font-bold">10 XP</span><br>
                                <span class="text-xs text-gray-500">限制: 每日最高 50 XP</span>
                            </div>
                        </div>
                    </div>
                </div>
            `
        }
    };

    function openVersionModal(e, tabId) {
        if(e) e.preventDefault();
        
        // Populate dynamic data
        const data = modalData[tabId] || modalData['tab-tier'];
        
        const warningHtml = `
            <div class="mt-4 flex items-start gap-2 text-sm text-gray-500 bg-orange-50 p-3 rounded-md border border-orange-100">
                <i class="fas fa-exclamation-triangle text-orange-500 mt-0.5"></i>
                <p>如果你选择“使用此版本覆盖草稿”，你当前<strong class="text-orange-600">未发布的修改将被全部清空并还原</strong>为上述配置。</p>
            </div>
        `;
        
        document.getElementById('modal-dynamic-body').innerHTML = data.content + warningHtml;
        
        const overlay = document.getElementById('version-modal-overlay');
        const container = document.getElementById('version-modal-container');
        if (overlay && container) {
            overlay.classList.remove('hidden');
            overlay.style.display = 'flex';
            setTimeout(() => {
                container.classList.remove('scale-95');
                container.classList.add('scale-100');
            }, 10);
        }
    }
    
    // Fallback for old calls without arguments just in case
    window.openVersionModalOld = window.openVersionModal;
</script>
"""

# Replace the old scripts with the new ones by just removing the old ones and appending.
# Wait, the old scripts were at the bottom of the body. Let's find any script that contains openVersionModal and remove it.
for script in soup.find_all('script'):
    if script.string and 'openVersionModal' in script.string:
        script.decompose()

soup.body.append(BeautifulSoup(new_modal_html, 'html.parser'))

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Dynamic modal applied.")
