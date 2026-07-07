import re

path = "/Users/RondoT/Documents/护卫军相关/04_成长与门激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"
# Wait, typo in my mental path? Let me check the actual path
path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_系统设置_文章管理页.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the ugly button from the blue banner
html = re.sub(
    r'<button onclick="toggleFullscreen\(\)".*?</button>',
    '',
    html,
    flags=re.DOTALL
)

# 2. Add the button to the toolbar
# Find: <button class="px-3 py-1.5 hover:bg-blue-50 rounded text-xs text-[#1890ff] border border-blue-200 transition-colors"><i class="fas fa-code mr-1"></i> HTML</button>
toolbar_button = """<button class="px-3 py-1.5 hover:bg-gray-100 rounded text-xs text-gray-600 border border-gray-200 transition-colors"><i class="far fa-eye mr-1"></i> 预览</button>
                                            <button class="px-3 py-1.5 hover:bg-blue-50 rounded text-xs text-[#1890ff] border border-blue-200 transition-colors"><i class="fas fa-code mr-1"></i> 源码</button>
                                            <button onclick="toggleFullscreen()" class="px-3 py-1.5 hover:bg-gray-800 bg-gray-700 text-white rounded text-xs border border-gray-700 transition-colors shadow-sm ml-2" title="全屏编辑">
                                                <i id="fullscreen-icon" class="fas fa-expand mr-1"></i> <span id="fullscreen-text">全屏排版</span>
                                            </button>"""

html = re.sub(
    r'<button class="px-3 py-1\.5 hover:bg-blue-50 rounded text-xs text-\[#1890ff\] border border-blue-200 transition-colors"><i class="fas fa-code mr-1"></i> HTML</button>',
    toolbar_button,
    html
)

# 3. Update the JS to use a better 'fullscreen' class that avoids the right sidebar and left menu
# Left menu = w-64 (16rem). Top nav = h-14 (3.5rem). Right phone preview = right-6 w-80 (20rem + margin = 22rem).
# So: fixed top-20 left-72 bottom-6 right-[360px]
new_js = """
    <script>
        function toggleFullscreen() {
            const container = document.getElementById('tiptap-editor-container');
            const icon = document.getElementById('fullscreen-icon');
            const text = document.getElementById('fullscreen-text');
            
            // We want it to cover the form area but leave Left Menu (w-64), Top Header (h-14), and Right Preview (w-80) visible.
            // Using precise fixed positioning: top-[72px] left-[272px] right-[360px] bottom-[24px]
            
            if (container.classList.contains('fixed')) {
                // Exit fullscreen
                container.classList.remove('fixed', 'top-[80px]', 'left-[280px]', 'right-[360px]', 'bottom-[24px]', 'z-[100]', 'shadow-2xl');
                container.classList.add('flex-1', 'relative', 'h-[600px]');
                icon.classList.remove('fa-compress');
                icon.classList.add('fa-expand');
                text.innerText = '全屏排版';
                document.body.style.overflow = '';
            } else {
                // Enter fullscreen
                container.classList.remove('flex-1', 'relative', 'h-[600px]');
                container.classList.add('fixed', 'top-[80px]', 'left-[280px]', 'right-[360px]', 'bottom-[24px]', 'z-[100]', 'shadow-2xl');
                icon.classList.remove('fa-expand');
                icon.classList.add('fa-compress');
                text.innerText = '退出全屏';
                document.body.style.overflow = 'hidden';
            }
        }
    </script>
</body>
"""

html = re.sub(r'<script>\s*function toggleFullscreen\(\).*?</script>\s*</body>', new_js, html, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Fullscreen fixed.")
