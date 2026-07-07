import os
import glob
from bs4 import BeautifulSoup

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # We only process files that have the dark sidebar
    if 'bg-[#313C48]' not in html:
        return False
        
    soup = BeautifulSoup(html, 'html.parser')
    aside = soup.find('aside')
    if not aside:
        return False
        
    # 1. Update aside classes
    aside['class'] = [c for c in aside.get('class', []) if c not in ('bg-[#313C48]', 'text-[#909399]')]
    aside['class'].extend(['bg-white', 'text-gray-600', 'border-r', 'border-gray-200'])
    
    # 2. Update header
    header = aside.find('div', class_='bg-[#2B3643]')
    if header:
        header['class'] = [c for c in header.get('class', []) if c != 'bg-[#2B3643]']
        header['class'].extend(['bg-white', 'border-b', 'border-gray-100'])
        span = header.find('span', class_='text-white')
        if span:
            span['class'] = [c for c in span.get('class', []) if c != 'text-white']
            span['class'].extend(['text-gray-900'])
            
            # Add the red '东' logo to match B端_作业管理列表.html
            logo_div = soup.new_tag('div')
            logo_div['class'] = "w-8 h-8 rounded-full bg-gradient-to-br from-red-500 to-dfred flex items-center justify-center text-white font-bold mr-3"
            logo_div.string = "东"
            span.insert_before(logo_div)

    # 3. Update menu groups
    for group in aside.find_all('div', class_='menu-group'):
        # Title div
        title_div = group.find('div', class_='hover:text-white')
        if title_div:
            title_div['class'] = [c for c in title_div.get('class', []) if c != 'hover:text-white']
            title_div['class'].extend(['hover:bg-gray-50'])
            span = title_div.find('span', class_='text-gray-200')
            if span:
                span['class'] = [c for c in span.get('class', []) if c != 'text-gray-200']
                span['class'].append('text-gray-800')

        # Links
        links_container = group.find('div', class_='flex-col')
        if links_container:
            for a in links_container.find_all('a'):
                classes = a.get('class', [])
                
                # Remove dark theme classes
                classes = [c for c in classes if c not in ('hover:text-white', 'text-white', 'bg-[#3B82F6]')]
                
                if 'active-menu' in classes:
                    # Apply light theme active classes
                    classes.extend(['bg-blue-50/80', 'text-dfblue', 'border-r-2', 'border-dfblue'])
                else:
                    # Apply light theme normal classes
                    classes.extend(['hover:bg-gray-50', 'hover:text-dfblue', 'text-gray-600'])
                
                a['class'] = classes

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    return True

changed = 0
for filepath in glob.glob('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_*.html'):
    if process_html(filepath):
        print(f"Updated sidebar in {filepath}")
        changed += 1

print(f"Total files updated: {changed}")
