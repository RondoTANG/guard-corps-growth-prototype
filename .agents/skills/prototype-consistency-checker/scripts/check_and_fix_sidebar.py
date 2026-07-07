import os
import re
import sys

# Define the mapping of B-end pages to their expected active sidebar text
EXPECTED_MAPPINGS = {
    "B端_成长数据健康度大盘.html": "成长数据大盘",
    "B端_等级规则与XP配置页.html": "成长规则配置",
    "B端_用户管理_XP干预页.html": "用户列表",
    "B端_系统设置_文章管理页.html": "文章管理"
}

def clean_active_state(html):
    def replace_active(match):
        full_a = match.group(0)
        inner_text_match = re.search(r'>([^<]+)</a>', full_a)
        if not inner_text_match:
            return full_a
        inner_text = inner_text_match.group(1)
        href_match = re.search(r'href="([^"]+)"', full_a)
        href_val = href_match.group(1) if href_match else "#"
        return f'<a class="px-9 py-2.5 hover:text-white transition-colors" href="{href_val}">{inner_text}</a>'
        
    html = re.sub(r'<a[^>]+bg-\[#3B82F6\][^>]+>.*?</a>', replace_active, html)
    html = re.sub(r'<a[^>]+bg-gray-700[^>]+>.*?</a>', replace_active, html)
    return html

def set_active_state(html, target_text):
    def replace_target(match):
        full_a = match.group(0)
        inner_text_match = re.search(r'>([^<]+)</a>', full_a)
        if not inner_text_match:
            return full_a
        inner_text = inner_text_match.group(1)
        href_match = re.search(r'href="([^"]+)"', full_a)
        href_val = href_match.group(1) if href_match else "#"
        if inner_text == target_text:
            return f'<a class="px-9 py-3 bg-[#3B82F6] text-white font-bold menu-link active-menu" href="{href_val}">{inner_text}</a>'
        return full_a
    
    html = re.sub(r'<a class="px-9[^>]+>([^<]+)</a>', replace_target, html)
    return html

def check_and_fix(directory, auto_fix=False):
    errors_found = 0
    fixed_count = 0
    
    print(f"🔍 Starting Prototype Consistency Audit in {directory}...")
    
    for filename, active_text in EXPECTED_MAPPINGS.items():
        path = os.path.join(directory, filename)
        if not os.path.exists(path):
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        
        sidebar_match = re.search(r'(<aside.*?</aside>)', html, re.DOTALL)
        if not sidebar_match:
            print(f"⚠️  [WARNING] No sidebar found in {filename}")
            continue
            
        sidebar = sidebar_match.group(1)
        
        # Check if the active menu is correct
        # It should ONLY have one active menu, and it must match active_text
        active_items = re.findall(r'<a[^>]+active-menu[^>]+>([^<]+)</a>', sidebar)
        
        is_correct = len(active_items) == 1 and active_items[0] == active_text
        
        if not is_correct:
            errors_found += 1
            print(f"❌ [ERROR] {filename}: Expected active item '{active_text}', but found: {active_items}")
            
            if auto_fix:
                print(f"   🛠️  Fixing {filename}...")
                new_sidebar = clean_active_state(sidebar)
                new_sidebar = set_active_state(new_sidebar, active_text)
                new_html = re.sub(r'<aside.*?</aside>', new_sidebar, html, flags=re.DOTALL)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_html)
                fixed_count += 1
                print(f"   ✅ Fixed!")
        else:
            print(f"✅ [PASS] {filename}")

    print("\n📊 Audit Summary:")
    print(f"Total Errors Found: {errors_found}")
    if auto_fix:
        print(f"Errors Fixed: {fixed_count}")
        
    if errors_found > 0 and not auto_fix:
        print("\n💡 Run script with --fix to automatically resolve these issues.")
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Audit and fix prototype UI consistency.")
    parser.add_argument("--dir", default=".", help="Directory containing HTML prototypes")
    parser.add_argument("--fix", action="store_true", help="Automatically fix issues found")
    args = parser.parse_args()
    
    check_and_fix(args.dir, args.fix)
