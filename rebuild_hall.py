import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/C端_作业大厅.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

head_and_sidebar_match = re.search(r'(.*?<div class="ml-64 flex gap-[^>]+>)', content, flags=re.DOTALL)
head_and_sidebar = head_and_sidebar_match.group(1) if head_and_sidebar_match else ""

def generate_phone(title, show_unlocked=False, show_locked_scenario2=False, show_locked_scenario3=False, is_empty=False, is_pending=False):
    html = f'''
    <!-- Phone -->
    <div class="flex flex-col gap-3 shrink-0">
        <div class="text-[13px] font-bold text-gray-700 text-center flex items-center justify-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-500"></span> {title}
        </div>
        <div class="phone-frame flex flex-col bg-white w-[375px] h-[812px] shadow-xl rounded-[40px] border-[8px] border-gray-900 overflow-hidden relative">
'''
    if is_pending:
        # 待办作业列表
        html += '''
            <!-- Header (Fixed at top) -->
            <div class="bg-white pb-2 shadow-[0_2px_10px_rgba(0,0,0,0.02)] z-20 relative shrink-0">
                <div class="flex items-center justify-between px-4 pt-10 pb-1">
                    <i class="fas fa-chevron-left text-lg text-gray-800 cursor-pointer" onclick="window.history.back()"></i>
                    <div class="font-bold text-[16px] tracking-wide text-gray-900">待办作业列表</div>
                    <div class="flex items-center text-gray-800 bg-gray-100/80 rounded-full px-2 py-1 border border-gray-200 backdrop-blur-sm">
                        <i class="fas fa-ellipsis-h text-sm"></i>
                        <div class="w-px h-3 bg-gray-300 mx-2"></div>
                        <i class="far fa-circle text-sm"></i>
                    </div>
                </div>
            </div>
            
            <div class="flex-1 overflow-y-auto hide-scrollbar flex flex-col bg-gray-50 w-full p-4 relative pb-20">
                
                <h2 class="text-sm font-bold text-gray-900 mb-3 flex items-center"><div class="w-1 h-3 bg-dfred mr-2 rounded-full"></div>待领取作业</h2>
                
                <div class="bg-white rounded-xl p-4 shadow-sm border border-gray-100 mb-6">
                    <div class="flex items-center text-[11px] text-gray-500 mb-2 gap-2">
                        <span class="flex items-center gap-1.5 text-gray-600 font-medium shrink-0">
                            <div class="w-4 h-4 bg-orange-100 rounded-full flex items-center justify-center text-[10px] text-orange-500"><i class="fas fa-edit scale-75"></i></div>
                            原创作业
                        </span>
                        <div class="w-px h-2.5 bg-gray-200 mx-0.5"></div>
                        <span class="bg-blue-50 text-blue-500 px-1 py-0.5 rounded border border-blue-100 whitespace-nowrap">重点车型</span>
                    </div>
                    
                    <div class="flex gap-3 mb-2 mt-3">
                        <div class="w-[70px] h-[70px] bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl flex-shrink-0 flex items-center justify-center shadow-inner relative overflow-hidden">
                            <i class="fas fa-gem text-yellow-500 text-xl drop-shadow-md"></i>
                            <div class="absolute bottom-0 w-full bg-black/40 text-center py-0.5 text-white text-[9px]">深度测评</div>
                        </div>
                        <div class="flex-1 flex flex-col justify-between min-w-0">
                            <h3 class="font-bold text-gray-900 text-[13px] leading-snug line-clamp-2">【首发招募】全新奕派007深度试驾图文通稿评测任务</h3>
                            <div class="flex items-center text-orange-500 font-bold text-[12px] gap-2 mt-auto">
                                <span>💰 500 积分</span>
                                <span class="text-dfblue bg-blue-50 px-1 py-0.5 rounded border border-blue-100 text-[10px]"><i class="fas fa-arrow-up text-[9px] mr-0.5"></i>XP +100</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex items-center justify-between text-[10px] text-gray-400 pt-2 border-t border-gray-50 mt-2">
                        <div class="flex gap-3"><span>剩余 8天</span><span>剩余 221个</span></div>
                        <button class="bg-dfred text-white px-3 py-1.5 rounded-full text-[11px] font-bold shadow-sm active:scale-95 transition-transform" onclick="window.location.href='C端_作业详情.html'">查看详情</button>
                    </div>
                </div>

                <h2 class="text-sm font-bold text-gray-900 mb-3 flex items-center"><div class="w-1 h-3 bg-dfred mr-2 rounded-full"></div>待完成作业</h2>
                
                <div class="bg-white rounded-xl p-4 shadow-sm border border-gray-100 relative">
                    <div class="absolute -left-1 top-2 bg-orange-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-r shadow-sm z-10">待完成</div>
                    <div class="flex items-center text-[11px] text-gray-500 mb-2 gap-2 pl-2">
                        <span class="flex items-center gap-1.5 text-gray-600 font-medium shrink-0">
                            <div class="w-4 h-4 bg-orange-100 rounded-full flex items-center justify-center text-[10px] text-orange-500"><i class="fas fa-edit scale-75"></i></div>
                            原创作业
                        </span>
                        <div class="w-px h-2.5 bg-gray-200 mx-0.5"></div>
                        <span class="bg-[#FFF4EC] text-[#FA6400] px-1 py-0.5 rounded border border-[#FFE0C2] whitespace-nowrap">额外补贴</span>
                    </div>
                    
                    <div class="flex gap-3 mb-2 mt-3 pl-2">
                        <div class="w-[70px] h-[70px] bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl flex-shrink-0 flex items-center justify-center shadow-inner relative overflow-hidden">
                            <i class="fas fa-gem text-yellow-500 text-xl drop-shadow-md"></i>
                            <div class="absolute bottom-0 w-full bg-black/40 text-center py-0.5 text-white text-[9px]">深度测评</div>
                        </div>
                        <div class="flex-1 flex flex-col justify-between min-w-0">
                            <h3 class="font-bold text-gray-900 text-[13px] leading-snug line-clamp-2">【首发招募】全新奕派007深度试驾图文通稿评测任务</h3>
                            <div class="flex items-center text-gray-500 text-[10px] gap-2 mt-auto">
                                <span class="flex items-center"><i class="far fa-eye mr-1"></i>20</span>
                                <span class="flex items-center"><i class="far fa-comment-dots mr-1"></i>0</span>
                                <span class="flex items-center"><i class="far fa-thumbs-up mr-1"></i>20</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex items-center justify-between text-[10px] text-gray-400 pt-2 border-t border-gray-50 mt-2 pl-2">
                        <span>剩余 00天 23小时 12分</span>
                        <button class="bg-orange-500 text-white px-3 py-1.5 rounded-full text-[11px] font-bold shadow-sm active:scale-95 transition-transform flex items-center">提交作业信息 <i class="fas fa-chevron-right text-[9px] ml-1"></i></button>
                    </div>
                </div>
            </div>
            
            <div class="absolute bottom-0 left-0 w-full bg-white border-t border-gray-100 p-4 pb-8 shadow-[0_-4px_20px_rgba(0,0,0,0.03)] z-30">
                <button class="w-full bg-blue-500 text-white py-3 rounded-full text-[14px] font-bold shadow-md shadow-blue-500/20 active:scale-95 transition-transform">返回首页</button>
            </div>
'''
    else:
        # 常规作业大厅
        html += '''
        <!-- Header (Fixed at top) -->
        <div class="bg-white pb-2 shadow-[0_2px_10px_rgba(0,0,0,0.02)] z-20 relative shrink-0">
            <!-- Top bar -->
            <div class="flex items-center justify-between px-4 pt-10 pb-1">
                <div class="flex space-x-1">
                    <div class="w-2 h-2 rounded-full border border-gray-400"></div><div class="w-2 h-2 rounded-full border border-gray-400"></div><div class="w-2 h-2 rounded-full border border-gray-400"></div>
                </div>
                <div class="flex items-center text-gray-500 bg-gray-100 rounded-full px-3 py-1 text-xs">
                    <i class="fas fa-link mr-1"></i> 作业中心 <i class="fas fa-times ml-2"></i>
                </div>
                <i class="fas fa-ellipsis-h text-gray-800"></i>
            </div>
        </div>

        <!-- Scrollable Page Content -->
        <div class="flex-1 overflow-y-auto hide-scrollbar flex flex-col bg-gray-50/50 w-full relative pb-20">
            
            <!-- White Top Section -->
            <div class="bg-white pt-2">
                <!-- Banner Image -->
                <div class="px-4 mb-2">
                    <div class="w-full h-24 rounded-xl bg-gradient-to-r from-blue-700 to-blue-400 flex items-center justify-center text-white text-3xl font-bold italic overflow-hidden relative shadow-sm border border-blue-200">
                        <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"></div>
                        <span class="z-10 tracking-widest text-shadow drop-shadow-md">金点子</span>
                        <i class="fas fa-lightbulb text-yellow-300 text-4xl absolute right-12 top-4 z-10 drop-shadow-lg transform rotate-12"></i>
                        <div class="absolute bottom-0 w-full bg-blue-900/50 py-0.5 text-center text-[9px] tracking-widest text-blue-100">智慧的碰撞 积分的积累</div>
                    </div>
                </div>

                <!-- 3 Action Buttons -->
                <div class="px-4 flex justify-between gap-3 mb-2">
                    <div class="flex-1 bg-[#F0F4FF] border border-[#E0E7FF] rounded-xl py-2 flex items-center justify-center text-xs font-bold text-gray-700 shadow-sm cursor-pointer">
                        <i class="fas fa-user-plus text-blue-500 mr-1.5 text-base"></i> 添加账号
                    </div>
                    <div class="flex-1 bg-[#FFF5F0] border border-[#FFEDD5] rounded-xl py-2 flex items-center justify-center text-xs font-bold text-gray-700 shadow-sm cursor-pointer">
                        <i class="fas fa-trophy text-orange-400 mr-1.5 text-base"></i> 排行榜
                    </div>
                    <div class="flex-1 bg-[#FFF0F2] border border-[#FFE4E6] rounded-xl py-2 flex items-center justify-center text-xs font-bold text-gray-700 shadow-sm cursor-pointer">
                        <i class="fas fa-edit text-dfred mr-1.5 text-base"></i> 作业申请
                    </div>
                </div>

                <!-- Notification -->
                <div class="px-4 mb-2">
                    <div class="bg-[#FFF5ED] text-orange-500 text-[11px] py-1.5 px-3 rounded flex items-center overflow-hidden font-medium border border-orange-100">
                        <i class="fas fa-bell mr-2 flex-shrink-0"></i>
                        <span class="truncate">最新通知: (加热-点赞) 全新猛士M817预热...</span>
                    </div>
                </div>
                
                <!-- Tabs -->
                <div class="px-4 flex items-center justify-between mb-1 mt-2">
                    <div class="flex items-center text-lg font-bold text-gray-800 tracking-wide">
                        发布作业
                    </div>
                    <div class="text-gray-500 text-[12px] flex items-center cursor-pointer">
                        已领取记录 <i class="fas fa-chevron-right text-[10px] ml-1"></i>
                    </div>
                </div>
                
                <div class="px-4 flex overflow-x-auto hide-scrollbar gap-2 mb-2 pb-1">
                    <div class="bg-red-50 text-dfred font-bold text-[13px] px-4 py-1.5 rounded-full whitespace-nowrap">全部作业</div>
                    <div class="bg-gray-100 text-gray-600 text-[13px] px-4 py-1.5 rounded-full whitespace-nowrap">互动作业</div>
                    <div class="bg-gray-100 text-gray-600 text-[13px] px-4 py-1.5 rounded-full whitespace-nowrap">转发作业</div>
                    <div class="bg-gray-100 text-gray-600 text-[13px] px-4 py-1.5 rounded-full whitespace-nowrap">原创作业</div>
                </div>
                
                <!-- Filter bar -->
                <div class="px-4 flex items-center justify-between py-2 border-t border-gray-100">
                    <div class="text-[12px] text-gray-500">共 124 个作业</div>
                    <div class="flex items-center text-[12px] text-gray-700 font-bold">
                        <!-- Switch toggle -->
                        <div class="w-8 h-4 bg-gray-200 rounded-full mr-2 relative cursor-pointer">
                            <div class="w-3.5 h-3.5 bg-white rounded-full shadow-sm absolute left-0.5 top-0.5"></div>
                        </div>
                        仅看我可做
                    </div>
                </div>
            </div>
            
            <div class="p-4 flex flex-col gap-4">
'''
        
        unlocked_task = '''
                <!-- Unlocked Task (Normal) -->
                <div class="bg-white rounded-2xl p-4 shadow-sm relative overflow-hidden border border-gray-100">
                    <div class="flex items-center text-[12px] text-gray-500 mb-3 gap-2">
                        <span class="flex items-center gap-1.5 text-gray-600 font-medium shrink-0">
                            <div class="w-4 h-4 bg-orange-100 rounded-full flex items-center justify-center text-[10px] text-orange-500"><i class="fas fa-edit scale-75"></i></div>
                            原创作业
                        </span>
                        <div class="w-px h-3 bg-gray-200 mx-0.5"></div>
                        <div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar">
                            <span class="bg-blue-50 text-blue-500 text-[9px] px-1 py-0.5 rounded border border-blue-100 whitespace-nowrap">护卫军专项</span>
                            <span class="bg-[#FFF4EC] text-[#FA6400] text-[9px] px-1 py-0.5 rounded border border-[#FFE0C2] whitespace-nowrap">双倍XP池</span>
                        </div>
                    </div>
                    
                    <div class="flex gap-3 mb-2">
                        <div class="w-[80px] h-[80px] bg-[#FDF8F5] rounded-xl flex-shrink-0 flex flex-col items-center justify-center text-gray-800 font-bold text-xs p-1 shadow-[0_0_0_0.5px_#F3E6DF] relative overflow-hidden">
                            <span class="text-[#D33024] text-[13px] leading-snug">建党节</span>
                            <span class="text-[7px] text-gray-500 font-normal scale-90 whitespace-nowrap">2021.07.01-2026.07.01</span>
                            <span class="text-[9px] mt-0.5 whitespace-nowrap">初心话给党旗听</span>
                        </div>
                        <div class="flex-1 flex flex-col justify-between min-w-0 py-0.5">
                            <h3 class="font-bold text-gray-900 text-[14px] leading-snug line-clamp-2">七一原创作业：初心话给党旗听</h3>
                            
                            <div class="flex items-center justify-between mt-auto pt-1.5 gap-1 flex-wrap">
                                <div class="flex flex-wrap items-center text-orange-500 font-bold text-[12px] gap-1.5">
                                    <span>💰 20~550 积分</span>
                                    <span class="text-dfblue bg-blue-50 px-1 py-0.5 rounded border border-blue-100 text-[10px]"><i class="fas fa-arrow-up text-[9px] mr-0.5"></i>XP +15</span>
                                </div>
                                <button class="bg-dfred text-white px-2.5 py-1 rounded-full text-[11px] font-bold shadow-sm active:scale-95 transition-transform shrink-0 whitespace-nowrap ml-auto" onclick="window.location.href='C端_作业详情.html'">查看详情</button>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center text-[11px] text-gray-500 gap-3 pt-3 mt-1 border-t border-gray-50">
                        <span>剩余 8天</span>
                        <span>剩余 221个</span>
                        <div class="flex-1 bg-[#F5F5F5] rounded-full h-1.5">
                            <div class="bg-gradient-to-r from-[#FF7A45] to-[#FA541C] h-1.5 rounded-full relative" style="width: 89%">
                                <div class="absolute right-0 top-1/2 -translate-y-1/2 w-2 h-2 bg-white rounded-full border border-orange-500 shadow-sm translate-x-1"></div>
                            </div>
                        </div>
                        <span class="text-gray-400">89%</span>
                    </div>
                </div>
'''
        locked_scenario2 = '''
                <!-- Locked Task (Scenario 2: Has other tasks available, jumps to pending list) -->
                <div class="bg-white rounded-2xl p-4 shadow-sm relative overflow-hidden border border-gray-100 opacity-90">
                    <div class="absolute top-0 right-0 bg-gradient-to-r from-yellow-100 to-yellow-50 text-yellow-700 text-[10px] font-bold px-2 py-1 rounded-bl-lg border-b border-l border-yellow-200 z-10 shadow-sm">
                        <i class="fas fa-crown text-yellow-500"></i> 尖兵/大师专属
                    </div>
                    
                    <div class="flex items-center text-[12px] text-gray-500 mb-3 gap-2">
                        <span class="flex items-center gap-1.5 text-gray-600 font-medium shrink-0">
                            <div class="w-4 h-4 bg-orange-100 rounded-full flex items-center justify-center text-[10px] text-orange-500"><i class="fas fa-edit scale-75"></i></div>
                            原创作业
                        </span>
                        <div class="w-px h-3 bg-gray-200 mx-0.5"></div>
                        <div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar">
                            <span class="bg-blue-50 text-blue-500 text-[9px] px-1 py-0.5 rounded border border-blue-100 whitespace-nowrap">重点车型</span>
                            <span class="bg-[#FFF4EC] text-[#FA6400] text-[9px] px-1 py-0.5 rounded border border-[#FFE0C2] whitespace-nowrap">额外补贴</span>
                        </div>
                    </div>
                    
                    <div class="flex gap-3 mb-2">
                        <div class="w-[80px] h-[80px] bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl flex-shrink-0 flex items-center justify-center shadow-inner relative overflow-hidden opacity-80">
                            <i class="fas fa-gem text-yellow-500 text-2xl drop-shadow-md"></i>
                            <div class="absolute bottom-0 w-full bg-black/40 text-center py-0.5 text-white text-[10px]">深度测评</div>
                        </div>
                        <div class="flex-1 flex flex-col justify-between opacity-60 min-w-0 py-0.5">
                            <h3 class="font-bold text-gray-900 text-[14px] leading-snug line-clamp-2">【首发招募】全新奕派007深度试驾图文通稿评测任务</h3>
                            <div class="flex items-center justify-between mt-auto pt-1.5 gap-2">
                                <div class="flex items-center text-orange-500 font-bold text-[13px] gap-2 shrink-0">
                                    <span>💰 500 积分</span>
                                    <span class="text-dfblue bg-blue-50 px-1.5 py-0.5 rounded border border-blue-100 text-[11px]"><i class="fas fa-arrow-up text-[10px] mr-0.5"></i>XP +100</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-4 bg-[#F8F9FA] rounded-lg p-3 border border-gray-200 relative">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[11px] text-gray-600 font-bold"><i class="fas fa-lock mr-1 text-gray-400"></i> 解锁需 2500 XP</span>
                            <span class="text-[10px] text-gray-500">进度: 1420 XP</span>
                        </div>
                        <div class="w-full bg-gray-200 rounded-full h-1.5 mb-3">
                            <div class="gradient-gold h-1.5 rounded-full" style="width: 56%"></div>
                        </div>
                        <button class="w-full bg-gradient-to-r from-[#FF8C3A] to-[#FF6B1A] text-white py-2 rounded-full text-[13px] font-bold shadow-sm flex items-center justify-center active:scale-95 transition-transform" onclick="alert('跳转至：【待办作业列表】')">
                            差 1080 XP，去做任务赚 XP <i class="fas fa-arrow-right ml-1 opacity-70"></i>
                        </button>
                    </div>
                </div>
'''
        locked_scenario3 = '''
                <!-- Locked Task (Scenario 3: No other tasks available, jumps to growth center) -->
                <div class="bg-white rounded-2xl p-4 shadow-sm relative overflow-hidden border border-gray-100 opacity-90">
                    <div class="absolute top-0 right-0 bg-gradient-to-r from-yellow-100 to-yellow-50 text-yellow-700 text-[10px] font-bold px-2 py-1 rounded-bl-lg border-b border-l border-yellow-200 z-10 shadow-sm">
                        <i class="fas fa-crown text-yellow-500"></i> 尖兵/大师专属
                    </div>
                    
                    <div class="flex items-center text-[12px] text-gray-500 mb-3 gap-2">
                        <span class="flex items-center gap-1.5 text-gray-600 font-medium shrink-0">
                            <div class="w-4 h-4 bg-orange-100 rounded-full flex items-center justify-center text-[10px] text-orange-500"><i class="fas fa-edit scale-75"></i></div>
                            原创作业
                        </span>
                        <div class="w-px h-3 bg-gray-200 mx-0.5"></div>
                        <div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar">
                            <span class="bg-blue-50 text-blue-500 text-[9px] px-1 py-0.5 rounded border border-blue-100 whitespace-nowrap">重点车型</span>
                            <span class="bg-[#FFF4EC] text-[#FA6400] text-[9px] px-1 py-0.5 rounded border border-[#FFE0C2] whitespace-nowrap">额外补贴</span>
                        </div>
                    </div>
                    
                    <div class="flex gap-3 mb-2">
                        <div class="w-[80px] h-[80px] bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl flex-shrink-0 flex items-center justify-center shadow-inner relative overflow-hidden opacity-80">
                            <i class="fas fa-gem text-yellow-500 text-2xl drop-shadow-md"></i>
                            <div class="absolute bottom-0 w-full bg-black/40 text-center py-0.5 text-white text-[10px]">深度测评</div>
                        </div>
                        <div class="flex-1 flex flex-col justify-between opacity-60 min-w-0 py-0.5">
                            <h3 class="font-bold text-gray-900 text-[14px] leading-snug line-clamp-2">【首发招募】全新奕派007深度试驾图文通稿评测任务</h3>
                            <div class="flex items-center justify-between mt-auto pt-1.5 gap-2">
                                <div class="flex items-center text-orange-500 font-bold text-[13px] gap-2 shrink-0">
                                    <span>💰 500 积分</span>
                                    <span class="text-dfblue bg-blue-50 px-1.5 py-0.5 rounded border border-blue-100 text-[11px]"><i class="fas fa-arrow-up text-[10px] mr-0.5"></i>XP +100</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-4 bg-[#F8F9FA] rounded-lg p-3 border border-gray-200 relative">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[11px] text-gray-600 font-bold"><i class="fas fa-lock mr-1 text-gray-400"></i> 解锁需 2500 XP</span>
                            <span class="text-[10px] text-gray-500">进度: 1420 XP</span>
                        </div>
                        <div class="w-full bg-gray-200 rounded-full h-1.5 mb-3">
                            <div class="gradient-gold h-1.5 rounded-full" style="width: 56%"></div>
                        </div>
                        <button class="w-full bg-gradient-to-r from-[#6366F1] to-[#818CF8] text-white py-2 rounded-full text-[13px] font-bold shadow-sm flex items-center justify-center active:scale-95 transition-transform" onclick="window.location.href='C端_成长中心大盘.html'">
                            差 1080 XP，查看成长攻略 <i class="fas fa-arrow-right ml-1 opacity-70"></i>
                        </button>
                    </div>
                </div>
'''

        if show_unlocked: html += unlocked_task
        if show_locked_scenario2: html += locked_scenario2
        if show_locked_scenario3: html += locked_scenario3
        
        html += '''
            </div>
            
            <!-- Bottom Navigation -->
            <div class="absolute bottom-0 left-0 w-full bg-white border-t border-gray-100 flex justify-between px-8 py-2 z-30">
                <div class="flex flex-col items-center justify-center text-dfred">
                    <i class="fas fa-home text-xl mb-1"></i>
                    <span class="text-[10px] font-bold">首页</span>
                </div>
                <div class="flex flex-col items-center justify-center text-gray-400">
                    <i class="fas fa-graduation-cap text-xl mb-1"></i>
                    <span class="text-[10px]">学院</span>
                </div>
                <div class="flex flex-col items-center justify-center text-gray-400">
                    <i class="fas fa-user text-xl mb-1"></i>
                    <span class="text-[10px]">我的</span>
                </div>
            </div>
        </div>
'''
    html += '''
        </div> <!-- Close .phone-frame -->
    </div> <!-- Close .flex-col shrink-0 wrapper -->
'''
    return html

# Make sure we don't carry over any old flex div issues from previous runs
head_and_sidebar_match = re.search(r'(.*?<div class="ml-64 flex gap-[^>]+>)', content, flags=re.DOTALL)
if head_and_sidebar_match:
    head_and_sidebar = head_and_sidebar_match.group(1)
else:
    head_and_sidebar = ""

# Since we might have already replaced it, let's just make sure it's correct
# Find everything up to the </div> that closes the sidebar, or just use regex to grab the sidebar:
head_and_sidebar = re.sub(r'<div class="ml-64 flex gap-12 items-start.*', '', content, flags=re.DOTALL)


new_content = head_and_sidebar + '''<div class="ml-64 flex gap-12 items-start w-[calc(100%-256px)] pl-10 pt-4 overflow-x-auto pb-10">
'''

# Phone 1
new_content += generate_phone("场景1：符合资格，只有可做作业", show_unlocked=True)
# Phone 2
new_content += generate_phone("场景2：当前有可做作业", show_unlocked=True, show_locked_scenario2=True)
# Phone 3
new_content += generate_phone("场景3：当前无可做作业", show_locked_scenario3=True)
# Phone 4
new_content += generate_phone("场景2点击跳转目标：待办作业列表", is_pending=True)

# Add sidebar
new_content += '''
    <!-- 右侧批注区 -->
    <div class="w-[350px] shrink-0 pt-8">
        <div class="annotation-block mb-6">
            <div class="annotation-title">【外显福利标签显示】</div>
            <div class="annotation-text">
                <p>与 B端 "新建作业" 中配置的【外显福利标签】字段联动。该字段在此处配置了标签（如 护卫军专项、双倍XP池），前端的作业卡片标题下方就会外显对应的高亮标签。旨在通过类似电商“百亿补贴”的特殊标签提升领取作业率。</p>
            </div>
        </div>

        <div class="annotation-block mb-6">
            <div class="annotation-title">【成长标签 (准入专属) 显示】</div>
            <div class="annotation-text">
                <p>仅当推送方式 = 阶梯体系推送时，才会出现此标签，数据来源于 B端 的“成长标签”字段。</p>
                <p class="mt-2">排版规则：准入专属标签（如：尖兵/大师专属）被绝对定位在卡片的右上角边缘，不占内容流空间；外显福利标签位于卡片内容第一行左侧，与"原创作业"图标对齐。两者在布局上完全解耦，不管怎么叠加都不会出现重叠挤压。</p>
            </div>
        </div>

        <div class="annotation-block">
            <div class="annotation-title">【逻辑说明】不符合资格作业的 CTA 按钮判断规则</div>
            <div class="annotation-text">
                <p class="mb-3 text-gray-600">当用户 XP 不足以领取某个带门槛的作业时，底部 CTA 按钮需要系统动态判断文案和跳转目标：</p>
                
                <p><b>场景1: 符合资格，只有可做作业</b></p>
                <p class="mb-3">全部作业均达到门槛，用户可自由领取。</p>

                <p><b>场景2: 当前有可做作业</b></p>
                <ul class="list-disc pl-4 mb-3">
                    <li><b>判断条件</b>：作业列表中存在至少 1 个该用户可领取（无门槛 或 已达到门槛）且状态为"可领取"或"领取待提交"的作业</li>
                    <li><b>按钮文案</b>：「差 XX XP，去做任务赚 XP →」</li>
                    <li><b>按钮颜色</b>：橙色渐变（醒目引导）</li>
                    <li><b>点击跳转</b>：跳转至【待办作业列表】，引导用户直接去完成目前可做的任务赚取XP</li>
                </ul>

                <p><b>场景3: 当前无可做作业</b></p>
                <ul class="list-disc pl-4 mb-3">
                    <li><b>判断条件</b>：作业列表中不存在任何该用户当前可领取的作业（全部已领完、已过期、或门槛不达标）</li>
                    <li><b>按钮文案</b>：「差 XX XP，查看成长攻略 →」</li>
                    <li><b>按钮颜色</b>：紫色渐变（区分引导方向）</li>
                    <li><b>点击跳转</b>：跳转至【成长中心大盘】页面，引导用户查看升级路径与XP获取途径</li>
                </ul>

                <p class="mt-2 text-red-500 font-bold">兜底场景：若接口异常无法判断，默认展示场景2文案。</p>
            </div>
        </div>
        
        <div class="annotation-block mt-6">
            <div class="annotation-title">【页面跳转串联】</div>
            <div class="annotation-text">
                <p>此处为做任务的落地页。点击顶部的关闭按钮，或者底部的【我的】，可回到个人中心页面。</p>
            </div>
        </div>
    </div>
</div>
</body>
</html>
'''

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
