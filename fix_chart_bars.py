from bs4 import BeautifulSoup
import re

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Fix the Tooltip for the bar chart
bar_chart_title_container = soup.find('div', class_=lambda c: c and 'cursor-help' in c)
if bar_chart_title_container:
    tooltip = bar_chart_title_container.find('div', class_=lambda c: c and 'absolute' in c)
    if tooltip:
        # Update tooltip content
        tooltip.clear()
        tooltip.append(BeautifulSoup('<b>统计规则：</b><br/>• <b>任务参与率</b> = 该段位提交过作业的用户数 / 该段位总用户数<br/>• <b>作业通过率</b> = 该段位审核通过的作业数 / 该段位提交的总作业数', 'html.parser'))
        arrow = soup.new_tag('div', attrs={'class': 'absolute left-4 bottom-full w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800'})
        tooltip.append(arrow)

# 2. Fix the Legend
legend_blue = soup.find('span', string=re.compile('作业通过率'))
if legend_blue:
    legend_blue.string = '任务参与率'
    
legend_orange = soup.find('span', string=re.compile('评优率|加码'))
if legend_orange:
    legend_orange.string = '作业通过率'

# 3. Fix the Bar Chart Values and Hover Titles
# Let's adjust the orange bar values to make sense for "Pass Rate" (should be high)
# And blue bar values for "Participation Rate" (should increase with tier)
bar_chart_container = soup.find('div', class_=lambda c: c and 'h-48' in c and 'flex' in c and 'items-end' in c)
if bar_chart_container:
    cols = bar_chart_container.find_all('div', class_=lambda c: c and 'flex-col' in c and 'items-center' in c and 'group' in c)
    # 4 cols for 新秀, 熟练, 专家, 大师
    new_values = [
        {'blue': '35%', 'orange': '65%'}, # 新秀: Low participation, Ok pass rate
        {'blue': '55%', 'orange': '82%'}, # 熟练: Med participation, Good pass rate
        {'blue': '85%', 'orange': '91%'}, # 专家: High participation, High pass rate
        {'blue': '98%', 'orange': '98%'}, # 大师: Very high participation, Very high pass rate
    ]
    
    for i, col in enumerate(cols):
        if i < len(new_values):
            bars = col.find_all('div', class_=lambda c: c and ('bg-blue-500' in c or 'bg-orange-500' in c))
            if len(bars) == 2:
                # Blue bar (Participation Rate)
                blue_bar = bars[0]
                blue_bar['style'] = f"height: {new_values[i]['blue']};"
                blue_bar['title'] = f"参与率: {new_values[i]['blue']}"
                span_b = blue_bar.find('span')
                if span_b:
                    span_b.string = new_values[i]['blue']
                
                # Orange bar (Pass Rate)
                orange_bar = bars[1]
                orange_bar['style'] = f"height: {new_values[i]['orange']};"
                orange_bar['title'] = f"通过率: {new_values[i]['orange']}"
                span_o = orange_bar.find('span')
                if span_o:
                    span_o.string = new_values[i]['orange']

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Bar chart updated to Participation vs Pass Rate")
