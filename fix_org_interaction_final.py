from bs4 import BeautifulSoup
import re

with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Fix the duplicate ID issue!
# Change the ID of the real sidebar to org-tree-sidebar
white_sidebar = soup.find('div', class_=lambda c: c and 'w-64' in c and 'bg-white' in c and 'border-r' in c)
if white_sidebar:
    white_sidebar['id'] = 'org-tree-sidebar'

# Update the JS to query 'org-tree-sidebar'
for script in soup.find_all('script'):
    if script.string and 'document.addEventListener(\'DOMContentLoaded\'' in script.string and 'orgCompareChart' in script.string:
        script.string = script.string.replace("getElementById('org-sidebar')", "getElementById('org-tree-sidebar')")

with open('B端_完整后台大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
# Keep both files in sync
with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed duplicate ID bug.")
