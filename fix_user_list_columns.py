from bs4 import BeautifulSoup
import re

with open('B端_用户管理_XP干预页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the header
thead = soup.find('thead')
if thead:
    tr = thead.find('tr')
    headers = tr.find_all('th')
    for i, th in enumerate(headers):
        if th.string and '当前段位' in th.string:
            th.string = '当前段位'
            # Insert new header
            new_th = soup.new_tag('th', scope='col', **{'class': 'px-4 py-3 text-left font-medium text-gray-500'})
            new_th.string = '定级状态'
            th.insert_after(new_th)
            col_index = i
            break

# Update rows
tbody = soup.find('tbody')
if tbody:
    rows = tbody.find_all('tr')
    for tr in rows:
        tds = tr.find_all('td')
        if len(tds) > col_index:
            target_td = tds[col_index]
            
            # The target_td contains a div with two spans (or just the old span if unedited)
            # Let's extract the text we need.
            tier_text = "Level X"
            status_text = "-"
            
            spans = target_td.find_all('span')
            if len(spans) > 0:
                # First span usually contains the tier
                tier_text = spans[0].get_text(strip=True)
            if len(spans) > 1:
                # Second span might contain the status
                status_text = spans[1].get_text(strip=True)
                
            # Clean up tier text (remove extra spaces if any)
            tier_text = re.sub(r'\s+', ' ', tier_text)
            
            # If the script above failed to get status, check if we added status previously
            if '定级状态' not in status_text and '保级' not in status_text and '保底' not in status_text and '正常' not in status_text:
                status_text = "-" # fallback
            
            if '保级' in target_td.text:
                status_text = '保级缓冲期'
            elif '保底' in target_td.text:
                status_text = '荣誉保底'
            elif '正常' in target_td.text:
                status_text = '正常 (XP达标)'
                
            if 'Level 4' in target_td.text:
                tier_text = 'Level 4 (大师)'
            elif 'Level 3' in target_td.text:
                tier_text = 'Level 3 (专家)'
            elif 'Level 2' in target_td.text:
                tier_text = 'Level 2 (熟练)'
            elif 'Level 1' in target_td.text:
                tier_text = 'Level 1 (新秀)'

            # Modify the target_td to just contain the plain text tier
            target_td.clear()
            target_td.string = tier_text
            target_td['class'] = 'px-4 py-3 whitespace-nowrap text-sm text-gray-900'
            
            # Create a new td for status
            new_td = soup.new_tag('td', **{'class': 'px-4 py-3 whitespace-nowrap text-sm text-gray-900'})
            new_td.string = status_text
            
            target_td.insert_after(new_td)

with open('B端_用户管理_XP干预页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Columns split and styled simply.")
