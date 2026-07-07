from bs4 import BeautifulSoup
import re

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find all tables
tables = soup.find_all('table', class_=lambda c: c and 'min-w-full' in c)

if len(tables) >= 2:
    table_anomaly = tables[0]
    table_xp = tables[1]
    
    # -----------------------------
    # 1. FIX ANOMALY TABLE
    # -----------------------------
    thead_anomaly = table_anomaly.find('thead')
    if thead_anomaly:
        tr = thead_anomaly.find('tr')
        tr.clear()
        headers_anomaly = ['用户信息', '原段位', '新段位', '异常原因', '发生时间', '操作']
        for h in headers_anomaly:
            th = soup.new_tag('th', scope='col', attrs={'class': 'px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'})
            th.string = h
            tr.append(th)
            
    tbody_anomaly = table_anomaly.find('tbody')
    if tbody_anomaly:
        tbody_anomaly.clear()
        anomaly_data = [
            {
                'user': '<div class="flex items-center"><img class="h-8 w-8 rounded-full" src="https://ui-avatars.com/api/?name=赵六&background=random"><div class="ml-3"><div class="text-sm font-medium text-gray-900">赵六 (ID:8841)</div></div></div>',
                'old_tier': '<span class="text-gray-500">熟练护卫军</span>',
                'new_tier': '<span class="text-yellow-600 font-bold">大师护卫军</span>',
                'reason': '<span class="text-red-600 bg-red-50 px-2 py-1 rounded text-xs">单日连跨两级，触发预警阀门</span>',
                'time': '2023-10-24 16:20:00',
                'action': '<button class="text-blue-600 hover:text-blue-800 text-sm font-medium">查看作业流水</button>'
            },
            {
                'user': '<div class="flex items-center"><img class="h-8 w-8 rounded-full" src="https://ui-avatars.com/api/?name=钱七&background=random"><div class="ml-3"><div class="text-sm font-medium text-gray-900">钱七 (ID:3321)</div></div></div>',
                'old_tier': '<span class="text-yellow-600 font-bold">专家护卫军</span>',
                'new_tier': '<span class="text-gray-500">实习护卫军</span>',
                'reason': '<span class="text-red-600 bg-red-50 px-2 py-1 rounded text-xs">人工介入：查实刷单行为，强制降级</span>',
                'time': '2023-10-23 09:15:22',
                'action': '<button class="text-blue-600 hover:text-blue-800 text-sm font-medium">查看处罚记录</button>'
            }
        ]
        
        for row in anomaly_data:
            tr = soup.new_tag('tr', attrs={'class': 'hover:bg-gray-50'})
            for key in ['user', 'old_tier', 'new_tier', 'reason', 'time', 'action']:
                td = soup.new_tag('td', attrs={'class': 'px-6 py-4 whitespace-nowrap text-sm'})
                if key in ['user', 'old_tier', 'new_tier', 'reason', 'action']:
                    td.append(BeautifulSoup(row[key], 'html.parser'))
                else:
                    td.string = row[key]
                tr.append(td)
            tbody_anomaly.append(tr)

    # -----------------------------
    # 2. FIX XP FLOW TABLE
    # -----------------------------
    thead_xp = table_xp.find('thead')
    if thead_xp:
        tr = thead_xp.find('tr')
        tr.clear()
        headers_xp = ['流水号', '发生时间', '用户名称', '用户ID', '手机号', '业务类型', '详细描述', '变动额度', '变动后余额', '特殊标记']
        for h in headers_xp:
            th = soup.new_tag('th', scope='col', attrs={'class': 'px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'})
            th.string = h
            tr.append(th)
            
    tbody_xp = table_xp.find('tbody')
    if tbody_xp:
        tbody_xp.clear()
        rows_data = [
            {
                'name': '张三', 'uid': '10086', 'phone': '138****1234',
                'type': '作业产出', 'desc': '完成原创试驾作业（知乎平台）',
                'amount_html': '<span class="text-green-600 font-bold">+100</span>',
                'balance': '1,450',
                'mark_html': '<span class="text-gray-400">-</span>'
            },
            {
                'name': '李四', 'uid': '10245', 'phone': '139****5678',
                'type': '作业产出', 'desc': '完成日常互动转发（微信视频号）',
                'amount_html': '<span class="text-green-600 font-bold">+10</span><span class="text-gray-400 line-through text-xs ml-1">(原应发: 20)</span>',
                'balance': '2,800',
                'mark_html': '<span class="text-red-600 text-xs font-medium"><i class="fas fa-shield-alt mr-1"></i>已达上限，超额截断</span>'
            },
            {
                'name': '王五', 'uid': '9952', 'phone': '137****9012',
                'type': '到期扣除', 'desc': '12个月前历史XP自动过期失效',
                'amount_html': '<span class="text-gray-600 font-bold">-150</span>',
                'balance': '350',
                'mark_html': '<span class="text-gray-400">-</span>'
            }
        ]
        
        for i in range(10):
            row = rows_data[i % len(rows_data)]
            tr = soup.new_tag('tr', attrs={'class': 'hover:bg-gray-50'})
            
            def make_td(content, is_html=False):
                td = soup.new_tag('td', attrs={'class': 'px-6 py-4 whitespace-nowrap text-sm text-gray-900'})
                if is_html:
                    td.append(BeautifulSoup(content, 'html.parser'))
                else:
                    td.string = content
                return td

            rid = f"TX_20231024_889{i+1}"
            rtime = f"2023-10-24 14:{30+i}:22"

            tr.append(make_td(rid))
            tr.append(make_td(rtime))
            tr.append(make_td(row['name']))
            tr.append(make_td(row['uid']))
            tr.append(make_td(row['phone']))
            
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
            
            tbody_xp.append(tr)

    # 3. FIX THE PAGINATION FOR XP FLOW TABLE
    # Ensure XP flow table has the right pagination text
    xp_section = table_xp.find_parent('div', class_=lambda c: c and 'bg-white' in c and 'border-gray-200' in c)
    if xp_section:
        for p in xp_section.find_all('p', class_='text-sm text-gray-700'):
            if '显示第' in p.text:
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

print("Both tables successfully fixed.")
