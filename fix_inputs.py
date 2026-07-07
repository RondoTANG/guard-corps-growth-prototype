import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# For Level 2, 3, 4, the name input shouldn't be disabled.
html = html.replace('<input type="text" value="熟练护卫军" disabled class="w-full bg-gray-100 text-gray-500 cursor-not-allowed border-gray-200 rounded-md shadow-sm text-sm p-2 border outline-none">',
                   '<input type="text" value="熟练护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred focus:ring-1 focus:ring-dfred outline-none">')

html = html.replace('<input type="text" value="专家护卫军" disabled class="w-full bg-gray-100 text-gray-500 cursor-not-allowed border-gray-200 rounded-md shadow-sm text-sm p-2 border outline-none">',
                   '<input type="text" value="专家护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred focus:ring-1 focus:ring-dfred outline-none">')

html = html.replace('<input type="text" value="大师护卫军" disabled class="w-full bg-gray-100 text-gray-500 cursor-not-allowed border-gray-200 rounded-md shadow-sm text-sm p-2 border outline-none">',
                   '<input type="text" value="大师护卫军" class="w-full border-gray-300 rounded-md shadow-sm text-sm p-2 border focus:border-dfred focus:ring-1 focus:ring-dfred outline-none">')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
