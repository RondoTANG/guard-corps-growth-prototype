import os

html_content = """
const B_SIDEBAR_HTML = `
<aside class="w-64 flex flex-col shrink-0 text-sm overflow-hidden select-none bg-white text-gray-600 border-r border-gray-200" id="org-sidebar">
<div class="h-16 flex items-center px-6 bg-white border-b border-gray-100">
<div class="w-8 h-8 rounded-full bg-dfred flex items-center justify-center text-white font-bold mr-3">东</div><span class="text-base font-bold tracking-wider text-gray-900">东风护卫军后台</span>
</div>
<div class="flex-1 overflow-y-auto style-scrollbar">
<nav class="flex flex-col pb-6 pt-2 space-y-1">

<!-- 独立菜单: 作业管理 -->
<a class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors menu-link hover:bg-gray-50 text-gray-800 font-bold" href="B端_作业管理列表.html">
    <span>作业管理</span>
</a>

<!-- 审核管理 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">审核管理</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col hidden pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">审核管理列表</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">人工审核</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">反馈审核列表</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">作业审核记录</a>
    </div>
</div>

<!-- 用户管理 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">用户管理</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col hidden pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">平台列表</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="B端_用户管理_XP干预页.html">用户列表</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">员工列表</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">用户标签管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">人群包管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">IAM员工列表</a>
    </div>
</div>

<!-- 内容管理 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">内容管理</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col hidden pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">文章编辑</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">广告管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">作业素材管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">千人千面素材管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">品牌素材管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">素材库</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">学院-栏目管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">学院-评论管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">学院-敏感词管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">优质内容管理</a>
    </div>
</div>

<!-- 系统设置 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">系统设置</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col hidden pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">系统日志</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">登录日志</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="B端_等级规则与XP配置页.html">成长规则配置</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">额外奖励设置</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">积分充值管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">标签管理(统计)</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">字典管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">消息推送</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">白名单作业管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="B端_系统设置_文章管理页.html">文章管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">审核话术管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">积分发放记录</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">服务号消息额度管理</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">作业用途分类管理</a>
    </div>
</div>

<!-- 统计分析 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">统计分析</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col hidden pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="B端_成长数据健康度大盘.html">成长数据大盘</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">用户台账</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">护卫军作业台账</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">党委排名数据</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">用户排名数据</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">累计零积分党委人数</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">累计零积分用户明细</a>
    </div>
</div>

</nav>
</div>
</aside>
`;

function initBSidebar(activeMenuName) {
    const container = document.getElementById('b-sidebar-container');
    if (!container) return;
    
    container.innerHTML = B_SIDEBAR_HTML;
    
    // Toggle Logic
    const menuGroups = container.querySelectorAll('.menu-group');
    menuGroups.forEach(group => {
        const header = group.querySelector('div.justify-between');
        const submenu = group.querySelector('.flex-col');
        if (!header || !submenu) return;
        const icon = header.querySelector('i');
        
        header.addEventListener('click', (e) => {
            const isHidden = submenu.classList.contains('hidden');
            if (isHidden) {
                submenu.classList.remove('hidden');
                if (icon) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                }
            } else {
                submenu.classList.add('hidden');
                if (icon) {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            }
        });
    });
    
    // Active Menu Logic
    if (activeMenuName) {
        const links = container.querySelectorAll('.menu-link');
        links.forEach(link => {
            if (link.textContent.trim() === activeMenuName) {
                // Determine if it's a top-level link or child link
                if (link.tagName === 'A' && !link.parentElement.classList.contains('flex-col')) {
                    // Top level standalone link
                    link.classList.remove('text-gray-800');
                    link.classList.add('text-blue-600', 'bg-blue-50');
                } else {
                    // Child link
                    link.classList.remove('text-gray-600');
                    link.classList.add('bg-blue-50', 'text-blue-600', 'font-medium');
                    
                    // Expand and highlight parent group
                    const group = link.closest('.menu-group');
                    if (group) {
                        const header = group.querySelector('div.justify-between');
                        const submenu = group.querySelector('.flex-col');
                        if (submenu) submenu.classList.remove('hidden');
                        
                        if (header) {
                            const icon = header.querySelector('i');
                            const span = header.querySelector('span');
                            
                            if (span) {
                                span.classList.remove('text-gray-800');
                                span.classList.add('text-blue-600');
                            }
                            if (icon) {
                                icon.classList.remove('fa-chevron-down', 'text-gray-400');
                                icon.classList.add('fa-chevron-up', 'text-blue-600');
                            }
                        }
                    }
                }
            }
        });
    }
}
"""

with open('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/b_sidebar.js', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("b_sidebar.js flattened successfully.")
