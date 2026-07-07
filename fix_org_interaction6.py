from bs4 import BeautifulSoup
import re

with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

new_script = """
document.addEventListener('DOMContentLoaded', function() {
    // Database for fake random data
    function getRandomData(name) {
        let hash = 0;
        for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
        const rand = Math.abs(hash) % 100;
        
        let l4 = 1 + (rand % 5);      // 1-5%
        let l3 = 5 + (rand % 10);     // 5-14%
        let l2 = 20 + (rand % 30);    // 20-49%
        let l1 = 100 - l4 - l3 - l2;  // remaining
        
        return {
            active: 40 + (rand % 50),
            l1: l1,
            l2: l2,
            l3: l3,
            l4: l4
        };
    }

    var orgChartDom = document.getElementById('orgCompareChart');
    var orgChart = null;
    var orgOption = {
        tooltip: { trigger: 'axis', axisPointer: { type: 'cross', crossStyle: { color: '#999' } } },
        legend: { data: ['活跃用户占比', '新秀(L1)占比', '熟练(L2)占比', '专家(L3)占比', '大师(L4)占比'], top: 0 },
        grid: { left: '3%', right: '3%', bottom: '5%', containLabel: true },
        xAxis: [ { type: 'category', data: [], axisPointer: { type: 'shadow' }, axisLabel: { interval: 0, rotate: 15 } } ],
        yAxis: [
            { type: 'value', name: '活跃度', min: 0, max: 100, interval: 20, axisLabel: { formatter: '{value} %' } },
            { type: 'value', name: '段位占比', min: 0, max: 100, interval: 20, axisLabel: { formatter: '{value} %' } }
        ],
        series: [
            { name: '活跃用户占比', type: 'bar', barWidth: '30%', itemStyle: { color: '#DBEAFE', borderRadius: [4, 4, 0, 0] }, data: [] },
            { name: '新秀(L1)占比', type: 'line', yAxisIndex: 1, itemStyle: { color: '#9CA3AF' }, symbolSize: 6, lineStyle: { width: 2 }, data: [] },
            { name: '熟练(L2)占比', type: 'line', yAxisIndex: 1, itemStyle: { color: '#3B82F6' }, symbolSize: 6, lineStyle: { width: 2 }, data: [] },
            { name: '专家(L3)占比', type: 'line', yAxisIndex: 1, itemStyle: { color: '#8B5CF6' }, symbolSize: 6, lineStyle: { width: 2 }, data: [] },
            { name: '大师(L4)占比', type: 'line', yAxisIndex: 1, itemStyle: { color: '#EF4444' }, symbolSize: 6, lineStyle: { width: 2 }, data: [] }
        ]
    };

    if (orgChartDom && typeof echarts !== 'undefined') {
        orgChart = echarts.init(orgChartDom);
        window.addEventListener('resize', function() { orgChart.resize(); });
    }

    function updateChart(checkedNames) {
        if (!orgChart) return;
        let names = checkedNames;
        if (names.length === 0) {
            // Default
            names = ['乘用车公司', '日产乘用车', '华神汽车', '商用车公司', '技术中心'];
        }
        
        let activeData = [], l1Data = [], l2Data = [], l3Data = [], l4Data = [];
        names.forEach(n => {
            let d = getRandomData(n);
            activeData.push(d.active);
            l1Data.push(d.l1);
            l2Data.push(d.l2);
            l3Data.push(d.l3);
            l4Data.push(d.l4);
        });

        orgOption.xAxis[0].data = names;
        orgOption.series[0].data = activeData;
        orgOption.series[1].data = l1Data;
        orgOption.series[2].data = l2Data;
        orgOption.series[3].data = l3Data;
        orgOption.series[4].data = l4Data;
        
        orgChart.setOption(orgOption, true);
    }

    // 1. Checkbox Interaction Logic
    const sidebar = document.getElementById('org-tree-sidebar');
    if (sidebar) {
        const checkboxes = sidebar.querySelectorAll('.w-4.h-4.rounded');
        checkboxes.forEach(box => {
            const parent = box.parentElement;
            if (parent && parent.classList.contains('flex')) {
                parent.style.cursor = 'pointer';
                parent.addEventListener('click', function(e) {
                    e.stopPropagation(); // prevent bubbling
                    // Check if currently checked (by checking bg color)
                    const isChecked = box.classList.contains('bg-blue-600') || box.classList.contains('bg-blue-500');
                    if (isChecked) {
                        // Uncheck it
                        box.classList.remove('bg-blue-600', 'bg-blue-500', 'border-blue-500');
                        box.classList.add('bg-white', 'border', 'border-gray-300');
                        box.innerHTML = ''; // Remove SVG
                    } else {
                        // Check it
                        box.classList.remove('bg-white', 'border', 'border-gray-300');
                        box.classList.add('bg-blue-600');
                        box.innerHTML = '<i class="fas fa-check text-white text-[10px]"></i>';
                    }

                    // Collect all checked nodes
                    let checkedNames = [];
                    sidebar.querySelectorAll('.w-4.h-4.rounded').forEach(b => {
                        if (b.classList.contains('bg-blue-600') || b.classList.contains('bg-blue-500')) {
                            let textSpan = b.parentElement.querySelector('span.text-gray-800, span.text-gray-600');
                            if(textSpan && textSpan.textContent.trim() !== '东风集团') {
                                checkedNames.push(textSpan.textContent.trim());
                            }
                        }
                    });
                    
                    // Update the Chart!
                    updateChart(checkedNames);
                });
            }
        });
        
        // Initial chart render
        let initialNames = [];
        sidebar.querySelectorAll('.w-4.h-4.rounded').forEach(b => {
            if (b.classList.contains('bg-blue-600') || b.classList.contains('bg-blue-500')) {
                let textSpan = b.parentElement.querySelector('span.text-gray-800, span.text-gray-600');
                if(textSpan && textSpan.textContent.trim() !== '东风集团') {
                    initialNames.push(textSpan.textContent.trim());
                }
            }
        });
        if (initialNames.length === 0) initialNames = ['东风乘用车公司', '东风日产乘用车', '东风华神汽车'];
        updateChart(initialNames);
    }
});
"""

# Update the JS to query 'org-tree-sidebar'
for script in soup.find_all('script'):
    if script.string and 'document.addEventListener(\'DOMContentLoaded\'' in script.string and 'orgCompareChart' in script.string:
        script.string = new_script

with open('B端_完整后台大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
# Keep both files in sync
with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Chart updated to show 4 lines.")
