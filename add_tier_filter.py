file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_用户管理_XP干预页.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

target = """<div class="flex items-center gap-2">
                        <label class="text-xs font-medium text-gray-700">身份:</label>
                        <select class="border border-gray-300 rounded p-1.5 text-xs w-32 focus:border-blue-500 outline-none bg-white">
                            <option>员工</option>
                        </select>
                    </div>"""

replacement = """<div class="flex items-center gap-2">
                        <label class="text-xs font-medium text-gray-700">身份:</label>
                        <select class="border border-gray-300 rounded p-1.5 text-xs w-24 focus:border-blue-500 outline-none bg-white">
                            <option>员工</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <label class="text-xs font-medium text-gray-700">段位:</label>
                        <select class="border border-gray-300 rounded p-1.5 text-xs w-32 focus:border-blue-500 outline-none bg-white">
                            <option>全部段位</option>
                            <option>Level 1 (新秀)</option>
                            <option>Level 2 (熟练)</option>
                            <option>Level 3 (专家)</option>
                            <option>Level 4 (大师)</option>
                        </select>
                    </div>"""

html = html.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
