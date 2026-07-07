from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tab_task = soup.find('div', id='tab-task')
if tab_task:
    wrapper = tab_task.find('div', class_=lambda c: c and 'max-h-[calc(100vh-280px)]' in c)
    if wrapper:
        table = wrapper.find('table')
        if table:
            # Restore table borders
            classes = table.get('class', [])
            if 'border' not in classes: classes.append('border')
            if 'border-gray-200' not in classes: classes.append('border-gray-200')
            if 'rounded-lg' not in classes: classes.append('rounded-lg')
            table['class'] = classes
            
            # Unwrap
            wrapper.unwrap()

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Table unwrapped. Reverted to page-level sticky.")
