import os
import re

dir_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型"

files = {
    'config': 'B端_等级规则与XP配置页.html',
    'users': 'B端_用户管理_XP干预页.html',
    'ledger': 'B端_XP资产流水明细表.html',
    'dashboard': 'B端_成长数据健康度大盘.html'
}

# The global sidebar used in C-end prototypes (adapted for B-end active state)
global_sidebar = """
    <!-- 原型全局侧边栏 -->
    <div class="w-64 bg-white shadow-[4px_0_24px_rgba(0,0,0,0.05)] border-r border-gray-100 z-[100] flex flex-col shrink-0">
        <div class="p-5 border-b border-gray-100 bg-gray-50/50">
            <h2 class="text-sm font-bold text-gray-800 flex items-center"><i class="fas fa-layer-group text-dfred mr-2"></i>护卫军体系原型</h2>
            <p class="text-[10px] text-gray-500 mt-1">交互与逻辑批注版</p>
        </div>
        <div class="flex-1 overflow-y-auto p-4 space-y-1">
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-2 px-2 tracking-wider">C端应用 (APP端)</div>
            <a href="C端_个人中心.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-user-circle w-5"></i> 个人中心 (入口)</a>
            <a href="C端_成长中心大盘.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-medal w-5"></i> 成长中心大盘</a>
            <a href="C端_成长值明细.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-list-alt w-5"></i> 成长值明细</a>
            <a href="C端_作业大厅.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-gray-100 transition flex items-center"><i class="fas fa-tasks w-5"></i> 作业大厅</a>
            
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-8 px-2 tracking-wider">B端管理 (PC端)</div>
            <a href="#" class="block px-3 py-2.5 rounded-lg text-xs bg-red-50 text-dfred font-bold transition flex items-center"><i class="fas fa-desktop w-5"></i> 护卫军管理平台管理 (SPA)</a>
        </div>
    </div>
"""

# The B-end dark sidebar
b_end_sidebar = """
    <!-- B端业务菜单 -->
    <aside class="w-64 bg-[#313C48] text-[#909399] flex flex-col shrink-0 text-sm overflow-hidden select-none z-50 shadow-xl">
        <div class="h-16 flex items-center px-6 bg-[#2B3643] shrink-0 border-b border-gray-700/50">
            <span class="text-white text-lg font-bold tracking-wider"><i class="fas fa-shield-alt text-dfred mr-2"></i>护卫军管理平台</span>
        </div>
        
        <div class="flex-1 overflow-y-auto py-4 custom-scrollbar">
            <nav class="space-y-1" id="b-end-nav">
                <!-- 护卫军作业管理 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                        <span class="font-bold text-gray-200">护卫军作业管理</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">护卫军作业任务配置</a>
                    </div>
                </div>

                <!-- 审核管理 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                        <span class="font-bold text-gray-200">审核管理</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">审核管理列表</a>
                    </div>
                </div>

                <!-- 用户管理 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors" data-group="users">
                        <span class="font-bold text-gray-200">用户管理</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">平台列表</a>
                        <a href="#" onclick="switchPage('users')" id="nav-users" class="px-9 py-2.5 hover:text-white transition-colors nav-item">用户列表</a>
                    </div>
                </div>

                <!-- 系统设置 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors" data-group="sys">
                        <span class="font-bold text-gray-200">系统设置</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="#" onclick="switchPage('config')" id="nav-config" class="px-9 py-2.5 hover:text-white transition-colors nav-item">成长规则配置</a>
                    </div>
                </div>

                <!-- 统计分析 -->
                <div class="menu-group">
                    <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors" data-group="stat">
                        <span class="font-bold text-gray-200">统计分析</span>
                        <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                    </div>
                    <div class="flex flex-col">
                        <a href="#" onclick="switchPage('ledger')" id="nav-ledger" class="px-9 py-2.5 hover:text-white transition-colors nav-item">XP资产流水</a>
                        <a href="#" onclick="switchPage('dashboard')" id="nav-dashboard" class="px-9 py-2.5 hover:text-white transition-colors nav-item">成长数据大盘</a>
                    </div>
                </div>
            </nav>
        </div>
    </aside>
"""

# HTML template
template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>护卫军成长体系 - B端完整管理后台 (SPA)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="assets/css/common.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { dfred: '#E60012' }
                }
            }
        }
    </script>
    <style>
        .custom-scrollbar::-webkit-scrollbar { width: 6px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background-color: rgba(156, 163, 175, 0.5); border-radius: 3px; }
        .page-content { display: none; height: 100%; flex-direction: column; overflow: hidden; }
        .page-content.active { display: flex; }
        
        /* Drawer animation classes */
        .drawer-overlay {
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        .drawer-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }
        .drawer-panel {
            transform: translateX(100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .drawer-panel.active {
            transform: translateX(0);
        }
    </style>
</head>
<body class="bg-gray-100 h-screen w-screen flex overflow-hidden font-sans">
    
    <!-- 1. Global Prototype Sidebar -->
    {GLOBAL_SIDEBAR}
    
    <!-- 2. B-end Dark Sidebar -->
    {B_END_SIDEBAR}

    <!-- 3. Main Content Area -->
    <div class="flex-1 relative bg-gray-50 overflow-hidden flex flex-col w-full h-full">
        <!-- Pages -->
        <div id="page-config" class="page-content">{MAIN_CONFIG}</div>
        <div id="page-users" class="page-content">{MAIN_USERS}</div>
        <div id="page-ledger" class="page-content">{MAIN_LEDGER}</div>
        <div id="page-dashboard" class="page-content">{MAIN_DASHBOARD}</div>
    </div>
    
    <!-- Drawers & Modals Container -->
    <div id="global-modals" class="z-[200] relative">
        {MODALS_CONFIG}
        {MODALS_USERS}
        {MODALS_LEDGER}
    </div>

    <!-- 4. SPA Logic & Extracted Scripts -->
    <script>
        // --- SPA Router Logic ---
        function switchPage(pageId) {
            // Hide all pages
            document.querySelectorAll('.page-content').forEach(el => el.classList.remove('active'));
            // Reset all nav items
            document.querySelectorAll('.nav-item').forEach(el => {
                el.classList.remove('bg-[#3B82F6]', 'text-white', 'font-bold');
                el.classList.add('text-gray-400');
            });
            
            // Show target page
            document.getElementById('page-' + pageId).classList.add('active');
            
            // Highlight nav item
            const navItem = document.getElementById('nav-' + pageId);
            if (navItem) {
                navItem.classList.remove('text-gray-400');
                navItem.classList.add('bg-[#3B82F6]', 'text-white', 'font-bold');
                
                // Ensure parent group is open (simulated by highlighting group header text)
                const group = navItem.closest('.menu-group');
                if (group) {
                    const groupTitle = group.querySelector('span');
                    if (groupTitle) groupTitle.classList.replace('text-gray-200', 'text-white');
                }
            }
            
            // Trigger ECharts resize if dashboard
            if (pageId === 'dashboard' && window.tierChart && window.conversionChart) {
                setTimeout(() => {
                    window.tierChart.resize();
                    window.conversionChart.resize();
                }, 50);
            }
        }
        
        // --- Extracted Scripts from Pages ---
        {SCRIPTS}
        
        // Init SPA
        document.addEventListener('DOMContentLoaded', () => {
            switchPage('config'); // Default page
        });
    </script>
</body>
</html>
"""

def extract_section(html, tag, class_name=None):
    if class_name:
        pattern = f'<{tag}[^>]*class="[^"]*{class_name}[^"]*"[^>]*>(.*?)</{tag}>'
        # Need to handle nested tags if regex is used, but for <main> it's usually simple or we use a better approach
    
    # Simple extraction using string finding for <main
    start_idx = html.find('<main')
    if start_idx == -1: return ""
    start_inner = html.find('>', start_idx) + 1
    end_idx = html.rfind('</main>')
    return html[start_inner:end_idx]

def extract_modals(html):
    # Extract drawer overlays (like id="editDrawer" or id="xpDrawer")
    modals = []
    
    # 1. Look for drawer overlay
    drawer_start = html.find('<div id="editDrawer"')
    if drawer_start != -1:
        # crude extraction to </body>
        end_idx = html.find('<script>', drawer_start)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start)
        modals.append(html[drawer_start:end_idx])
        
    drawer_start_xp = html.find('<div id="xp-drawer-overlay"')
    if drawer_start_xp != -1:
        end_idx = html.find('<script>', drawer_start_xp)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start_xp)
        modals.append(html[drawer_start_xp:end_idx])
        
    # Toast
    toast_start = html.find('<div id="toast"')
    if toast_start != -1:
        end_idx = html.find('</div>', toast_start) + 6
        modals.append(html[toast_start:end_idx])
        
            
    drawer_start_ev = html.find('<div id="evidence-modal-overlay"')
    if drawer_start_ev != -1:
        end_idx = html.find('<script>', drawer_start_ev)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start_ev)
        modals.append(html[drawer_start_ev:end_idx])
        
            
    drawer_start_priv = html.find('<div id="privilege-drawer-overlay"')
    if drawer_start_priv != -1:
        end_idx = html.find('<script>', drawer_start_priv)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start_priv)
        modals.append(html[drawer_start_priv:end_idx])

    toast_container_start = html.find('<div id="toast-container"')
    if toast_container_start != -1:
        end_idx = html.find('</div>', toast_container_start) + 6
        modals.append(html[toast_container_start:end_idx])

    return "\n".join(modals)

def extract_scripts(html):
    scripts = []
    # Find all <script>...</script>
    for match in re.finditer(r'<script>(.*?)</script>', html, re.DOTALL):
        script_content = match.group(1)
        if 'tailwind.config' not in script_content:
            scripts.append(script_content)
    return "\n".join(scripts)

def build_spa():
    contents = {}
    modals = {}
    scripts = []
    
    for key, filename in files.items():
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        main_content = extract_section(html, 'main')
        # Remove the <header> inside main if it contains the breadcrumb, or keep it. 
        # Actually keeping it is fine, each page has its own header.
        contents[key] = main_content
        modals[key] = extract_modals(html)
        scripts.append(extract_scripts(html))
        
    final_html = template
    final_html = final_html.replace('{GLOBAL_SIDEBAR}', global_sidebar)
    final_html = final_html.replace('{B_END_SIDEBAR}', b_end_sidebar)
    final_html = final_html.replace('{MAIN_CONFIG}', contents['config'])
    final_html = final_html.replace('{MAIN_USERS}', contents['users'])
    final_html = final_html.replace('{MAIN_LEDGER}', contents['ledger'])
    final_html = final_html.replace('{MAIN_DASHBOARD}', contents['dashboard'])
    final_html = final_html.replace('{MODALS_CONFIG}', modals['config'])
    final_html = final_html.replace('{MODALS_USERS}', modals['users'])
    final_html = final_html.replace('{MODALS_LEDGER}', modals['ledger'])
    final_html = final_html.replace('{SCRIPTS}', "\n".join(scripts))
    
    # Fix some script collisions (e.g. initCharts in dashboard)
    # The dashboard script defines var tierChart, we need to make them global
    final_html = final_html.replace('var tierChart = echarts.init', 'window.tierChart = echarts.init')
    final_html = final_html.replace('var conversionChart = echarts.init', 'window.conversionChart = echarts.init')
    
    out_path = os.path.join(dir_path, 'B端_完整后台大盘.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Successfully generated SPA at {out_path}")

if __name__ == '__main__':
    build_spa()
