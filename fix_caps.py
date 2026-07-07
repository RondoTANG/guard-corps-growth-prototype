import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the rows where category is "日常类" and change the cap config to a hardcoded "每日封顶: [input] XP"
# The rows look like:
# <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500" rowspan="X">日常类</td>
# ...
# <td><div class="flex items-center gap-2"><select...><option value="post">单篇</option><option value="daily">每日</option><option value="monthly">每月</option></select>上限 <input...> XP</div></td>

# This is a bit tricky to do with simple string replace because the cap dropdown is identical for all rows.
# But I can parse with BeautifulSoup or just write a small parser.

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find the tbody inside tab-task
tab_task = soup.find('div', id='tab-task')
if not tab_task:
    print("Could not find tab-task")
    exit(1)

tbody = tab_task.find('tbody')
rows = tbody.find_all('tr')

current_category = None

for row in rows:
    # Find category
    tds = row.find_all('td')
    if not tds:
        continue
    
    # Check if first td has rowspan, meaning it's a category td
    if tds[0].has_attr('rowspan'):
        current_category = tds[0].get_text().strip()
        cap_td_index = 4
        switch_td_index = 5
    else:
        cap_td_index = 3
        switch_td_index = 4
        
    if len(tds) > cap_td_index:
        cap_td = tds[cap_td_index]
        
        if current_category == "日常类":
            # Just keep "每日上限 [input] XP"
            input_el = cap_td.find('input')
            if input_el:
                new_html = f'<div class="flex items-center gap-2 text-sm text-gray-700">每日上限 <input type="number" value="{input_el.get("value", 50)}" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1 border focus:border-dfred outline-none"> XP</div>'
                cap_td.clear()
                cap_td.append(BeautifulSoup(new_html, 'html.parser'))
                
        elif current_category in ["互动类", "人工干预类"]:
            # Dropdown with only Daily, Monthly
            input_el = cap_td.find('input')
            if input_el:
                new_html = f'''<div class="flex items-center gap-2">
                    <select class="border-gray-300 rounded-md shadow-sm text-sm p-1 border focus:border-dfred outline-none">
                        <option value="daily">每日</option>
                        <option value="monthly">每月</option>
                    </select>
                    上限 <input type="number" value="{input_el.get("value", 100)}" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1 border focus:border-dfred outline-none"> XP
                </div>'''
                cap_td.clear()
                cap_td.append(BeautifulSoup(new_html, 'html.parser'))

# Fix the toggle switches to be clickable (just simple UI state toggle via inline onclick for prototype)
# A lot of spans have class="bg-gray-200 relative inline-flex ... cursor-pointer"
# Let's add an onclick handler to toggle them.
for toggle in soup.find_all('span', class_=re.compile(r'relative inline-flex')):
    if 'cursor-pointer' in toggle.get('class', []):
        # Add onclick toggle logic
        toggle['onclick'] = "this.classList.toggle('bg-green-500'); this.classList.toggle('bg-gray-200'); this.querySelector('span').classList.toggle('translate-x-5'); this.querySelector('span').classList.toggle('translate-x-0');"

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done fixing caps and switches")
