from bs4 import BeautifulSoup

with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Update the JS to query 'org-tree-sidebar'
for script in soup.find_all('script'):
    if script.string and 'document.addEventListener(\'DOMContentLoaded\'' in script.string and 'orgCompareChart' in script.string:
        # Fix the bug where b.closest('.flex') returns the checkbox itself
        script.string = script.string.replace("b.closest('.flex')", "b.parentElement")
        # Ensure we use textContent instead of innerText
        script.string = script.string.replace("innerText", "textContent")

with open('B端_完整后台大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
# Keep both files in sync
with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed parentElement bug.")
