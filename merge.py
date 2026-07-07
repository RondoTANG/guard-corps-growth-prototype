from bs4 import BeautifulSoup
import os

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    dashboard_soup = BeautifulSoup(f.read(), 'html.parser')

with open('B端_XP资产流水明细表.html', 'r', encoding='utf-8') as f:
    table_soup = BeautifulSoup(f.read(), 'html.parser')

# Find the content area in dashboard
content_area = dashboard_soup.find('div', class_=lambda c: c and 'flex-1' in c and 'overflow-y-auto' in c)

# Find the charts grid
charts_grid = dashboard_soup.find('div', class_=lambda c: c and 'grid-cols-2' in c and 'gap-6' in c)

if charts_grid:
    # Change to grid-cols-3
    classes = charts_grid['class']
    classes = [c if c != 'grid-cols-2' else 'grid-cols-3' for c in classes]
    charts_grid['class'] = classes
    
    # Create the 3rd chart container
    new_chart = BeautifulSoup("""
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-5 flex flex-col">
        <div class="flex items-center justify-between mb-4">
            <h3 class="font-bold text-gray-800 text-sm">用户定级状态分布 (保护期监控)</h3>
            <button class="text-gray-400 hover:text-gray-600"><i class="fas fa-ellipsis-h"></i></button>
        </div>
        <div class="flex-1 min-h-[250px]" id="protectionStatusChart"></div>
        <div class="mt-4 pt-4 border-t border-gray-100 flex justify-between text-xs text-gray-500">
            <span>正常: 85%</span>
            <span class="text-yellow-600">保级缓冲: 12%</span>
            <span class="text-red-500">荣誉保底: 3%</span>
        </div>
    </div>
    """, 'html.parser')
    charts_grid.append(new_chart)
    
    # Add script for the 3rd chart
    script_tag = dashboard_soup.new_tag('script')
    script_tag.string = """
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize Protection Status Chart
        var statusChart = echarts.init(document.getElementById('protectionStatusChart'));
        statusChart.setOption({
            tooltip: { trigger: 'item' },
            legend: { top: 'bottom', textStyle: { fontSize: 10 } },
            series: [{
                name: '定级状态',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 5,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: { show: false, position: 'center' },
                emphasis: {
                    label: { show: true, fontSize: 14, fontWeight: 'bold' }
                },
                labelLine: { show: false },
                data: [
                    { value: 10582, name: '正常段位', itemStyle: { color: '#3B82F6' } },
                    { value: 1494, name: '保级缓冲期', itemStyle: { color: '#F59E0B' } },
                    { value: 374, name: '荣誉保底', itemStyle: { color: '#EF4444' } }
                ]
            }]
        });
        
        window.addEventListener('resize', function() {
            statusChart.resize();
        });
    });
    """
    dashboard_soup.body.append(script_tag)

# Find the table area in B端_XP资产流水明细表.html
# Usually it's inside the main flex-1 overflow-y-auto container
table_content_area = table_soup.find('div', class_=lambda c: c and 'flex-1' in c and 'overflow-y-auto' in c)

if table_content_area and content_area:
    # Append a separator
    separator = BeautifulSoup("""
    <div class="mt-8 mb-4">
        <h2 class="text-lg font-bold text-gray-800 border-l-4 border-dfred pl-2">XP资产流水明细</h2>
        <p class="text-sm text-gray-500 mt-1">全站 XP 发放与核销明细账本，支持多维度对账检索。</p>
    </div>
    """, 'html.parser')
    content_area.append(separator)
    
    # Append the children of table_content_area to content_area
    # skip the first Header/Global Filter Bar if they duplicate
    for child in table_content_area.contents:
        if child.name == 'div' and 'bg-white p-4 rounded-md shadow-sm border border-gray-200 flex flex-col gap-4' in child.get('class', []):
            content_area.append(child)
        elif child.name == 'div' and 'bg-white border border-gray-200 rounded-md shadow-sm overflow-hidden' in child.get('class', []):
            content_area.append(child)
        elif child.name == 'div' and 'flex items-center justify-between mt-4' in child.get('class', []):
            content_area.append(child)
            
# Also remove "XP资产流水" from the sidebar menu to reflect the merge
for a in dashboard_soup.find_all('a', class_='menu-link'):
    if 'XP资产流水' in a.text:
        a.decompose()

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(dashboard_soup))

print("Merged successfully.")
