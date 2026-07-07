import os

html_file = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_新建作业.html'

html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新建作业 - 东风护卫军后台</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        dfred: '#E60012',
                        dfredHover: '#cc0010',
                        dfblue: '#1890ff',
                    }
                }
            }
        }
    </script>
    <style>
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; }
        ::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #9ca3af; }
        
        .toggle-checkbox:checked { right: 0; border-color: #f97316; }
        .toggle-checkbox:checked + .toggle-label { background-color: #f97316; }

        .step-content { display: none; }
        .step-content.active { display: block; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans h-screen flex overflow-hidden text-sm">

    <!-- Left Sidebar -->
    <div id="b-sidebar-container" class="shrink-0 flex h-full"></div>
    <script src="b_sidebar.js"></script>
    <script>initBSidebar('');</script>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col min-w-0 bg-gray-50 relative">
        <!-- Header -->
        <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0 z-10 shadow-sm">
            <div class="flex items-center text-sm text-gray-500">
                <a href="#" class="hover:text-dfblue">护卫军作业管理</a><span class="mx-2">/</span>
                <a href="B端_作业管理列表.html" class="hover:text-dfblue">作业管理</a><span class="mx-2">/</span>
                <span class="text-gray-900 font-medium">新建作业</span>
            </div>
            <div class="flex items-center gap-4">
                <div class="flex items-center gap-2 cursor-pointer">
                    <div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center text-gray-500"><i class="fas fa-user text-sm"></i></div>
                    <span class="text-sm font-medium text-gray-700">汤志朗</span>
                </div>
            </div>
        </header>

        <div class="flex-1 overflow-auto pb-24">
            <!-- Top Wizard -->
            <div class="bg-white border-b border-gray-200 py-6 mb-6 sticky top-0 z-20">
                <div class="max-w-4xl mx-auto flex items-center justify-between px-8">
                    <div class="flex items-center cursor-pointer step-nav" onclick="goToStep(1)">
                        <div id="step-icon-1" class="w-8 h-8 rounded-full bg-dfblue text-white flex items-center justify-center font-bold text-sm shadow-md transition-all">1</div>
                        <span id="step-text-1" class="ml-3 font-bold text-dfblue transition-all">第一步：基础信息</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-200 mx-6"></div>
                    <div class="flex items-center cursor-pointer step-nav" onclick="goToStep(2)">
                        <div id="step-icon-2" class="w-8 h-8 rounded-full border-2 border-gray-300 bg-white text-gray-400 flex items-center justify-center font-bold text-sm transition-all">2</div>
                        <span id="step-text-2" class="ml-3 font-medium text-gray-400 transition-all">第二步：内容配置</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-200 mx-6"></div>
                    <div class="flex items-center cursor-pointer step-nav" onclick="goToStep(3)">
                        <div id="step-icon-3" class="w-8 h-8 rounded-full border-2 border-gray-300 bg-white text-gray-400 flex items-center justify-center font-bold text-sm transition-all">3</div>
                        <span id="step-text-3" class="ml-3 font-medium text-gray-400 transition-all">第三步：奖励配置</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-200 mx-6"></div>
                    <div class="flex items-center cursor-pointer step-nav" onclick="goToStep(4)">
                        <div id="step-icon-4" class="w-8 h-8 rounded-full border-2 border-gray-300 bg-white text-gray-400 flex items-center justify-center font-bold text-sm transition-all">4</div>
                        <span id="step-text-4" class="ml-3 font-medium text-gray-400 transition-all">第四步：推送策略</span>
                    </div>
                </div>
            </div>

            <div class="max-w-4xl mx-auto">
                <!-- STEP 1: Basic Info -->
                <div id="step-1" class="step-content active space-y-6">
                    <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
                        <h2 class="text-lg font-bold text-gray-900 border-l-4 border-dfblue pl-3 mb-6">作业基本信息</h2>
                        <div class="grid grid-cols-2 gap-x-12 gap-y-6">
                            <div class="space-y-6">
                                <div>
                                    <label class="block text-sm text-gray-700 mb-2">作业封面 <span class="text-xs text-gray-400 ml-2">建议比例3:2，大小1M以内</span></label>
                                    <div class="border-2 border-dashed border-gray-300 rounded-lg h-32 flex flex-col items-center justify-center text-gray-400 bg-gray-50 hover:bg-gray-100 hover:border-dfblue cursor-pointer transition-colors">
                                        <i class="far fa-image text-2xl mb-2"></i>
                                        <span class="text-xs">点击上传封面图</span>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm text-gray-700 mb-2"><span class="text-red-500 mr-1">*</span>作业总量</label>
                                    <input type="number" class="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none" placeholder="请输入作业总个数">
                                </div>
                            </div>

                            <div class="space-y-6">
                                <div>
                                    <label class="block text-sm text-gray-700 mb-2"><span class="text-red-500 mr-1">*</span>作业用途分类</label>
                                    <div class="flex gap-4">
                                        <select class="flex-1 border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none bg-white">
                                            <option>转发作业</option>
                                        </select>
                                        <select class="flex-1 border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none bg-white">
                                            <option>选择用途分类</option>
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm text-gray-700 mb-2"><span class="text-red-500 mr-1">*</span>作业时间</label>
                                    <div class="flex items-center border border-gray-300 rounded-md px-3 py-2 bg-white focus-within:border-dfblue">
                                        <input type="text" class="text-sm outline-none w-full" placeholder="开始日期">
                                        <span class="text-gray-300 mx-2">→</span>
                                        <input type="text" class="text-sm outline-none w-full text-right" placeholder="结束日期">
                                        <i class="far fa-calendar-alt text-gray-400 ml-2"></i>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm text-gray-700 mb-2">
                                        <span class="text-red-500 mr-1">*</span>作业优先级 <i class="far fa-question-circle text-gray-400 ml-1"></i>
                                    </label>
                                    <div class="flex items-center gap-6 mt-2">
                                        <label class="flex items-center cursor-pointer">
                                            <input type="radio" name="priority" class="w-4 h-4 text-dfblue border-gray-300 focus:ring-dfblue" checked>
                                            <span class="ml-2 text-gray-700">常规作业</span>
                                        </label>
                                        <label class="flex items-center cursor-pointer">
                                            <input type="radio" name="priority" class="w-4 h-4 text-dfblue border-gray-300 focus:ring-dfblue">
                                            <span class="ml-2 text-gray-700">紧急作业 (加急展示)</span>
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Threshold (Moved to Step 1 per standard logical flow or keep here) -->
                    <div class="bg-white rounded-lg border border-orange-200 shadow-sm p-8 relative overflow-hidden">
                        <div class="absolute top-0 left-0 w-1 h-full bg-orange-500"></div>
                        <h2 class="text-lg font-bold text-gray-900 flex items-center mb-6">
                            <span class="text-orange-600 mr-2">【新增】</span>成长策略：承接门槛
                        </h2>
                        
                        <div class="flex gap-12">
                            <div class="flex-1">
                                <label class="block font-bold text-gray-800 mb-2">配置承接门槛 <span class="font-normal text-gray-500">（限制作业领取资格）</span></label>
                                <select class="w-full border border-orange-300 rounded-md px-3 py-2 text-sm focus:border-orange-500 outline-none bg-orange-50/30">
                                    <option>Lv4 大师护卫军 (核心产出层)</option>
                                    <option>Lv3 专家护卫军</option>
                                    <option>Lv2 熟练护卫军</option>
                                    <option>无门槛</option>
                                </select>
                                <div class="text-xs text-gray-500 mt-2">设置后，不满足条件的用户在操作领取作业时会被拦截提示。</div>
                            </div>
                            <div class="flex-1">
                                <label class="block font-bold text-gray-800 mb-2">前台外显策略 <span class="font-normal text-gray-500">（调控机制）</span></label>
                                <div class="flex items-center mb-2">
                                    <div class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in">
                                        <input type="checkbox" name="toggle" id="toggle1" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 translate-x-5 border-orange-500" checked/>
                                        <label for="toggle1" class="toggle-label block overflow-hidden h-5 rounded-full bg-orange-500 cursor-pointer"></label>
                                    </div>
                                    <span class="font-bold text-gray-800">未达标用户也【全员可见】</span>
                                </div>
                                <div class="text-xs text-orange-600 bg-orange-50 p-2 rounded">强力推荐开启。不满足条件的用户仍会在大厅看到该高优任务，点击时提示“升级至要求段位即可领取作业”，极大刺激升级欲望。</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- STEP 2: Content -->
                <div id="step-2" class="step-content space-y-6">
                    <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
                        <h2 class="text-lg font-bold text-gray-900 border-l-4 border-dfblue pl-3 mb-6">作业内容配置</h2>
                        <div class="border border-dashed border-gray-300 rounded-lg p-12 text-center text-gray-400 bg-gray-50">
                            <i class="fas fa-edit text-3xl mb-3"></i>
                            <p>此处为作业的具体物料、文案、链接等内容的配置模块</p>
                        </div>
                    </div>
                </div>

                <!-- STEP 3: Rewards (XP moved here) -->
                <div id="step-3" class="step-content space-y-6">
                    <!-- Standard Points Reward -->
                    <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
                        <h2 class="text-lg font-bold text-gray-900 border-l-4 border-dfblue pl-3 mb-6">积分奖励配置</h2>
                        <div class="grid grid-cols-2 gap-8">
                            <div>
                                <label class="block text-sm text-gray-700 mb-2">基础奖励积分 (必填)</label>
                                <input type="number" class="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none" placeholder="输入积分">
                            </div>
                            <div>
                                <label class="block text-sm text-gray-700 mb-2">效果奖励模式</label>
                                <select class="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none">
                                    <option>无效果奖励</option>
                                    <option>按转评赞数量</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- XP Reward -->
                    <div class="bg-white rounded-lg border border-red-200 shadow-sm p-8 relative overflow-hidden">
                        <div class="absolute top-0 left-0 w-1 h-full bg-dfred"></div>
                        <h2 class="text-lg font-bold text-gray-900 flex items-center mb-6">
                            <span class="text-dfred mr-2">【新增】</span>成长策略：单次发放XP配置
                        </h2>
                        
                        <div class="flex gap-12 items-start">
                            <div class="flex-1">
                                <label class="block font-bold text-gray-800 mb-2">关联基础XP <span class="font-normal text-gray-500">（由系统自动带出）</span></label>
                                <div class="bg-gray-100 rounded px-3 py-2 text-gray-500 flex items-center">
                                    <i class="fas fa-link mr-2 text-gray-400"></i>
                                    当前作业用途默认下发: <span class="font-bold text-gray-700 ml-1">100 XP</span>
                                </div>
                                <div class="text-xs text-gray-500 mt-2">该数值由《成长规则配置》统一管理，如需全局调整请前往系统设置。</div>
                            </div>
                            <div class="flex-1">
                                <label class="block font-bold text-gray-800 mb-2">特殊干预发放XP <span class="font-normal text-gray-500">（覆盖默认值）</span></label>
                                <div class="flex items-center">
                                    <input type="number" class="w-40 border border-red-300 rounded-l-md px-3 py-2 text-sm focus:border-red-500 outline-none font-bold text-dfred bg-red-50/30" value="200">
                                    <div class="bg-red-100 text-red-600 border border-l-0 border-red-300 rounded-r-md px-3 py-2 font-bold">XP</div>
                                </div>
                                <div class="text-xs text-red-500 mt-2 flex items-start">
                                    <i class="fas fa-exclamation-triangle mt-0.5 mr-1"></i> 
                                    <span>已修改。本次作业下发 XP 将以此数值为准，并在前端卡片特殊高亮。</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Tags -->
                    <div class="bg-white rounded-lg border border-blue-200 shadow-sm p-8 relative overflow-hidden">
                        <div class="absolute top-0 left-0 w-1 h-full bg-blue-500"></div>
                        <h2 class="text-lg font-bold text-gray-900 flex items-center mb-6">
                            <span class="text-blue-600 mr-2">【新增】</span>成长策略：外显福利标签
                        </h2>
                        
                        <label class="block font-bold text-gray-800 mb-3">选择要在前台外显的福利/成长标签 <span class="font-normal text-gray-500">（最多选2个，提升作业领取转化）</span></label>
                        <div class="flex flex-wrap gap-3">
                            <div class="px-4 py-2 border-2 border-blue-500 bg-blue-50 text-blue-700 rounded-md cursor-pointer font-bold flex items-center relative shadow-sm">
                                护卫军专项
                                <i class="fas fa-check-circle absolute -right-2 -top-2 text-blue-500 bg-white rounded-full text-lg shadow-sm"></i>
                            </div>
                            <div class="px-4 py-2 border border-gray-300 bg-white hover:bg-gray-50 text-gray-600 rounded-md cursor-pointer transition-colors font-medium">
                                核心共创
                            </div>
                            <div class="px-4 py-2 border-2 border-blue-500 bg-blue-50 text-blue-700 rounded-md cursor-pointer font-bold flex items-center relative shadow-sm">
                                双倍XP池
                                <i class="fas fa-check-circle absolute -right-2 -top-2 text-blue-500 bg-white rounded-full text-lg shadow-sm"></i>
                            </div>
                            <div class="px-4 py-2 border border-gray-300 bg-white hover:bg-gray-50 text-gray-600 rounded-md cursor-pointer transition-colors font-medium text-gray-400 border-dashed">
                                <i class="fas fa-plus mr-1"></i> 新增标签
                            </div>
                        </div>
                    </div>
                </div>

                <!-- STEP 4: Push -->
                <div id="step-4" class="step-content space-y-6">
                    <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
                        <h2 class="text-lg font-bold text-gray-900 border-l-4 border-dfblue pl-3 mb-6">作业推送策略</h2>
                        
                        <div class="mb-6">
                            <label class="block font-bold text-gray-800 mb-3"><span class="text-red-500 mr-1">*</span>推送人员范围</label>
                            <div class="flex items-center gap-6">
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="push" class="w-4 h-4 text-dfblue border-gray-300">
                                    <span class="ml-2 text-gray-700">全量推送</span>
                                </label>
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="push" class="w-4 h-4 text-dfblue border-gray-300">
                                    <span class="ml-2 text-gray-700">白名单推送</span>
                                </label>
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="push" class="w-4 h-4 text-dfblue border-gray-300" checked>
                                    <span class="ml-2 text-gray-700 font-bold">按段位标签推送</span>
                                </label>
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="push" class="w-4 h-4 text-dfblue border-gray-300">
                                    <span class="ml-2 text-gray-700">人群包推送</span>
                                </label>
                            </div>
                        </div>

                        <!-- Tag Selection Box -->
                        <div class="border border-blue-100 rounded-lg p-5 bg-blue-50/30 mb-6">
                            <label class="block text-sm font-bold text-gray-800 mb-3">选择触达的段位标签 (优先精准触达核心用户)</label>
                            <div class="flex gap-4">
                                <div class="px-5 py-2.5 border border-gray-300 bg-white rounded-md cursor-pointer hover:border-dfblue transition-colors flex items-center font-medium text-gray-600 shadow-sm">
                                    <i class="fas fa-seedling text-green-500 mr-2"></i> Lv1 新秀
                                </div>
                                <div class="px-5 py-2.5 border border-gray-300 bg-white rounded-md cursor-pointer hover:border-dfblue transition-colors flex items-center font-medium text-gray-600 shadow-sm">
                                    <i class="fas fa-shield-alt text-gray-500 mr-2"></i> Lv2 熟练
                                </div>
                                <div class="px-5 py-2.5 border-2 border-dfblue bg-blue-50 text-dfblue rounded-md cursor-pointer font-bold flex items-center relative shadow-sm">
                                    <i class="fas fa-medal text-dfblue mr-2"></i> Lv3 专家
                                    <i class="fas fa-check-circle absolute -right-2 -top-2 text-dfblue bg-white rounded-full text-lg"></i>
                                </div>
                                <div class="px-5 py-2.5 border border-gray-300 bg-white rounded-md cursor-pointer hover:border-dfblue transition-colors flex items-center font-medium text-gray-600 shadow-sm">
                                    <i class="fas fa-crown text-orange-500 mr-2"></i> Lv4 大师
                                </div>
                            </div>
                        </div>

                        <div>
                            <label class="block font-bold text-gray-800 mb-2">排除人员 <span class="font-normal text-gray-500 text-sm">（选填）</span></label>
                            <input type="text" class="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:border-dfblue outline-none" placeholder="输入名单或选择人群包">
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- Sticky Footer -->
        <div class="absolute bottom-0 left-0 right-0 bg-white border-t border-gray-200 p-4 flex justify-center gap-4 z-20 shadow-[0_-5px_10px_rgba(0,0,0,0.02)]">
            <button id="btn-prev" class="hidden px-8 py-2 border border-gray-300 rounded text-gray-700 hover:bg-gray-50 transition-colors font-medium" onclick="prevStep()">上一步</button>
            <button id="btn-next" class="px-8 py-2 bg-dfblue hover:bg-blue-600 text-white rounded font-medium transition-colors shadow-sm" onclick="nextStep()">下一步</button>
            <button id="btn-submit" class="hidden px-8 py-2 bg-dfred hover:bg-dfredHover text-white rounded font-medium transition-colors shadow-sm">发布作业</button>
        </div>

    </main>

    <script>
        let currentStep = 1;
        const totalSteps = 4;

        function updateUI() {
            // Update contents
            document.querySelectorAll('.step-content').forEach(el => el.classList.remove('active'));
            document.getElementById('step-' + currentStep).classList.add('active');

            // Update top nav
            for(let i=1; i<=totalSteps; i++) {
                const icon = document.getElementById('step-icon-' + i);
                const text = document.getElementById('step-text-' + i);
                
                if (i === currentStep) {
                    icon.className = "w-8 h-8 rounded-full bg-dfblue text-white flex items-center justify-center font-bold text-sm shadow-md transition-all";
                    text.className = "ml-3 font-bold text-dfblue transition-all";
                } else if (i < currentStep) {
                    icon.className = "w-8 h-8 rounded-full bg-blue-100 text-dfblue flex items-center justify-center font-bold text-sm transition-all";
                    icon.innerHTML = '<i class="fas fa-check"></i>';
                    text.className = "ml-3 font-medium text-gray-700 transition-all";
                } else {
                    icon.className = "w-8 h-8 rounded-full border-2 border-gray-300 bg-white text-gray-400 flex items-center justify-center font-bold text-sm transition-all";
                    icon.innerHTML = i;
                    text.className = "ml-3 font-medium text-gray-400 transition-all";
                }
            }

            // Update buttons
            document.getElementById('btn-prev').classList.toggle('hidden', currentStep === 1);
            
            if (currentStep === totalSteps) {
                document.getElementById('btn-next').classList.add('hidden');
                document.getElementById('btn-submit').classList.remove('hidden');
            } else {
                document.getElementById('btn-next').classList.remove('hidden');
                document.getElementById('btn-submit').classList.add('hidden');
            }
        }

        function nextStep() {
            if(currentStep < totalSteps) {
                currentStep++;
                updateUI();
            }
        }

        function prevStep() {
            if(currentStep > 1) {
                currentStep--;
                updateUI();
            }
        }

        function goToStep(step) {
            currentStep = step;
            updateUI();
        }
    </script>
</body>
</html>"""

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

