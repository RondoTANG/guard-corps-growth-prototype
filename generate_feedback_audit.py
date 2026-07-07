html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>反馈单核列表 - 护卫军管理后台</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet"/>
<script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        dfblue: '#1890ff',
                        dfred: '#E60012',
                    }
                }
            }
        }
</script>
<style>
    .modal-overlay {
        background-color: rgba(0, 0, 0, 0.5);
    }
</style>
</head>
<body class="bg-gray-100 h-screen flex overflow-hidden font-sans text-sm text-gray-800">
<!-- Main Content -->
<div class="shrink-0 flex h-full" id="b-sidebar-container"></div>
<script src="b_sidebar.js"></script>
<script>initBSidebar('反馈单核列表');</script>

<main class="flex-1 flex flex-col overflow-hidden bg-gray-50">
<!-- Header -->
<header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0">
<div class="flex items-center text-sm text-gray-500">
<a class="hover:text-gray-900" href="#">审核管理</a>
<i class="fas fa-chevron-right text-[10px] mx-2"></i>
<span class="text-gray-900 font-medium">反馈单核列表</span>
</div>
<div class="flex items-center">
<div class="w-8 h-8 rounded-full bg-dfred text-white flex items-center justify-center font-bold text-sm">
    Admin
</div>
</div>
</header>

<!-- Content Area -->
<div class="flex-1 overflow-y-auto p-6">

<!-- Filter Tags -->
<div class="flex gap-2 mb-4">
    <div class="bg-gray-100 px-3 py-1 text-xs text-gray-600 rounded flex items-center cursor-pointer hover:bg-gray-200">
        用户积分明细 <i class="fas fa-times ml-2 text-gray-400"></i>
    </div>
    <div class="bg-gray-100 px-3 py-1 text-xs text-gray-600 rounded flex items-center cursor-pointer hover:bg-gray-200">
        积分下发审核 <i class="fas fa-times ml-2 text-gray-400"></i>
    </div>
</div>

<!-- Filter Bar -->
<div class="bg-white p-6 rounded-md shadow-sm border border-gray-200 mb-4">
    <div class="grid grid-cols-4 gap-6">
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-16 text-right">反馈类型:</label>
            <select class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none bg-white text-gray-400">
                <option>请选择</option>
            </select>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-24 text-right">作业用途分类:</label>
            <select class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none bg-white text-gray-400">
                <option>选择用途分类</option>
            </select>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-16 text-right">姓名:</label>
            <input class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none" placeholder="请输入内容" type="text"/>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-16 text-right">手机:</label>
            <input class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none" placeholder="请输入内容" type="text"/>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-16 text-right">提交时间:</label>
            <div class="flex-1 flex items-center border border-gray-300 rounded bg-white">
                <input class="w-1/2 p-1.5 text-xs outline-none text-gray-400 text-center" placeholder="开始日期">
                <span class="text-gray-300 text-xs">-</span>
                <input class="w-1/2 p-1.5 text-xs outline-none text-gray-400 text-center" placeholder="结束日期">
            </div>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-24 text-right">审核状态:</label>
            <select class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none bg-white text-gray-400">
                <option>请选择</option>
            </select>
        </div>
        <div class="flex items-center gap-2">
            <label class="text-xs font-medium text-gray-700 w-16 text-right">建议方向:</label>
            <select class="flex-1 border border-gray-300 rounded p-1.5 text-xs focus:border-blue-500 outline-none bg-white text-gray-400">
                <option>请选择</option>
            </select>
        </div>
        <div class="flex justify-end gap-2 items-center">
            <button class="bg-white border border-gray-300 text-gray-700 px-4 py-1.5 rounded text-xs hover:bg-gray-50 transition-colors">重置</button>
            <button class="bg-[#1890ff] text-white px-4 py-1.5 rounded text-xs hover:bg-blue-500 transition-colors">搜索</button>
            <button class="bg-[#1890ff] text-white px-4 py-1.5 rounded text-xs hover:bg-blue-500 transition-colors">导出</button>
            <button class="bg-[#1890ff] text-white px-4 py-1.5 rounded text-xs hover:bg-blue-500 transition-colors">查看导出记录</button>
        </div>
    </div>
</div>

<!-- Data Table -->
<div class="bg-white rounded-md shadow-sm border border-gray-200 overflow-hidden">
<div class="overflow-x-auto custom-scrollbar">
<table class="w-max min-w-full divide-y divide-gray-200 text-xs">
<thead class="bg-gray-50">
<tr>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">序号</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">反馈分类</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">建议方向</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">关联作业</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">作业用途分类</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">用户ID</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">姓名</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">手机</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">所在党委</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">提交时间</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">分配品牌</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">审核状态</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">获得积分</th>
<th class="px-3 py-3 text-left font-bold text-dfblue bg-blue-50" scope="col">获得成长值</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">审核人</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">审核时间</th>
<th class="px-3 py-3 text-left font-medium text-gray-500" scope="col">备注</th>
<th class="px-3 py-3 text-left font-medium text-gray-500 sticky right-0 bg-gray-50 z-10 shadow-[-4px_0_10px_rgba(0,0,0,0.05)]" scope="col">操作</th>
</tr>
</thead>
<tbody class="bg-white divide-y divide-gray-200">
<tr class="hover:bg-gray-50 group">
<td class="px-3 py-3 whitespace-nowrap text-gray-500">1</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">作业申请</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">1766988633188401154</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">闵笛迪</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">135****5352</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">2025-01-09 20:28:57</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">东风护卫军</td>
<td class="px-3 py-3 whitespace-nowrap text-yellow-600">待审核</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap font-bold text-dfblue bg-blue-50/20">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-blue-600 sticky right-0 bg-white z-10 shadow-[-4px_0_10px_rgba(0,0,0,0.02)] group-hover:bg-gray-50">
    <button onclick="openAuditModal()" class="hover:underline text-blue-600 font-medium">审核</button>
</td>
</tr>
<tr class="hover:bg-gray-50 group">
<td class="px-3 py-3 whitespace-nowrap text-gray-500">2</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">改善建议</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">作业审核</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">1834060270787043330</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">康才康</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">158****8778</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">中共东风物流集团股份有限公司委员会</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">2025-01-10 09:58:18</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">东风护卫军</td>
<td class="px-3 py-3 whitespace-nowrap text-green-600">审核通过</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-900">20</td>
<td class="px-3 py-3 whitespace-nowrap font-bold text-dfblue bg-blue-50/20">20 XP</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">zhangyanhong-admin</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">2025-02-23 14:00:48</td>
<td class="px-3 py-3 whitespace-nowrap text-gray-500">-</td>
<td class="px-3 py-3 whitespace-nowrap text-blue-600 sticky right-0 bg-white z-10 shadow-[-4px_0_10px_rgba(0,0,0,0.02)] group-hover:bg-gray-50">
    <a href="#" class="hover:underline text-blue-600">详情</a>
</td>
</tr>
</tbody>
</table>
</div>
<!-- Pagination -->
<div class="px-6 py-4 border-t border-gray-200 flex items-center justify-end text-xs text-gray-500 gap-4">
<span>共 3415 条数据</span>
<div class="flex gap-1">
    <button class="w-6 h-6 border border-gray-300 rounded flex items-center justify-center hover:bg-gray-50"><i class="fas fa-chevron-left"></i></button>
    <button class="w-6 h-6 border border-[#1890ff] bg-[#1890ff] text-white rounded flex items-center justify-center">1</button>
    <button class="w-6 h-6 border border-gray-300 rounded flex items-center justify-center hover:bg-gray-50">2</button>
    <button class="w-6 h-6 border border-gray-300 rounded flex items-center justify-center hover:bg-gray-50">3</button>
    <span class="px-1">...</span>
    <button class="w-6 h-6 border border-gray-300 rounded flex items-center justify-center hover:bg-gray-50">342</button>
    <button class="w-6 h-6 border border-gray-300 rounded flex items-center justify-center hover:bg-gray-50"><i class="fas fa-chevron-right"></i></button>
</div>
<div class="flex items-center gap-2">
    <select class="border border-gray-300 rounded px-2 py-1 outline-none"><option>10 条/页</option></select>
    <span>跳至</span>
    <input class="w-10 border border-gray-300 rounded px-1 py-1 text-center outline-none" value="1">
    <span>页</span>
</div>
</div>
</div>
</div>
</main>

<!-- Modal: Audit -->
<div id="audit-modal" class="fixed inset-0 z-50 flex items-center justify-center modal-overlay hidden">
    <div class="bg-white rounded-lg shadow-xl w-[800px] flex flex-col max-h-[90vh]">
        <div class="flex justify-between items-center px-6 py-4 border-b border-gray-200 shrink-0">
            <h3 class="text-base font-bold text-gray-800">审核</h3>
            <button onclick="closeAuditModal()" class="text-gray-400 hover:text-gray-600 focus:outline-none">
                <i class="fas fa-times text-lg"></i>
            </button>
        </div>
        
        <div class="p-6 overflow-y-auto flex-1">
            <h4 class="font-bold text-gray-800 mb-4 text-sm">基本信息：</h4>
            <div class="grid grid-cols-3 gap-y-4 text-sm text-gray-700 mb-6">
                <div><span class="text-gray-500 mr-2">反馈类型:</span>作业申请</div>
                <div><span class="text-gray-500 mr-2">申请作业事由:</span>宣传推广</div>
                <div><span class="text-gray-500 mr-2">作业平台:</span>公众号</div>
                
                <div><span class="text-gray-500 mr-2">账号类别:</span>集团账号</div>
                <div><span class="text-gray-500 mr-2">账号名称:</span>东风汽车</div>
                <div><span class="text-gray-500 mr-2">作品情绪:</span>中性</div>
                
                <div><span class="text-gray-500 mr-2">作业要求:</span>点赞</div>
                <div><span class="text-gray-500 mr-2">作业数量:</span>100</div>
                <div><span class="text-gray-500 mr-2">作业链接:</span><a href="#" class="text-blue-500 hover:underline">https://weibo.com/</a></div>
                
                <div class="col-span-3 flex items-start gap-12">
                    <div><span class="text-gray-500 mr-2">视频号ID:</span>https://weibo.com/</div>
                    <div><span class="text-gray-500 mr-2">视频ID:</span>https://weibo.com/</div>
                    <div class="flex items-center gap-2">
                        <span class="text-gray-500">视频号分享二维码:</span>
                        <div class="w-16 h-16 bg-gray-100 border border-gray-200 flex items-center justify-center text-xs text-gray-400">QR Code</div>
                    </div>
                </div>
                
                <div><span class="text-gray-500 mr-2">排期建议:</span>2024-12-12</div>
                <div class="col-span-2"><span class="text-gray-500 mr-2">作业名称:</span>1000辆大单！向“新”跃升！</div>
                
                <div class="col-span-3"><span class="text-gray-500 mr-2">作业申请主体:</span>个人</div>
                
                <div class="col-span-3">
                    <span class="text-gray-500 mr-2">作业指导:</span>
                    1000辆大单！向“新”跃升！1000辆大单！向“新”跃升！1000辆大单！向“新”跃升！
                </div>
            </div>
            
            <hr class="border-gray-100 my-6">
            
            <h4 class="font-bold text-gray-800 mb-4 text-sm">基本信息：</h4>
            <div class="grid grid-cols-3 gap-y-4 text-sm text-gray-700 mb-6">
                <div><span class="text-gray-500 mr-2">姓名:</span>张三</div>
                <div><span class="text-gray-500 mr-2">电话:</span>13660457322</div>
                <div><span class="text-gray-500 mr-2">所在党委:</span>中共东风汽车</div>
            </div>
            
            <div class="flex items-center gap-4 mb-4">
                <label class="text-sm text-gray-700 w-20 text-right">奖励积分:</label>
                <input type="number" class="border border-gray-300 rounded px-3 py-1.5 text-sm outline-none focus:border-blue-500 w-64" placeholder="请输入积分">
            </div>
            
            <div class="flex items-center gap-4 mb-4">
                <label class="text-sm font-bold text-dfblue w-20 text-right">奖励成长值:</label>
                <div class="flex items-center gap-2 w-64">
                    <input type="number" class="border border-blue-300 rounded px-3 py-1.5 text-sm outline-none focus:border-blue-500 flex-1 text-dfblue font-bold bg-blue-50/30" value="20">
                    <span class="text-sm text-gray-500">XP</span>
                </div>
                <div class="text-xs text-gray-400"><i class="fas fa-info-circle text-blue-400 mr-1"></i>系统带出默认配置值，支持手动修改</div>
            </div>
            
            <div class="flex items-start gap-4">
                <label class="text-sm text-gray-700 w-20 text-right mt-1">审核说明:</label>
                <div class="relative flex-1">
                    <textarea class="border border-gray-300 rounded p-2 text-sm outline-none focus:border-blue-500 w-full h-24 resize-none" placeholder="请输入不超过200字的审核说明"></textarea>
                    <div class="absolute bottom-2 right-2 text-xs text-gray-400">0/200</div>
                </div>
            </div>
        </div>
        
        <div class="px-6 py-4 border-t border-gray-200 flex justify-end gap-3 bg-gray-50 rounded-b-lg">
            <button class="bg-[#1890ff] text-white px-5 py-2 rounded text-sm hover:bg-blue-500 transition-colors">分配</button>
            <button class="bg-white border border-gray-300 text-gray-700 px-5 py-2 rounded text-sm hover:bg-gray-50 transition-colors">不通过</button>
            <button class="bg-[#1890ff] text-white px-5 py-2 rounded text-sm hover:bg-blue-500 transition-colors">审核通过</button>
        </div>
    </div>
</div>

<script>
    function openAuditModal() {
        document.getElementById('audit-modal').classList.remove('hidden');
    }
    function closeAuditModal() {
        document.getElementById('audit-modal').classList.add('hidden');
    }
</script>
</body>
</html>
"""
with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_反馈审核列表页.html", "w", encoding="utf-8") as f:
    f.write(html_content)
