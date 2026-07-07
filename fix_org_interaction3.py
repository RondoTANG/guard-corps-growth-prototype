from bs4 import BeautifulSoup
import re

with open('B端_完整后台大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the script tag containing the DOMContentLoaded logic
for script in soup.find_all('script'):
    if script.string and 'document.addEventListener(\'DOMContentLoaded\'' in script.string and 'orgCompareChart' in script.string:
        script.string = """
document.addEventListener('DOMContentLoaded', function() {
    // Database for fake random data
    function getRandomData(name) {
        // Just hashing the string to a predictable random number
        let hash = 0;
        for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
        const rand = Math.abs(hash) % 100;
        return {
            active: 40 + (rand % 50), // 40-90
            highTier: 5 + (rand % 20) // 5-25
        };
    }

    var orgChartDom = document.getElementById('orgCompareChart');
    var orgChart = null;
    var orgOption = {
        tooltip: { trigger: 'axis', axisPointer: { type: 'cross', crossStyle: { color: '#999' } } },
        legend: { data: ['活跃用户占比', '高段位占比(专家/大师)'], top: 0 },
        grid: { left: '3%', right: '3%', bottom: '5%', containLabel: true },
        xAxis: [ { type: 'category', data: [], axisPointer: { type: 'shadow' }, axisLabel: { interval: 0, rotate: 15 } } ],
        yAxis: [
            { type: 'value', name: '活跃度', min: 0, max: 100, interval: 20, axisLabel: { formatter: '{value} %' } },
            { type: 'value', name: '高段位占比', min: 0, max: 30, interval: 5, axisLabel: { formatter: '{value} %' } }
        ],
        series: [
            { name: '活跃用户占比', type: 'bar', barWidth: '30%', itemStyle: { color: '#3B82F6', borderRadius: [4, 4, 0, 0] }, data: [] },
            { name: '高段位占比(专家/大师)', type: 'line', yAxisIndex: 1, itemStyle: { color: '#EF4444' }, symbolSize: 8, lineStyle: { width: 3 }, data: [] }
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
        
        let activeData = [];
        let highTierData = [];
        names.forEach(n => {
            let d = getRandomData(n);
            activeData.push(d.active);
            highTierData.push(d.highTier);
        });

        orgOption.xAxis[0].data = names;
        orgOption.series[0].data = activeData;
        orgOption.series[1].data = highTierData;
        
        orgChart.setOption(orgOption, true);
    }

    // 1. Checkbox Interaction Logic
    const sidebar = document.getElementById('org-sidebar');
    if (sidebar) {
        const checkboxes = sidebar.querySelectorAll('.w-4.h-4.rounded');
        checkboxes.forEach(box => {
            const parent = box.closest('.flex.items-center');
            if (parent) {
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
                            let textSpan = b.closest('.flex').querySelector('span.text-gray-800, span.text-gray-600');
                            if(textSpan && textSpan.innerText.trim() !== '东风集团') {
                                checkedNames.push(textSpan.innerText.trim());
                            }
                        }
                    });
                    
                    // Update the Chart!
                    updateChart(checkedNames);
                });
            }
        });
        
        // Initial chart render
        updateChart(['东风乘用车公司', '东风日产乘用车', '东风华神汽车']);
    }
});
"""
        break

with open('B端_完整后台大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
# Copy back to B端_成长数据健康度大盘.html to keep both in sync
with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Checkbox interaction with chart linkage updated successfully.")
