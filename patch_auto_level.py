import re

filepath = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"
with open(filepath, "r") as f:
    content = f.read()

new_get_info = """
            function getSelectedNodesInfo() {
                let checkedNames = [];
                let checkedLevels = new Set();

                const nodes = sidebar.querySelectorAll('.org-node');
                nodes.forEach(node => {
                    const box = node.querySelector('.checkbox-box');
                    if (getCheckboxState(box) === 1) {
                        const nameSpan = node.querySelector('.flex-1.truncate');
                        if (nameSpan) {
                            let name = nameSpan.textContent.trim();
                            let level = parseInt(node.dataset.level);
                            if (level > 1) { // 过滤掉集团级(L1)，因为1个对比没意义
                                checkedNames.push({name, level});
                                checkedLevels.add(level);
                            }
                        }
                    }
                });

                const levelSelector = document.getElementById('chart-level-selector');
                let forcedLevel = levelSelector ? levelSelector.value : 'auto';
                
                let filteredNames = [];
                let resolvedLevel = null;

                if (forcedLevel === 'auto') {
                    if (checkedLevels.size > 0) {
                        let minLevel = Math.min(...Array.from(checkedLevels));
                        let candidates = checkedNames.filter(n => n.level === minLevel);
                        
                        // 智能向下钻取：如果当前层级只有1个，且下面还有子节点被选中，那对比1个没意义，自动取下一级
                        while (candidates.length === 1 && checkedLevels.has(minLevel + 1)) {
                            minLevel++;
                            candidates = checkedNames.filter(n => n.level === minLevel);
                        }
                        
                        filteredNames = candidates.map(n => n.name);
                        resolvedLevel = minLevel;
                    }
                } else {
                    let targetLevel = parseInt(forcedLevel);
                    filteredNames = checkedNames.filter(n => n.level === targetLevel).map(n => n.name);
                    resolvedLevel = targetLevel;
                }

                // 自动更新下拉框的“自动”文案
                if (levelSelector) {
                    const autoOption = levelSelector.querySelector('option[value="auto"]');
                    if (autoOption) {
                        // 只有在auto模式下才计算auto会落在哪个层级
                        let autoLevelStr = "";
                        if (checkedLevels.size > 0) {
                            let minLevel = Math.min(...Array.from(checkedLevels));
                            let candidates = checkedNames.filter(n => n.level === minLevel);
                            while (candidates.length === 1 && checkedLevels.has(minLevel + 1)) {
                                minLevel++;
                                candidates = checkedNames.filter(n => n.level === minLevel);
                            }
                            const levelNames = {2: '二级党委', 3: '三级党组织', 4: '四级党组织', 5: '党支部'};
                            autoLevelStr = levelNames[minLevel] || '';
                        }
                        autoOption.textContent = autoLevelStr ? `自动(${autoLevelStr})` : '自动(当前选中最高层级)';
                    }
                }

                return {
                    names: filteredNames,
                    count: filteredNames.length,
                    resolvedLevel: resolvedLevel
                };
            }
"""

# Replace getSelectedNodesInfo
content = re.sub(r'function getSelectedNodesInfo\(\) \{.*?return \{\s*names: filteredNames,\s*count: filteredNames\.length\s*\};\s*\}', new_get_info.strip(), content, flags=re.DOTALL)

with open(filepath, "w") as f:
    f.write(content)

print("Updated auto level logic successfully!")
