from bs4 import BeautifulSoup

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for div in soup.find_all('div', class_=lambda c: c and 'sticky' in c and 'bottom-0' in c):
    # Remove sticky and bottom-0, remove negative margins
    classes = div['class']
    new_classes = [c for c in classes if c not in ['sticky', 'bottom-0', '-mx-6', '-mb-6', 'shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]']]
    # Add rounded corners since it's now a block
    new_classes.extend(['rounded-b-lg', 'border', 'shadow-sm'])
    div['class'] = new_classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Unstickied successfully.")
