from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tab_task = soup.find('div', id='tab-task')
if tab_task:
    table = tab_task.find('table')
    if table:
        # Check if it's already wrapped in our specific div
        parent = table.parent
        if 'max-h-[600px]' not in parent.get('class', []):
            # Create wrapper
            wrapper = soup.new_tag('div', **{'class': 'border border-gray-200 rounded-lg overflow-x-auto overflow-y-auto max-h-[calc(100vh-280px)] shadow-sm'})
            
            # Remove border from table to prevent double borders
            table_classes = table.get('class', [])
            if 'border' in table_classes: table_classes.remove('border')
            if 'border-gray-200' in table_classes: table_classes.remove('border-gray-200')
            if 'rounded-lg' in table_classes: table_classes.remove('rounded-lg')
            table['class'] = table_classes
            
            # Make sure th has proper sticky classes
            for th in table.find('thead').find_all('th'):
                classes = th.get('class', [])
                if 'sticky' not in classes:
                    classes.extend(['sticky', 'top-0', 'z-10', 'bg-gray-50'])
                # Make sure top-0 is there, not top-[-1px] or anything else
                th['class'] = classes
            
            table.wrap(wrapper)

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Table wrapped for correct sticky behavior.")
