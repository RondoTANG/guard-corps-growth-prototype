import re

file_path = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_作业管理列表.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove <h1>作业管理</h1>
content = content.replace('<div class="flex items-center justify-between mb-4">\n<h1 class="text-xl font-bold text-gray-900">作业管理</h1>', '<div class="flex items-center justify-end mb-4">')

# 2. Update table wrapper min-width
content = content.replace('min-w-[1500px]', 'min-w-[2800px]')

# 3. Update thead
new_thead = """<tr class="bg-gray-50 border-b border-gray-200 text-xs text-gray-500">
<th class="py-3 px-4 w-10 text-center"><input class="rounded border-gray-300" type="checkbox"/></th>
<th class="py-3 px-4 font-medium">作业ID</th>
<th class="py-3 px-4 font-medium min-w-[200px]">作业名称</th>
<th class="py-3 px-4 font-medium">作业类型</th>
<th class="py-3 px-4 font-medium">作业用途分类</th>
<th class="py-3 px-4 font-medium">作业状态</th>
<th class="py-3 px-4 font-medium">作业平台</th>
<th class="py-3 px-4 font-medium">作业时间</th>
<th class="py-3 px-4 font-medium min-w-[100px]">承接门槛 <i class="fas fa-info-circle text-gray-400 ml-1 cursor-help" title="承接此任务需满足的段位或XP要求"></i></th>
<th class="py-3 px-4 font-medium min-w-[100px]">单次发放XP <i class="fas fa-info-circle text-gray-400 ml-1 cursor-help" title="完成此任务后系统发放的成长经验值"></i></th>
<th class="py-3 px-4 font-medium">作业总量</th>
<th class="py-3 px-4 font-medium">推送方式</th>
<th class="py-3 px-4 font-medium">轮回次数</th>
<th class="py-3 px-4 font-medium">推送人数</th>
<th class="py-3 px-4 font-medium">基础奖励积分</th>
<th class="py-3 px-4 font-medium">效果奖励模式</th>
<th class="py-3 px-4 font-medium">效果奖励积分上限</th>
<th class="py-3 px-4 font-medium">积分预算</th>
<th class="py-3 px-4 font-medium">AI审核</th>
<th class="py-3 px-4 font-medium">排序</th>
<th class="py-3 px-4 font-medium">备注</th>
<th class="py-3 px-4 font-medium">创建人</th>
<th class="py-3 px-4 font-medium min-w-[120px]">创建时间</th>
<th class="py-3 px-4 font-medium sticky right-0 bg-gray-50 shadow-[-5px_0_10px_-5px_rgba(0,0,0,0.1)] text-center min-w-[300px]">操作</th>
</tr>"""

content = re.sub(r'<tr class="bg-gray-50 border-b border-gray-200 text-xs text-gray-500">.*?</tr>', new_thead, content, flags=re.DOTALL)

# 4. Update the tbody mock data
new_tbody = """<tbody class="text-sm divide-y divide-gray-100">
<tr class="hover:bg-blue-50/30 transition-colors">
<td class="py-4 px-4 text-center"><input class="rounded border-gray-300" type="checkbox"/></td>
<td class="py-4 px-4 text-gray-500">202607101</td>
<td class="py-4 px-4">
<div class="font-medium text-gray-900 truncate w-[250px]">(加推) 东风奕派M8获得中汽中心...</div>
</td>
<td class="py-4 px-4">互动作业</td>
<td class="py-4 px-4 text-gray-500 truncate w-[150px]">品牌专项&gt;车型上新&gt;奕派M8</td>
<td class="py-4 px-4">
<span class="inline-flex items-center text-green-600 text-xs">
<span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>发布中
</span>
</td>
<td class="py-4 px-4 text-gray-500">微信公众号</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-03 00:00</div>
<div>2026-07-04 23:59</div>
</td>
<td class="py-4 px-4">
<span class="px-2 py-0.5 bg-orange-50 text-orange-600 border border-orange-200 rounded text-xs font-medium"><i class="fas fa-crown text-[10px] mr-1"></i>大师专属</span>
</td>
<td class="py-4 px-4">
<span class="font-bold text-dfred">+200 XP</span>
</td>
<td class="py-4 px-4 text-gray-500">5000</td>
<td class="py-4 px-4 text-blue-500 cursor-pointer hover:underline">段位推送</td>
<td class="py-4 px-4 text-gray-500">第1次轮回</td>
<td class="py-4 px-4 text-blue-500 cursor-pointer hover:underline">5000</td>
<td class="py-4 px-4 text-gray-500">8</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">40000</td>
<td class="py-4 px-4 text-gray-500">是</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">梁昊悠</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-03</div>
<div>15:49:30</div>
</td>
<td class="py-4 px-4 sticky right-0 bg-white group-hover:bg-blue-50/30 shadow-[-5px_0_10px_-5px_rgba(0,0,0,0.05)] text-center">
<div class="flex items-center justify-center gap-2 text-dfblue text-xs flex-wrap">
<a class="hover:text-blue-800" href="#">作业详情</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">查看作业</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">复制</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">排序</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">预览</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">备注</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">用途分类</a>
</div>
</td>
</tr>

<tr class="hover:bg-blue-50/30 transition-colors">
<td class="py-4 px-4 text-center"><input class="rounded border-gray-300" type="checkbox"/></td>
<td class="py-4 px-4 text-gray-500">202607100</td>
<td class="py-4 px-4">
<div class="font-medium text-gray-900 truncate w-[250px]">【日常点赞】懂车帝M8口碑维护</div>
</td>
<td class="py-4 px-4">外链作业</td>
<td class="py-4 px-4 text-gray-500 truncate w-[150px]">日常维护&gt;口碑建设</td>
<td class="py-4 px-4">
<span class="inline-flex items-center text-blue-600 text-xs">
<span class="w-1.5 h-1.5 rounded-full bg-blue-500 mr-1.5"></span>待发布
</span>
</td>
<td class="py-4 px-4 text-gray-500">APP跳转</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-05 10:00</div>
<div>2026-07-06 23:59</div>
</td>
<td class="py-4 px-4">
<span class="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">无门槛</span>
</td>
<td class="py-4 px-4">
<span class="text-gray-400">-</span>
</td>
<td class="py-4 px-4 text-gray-500">不限</td>
<td class="py-4 px-4 text-blue-500 cursor-pointer hover:underline">人群包推送</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-blue-500 cursor-pointer hover:underline">120</td>
<td class="py-4 px-4 text-gray-500">10</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">1200</td>
<td class="py-4 px-4 text-gray-500">是</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">评论209+210</td>
<td class="py-4 px-4 text-gray-500">梁昊悠</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-03</div>
<div>15:49:27</div>
</td>
<td class="py-4 px-4 sticky right-0 bg-white group-hover:bg-blue-50/30 shadow-[-5px_0_10px_-5px_rgba(0,0,0,0.05)] text-center">
<div class="flex items-center justify-center gap-2 text-dfblue text-xs flex-wrap">
<a class="hover:text-blue-800" href="#">作业详情</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">查看作业</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">复制</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">排序</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">预览</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">备注</a><span class="text-gray-200">|</span>
<a class="hover:text-blue-800" href="#">用途分类</a>
</div>
</td>
</tr>
</tbody>"""

content = re.sub(r'<tbody class="text-sm divide-y divide-gray-100">.*?</tbody>', new_tbody, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Table successfully updated!")
