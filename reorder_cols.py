import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update header
# Old header block:
old_header = """<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">单次发放 XP</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">逾期扣除 XP</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">封顶限制开关</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider bg-gray-50" scope="col">限制规则与阀值配置</th>"""

new_header = """<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">单次发放 XP</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50" scope="col">封顶限制开关</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider bg-gray-50" scope="col">限制规则与阀值配置</th>
<th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 bg-gray-50 border-l border-gray-200" scope="col">
    逾期扣除 XP 
    <i class="fas fa-info-circle text-gray-400 cursor-help" title="若用户领取了限量的作业任务但未按时提交，系统将自动扣除此分值作为惩罚"></i>
</th>"""
content = content.replace(old_header, new_header)

# 2. Reorder tds in each row.
# Each row has a set of tds. The "逾期扣除 XP" td is currently right after "单次发放 XP" td.
# We need to find the "逾期扣除 XP" td and move it after the "限制规则" td.
# The structure is:
# td_issue = <td class="px-6 py-3 whitespace-nowrap">\n<input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none" type="number" value="\d+"/>\n</td>
# td_deduct = \n<td class="px-6 py-3 whitespace-nowrap">\n<input class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none text-red-600 font-bold" type="number" value="-?\d+"/>\n</td>
# td_switch = \n<td class="px-6 py-3 whitespace-nowrap">\n<div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in">\n<input checked="" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer" id="toggle-\d+" type="checkbox"/>\n<label class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300 cursor-pointer" for="toggle-\d+"></label>\n</div>\n</td>
# td_limit = \n<td class="px-6 py-3 whitespace-nowrap">\n<div class="flex items-center gap-2 limit-config-group">\n...\n</td>

# Let's use a simpler approach. Split by <tr> and </tr>
new_rows = []
rows = content.split('<tr')
new_rows.append(rows[0])
for row in rows[1:]:
    if 'border-gray-300 rounded-md shadow-sm text-sm p-1.5 border' not in row:
        new_rows.append('<tr' + row)
        continue
    
    # It's a row in our table.
    # We will split it by <td class="px-6 py-3 whitespace-nowrap">.
    # The first few tds might have rowspan, so they might have different classes.
    # But the 4 columns we care about all start with '<td class="px-6 py-3 whitespace-nowrap">' or something similar?
    # Let's check exactly how they are formatted.
    pass

# We can use regex to match the sequence of 4 tds:
# 1. <td ...> ... <input ... value="\d+"/> ... </td>  (Issue XP)
# 2. <td ...> ... <input ... text-red-600 ... value="-?\d+"/> ... </td> (Deduct XP)
# 3. <td ...> ... toggle-checkbox ... </td> (Switch)
# 4. <td ...> ... limit-config-group ... </td> (Limit)

import re

# Match the 4 tds:
# We will match from the start of td_issue to the end of td_limit.
pattern = r'(<td class="px-6 py-3 whitespace-nowrap">(?:.(?!<td))*?<input[^>]*?type="number"[^>]*?>\s*</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">\s*<input[^>]*?text-red-600[^>]*?>\s*</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">.*?</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">.*?</td>)'

def replacer(match):
    td_issue = match.group(1)
    td_deduct = match.group(2)
    td_switch = match.group(3)
    td_limit = match.group(4)
    # Add border to td_deduct to match the header border
    td_deduct = td_deduct.replace('<td class="px-6 py-3 whitespace-nowrap">', '<td class="px-6 py-3 whitespace-nowrap border-l border-gray-100 bg-red-50/20">')
    return f"{td_issue}\n{td_switch}\n{td_limit}\n{td_deduct}"

content = re.sub(pattern, replacer, content, flags=re.DOTALL)

# Handle special rows like "人工干预调账" or rows without inputs
special_pattern = r'(<td class="px-6 py-3 whitespace-nowrap">\s*<span class="text-sm text-gray-400">无固定值</span>\s*</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">\s*<span class="text-sm text-gray-400">--</span>\s*</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">.*?</td>)\s*(<td class="px-6 py-3 whitespace-nowrap">.*?</td>)'
def special_replacer(match):
    td_issue = match.group(1)
    td_deduct = match.group(2)
    td_switch = match.group(3)
    td_limit = match.group(4)
    td_deduct = td_deduct.replace('<td class="px-6 py-3 whitespace-nowrap">', '<td class="px-6 py-3 whitespace-nowrap border-l border-gray-100 bg-red-50/20">')
    return f"{td_issue}\n{td_switch}\n{td_limit}\n{td_deduct}"

content = re.sub(special_pattern, special_replacer, content, flags=re.DOTALL)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Reordered columns!")
