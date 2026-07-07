import os
import glob
import re

directory = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/"
files = glob.glob(os.path.join(directory, "C端_*.html"))

new_item_template = '            <a href="C端_作业详情.html" class="block px-3 py-2.5 rounded-lg text-xs {active_class} transition flex items-center"><i class="fas fa-file-alt w-5"></i> 作业详情</a>\n'

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already added
    if 'href="C端_作业详情.html"' in content and file_path != os.path.join(directory, "C端_作业详情.html"):
        continue

    # Determine if this file IS the details page
    is_details = file_path.endswith("C端_作业详情.html")
    active_class = "bg-red-50 text-dfred font-bold" if is_details else "text-gray-600 hover:bg-gray-100"
    
    new_item = new_item_template.format(active_class=active_class)
    
    # We need to insert this after the 作业大厅 link
    # The regex targets the block containing href="C端_作业大厅.html"
    pattern = r'(<a href="C端_作业大厅\.html".*?</a>\n)'
    
    # If we are in C端_作业详情.html itself, it currently doesn't have the sidebar!
    # Wait, in C端_作业详情.html, I didn't even put the left sidebar in the HTML.
    
    if is_details:
        # C端_作业详情.html is a standalone phone frame. It doesn't have the left sidebar.
        pass
    else:
        content = re.sub(pattern, r'\1' + new_item, content, count=1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Done")
