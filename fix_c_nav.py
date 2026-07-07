import glob
import re

files = glob.glob("C端_*.html")
for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to find any link pointing to B端_完整后台大盘.html and change it to B端_后台总控大盘_Iframe.html
    # We'll use regex to match the <a> tag
    pattern = r'<a href="B端_完整后台大盘.html"[^>]*>.*?</a>'
    replacement = '<a href="B端_后台总控大盘_Iframe.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center" target="_blank"><i class="fas fa-desktop w-5"></i> 护卫军后台总控 (Iframe)</a>'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")

