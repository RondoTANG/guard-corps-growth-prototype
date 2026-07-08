
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
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="B端_反馈审核列表页.html">反馈审核列表</a>
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

<!-- 成长体系与AI中台 -->
<div class="menu-group">
    <div class="flex items-center justify-between px-5 py-3 cursor-pointer transition-colors hover:bg-gray-50">
        <span class="font-bold text-gray-800">成长体系与AI中台</span>
        <i class="fas text-xs text-gray-400 fa-chevron-down"></i>
    </div>
    <div class="flex flex-col pb-1 pt-1">
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-gray-50 hover:text-blue-600 text-gray-600" href="#">体系规则配置</a>
        <a class="pl-10 pr-4 py-2.5 transition-colors menu-link hover:bg-purple-50 text-purple-700 font-bold cursor-pointer" onclick="toggleAICruiser()">
            <i class="fas fa-robot mr-1"></i> 生态巡航分析智能体
        </a>
    </div>
</div>

</nav>
</div>
</aside>
`;

function initBSidebar(activeMenuName) {
    const container = document.getElementById('b-sidebar-container');
    
    // 初始化全局悬浮智能体
    initAICopilot();
    
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

    // Auto-open AI Copilot if hash is #open-ai
    if (window.location.hash.includes('open-ai')) {
        setTimeout(() => {
            if (typeof toggleAICruiser === 'function') {
                toggleAICruiser();
            }
        }, 300); // Wait for rendering and transition
    }
}

/* =====================================================================
   全局悬浮智能体 (Eco-Cruiser AI Copilot) 注入
===================================================================== */
const B_COPILOT_HTML = `
<!-- 抽屉遮罩 -->
<div id="aiCruiserOverlay" class="fixed inset-0 bg-gray-900/40 z-[1000] hidden opacity-0 transition-opacity duration-300" onclick="toggleAICruiser()"></div>

<!-- 右侧抽屉 -->
<div id="aiCruiserDrawer" class="fixed right-0 top-0 bottom-0 w-[480px] bg-white shadow-xl z-[1001] transform translate-x-full transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] flex flex-col border-l border-gray-200">
    
    <!-- 头部 -->
    <div class="px-6 py-5 border-b border-gray-100 flex items-center justify-between bg-gradient-to-r from-purple-50 to-white relative overflow-hidden">
        <div class="flex items-center gap-4 relative z-10">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-indigo-600 shadow-sm flex items-center justify-center text-white">
                <i class="fas fa-robot text-xl"></i>
            </div>
            <div>
                <h2 class="text-lg font-bold text-gray-800 tracking-tight">成长体系健康诊断报告</h2>
                <div class="flex items-center gap-1.5 mt-0.5">
                    <span class="w-2 h-2 rounded-full bg-green-500"></span>
                    <p class="text-xs text-gray-500">今日 02:00 定时跑批完成</p>
                </div>
            </div>
        </div>
        <div class="flex items-center gap-2 relative z-10">
            <button onclick="toggleCruiserSettings()" id="aiSettingsBtn" class="px-3 py-1.5 text-sm font-medium text-purple-600 bg-purple-50 hover:bg-purple-100 rounded-lg transition-colors flex items-center gap-1.5" title="调整健康度目标">
                <i class="fas fa-sliders-h text-sm"></i> 健康度配置
            </button>
            <button onclick="toggleAICruiser()" class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors ml-1">
                <i class="fas fa-times text-lg"></i>
            </button>
        </div>
    </div>

    <!-- 视图 1: 报告 -->
    <div id="aiReportView" class="flex-1 overflow-y-auto p-6 bg-gray-50/50">
        <div class="space-y-6">
            <!-- 结论卡片 -->
            <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
                <div class="bg-orange-50 border-b border-orange-100 px-4 py-3 flex items-start gap-3">
                    <i class="fas fa-exclamation-triangle text-orange-500 mt-1"></i>
                    <div>
                        <h3 class="font-bold text-orange-800 text-sm">宽腰流失预警</h3>
                        <p class="text-orange-700/80 text-xs mt-1 leading-relaxed">当前 L2 阶位人数占比下滑至 <strong class="text-orange-800">41%</strong>（低于健康水位 47%）。未来 15 天预计有 <strong class="text-orange-800">120 名</strong> L3 核心战力因活跃度下降面临降级风险。</p>
                    </div>
                </div>
                <div class="px-4 py-3 bg-white">
                    <p class="text-xs text-gray-500 flex items-start gap-2">
                        <i class="fas fa-search text-gray-400 mt-0.5"></i>
                        <span><strong>AI 归因：</strong>近两周「基础互动作业」发布量环比下降 45%，底层生态饥饿指数升至 28%，导致腰底盘用户无作业可领，活跃度下跌。</span>
                    </p>
                </div>
            </div>

            <!-- 处方建议 -->
            <div>
                <h3 class="text-sm font-bold text-gray-800 mb-3 flex items-center gap-2">
                    <i class="fas fa-stethoscope text-purple-500"></i> AI 运营处方建议
                </h3>
                <div class="bg-white rounded-xl border border-purple-100 shadow-sm p-4 relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-1 h-full bg-purple-500"></div>
                    <p class="text-sm text-gray-700 leading-relaxed mb-4">
                        建议本周内立刻追加 <strong class="text-purple-600">3~5 个</strong> 面向 L1/L2 开放的 <strong>基础互动作业</strong>，单次奖励可适度上调至 <strong class="text-purple-600">15 XP</strong>。
                    </p>
                    
                    <div class="bg-gray-50 rounded-lg p-3 border border-gray-100 mb-4">
                        <div class="text-[11px] font-semibold text-gray-400 mb-2 uppercase">AI 推荐参数草稿</div>
                        <div class="grid grid-cols-2 gap-y-3 gap-x-2 text-xs">
                            <div class="flex flex-col"><span class="text-gray-400 mb-0.5">作业类型</span><span class="font-medium text-gray-800">基础互动</span></div>
                            <div class="flex flex-col"><span class="text-gray-400 mb-0.5">开放圈层</span><span class="font-medium text-gray-800">L1, L2</span></div>
                            <div class="flex flex-col"><span class="text-gray-400 mb-0.5">奖励 XP</span><span class="font-bold text-purple-600">15 / 次</span></div>
                            <div class="flex flex-col"><span class="text-gray-400 mb-0.5">建议投放量</span><span class="font-medium text-gray-800">20,000 份</span></div>
                        </div>
                    </div>

                </div>
            </div>
            
            <!-- 底部按钮 -->
            <div class="mt-8 border-t border-gray-100 pt-6 flex justify-center">
                <button onclick="openAiDataReqModal()" class="w-full py-3 bg-blue-50 hover:bg-blue-100 text-blue-600 font-bold rounded-xl border border-blue-100 shadow-sm transition-colors flex items-center justify-center gap-2">
                    <i class="fas fa-file-code"></i> 查看系统数据输入要求
                </button>
            </div>
        </div>
    </div>

    <!-- 视图 2: 沙盘推演 -->
    <div id="aiSettingsView" class="flex-1 overflow-y-auto p-6 bg-gray-50 hidden flex-col">
        <div class="mb-6">
            <h3 class="text-base font-bold text-gray-800 flex items-center gap-2">
                <i class="fas fa-microchip text-purple-500"></i> 目标沙盘推演
            </h3>
            <p class="text-xs text-gray-500 mt-1">如果当期业务存在特殊大促目标，您可强行调整各段位的期望健康占比。AI 将以新目标为准重新推演。</p>
        </div>

        <div class="space-y-6 flex-1">
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label class="text-sm font-medium text-gray-700">L1 新秀护卫军 期望占比</label>
                    <div class="flex items-center">
                        <input type="number" id="inputL1" value="50" step="0.1" class="w-16 px-2 py-0.5 text-right text-sm font-bold text-purple-600 bg-white border border-gray-200 rounded focus:outline-none focus:border-purple-400 focus:ring-1 focus:ring-purple-400" oninput="syncInputToSlider('L1')">
                        <span class="text-sm font-bold text-gray-500 ml-1.5">%</span>
                    </div>
                </div>
                <input type="range" id="sliderL1" min="30" max="70" step="0.1" value="50" class="w-full h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer" oninput="updateSliderSum()">
            </div>
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label class="text-sm font-medium text-gray-700">L2 熟练护卫军 期望占比</label>
                    <div class="flex items-center">
                        <input type="number" id="inputL2" value="47" step="0.1" class="w-16 px-2 py-0.5 text-right text-sm font-bold text-purple-600 bg-white border border-gray-200 rounded focus:outline-none focus:border-purple-400 focus:ring-1 focus:ring-purple-400" oninput="syncInputToSlider('L2')">
                        <span class="text-sm font-bold text-gray-500 ml-1.5">%</span>
                    </div>
                </div>
                <input type="range" id="sliderL2" min="20" max="60" step="0.1" value="47" class="w-full h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer" oninput="updateSliderSum()">
            </div>
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label class="text-sm font-medium text-gray-700">L3 专家护卫军 期望占比</label>
                    <div class="flex items-center">
                        <input type="number" id="inputL3" value="2.5" step="0.1" class="w-16 px-2 py-0.5 text-right text-sm font-bold text-purple-600 bg-white border border-gray-200 rounded focus:outline-none focus:border-purple-400 focus:ring-1 focus:ring-purple-400" oninput="syncInputToSlider('L3')">
                        <span class="text-sm font-bold text-gray-500 ml-1.5">%</span>
                    </div>
                </div>
                <input type="range" id="sliderL3" min="1" max="10" step="0.1" value="2.5" class="w-full h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer" oninput="updateSliderSum()">
            </div>
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label class="text-sm font-medium text-gray-700">L4 大师护卫军 期望占比</label>
                    <div class="flex items-center">
                        <input type="number" id="inputL4" value="0.5" step="0.1" class="w-16 px-2 py-0.5 text-right text-sm font-bold text-purple-600 bg-white border border-gray-200 rounded focus:outline-none focus:border-purple-400 focus:ring-1 focus:ring-purple-400" oninput="syncInputToSlider('L4')">
                        <span class="text-sm font-bold text-gray-500 ml-1.5">%</span>
                    </div>
                </div>
                <input type="range" id="sliderL4" min="0.1" max="5" step="0.1" value="0.5" class="w-full h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer" oninput="updateSliderSum()">
            </div>
        </div>
        
        <div id="sumWarningBox" class="mt-4 p-3 rounded-lg bg-green-50 border border-green-200 flex justify-between items-center transition-colors">
            <span class="text-sm text-gray-600">当前占比总和：<strong id="totalSumStr" class="text-green-600">100%</strong></span>
            <span id="sumErrorMsg" class="text-xs text-red-500 hidden"><i class="fas fa-exclamation-circle"></i> 必须等于 100%</span>
        </div>

        <div class="mt-4 pt-4 border-t border-gray-200">
            <button onclick="reAnalyzeAI()" id="reanalyzeBtn" class="w-full flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-900 text-white py-3 rounded-xl text-sm font-semibold transition-all">
                <i class="fas fa-sync-alt" id="spinIcon"></i> 按新目标重新推演策略
            </button>
        </div>
    </div>
</div>

<!-- Data Req Modal -->
<div class="fixed inset-0 bg-gray-900 bg-opacity-60 z-[1100] hidden flex items-center justify-center backdrop-blur-sm transition-opacity" id="aiDataReqModal">
    <div class="bg-white rounded-xl w-3/4 max-w-5xl h-[85vh] flex flex-col shadow-2xl overflow-hidden transform transition-transform">
        <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center bg-gray-50/80">
            <h3 class="text-lg font-bold text-gray-800 flex items-center"><i class="fas fa-file-code text-blue-500 mr-2 text-xl"></i> 生态巡航智能体 - 业务系统输入数据指标要求</h3>
            <button class="text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-lg p-1.5 transition-colors" onclick="closeAiDataReqModal()">
                <i class="fas fa-times text-xl w-6 h-6 flex items-center justify-center"></i>
            </button>
        </div>
        <div class="p-8 overflow-y-auto flex-1 prose prose-sm prose-blue max-w-none prose-headings:text-gray-800 prose-h2:text-blue-600 prose-h2:border-b prose-h2:border-gray-200 prose-h2:pb-2 prose-h2:mt-6 prose-p:text-gray-600 prose-li:text-gray-600" id="aiDataReqContent">
        </div>
    </div>
</div>
<script id="aiDataReqMarkdown" type="text/markdown">
# 生态巡航智能体 (Eco-Cruiser AI) - 业务系统输入数据指标要求

为了让生态巡航智能体能够准确诊断“护卫军成长体系”的健康度，并输出精准的运营处方（如：宽腰流失预警、任务下发建议等），**业务后端系统（或数据中台）需要定时（如每日凌晨）向 AI 智能体的大模型 API 输入以下结构化的 JSON 统计指标**。

---

## 1. 基础大盘水位 (Macro Health Metrics)
用于评估整个护卫军生态的总盘子和生命力。
*   **总用户数 (Total Users)**：当前注册护卫军的总人数。
*   **活跃率 (Active Rate)**：近 30 天内有登录或做任务行为的用户占比。
*   **环比涨跌幅 (MoM Growth)**：总用户、活跃用户较上个周期的波动百分比。
*   **升降级规模 (Tier Mobility)**：近 30 天内【成功晋段】与【掉段降级】的人数绝对值。

## 2. 阶梯结构与断层预警 (Tier Distribution & Warning)
用于大模型判断当前的段位分布是否呈现健康的“金字塔”或“橄榄型”结构，是否存在某个段位断层（例如 L2 占比过低导致宽腰塌陷）。
*   **各段位当前人数与占比**：
    *   L1 新秀（人数，占比%）
    *   L2 熟练（人数，占比%）
    *   L3 专家（人数，占比%）
    *   L4 大师（人数，占比%）
*   **各段位期望健康水位线 (Expected Health Baseline)**：由业务规则预设。例如规定 L2 的健康水位需维持在 45%~50% 之间。
*   **各段位活跃度异动**：例如 L3 专家近两周活跃度环比下降情况。
*   **高危降级预警名单规模 (Risk Group)**：处于保级期末尾（未来 15 天内到期）且当前 XP 未达保级线的用户数量（按段位分布）。

## 3. 作业供需生态指标 (Task Supply & Demand Index)
成长体系的本质是“做作业赚 XP”。如果底层断流（无作业可做）或头部通胀（高分作业乱发），系统都会失衡。
*   **作业投放规模 (Task Supply)**：近 15/30 天发布的各类型作业数量。
    *   类型拆分：基础互动作业、深度原创作业等。
    *   圈层拆分：面向全员开放、仅限 L3/L4 开放的比例。
*   **底层生态饥饿指数 (Hunger Index)**：这是最重要的复合指标。指 L1/L2 用户尝试接单但因“已被抢光”或“无权限”导致接单失败的频率。如果饥饿指数飙升，意味着底层供血不足。
*   **作业核销转化率 (Task Completion Rate)**：作业被领取后的最终按时交付率及审核通过率。

## 4. 信用与违规指标 (Credit & Violation Metrics)
用于判断生态内是否存在恶意刷分或占坑不作为的现象。
*   **违约率 (Violation Rate)**：领取专属任务后逾期未交、或逾期未领触发扣分（-50XP / -100XP）的绝对次数及环比变化趋势。

---

## 💡 给后端开发的对接建议

*   **数据封装**：建议后端通过定时任务（如每天 02:00），跑批统计以上所有字段，组装为一个大的 \`JSON Object\`。
*   **Prompt 注入**：将该 JSON 作为大模型 Prompt 的 \`<Current_Stats>\` 标签内容喂给 Eco-Cruiser 智能体。
*   **输出解析**：AI 返回结构化的诊断结果（预警 Title、归因描述、建议下发参数），后端将其存储至数据库中，并在 B 端“成长体系健康诊断报告”抽屉中直接渲染给运营人员。
</script>
`;

function initAICopilot() {
    if (!document.getElementById('aiCruiserDrawer')) {
        document.body.insertAdjacentHTML('beforeend', B_COPILOT_HTML);
    }
}

window.toggleAICruiser = function() {
    const drawer = document.getElementById('aiCruiserDrawer');
    const overlay = document.getElementById('aiCruiserOverlay');
    
    if (drawer.classList.contains('translate-x-full')) {
        overlay.classList.remove('hidden');
        requestAnimationFrame(() => {
            overlay.classList.remove('opacity-0');
            drawer.classList.remove('translate-x-full');
        });
    } else {
        overlay.classList.add('opacity-0');
        drawer.classList.add('translate-x-full');
        setTimeout(() => {
            overlay.classList.add('hidden');
        }, 300);
    }
}

window.toggleCruiserSettings = function() {
    const reportView = document.getElementById('aiReportView');
    const settingsView = document.getElementById('aiSettingsView');
    const btn = document.getElementById('aiSettingsBtn');
    
    if (settingsView.classList.contains('hidden')) {
        reportView.classList.add('hidden');
        settingsView.classList.remove('hidden');
        settingsView.classList.add('flex');
        btn.classList.add('bg-purple-100', 'text-purple-700');
        // Initialize sum correctly
        if(typeof updateSliderSum === 'function') updateSliderSum();
    } else {
        settingsView.classList.add('hidden');
        settingsView.classList.remove('flex');
        reportView.classList.remove('hidden');
        btn.classList.remove('bg-purple-100', 'text-purple-700');
    }
}

window.syncInputToSlider = function(level) {
    const inputVal = document.getElementById('input' + level).value;
    document.getElementById('slider' + level).value = inputVal || 0;
    updateSliderSum();
}

window.updateSliderSum = function() {
    const v1 = parseFloat(document.getElementById('sliderL1').value) || 0;
    const v2 = parseFloat(document.getElementById('sliderL2').value) || 0;
    const v3 = parseFloat(document.getElementById('sliderL3').value) || 0;
    const v4 = parseFloat(document.getElementById('sliderL4').value) || 0;
    const total = +(v1 + v2 + v3 + v4).toFixed(1);
    
    // Only update inputs if they are not actively focused, 
    // or simply always update them if value differs to ensure sync
    if (document.getElementById('inputL1').value != v1) document.getElementById('inputL1').value = v1;
    if (document.getElementById('inputL2').value != v2) document.getElementById('inputL2').value = v2;
    if (document.getElementById('inputL3').value != v3) document.getElementById('inputL3').value = v3;
    if (document.getElementById('inputL4').value != v4) document.getElementById('inputL4').value = v4;
    
    const sumStr = document.getElementById('totalSumStr');
    const errMsg = document.getElementById('sumErrorMsg');
    const box = document.getElementById('sumWarningBox');
    const btn = document.getElementById('reanalyzeBtn');
    
    sumStr.innerText = total + '%';
    
    if (total === 100) {
        sumStr.className = 'text-green-600 font-bold';
        errMsg.classList.add('hidden');
        box.classList.remove('bg-red-50', 'border-red-200');
        box.classList.add('bg-green-50', 'border-green-200');
        btn.disabled = false;
        btn.classList.remove('bg-gray-400', 'cursor-not-allowed');
        btn.classList.add('bg-gray-800', 'hover:bg-gray-900');
    } else {
        sumStr.className = 'text-red-600 font-bold';
        errMsg.classList.remove('hidden');
        box.classList.remove('bg-green-50', 'border-green-200');
        box.classList.add('bg-red-50', 'border-red-200');
        btn.disabled = true;
        btn.classList.remove('bg-gray-800', 'hover:bg-gray-900');
        btn.classList.add('bg-gray-400', 'cursor-not-allowed');
    }
}

window.reAnalyzeAI = function() {
    const btn = document.getElementById('reanalyzeBtn');
    const originalHtml = btn.innerHTML;
    btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> AI 实时推演中...`;
    btn.classList.add('opacity-80', 'cursor-not-allowed');
    
    setTimeout(() => {
        btn.innerHTML = `<i class="fas fa-check text-green-400"></i> 推演完成，已更新报告`;
        setTimeout(() => {
            btn.innerHTML = originalHtml;
            btn.classList.remove('opacity-80', 'cursor-not-allowed');
            toggleCruiserSettings(); 
        }, 1000);
    }, 1500);
}

/* =====================================================================
   AI Data Req Modal Functions
===================================================================== */
function openAiDataReqModal() {
    const modal = document.getElementById('aiDataReqModal');
    const contentDiv = document.getElementById('aiDataReqContent');
    const mdScript = document.getElementById('aiDataReqMarkdown');
    
    if (modal && contentDiv && mdScript && typeof marked !== 'undefined') {
        contentDiv.innerHTML = marked.parse(mdScript.textContent);
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    } else if (typeof marked === 'undefined') {
        alert("系统缺少 marked.js 渲染器，无法显示 Markdown 内容");
    }
}

function closeAiDataReqModal() {
    const modal = document.getElementById('aiDataReqModal');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
    }
}

// Add click event to close when clicking outside the modal
document.addEventListener('click', function(e) {
    const modal = document.getElementById('aiDataReqModal');
    if (modal && !modal.classList.contains('hidden')) {
        const modalContent = modal.querySelector('.bg-white');
        if (!modalContent.contains(e.target) && !e.target.closest('button[onclick="openAiDataReqModal()"]')) {
            closeAiDataReqModal();
        }
    }
});
