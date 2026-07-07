from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the specific table for XP mapping
tab_task = soup.find('div', id='tab-task')
if tab_task:
    table = tab_task.find('table')
    if table:
        thead = table.find('thead')
        if 'sticky' in thead.get('class', []):
            thead['class'].remove('sticky')
        if 'top-0' in thead.get('class', []):
            thead['class'].remove('top-0')
        if 'z-10' in thead.get('class', []):
            thead['class'].remove('z-10')
        if 'shadow-sm' in thead.get('class', []):
            thead['class'].remove('shadow-sm')
            
        # Apply sticky to the th elements
        for th in thead.find_all('th'):
            classes = th.get('class', [])
            if 'sticky' not in classes:
                classes.extend(['sticky', 'top-0', 'z-10', 'bg-gray-50', 'shadow-[0_2px_0_0_#e5e7eb]'])
            # remove border-b-2 to avoid double border weirdness with shadow
            if 'border-b-2' in classes:
                classes.remove('border-b-2')
            if 'border-gray-200' in classes:
                classes.remove('border-gray-200')
                
            th['class'] = classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed sticky header.")
