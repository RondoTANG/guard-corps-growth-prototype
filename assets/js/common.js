/* ========================================================
   C端成长中心 - 状态切换逻辑
======================================================== */
const states = {
    'normal': { tier: 2, xp: 1850, newXp: 450, expiringXp: 120, nextTierName: '大师', nextTierXp: 2500, protection: false, softLanding: false, isMax: false },
    'protection': { tier: 2, xp: 1050, newXp: 0, expiringXp: 300, nextTierName: '大师', nextTierXp: 2500, protection: true, softLanding: false, isMax: false },
    'soft-landing': { tier: 1, xp: 0, newXp: 0, expiringXp: 0, nextTierName: '专家', nextTierXp: 1000, protection: false, softLanding: true, isMax: false },
    'master': { tier: 3, xp: 3200, newXp: 200, expiringXp: 0, nextTierName: '', nextTierXp: 2500, protection: false, softLanding: false, isMax: true }
};

const tierNames = ['新秀', '熟练', '专家', '大师'];

function setDemoState(stateKey) {
    if (!document.getElementById('btn-normal')) return; // 确保在C端页面执行

    // Update Buttons
    ['normal', 'protection', 'soft-landing', 'master'].forEach(k => {
        const btn = document.getElementById('btn-' + k);
        if (k === stateKey) {
            btn.className = "px-3 py-2 text-xs font-bold rounded-lg bg-dfred text-white transition";
        } else {
            btn.className = "px-3 py-2 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition";
        }
    });

    const data = states[stateKey];

    // Update Alerts
    document.getElementById('alert-protection').style.display = data.protection ? 'flex' : 'none';
    document.getElementById('alert-soft-landing').style.display = data.softLanding ? 'flex' : 'none';

    // Update Nodes
    for(let i=0; i<4; i++) {
        const node = document.getElementById('node-' + i);
        const label = document.getElementById('label-' + i);
        const tooltip = document.getElementById('tooltip-' + i);
        const container = document.getElementById('node-container-' + i);

        if (container) container.classList.remove('-mt-[6px]');
        if (tooltip) tooltip.classList.add('hidden');

        if (i < data.tier) {
            // Passed
            node.className = "w-[32px] h-[32px] rounded-full bg-dfred border-[2px] border-white shadow-sm flex items-center justify-center transition-all";
            node.innerHTML = '<i class="fas fa-check text-white text-[12px]"></i>';
            label.className = "text-[11px] text-gray-500 mt-2 font-medium";
        } else if (i === data.tier) {
            // Current
            if (container) container.classList.add('-mt-[6px]');
            if (tooltip) tooltip.classList.remove('hidden');
            node.className = "w-[44px] h-[44px] rounded-full bg-gradient-to-br from-red-500 to-dfred border-[3px] border-white shadow-[0_4px_12px_rgba(224,30,46,0.3)] flex items-center justify-center transition-all";
            node.innerHTML = '<i class="fas fa-crown text-white text-[18px]"></i>';
            label.className = "text-[13px] text-gray-900 mt-1.5 font-bold tracking-wide";
        } else {
            // Locked
            node.className = "w-[32px] h-[32px] rounded-full bg-white border-[2px] border-gray-200 shadow-sm flex items-center justify-center transition-all";
            node.innerHTML = '<i class="fas fa-lock text-gray-300 text-[10px]"></i>';
            label.className = "text-[11px] text-gray-400 mt-2 font-medium";
        }
    }

    // Update Progress Line
    const lineProgressMap = {0: 0, 1: 33.3, 2: 66.6, 3: 100};
    document.getElementById('progress-line').style.width = `calc(${lineProgressMap[data.tier]}% - 32px)`;

    // Update Progress Card
    document.getElementById('display-xp').innerText = data.xp;
    document.getElementById('display-new-xp').innerText = "+" + data.newXp;
    document.getElementById('display-expiring-xp').innerText = "-" + data.expiringXp;
    
    let percent = data.isMax ? 100 : (data.xp / data.nextTierXp) * 100;
    document.getElementById('bar-progress').style.width = `${percent}%`;

    if (data.isMax) {
        document.getElementById('progress-labels').innerHTML = `<span>大师 (${data.xp})</span><span class="text-dfred font-bold">已达顶峰</span>`;
        document.getElementById('progress-desc').innerHTML = `近12个月滚动累计 · 已达最高段位，保持活跃防跌落`;
    } else {
        let base = tierNames[data.tier];
        document.getElementById('progress-labels').innerHTML = `<span>${base} (${data.xp - data.newXp})</span><span class="text-dfred font-bold">${data.nextTierName} (${data.nextTierXp})</span>`;
        document.getElementById('progress-desc').innerHTML = `近12个月滚动累计 · 距离升段还差 <span class="text-dfred font-bold">${data.nextTierXp - data.xp} XP</span>`;
    }

    // Update Privileges
    let unlockedCount = data.tier >= 2 ? (data.isMax ? 3 : 2) : 1;
    document.getElementById('privilege-count').innerText = `已解锁 ${unlockedCount} 项`;

    // Priv 2
    const p2 = document.getElementById('priv-2');
    const p2Lock = document.getElementById('priv-2-lock');
    const p2IconBg = document.getElementById('priv-2-icon-bg');
    const p2Icon = document.getElementById('priv-2-icon');
    const p2Title = document.getElementById('priv-2-title');
    
    if (data.tier >= 2) {
        p2.className = "flex-1 bg-white rounded-[16px] p-3 shadow-[0_2px_10px_rgba(0,0,0,0.03)] border border-gray-100 flex flex-col items-center text-center relative overflow-hidden transition-all";
        p2Lock.classList.add('hidden');
        p2IconBg.className = "w-11 h-11 rounded-full bg-gradient-to-br from-blue-50 to-blue-100/50 border border-blue-100 flex items-center justify-center mb-2";
        p2Icon.className = "fas fa-award text-blue-500 text-lg";
        p2Title.className = "text-xs font-bold text-gray-800";
    } else {
        p2.className = "flex-1 bg-gray-50/50 rounded-[16px] p-3 border border-gray-100 flex flex-col items-center text-center opacity-60 grayscale-[30%] relative overflow-hidden transition-all";
        p2Lock.classList.remove('hidden');
        p2IconBg.className = "w-11 h-11 rounded-full bg-gray-200 border border-transparent flex items-center justify-center mb-2 mt-1";
        p2Icon.className = "fas fa-award text-gray-400 text-lg";
        p2Title.className = "text-xs font-bold text-gray-500";
    }

    // Priv 3
    const p3 = document.getElementById('priv-3');
    const p3Lock = document.getElementById('priv-3-lock');
    const p3IconBg = document.getElementById('priv-3-icon-bg');
    const p3Icon = document.getElementById('priv-3-icon');
    const p3Title = document.getElementById('priv-3-title');

    if (data.isMax) {
        p3.className = "flex-1 bg-white rounded-[16px] p-3 shadow-[0_2px_10px_rgba(0,0,0,0.03)] border border-gray-100 flex flex-col items-center text-center relative overflow-hidden transition-all";
        p3Lock.classList.add('hidden');
        p3IconBg.className = "w-11 h-11 rounded-full bg-gradient-to-br from-amber-50 to-amber-100/50 border border-amber-100 flex items-center justify-center mb-2";
        p3Icon.className = "fas fa-gift text-amber-500 text-lg";
        p3Title.className = "text-xs font-bold text-gray-800";
    } else {
        p3.className = "flex-1 bg-gray-50/50 rounded-[16px] p-3 border border-gray-100 flex flex-col items-center text-center opacity-60 grayscale-[30%] relative overflow-hidden transition-all";
        p3Lock.classList.remove('hidden');
        p3IconBg.className = "w-11 h-11 rounded-full bg-gray-200 border border-transparent flex items-center justify-center mb-2 mt-1";
        p3Icon.className = "fas fa-gift text-gray-400 text-lg";
        p3Title.className = "text-xs font-bold text-gray-500";
    }
}

/* ========================================================
   B端配置大盘 - Tab切换逻辑
======================================================== */
function switchTab(tabId) {
    if (!document.getElementById('tab-tier')) return; // 确保在B端页面执行

    // Hide all tabs
    document.getElementById('tab-tier').classList.add('hidden');
    document.getElementById('tab-global').classList.add('hidden');
    document.getElementById('tab-task').classList.add('hidden');
    
    // Reset tab buttons
    document.getElementById('btn-tab-tier').className = "pb-3 px-1 tab-inactive text-sm";
    document.getElementById('btn-tab-global').className = "pb-3 px-1 tab-inactive text-sm";
    document.getElementById('btn-tab-task').className = "pb-3 px-1 tab-inactive text-sm";

    // Show active tab
    document.getElementById(tabId).classList.remove('hidden');
    document.getElementById('btn-' + tabId).className = "pb-3 px-1 tab-active text-sm";
}
