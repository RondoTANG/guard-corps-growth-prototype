from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for tab_id in ['tab-tier', 'tab-global', 'tab-task']:
    tab = soup.find('div', id=tab_id)
    if tab:
        # Add padding bottom to the tab content so it doesn't get obscured by the fixed footer
        tab['class'] = tab.get('class', []) + ['pb-24']
        
        # Find the bottom bar
        # In the previous script I changed it to block: 'rounded-b-lg', 'border', 'shadow-sm', 'mt-8', 'p-4'
        bottom_bar = tab.find('div', class_=lambda c: c and 'rounded-b-lg' in c and 'shadow-sm' in c)
        if bottom_bar:
            classes = bottom_bar.get('class', [])
            # Remove old classes
            for c in ['rounded-b-lg', 'border', 'shadow-sm', 'mt-8', 'p-4', '-mx-6', '-mb-6']:
                if c in classes:
                    classes.remove(c)
            # Add fixed styling
            classes.extend([
                'fixed', 'bottom-0', 'right-0', 'left-64',
                'bg-white', 'border-t', 'border-gray-200', 'px-8', 'py-4',
                'flex', 'items-center', 'justify-between',
                'z-[45]', 'shadow-[0_-5px_15px_-3px_rgba(0,0,0,0.05)]'
            ])
            bottom_bar['class'] = classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed bars applied.")
