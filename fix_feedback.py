from bs4 import BeautifulSoup
import re

# 1. Update HTML
with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Fix terminology: 核销 -> 扣减
for text_node in soup.find_all(string=re.compile('核销')):
    new_text = text_node.replace('核销', '扣减')
    text_node.replace_with(new_text)

# Add '实时更新' badge to XP Flow Heading
xp_heading = soup.find('h2', string=re.compile('XP资产流水明细'))
if xp_heading:
    # It's an h2 tag. Let's make it a flex container to align the badge
    if not 'flex' in xp_heading.get('class', []):
        xp_heading['class'] = xp_heading.get('class', []) + ['flex', 'items-center']
    
    # Check if badge already exists to avoid duplicates
    if not xp_heading.find('span', string='实时'):
        badge = soup.new_tag('span', attrs={'class': 'ml-3 bg-green-100 text-green-700 text-xs px-2 py-0.5 rounded font-medium border border-green-200'})
        badge.append(soup.new_tag('i', attrs={'class': 'fas fa-bolt mr-1 text-green-500'}))
        badge.append("实时")
        xp_heading.append(badge)

# Fix Unchecked Checkboxes in Organization Tree
# Remove opacity-60 and add bg-white
for div in soup.find_all('div', class_=lambda c: c and 'opacity-60' in c):
    classes = div.get('class', [])
    if 'opacity-60' in classes:
        classes.remove('opacity-60')
    if 'hover:opacity-100' in classes:
        classes.remove('hover:opacity-100')
    div['class'] = classes

# Add bg-white to the empty border squares
for square in soup.find_all('div', class_=lambda c: c and 'w-4' in c and 'h-4' in c and 'border' in c and 'border-gray-300' in c):
    if not square.contents: # It's empty, so it's unchecked
        classes = square.get('class', [])
        if 'bg-white' not in classes:
            classes.append('bg-white')
        square['class'] = classes

# Add values to the Bar Chart
# The bar chart has blue and orange bars. Let's find them and add labels.
bar_chart_container = soup.find('div', class_=lambda c: c and 'h-48' in c and 'flex' in c and 'items-end' in c)
if bar_chart_container:
    bars = bar_chart_container.find_all('div', class_=lambda c: c and ('bg-blue-500' in c or 'bg-orange-500' in c))
    for bar in bars:
        # Check if label already exists
        if not bar.find('span'):
            # Calculate value from height style (e.g. height: 65%)
            style = bar.get('style', '')
            match = re.search(r'height:\s*(\d+)%', style)
            if match:
                val = match.group(1) + '%'
                label = soup.new_tag('span', attrs={'class': 'absolute -top-5 left-1/2 -translate-x-1/2 text-[10px] text-gray-600 font-medium'})
                label.string = val
                bar['class'] = bar.get('class', []) + ['relative'] # Ensure parent is relative
                bar.append(label)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 2. Update PRD
with open('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/02_成长体系规划/implementation_plan.md', 'r', encoding='utf-8') as f:
    prd_content = f.read()

prd_content = prd_content.replace('获取或核销', '获取或扣减')
prd_content = prd_content.replace('发放与核销明细', '发放与扣减明细')

with open('/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/02_成长体系规划/implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(prd_content)

print("Feedback fixes applied successfully.")
