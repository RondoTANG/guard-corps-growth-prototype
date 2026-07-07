from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the aside
aside = soup.find('aside')
if aside:
    # Remove any tables inside aside
    for table in aside.find_all('table'):
        table.decompose()
    # Remove any div that looks like a filter bar or table container in aside
    for div in aside.find_all('div', class_=lambda c: c and 'bg-white' in c and 'border-gray-200' in c):
        div.decompose()
    # Remove the h2 'XP资产流水明细' in aside
    for h2 in aside.find_all('h2', string='XP资产流水明细'):
        if h2.parent:
            h2.parent.decompose()

# Now update the remaining table (which is the correct one in main)
table = soup.find('table', class_='min-w-full divide-y divide-gray-200')
if table:
    # Update thead
    thead = table.find('thead')
    if thead:
        tr = thead.find('tr')
        tr.clear()
        
        headers = [
            '流水号', '发生时间', '用户名称', '用户ID', '手机号', '业务类型', '详细描述', '变动额度', '变动后余额', '特殊标记'
        ]
        
        for h in headers:
            th = soup.new_tag('th', scope='col', attrs={'class': 'px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'})
            th.string = h
            tr.append(th)

    # Update tbody
    tbody = table.find('tbody')
    if tbody:
        tbody.clear()
        
        rows_data = [
            {
                'id': 'TX_20231024_8891', 'time': '2023-10-24 14:30:22',
                'name': '张三', 'uid': '10086', 'phone': '138****1234',
                'type': '作业产出', 'desc': '完成原创试驾作业（知乎平台）',
                'amount_html': '<span class="text-green-600 font-bold">+100</span>',
                'balance': '1,450',
                'mark_html': '<span class="text-gray-400">-</span>'
            },
            {
                'id': 'TX_20231024_8892', 'time': '2023-10-24 15:10:05',
                'name': '李四', 'uid': '10245', 'phone': '139****5678',
                'type': '作业产出', 'desc': '完成日常互动转发（微信视频号）',
                'amount_html': '<span class="text-green-600 font-bold">+10</span><span class="text-gray-400 line-through text-xs ml-1">(原应发: 20)</span>',
                'balance': '2,800',
                'mark_html': '<span class="text-red-600 text-xs font-medium"><i class="fas fa-shield-alt mr-1"></i>已达上限，超额截断</span>'
            },
            {
                'id': 'TX_20231025_0012', 'time': '2023-10-25 09:00:00',
                'name': '王五', 'uid': '9952', 'phone': '137****9012',
                'type': '到期扣除', 'desc': '12个月前历史XP自动过期失效',
                'amount_html': '<span class="text-gray-600 font-bold">-150</span>',
                'balance': '350',
                'mark_html': '<span class="text-gray-400">-</span>'
            }
        ]
        
        # We need 10 rows
        for i in range(10):
            row = rows_data[i % len(rows_data)]
            tr = soup.new_tag('tr', attrs={'class': 'hover:bg-gray-50'})
            
            # Helper to create td
            def make_td(content, is_html=False):
                td = soup.new_tag('td', attrs={'class': 'px-6 py-4 whitespace-nowrap text-sm text-gray-900'})
                if is_html:
                    td.append(BeautifulSoup(content, 'html.parser'))
                else:
                    td.string = content
                return td

            # Modify ID/Time for unique rows
            rid = f"TX_20231024_889{i+1}"
            rtime = f"2023-10-24 14:{30+i}:22"

            tr.append(make_td(rid))
            tr.append(make_td(rtime))
            tr.append(make_td(row['name']))
            tr.append(make_td(row['uid']))
            tr.append(make_td(row['phone']))
            
            # Business Type
            td_type = soup.new_tag('td', attrs={'class': 'px-6 py-4 whitespace-nowrap text-sm'})
            span = soup.new_tag('span', attrs={'class': 'px-2 py-1 text-xs font-medium rounded bg-gray-100 text-gray-800'})
            if '产出' in row['type']:
                span['class'] = 'px-2 py-1 text-xs font-medium rounded bg-green-100 text-green-800'
            span.string = row['type']
            td_type.append(span)
            tr.append(td_type)
            
            tr.append(make_td(row['desc']))
            tr.append(make_td(row['amount_html'], is_html=True))
            tr.append(make_td(row['balance']))
            tr.append(make_td(row['mark_html'], is_html=True))
            
            tbody.append(tr)

# Fix pagination text again just in case
for p in soup.find_all('p', class_='text-sm text-gray-700'):
    if '显示第' in p.text and '条数据' in p.text:
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

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed leftover table in sidebar and updated the main table.")
