from bs4 import BeautifulSoup

with open('C端_护卫军后台功能导航页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find Card 1: 成长数据大盘 and update it
for a in soup.find_all('a'):
    if 'B端_成长数据健康度大盘.html' in a.get('href', ''):
        h2 = a.find('h2')
        if h2:
            h2.string = '大盘数据与XP资产流水'
        p = a.find('p')
        if p:
            p.string = '护卫军全盘宏观数据监控，以及全局XP产出与消耗明细对账审计。'

# Find Card 4: XP 资产流水 and remove it
for a in soup.find_all('a'):
    if 'B端_XP资产流水明细表.html' in a.get('href', ''):
        a.decompose()

with open('C端_护卫军后台功能导航页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Updated navigation page.")
