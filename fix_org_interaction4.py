from bs4 import BeautifulSoup

with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Change chart title
for h3 in soup.find_all('h3'):
    if h3.string == '各组织成长健康度排行':
        h3.string = '各党组织活跃与段位分布对比'

with open('B端_完整后台大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Title updated.")
