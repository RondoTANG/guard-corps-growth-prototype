from bs4 import BeautifulSoup
import re

# 1. Read current broken B端_等级规则与XP配置页.html
with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 2. Recover tab-tier
with open('recovered_tier.html', 'r', encoding='utf-8') as f:
    recovered_tier_html = f.read()
recovered_tier_soup = BeautifulSoup(recovered_tier_html, 'html.parser')

tab_tier = soup.find('div', id='tab-tier')
if tab_tier:
    tab_tier.replace_with(recovered_tier_soup)

# 3. Fix tab-task filtering
# Remove the old filter block
for div in soup.find_all('div', class_=re.compile('bg-white p-4 rounded-lg border border-gray-200')):
    if '作业大类' in div.text and '重置' in div.text:
        div.extract()

tab_task = soup.find('div', id='tab-task')

# Make the table headers dropdowns
if tab_task:
    headers = tab_task.find_all('th')
    for th in headers:
        text = th.text.strip()
        if text == '作业大类':
            th.clear()
            select = soup.new_tag('select', attrs={'class': 'text-xs font-bold text-gray-500 uppercase tracking-wider bg-transparent outline-none cursor-pointer w-full appearance-none'})
            # We add an icon using a wrapper if we want, but a native select is fine for prototype
            select.append(BeautifulSoup('<option>全部大类 ▼</option><option>转发</option><option>原创</option><option>点赞/评论</option>', 'html.parser'))
            th.append(select)
            th['class'] = th.get('class', []) + ['hover:bg-gray-100', 'transition-colors', 'cursor-pointer']
        elif text == '作业平台':
            th.clear()
            select = soup.new_tag('select', attrs={'class': 'text-xs font-bold text-gray-500 uppercase tracking-wider bg-transparent outline-none cursor-pointer w-full appearance-none'})
            select.append(BeautifulSoup('<option>全部平台 ▼</option><option>朋友圈</option><option>知乎</option><option>微信视频号</option>', 'html.parser'))
            th.append(select)
            th['class'] = th.get('class', []) + ['hover:bg-gray-100', 'transition-colors', 'cursor-pointer']

# 4. Fix Toggle Switches
switches = tab_task.find_all('button', role='switch')
for i, btn in enumerate(switches):
    btn['onclick'] = "toggleSwitch(this)"
    circle = btn.find('span')
    # Default some to ON
    if i < 4:
        btn['aria-checked'] = 'true'
        btn['class'] = [c.replace('bg-gray-200', 'bg-dfred') for c in btn.get('class', [])]
        if 'bg-dfred' not in btn['class']:
            btn['class'].append('bg-dfred')
        
        if circle:
            circle['class'] = [c.replace('translate-x-0', 'translate-x-5') for c in circle.get('class', [])]
            if 'translate-x-5' not in circle['class']:
                circle['class'].append('translate-x-5')
    else:
        btn['aria-checked'] = 'false'
        btn['class'] = [c.replace('bg-dfred', 'bg-gray-200') for c in btn.get('class', [])]
        if 'bg-gray-200' not in btn['class']:
            btn['class'].append('bg-gray-200')
            
        if circle:
            circle['class'] = [c.replace('translate-x-5', 'translate-x-0') for c in circle.get('class', [])]
            if 'translate-x-0' not in circle['class']:
                circle['class'].append('translate-x-0')

# 5. Inject JS
js = """
        function toggleSwitch(btn) {
            const isChecked = btn.getAttribute('aria-checked') === 'true';
            const circle = btn.querySelector('span');
            
            if (isChecked) {
                btn.setAttribute('aria-checked', 'false');
                btn.classList.remove('bg-dfred');
                btn.classList.add('bg-gray-200');
                circle.classList.remove('translate-x-5');
                circle.classList.add('translate-x-0');
            } else {
                btn.setAttribute('aria-checked', 'true');
                btn.classList.remove('bg-gray-200');
                btn.classList.add('bg-dfred');
                circle.classList.remove('translate-x-0');
                circle.classList.add('translate-x-5');
            }
        }
"""
script_tag = soup.find_all('script')[-1]
if 'toggleSwitch(btn)' not in script_tag.text:
    script_tag.string = script_tag.string + js

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("All fixes applied successfully.")
