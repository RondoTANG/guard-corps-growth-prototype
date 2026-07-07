from bs4 import BeautifulSoup
import glob

# Process all B-end HTML files
for filename in glob.glob('B端_*.html'):
    if 'B端_成长数据健康度大盘.html' == filename:
        continue # Already processed in previous step
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    # Find all menu links
    for a in soup.find_all('a', class_=lambda c: c and 'menu-link' in c or 'transition-colors' in c):
        if 'XP资产流水' in a.text or 'B端_XP资产流水明细表.html' in a.get('href', ''):
            a.decompose()
            modified = True
            
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated menu in {filename}")

