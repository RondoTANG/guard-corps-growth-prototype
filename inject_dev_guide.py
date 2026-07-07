import re
import os

html_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"
md_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘_开发指南.md"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# 1. Update tailwind config to include typography
html = html.replace(
    '<script src="https://cdn.tailwindcss.com"></script>',
    '<script src="https://cdn.tailwindcss.com?plugins=typography"></script>'
)

# 2. Inject Dev Guide Button
old_btn_container = """                    <div class="flex items-center">
                        <button
                            class="bg-blue-50 text-blue-600 px-4 py-1.5 rounded text-sm hover:bg-blue-100 font-medium"><i
                                class="fas fa-download mr-1"></i> 导出报表</button>
                    </div>"""
new_btn_container = """                    <div class="flex items-center space-x-3">
                        <button id="btnDevGuide" class="bg-gray-100 text-gray-700 px-4 py-1.5 rounded text-sm hover:bg-gray-200 border border-gray-300 font-medium flex items-center transition-colors">
                            <i class="fas fa-code mr-1.5"></i> 开发指南
                        </button>
                        <button class="bg-blue-50 text-blue-600 px-4 py-1.5 rounded text-sm hover:bg-blue-100 font-medium transition-colors">
                            <i class="fas fa-download mr-1"></i> 导出报表
                        </button>
                    </div>"""
html = html.replace(old_btn_container, new_btn_container)

# 3. Inject Modal at the end of body
modal_html = f"""
    <!-- Dev Guide Modal -->
    <div id="devGuideModal" class="fixed inset-0 bg-gray-900 bg-opacity-60 z-[100] hidden flex items-center justify-center backdrop-blur-sm transition-opacity">
        <div class="bg-white rounded-xl w-3/4 max-w-5xl h-[85vh] flex flex-col shadow-2xl overflow-hidden transform transition-transform">
            <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center bg-gray-50/80">
                <h3 class="text-lg font-bold text-gray-800 flex items-center"><i class="fas fa-book-open text-blue-500 mr-2 text-xl"></i> 成长大盘 - 开发指南</h3>
                <button id="closeDevGuideBtn" class="text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-lg p-1.5 transition-colors">
                    <i class="fas fa-times text-xl w-6 h-6 flex items-center justify-center"></i>
                </button>
            </div>
            <div class="p-8 overflow-y-auto flex-1 prose prose-blue max-w-none prose-h2:border-b prose-h2:pb-2 prose-h2:mt-8" id="devGuideContent">
            </div>
        </div>
    </div>
    
    <script type="text/markdown" id="devGuideMarkdown">{md_content}</script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const btnDevGuide = document.getElementById('btnDevGuide');
            const devGuideModal = document.getElementById('devGuideModal');
            const closeDevGuideBtn = document.getElementById('closeDevGuideBtn');
            const devGuideContent = document.getElementById('devGuideContent');
            
            if(btnDevGuide && devGuideModal) {{
                btnDevGuide.addEventListener('click', () => {{
                    devGuideModal.classList.remove('hidden');
                    const mdText = document.getElementById('devGuideMarkdown').textContent;
                    if(window.marked) {{
                        devGuideContent.innerHTML = marked.parse(mdText);
                    }} else {{
                        devGuideContent.innerHTML = "<p class='text-red-500'>⚠️ 无法加载 marked.js 渲染器。</p>";
                    }}
                }});
                
                closeDevGuideBtn.addEventListener('click', () => {{
                    devGuideModal.classList.add('hidden');
                }});
                
                devGuideModal.addEventListener('click', (e) => {{
                    if (e.target === devGuideModal) {{
                        devGuideModal.classList.add('hidden');
                    }}
                }});
            }}
        }});
    </script>
</body>"""

html = html.replace("</body>", modal_html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Modal injected successfully!")
