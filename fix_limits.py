import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix the button text
html = re.sub(
    r'<button onclick="switchConfigTab\(\'tab-task\'\)" id="btn-tab-task"[^>]*>.*?</button>',
    '<button onclick="switchConfigTab(\'tab-task\')" id="btn-tab-task"\n                            class="px-4 py-2 rounded-md text-sm font-medium text-gray-500 hover:text-gray-700 hover:bg-gray-200 transition-all tab-btn">作业 XP 产出映射配置</button>',
    html,
    flags=re.DOTALL
)

# Fix Headers
html = re.sub(
    r'<th[^>]*>\s*单次基础 XP 奖励\s*</th>\s*<th[^>]*>\s*单篇封顶限制\s*</th>\s*<th[^>]*>\s*最高阀门值\s*</th>',
    '''<th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">
                                        单次发放 XP</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">
                                        封顶限制开关</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        限制规则与阀值配置</th>''',
    html,
    flags=re.DOTALL
)

# Row 1 (Original)
html = re.sub(
    r'<span class="text-sm text-gray-500">上限</span>\s*<input type="number" value="100"[^>]*>\s*<span class="text-sm text-gray-500">XP / 篇</span>',
    '''<select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
                                                <option selected>单篇最高</option>
                                                <option>每日最高</option>
                                                <option>每月最高</option>
                                            </select>
                                            <input type="number" value="150" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">
                                            <span class="text-sm text-gray-500">XP</span>''',
    html,
    flags=re.DOTALL
)

# Row 2 (Comment)
html = re.sub(
    r'<span class="text-sm text-gray-500">每月最多可得</span>\s*<input type="number" value="300"[^>]*>\s*<span class="text-sm text-gray-500">XP</span>',
    '''<select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
                                                <option>单篇最高</option>
                                                <option>每日最高</option>
                                                <option selected>每月最高</option>
                                            </select>
                                            <input type="number" value="300" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">
                                            <span class="text-sm text-gray-500">XP</span>''',
    html,
    flags=re.DOTALL
)

# Row 3 (Video)
html = re.sub(
    r'<td class="px-6 py-4 whitespace-nowrap">\s*<span class="text-sm text-gray-500">XP</span>\s*</td>',
    '''<td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex items-center gap-2">
                                            <select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
                                                <option>单篇最高</option>
                                                <option selected>每日最高</option>
                                                <option>每月最高</option>
                                            </select>
                                            <input type="number" value="20" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none disabled:bg-gray-100 disabled:text-gray-400">
                                            <span class="text-sm text-gray-500">XP</span>
                                        </div>
                                    </td>''',
    html,
    count=1,
    flags=re.DOTALL
)

# Row 4 (Daily Checkin)
html = re.sub(
    r'<span class="text-sm text-gray-500">每日最多可得</span>\s*<input type="number" value="2"[^>]*>\s*<span class="text-sm text-gray-500">XP</span>',
    '''<select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
                                                <option>单篇最高</option>
                                                <option selected>每日最高</option>
                                                <option>每月最高</option>
                                            </select>
                                            <input type="number" value="2" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">
                                            <span class="text-sm text-gray-500">XP</span>''',
    html,
    flags=re.DOTALL
)

# Fix Javascript target from td:last-child input to match both select and input
html = html.replace(
    "const inputs = tr.querySelectorAll('td:last-child input');",
    "const inputs = tr.querySelectorAll('td:last-child input, td:last-child select');"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")
