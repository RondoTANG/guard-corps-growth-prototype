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

const tierPrivileges = [
    { title: "新秀护卫军", count: 1, items: [
        { icon: "fas fa-handshake", color: "blue", name: "基础特权", desc: "基础作业领取" }
    ]},
    { title: "熟练护卫军", count: 1, items: [
        { icon: "fas fa-shield-alt", color: "green", name: "常规特权", desc: "常规作业领取" }
    ]},
    { title: "专家护卫军", count: 2, items: [
        { icon: "fas fa-award", color: "blue", name: "发光徽章", desc: "专家专属标识" },
        { icon: "fas fa-bolt", color: "red", name: "作业绿通", desc: "高优任务优先领" }
    ]},
    { title: "大师护卫军", count: 3, items: [
        { icon: "fas fa-crown", color: "amber", name: "身份标识", desc: "大师专属标识" },
        { icon: "fas fa-users", color: "purple", name: "直面高管", desc: "圆桌会议" },
        { icon: "fas fa-rocket", color: "red", name: "1.5倍加速", desc: "积分获取加速" }
    ]}
];

let currentUserState = null;

function renderPrivileges(tierIndex) {
    const data = tierPrivileges[tierIndex];
    const titleEl = document.getElementById('preview-tier-title');
    const countEl = document.getElementById('preview-privilege-count');
    const container = document.getElementById('privileges-container');
    
    if(!titleEl || !container) return;

    titleEl.innerText = `${data.title} 专属特权`;
    countEl.innerText = `可享 ${data.count} 项特权`;
    
    let html = '';
    data.items.forEach(item => {
        let isLocked = (currentUserState && currentUserState.tier < tierIndex);
        let opacityClass = isLocked ? "opacity-60 grayscale-[30%]" : "";
        let lockHtml = isLocked ? `<div class="absolute -right-2 top-0 bg-gray-200 text-[8px] text-gray-500 px-3 py-0.5 rounded-bl font-medium shadow-sm"><i class="fas fa-lock mr-1"></i> 锁定</div>` : "";
        
        let bgMap = {
            "red": "from-red-50 to-red-100/50 border-red-100 text-red-500",
            "blue": "from-blue-50 to-blue-100/50 border-blue-100 text-blue-500",
            "amber": "from-amber-50 to-amber-100/50 border-amber-100 text-amber-500",
            "green": "from-green-50 to-green-100/50 border-green-100 text-green-500",
            "purple": "from-purple-50 to-purple-100/50 border-purple-100 text-purple-500",
        };
        
        let iconBg = isLocked ? "bg-gray-200 border-transparent text-gray-400" : bgMap[item.color];
        
        html += `
        <div class="flex-1 min-w-[95px] max-w-[110px] bg-white rounded-[16px] p-3 shadow-[0_2px_10px_rgba(0,0,0,0.03)] border border-gray-100 flex flex-col items-center text-center relative overflow-hidden transition-all ${opacityClass}">
            ${lockHtml}
            <div class="w-11 h-11 rounded-full bg-gradient-to-br ${iconBg} border flex items-center justify-center mb-2">
                <i class="${item.icon} text-lg ${isLocked ? 'text-gray-400' : ''}"></i>
            </div>
            <div class="text-xs font-bold ${isLocked ? 'text-gray-500' : 'text-gray-800'}">${item.name}</div>
            <div class="text-[9px] ${isLocked ? 'text-gray-400' : 'text-gray-500'} mt-1 scale-90 whitespace-nowrap">${item.desc}</div>
        </div>
        `;
    });
    
    container.innerHTML = html;
}

function previewTier(index) {
    if(!document.getElementById('node-0')) return;
    
    for(let i=0; i<4; i++) {
        let node = document.getElementById('node-' + i);
        let label = document.getElementById('label-' + i);
        let indicator = node.querySelector('.preview-indicator');
        
        if (i === index) {
            if (indicator) indicator.classList.remove('hidden');
            label.className = "text-[13px] text-dfred mt-1.5 font-bold tracking-wide transition-all";
            if (!node.classList.contains('scale-[1.15]')) node.classList.add('scale-[1.15]');
        } else {
            if (indicator) indicator.classList.add('hidden');
            label.className = "text-[11px] text-gray-500 mt-2 font-medium transition-all";
            node.classList.remove('scale-[1.15]');
        }
    }
    renderPrivileges(index);
}

function setDemoState(stateKey) {
    if (!document.getElementById('btn-normal')) return;

    ['normal', 'protection', 'soft-landing', 'master'].forEach(k => {
        const btn = document.getElementById('btn-' + k);
        if (k === stateKey) {
            btn.className = "px-3 py-2 text-xs font-bold rounded-lg bg-dfred text-white transition";
        } else {
            btn.className = "px-3 py-2 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition";
        }
    });

    const data = states[stateKey];
    currentUserState = data;

    document.getElementById('alert-protection').style.display = data.protection ? 'flex' : 'none';
    document.getElementById('alert-soft-landing').style.display = data.softLanding ? 'flex' : 'none';

    for(let i=0; i<4; i++) {
        const node = document.getElementById('node-' + i);
        const icon = node.querySelector('i:not(.preview-indicator)');
        
        node.className = "w-[32px] h-[32px] rounded-full flex items-center justify-center transition-all relative";
        
        if (i < data.tier) {
            node.classList.add('bg-dfred', 'border-[2px]', 'border-white', 'shadow-sm');
            icon.className = "fas fa-check text-white text-[12px]";
        } else if (i === data.tier) {
            node.className = "w-[42px] h-[42px] rounded-full bg-gradient-to-br from-red-500 to-dfred border-[3px] border-white shadow-[0_4px_12px_rgba(224,30,46,0.3)] flex items-center justify-center transition-all relative";
            icon.className = "fas fa-crown text-white text-[16px]";
        } else {
            node.classList.add('bg-gray-50', 'border-[2px]', 'border-gray-200', 'shadow-sm');
            icon.className = "fas fa-lock text-gray-300 text-[10px]";
        }
    }

    const lineProgressMap = {0: 0, 1: 33.3, 2: 66.6, 3: 100};
    document.getElementById('progress-line').style.width = `calc(${lineProgressMap[data.tier]}% - 32px)`;

    document.getElementById('display-xp').innerText = data.xp;
    document.getElementById('display-new-xp').innerText = "+" + data.newXp;
    document.getElementById('display-expiring-xp').innerText = "-" + data.expiringXp;
    document.getElementById('display-tier-badge').innerText = tierPrivileges[data.tier].title;

    let percent = data.isMax ? 100 : (data.xp / data.nextTierXp) * 100;
    document.getElementById('bar-progress').style.width = `${percent}%`;

    const progContainer = document.getElementById('progress-container');
    const progMaxContainer = document.getElementById('progress-container-max');
    
    if (data.isMax) {
        if(progContainer) progContainer.classList.add('hidden');
        if(progMaxContainer) progMaxContainer.classList.remove('hidden');
    } else {
        if(progContainer) progContainer.classList.remove('hidden');
        if(progMaxContainer) progMaxContainer.classList.add('hidden');
        
        let base = tierNames[data.tier];
        document.getElementById('progress-labels').innerHTML = `<span>${base} (${data.xp - data.newXp})</span><span class="text-dfred font-bold">${data.nextTierName} (${data.nextTierXp})</span>`;
        document.getElementById('progress-desc').innerHTML = `近12个月滚动累计 · 距离升段还差 <span class="text-dfred font-bold">${data.nextTierXp - data.xp} XP</span>`;
    }

    previewTier(data.tier);
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('btn-normal')) {
        setDemoState('normal');
    }
});

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
