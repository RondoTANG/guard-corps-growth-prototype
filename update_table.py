import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update header
content = content.replace(
    '<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">单次发放 XP</th>',
    '<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">单次发放 XP</th>\n<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">逾期扣除 XP</th>'
)

# 2. Add the new td for each row.
# We look for the <td> that contains the "单次发放 XP" input.
# It looks like:
# <td class="px-6 py-3 whitespace-nowrap">
# <input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none" type="number" value="20"/>
# </td>
# We can use regex to find this block and append a new td with a default penalty value.
# Wait, some rows have 'value="10"', 'value="5"', 'value="100"', 'value="2"'.
# We can parse it and set penalty to something like - (value).
def replacer(match):
    original_td = match.group(0)
    val = int(match.group(1))
    penalty = -val if val > 0 else 0
    if penalty == 0:
        # for '无固定值' row or similar
        return original_td
    new_td = f'\n<td class="px-6 py-3 whitespace-nowrap">\n<input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none text-red-600 font-bold" type="number" value="{penalty}"/>\n</td>'
    return original_td + new_td

# Regex to match the issue XP td
pattern = r'<td class="px-6 py-3 whitespace-nowrap">\s*<input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none" type="number" value="(\d+)"/>\s*</td>'
content = re.sub(pattern, replacer, content)

# 3. Handle the two special rows at the bottom: "王牌护卫军" and "人工干预调账".
# Actually, the regex above will catch "王牌护卫军" which has value="100". It will get -100.
# "人工干预调账" has a span, not an input, so it will be ignored by regex. We need to manually add an empty td.
content = content.replace(
    '<td class="px-6 py-3 whitespace-nowrap">\n<span class="text-sm text-gray-400">无固定值</span>\n</td>',
    '<td class="px-6 py-3 whitespace-nowrap">\n<span class="text-sm text-gray-400">无固定值</span>\n</td>\n<td class="px-6 py-3 whitespace-nowrap">\n<span class="text-sm text-gray-400">--</span>\n</td>'
)

# 4. Remove the global "惩罚扣减" row we added previously (lines 1515-1533 approx)
start_idx = content.find('<tr class="border-t-2 border-gray-200 hover:bg-red-50">')
if start_idx != -1:
    end_idx = content.find('<tr class="border-t-2 border-gray-200 hover:bg-blue-50">\n<td class="px-6 py-3 whitespace-nowrap text-sm font-bold text-gray-900 border-t-2 border-gray-200 bg-gray-50 align-top" rowspan="1">人工干预调账</td>')
    if end_idx != -1:
        content = content[:start_idx] + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML table updated successfully.")
