import os
import glob
from bs4 import BeautifulSoup

for filepath in glob.glob('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    head = soup.find('head')
    if head:
        # Check if viewport meta exists
        viewport_meta = head.find('meta', attrs={'name': 'viewport'})
        if not viewport_meta:
            new_meta = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'})
            # Insert right after charset meta or at the beginning of head
            charset_meta = head.find('meta', charset=True)
            if charset_meta:
                charset_meta.insert_after(new_meta)
            else:
                head.insert(0, new_meta)
                
    body = soup.find('body')
    if body:
        classes = body.get('class', [])
        # Unify font to text-sm (14px) and ensure text-gray-800
        if 'text-sm' not in classes:
            classes.append('text-sm')
        if 'text-gray-800' not in classes:
            classes.append('text-gray-800')
        body['class'] = classes

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Fixed viewports and global body font sizes.")
