import os
import glob
from bs4 import BeautifulSoup

def process_html(filepath):
    # Skip the files that already use the custom sidebar or no sidebar
    if '作业管理列表' in filepath or '新建作业' in filepath:
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    menu_groups = soup.find_all('div', class_='menu-group')
    if not menu_groups:
        return False
        
    changed = False
    
    for group in menu_groups:
        # Check if active menu exists inside this group
        is_active_group = group.find('a', class_='active-menu') is not None
        
        # The first div inside menu-group is the header
        header_div = group.find('div', class_=lambda x: x and 'justify-between' in x)
        # The second div is the sub-menu container
        sub_menu = group.find('div', class_='flex-col')
        
        if not header_div or not sub_menu:
            continue
            
        span = header_div.find('span')
        icon = header_div.find('i')
        
        if is_active_group:
            # Expand and highlight
            # 1. Background for header
            header_classes = header_div.get('class', [])
            if 'bg-blue-50/50' not in header_classes:
                header_classes.append('bg-blue-50/50')
                header_div['class'] = header_classes
                changed = True
                
            # 2. Text color for span
            if span:
                span_classes = span.get('class', [])
                if 'text-gray-800' in span_classes:
                    span_classes.remove('text-gray-800')
                if 'text-dfblue' not in span_classes:
                    span_classes.append('text-dfblue')
                span['class'] = span_classes
                changed = True
                
            # 3. Icon color and direction
            if icon:
                icon_classes = icon.get('class', [])
                if 'fa-chevron-down' in icon_classes:
                    icon_classes.remove('fa-chevron-down')
                    icon_classes.append('fa-chevron-up')
                if 'text-gray-400' in icon_classes:
                    icon_classes.remove('text-gray-400')
                if 'text-dfblue' not in icon_classes:
                    icon_classes.append('text-dfblue')
                icon['class'] = icon_classes
                changed = True
                
            # 4. Ensure sub_menu is visible
            sub_classes = sub_menu.get('class', [])
            if 'hidden' in sub_classes:
                sub_classes.remove('hidden')
                sub_menu['class'] = sub_classes
                changed = True
                
        else:
            # Collapse and remove highlight
            # 1. Background
            header_classes = header_div.get('class', [])
            if 'bg-blue-50/50' in header_classes:
                header_classes.remove('bg-blue-50/50')
                header_div['class'] = header_classes
                changed = True
                
            # 2. Span color
            if span:
                span_classes = span.get('class', [])
                if 'text-dfblue' in span_classes:
                    span_classes.remove('text-dfblue')
                if 'text-gray-800' not in span_classes:
                    span_classes.append('text-gray-800')
                span['class'] = span_classes
                changed = True
                
            # 3. Icon color and direction
            if icon:
                icon_classes = icon.get('class', [])
                if 'fa-chevron-up' in icon_classes:
                    icon_classes.remove('fa-chevron-up')
                    icon_classes.append('fa-chevron-down')
                if 'text-dfblue' in icon_classes:
                    icon_classes.remove('text-dfblue')
                if 'text-gray-400' not in icon_classes:
                    icon_classes.append('text-gray-400')
                icon['class'] = icon_classes
                changed = True
                
            # 4. Collapse sub_menu
            sub_classes = sub_menu.get('class', [])
            if 'hidden' not in sub_classes:
                sub_classes.append('hidden')
                sub_menu['class'] = sub_classes
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

changed_count = 0
for filepath in glob.glob('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_*.html'):
    if process_html(filepath):
        print(f"Collapsed menus in {filepath}")
        changed_count += 1

print(f"Total files updated: {changed_count}")
