from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tab_task = soup.find('div', id='tab-task')
if tab_task:
    table = tab_task.find('table')
    if table:
        thead = table.find('thead')
        
        # Reset thead
        thead['class'] = ['sticky', 'top-0', 'z-10', 'shadow-sm']
        
        # Ensure every th has bg-gray-50 so it's opaque
        for th in thead.find_all('th'):
            classes = th.get('class', [])
            
            # Remove any sticky/top-0/z-10 from th since they are on thead now
            for c in ['sticky', 'top-0', 'z-10', 'shadow-[0_2px_0_0_#e5e7eb]', 'bg-gray-50']:
                if c in classes:
                    classes.remove(c)
                    
            # Add bg-gray-50 to th to ensure it's not transparent
            classes.append('bg-gray-50')
            th['class'] = classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Applied clean sticky top to thead with opaque th.")
