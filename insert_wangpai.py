import os

html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

target = '<tr class="border-t-2 border-gray-200 hover:bg-blue-50">\n<td class="px-6 py-3 whitespace-nowrap text-sm font-bold text-gray-900 border-t-2 border-gray-200 bg-gray-50 align-top" rowspan="1">人工干预调账</td>'

new_row = """<tr class="border-t-2 border-gray-200 hover:bg-blue-50">
<td class="px-6 py-3 whitespace-nowrap text-sm font-bold text-gray-900 border-t-2 border-gray-200 bg-gray-50 align-top" rowspan="1">官方内容精选</td>
<td class="px-6 py-3 whitespace-nowrap text-sm font-medium text-gray-700 bg-white align-top" rowspan="1">后台-文章管理</td>
<td class="px-6 py-3 whitespace-nowrap text-sm text-gray-500">登上王牌护卫军</td>
<td class="px-6 py-3 whitespace-nowrap">
<input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none" type="number" value="100"/>
</td>
<td class="px-6 py-3 whitespace-nowrap">
<div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in">
<input checked="" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer" id="toggle-wangpai" type="checkbox"/>
<label class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300 cursor-pointer" for="toggle-wangpai"></label>
</div>
</td>
<td class="px-6 py-3 whitespace-nowrap">
<div class="flex items-center gap-2 limit-config-group">
<select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
<option selected="">无上限</option>
<option>每日最高</option>
<option>每月最高</option>
</select>
<span class="text-sm text-gray-400">需发布文章时确认</span>
</div>
</td>
</tr>
"""

if target in html:
    html = html.replace(target, new_row + target)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully inserted 王牌护卫军 row.")
else:
    print("Could not find target row for replacement.")
