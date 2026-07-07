from bs4 import BeautifulSoup
import re

with open('B端_成长数据健康度大盘.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Add JS to toggle checkboxes
# Let's add an id to the sidebar container for easy querying
sidebar = soup.find('aside')
if sidebar:
    sidebar['id'] = 'org-sidebar'

# 2. Add the New Chart: 各组织成长健康度排行
# Find the charts container (the grid with 2 cols)
charts_grid = soup.find('div', class_=lambda c: c and 'grid-cols-1' in c and 'lg:grid-cols-2' in c)

# Create a new full-width container for the Org comparison chart
new_chart_container = soup.new_tag('div', attrs={'class': 'bg-white rounded-lg shadow-sm border border-gray-200 p-5 mb-6'})
header = soup.new_tag('div', attrs={'class': 'flex justify-between items-center border-b border-gray-100 pb-3 mb-4'})
title = soup.new_tag('h3', attrs={'class': 'font-bold text-gray-800 text-base'})
title.append("各组织成长健康度排行")
header.append(title)
new_chart_container.append(header)

chart_div = soup.new_tag('div', attrs={'id': 'orgCompareChart', 'class': 'h-80 w-full'})
new_chart_container.append(chart_div)

# Insert it AFTER the first grid of charts
if charts_grid:
    charts_grid.insert_after(new_chart_container)

# 3. Inject JS for Checkboxes and the New Chart
script_tag = soup.new_tag('script')
script_tag.string = """
document.addEventListener('DOMContentLoaded', function() {
    // 1. Checkbox Interaction Logic
    const sidebar = document.getElementById('org-sidebar');
    if (sidebar) {
        // Find all checkbox containers (divs with w-4 h-4 border)
        const checkboxes = sidebar.querySelectorAll('.w-4.h-4.border');
        checkboxes.forEach(box => {
            // Make parent clickable
            const parent = box.closest('.flex.items-center');
            if (parent) {
                parent.style.cursor = 'pointer';
                parent.addEventListener('click', function(e) {
                    e.stopPropagation(); // prevent bubbling
                    // Toggle state
                    const isChecked = box.classList.contains('bg-blue-500');
                    if (isChecked) {
                        // Uncheck it
                        box.classList.remove('bg-blue-500', 'border-blue-500');
                        box.classList.add('bg-white', 'border-gray-300');
                        box.innerHTML = ''; // Remove SVG
                    } else {
                        // Check it
                        box.classList.remove('bg-white', 'border-gray-300');
                        box.classList.add('bg-blue-500', 'border-blue-500');
                        box.innerHTML = '<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>';
                    }
                });
            }
        });
    }

    // 2. Org Comparison Chart (ECharts)
    var orgChartDom = document.getElementById('orgCompareChart');
    if (orgChartDom && typeof echarts !== 'undefined') {
        var orgChart = echarts.init(orgChartDom);
        var orgOption = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'cross', crossStyle: { color: '#999' } }
            },
            legend: {
                data: ['活跃用户占比', '高段位占比(专家/大师)'],
                top: 0
            },
            grid: { left: '3%', right: '3%', bottom: '5%', containLabel: true },
            xAxis: [
                {
                    type: 'category',
                    data: ['乘用车公司', '日产乘用车', '华神汽车', '商用车公司', '技术中心'],
                    axisPointer: { type: 'shadow' },
                    axisLabel: { interval: 0, rotate: 15 }
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '活跃度',
                    min: 0,
                    max: 100,
                    interval: 20,
                    axisLabel: { formatter: '{value} %' }
                },
                {
                    type: 'value',
                    name: '高段位占比',
                    min: 0,
                    max: 30,
                    interval: 5,
                    axisLabel: { formatter: '{value} %' }
                }
            ],
            series: [
                {
                    name: '活跃用户占比',
                    type: 'bar',
                    barWidth: '30%',
                    itemStyle: { color: '#3B82F6', borderRadius: [4, 4, 0, 0] },
                    data: [82, 75, 68, 54, 89]
                },
                {
                    name: '高段位占比(专家/大师)',
                    type: 'line',
                    yAxisIndex: 1,
                    itemStyle: { color: '#EF4444' },
                    symbolSize: 8,
                    lineStyle: { width: 3 },
                    data: [15.2, 12.5, 8.4, 5.2, 22.1]
                }
            ]
        };
        orgChart.setOption(orgOption);
        window.addEventListener('resize', function() {
            orgChart.resize();
        });
    }
});
"""
soup.body.append(script_tag)

with open('B端_成长数据健康度大盘.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("JS interactions and new chart added successfully.")
