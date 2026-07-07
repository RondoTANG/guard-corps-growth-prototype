from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tab_task = soup.find('div', id='tab-task')
if tab_task:
    table = tab_task.find('table')
    if table:
        thead = table.find('thead')
        
        # Add border/outline to thead to make it look like a cohesive box when it floats
        thead['class'] = ['sticky', 'top-0', 'z-10', 'shadow-sm', 'outline', 'outline-1', 'outline-gray-200', 'bg-gray-50']
        
        for th in thead.find_all('th'):
            classes = th.get('class', [])
            if 'bg-gray-50' not in classes:
                classes.append('bg-gray-50')
            th['class'] = classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Applied outline and bg to sticky header.")
