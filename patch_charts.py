import re

filepath = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"

with open(filepath, "r") as f:
    content = f.read()

# 1. Update the chart header with a select dropdown
old_header = '<span class="ml-2 text-xs font-normal text-gray-500 bg-gray-100 px-2 py-0.5 rounded" id="chart-dimension-label">当前对比维度：未选择</span>'
new_header = """<select id="chart-level-selector" class="ml-2 border border-gray-200 rounded px-2 py-0.5 text-xs outline-none focus:border-blue-500 text-gray-700 bg-white hover:bg-gray-50 font-normal">
<option value="auto">自动(当前选中最高层级)</option>
<option value="2">二级党委</option>
<option value="3">三级党组织</option>
<option value="4">四级党组织</option>
<option value="5">党支部</option>
</select>
<span class="ml-2 text-xs font-normal text-blue-600 bg-blue-50 px-2 py-0.5 rounded border border-blue-100 hidden" id="chart-dimension-label">已选: 0个</span>"""
content = content.replace(old_header, new_header)

# 2. Add missing chart initializations and update getSelectedNodesInfo
js_missing_init = """
        // Initialize Tier Distribution Chart
        var tierChartDom = document.getElementById('chart-tier-distribution');
        if (tierChartDom) {
            window.tierChart = echarts.init(tierChartDom);
            window.tierOption = {
                tooltip: { trigger: 'item' },
                legend: { top: 'bottom', textStyle: { fontSize: 10 } },
                series: [{
                    name: '段位分布',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    itemStyle: { borderRadius: 4, borderColor: '#fff', borderWidth: 2 },
                    label: { show: false, position: 'center' },
                    emphasis: { label: { show: true, fontSize: '14', fontWeight: 'bold' } },
                    labelLine: { show: false },
                    data: []
                }]
            };
            window.tierChart.setOption(window.tierOption);
        }

        // Initialize Conversion Chart
        var conversionChartDom = document.getElementById('chart-conversion');
        if (conversionChartDom) {
            window.conversionChart = echarts.init(conversionChartDom);
            window.conversionOption = {
                tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
                legend: { top: 'bottom', textStyle: { fontSize: 10 } },
                grid: { left: '3%', right: '3%', bottom: '15%', top: '5%', containLabel: true },
                xAxis: { type: 'category', data: ['新秀(L1)', '熟练(L2)', '专家(L3)', '大师(L4)'], axisLabel: { fontSize: 10 } },
                yAxis: { type: 'value', max: 100, axisLabel: { formatter: '{value}%' } },
                series: [
                    { name: '任务参与率', type: 'bar', barWidth: '30%', itemStyle: { color: '#93C5FD', borderRadius: [2, 2, 0, 0] }, data: [] },
                    { name: '作业通过率', type: 'bar', barWidth: '30%', itemStyle: { color: '#3B82F6', borderRadius: [2, 2, 0, 0] }, data: [] }
                ]
            };
            window.conversionChart.setOption(window.conversionOption);
        }
"""

js_update_get_selected = """
        function getSelectedNodesInfo() {
            let checkedNames = [];
            let checkedLevels = new Set();
            let count = 0;
            
            const levelSelector = document.getElementById('chart-level-selector');
            const forcedLevel = levelSelector ? levelSelector.value : 'auto';
            
            const allNodes = sidebar.querySelectorAll('.org-node');
            allNodes.forEach(node => {
                const box = node.querySelector('.checkbox-box');
                const state = getCheckboxState(box);
                
                if (state === 1 || state === 2) {
                    if (state === 1) count++;
                }
                
                if (state === 1) {
                    const level = parseInt(node.dataset.level || 0);
                    const name = node.dataset.name;
                    
                    if (name === '中国共产党东风汽车集团有限公司委员会') return; // skip root
                    
                    if (forcedLevel !== 'auto') {
                        // Use explicit level filtering
                        if (level === parseInt(forcedLevel)) {
                            checkedNames.push(name);
                            checkedLevels.add(level);
                        }
                    } else {
                        // Auto drill-down logic: only top-most checked nodes
                        let isTopMost = true;
                        const parentContainer = node.closest('.children-container');
                        if (parentContainer) {
                            const parentNode = parentContainer.previousElementSibling;
                            if (parentNode && parentNode.classList.contains('org-node')) {
                                const pBox = parentNode.querySelector('.checkbox-box');
                                const pName = parentNode.dataset.name;
                                if (getCheckboxState(pBox) === 1 && pName !== '中国共产党东风汽车集团有限公司委员会') {
                                    isTopMost = false;
                                }
                            }
                        }
                        
                        if (isTopMost) {
                            checkedNames.push(name);
                            checkedLevels.add(level);
                        }
                    }
                }
            });
            
            const countBadge = sidebar.querySelector('.badge-count');
            if (countBadge) {
                countBadge.textContent = '已选 ' + count;
            }
            
            return {
                names: checkedNames,
                count: checkedNames.length
            };
        }
"""

js_update_chart_label = """
            const dimLabel = document.getElementById('chart-dimension-label');
            if (dimLabel) {
                if (info.count === 0) {
                    dimLabel.classList.add('hidden');
                } else {
                    dimLabel.classList.remove('hidden');
                    dimLabel.textContent = `共 ${info.count} 项`;
                }
            }
"""

# Apply JS insertions
idx_init = content.find("var statusChartDom = document.getElementById('protectionStatusChart');")
if idx_init != -1:
    content = content[:idx_init] + js_missing_init + content[idx_init:]

# Replace getSelectedNodesInfo
idx_get_start = content.find("function getSelectedNodesInfo() {")
idx_get_end = content.find("if (sidebar) {", idx_get_start)
if idx_get_start != -1 and idx_get_end != -1:
    content = content[:idx_get_start] + js_update_get_selected + "\n        " + content[idx_get_end:]

# Replace chart dimension label logic
old_label_logic = """
            const dimLabel = document.getElementById('chart-dimension-label');
            if (dimLabel) {
                if (info.count === 0) {
                    dimLabel.textContent = `当前对比维度：未选择`;
                    dimLabel.className = 'ml-2 text-xs font-normal text-gray-500 bg-gray-100 px-2 py-0.5 rounded';
                } else {
                    dimLabel.textContent = `当前对比维度：${info.dimensionText} (${info.count}个)`;
                    dimLabel.className = 'ml-2 text-xs font-normal text-blue-600 bg-blue-50 px-2 py-0.5 rounded border border-blue-100';
                }
            }
"""
content = content.replace(old_label_logic, js_update_chart_label)

# Add event listener for the new selector
js_selector_event = """
        const levelSelector = document.getElementById('chart-level-selector');
        if (levelSelector) {
            levelSelector.addEventListener('change', () => {
                updateChart(getSelectedNodesInfo());
            });
        }
"""
idx_sidebar_actions = content.find("// Sidebar Actions")
if idx_sidebar_actions != -1:
    content = content[:idx_sidebar_actions] + js_selector_event + "\n        " + content[idx_sidebar_actions:]

with open(filepath, "w") as f:
    f.write(content)

print("Charts fixed and level selector added!")

