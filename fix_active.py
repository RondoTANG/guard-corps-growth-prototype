import re

files = [
    'B端_等级规则与XP配置页.html',
    'B端_用户管理_XP干预页.html',
    'B端_XP资产流水明细表.html',
    'B端_成长数据健康度大盘.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find the <a> tag with href == file_path inside the <aside>
    # and ensure its class contains "bg-[#3B82F6] text-white font-bold"
    
    # Replace any existing active class to be safe (though there shouldn't be any now)
    content = re.sub(r'(<a href="[^"]+".*?)class="[^"]*bg-\[#3B82F6\].*?"', r'\1class="px-9 py-2.5 hover:text-white transition-colors menu-link"', content)
    
    # Now specifically target the one matching the current file
    pattern = f'(<a href="{file_path}"[^>]*)class="[^"]*"'
    replacement = r'\1class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu"'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed active state in {file_path}")

