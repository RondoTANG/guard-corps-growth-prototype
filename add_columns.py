import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_用户管理_XP干预页.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add to thead
html = html.replace(
    '<th scope="col" class="px-4 py-3 text-left font-medium text-gray-500">状态</th>',
    '<th scope="col" class="px-4 py-3 text-left font-medium text-gray-500">当前段位</th>\n                                <th scope="col" class="px-4 py-3 text-left font-medium text-gray-500">XP余额</th>\n                                <th scope="col" class="px-4 py-3 text-left font-medium text-gray-500">状态</th>'
)

# Row 1
html = html.replace(
    '<td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 09:15:42</td>',
    '<td class="px-4 py-3 whitespace-nowrap"><span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800 border border-yellow-200"><i class="fas fa-crown mr-1 mt-0.5"></i> Level 4 (大师)</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-900 font-bold">12,450</td>\n                                <td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 09:15:42</td>',
    1
)

# Row 2
html = html.replace(
    '<td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 08:52:01</td>',
    '<td class="px-4 py-3 whitespace-nowrap"><span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800 border border-blue-200">Level 2 (熟练)</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-900 font-bold">1,450</td>\n                                <td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 08:52:01</td>',
    1
)

# Row 3
html = html.replace(
    '<td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 08:30:55</td>',
    '<td class="px-4 py-3 whitespace-nowrap"><span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800 border border-gray-200">Level 1 (新秀)</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-900 font-bold">120</td>\n                                <td class="px-4 py-3 whitespace-nowrap"><span class="flex items-center text-gray-700"><span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-1.5"></span>正常</span></td>\n                                <td class="px-4 py-3 whitespace-nowrap text-gray-500">2026-07-03 08:30:55</td>',
    1
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Added columns")
