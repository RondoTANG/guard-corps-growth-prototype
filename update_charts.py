from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Add Tooltip for "不同段位作业转化质量对比"
bar_chart_title = soup.find('h3', string='不同段位作业转化质量对比')
if bar_chart_title:
    # Wrap in a flex container if not already
    parent = bar_chart_title.parent
    if 'flex' not in parent.get('class', []):
        parent['class'] = parent.get('class', []) + ['flex', 'items-center', 'justify-between']
    
    # Check if tooltip already exists
    if not bar_chart_title.find('i'):
        # Make the h3 itself a flex container for the title and icon
        bar_chart_title.string = ''
        
        container = soup.new_tag('div', attrs={'class': 'flex items-center group cursor-help relative'})
        container.append("不同段位作业转化质量对比")
        
        icon = soup.new_tag('i', attrs={'class': 'far fa-question-circle text-gray-300 ml-1 hover:text-gray-500 transition-colors text-xs'})
        container.append(icon)
        
        # Tooltip content
        tooltip = soup.new_tag('div', attrs={'class': 'absolute left-0 top-full mt-2 hidden group-hover:block w-72 bg-gray-800 text-white text-xs rounded p-2 z-50 shadow-lg font-normal'})
        tooltip.append(BeautifulSoup('<b>统计规则：</b><br/>• <b>作业通过率</b> = 审核通过的作业数 / 该段位提交的总作业数<br/>• <b>评优率(加码)</b> = 获得加码奖励(评优)的作业数 / 审核通过的作业数', 'html.parser'))
        # Arrow
        arrow = soup.new_tag('div', attrs={'class': 'absolute left-4 bottom-full w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800'})
        tooltip.append(arrow)
        
        container.append(tooltip)
        bar_chart_title.append(container)


# 2. Add fixed percentage labels to Pie Chart 1
# Find the div with the conic-gradient style
pie1 = None
for div in soup.find_all('div', class_=lambda c: c and 'rounded-full' in c and 'w-48' in c and 'h-48' in c):
    style = div.get('style', '')
    if '9ca3af' in style and '3b82f6' in style: # Level pie
        pie1 = div
        break

if pie1:
    # It must be relative to position the labels
    if 'relative' not in pie1.get('class', []):
        pie1['class'] = pie1.get('class', []) + ['relative']
    
    # Remove existing labels if any
    for span in pie1.find_all('span'):
        span.decompose()

    labels_html = """
    <span class="absolute text-gray-600 font-bold text-sm" style="top: 65%; left: 75%; transform: translate(-50%, -50%);" title="新秀: 65%">65%</span>
    <span class="absolute text-blue-100 font-bold text-sm" style="top: 45%; left: 15%; transform: translate(-50%, -50%);" title="熟练: 25%">25%</span>
    <span class="absolute text-purple-800 font-bold text-xs" style="top: 10%; left: 35%; transform: translate(-50%, -50%);" title="专家: 7%">7%</span>
    <span class="absolute text-red-800 font-bold text-xs" style="top: 5%; left: 52%; transform: translate(-50%, -50%);" title="大师: 3%">3%</span>
    """
    pie1.append(BeautifulSoup(labels_html, 'html.parser'))

# 3. Add fixed percentage labels to Pie Chart 2
pie2 = None
for div in soup.find_all('div', class_=lambda c: c and 'rounded-full' in c and 'w-48' in c and 'h-48' in c):
    style = div.get('style', '')
    if '3b82f6' in style and 'f59e0b' in style: # Status pie
        pie2 = div
        break

if pie2:
    if 'relative' not in pie2.get('class', []):
        pie2['class'] = pie2.get('class', []) + ['relative']
    
    for span in pie2.find_all('span'):
        span.decompose()

    labels_html2 = """
    <span class="absolute text-blue-100 font-bold text-sm" style="top: 60%; left: 60%; transform: translate(-50%, -50%);" title="正常段位: 85%">85%</span>
    <span class="absolute text-yellow-900 font-bold text-xs" style="top: 15%; left: 25%; transform: translate(-50%, -50%);" title="保级缓冲期: 12%">12%</span>
    <span class="absolute text-red-900 font-bold text-[10px]" style="top: 5%; left: 45%; transform: translate(-50%, -50%);" title="荣誉保底: 3%">3%</span>
    """
    pie2.append(BeautifulSoup(labels_html2, 'html.parser'))

# 4. Make sure bar chart labels have hover title as well
bar_chart_container = soup.find('div', class_=lambda c: c and 'h-48' in c and 'flex' in c and 'items-end' in c)
if bar_chart_container:
    bars = bar_chart_container.find_all('div', class_=lambda c: c and ('bg-blue-500' in c or 'bg-orange-500' in c))
    for bar in bars:
        span = bar.find('span')
        if span:
            val = span.text
            # Add title to the bar itself
            bar['title'] = f"数值: {val}"
            # Add hover effect
            classes = bar.get('class', [])
            if 'hover:opacity-80' not in classes:
                classes.append('hover:opacity-80')
            if 'cursor-pointer' not in classes:
                classes.append('cursor-pointer')
            bar['class'] = classes

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Chart labels and tooltips updated.")
