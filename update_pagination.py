from bs4 import BeautifulSoup
import copy

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

table = soup.find('table', class_='min-w-full divide-y divide-gray-200')
if table:
    tbody = table.find('tbody')
    if tbody:
        rows = tbody.find_all('tr', recursive=False)
        if len(rows) > 0:
            # We want exactly 10 rows
            target_count = 10
            current_count = len(rows)
            
            # Use the first row as template for duplicating
            template_row = rows[0]
            
            for i in range(current_count, target_count):
                new_row = copy.copy(template_row)
                # Slightly alter ID and time just for some variation
                tds = new_row.find_all('td')
                if len(tds) > 0:
                    tds[0].string = f"TX_20231024_889{i+3}"
                    tds[1].string = f"2023-10-24 14:{30+i}:22"
                tbody.append(new_row)

# Find pagination text and update
# Look for text like "显示第 1 到 3 条数据"
for p in soup.find_all('p', class_='text-sm text-gray-700'):
    if '显示第' in p.text and '条数据' in p.text:
        # Rebuild the string
        p.clear()
        p.append("显示第 ")
        span1 = soup.new_tag('span', attrs={'class': 'font-medium'})
        span1.string = "1"
        p.append(span1)
        p.append(" 到 ")
        span2 = soup.new_tag('span', attrs={'class': 'font-medium'})
        span2.string = "10"
        p.append(span2)
        p.append(" 条数据，共 ")
        span3 = soup.new_tag('span', attrs={'class': 'font-medium'})
        span3.string = "24,582"
        p.append(span3)
        p.append(" 条")
        break

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Rows expanded to 10 and pagination updated.")
