from bs4 import BeautifulSoup

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# The correct content area is inside <main>
main_tag = soup.find('main')
correct_content_area = main_tag.find('div', class_=lambda c: c and 'flex-1' in c and 'overflow-y-auto' in c)

# The wrong content area was the first 'flex-1 overflow-y-auto' which is in the aside
aside_tag = soup.find('aside')
wrong_content_area = aside_tag.find('div', class_=lambda c: c and 'flex-1' in c and 'overflow-y-auto' in c)

if wrong_content_area and correct_content_area:
    # We want to move everything that comes AFTER the <nav> tag inside wrong_content_area
    nav_tag = wrong_content_area.find('nav')
    if nav_tag:
        # Get all siblings after nav_tag
        elements_to_move = []
        sibling = nav_tag.next_sibling
        while sibling:
            next_sibling = sibling.next_sibling
            elements_to_move.append(sibling)
            sibling = next_sibling
            
        for el in elements_to_move:
            correct_content_area.append(el)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed merge.")
