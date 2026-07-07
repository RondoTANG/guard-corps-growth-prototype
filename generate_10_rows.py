import re
import random

html_file = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_作业管理列表.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define options for the 10 rows
levels = [
    '<span class="px-2 py-0.5 bg-orange-50 text-orange-600 border border-orange-200 rounded text-xs font-medium"><i class="fas fa-crown text-[10px] mr-1"></i>Lv4 大师护卫军</span>',
    '<span class="px-2 py-0.5 bg-blue-50 text-blue-600 border border-blue-200 rounded text-xs font-medium"><i class="fas fa-medal text-[10px] mr-1"></i>Lv3 专家护卫军</span>',
    '<span class="px-2 py-0.5 bg-green-50 text-green-600 border border-green-200 rounded text-xs font-medium"><i class="fas fa-shield-alt text-[10px] mr-1"></i>Lv2 熟练护卫军</span>',
    '<span class="px-2 py-0.5 bg-gray-50 text-gray-600 border border-gray-200 rounded text-xs font-medium"><i class="fas fa-seedling text-[10px] mr-1"></i>Lv1 新秀护卫军</span>',
    '<span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded text-xs">无门槛</span>'
]

xps = [
    '<span class="font-bold text-dfred">+200 XP <span class="text-xs text-gray-400 font-normal">(特殊)</span></span>',
    '<span class="text-gray-600">+100 XP <span class="text-xs text-gray-400 font-normal">(默认)</span></span>',
    '<span class="text-gray-600">+50 XP <span class="text-xs text-gray-400 font-normal">(默认)</span></span>',
    '<span class="font-bold text-dfred">+300 XP <span class="text-xs text-gray-400 font-normal">(特殊)</span></span>',
    '<span class="text-gray-400">-</span>'
]

statuses = [
    '<span class="inline-flex items-center text-green-600 text-xs"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>发布中</span>',
    '<span class="inline-flex items-center text-blue-600 text-xs"><span class="w-1.5 h-1.5 rounded-full bg-blue-500 mr-1.5"></span>待发布</span>',
    '<span class="inline-flex items-center text-gray-500 text-xs"><span class="w-1.5 h-1.5 rounded-full bg-gray-400 mr-1.5"></span>已结束</span>'
]

push_types = ['段位推送', '人群包推送', '全量推送', '标签推送']

rows = []
for i in range(10):
    level = levels[i % 5]
    xp = xps[(i + 1) % 5]
    status = statuses[i % 3]
    push = push_types[i % 4]
    
    row = f"""<tr class="hover:bg-blue-50/30 transition-colors">
<td class="py-4 px-4 text-center"><input class="rounded border-gray-300" type="checkbox"/></td>
<td class="py-4 px-4 text-gray-500">2026071{10-i:02d}</td>
<td class="py-4 px-4">
<div class="font-medium text-gray-900 truncate w-[250px]">测试作业内容_编号{10-i}</div>
</td>
<td class="py-4 px-4">互动作业</td>
<td class="py-4 px-4 text-gray-500 truncate w-[150px]">日常维护&gt;口碑建设</td>
<td class="py-4 px-4">{status}</td>
<td class="py-4 px-4 text-gray-500">APP跳转</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-0{i%5+1} 10:00</div>
<div>2026-07-0{i%5+2} 23:59</div>
</td>
<td class="py-4 px-4">{level}</td>
<td class="py-4 px-4">{xp}</td>
<td class="py-4 px-4 text-gray-500">{"不限" if i%2==0 else "5000"}</td>
<td class="py-4 px-4 text-gray-500">{push}</td>
<td class="py-4 px-4 text-gray-500">{"-" if i%2==0 else "第1次轮回"}</td>
<td class="py-4 px-4 text-gray-500">{"-" if push=='全量推送' else "1000"}</td>
<td class="py-4 px-4 text-gray-500">10</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">10000</td>
<td class="py-4 px-4 text-gray-500">是</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">-</td>
<td class="py-4 px-4 text-gray-500">梁昊悠</td>
<td class="py-4 px-4 text-gray-500 text-xs leading-tight">
<div>2026-07-01</div>
<div>15:49:00</div>
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
</tr>"""
    rows.append(row)

new_tbody = '<tbody class="text-sm divide-y divide-gray-100">\n' + '\n'.join(rows) + '\n</tbody>'

# Fix the table headers tooltips to be better (use CSS tooltips if possible, or just standard titles, but let's make it CSS tooltip)
# Actually, standard title is fine, but since user asked, let's add a custom tooltip
content = re.sub(r'<tbody class="text-sm divide-y divide-gray-100">.*?</tbody>', new_tbody, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

