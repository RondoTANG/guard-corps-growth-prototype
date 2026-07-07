import os
import glob
from bs4 import BeautifulSoup

source_file = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html'
with open(source_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

aside = soup.find('aside')

# We need to add "作业管理" to "护卫军作业管理" group if it's missing
nav = aside.find('nav')
hwj_group = None
for group in nav.find_all('div', class_='menu-group'):
    span = group.find('span')
    if span and '护卫军作业管理' in span.get_text():
        hwj_group = group
        break

if hwj_group:
    submenu = hwj_group.find('div', class_='flex-col')
    if submenu:
        # Check if 作业管理 exists
        if not any('作业管理' == a.get_text(strip=True) for a in submenu.find_all('a')):
            new_a = soup.new_tag('a', href='B端_作业管理列表.html')
            new_a.string = '作业管理'
            new_a['class'] = ['px-9', 'py-2.5', 'transition-colors', 'menu-link', 'hover:bg-gray-50', 'hover:text-dfblue', 'text-gray-600']
            submenu.insert(0, new_a)

# Clean up all active states and make everything collapsed by default
for group in aside.find_all('div', class_='menu-group'):
    header = group.find('div', class_=lambda x: x and 'justify-between' in x)
    submenu = group.find('div', class_='flex-col')
    
    if header:
        # Remove active background
        classes = header.get('class', [])
        if 'bg-blue-50/50' in classes: classes.remove('bg-blue-50/50')
        header['class'] = classes
        
        span = header.find('span')
        if span:
            span_classes = span.get('class', [])
            if 'text-dfblue' in span_classes: span_classes.remove('text-dfblue')
            if 'text-gray-800' not in span_classes: span_classes.append('text-gray-800')
            span['class'] = span_classes
            
        icon = header.find('i')
        if icon:
            icon_classes = icon.get('class', [])
            if 'text-dfblue' in icon_classes: icon_classes.remove('text-dfblue')
            if 'text-gray-400' not in icon_classes: icon_classes.append('text-gray-400')
            if 'fa-chevron-up' in icon_classes: 
                icon_classes.remove('fa-chevron-up')
                icon_classes.append('fa-chevron-down')
            icon['class'] = icon_classes
            
    if submenu:
        # Hide all submenus
        sub_classes = submenu.get('class', [])
        if 'hidden' not in sub_classes: sub_classes.append('hidden')
        submenu['class'] = sub_classes
        
        # Remove active states from links
        for a in submenu.find_all('a'):
            a_classes = a.get('class', [])
            for c in ['active-menu', 'bg-blue-50/80', 'text-dfblue', 'border-r-2', 'border-dfblue']:
                if c in a_classes: a_classes.remove(c)
            if 'hover:bg-gray-50' not in a_classes: a_classes.append('hover:bg-gray-50')
            if 'hover:text-dfblue' not in a_classes: a_classes.append('hover:text-dfblue')
            if 'text-gray-600' not in a_classes: a_classes.append('text-gray-600')
            a['class'] = a_classes

aside_html = str(aside).replace('`', '\\`')

js_content = f"""
const B_SIDEBAR_HTML = `
{aside_html}
`;

function initBSidebar(activeMenuName) {{
    const container = document.getElementById('b-sidebar-container');
    if (!container) return;
    
    container.innerHTML = B_SIDEBAR_HTML;
    
    // Toggle Logic
    const menuGroups = container.querySelectorAll('.menu-group');
    menuGroups.forEach(group => {{
        const header = group.querySelector('div.justify-between');
        const submenu = group.querySelector('.flex-col');
        const icon = header.querySelector('i');
        
        header.addEventListener('click', () => {{
            const isHidden = submenu.classList.contains('hidden');
            if (isHidden) {{
                submenu.classList.remove('hidden');
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }} else {{
                submenu.classList.add('hidden');
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }}
        }});
    }});
    
    // Active Menu Logic
    if (activeMenuName) {{
        const links = container.querySelectorAll('.menu-link');
        links.forEach(link => {{
            if (link.textContent.trim() === activeMenuName) {{
                // Highlight Link
                link.classList.remove('text-gray-600');
                link.classList.add('bg-blue-50/80', 'text-dfblue', 'border-r-2', 'border-dfblue', 'active-menu');
                
                // Expand and Highlight Group
                const group = link.closest('.menu-group');
                if (group) {{
                    const header = group.querySelector('div.justify-between');
                    const submenu = group.querySelector('.flex-col');
                    const icon = header.querySelector('i');
                    const span = header.querySelector('span');
                    
                    submenu.classList.remove('hidden');
                    header.classList.add('bg-blue-50/50');
                    span.classList.remove('text-gray-800');
                    span.classList.add('text-dfblue');
                    icon.classList.remove('fa-chevron-down', 'text-gray-400');
                    icon.classList.add('fa-chevron-up', 'text-dfblue');
                }}
            }}
        }});
    }}
}}
"""

with open('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/b_sidebar.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("b_sidebar.js generated successfully!")
