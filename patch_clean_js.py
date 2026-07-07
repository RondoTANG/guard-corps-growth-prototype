import re

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "r") as f:
    content = f.read()

# 1. Remove inline script inside the tree
# We can use regex to remove any script tag that contains btnSelectAll
content = re.sub(r'<script>\s*const btnSelectAll = document\.getElementById.*?btnOnlyL2.*?<\/script>', '', content, flags=re.DOTALL)

# 2. Add the dynamic title label to the chart title
title_target = '<div class="flex items-center group cursor-help relative">各党组织活跃与段位分布对比'
title_replacement = '<div class="flex items-center group cursor-help relative">各党组织活跃与段位分布对比<span id="chart-dimension-label" class="ml-2 text-xs font-normal text-gray-500 bg-gray-100 px-2 py-0.5 rounded">当前对比维度：未选择</span>'
content = content.replace(title_target, title_replacement)

# 3. Completely replace the main DOMContentLoaded script block to guarantee clean logic
script_start_marker = "document.addEventListener('DOMContentLoaded', function() {"
script_start_idx = content.find(script_start_marker)

if script_start_idx != -1:
    # Find the end of the script block (assuming it's the last script in body)
    script_end_idx = content.find("</script></body>", script_start_idx)
    
    if script_end_idx != -1:
        new_script = """document.addEventListener('DOMContentLoaded', function() {
        // Initialize Protection Status Chart
        var statusChartDom = document.getElementById('protectionStatusChart');
        if (statusChartDom) {
            window.statusChart = echarts.init(statusChartDom);
            window.statusOption = {
                tooltip: { trigger: 'item' },
                legend: { top: 'bottom', textStyle: { fontSize: 10 } },
                series: [{
                    name: '定级状态',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    itemStyle: { borderRadius: 4, borderColor: '#fff', borderWidth: 2 },
                    label: { show: false, position: 'center' },
                    emphasis: { label: { show: true, fontSize: '14', fontWeight: 'bold' } },
                    labelLine: { show: false },
                    data: [
                        { value: 85, name: '受保护', itemStyle: { color: '#10B981' } },
                        { value: 15, name: '未受保护', itemStyle: { color: '#D1D5DB' } }
                    ]
                }]
            };
            window.statusChart.setOption(window.statusOption);
        }

        // Initialize main orgCompareChart
        var orgChartDom = document.getElementById('orgCompareChart');
        var orgChart;
        var orgOption = {
            tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
            dataZoom: [
                { type: 'slider', show: true, xAxisIndex: [0], bottom: -5, start: 0, end: 100, height: 20 }
            ],
            legend: { data: ['活跃度', '大师(L4)', '专家(L3)', '熟练(L2)', '新秀(L1)'], top: 0, icon: 'circle' },
            grid: { left: '3%', right: '3%', bottom: '8%', containLabel: true },
            xAxis: [ { type: 'category', data: [], axisPointer: { type: 'shadow' }, axisLabel: { interval: 0, rotate: 15, fontSize: 10 } } ],
            yAxis: [
                { type: 'value', name: '段位构成', min: 0, max: 100, interval: 20, axisLabel: { formatter: '{value} %' } },
                { type: 'value', name: '活跃度', min: 0, max: 100, interval: 20, axisLabel: { formatter: '{value} %' }, splitLine: { show: false } }
            ],
            series: [
                { name: '新秀(L1)', type: 'bar', stack: 'tier', barWidth: '35%', itemStyle: { color: '#E5E7EB' }, data: [] },
                { name: '熟练(L2)', type: 'bar', stack: 'tier', itemStyle: { color: '#93C5FD' }, data: [] },
                { name: '专家(L3)', type: 'bar', stack: 'tier', itemStyle: { color: '#3B82F6' }, data: [] },
                { name: '大师(L4)', type: 'bar', stack: 'tier', itemStyle: { color: '#1E3A8A', borderRadius: [4, 4, 0, 0] }, data: [] },
                { name: '活跃度', type: 'line', yAxisIndex: 1, itemStyle: { color: '#F59E0B' }, symbol: 'circle', symbolSize: 8, lineStyle: { width: 3, shadowColor: 'rgba(245, 158, 11, 0.4)', shadowBlur: 10, shadowOffsetY: 5 }, data: [], z: 10 }
            ]
        };

        if (orgChartDom && typeof echarts !== 'undefined') {
            orgChart = echarts.init(orgChartDom);
            window.addEventListener('resize', function() { orgChart.resize(); });
        }

        // Mock data generator
        function getRandomData(name) {
            let active = Math.floor(40 + Math.random() * 50);
            let l4 = Math.floor(Math.random() * 10);
            let l3 = Math.floor(Math.random() * 20);
            let l2 = Math.floor(20 + Math.random() * 30);
            let l1 = 100 - l4 - l3 - l2;
            return { active, l4, l3, l2, l1 };
        }

        function updateChart(info) {
            if (!orgChart) return;
            
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
            
            let names = info.names;
            
            if (names.length === 0) {
                orgOption.xAxis[0].data = [];
                orgOption.series.forEach(s => s.data = []);
                orgChart.setOption(orgOption, true);
                
                if (window.tierChart && window.tierOption) {
                    window.tierOption.series[0].data = [];
                    window.tierChart.setOption(window.tierOption, true);
                }
                if (window.conversionChart && window.conversionOption) {
                    window.conversionOption.series[0].data = [];
                    window.conversionOption.series[1].data = [];
                    window.conversionChart.setOption(window.conversionOption, true);
                }
                if (window.statusChart && window.statusOption) {
                    window.statusOption.series[0].data = [];
                    window.statusChart.setOption(window.statusOption, true);
                }
                return;
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
            orgOption.series[0].data = l1Data; 
            orgOption.series[1].data = l2Data; 
            orgOption.series[2].data = l3Data; 
            orgOption.series[3].data = l4Data; 
            orgOption.series[4].data = activeData; 
            
            if(orgOption.dataZoom) {
                let numItems = names.length;
                let endPercent = 100;
                if (numItems > 15) {
                    endPercent = Math.max(2, Math.floor(15 * 100 / numItems));
                }
                orgOption.dataZoom[0].end = endPercent;
            }

            orgChart.setOption(orgOption, true);
            
            if (window.tierChart && window.tierOption) {
                let totalL1 = l1Data.reduce((a,b)=>a+b, 0);
                let totalL2 = l2Data.reduce((a,b)=>a+b, 0);
                let totalL3 = l3Data.reduce((a,b)=>a+b, 0);
                let totalL4 = l4Data.reduce((a,b)=>a+b, 0);
                if(totalL1===0 && totalL2===0 && totalL3===0 && totalL4===0) {
                    totalL1 = 8500; totalL2 = 3100; totalL3 = 550; totalL4 = 300;
                }
                window.tierOption.series[0].data = [
                    { value: totalL1, name: 'Level 1 (新秀)' },
                    { value: totalL2, name: 'Level 2 (熟练)' },
                    { value: totalL3, name: 'Level 3 (专家)' },
                    { value: totalL4, name: 'Level 4 (大师)' }
                ];
                window.tierChart.setOption(window.tierOption);
            }
            
            if (window.conversionChart && window.conversionOption) {
                let passRate = [
                    Math.floor(60 + Math.random()*10),
                    Math.floor(70 + Math.random()*10),
                    Math.floor(80 + Math.random()*10),
                    Math.floor(90 + Math.random()*5)
                ];
                let participationRate = [
                    Math.floor(30 + Math.random()*10),
                    Math.floor(50 + Math.random()*10),
                    Math.floor(80 + Math.random()*10),
                    Math.floor(95 + Math.random()*3)
                ];
                window.conversionOption.series[0].data = participationRate;
                window.conversionOption.series[1].data = passRate;
                window.conversionChart.setOption(window.conversionOption);
            }
            
            if (window.statusChart && window.statusOption) {
                let protectedVal = Math.floor(60 + Math.random()*20);
                window.statusOption.series[0].data = [
                    { value: protectedVal, name: '受保护', itemStyle: { color: '#10B981' } },
                    { value: 100 - protectedVal, name: '未受保护', itemStyle: { color: '#D1D5DB' } }
                ];
                window.statusChart.setOption(window.statusOption);
            }
        }

        // Tree interactions
        const sidebar = document.getElementById('org-tree-sidebar');
        
        function setCheckboxState(box, state) {
            if (!box) return;
            box.dataset.state = state;
            box.classList.remove('bg-blue-600', 'bg-blue-500', 'border-blue-600', 'border-blue-500', 'bg-white', 'border-gray-300');
            if (state === 1) { // Checked
                box.classList.add('bg-blue-600', 'border-blue-600');
                box.innerHTML = '<i class="fas fa-check text-white text-[10px]"></i>';
            } else if (state === 2) { // Indeterminate
                box.classList.add('bg-blue-500', 'border-blue-500');
                box.innerHTML = '<i class="fas fa-minus text-white text-[10px]"></i>';
            } else { // Unchecked
                box.classList.add('bg-white', 'border', 'border-gray-300');
                box.innerHTML = '';
            }
        }

        function getCheckboxState(box) {
            if (!box) return 0;
            return parseInt(box.dataset.state || 0);
        }

        function updateChildren(container, state) {
            if (!container) return;
            const childBoxes = container.querySelectorAll('.checkbox-box');
            childBoxes.forEach(box => setCheckboxState(box, state));
        }

        function updateParents(nodeDiv) {
            const parentContainer = nodeDiv.closest('.children-container');
            if (!parentContainer) return;
            const parentNode = parentContainer.previousElementSibling;
            if (!parentNode || !parentNode.classList.contains('org-node')) return;
            
            const siblingNodes = parentContainer.querySelectorAll(':scope > .org-node');
            let allChecked = true;
            let anyChecked = false;
            
            siblingNodes.forEach(sibling => {
                const box = sibling.querySelector('.checkbox-box');
                const state = getCheckboxState(box);
                if (state === 1) anyChecked = true;
                else if (state === 2) { anyChecked = true; allChecked = false; }
                else allChecked = false;
            });
            
            const parentBox = parentNode.querySelector('.checkbox-box');
            let newState = 0;
            if (allChecked) newState = 1;
            else if (anyChecked) newState = 2;
            
            setCheckboxState(parentBox, newState);
            updateParents(parentNode);
        }

        function getSelectedNodesInfo() {
            let checkedNames = [];
            let checkedLevels = new Set();
            let checkedTypes = new Set();
            let count = 0;
            
            const allNodes = sidebar.querySelectorAll('.org-node');
            allNodes.forEach(node => {
                const box = node.querySelector('.checkbox-box');
                const state = getCheckboxState(box);
                
                if (state === 1 || state === 2) {
                    if (state === 1) count++;
                }
                
                if (state === 1) {
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
                    
                    const name = node.dataset.name;
                    if (isTopMost && name && name !== '中国共产党东风汽车集团有限公司委员会') {
                        checkedNames.push(name);
                        checkedLevels.add(parseInt(node.dataset.level || 0));
                        let t = node.dataset.type;
                        if(t) checkedTypes.add(t);
                    }
                }
            });
            
            const countBadge = sidebar.querySelector('.badge-count');
            if (countBadge) {
                countBadge.textContent = '已选 ' + count;
            }
            
            let dimensionText = "未选择";
            if (checkedNames.length > 0) {
                if (checkedLevels.size === 1) {
                    let typeArr = Array.from(checkedTypes);
                    dimensionText = typeArr.length > 0 ? typeArr[0] : "同级组织";
                } else {
                    dimensionText = "跨层级节点";
                }
            }
            
            return {
                names: checkedNames,
                dimensionText: dimensionText,
                count: checkedNames.length
            };
        }

        if (sidebar) {
            const nodes = sidebar.querySelectorAll('.org-node');
            nodes.forEach(node => {
                const box = node.querySelector('.checkbox-box');
                setCheckboxState(box, 0); // init
                
                node.addEventListener('click', function(e) {
                    e.stopPropagation();
                    
                    const target = e.target;
                    if (target.closest('.toggle-icon')) {
                        const icon = node.querySelector('.toggle-icon i');
                        const childrenContainer = node.nextElementSibling;
                        if (childrenContainer && childrenContainer.classList.contains('children-container')) {
                            childrenContainer.classList.toggle('hidden');
                            if (childrenContainer.classList.contains('hidden')) {
                                icon.classList.remove('fa-chevron-down');
                                icon.classList.add('fa-chevron-right');
                            } else {
                                icon.classList.remove('fa-chevron-right');
                                icon.classList.add('fa-chevron-down');
                            }
                        }
                        return;
                    }
                    
                    const currentState = getCheckboxState(box);
                    const newState = (currentState === 1) ? 0 : 1; 
                    
                    setCheckboxState(box, newState);
                    
                    const childrenContainer = node.nextElementSibling;
                    if (childrenContainer && childrenContainer.classList.contains('children-container')) {
                        updateChildren(childrenContainer, newState);
                    }
                    
                    updateParents(node);
                    updateChart(getSelectedNodesInfo());
                });
            });

            // Initial click
            const dmp = sidebar.querySelector('.org-node[data-name="中共东风商用车有限公司委员会"]');
            if (dmp) {
                dmp.click();
            } else if (nodes.length > 1) {
                nodes[1].click();
            }
        }

        // Sidebar Actions
        const btnClearAll = document.getElementById('btn-clear-all');
        const btnOnlyL2 = document.getElementById('btn-only-l2');
        const btnToggleCollapse = document.getElementById('btn-toggle-collapse');

        if (btnClearAll) {
            btnClearAll.addEventListener('click', () => {
                const allBoxes = sidebar.querySelectorAll('.checkbox-box');
                allBoxes.forEach(box => setCheckboxState(box, 0));
                updateChart(getSelectedNodesInfo());
            });
        }

        if (btnToggleCollapse) {
            let isCollapsed = false;
            btnToggleCollapse.addEventListener('click', () => {
                isCollapsed = !isCollapsed;
                btnToggleCollapse.innerHTML = isCollapsed ? '一键展开' : '一键收起';
                const allContainers = sidebar.querySelectorAll('.children-container');
                const allIcons = sidebar.querySelectorAll('.toggle-icon i');
                
                allContainers.forEach(c => {
                    const parentNode = c.previousElementSibling;
                    if (parentNode && parseInt(parentNode.dataset.level) >= 1) {
                        if (isCollapsed) c.classList.add('hidden');
                        else c.classList.remove('hidden');
                    }
                });
                allIcons.forEach(icon => {
                    const pNode = icon.closest('.org-node');
                    if (pNode && parseInt(pNode.dataset.level) >= 1) {
                        if (isCollapsed) {
                            icon.classList.remove('fa-chevron-down');
                            icon.classList.add('fa-chevron-right');
                        } else {
                            icon.classList.remove('fa-chevron-right');
                            icon.classList.add('fa-chevron-down');
                        }
                    }
                });
            });
        }

        if (btnOnlyL2) {
            btnOnlyL2.addEventListener('click', () => {
                const allBoxes = sidebar.querySelectorAll('.checkbox-box');
                allBoxes.forEach(box => setCheckboxState(box, 0));
                
                const l2Nodes = sidebar.querySelectorAll('.org-node[data-level="2"]');
                l2Nodes.forEach(node => {
                    const box = node.querySelector('.checkbox-box');
                    if(getCheckboxState(box) !== 1) {
                         node.click();
                    }
                });
                
                if (btnToggleCollapse && btnToggleCollapse.innerHTML === '一键收起') {
                    btnToggleCollapse.click();
                }
            });
        }

        // Sidebar Resizer
        const resizer = document.getElementById('sidebar-resizer');
        if (sidebar && resizer) {
            let isResizing = false;
            resizer.addEventListener('mousedown', (e) => {
                isResizing = true;
                document.body.style.cursor = 'col-resize';
                document.body.style.userSelect = 'none';
            });
            
            document.addEventListener('mousemove', (e) => {
                if (!isResizing) return;
                const sidebarRect = sidebar.getBoundingClientRect();
                let newWidth = e.clientX - sidebarRect.left;
                if (newWidth < 200) newWidth = 200;
                if (newWidth > 600) newWidth = 600;
                sidebar.style.width = newWidth + 'px';
                
                if (orgChart) orgChart.resize();
                if (window.tierChart) window.tierChart.resize();
                if (window.conversionChart) window.conversionChart.resize();
                if (window.statusChart) window.statusChart.resize();
            });
            
            document.addEventListener('mouseup', () => {
                if (isResizing) {
                    isResizing = false;
                    document.body.style.cursor = '';
                    document.body.style.userSelect = '';
                }
            });
        }
"""
        content = content[:script_start_idx] + new_script + content[script_end_idx:]

with open("/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html", "w") as f:
    f.write(content)

