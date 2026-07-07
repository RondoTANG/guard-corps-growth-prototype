import re

filepath = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"
with open(filepath, "r") as f:
    content = f.read()

# 1. Remove the sentence
text_to_remove = """                        <div class="mt-2 flex items-center gap-2">
                            <span class="text-xs text-gray-400">其中 45 人晋升至Level3专家</span>
                        </div>"""
content = content.replace(text_to_remove, "")

# 2. Add the HTML for trend chart right after orgCompareChart block
html_to_add = """                    <div class="h-80 w-full" id="orgCompareChart"></div>
                </div>

                <!-- Trend Chart Section -->
                <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-5 mt-6 mb-6">
                    <div class="flex justify-between items-center border-b border-gray-100 pb-3 mb-4">
                        <h3 class="font-bold text-gray-800 text-base">
                            <div class="flex items-center group cursor-help relative">组织晋升与降级趋势分析 (近30天)
                                <i class="far fa-question-circle text-gray-300 ml-1 hover:text-gray-500 transition-colors text-xs"></i>
                                <div class="absolute left-0 top-full mt-2 hidden group-hover:block w-72 bg-gray-800 text-white text-xs rounded p-2 z-50 shadow-lg font-normal">
                                    展示当前选中组织（含子组织）在过去30天内，每日触发定级规则成功晋级或保级失败降级的人次波动趋势。
                                    <div class="absolute left-4 bottom-full w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                                </div>
                            </div>
                        </h3>
                    </div>
                    <div class="h-64 w-full" id="trendChart"></div>
                </div>"""

content = content.replace("""                    <div class="h-80 w-full" id="orgCompareChart"></div>
                </div>""", html_to_add)

# 3. Add JS for trendChart
js_setup_to_add = """            var orgChartDom = document.getElementById('orgCompareChart');
            var orgChart;
            var trendChartDom = document.getElementById('trendChart');
            var trendChart;"""

content = content.replace("""            var orgChartDom = document.getElementById('orgCompareChart');
            var orgChart;""", js_setup_to_add)

# Add trendChart initialization and resize
js_init_to_add = """                if (orgChartDom) {
                    orgChart = echarts.init(orgChartDom);
                }
                
                if (trendChartDom) {
                    trendChart = echarts.init(trendChartDom);
                    window.addEventListener('resize', () => {
                        if (trendChart) trendChart.resize();
                    });
                }"""

content = content.replace("""                if (orgChartDom) {
                    orgChart = echarts.init(orgChartDom);
                }""", js_init_to_add)

# Add data generation in updateTopCharts
js_data_to_add = """                if (window.statusChart && window.statusOption) {
                    let normalVal = Math.floor(75 + pseudoRandom() * 15);
                    let bufferVal = Math.floor(5 + pseudoRandom() * 10);
                    let floorVal = 100 - normalVal - bufferVal;

                    window.statusOption.series[0].data = [
                        { value: normalVal, name: '正常', itemStyle: { color: '#10B981' } },
                        { value: bufferVal, name: '保级缓冲', itemStyle: { color: '#D97706' } },
                        { value: floorVal, name: '荣誉保底', itemStyle: { color: '#EF4444' } }
                    ];

                    const txtNormal = document.getElementById('status-text-normal');
                    if (txtNormal) txtNormal.textContent = `正常: ${normalVal}%`;
                    const txtBuffer = document.getElementById('status-text-buffer');
                    if (txtBuffer) txtBuffer.textContent = `保级缓冲: ${bufferVal}%`;
                    const txtFloor = document.getElementById('status-text-floor');
                    if (txtFloor) txtFloor.textContent = `荣誉保底: ${floorVal}%`;
                    window.statusChart.setOption(window.statusOption);
                }
                
                if (trendChart) {
                    let dates = [];
                    let promoData = [];
                    let demoData = [];
                    for(let i=30; i>=1; i--) {
                        let d = new Date();
                        d.setDate(d.getDate() - i);
                        dates.push((d.getMonth()+1)+'/'+d.getDate());
                        
                        let basePromo = 10 + Math.floor(pseudoRandom() * 30);
                        let baseDemo = Math.floor(pseudoRandom() * 15);
                        
                        // Add some volatility
                        let vol = Math.sin(i) * 5;
                        promoData.push(Math.max(0, Math.floor(basePromo + vol)));
                        demoData.push(Math.max(0, Math.floor(baseDemo + vol*0.5)));
                    }
                    
                    let trendOption = {
                        tooltip: { trigger: 'axis' },
                        legend: { data: ['晋升人次', '降级人次'], bottom: 0 },
                        grid: { left: '3%', right: '4%', bottom: '15%', top: '10%', containLabel: true },
                        xAxis: { type: 'category', boundaryGap: false, data: dates },
                        yAxis: { type: 'value' },
                        series: [
                            { 
                                name: '晋升人次', type: 'line', smooth: true, 
                                itemStyle: { color: '#F59E0B' }, 
                                areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: 'rgba(245,158,11,0.3)'}, {offset: 1, color: 'rgba(245,158,11,0)'}]) }, 
                                data: promoData 
                            },
                            { 
                                name: '降级人次', type: 'line', smooth: true, 
                                itemStyle: { color: '#EF4444' }, 
                                areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: 'rgba(239,68,68,0.3)'}, {offset: 1, color: 'rgba(239,68,68,0)'}]) }, 
                                data: demoData 
                            }
                        ]
                    };
                    trendChart.setOption(trendOption);
                }"""

content = content.replace("""                if (window.statusChart && window.statusOption) {
                    let normalVal = Math.floor(75 + pseudoRandom() * 15);
                    let bufferVal = Math.floor(5 + pseudoRandom() * 10);
                    let floorVal = 100 - normalVal - bufferVal;

                    window.statusOption.series[0].data = [
                        { value: normalVal, name: '正常', itemStyle: { color: '#10B981' } },
                        { value: bufferVal, name: '保级缓冲', itemStyle: { color: '#D97706' } },
                        { value: floorVal, name: '荣誉保底', itemStyle: { color: '#EF4444' } }
                    ];

                    const txtNormal = document.getElementById('status-text-normal');
                    if (txtNormal) txtNormal.textContent = `正常: ${normalVal}%`;
                    const txtBuffer = document.getElementById('status-text-buffer');
                    if (txtBuffer) txtBuffer.textContent = `保级缓冲: ${bufferVal}%`;
                    const txtFloor = document.getElementById('status-text-floor');
                    if (txtFloor) txtFloor.textContent = `荣誉保底: ${floorVal}%`;
                    window.statusChart.setOption(window.statusOption);
                }""", js_data_to_add)

# Empty out trend chart if nothing selected
js_empty_to_add = """                    if (window.statusChart && window.statusOption) {
                        window.statusOption.series[0].data = [];
                        window.statusChart.setOption(window.statusOption, true);
                    }
                    if (trendChart) {
                        trendChart.clear();
                    }"""

content = content.replace("""                    if (window.statusChart && window.statusOption) {
                        window.statusOption.series[0].data = [];
                        window.statusChart.setOption(window.statusOption, true);
                    }""", js_empty_to_add)

with open(filepath, "w") as f:
    f.write(content)

print("Added trend chart successfully!")
