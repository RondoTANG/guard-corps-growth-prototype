import glob

files = glob.glob("C端_*.html")
for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to remove `target="_blank"` from the link to C端_护卫军后台功能导航页.html
    # It looks something like: <a href="C端_护卫军后台功能导航页.html" ... target="_blank">
    
    # We can just replace 'href="C端_护卫军后台功能导航页.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center" target="_blank"'
    # with the same without target="_blank"
    
    new_content = content.replace('href="C端_护卫军后台功能导航页.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center" target="_blank"',
                                  'href="C端_护卫军后台功能导航页.html" class="block px-3 py-2.5 rounded-lg text-xs text-gray-600 hover:bg-red-50 hover:text-dfred transition flex items-center"')
    
    # also try simpler replace if the above doesn't match exactly
    import re
    new_content = re.sub(r'(href="C端_护卫军后台功能导航页.html"[^>]*) target="_blank"', r'\1', new_content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")

