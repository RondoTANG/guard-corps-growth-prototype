from bs4 import BeautifulSoup

with open('B端_用户管理_XP干预页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Update Header
for th in soup.find_all('th'):
    if th.string and '当前段位' in th.string:
        th.string = '当前段位 & 定级状态'

# 2. Update Rows
tbody = soup.find('tbody')
if tbody:
    rows = tbody.find_all('tr')
    for i, tr in enumerate(rows):
        tds = tr.find_all('td')
        if len(tds) > 18:
            level_td = tds[17]
            
            # Wrap the existing level span inside a flex container
            old_span = level_td.find('span')
            if old_span:
                # Decide status based on row index to show different states
                status_html = ""
                if i % 3 == 0:
                    # e.g., Row 1: Level 4, 12450 XP (Below 20k) -> Grace Period
                    status_html = '<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-orange-50 text-orange-700 border border-orange-200 mt-1 inline-block">保级缓冲期</span>'
                elif i % 3 == 1:
                    # e.g., Row 2: Level 2, 1450 XP (Normal)
                    status_html = '<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-green-50 text-green-700 border border-green-200 mt-1 inline-block">正常 (XP达标)</span>'
                else:
                    # e.g., Row 3: Level 2, 0 XP (Bottom line)
                    status_html = '<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-purple-50 text-purple-700 border border-purple-200 mt-1 inline-block">荣誉保底</span>'

                # Create new container
                wrapper = soup.new_tag('div')
                wrapper['class'] = 'flex flex-col items-start'
                
                # Extract old span and put into wrapper
                old_span_extracted = old_span.extract()
                wrapper.append(old_span_extracted)
                
                # Append status
                status_soup = BeautifulSoup(status_html, 'html.parser')
                wrapper.append(status_soup)
                
                level_td.append(wrapper)

with open('B端_用户管理_XP干预页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("User status updated successfully.")
