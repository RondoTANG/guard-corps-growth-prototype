import re

filepath = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"
with open(filepath, "r") as f:
    content = f.read()

# 1. Update the JS logic
# Find updateChart(info) definition
idx = content.find("function updateChart(info) {")

if idx != -1:
    end_idx = content.find("// Tree interactions", idx)
    
    new_update_logic = """
        function getBaseSelectedCount() {
            let count = 0;
            const allNodes = sidebar.querySelectorAll('.org-node');
            allNodes.forEach(node => {
                const box = node.querySelector('.checkbox-box');
                const state = getCheckboxState(box);
                if (state === 1) count++;
            });
            return count;
        }
        
        function updateTopCharts() {
            let baseCount = getBaseSelectedCount();
            if (baseCount === 0) {
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
            
            // Generate some stable-ish random data based on count
            Math.seed = baseCount;
            function pseudoRandom() {
                var x = Math.sin(Math.seed++) * 10000;
                return x - Math.floor(x);
            }
            
            if (window.tierChart && window.tierOption) {
                let totalL1 = Math.floor(8500 + pseudoRandom()*1000); 
                let totalL2 = Math.floor(3100 + pseudoRandom()*500); 
                let totalL3 = Math.floor(550 + pseudoRandom()*100); 
                let totalL4 = Math.floor(300 + pseudoRandom()*50);
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
                    Math.floor(60 + pseudoRandom()*10),
                    Math.floor(70 + pseudoRandom()*10),
                    Math.floor(80 + pseudoRandom()*10),
                    Math.floor(90 + pseudoRandom()*5)
                ];
                let participationRate = [
                    Math.floor(30 + pseudoRandom()*10),
                    Math.floor(50 + pseudoRandom()*10),
                    Math.floor(80 + pseudoRandom()*10),
                    Math.floor(95 + pseudoRandom()*3)
                ];
                window.conversionOption.series[0].data = participationRate;
                window.conversionOption.series[1].data = passRate;
                window.conversionChart.setOption(window.conversionOption);
            }
            
            if (window.statusChart && window.statusOption) {
                let protectedVal = Math.floor(60 + pseudoRandom()*20);
                window.statusOption.series[0].data = [
                    { value: protectedVal, name: '受保护', itemStyle: { color: '#10B981' } },
                    { value: 100 - protectedVal, name: '未受保护', itemStyle: { color: '#D1D5DB' } }
                ];
                window.statusChart.setOption(window.statusOption);
            }
        }
        
        function updateChart(info) {
            if (!orgChart) return;
            
            const dimLabel = document.getElementById('chart-dimension-label');
            if (dimLabel) {
                if (info.count === 0) {
                    dimLabel.classList.add('hidden');
                } else {
                    dimLabel.classList.remove('hidden');
                    dimLabel.textContent = `共 ${info.count} 项`;
                }
            }
            
            let names = info.names;
            
            const overlay = document.getElementById('empty-selection-overlay');
            if (names.length === 0) {
                if (overlay) overlay.classList.remove('hidden');
                orgOption.xAxis[0].data = [];
                orgOption.series.forEach(s => s.data = []);
                orgChart.setOption(orgOption, true);
                return;
            } else {
                if (overlay) overlay.classList.add('hidden');
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
        }
"""
    content = content[:idx] + new_update_logic + content[end_idx:]

# 2. Fix the place where updateChart(getSelectedNodesInfo()) is called in tree click to ALSO call updateTopCharts()
content = content.replace("updateChart(getSelectedNodesInfo());", "updateChart(getSelectedNodesInfo()); updateTopCharts();")

# But wait, we DONT want updateTopCharts() when selector changes!
# So for levelSelector event:
level_selector_fix = """
        const levelSelector = document.getElementById('chart-level-selector');
        if (levelSelector) {
            levelSelector.addEventListener('change', () => {
                updateChart(getSelectedNodesInfo()); // ONLY updates the compare chart
            });
        }
"""
content = re.sub(r'const levelSelector = document.getElementById\(\'chart-level-selector\'\);.*?\}\);.*?\}', level_selector_fix, content, flags=re.DOTALL)


# 3. Add "违规扣减" and "人工调账" to table
tr_wg = '<tr class="hover:bg-gray-50"><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">TX_20231024_8894</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">2023-10-24 14:33:22</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">赵六</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">10886</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">135****3333</td><td class="px-6 py-4 whitespace-nowrap text-[11px]"><span class="px-2 py-1 text-[11px] font-medium rounded bg-red-100 text-red-800">违规扣减</span></td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">完成日常互动转发（微信视频号）领取无按时提交</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900"><span class="text-red-600 font-bold">-50</span></td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">850</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900"><span class="text-gray-400">-</span></td></tr>'
tr_rg = '<tr class="hover:bg-gray-50"><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">TX_20231024_8895</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">2023-10-24 14:34:22</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">孙七</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">11045</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">189****6666</td><td class="px-6 py-4 whitespace-nowrap text-[11px]"><span class="px-2 py-1 text-[11px] font-medium rounded bg-yellow-100 text-yellow-800">人工调账</span></td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">客诉补偿：上月精华发帖漏算XP</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900"><span class="text-green-600 font-bold">+200</span></td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900">3,000</td><td class="px-6 py-4 whitespace-nowrap text-[11px] text-gray-900"><span class="text-gray-400">-</span></td></tr>'

# Let's replace the 4th and 5th tr with these two new ones.
# First extract all trs
idx_tbody = content.find('<tbody class="bg-white divide-y divide-gray-100 text-[11px]">')
idx_tbody_end = content.find('</tbody>', idx_tbody)

if idx_tbody != -1 and idx_tbody_end != -1:
    tbody_html = content[idx_tbody:idx_tbody_end]
    trs = tbody_html.split('</tr>')
    if len(trs) > 5:
        trs[3] = tr_wg
        trs[4] = tr_rg
    
    new_tbody_html = "</tr>".join(trs)
    content = content[:idx_tbody] + new_tbody_html + content[idx_tbody_end:]

with open(filepath, "w") as f:
    f.write(content)

print("Updated JS and table successfully!")
