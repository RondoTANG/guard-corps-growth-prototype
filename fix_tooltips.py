import re

html_file = '/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_作业管理列表.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add a CSS class for tooltip in the <style> section if it exists, or just add it
tooltip_css = """
        .custom-tooltip {
            position: relative;
            display: inline-block;
            cursor: help;
        }
        .custom-tooltip .tooltip-text {
            visibility: hidden;
            width: max-content;
            background-color: rgba(0,0,0,0.75);
            color: #fff;
            text-align: center;
            border-radius: 4px;
            padding: 6px 10px;
            position: absolute;
            z-index: 50;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.2s;
            font-size: 12px;
            font-weight: normal;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        .custom-tooltip .tooltip-text::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: rgba(0,0,0,0.75) transparent transparent transparent;
        }
        .custom-tooltip:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
"""

if '.custom-tooltip' not in content:
    content = content.replace('</style>', tooltip_css + '\n    </style>')

# Replace the native title tooltips with the custom CSS tooltips
content = content.replace(
    '<th class="py-3 px-4 font-medium min-w-[100px]">承接门槛 <i class="fas fa-info-circle text-gray-400 ml-1 cursor-help" title="承接此任务需满足的段位或XP要求"></i></th>',
    '<th class="py-3 px-4 font-medium min-w-[100px]">承接门槛 <div class="custom-tooltip"><i class="fas fa-info-circle text-gray-400 ml-1"></i><span class="tooltip-text">承接此任务需满足的段位或XP要求</span></div></th>'
)

content = content.replace(
    '<th class="py-3 px-4 font-medium min-w-[100px]">单次发放XP <i class="fas fa-info-circle text-gray-400 ml-1 cursor-help" title="完成此任务后系统发放的成长经验值"></i></th>',
    '<th class="py-3 px-4 font-medium min-w-[100px]">单次发放XP <div class="custom-tooltip"><i class="fas fa-info-circle text-gray-400 ml-1"></i><span class="tooltip-text">完成此任务后系统发放的成长经验值</span></div></th>'
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

