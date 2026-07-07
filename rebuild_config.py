import re

# 1. Read base sidebar and header from B端_成长数据健康度大盘.html
with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    dashboard_html = f.read()

aside_match = re.search(r'(<aside class="w-64 bg-\[#313C48\].*?</aside>)', dashboard_html, re.DOTALL)
aside = aside_match.group(1)
# Adjust active menu to target config page
aside = re.sub(r'href="B端_成长数据健康度大盘.html"\s*class="[^"]*bg-\[#3B82F6\].*?"', 'href="B端_成长数据健康度大盘.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link"', aside)
aside = re.sub(r'href="B端_等级规则与XP配置页.html"\s*class="[^"]*hover:text-white.*?"', 'href="B端_等级规则与XP配置页.html" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu"', aside)

# 2. Extract clean tabs from B端_完整后台大盘.html
with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    spa_html = f.read()

# tab-tier
tier_match = re.search(r'<div class="block" id="tab-tier">.*?</tbody>\s*</table>\s*</div>\s*</div>', spa_html, re.DOTALL)
tab_tier = tier_match.group(0)

# tab-global
global_match = re.search(r'<div class="hidden" id="tab-global">.*?</div>\s*</div>\s*</div>', spa_html, re.DOTALL)
# The tab-global ends with <div class="hidden" id="tab-task"> starting.
# Let's cleanly extract it by matching from <div class="hidden" id="tab-global"> until <div class="hidden" id="tab-task">
global_match = re.search(r'(<div class="hidden" id="tab-global">.*?)\s*<div class="hidden" id="tab-task">', spa_html, re.DOTALL)
tab_global = global_match.group(1)

# tab-task
task_match = re.search(r'(<div class="hidden" id="tab-task">.*?)\s*</div>\s*</div>\s*</div>\s*<div id="editDrawer"', spa_html, re.DOTALL)
if not task_match:
    task_match = re.search(r'(<div class="hidden" id="tab-task">.*?)\s*<div id="editDrawer"', spa_html, re.DOTALL)
    
tab_task = task_match.group(1)
# Tab task needs closing divs. The match probably didn't grab the closing ones.
# Actually, inside tab-task there's a table. It ends with </tbody></table></div></div>
# Let's just find that.
tab_task_inner = re.search(r'(<div class="hidden" id="tab-task">.*?</tbody>\s*</table>\s*</div>\s*</div>)', spa_html, re.DOTALL)
if tab_task_inner:
    tab_task = tab_task_inner.group(1)
else:
    # Just grab up to <!-- Toast Container -->
    m = re.search(r'(<div class="hidden" id="tab-task">.*?)<!-- Toast Container -->', spa_html, re.DOTALL)
    tab_task = m.group(1)
    # trim trailing </div>s
    tab_task = re.sub(r'(</div>\s*){3,4}$', '</div>', tab_task)

# Apply Terminology Fixes
for string_ref in [tab_tier, tab_global, tab_task]:
    pass # we will do it on full content

# Add filtering to tab-task
filter_html = """
    <div class="mb-4 mt-2 bg-white p-4 rounded-lg border border-gray-200 flex justify-between items-center shadow-sm">
        <div class="flex items-center gap-5">
            <div class="flex items-center gap-2">
                <label class="text-sm text-gray-700 font-medium">作业大类</label>
                <select class="border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none w-32 bg-gray-50">
                    <option>全部大类</option>
                    <option>转发</option>
                    <option>原创</option>
                    <option>点赞/评论</option>
                    <option>线索收集</option>
                    <option>其他活动类</option>
                </select>
            </div>
            <div class="flex items-center gap-2">
                <label class="text-sm text-gray-700 font-medium">作业平台</label>
                <select class="border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none w-32 bg-gray-50">
                    <option>全部平台</option>
                    <option>朋友圈</option>
                    <option>知乎</option>
                    <option>小红书</option>
                    <option>抖音</option>
                    <option>微信视频号</option>
                </select>
            </div>
            <div class="relative ml-2">
                <i class="fas fa-search absolute left-3 top-2.5 text-gray-400 text-sm"></i>
                <input type="text" placeholder="搜索作业小类名称..." class="pl-8 pr-3 py-1.5 border border-gray-300 rounded-md text-sm focus:border-dfred outline-none w-56 bg-gray-50">
            </div>
        </div>
        <button class="text-gray-500 hover:text-dfred text-sm font-medium transition-colors"><i class="fas fa-redo mr-1"></i>重置</button>
    </div>
"""
# insert filter HTML after the blue banner inside tab-task
tab_task = re.sub(r'(<div class="mb-4 flex justify-between items-center bg-blue-50.*?</div>)', r'\1\n' + filter_html, tab_task, flags=re.DOTALL)

# 3. Build Full HTML
full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>成长字典与参数配置 - 东风日产护卫军后台</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        dfred: '#C8102E',
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .custom-scrollbar::-webkit-scrollbar {{ width: 6px; }}
        .custom-scrollbar::-webkit-scrollbar-track {{ background: transparent; }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{ background-color: rgba(156, 163, 175, 0.5); border-radius: 3px; }}
        
        .drawer-overlay {{
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }}
        .drawer-overlay.active {{
            opacity: 1;
            pointer-events: auto;
        }}
        .drawer-panel {{
            transform: translateX(100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .drawer-panel.active {{
            transform: translateX(0);
        }}
    </style>
</head>
<body class="flex h-screen overflow-hidden text-gray-800 font-sans">
    {aside}
    
    <main class="flex-1 flex flex-col overflow-hidden bg-gray-50 relative">
        <!-- Header -->
        <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0 z-20">
            <div class="flex items-center text-sm text-gray-500">
                <a href="#" class="hover:text-gray-900">系统设置</a>
                <i class="fas fa-chevron-right text-[10px] mx-2"></i>
                <span class="text-gray-900 font-medium">成长字典与参数配置</span>
            </div>
            <div class="flex items-center">
                <div class="w-8 h-8 rounded-full bg-dfred text-white flex items-center justify-center font-bold text-sm shadow-sm">
                    Admin
                </div>
            </div>
        </header>

        <!-- Page Content -->
        <div class="flex-1 overflow-y-auto p-6 pb-28 custom-scrollbar relative">
            <div class="flex justify-between items-start mb-6">
                <div>
                    <h1 class="text-2xl font-bold text-gray-900">成长参数全局配置</h1>
                    <p class="text-sm text-gray-500 mt-1">管理护卫军等级门槛、保级规则及各项作业的 XP 发放规则及上限。</p>
                </div>
            </div>

            <div class="bg-white rounded-lg shadow-sm border border-gray-200">
                <!-- Tabs -->
                <div class="px-6 pt-6 pb-2 border-b border-gray-100">
                    <div class="bg-gray-100 p-1 rounded-lg inline-flex gap-1">
                        <button id="btn-tab-tier" onclick="switchConfigTab('tab-tier')" class="px-4 py-2 rounded-md text-sm font-medium bg-white text-gray-900 shadow-sm transition-all tab-btn">等级门槛与特权配置</button>
                        <button id="btn-tab-global" onclick="switchConfigTab('tab-global')" class="px-4 py-2 rounded-md text-sm font-medium text-gray-500 hover:text-gray-700 hover:bg-gray-200 transition-all tab-btn">全局周期与保护规则</button>
                        <button id="btn-tab-task" onclick="switchConfigTab('tab-task')" class="px-4 py-2 rounded-md text-sm font-medium text-gray-500 hover:text-gray-700 hover:bg-gray-200 transition-all tab-btn">作业 XP 产出映射配置</button>
                    </div>
                </div>

                <div class="p-6">
                    {tab_tier}
                    {tab_global}
                    {tab_task}
                </div>
            </div>
        </div>

        <!-- Sticky Footer for Save/Publish -->
        <div class="absolute bottom-0 left-0 right-0 bg-white border-t border-gray-200 px-8 py-4 flex justify-between items-center z-10 shadow-[0_-4px_10px_rgba(0,0,0,0.02)]">
            <div class="flex items-center text-sm text-gray-500">
                <i class="fas fa-check-circle text-green-500 mr-2"></i>
                <span id="update-time-text">配置自动保存至本地草稿箱 (2026-07-03 14:40:22)</span>
            </div>
            <div class="flex gap-3">
                <button onclick="showToast('草稿已保存')" class="px-5 py-2.5 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 hover:text-gray-900 transition-all shadow-sm">
                    保存草稿
                </button>
                <button onclick="showToast('当前配置已成功发布至生产环境！')" class="bg-dfred hover:bg-red-700 text-white px-6 py-2.5 rounded-md text-sm font-medium shadow-md hover:shadow-lg transition-all flex items-center">
                    <i class="fas fa-paper-plane mr-2"></i> 发布生效
                </button>
            </div>
        </div>
    </main>

    <!-- Modals & Drawers -->
    <!-- Toast Container -->
    <div id="toast-container" class="fixed top-5 left-1/2 transform -translate-x-1/2 z-[200] flex flex-col gap-3"></div>

    <!-- Privilege Drawer -->
    <div id="privilege-drawer-overlay" class="fixed inset-0 bg-black bg-opacity-30 z-50 hidden opacity-0 transition-opacity duration-300" onclick="closePrivilegeDrawer()"></div>
    <div id="privilege-drawer" class="fixed right-0 top-0 h-full w-[450px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col">
        <div class="h-16 flex items-center justify-between px-6 border-b border-gray-200 shrink-0 bg-gray-50">
            <h2 id="drawer-title" class="text-lg font-bold text-gray-900">配置特权规则</h2>
            <button onclick="closePrivilegeDrawer()" class="text-gray-400 hover:text-gray-600"><i class="fas fa-times text-xl"></i></button>
        </div>
        <div class="flex-1 overflow-y-auto p-6 relative">
            <div class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">适用系统等级</label>
                    <select id="drawer-level" class="w-full border border-gray-300 rounded-md p-2 text-sm focus:border-dfred outline-none">
                        <option value="1">Level 1 - 新秀护卫军</option>
                        <option value="2">Level 2 - 熟练护卫军</option>
                        <option value="3">Level 3 - 核心护卫军</option>
                        <option value="4">Level 4 - 大师护卫军</option>
                    </select>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">前台展示特权名称</label>
                    <input id="drawer-priv-name" type="text" class="w-full border border-gray-300 rounded-md p-2 text-sm focus:border-dfred outline-none" value="解锁周边兑换商城资格">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">特权类型 <span class="text-red-500">*</span></label>
                    <select id="priv-type-select" class="w-full border border-gray-300 rounded-md p-2 text-sm focus:border-dfred outline-none" onchange="togglePrivilegeConfig()">
                        <option value="points">积分/XP加速类</option>
                        <option value="rights">权益通道类 (作业分配/审核)</option>
                        <option value="offline">线下活动类</option>
                        <option value="visual">视觉标识类 (勋章/皮肤)</option>
                    </select>
                </div>
                <div id="priv-config-points" class="bg-blue-50 p-4 rounded-lg border border-blue-100">
                    <h4 class="text-sm font-bold text-blue-800 mb-3">参数配置</h4>
                    <div class="space-y-3">
                        <div>
                            <label class="block text-xs text-blue-700 mb-1">系统作业基础产出乘数 (倍数)</label>
                            <input type="number" step="0.1" value="1.1" class="w-full border border-blue-200 rounded p-1.5 text-sm outline-none">
                        </div>
                    </div>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">特权详情描述 (前台展示)</label>
                    <textarea class="w-full border border-gray-300 rounded-md p-2 text-sm focus:border-dfred outline-none h-24" placeholder="向用户展示的详细说明..."></textarea>
                </div>
            </div>
        </div>
        <div class="h-16 border-t border-gray-200 flex items-center justify-end px-6 gap-3 bg-gray-50">
            <button onclick="closePrivilegeDrawer()" class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">取消</button>
            <button onclick="savePrivilege()" class="px-4 py-2 bg-dfred text-white rounded-md text-sm font-medium hover:bg-red-700">保存配置</button>
        </div>
    </div>

    <!-- Scripts -->
    <script>
        function showToast(message) {{
            const toastContainer = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'bg-gray-900 bg-opacity-90 text-white px-6 py-3 rounded shadow-lg text-sm flex items-center transition-opacity duration-300';
            toast.innerHTML = `<i class="fas fa-check-circle text-green-400 mr-2"></i> ${{message}}`;
            toastContainer.appendChild(toast);
            
            // Auto update the sticky footer text
            document.getElementById('update-time-text').innerText = '配置自动保存至本地草稿箱 (' + new Date().toLocaleTimeString() + ')';

            setTimeout(() => {{
                toast.classList.add('opacity-0');
                setTimeout(() => toast.remove(), 300);
            }}, 3000);
        }}

        function switchConfigTab(tabId) {{
            ['tab-tier', 'tab-global', 'tab-task'].forEach(id => {{
                document.getElementById(id).classList.add('hidden');
                document.getElementById(id).classList.remove('block');
            }});
            document.getElementById(tabId).classList.remove('hidden');
            document.getElementById(tabId).classList.add('block');

            ['btn-tab-tier', 'btn-tab-global', 'btn-tab-task'].forEach(id => {{
                const btn = document.getElementById(id);
                btn.classList.remove('bg-white', 'text-gray-900', 'shadow-sm');
                btn.classList.add('text-gray-500', 'hover:text-gray-700', 'hover:bg-gray-200');
            }});

            const activeBtn = document.getElementById('btn-' + tabId);
            activeBtn.classList.remove('text-gray-500', 'hover:text-gray-700', 'hover:bg-gray-200');
            activeBtn.classList.add('bg-white', 'text-gray-900', 'shadow-sm');
        }}

        let isEditing = false;
        let currentAddBtn = null;

        function openPrivilegeDrawer(level, privName, isEdit = true, btnElement = null) {{
            isEditing = isEdit;
            currentAddBtn = btnElement;

            document.getElementById('drawer-level').value = level;
            
            if (isEdit) {{
                document.getElementById('drawer-title').innerText = '编辑特权规则';
                document.getElementById('drawer-priv-name').value = privName;
                document.getElementById('priv-type-select').value = 'rights';
                togglePrivilegeConfig();
            }} else {{
                document.getElementById('drawer-title').innerText = '新增特权规则';
                document.getElementById('drawer-priv-name').value = '';
                document.getElementById('priv-type-select').value = 'points';
                togglePrivilegeConfig();
            }}

            const overlay = document.getElementById('privilege-drawer-overlay');
            const drawer = document.getElementById('privilege-drawer');

            overlay.classList.remove('hidden');
            void overlay.offsetWidth;
            overlay.classList.remove('opacity-0');
            drawer.classList.remove('translate-x-full');
        }}

        function closePrivilegeDrawer() {{
            const overlay = document.getElementById('privilege-drawer-overlay');
            const drawer = document.getElementById('privilege-drawer');

            overlay.classList.add('opacity-0');
            drawer.classList.add('translate-x-full');

            setTimeout(() => {{
                overlay.classList.add('hidden');
            }}, 300);
        }}

        function savePrivilege() {{
            const privNameInput = document.getElementById('drawer-priv-name').value.trim();
            const privName = privNameInput || '新特权配置';

            if (!isEditing && currentAddBtn) {{
                const newCard = document.createElement('div');
                newCard.className = "flex items-center justify-between bg-white border border-red-200 rounded p-2 mb-2";
                newCard.innerHTML = `
                    <div class="flex items-center gap-2">
                        <span class="text-xs bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded">新增类</span>
                        <span class="text-sm text-gray-800">${{privName}}</span>
                    </div>
                    <button onclick="openPrivilegeDrawer(document.getElementById('drawer-level').value, '${{privName}}')" class="text-dfred hover:text-red-700 text-xs font-medium"><i class="fas fa-cog"></i> 配置</button>
                `;
                const addBtnContainer = currentAddBtn.closest('div');
                addBtnContainer.parentNode.insertBefore(newCard, addBtnContainer);
            }}

            showToast('特权配置已保存草稿。');
            closePrivilegeDrawer();
        }}

        function togglePrivilegeConfig() {{
            const type = document.getElementById('priv-type-select').value;
            const pointsConfig = document.getElementById('priv-config-points');
            
            if (type === 'points') {{
                pointsConfig.style.display = 'block';
            }} else {{
                pointsConfig.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>
"""

full_html = full_html.replace('XP 产出阀门', 'XP 发放规则及上限')
full_html = full_html.replace('降级软着陆规则', '降级跌幅限制规则')
full_html = full_html.replace('开启降级软着陆保护', '开启最大降幅限制保护')

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print("Rebuild Complete")
