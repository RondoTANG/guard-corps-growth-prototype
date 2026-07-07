import os

html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_内容管理_文章发布页.html"

html_content = """<!DOCTYPE html>
<html lang="zh-CN" style="font-size: 14px;">
<head>
    <meta charset="utf-8"/>
    <title>文章发布 - 护卫军内容管理</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet"/>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        dfred: '#E60012',
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-gray-100 h-screen flex font-sans overflow-hidden">

<!-- Main Content -->
<aside class="w-64 bg-[#313C48] text-[#909399] flex flex-col shrink-0 text-sm overflow-hidden select-none">
    <div class="h-16 flex items-center px-6 bg-[#2B3643]">
        <span class="text-base font-bold text-white tracking-wider">东风护卫军后台</span>
    </div>
    <div class="flex-1 overflow-y-auto style-scrollbar">
        <nav class="flex flex-col pb-6 pt-2 space-y-1">
            <!-- 护卫军作业管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">护卫军作业管理</span>
                    <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                </div>
                <div class="flex flex-col">
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors menu-link">护卫军作业任务配置</a>
                </div>
            </div>
            
            <!-- 审核管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">审核管理</span>
                    <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                </div>
                <div class="flex flex-col">
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors menu-link">审核管理列表</a>
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">人工审核</a>
                </div>
            </div>

            <!-- 用户管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">用户管理</span>
                    <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                </div>
                <div class="flex flex-col">
                    <a href="B端_用户管理_XP干预页.html" class="px-9 py-2.5 hover:text-white transition-colors">用户列表</a>
                </div>
            </div>

            <!-- 内容管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">内容管理</span>
                    <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                </div>
                <div class="flex flex-col">
                    <a href="B端_内容管理_文章发布页.html" class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu">文章编辑</a>
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">优质内容管理</a>
                </div>
            </div>

            <!-- 系统设置 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">系统设置</span>
                    <i class="fas fa-chevron-up text-xs text-gray-400"></i>
                </div>
                <div class="flex flex-col">
                    <a href="B端_等级规则与XP配置页.html" class="px-9 py-2.5 hover:text-white transition-colors menu-link">成长规则配置</a>
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">文章管理</a>
                </div>
            </div>
            
        </nav>
    </div>
</aside>

<!-- Right Content Area -->
<div class="flex-1 flex flex-col min-w-0 overflow-hidden bg-gray-50">
    
    <!-- Top Header -->
    <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0 z-10">
        <div class="flex items-center text-sm">
            <span class="text-gray-500">内容管理</span>
            <i class="fas fa-angle-right mx-2 text-gray-400"></i>
            <span class="text-gray-500">文章编辑</span>
            <i class="fas fa-angle-right mx-2 text-gray-400"></i>
            <span class="text-gray-900 font-bold">发布新文章</span>
        </div>
        <div class="flex items-center space-x-4">
            <div class="flex items-center text-sm text-gray-600">
                <img src="https://ui-avatars.com/api/?name=Admin&background=E60012&color=fff" alt="Admin" class="w-8 h-8 rounded-full mr-2">
                <span>超级管理员</span>
            </div>
        </div>
    </header>

    <!-- Main Scrollable Content -->
    <main class="flex-1 overflow-y-auto p-6">
        
        <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
            <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
                <h2 class="text-lg font-bold text-gray-800">编辑文章内容</h2>
            </div>
            
            <div class="p-8 space-y-6">
                <!-- Title -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">文章标题 <span class="text-red-500">*</span></label>
                    <input type="text" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-3 border focus:border-dfred outline-none focus:ring-1 focus:ring-dfred" placeholder="请输入文章标题，最多 50 个字符">
                </div>

                <!-- Author -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">关联创作者 (发文用户) <span class="text-red-500">*</span></label>
                    <div class="flex items-center border border-gray-300 rounded-md p-2 w-72">
                        <img src="https://ui-avatars.com/api/?name=User&background=random" class="w-6 h-6 rounded-full mr-2">
                        <input type="text" class="w-full text-sm outline-none bg-transparent" placeholder="搜索护卫军用户..." value="护卫军-李师傅">
                    </div>
                </div>

                <!-- Content -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">正文内容 <span class="text-red-500">*</span></label>
                    <div class="border border-gray-300 rounded-md overflow-hidden">
                        <div class="bg-gray-50 border-b border-gray-200 px-3 py-2 flex items-center space-x-3 text-gray-500">
                            <i class="fas fa-bold cursor-pointer hover:text-gray-800"></i>
                            <i class="fas fa-italic cursor-pointer hover:text-gray-800"></i>
                            <i class="fas fa-list-ul cursor-pointer hover:text-gray-800"></i>
                            <i class="fas fa-image cursor-pointer hover:text-gray-800"></i>
                            <i class="fas fa-link cursor-pointer hover:text-gray-800"></i>
                        </div>
                        <textarea class="w-full h-64 p-4 text-sm outline-none resize-none" placeholder="在此输入文章正文..."></textarea>
                    </div>
                </div>

                <hr class="border-gray-200">

                <!-- Advanced Options -->
                <div>
                    <h3 class="text-sm font-bold text-gray-800 mb-4">运营及成长系统附加项</h3>
                    
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-5">
                        <label class="flex items-start cursor-pointer">
                            <div class="flex items-center h-5">
                                <input id="ace-guard-checkbox" type="checkbox" class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500 mt-0.5">
                            </div>
                            <div class="ml-3 text-sm">
                                <span class="font-bold text-gray-900 block mb-1">👑 关联并入选【王牌护卫军】</span>
                                <span class="text-gray-500">勾选后，文章将被打上王牌徽章标签。同时，将触发底层《成长规则配置》动作，为创作者发放对应的 XP 奖励。</span>
                            </div>
                        </label>
                    </div>
                </div>

            </div>
            
            <!-- Footer Actions -->
            <div class="px-6 py-4 bg-gray-50 border-t border-gray-200 flex justify-end space-x-3">
                <button class="px-5 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                    存为草稿
                </button>
                <button onclick="handlePublish()" class="px-5 py-2 bg-dfred text-white rounded-md text-sm font-medium hover:bg-red-700 transition-colors shadow-sm flex items-center">
                    <i class="fas fa-paper-plane mr-2"></i> 确认发布
                </button>
            </div>
        </div>

    </main>
</div>

<!-- Modal Overlay -->
<div id="publish-modal" class="fixed inset-0 bg-black bg-opacity-50 z-[100] hidden flex items-center justify-center transition-opacity">
    <div class="bg-white rounded-lg shadow-xl w-full max-w-md mx-4 overflow-hidden transform scale-95 transition-transform duration-200" id="publish-modal-content">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
            <h3 class="text-lg font-bold text-gray-900 flex items-center">
                <i class="fas fa-exclamation-circle text-orange-500 mr-2"></i> 发布确认与 XP 奖励联动
            </h3>
            <button onclick="closeModal()" class="text-gray-400 hover:text-gray-600 transition-colors">
                <i class="fas fa-times"></i>
            </button>
        </div>
        
        <div class="p-6">
            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                当前操作将发布文章并关联至【王牌护卫军】。
            </p>
            <div class="bg-orange-50 border border-orange-100 rounded-md p-4 mb-4">
                <p class="text-sm font-medium text-orange-800">
                    💡 <strong>系统提示：</strong> 根据 <a href="B端_等级规则与XP配置页.html" class="text-blue-600 underline">《成长规则配置》</a> 设定，该操作将自动为创作者（护卫军-李师傅）发放 <strong class="text-dfred text-lg mx-1">100</strong> XP 奖励。
                </p>
            </div>
            <p class="text-gray-500 text-xs">
                是否确认执行发布操作？发布后 XP 奖励将即刻生效并记录流账。
            </p>
        </div>
        
        <div class="px-6 py-4 bg-gray-50 border-t border-gray-200 flex justify-end space-x-3">
            <button onclick="closeModal()" class="px-4 py-2 border border-gray-300 rounded text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                取消
            </button>
            <button onclick="confirmPublish()" class="px-4 py-2 bg-dfred text-white rounded text-sm font-medium hover:bg-red-700 transition-colors">
                确认发布并奖励 XP
            </button>
        </div>
    </div>
</div>

<script>
    function handlePublish() {
        const isAceChecked = document.getElementById('ace-guard-checkbox').checked;
        if (isAceChecked) {
            // Show modal
            const modal = document.getElementById('publish-modal');
            const content = document.getElementById('publish-modal-content');
            modal.classList.remove('hidden');
            
            // tiny reflow delay to trigger animation
            setTimeout(() => {
                content.classList.remove('scale-95');
                content.classList.add('scale-100');
            }, 10);
        } else {
            alert('文章已直接发布成功！(未关联XP奖励)');
        }
    }

    function closeModal() {
        const modal = document.getElementById('publish-modal');
        const content = document.getElementById('publish-modal-content');
        content.classList.remove('scale-100');
        content.classList.add('scale-95');
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 200);
    }
    
    function confirmPublish() {
        closeModal();
        setTimeout(() => {
            alert('发布成功！作者已成功获取 100 XP。');
        }, 300);
    }
</script>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created {html_path}")
