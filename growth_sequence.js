// 成长体系运转时序图 - Mermaid 源码
// 由 HTML 通过 <script src> 加载，渲染到 #mermaid-container
(function() {
    var code = `sequenceDiagram
    autonumber
    actor OP as 运营人员
    actor User as 护卫军用户
    participant TaskSys as 任务大厅
    participant GrowthSys as 成长体系服务

    rect rgb(240, 248, 255)
    note right of OP: 1. 运营动作：规则配置、人工干预、作业发放
    OP->>GrowthSys: 全局配置 (段位门槛/保级天数等)
    OP->>GrowthSys: 人工调账 (后台触发XP增补或扣回)
    OP->>TaskSys: 发布日常/高优激励作业
    end

    rect rgb(245, 255, 245)
    note right of OP: 2. 用户XP获取、违规扣减与到期扣除
    User->>TaskSys: 领取并完成作业 (发帖/转评赞等)
    TaskSys->>GrowthSys: 验收通过，发放正向XP (带时间戳)
    GrowthSys->>GrowthSys: 夜间定时跑批任务
    alt 存在满365天的正向XP记录
        GrowthSys->>GrowthSys: 【自然核销】自动扣除过期XP (无通知，明细可查)
    end
    alt 用户产生违规行为 (如恶意刷单)
        GrowthSys->>GrowthSys: 【违规扣减】即刻扣除相关XP (不受365天限制)
    end
    end

    rect rgb(255, 245, 245)
    note right of OP: 3. 降级保护状态机 (保级缓冲与软着陆)
    GrowthSys->>GrowthSys: 触发状态判定 (XP变动或跑批结算)
    alt 正常状态：XP跌破门槛，且为高段位
        GrowthSys->>User: 正常 ➞ 进入【保级缓冲期】 (开启90天倒计时，特权保留)
    else 缓冲期内：用户做作业使XP重新达标
        GrowthSys->>User: 保级缓冲期 ➞ 恢复【正常】状态 (倒计时解除)
    else 缓冲期满：XP仍未达标
        GrowthSys->>User: 保级缓冲期 ➞ 【荣誉保底】 (触发软着陆，仅降一级托底)
    else 长期沉睡：XP被扣光且无保底资格
        GrowthSys->>User: 任何状态 ➞ 【退出暂不评级】 (掉出核心护卫军体系)
    end
    end`;

    document.addEventListener('DOMContentLoaded', function() {
        var container = document.getElementById('mermaid-container');
        if (!container) return;
        mermaid.render('mermaid-svg', code).then(function(result) {
            container.innerHTML = result.svg;
        }).catch(function(err) {
            console.error('Mermaid render error:', err);
            container.innerHTML = '<p style="color:red;">时序图渲染失败，请检查控制台。</p>';
        });
    });
})();
