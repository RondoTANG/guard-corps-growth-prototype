import re

file_path = "B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add limit-config-group to any div inside the last td of rows that have a toggle
# Let's just find <div class="flex items-center gap-2"> that are next to <span class="text-sm text-gray-500">XP</span>
# and make sure they have limit-config-group

pattern = r'<div class="flex items-center gap-2(?: limit-config-group)?">(\s*<select.*?</select>)?(\s*<span class="text-sm font-medium[^>]*>.*?</span>)?\s*<input type="number"[^>]*>\s*<span class="text-sm text-gray-500">XP</span>\s*</div>'

def repl(m):
    inner = m.group(0)
    # Ensure it has limit-config-group
    if 'limit-config-group' not in inner:
        inner = inner.replace('class="flex items-center gap-2"', 'class="flex items-center gap-2 limit-config-group"')
    return inner

new_html = re.sub(pattern, repl, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Classes fixed.")
