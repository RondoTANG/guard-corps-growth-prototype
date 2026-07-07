from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the heading "段位变动异常监控"
heading = soup.find('h3', string='段位变动异常监控')
if heading:
    # The heading is likely inside a container div (bg-white border rounded etc)
    # Let's find its parent container and remove the whole block
    container = heading.find_parent('div', class_=lambda c: c and 'bg-white' in c and 'border' in c)
    if container:
        container.decompose()

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Removed anomaly table.")
