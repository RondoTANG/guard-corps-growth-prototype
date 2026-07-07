 ---
        function switchPage(pageId) {
            // Hide all pages
            document.querySelectorAll('.page-content').forEach(el => el.classList.remove('active'));
            // Reset all nav items
            document.querySelectorAll('.nav-item').forEach(el => {
                el.classList.remove('bg-[#3B82F6]', 'text-white', 'font-bold');
                el.classList.add('text-gray-400');
            });
            
            // Show target page
            document.getElementById('page-' + pageId).classList.add('active');
            
            // Highlight nav item
            const navItem = document.getElementById('nav-' + pageId);
            if (navItem) {
                navItem.classList.remove('text-gray-400');
                navItem.classList.add('bg-[#3B82F6]', 'text-white', 'font-bold');
                
                // Ensure parent group is open (simulated by highlighting group header text)
                const group = navItem.closest('.menu-group');
                if (group) {
                    const groupTitle = group.querySelector('span');
                    if (groupTitle) groupTitle.classList.replace('text-gray-200', 'text-white');
                }
            }
            
            // Trigger ECharts resize if dashboard
            if (pageId === 'dashboard' && window.tierChart && window.conversionChart) {
                setTimeout(() => {
                    window.tierChart.resize();
                    window.conversionChart.resize();
                }, 50);
            }
        }
        
        // --- Extracted Scripts from Pages ---
        
        let currentAddBtn = null;
        let isEditing = false;

        
        function switchConfigTab(tabId) {
            // Hide all tabs
            ['tab-tier', 'tab-global', 'tab-task'].forEach(id => {
                document.getElementById(id).classList.add('hidden');
                const btn = document.getElementById('btn-' + id);
                btn.classList.remove('tab-active', 'text-dfred', 'font-bold', 'border-b-2', 'border-dfred');
                btn.classList.add('tab-inactive', 'text-gray-500');
            });
            
            // Show active tab
            document.getElementById(tabId).classList.remove('hidden');
            const activeBtn = document.getElementById('btn-' + tabId);
            activeBtn.classList.remove('tab-inactive', 'text-gray-500');
            activeBtn.classList.add('tab-active', 'text-dfred', 'font-bold', 'border-b-2', 'border-dfred');
        }

        function showToast(message) {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'bg-gray-800 text-white px-6 py-3 rounded shadow-lg text-sm flex items-center gap-2 transform transition-all duration-300 -translate-y-10 opacity-0';
            toast.innerHTML = `<i class="fas fa-check-circle text-green-400"></i> <span>${message}</span>`;
            container.appendChild(toast);
            
            // Trigger animation
            requestAnimationFrame(() => {
                toast.classList.remove('-translate-y-10', 'opacity-0');
            });

            // Auto remove
            setTimeout(() => {
                toast.classList.add('-translate-y-10', 'opacity-0');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        function togglePrivilegeConfig() {
            const type = document.getElementById('priv-type-select').value;
            document.getElementById('config-block-points').classList.add('hidden');
            document.getElementById('config-block-task').classList.add('hidden');
            document.getElementById('config-block-identity').classList.add('hidden');
            
            document.getElementById('config-block-' + type).classList.remove('hidden');
        }

        function openPrivilegeDrawer(level, privName, btn = null) {
            currentAddBtn = btn;
            isEditing = !!privName;
            
            document.getElementById('drawer-level').value = level;
            document.getElementById('drawer-priv-name').value = privName || '';
            document.getElementById('drawer-title').innerText = isEditing ? '编辑特权' : '新增特权';

            if (!isEditing) {
                document.getElementById('priv-type-select').value = 'points';
                togglePrivilegeConfig();
            }
            
            const overlay = document.getElementById('privilege-drawer-overlay');
            const drawer = document.getElementById('privilege-drawer');
            
            overlay.classList.remove('hidden');
            void overlay.offsetWidth; // reflow
            overlay.classList.remove('opacity-0');
            drawer.classList.remove('translate-x-full');
        }

        function closePrivilegeDrawer() {
            const overlay = document.getElementById('privilege-drawer-overlay');
            const drawer = document.getElementById('privilege-drawer');
            
            overlay.classList.add('opacity-0');
            drawer.classList.add('translate-x-full');
            
            setTimeout(() => {
                overlay.classList.add('hidden');
            }, 300);
        }

        function savePrivilege() {
            const privNameInput = document.getElementById('drawer-priv-name').value.trim();
            const privName = privNameInput || '新特权配置';

            if (!isEditing && currentAddBtn) {
                // Dynamically add a new privilege card to the UI
                const newCard = document.createElement('div');
                newCard.className = "flex items-center justify-between bg-white border border-red-200 rounded p-2 mb-2";
                newCard.innerHTML = `
                    <div class="flex items-center gap-2">
                        <span class="text-xs bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded">新增类</span>
                        <span class="text-sm text-gray-800">${privName}</span>
                    </div>
                    <button onclick="openPrivilegeDrawer(document.getElementById('drawer-level').value, '${privName}')" class="text-dfred hover:text-red-700 text-xs font-medium"><i class="fas fa-cog"></i> 配置</button>
                `;
                const addBtnContainer = currentAddBtn.closest('div');
                addBtnContainer.parentNode.insertBefore(newCard, addBtnContainer);
            }

            showToast('特权配置已临时保存在页面中。正式环境需点击左上角“保存并发布”！');
            closePrivilegeDrawer();
        }
    

        let currentXp = 0;

        function showToast(message, type = 'success') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            const icon = type === 'success' ? '<i class="fas fa-check-circle text-green-400"></i>' : '<i class="fas fa-exclamation-circle text-red-400"></i>';
            toast.className = 'bg-gray-800 text-white px-6 py-3 rounded shadow-lg text-sm flex items-center gap-2 transform transition-all duration-300 -translate-y-10 opacity-0';
            toast.innerHTML = `${icon} <span>${message}</span>`;
            container.appendChild(toast);
            
            requestAnimationFrame(() => {
                toast.classList.remove('-translate-y-10', 'opacity-0');
            });

            setTimeout(() => {
                toast.classList.add('-translate-y-10', 'opacity-0');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        function openXpDrawer(id, name, tier, xp) {
            currentXp = xp;
            document.getElementById('drawer-user-id').innerText = `(ID: ${id})`;
            document.getElementById('drawer-user-name').innerText = name;
            document.getElementById('drawer-user-tier').innerText = tier;
            document.getElementById('drawer-user-xp').innerText = xp;
            
            document.getElementById('drawer-amount').value = '';
            document.getElementById('preview-balance').innerText = '--';

            const overlay = document.getElementById('xp-drawer-overlay');
            const drawer = document.getElementById('xp-drawer');
            
            overlay.classList.remove('hidden');
            void overlay.offsetWidth; 
            overlay.classList.remove('opacity-0');
            drawer.classList.remove('translate-x-full');
        }

        function closeXpDrawer() {
            const overlay = document.getElementById('xp-drawer-overlay');
            const drawer = document.getElementById('xp-drawer');
            
            overlay.classList.add('opacity-0');
            drawer.classList.add('translate-x-full');
            
            setTimeout(() => {
                overlay.classList.add('hidden');
            }, 300);
        }

        function toggleXpType() {
            const type = document.querySelector('input[name="xp_type"]:checked').value;
            const addLbl = document.getElementById('type-add-lbl');
            const deductLbl = document.getElementById('type-deduct-lbl');
            const prefix = document.getElementById('amount-prefix');

            if(type === 'add') {
                addLbl.className = 'flex-1 flex items-center justify-center gap-2 border-2 border-green-500 bg-green-50 rounded-md py-2 cursor-pointer relative';
                addLbl.querySelector('span').className = 'font-bold text-green-700';
                
                deductLbl.className = 'flex-1 flex items-center justify-center gap-2 border border-gray-200 bg-white rounded-md py-2 cursor-pointer relative';
                deductLbl.querySelector('span').className = 'font-medium text-gray-600';
                prefix.innerText = '+';
                prefix.className = 'text-green-600 font-bold';
            } else {
                deductLbl.className = 'flex-1 flex items-center justify-center gap-2 border-2 border-red-500 bg-red-50 rounded-md py-2 cursor-pointer relative';
                deductLbl.querySelector('span').className = 'font-bold text-red-700';
                
                addLbl.className = 'flex-1 flex items-center justify-center gap-2 border border-gray-200 bg-white rounded-md py-2 cursor-pointer relative';
                addLbl.querySelector('span').className = 'font-medium text-gray-600';
                prefix.innerText = '-';
                prefix.className = 'text-red-500 font-bold';
            }
            updatePreview();
        }

        function updatePreview() {
            const type = document.querySelector('input[name="xp_type"]:checked').value;
            const amount = parseInt(document.getElementById('drawer-amount').value) || 0;
            let preview = currentXp;
            if(type === 'add') {
                preview += amount;
            } else {
                preview = Math.max(0, preview - amount);
            }
            document.getElementById('preview-balance').innerText = preview;
        }

        document.getElementById('drawer-amount').addEventListener('input', updatePreview);

        function submitXp() {
            const amount = document.getElementById('drawer-amount').value;
            if(!amount || amount <= 0) {
                showToast('请输入有效的变动额度', 'error');
                return;
            }
            showToast('调账成功！系统流水已生成，用户端余额已更新。');
            closeXpDrawer();
        }
    

        function openEvidenceModal() {
            const overlay = document.getElementById('evidence-modal-overlay');
            const modal = document.getElementById('evidence-modal');
            
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
            void overlay.offsetWidth; // reflow
            overlay.classList.remove('opacity-0');
            modal.classList.remove('scale-95', 'opacity-0');
        }

        function closeEvidenceModal() {
            const overlay = document.getElementById('evidence-modal-overlay');
            const modal = document.getElementById('evidence-modal');
            
            overlay.classList.add('opacity-0');
            modal.classList.add('scale-95', 'opacity-0');
            
            setTimeout(() => {
                overlay.classList.add('hidden');
                overlay.classList.remove('flex');
            }, 300);
        }
    

        // Init ECharts
        document.addEventListener('DOMContentLoaded', function() {
            // Chart 1: Tier Distribution
            window.tierChart = echarts.init(document.getElementById('chart-tier-distribution'));
            var tierOption = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c}人 ({d}%)'
                },
                legend: {
                    bottom: '0%',
                    left: 'center'
                },
                color: ['#9CA3AF', '#3B82F6', '#8B5CF6', '#EF4444'], // Colors for tiers
                series: [
                    {
                        name: '全站段位占比',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 20,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: 8500, name: 'Level 1 (新秀)' },
                            { value: 3100, name: 'Level 2 (熟练)' },
                            { value: 550, name: 'Level 3 (专家)' },
                            { value: 300, name: 'Level 4 (大师)' } // 300 / 12450 = 2.4% (Triggers warning)
                        ]
                    }
                ]
            };
            tierChart.setOption(tierOption);

            // Chart 2: Conversion by Tier
            window.conversionChart = echarts.init(document.getElementById('chart-conversion'));
            var conversionOption = {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: { type: 'shadow' }
                },
                legend: {
                    data: ['作业通过率', '评优率 (加精)']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        data: ['新秀', '熟练', '专家', '大师'],
                        axisTick: { alignWithLabel: true }
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        axisLabel: {
                            formatter: '{value} %'
                        },
                        max: 100
                    }
                ],
                series: [
                    {
                        name: '作业通过率',
                        type: 'bar',
                        barWidth: '20%',
                        itemStyle: { color: '#60A5FA' },
                        data: [65, 82, 91, 98]
                    },
                    {
                        name: '评优率 (加精)',
                        type: 'bar',
                        barWidth: '20%',
                        itemStyle: { color: '#F59E0B' },
                        data: [5, 12, 35, 62]
                    }
                ]
            };
            conversionChart.setOption(conversionOption);

            // Responsive charts on resize
            window.addEventListener('resize', function() {
                tierChart.resize();
                conversionChart.resize();
            });
        });
    
        
        // Init SPA
        document.addEventListener('DOMContentLoaded', () => {
            switchPage('config'); // Default page
        });
    