import os
import glob
from bs4 import BeautifulSoup

sidebar_js_path = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/b_sidebar.js'

# 1. Update b_sidebar.js to use text-blue-600 instead of dfblue for exact matching
with open(sidebar_js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace text-dfblue with text-blue-600 and border-dfblue with border-blue-600
js_content = js_content.replace('text-dfblue', 'text-blue-600')
js_content = js_content.replace('border-dfblue', 'border-blue-600')
# Change bg-blue-50/80 to bg-blue-50 (for link active bg)
js_content = js_content.replace('bg-blue-50/80', 'bg-blue-50')
js_content = js_content.replace('style="min-height: 100vh;"', 'class="h-full"')

with open(sidebar_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Iterate through all B端 HTML files
for filepath in glob.glob('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_*.html'):
    if '新建作业' in filepath: 
        # Skip wizards without sidebar
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if 'b_sidebar.js' in html:
        # Already processed
        print(f"Skipping {filepath}, already has global sidebar.")
        continue

    soup = BeautifulSoup(html, 'html.parser')
    aside = soup.find('aside')
    if not aside:
        print(f"No aside found in {filepath}")
        continue
        
    # Determine active menu name
    active_menu_name = ''
    # Find active menu by class (my script used active-menu, the manual one used border-blue-600)
    active_link = aside.find('a', class_=lambda x: x and ('active-menu' in x or 'border-blue-600' in x or 'bg-blue-50/80' in x))
    if active_link:
        active_menu_name = active_link.get_text(strip=True)
    elif '文章管理' in filepath:
        active_menu_name = '文章管理'
    elif 'XP干预' in filepath:
        active_menu_name = '用户列表'
    elif '等级规则' in filepath:
        active_menu_name = '成长规则配置'
    elif '健康度大盘' in filepath or '完整后台大盘' in filepath:
        active_menu_name = '成长数据大盘' if '健康度大盘' in filepath else '完整数据大盘'
    
    # Replace aside with container
    container = soup.new_tag('div', id='b-sidebar-container', **{'class': 'shrink-0 flex h-full'})
    aside.replace_with(container)
    
    # Add script tags at the end of body or right after container
    # Since sidebar script is synchronous, we can just put it right after container
    script_src = soup.new_tag('script', src='b_sidebar.js')
    script_init = soup.new_tag('script')
    script_init.string = f"initBSidebar('{active_menu_name}');"
    
    container.insert_after(script_init)
    container.insert_after(script_src)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Applied global sidebar to {filepath} (Active: {active_menu_name})")

print("Done!")
