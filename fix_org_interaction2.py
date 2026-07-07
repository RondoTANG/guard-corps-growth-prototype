from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

charts_grid = soup.find('div', class_=lambda c: c and 'grid-cols-3' in c)

# Create a new full-width container for the Org comparison chart
new_chart_container = soup.new_tag('div', attrs={'class': 'bg-white rounded-lg shadow-sm border border-gray-200 p-5 mt-6 mb-6'})
header = soup.new_tag('div', attrs={'class': 'flex justify-between items-center border-b border-gray-100 pb-3 mb-4'})
title = soup.new_tag('h3', attrs={'class': 'font-bold text-gray-800 text-base'})
title.append("各组织成长健康度排行")
header.append(title)
new_chart_container.append(header)

chart_div = soup.new_tag('div', attrs={'id': 'orgCompareChart', 'class': 'h-80 w-full'})
new_chart_container.append(chart_div)

# Insert it AFTER the first grid of charts
if charts_grid:
    charts_grid.insert_after(new_chart_container)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("New chart added successfully.")
