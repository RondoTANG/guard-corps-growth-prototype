from bs4 import BeautifulSoup
import re

with open('B端_等级规则与XP配置页.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Get the full tables from the document to use as base for the modal snapshots
tier_table = str(soup.find('div', id='tab-tier').find('table'))
task_table = str(soup.find('div', id='tab-task').find('table'))

# For global, just take the form content
global_content = soup.find('div', id='tab-global')
global_form = ""
if global_content:
    # Just grab the main content divs, not the fixed bar
    for child in global_content.children:
        if child.name == 'div' and 'fixed' not in child.get('class', []):
            global_form += str(child)

# Now we need to update the script block that has openVersionModal
for script in soup.find_all('script'):
    if script.string and 'openVersionModal' in script.string:
        script.decompose()

# We'll write a new script that injects these, but we'll modify the HTML slightly in JS to make it "read-only"
new_script = """
<script>
    function closeVersionModal() {
        const overlay = document.getElementById('version-modal-overlay');
        const container = document.getElementById('version-modal-container');
        if (overlay && container) {
            container.classList.remove('scale-100');
            container.classList.add('scale-95');
            setTimeout(() => {
                overlay.style.display = 'none';
                overlay.classList.add('hidden');
            }, 150);
        }
    }

    function generateReadOnlyHtml(htmlStr) {
        // A simple way to make the cloned HTML look like a read-only snapshot:
        // Replace inputs with spans
        let parser = new DOMParser();
        let doc = parser.parseFromString(htmlStr, 'text/html');
        
        // Remove interactive buttons and action columns
        doc.querySelectorAll('button, a, .fas.fa-trash, .fas.fa-edit').forEach(el => el.remove());
        
        // Replace inputs with text
        doc.querySelectorAll('input[type="text"], input[type="number"]').forEach(el => {
            let span = doc.createElement('span');
            span.className = 'font-bold text-gray-900';
            span.textContent = el.value || el.placeholder || '-';
            el.parentNode.replaceChild(span, el);
        });
        
        // Replace selects with text
        doc.querySelectorAll('select').forEach(el => {
            let span = doc.createElement('span');
            span.className = 'font-bold text-gray-900';
            let selected = el.options[el.selectedIndex];
            span.textContent = selected ? selected.text : '-';
            el.parentNode.replaceChild(span, el);
        });
        
        // Disable toggles (just visual)
        doc.querySelectorAll('.toggle-checkbox').forEach(el => {
            el.disabled = true;
        });

        return doc.body.innerHTML;
    }

    function openVersionModal(e, tabId) {
        if(e) e.preventDefault();
        
        // Get the current tab's content directly from the DOM to simulate the "Full Configuration"
        const currentTab = document.getElementById(tabId);
        let cloneHtml = "";
        
        if (tabId === 'tab-tier') {
            const table = currentTab.querySelector('table');
            cloneHtml = table ? table.outerHTML : '';
        } else if (tabId === 'tab-task') {
            const table = currentTab.querySelector('table');
            cloneHtml = table ? table.outerHTML : '';
        } else if (tabId === 'tab-global') {
            // grab the content excluding the fixed bottom bar
            const contentDivs = Array.from(currentTab.children).filter(el => !el.classList.contains('fixed'));
            cloneHtml = contentDivs.map(el => el.outerHTML).join('');
        }
        
        // Convert to read-only snapshot
        const snapshotHtml = generateReadOnlyHtml(cloneHtml);
        
        let title = "线上运行版本预览";
        if(tabId === 'tab-tier') title = "【等级门槛与特权】全量快照";
        if(tabId === 'tab-global') title = "【全局周期与保护规则】全量快照";
        if(tabId === 'tab-task') title = "【作业 XP 产出映射】全量快照";
        
        document.getElementById('modal-title-text').innerText = title;
        
        const headerHtml = `
            <div class="mb-4 relative">
                <div class="absolute top-0 right-0 bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">线上生效中 (版本号: V1.2)</div>
                <h4 class="text-sm font-bold text-gray-800 mb-2 pl-2 border-l-4 border-blue-500">线上全量配置数据</h4>
                <p class="text-xs text-gray-500 mb-4 pl-3">以下为当前线上环境正在运行的完整配置数据，覆盖将替换整个页面的所有设置。</p>
            </div>
        `;
        
        const warningHtml = `
            <div class="mt-6 flex items-start gap-2 text-sm text-gray-500 bg-orange-50 p-3 rounded-md border border-orange-100">
                <i class="fas fa-exclamation-triangle text-orange-500 mt-0.5"></i>
                <p>如果你选择“使用此版本覆盖草稿”，你当前<strong class="text-orange-600">未发布的修改将被全部清空并还原</strong>为上述配置。</p>
            </div>
        `;
        
        document.getElementById('modal-dynamic-body').innerHTML = headerHtml + '<div class="bg-white border border-gray-200 rounded-lg shadow-sm p-4 overflow-x-auto text-sm">' + snapshotHtml + '</div>' + warningHtml;
        
        const overlay = document.getElementById('version-modal-overlay');
        const container = document.getElementById('version-modal-container');
        if (overlay && container) {
            overlay.classList.remove('hidden');
            overlay.style.display = 'flex';
            setTimeout(() => {
                container.classList.remove('scale-95');
                container.classList.add('scale-100');
            }, 10);
        }
    }
</script>
"""

soup.body.append(BeautifulSoup(new_script, 'html.parser'))

# Also, let's make the modal wider so the massive tables fit better
overlay = soup.find('div', id='version-modal-overlay')
if overlay:
    container = overlay.find('div', id='version-modal-container')
    if container:
        classes = container.get('class', [])
        if 'w-[700px]' in classes:
            classes.remove('w-[700px]')
        classes.append('w-[1000px]')
        container['class'] = classes

with open('B端_等级规则与XP配置页.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modal fixed fully.")
