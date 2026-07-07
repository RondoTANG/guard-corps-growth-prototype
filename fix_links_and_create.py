import os
import re

config_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"

with open(config_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix 文章编辑 back to #
content = content.replace(
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_内容管理_文章发布页.html">文章编辑</a>',
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="#">文章编辑</a>'
)

# Update 文章管理 to point to new page
content = content.replace(
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_内容管理_文章发布页.html">文章管理</a>',
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_系统设置_文章管理页.html">文章管理</a>'
)

# If the old replacement didn't match, try matching href="#" just in case
content = content.replace(
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="#">文章管理</a>',
    '<a class="px-9 py-2.5 hover:text-white transition-colors" href="B端_系统设置_文章管理页.html">文章管理</a>'
)

with open(config_path, "w", encoding="utf-8") as f:
    f.write(content)

new_page_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"

new_html = """<!DOCTYPE html>
<html lang="zh-CN" style="font-size: 14px;">
<head>
    <meta charset="utf-8"/>
    <title>文章管理 - 护卫军管理后台</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet"/>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        dfred: '#1890ff', /* Changed to typical blue for operations, but keep original for XP red later */
                        dfblue: '#1890ff'
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
    <div class="flex-1 overflow-y-auto style-scrollbar" style="scrollbar-width: thin;">
        <nav class="flex flex-col pb-6 pt-2 space-y-1">
            <!-- 平台管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">平台管理</span>
                    <i class="fas fa-chevron-down text-xs text-gray-400"></i>
                </div>
            </div>
            <!-- 积分管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">积分管理</span>
                    <i class="fas fa-chevron-down text-xs text-gray-400"></i>
                </div>
            </div>
            <!-- 商城后台管理 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">商城后台管理</span>
                    <i class="fas fa-chevron-down text-xs text-gray-400"></i>
                </div>
            </div>
            <!-- 护卫军作业管理 (Expanded) -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-[#1890ff]">护卫军作业管理</span>
                    <i class="fas fa-chevron-up text-xs text-[#1890ff]"></i>
                </div>
                <div class="flex flex-col">
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">作业管理</a>
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">审核管理</a>
                    <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">用户管理</a>
                    <!-- 系统设置 under 护卫军作业管理 -->
                    <div class="flex items-center justify-between px-9 py-2.5 cursor-pointer hover:text-white transition-colors">
                        <span class="text-[#1890ff]">系统设置</span>
                        <i class="fas fa-chevron-up text-xs text-[#1890ff]"></i>
                    </div>
                    <div class="flex flex-col ml-4">
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">系统日志</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">登录日志</a>
                        <a href="B端_等级规则与XP配置页.html" class="px-9 py-2.5 hover:text-white transition-colors">成长规则配置</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">额外奖励设置</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">积分充值管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">标签管理(统计)</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">字典管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">消息推送</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">白名单作业管理</a>
                        <a href="#" class="px-9 py-3 bg-[#e6f7ff] text-[#1890ff] font-bold border-r-4 border-[#1890ff] block">文章管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">审核话术管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">积分发放记录</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">服务号消息额度管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">作业用途分类管理</a>
                        <a href="#" class="px-9 py-2.5 hover:text-white transition-colors">全量黑名单管理</a>
                    </div>
                </div>
            </div>
            <!-- 统计分析 -->
            <div class="menu-group">
                <div class="flex items-center justify-between px-5 py-3 cursor-pointer hover:text-white transition-colors">
                    <span class="font-bold text-gray-200">统计分析</span>
                    <i class="fas fa-chevron-down text-xs text-gray-400"></i>
                </div>
            </div>
        </nav>
    </div>
</aside>

<!-- Right Content Area -->
<div class="flex-1 flex flex-col min-w-0 overflow-hidden bg-gray-50 relative">
    
    <!-- Top Header -->
    <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0 z-10">
        <div class="flex items-center text-sm">
            <span class="text-gray-500">系统设置</span>
            <span class="mx-2 text-gray-400">/</span>
            <span class="text-gray-900 font-bold">文章管理</span>
        </div>
        <div class="flex items-center space-x-4">
            <div class="flex items-center text-sm text-gray-600">
                <i class="far fa-user text-lg mr-2"></i>
                <span>浩哥</span>
            </div>
        </div>
    </header>

    <!-- LIST VIEW -->
    <main id="list-view" class="flex-1 overflow-y-auto p-6 block">
        <div class="bg-white p-6 rounded shadow-sm border border-gray-200">
            <!-- Search Form -->
            <div class="flex flex-wrap items-center gap-4 mb-6">
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">文章ID：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请输入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">文章标题：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请输入内容">
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-12 text-right">栏目：</label>
                    <select class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue bg-white text-gray-400">
                        <option>请选择栏目</option>
                    </select>
                </div>
                <div class="flex items-center">
                    <label class="text-sm text-gray-600 mr-2 w-16 text-right">创建人：</label>
                    <input type="text" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue" placeholder="请输入内容">
                </div>
            </div>
            
            <div class="flex flex-wrap items-center gap-4 mb-6 justify-between">
                <div class="flex items-center gap-4">
                    <div class="flex items-center">
                        <label class="text-sm text-gray-600 mr-2 w-16 text-right">状态：</label>
                        <select class="border border-gray-300 rounded px-3 py-1.5 text-sm w-48 outline-none focus:border-dfblue bg-white text-gray-400">
                            <option>请选择</option>
                        </select>
                    </div>
                    <div class="flex items-center">
                        <label class="text-sm text-gray-600 mr-2 w-16 text-right">发布时间：</label>
                        <div class="flex items-center border border-gray-300 rounded px-3 py-1.5 w-64 bg-white">
                            <input type="text" class="text-sm w-full outline-none text-gray-400" placeholder="开始日期">
                            <span class="text-gray-300 mx-2">→</span>
                            <input type="text" class="text-sm w-full outline-none text-gray-400" placeholder="结束日期">
                            <i class="far fa-calendar-alt text-gray-400 ml-2"></i>
                        </div>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="showFormView()" class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600">新增文章</button>
                    <button class="px-4 py-1.5 border border-gray-300 text-gray-600 rounded text-sm hover:border-[#1890ff] hover:text-[#1890ff]">重置</button>
                    <button class="px-4 py-1.5 bg-[#1890ff] text-white rounded text-sm hover:bg-blue-600">搜索</button>
                </div>
            </div>

            <!-- Table -->
            <div class="overflow-x-auto">
                <table class="min-w-full border-t border-gray-100">
                    <thead class="bg-gray-50 text-gray-500 text-sm">
                        <tr>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">ID</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">文章标题</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">归属分类</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">创建人</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">创建时间</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">状态</th>
                            <th class="py-3 px-4 text-left font-normal border-b border-gray-100">操作</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm text-gray-700 divide-y divide-gray-100">
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">1272</td>
                            <td class="py-3 px-4">采集类作业指引</td>
                            <td class="py-3 px-4">备选</td>
                            <td class="py-3 px-4">梁吴皓</td>
                            <td class="py-3 px-4">2026-03-30 18:53:16</td>
                            <td class="py-3 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-3 px-4 space-x-2 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline text-red-500">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">2947</td>
                            <td class="py-3 px-4">第五十九期点评：黄阳运</td>
                            <td class="py-3 px-4">王牌护卫军</td>
                            <td class="py-3 px-4">梁吴皓</td>
                            <td class="py-3 px-4">2026-07-03 10:51:52</td>
                            <td class="py-3 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-3 px-4 space-x-2 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline text-red-500">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors">
                            <td class="py-3 px-4">2946</td>
                            <td class="py-3 px-4">金点子积分榜+反馈精选（2026年6月）</td>
                            <td class="py-3 px-4">金点子排名</td>
                            <td class="py-3 px-4">梁吴皓</td>
                            <td class="py-3 px-4">2026-07-02 14:59:45</td>
                            <td class="py-3 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-3 px-4 space-x-2 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline text-red-500">删除</a>
                            </td>
                        </tr>
                        <tr class="hover:bg-blue-50 transition-colors bg-gray-50">
                            <td class="py-3 px-4">2886</td>
                            <td class="py-3 px-4">第五十八期点评：王五</td>
                            <td class="py-3 px-4">王牌护卫军</td>
                            <td class="py-3 px-4">梁吴皓</td>
                            <td class="py-3 px-4">2026-06-26 17:39:30</td>
                            <td class="py-3 px-4"><span class="flex items-center"><span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>启用</span></td>
                            <td class="py-3 px-4 space-x-2 text-[#1890ff]">
                                <a href="#" class="hover:underline">复制链接</a>
                                <a href="#" class="hover:underline">编辑</a>
                                <a href="#" class="hover:underline text-red-500">删除</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <!-- Pagination -->
            <div class="flex items-center justify-end mt-6 text-sm text-gray-500">
                <span>共 215 条数据</span>
                <div class="flex items-center ml-4 space-x-1">
                    <button class="px-2 py-1 border border-gray-300 bg-white rounded text-gray-400">&lt;</button>
                    <button class="px-2.5 py-1 bg-[#1890ff] text-white rounded">1</button>
                    <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">2</button>
                    <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">3</button>
                    <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">4</button>
                    <span class="px-1">...</span>
                    <button class="px-2.5 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">22</button>
                    <button class="px-2 py-1 border border-gray-300 bg-white rounded hover:text-[#1890ff] hover:border-[#1890ff]">&gt;</button>
                </div>
                <select class="border border-gray-300 rounded ml-4 px-2 py-1 outline-none">
                    <option>10 条/页</option>
                </select>
                <div class="flex items-center ml-4">
                    <span>前往</span>
                    <input type="text" class="w-10 border border-gray-300 rounded mx-2 py-1 text-center outline-none">
                    <span>页</span>
                </div>
            </div>
        </div>
    </main>

    <!-- FORM VIEW (Hidden by default) -->
    <main id="form-view" class="flex-1 overflow-y-auto p-6 hidden">
        <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
            <div class="px-6 py-4 border-b border-gray-200 bg-gray-50 flex items-center justify-between">
                <div class="flex items-center">
                    <button onclick="showListView()" class="mr-3 text-gray-500 hover:text-[#1890ff] transition-colors group">
                        <i class="fas fa-arrow-left"></i>
                        <span class="ml-1 text-xs opacity-0 group-hover:opacity-100 transition-opacity">返回列表</span>
                    </button>
                    <h2 class="text-lg font-bold text-gray-800">编辑文章内容</h2>
                </div>
            </div>
            
            <div class="p-8 space-y-6">
                <!-- Title -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">文章标题 <span class="text-red-500">*</span></label>
                    <input type="text" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-3 border outline-none focus:border-[#1890ff] focus:ring-1 focus:ring-[#1890ff]" placeholder="请输入文章标题，最多 50 个字符">
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
                                <input id="ace-guard-checkbox" type="checkbox" class="w-4 h-4 text-[#1890ff] border-gray-300 rounded focus:ring-[#1890ff] mt-0.5">
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
                <button onclick="showListView()" class="px-5 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                    取消/返回
                </button>
                <button class="px-5 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                    存为草稿
                </button>
                <button onclick="handlePublish()" class="px-5 py-2 bg-[#1890ff] text-white rounded-md text-sm font-medium hover:bg-blue-600 transition-colors shadow-sm flex items-center">
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
                    💡 <strong>系统提示：</strong> 根据 <a href="B端_等级规则与XP配置页.html" class="text-blue-600 underline">《成长规则配置》</a> 设定，该操作将自动为创作者（护卫军-李师傅）发放 <strong class="text-red-600 text-lg mx-1">100</strong> XP 奖励。
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
            <button onclick="confirmPublish()" class="px-4 py-2 bg-red-600 text-white rounded text-sm font-medium hover:bg-red-700 transition-colors">
                确认发布并奖励 XP
            </button>
        </div>
    </div>
</div>

<script>
    function showFormView() {
        document.getElementById('list-view').classList.add('hidden');
        document.getElementById('list-view').classList.remove('block');
        
        document.getElementById('form-view').classList.remove('hidden');
        document.getElementById('form-view').classList.add('block');
    }

    function showListView() {
        document.getElementById('form-view').classList.add('hidden');
        document.getElementById('form-view').classList.remove('block');
        
        document.getElementById('list-view').classList.remove('hidden');
        document.getElementById('list-view').classList.add('block');
    }

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
            showListView();
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
            showListView();
        }, 300);
    }
</script>

</body>
</html>
"""

with open(new_page_path, "w", encoding="utf-8") as f:
    f.write(new_html)

# Clean up the previous unwanted file if it exists
old_page_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_内容管理_文章发布页.html"
if os.path.exists(old_page_path):
    os.remove(old_page_path)

print(f"Created {new_page_path} based on screenshot.")
