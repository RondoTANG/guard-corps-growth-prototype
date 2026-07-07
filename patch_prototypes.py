import os
import re

sidebar_html = """
    <!-- 原型全局侧边栏 (方便切换页面) -->
    <div class="fixed left-0 top-0 w-64 h-full bg-white shadow-[4px_0_24px_rgba(0,0,0,0.05)] border-r border-gray-100 z-[100] flex flex-col">
        <div class="p-5 border-b border-gray-100 bg-gray-50/50">
            <h2 class="text-sm font-bold text-gray-800 flex items-center"><i class="fas fa-layer-group text-dfred mr-2"></i>护卫军体系原型</h2>
            <p class="text-[10px] text-gray-500 mt-1">交互与逻辑批注版</p>
        </div>
        <div class="flex-1 overflow-y-auto p-4 space-y-1">
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-2 px-2 tracking-wider">C端应用 (APP端)</div>
            <a href="C端_个人中心.html" class="block px-3 py-2.5 rounded-lg text-xs {{active_personal}} transition flex items-center"><i class="fas fa-user-circle w-5"></i> 个人中心 (入口)</a>
            <a href="C端_成长中心大盘.html" class="block px-3 py-2.5 rounded-lg text-xs {{active_growth}} transition flex items-center"><i class="fas fa-medal w-5"></i> 成长中心大盘</a>
            <a href="C端_成长值明细.html" class="block px-3 py-2.5 rounded-lg text-xs {{active_details}} transition flex items-center"><i class="fas fa-list-alt w-5"></i> 成长值明细</a>
            <a href="C端_作业大厅.html" class="block px-3 py-2.5 rounded-lg text-xs {{active_hall}} transition flex items-center"><i class="fas fa-tasks w-5"></i> 作业大厅</a>
            
            <div class="text-[10px] font-bold text-gray-400 mb-3 mt-8 px-2 tracking-wider">B端管理 (PC端)</div>
            <a href="B端_完整后台大盘.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center"><i class="fas fa-desktop w-5"></i> 护卫军管理平台管理 (SPA)</a>
        </div>
    </div>
"""

def process_file(filename, active_key, right_panel_html=""):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject sidebar
    active_classes = "bg-red-50 text-dfred font-bold"
    inactive_classes = "text-gray-600 hover:bg-gray-100"
    
    sidebar = sidebar_html.replace('{{active_personal}}', active_classes if active_key == 'personal' else inactive_classes)
    sidebar = sidebar.replace('{{active_growth}}', active_classes if active_key == 'growth' else inactive_classes)
    sidebar = sidebar.replace('{{active_details}}', active_classes if active_key == 'details' else inactive_classes)
    sidebar = sidebar.replace('{{active_hall}}', active_classes if active_key == 'hall' else inactive_classes)

    # 2. Add flex wrapper and sidebar
    if '<div class="ml-64 flex' not in content:
        # Wrap the content inside body
        body_start = re.search(r'<body[^>]*>', content)
        if body_start:
            end_pos = body_start.end()
            # Extract everything until the script tags or closing body
            body_inner = content[end_pos:content.rfind('<script src="./assets/js/common.js">')]
            if body_inner.strip() == "":
                body_inner = content[end_pos:content.rfind('</body>')]
            
            # For C端_成长中心大盘.html, we might already have a flex wrapper from previous partial edit
            if '<div class="flex gap-12 items-start max-w-[1000px]' in body_inner:
                # Remove the old wrapper to rebuild
                body_inner = body_inner.replace('<div class="flex gap-12 items-start max-w-[1000px] w-full">', '')
                # and remove the closing div
                body_inner = body_inner.rsplit('</div>', 1)[0]
                
            new_inner = f"""
{sidebar}
<div class="ml-64 flex gap-12 items-start w-full pl-10 pt-4">
    {body_inner}
    {right_panel_html}
</div>
"""
            # Replace the body content
            content = content[:end_pos] + new_inner + content[content.rfind('<script src="./assets/js/common.js">'):] if '<script src="./assets/js/common.js">' in content else content[:end_pos] + new_inner + content[content.rfind('</body>'):]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Define right panels for annotations
growth_panel = """
    <!-- 右侧：控制台与批注区 -->
    <div class="w-[450px] flex flex-col shrink-0">
        
        <!-- 演示控制面板 -->
        <div class="bg-white p-5 rounded-2xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-gray-100 mb-8 relative overflow-hidden">
            <div class="absolute top-0 left-0 w-1 h-full bg-dfred"></div>
            <h3 class="text-sm font-bold mb-4 text-gray-800 flex items-center gap-2">
                <i class="fas fa-bolt text-yellow-500"></i> 原型状态切换控制台
            </h3>
            <div class="grid grid-cols-2 gap-3">
                <button onclick="setDemoState('normal')" id="btn-normal" class="px-3 py-2 text-xs font-bold rounded-lg bg-dfred text-white transition">【场景1】常态升段</button>
                <button onclick="setDemoState('protection')" id="btn-protection" class="px-3 py-2 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition">【场景2】90天保级中</button>
                <button onclick="setDemoState('soft-landing')" id="btn-soft-landing" class="px-3 py-2 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition">【场景3】防跌落生效</button>
                <button onclick="setDemoState('master')" id="btn-master" class="px-3 py-2 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition">【场景4】大师满级</button>
            </div>
            <p class="text-[10px] text-gray-400 mt-3 flex items-start">
                <i class="fas fa-info-circle mt-0.5 mr-1"></i> 点击上方按钮，左侧的原型将自动联动。
            </p>
        </div>

        <!-- 逻辑批注区 -->
        <div class="space-y-2">
            <div class="annotation-block">
                <div class="annotation-title">【业务逻辑】节点状态可视化</div>
                <div class="annotation-text">
                    <p>直观反映用户所处的生命周期：</p>
                    <ul class="list-disc ml-4 mt-1 space-y-1">
                        <li>已达成的段位，显示为红色的“勾”。</li>
                        <li>当前段位，显示高亮的带状边框和皇冠。</li>
                        <li>未达成的段位，置灰并显示锁图标。</li>
                    </ul>
                </div>
            </div>
            <div class="annotation-block">
                <div class="annotation-title">【业务逻辑】月度失效预警</div>
                <div class="annotation-text">
                    在进度条下方，新增了“本月新增”与“月底过期”的变动概览。提示用户抓紧做任务。
                </div>
            </div>
            <div class="annotation-block">
                <div class="annotation-title">【交互说明】特权区联动点亮</div>
                <div class="annotation-text">
                    下方的特权模块，会根据当前所在的段位，自动点亮或置灰。未解锁的特权带有锁标签。
                </div>
            </div>
            <div class="annotation-block">
                <div class="annotation-title">【页面跳转串联】</div>
                <div class="annotation-text">
                    <ul class="list-disc ml-4 mt-1 space-y-1">
                        <li>点击左上角“返回” ➔ 跳转至个人中心。</li>
                        <li>点击“去完成” ➔ 跳转至作业大厅。</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
"""

personal_panel = """
    <!-- 右侧：批注区 -->
    <div class="w-[350px] flex flex-col shrink-0 pt-4">
        <div class="space-y-2">
            <div class="annotation-block">
                <div class="annotation-title">【字段调整】保级无忧 → 当前有效成长值</div>
                <div class="annotation-text">
                    根据业务逻辑，普通情况下不应显示“保级无忧”，已修改为通用的“当前有效成长值”。
                </div>
            </div>
            <div class="annotation-block">
                <div class="annotation-title">【页面跳转串联】</div>
                <div class="annotation-text">
                    点击“专家护卫军”卡片，可直接跳转至【成长中心大盘】。
                </div>
            </div>
        </div>
    </div>
"""

hall_panel = """
    <!-- 右侧：批注区 -->
    <div class="w-[350px] flex flex-col shrink-0 pt-4">
        <div class="space-y-2">
            <div class="annotation-block">
                <div class="annotation-title">【页面跳转串联】</div>
                <div class="annotation-text">
                    此处为做任务的落地页。点击左上角返回按钮，可回到【个人中心】。
                </div>
            </div>
        </div>
    </div>
"""

process_file('C端_成长中心大盘.html', 'growth', growth_panel)
process_file('C端_个人中心.html', 'personal', personal_panel)
process_file('C端_作业大厅.html', 'hall', hall_panel)

