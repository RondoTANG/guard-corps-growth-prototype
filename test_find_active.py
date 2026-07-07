import glob
from bs4 import BeautifulSoup

for filepath in glob.glob('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_*.html'):
    if '新建作业' in filepath: continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    aside = soup.find('aside')
    if not aside:
        print(f"No aside in {filepath}")
        continue
    
    active_menu = aside.find('a', class_=lambda x: x and ('active-menu' in x or 'border-blue-600' in x))
    if active_menu:
        print(f"{filepath}: ACTIVE MENU -> {active_menu.get_text(strip=True)}")
    else:
        print(f"{filepath}: NO ACTIVE MENU FOUND")
