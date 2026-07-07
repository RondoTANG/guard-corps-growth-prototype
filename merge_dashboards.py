from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup_dashboard = BeautifulSoup(f.read(), 'html.parser')

with open('B端_XP资产流水明细表.html', 'r', encoding='utf-8') as f:
    soup_table = BeautifulSoup(f.read(), 'html.parser')

# We will create a new HTML file taking the layout from the dashboard, 
# but we need to see what's in them first.
