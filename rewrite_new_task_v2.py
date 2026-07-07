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
                        dfblue: '#1890ff',
                        dflightblue: '#e6f7ff',
                        dfred: '#ff4d4f'
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
        
        body { background-color: #ffffff; color: #333; }
        .step-content { display: none; }
        .step-content.active { display: block; animation: fadeIn 0.2s ease; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .form-label { display: block; font-size: 14px; color: #333; margin-bottom: 8px; }
        .required::before { content: "*"; color: #ff4d4f; margin-right: 4px; }
        
        .form-input {
            width: 100%; border: 1px solid #d9d9d9; border-radius: 2px; padding: 6px 11px;
            font-size: 14px; color: #333; outline: none; transition: all 0.2s;
        }
        .form-input:focus { border-color: #1890ff; box-shadow: 0 0 0 2px rgba(24,144,255,0.2); }
        
        .toggle-checkbox:checked { right: 0; border-color: #1890ff; }
        .toggle-checkbox:checked + .toggle-label { background-color: #1890ff; }
    </style>
</head>
<body class="h-screen flex overflow-hidden">

    <!-- Left Sidebar -->
    <div id="b-sidebar-container" class="shrink-0 flex h-full border-r border-gray-200"></div>
    <script src="b_sidebar.js"></script>
    <script>initBSidebar('');</script>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col min-w-0 bg-white relative">
        
        <!-- Header -->
        <header class="h-14 flex items-center justify-between px-6 shrink-0 border-b border-gray-100 bg-white">
            <div class="text-gray-800 font-medium">新建作业</div>
            <div class="flex items-center text-sm text-gray-600">
                <i class="far fa-user mr-2"></i> 汤志朗
            </div>
        </header>

        <div class="flex-1 overflow-auto pb-20">
            <!-- Top Wizard -->
            <div class="bg-gray-50 border-b border-gray-200 py-6 mb-8">
                <div class="max-w-4xl mx-auto flex items-center justify-between px-8 relative">
                    <!-- Step 1 -->
                    <div class="flex items-center cursor-pointer relative z-10" onclick="goToStep(1)">
                        <div id="step-icon-1" class="w-8 h-8 rounded-full border border-dfblue text-dfblue flex items-center justify-center font-bold text-sm bg-white"><i class="fas fa-times text-xs"></i></div>
                        <span id="step-text-1" class="ml-2 font-medium text-dfred">第一步</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-300 mx-4"></div>
                    <!-- Step 2 -->
                    <div class="flex items-center cursor-pointer relative z-10" onclick="goToStep(2)">
                        <div id="step-icon-2" class="w-8 h-8 rounded-full border border-gray-300 text-gray-400 flex items-center justify-center font-medium text-sm bg-white">2</div>
                        <span id="step-text-2" class="ml-2 font-medium text-gray-500">第二步</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-300 mx-4"></div>
                    <!-- Step 3 -->
                    <div class="flex items-center cursor-pointer relative z-10" onclick="goToStep(3)">
                        <div id="step-icon-3" class="w-8 h-8 rounded-full border border-gray-300 text-gray-400 flex items-center justify-center font-medium text-sm bg-white">3</div>
                        <span id="step-text-3" class="ml-2 font-medium text-gray-500">第三步</span>
                    </div>
                    <div class="flex-1 h-px bg-gray-300 mx-4"></div>
                    <!-- Step 4 -->
                    <div class="flex items-center cursor-pointer relative z-10" onclick="goToStep(4)">
                        <div id="step-icon-4" class="w-8 h-8 rounded-full border border-dfblue text-dfblue flex items-center justify-center font-medium text-sm bg-white"><i class="fas fa-check text-xs"></i></div>
                        <span id="step-text-4" class="ml-2 font-medium text-gray-800">第四步</span>
                    </div>
                </div>
            </div>

            <!-- STEP 1: Basic Info -->
            <div id="step-1" class="step-content active px-10 pb-10">
                <div class="max-w-6xl mx-auto">
                    <h2 class="text-base font-bold text-gray-800 mb-6">作业设置</h2>
                    
                    <div class="mb-10">
                        <h3 class="text-sm font-bold text-gray-800 mb-4">基本信息</h3>
                        <div class="grid grid-cols-[300px_1fr] gap-12">
                            <!-- Left -->
                            <div>
                                <label class="form-label required">作业封面</label>
                                <div class="border border-dashed border-gray-300 rounded bg-gray-50 h-32 flex flex-col items-center justify-center text-center cursor-pointer hover:border-dfblue text-gray-500">
                                    <i class="fas fa-inbox text-2xl text-dfblue mb-2"></i>
                                    <span class="text-xs">点击或将文件拖拽到这里上传</span>
                                </div>
                                <div class="text-[11px] text-gray-400 mt-2">请上传比例为750x500的图片，建议图标比例3:2,大小1M以内</div>
                                <div class="text-[11px] text-red-500 mt-1">作业封面是必填项</div>
                            </div>
                            
                            <!-- Right -->
                            <div class="grid grid-cols-2 gap-x-8 gap-y-6">
                                <div>
                                    <label class="form-label required">作业名称</label>
                                    <input type="text" class="form-input border-red-400" placeholder="请输入作业名称">
                                    <div class="text-[11px] text-red-500 mt-1">作业名称是必填项</div>
                                </div>
                                <div>
                                    <label class="form-label required">作业类型</label>
                                    <select class="form-input">
                                        <option>转发作业</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="form-label required">作业开始/结束时间</label>
                                    <div class="flex items-center border border-red-400 rounded-sm px-3 py-1.5 bg-white">
                                        <input type="text" class="text-sm outline-none w-full text-gray-400" placeholder="开始日期">
                                        <span class="text-gray-300 mx-2">→</span>
                                        <input type="text" class="text-sm outline-none w-full text-right text-gray-400" placeholder="结束日期">
                                        <i class="far fa-calendar-alt text-gray-300 ml-2"></i>
                                    </div>
                                    <div class="text-[11px] text-red-500 mt-1">作业开始/结束时间是必填项</div>
                                </div>
                                <div>
                                    <label class="form-label required">作业平台</label>
                                    <select class="form-input border-red-400 text-gray-400">
                                        <option>请选择</option>
                                    </select>
                                    <div class="text-[11px] text-red-500 mt-1">作业平台是必填项</div>
                                </div>
                                <div class="col-span-2">
                                    <label class="form-label required flex items-center">作业优先级 <i class="far fa-question-circle text-gray-400 ml-1"></i></label>
                                    <div class="flex items-center gap-6 mt-1">
                                        <label class="flex items-center cursor-pointer">
                                            <input type="radio" name="priority" class="w-4 h-4 text-dfblue border-gray-300 focus:ring-dfblue" checked>
                                            <span class="ml-2 text-sm text-gray-700">常规作业</span>
                                        </label>
                                        <label class="flex items-center cursor-pointer">
                                            <input type="radio" name="priority" class="w-4 h-4 text-gray-300">
                                            <span class="ml-2 text-sm text-gray-700">紧急作业</span>
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="mt-6 w-1/3">
                            <label class="form-label">作业用途分类</label>
                            <input type="text" class="form-input" placeholder="选择用途分类">
                        </div>

                        <div class="mt-6 w-1/3">
                            <label class="form-label required">作业总量</label>
                            <div class="relative border border-red-400 rounded-sm">
                                <input type="number" class="w-full px-3 py-1.5 text-sm outline-none" placeholder="请输入作业总个数">
                                <i class="fas fa-arrow-up absolute right-3 top-2 text-gray-400 text-xs"></i>
                            </div>
                            <div class="text-[11px] text-red-500 mt-1">作业总量是必填项</div>
                        </div>
                    </div>

                    <!-- New Added: Growth threshold config (Cleanly integrated) -->
                    <div class="mb-10 p-5 bg-orange-50/50 border border-orange-100 rounded">
                        <h3 class="text-sm font-bold text-orange-600 mb-4 flex items-center"><i class="fas fa-layer-group mr-2"></i>【新增】成长策略：承接门槛</h3>
                        <div class="flex gap-16">
                            <div class="w-1/3">
                                <label class="form-label font-bold">限制作业领取资格段位</label>
                                <select class="form-input bg-white">
                                    <option>Lv3 专家护卫军 (核心产出层)</option>
                                    <option>Lv2 熟练护卫军</option>
                                    <option>无门槛</option>
                                </select>
                                <div class="text-xs text-gray-500 mt-2">不满足条件的用户在操作领取作业时会被拦截。</div>
                            </div>
                            <div class="w-1/2">
                                <label class="form-label font-bold">前台外显策略（调控）</label>
                                <div class="flex items-center mt-2">
                                    <div class="relative inline-block w-10 mr-3 align-middle select-none">
                                        <input type="checkbox" name="toggle" id="toggle1" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 translate-x-5 border-dfblue" checked/>
                                        <label for="toggle1" class="toggle-label block overflow-hidden h-5 rounded-full bg-dfblue cursor-pointer"></label>
                                    </div>
                                    <span class="text-sm text-gray-800">未达标用户也全员可见</span>
                                </div>
                                <div class="text-xs text-gray-500 mt-2">推荐开启。不满足条件的用户大厅可见该任务，点击提示“升级段位即可领取作业”，刺激升级。</div>
                            </div>
                        </div>
                    </div>

                    <div class="mb-10">
                        <h3 class="text-sm font-bold text-gray-800 mb-4">作业推送</h3>
                        <div class="space-y-6">
                            <div>
                                <label class="form-label required">推送人员</label>
                                <div class="flex items-center gap-8 mt-2">
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="push" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">全量推送</span>
                                    </label>
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="push" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">白名单推送</span>
                                    </label>
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="push" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">标签推送</span>
                                    </label>
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="push" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">人群包推送</span>
                                    </label>
                                </div>
                            </div>
                            
                            <div>
                                <label class="form-label">排除人员</label>
                                <div class="flex items-center gap-8 mt-2">
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="exclude" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">黑名单剔除</span>
                                    </label>
                                    <label class="flex items-center cursor-pointer">
                                        <input type="radio" name="exclude" class="w-4 h-4 text-gray-300">
                                        <span class="ml-2 text-sm text-gray-700">标签剔除</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- STEP 2: Content -->
            <div id="step-2" class="step-content px-10 pb-10">
                <div class="max-w-6xl mx-auto">
                    <h2 class="text-base font-bold text-gray-800 mb-6">作业素材</h2>
                    <div class="flex gap-2 mb-8">
                        <button class="bg-dfblue text-white px-4 py-1.5 rounded-sm text-sm">添加素材</button>
                        <button class="bg-dfblue text-white px-4 py-1.5 rounded-sm text-sm">添加素材组</button>
                    </div>

                    <h2 class="text-base font-bold text-gray-800 mb-6">作业要求和积分规则</h2>
                    <div class="space-y-6 max-w-4xl">
                        <div>
                            <label class="form-label required">作业要求</label>
                            <div class="border border-gray-300 rounded-sm">
                                <div class="border-b border-gray-300 bg-gray-50 flex items-center px-2 py-1 gap-2 text-gray-600 text-sm">
                                    <span class="px-2 cursor-pointer hover:text-dfblue">正文</span>
                                    <span class="text-gray-300">|</span>
                                    <i class="fas fa-bold px-1 cursor-pointer hover:text-dfblue"></i>
                                    <i class="fas fa-italic px-1 cursor-pointer hover:text-dfblue"></i>
                                    <i class="fas fa-underline px-1 cursor-pointer hover:text-dfblue"></i>
                                    <span class="text-gray-300">|</span>
                                    <i class="far fa-image px-1 cursor-pointer hover:text-dfblue"></i>
                                </div>
                                <textarea class="w-full h-40 p-3 outline-none resize-none text-sm text-gray-400" placeholder="请输入作业要求"></textarea>
                                <div class="text-right px-2 pb-1 text-xs text-gray-400">0/2000</div>
                            </div>
                            <div class="text-[11px] text-red-500 mt-1">作业要求未完善，无法提交/保存</div>
                        </div>
                        
                        <div>
                            <label class="form-label required">积分规则</label>
                            <div class="border border-gray-300 rounded-sm">
                                <div class="border-b border-gray-300 bg-gray-50 flex items-center px-2 py-1 gap-2 text-gray-600 text-sm">
                                    <span class="px-2 cursor-pointer hover:text-dfblue">正文</span>
                                    <span class="text-gray-300">|</span>
                                    <i class="fas fa-bold px-1 cursor-pointer hover:text-dfblue"></i>
                                    <i class="fas fa-italic px-1 cursor-pointer hover:text-dfblue"></i>
                                </div>
                                <textarea class="w-full h-40 p-3 outline-none resize-none text-sm text-gray-400" placeholder="请输入积分规则内容"></textarea>
                                <div class="text-right px-2 pb-1 text-xs text-gray-400">0/2000</div>
                            </div>
                            <div class="text-[11px] text-red-500 mt-1">规则内容是必填项</div>
                        </div>
                        
                        <div class="flex items-center mt-6">
                            <span class="text-sm text-gray-800 mr-4">弹窗广告推送</span>
                            <div class="relative inline-block w-10 align-middle select-none">
                                <input type="checkbox" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 border-gray-300"/>
                                <label class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300 cursor-pointer"></label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- STEP 3: Rewards -->
            <div id="step-3" class="step-content px-10 pb-10">
                <div class="max-w-6xl mx-auto">
                    <h2 class="text-base font-bold text-dfblue mb-6">奖励基础设置</h2>
                    
                    <div class="grid grid-cols-2 gap-x-12 gap-y-8 max-w-4xl mb-12">
                        <div>
                            <label class="form-label required">作业总量</label>
                            <div class="relative border border-gray-300 rounded-sm bg-gray-50">
                                <input type="text" class="w-full px-3 py-1.5 text-sm outline-none bg-transparent text-gray-400 cursor-not-allowed" value="请先在第一步填写作业总量" readonly>
                                <i class="fas fa-arrow-up absolute right-3 top-2 text-gray-400 text-xs"></i>
                            </div>
                        </div>
                        <div>
                            <label class="form-label required">积分预算</label>
                            <div class="flex items-center gap-2">
                                <input type="number" class="form-input w-full bg-gray-50 text-gray-500" value="8" readonly>
                                <span class="text-sm text-gray-600">积分</span>
                            </div>
                        </div>
                        <div>
                            <label class="form-label required">基础奖励积分</label>
                            <div class="flex items-center gap-2">
                                <input type="number" class="form-input w-full" value="8">
                                <span class="text-sm text-gray-600">积分</span>
                            </div>
                        </div>
                        <div>
                            <label class="form-label required">额外奖励积分: (0积分)</label>
                            <div class="flex items-center gap-6 mt-2">
                                <label class="flex items-center cursor-not-allowed text-gray-400">
                                    <input type="radio" class="w-4 h-4 text-gray-200" disabled>
                                    <span class="ml-2 text-sm">开启</span>
                                </label>
                                <label class="flex items-center cursor-not-allowed text-gray-400">
                                    <input type="radio" class="w-4 h-4 text-gray-200" checked disabled>
                                    <span class="ml-2 text-sm">关闭</span>
                                </label>
                            </div>
                        </div>
                        <div class="col-span-2">
                            <label class="form-label required">效果奖励积分</label>
                            <div class="flex items-center mt-2">
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" class="w-4 h-4 text-dfblue border-gray-300 focus:ring-dfblue" checked>
                                    <span class="ml-2 text-sm text-gray-700">普通奖励模式</span>
                                </label>
                            </div>
                            <div class="text-[11px] text-red-500 mt-1">效果奖励积分是必填项</div>
                        </div>
                    </div>

                    <!-- New Added: Growth XP and Tags -->
                    <div class="max-w-4xl border-t border-gray-100 pt-8 mt-8">
                        <h2 class="text-base font-bold text-dfblue mb-6">成长激励策略配置 <span class="text-xs text-gray-400 font-normal ml-2">（此模块为新增的成长体系专属配置）</span></h2>
                        
                        <div class="bg-blue-50/30 border border-blue-100 rounded p-6 mb-6">
                            <h3 class="text-sm font-bold text-gray-800 mb-4">单次发放XP配置</h3>
                            <div class="flex gap-12 items-start">
                                <div class="flex-1">
                                    <label class="block text-sm text-gray-700 mb-2">关联基础XP <span class="text-xs text-gray-400">（由系统带出）</span></label>
                                    <div class="bg-gray-100 rounded-sm px-3 py-1.5 text-gray-500 text-sm">
                                        <i class="fas fa-link mr-1"></i> 当前用途默认下发: <strong class="text-gray-700">100 XP</strong>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <label class="block text-sm text-gray-700 mb-2">特殊干预发放XP <span class="text-xs text-gray-400">（覆盖默认值）</span></label>
                                    <div class="flex items-center">
                                        <input type="number" class="w-32 border border-red-300 rounded-l-sm px-3 py-1.5 text-sm outline-none font-bold text-dfred bg-red-50/20" value="200">
                                        <div class="bg-red-50 text-dfred border border-l-0 border-red-300 rounded-r-sm px-3 py-1.5 text-sm">XP</div>
                                    </div>
                                    <div class="text-xs text-red-500 mt-1"><i class="fas fa-info-circle mr-1"></i> 已修改，将在C端特殊高亮。</div>
                                </div>
                            </div>
                        </div>

                        <div class="bg-blue-50/30 border border-blue-100 rounded p-6">
                            <h3 class="text-sm font-bold text-gray-800 mb-4">外显福利标签 <span class="text-xs text-gray-400 font-normal">（最多选2个）</span></h3>
                            <div class="flex gap-3">
                                <div class="px-3 py-1.5 border border-dfblue bg-blue-50 text-dfblue rounded-sm cursor-pointer text-sm font-medium relative">
                                    护卫军专项 <i class="fas fa-check absolute -top-1.5 -right-1.5 bg-white text-dfblue rounded-full text-[10px]"></i>
                                </div>
                                <div class="px-3 py-1.5 border border-gray-300 bg-white text-gray-600 rounded-sm cursor-pointer hover:border-dfblue text-sm">
                                    核心共创
                                </div>
                                <div class="px-3 py-1.5 border border-dfblue bg-blue-50 text-dfblue rounded-sm cursor-pointer text-sm font-medium relative">
                                    双倍XP池 <i class="fas fa-check absolute -top-1.5 -right-1.5 bg-white text-dfblue rounded-full text-[10px]"></i>
                                </div>
                                <div class="px-3 py-1.5 border border-dashed border-gray-300 bg-white text-gray-400 rounded-sm cursor-pointer hover:border-dfblue text-sm">
                                    + 新增标签
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- STEP 4: Submit -->
            <div id="step-4" class="step-content px-10 pb-10">
                <div class="max-w-6xl mx-auto">
                    <h2 class="text-base font-bold text-dfblue mb-6">审核设置</h2>
                    
                    <div class="grid grid-cols-3 gap-x-8 gap-y-6 max-w-5xl mb-8">
                        <div>
                            <label class="form-label required">审核方式</label>
                            <div class="flex items-center gap-6 mt-2">
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" class="w-4 h-4 text-dfblue border-gray-300 focus:ring-dfblue" checked>
                                    <span class="ml-2 text-sm text-gray-700">人工审核</span>
                                </label>
                                <label class="flex items-center cursor-not-allowed text-gray-400">
                                    <input type="radio" class="w-4 h-4 text-gray-200" disabled>
                                    <span class="ml-2 text-sm">系统审核</span>
                                </label>
                            </div>
                        </div>
                        <div>
                            <label class="form-label required">申诉周期</label>
                            <div class="flex items-center gap-2">
                                <input type="number" class="form-input w-full" value="7">
                                <span class="text-sm text-gray-600">天</span>
                            </div>
                        </div>
                        <div>
                            <label class="form-label">审核人员</label>
                            <input type="text" class="form-input" placeholder="请选择">
                        </div>
                    </div>

                    <div class="flex items-center gap-3 mb-8">
                        <span class="text-sm font-bold text-dfblue">AI审核</span>
                        <div class="relative inline-block w-10 align-middle select-none">
                            <input type="checkbox" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 border-dfblue" checked/>
                            <label class="toggle-label block overflow-hidden h-5 rounded-full bg-dfblue cursor-pointer"></label>
                        </div>
                        <span class="text-xs text-white bg-dfblue px-1.5 rounded-sm">开</span>
                    </div>

                    <div class="border-t border-gray-100 pt-8 mt-4 max-w-5xl">
                        <div class="flex items-center mb-6">
                            <span class="text-sm text-gray-800 w-24">作业审核规则</span>
                            <div class="flex items-center">
                                <span class="text-red-500 mr-1">*</span>
                                <span class="text-sm text-gray-700 mr-3">AI审核通过逻辑：</span>
                                <select class="form-input w-40 text-sm">
                                    <option>全部匹配成功</option>
                                </select>
                            </div>
                        </div>

                        <div class="space-y-4">
                            <div class="flex items-center gap-4">
                                <span class="text-sm text-gray-700 w-24"><span class="text-red-500 mr-1">*</span>审核规则一：</span>
                                <input type="text" class="form-input w-64" value="是否点赞(大拇指)">
                                <input type="text" class="form-input w-40 bg-gray-50 text-gray-400" placeholder="请输入变量内容" readonly>
                                <span class="text-sm text-gray-700 ml-4"><span class="text-red-500 mr-1">*</span>审核答案：</span>
                                <select class="form-input w-32 text-gray-400">
                                    <option>请选择</option>
                                </select>
                            </div>
                            <div class="flex items-center gap-4">
                                <span class="text-sm text-gray-700 w-24"><span class="text-red-500 mr-1">*</span>审核规则二：</span>
                                <input type="text" class="form-input w-64" value="是否喜欢 (爱心)">
                                <input type="text" class="form-input w-40 bg-gray-50 text-gray-400" placeholder="请输入变量内容" readonly>
                                <span class="text-sm text-gray-700 ml-4"><span class="text-red-500 mr-1">*</span>审核答案：</span>
                                <select class="form-input w-32 text-gray-400">
                                    <option>请选择</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Sticky Footer -->
        <div class="h-14 bg-white border-t border-gray-200 px-6 flex items-center justify-end gap-3 z-20 shrink-0">
            <button class="px-5 py-1.5 border border-gray-300 rounded-sm text-gray-700 hover:bg-gray-50 transition-colors text-sm">取消</button>
            <button class="px-5 py-1.5 bg-dfblue hover:bg-blue-600 text-white rounded-sm transition-colors text-sm">保存</button>
            <button id="btn-prev" class="hidden px-5 py-1.5 bg-dfblue hover:bg-blue-600 text-white rounded-sm transition-colors text-sm" onclick="prevStep()">上一步</button>
            <button id="btn-next" class="px-5 py-1.5 bg-dfblue hover:bg-blue-600 text-white rounded-sm transition-colors text-sm" onclick="nextStep()">下一步</button>
            <button id="btn-preview" class="hidden px-5 py-1.5 bg-dfblue hover:bg-blue-600 text-white rounded-sm transition-colors text-sm">保存并预览</button>
            <button id="btn-submit" class="hidden px-5 py-1.5 bg-dfblue hover:bg-blue-600 text-white rounded-sm transition-colors text-sm">保存并发布</button>
        </div>

    </main>

    <script>
        let currentStep = 1;
        const totalSteps = 4;

        function updateUI() {
            document.querySelectorAll('.step-content').forEach(el => el.classList.remove('active'));
            document.getElementById('step-' + currentStep).classList.add('active');

            for(let i=1; i<=totalSteps; i++) {
                const icon = document.getElementById('step-icon-' + i);
                const text = document.getElementById('step-text-' + i);
                
                if (i === currentStep) {
                    if(i===1) {
                        icon.className = "w-8 h-8 rounded-full border border-dfred text-dfred flex items-center justify-center font-bold text-sm bg-white";
                        icon.innerHTML = "<i class='fas fa-times text-xs'></i>";
                        text.className = "ml-2 font-medium text-dfred";
                    } else if (i===4) {
                        icon.className = "w-8 h-8 rounded-full border border-dfblue text-dfblue flex items-center justify-center font-bold text-sm bg-white";
                        icon.innerHTML = "<i class='fas fa-check text-xs'></i>";
                        text.className = "ml-2 font-medium text-dfblue";
                    } else {
                        icon.className = "w-8 h-8 rounded-full bg-dfblue text-white flex items-center justify-center font-bold text-sm";
                        icon.innerHTML = i;
                        text.className = "ml-2 font-medium text-dfblue";
                    }
                } else {
                    icon.className = "w-8 h-8 rounded-full border border-gray-300 text-gray-400 flex items-center justify-center font-medium text-sm bg-white";
                    icon.innerHTML = i;
                    text.className = "ml-2 font-medium text-gray-500";
                }
            }

            document.getElementById('btn-prev').classList.toggle('hidden', currentStep === 1 || currentStep === 2); // In screenshot, step 2 has no "上一步"
            
            if (currentStep === totalSteps) {
                document.getElementById('btn-next').classList.add('hidden');
                document.getElementById('btn-prev').classList.remove('hidden');
                document.getElementById('btn-preview').classList.remove('hidden');
                document.getElementById('btn-submit').classList.remove('hidden');
            } else {
                document.getElementById('btn-next').classList.remove('hidden');
                document.getElementById('btn-preview').classList.add('hidden');
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

print("Rewritten exactly to match screenshots!")
