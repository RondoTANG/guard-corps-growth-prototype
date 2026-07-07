import re

data = [
    ("转发", [
        ("朋友圈", ["转发"]),
        ("知乎", ["转发"]),
        ("微信视频号", ["转发"]),
        ("头条号", ["转发"]),
        ("微博", ["转发"]),
    ]),
    ("原创", [
        ("微信公众号", ["原创"]),
        ("知乎", ["原创"]),
        ("小红书", ["原创"]),
        ("B站", ["原创"]),
        ("快手", ["原创"]),
        ("微信", ["原创"]),
        ("微信视频号", ["原创"]),
        ("头条号", ["原创"]),
        ("抖音", ["原创"]),
        ("微博", ["原创"]),
    ]),
    ("素材分发作业", [
        ("微信公众号", ["素材分发"]),
        ("知乎", ["素材分发"]),
        ("小红书", ["素材分发"]),
        ("B站", ["素材分发"]),
        ("快手", ["素材分发"]),
        ("微信", ["素材分发"]),
        ("微信视频号", ["素材分发"]),
        ("头条号", ["素材分发"]),
        ("抖音", ["素材分发"]),
        ("微博", ["素材分发"]),
    ]),
    ("互动", [
        ("微信公众号", ["互动-点赞帖子类-图片", "互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("视频号直播", ["互动-直播类-评论-图片"]),
        ("抖音直播", ["互动-直播类-评论-图片"]),
        ("知乎", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("小红书", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("B站", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("快手", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("微信", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("微信视频号", ["互动-点赞帖子类-图片", "互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("头条号", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("抖音", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
        ("微博", ["互动-点赞帖子评论类-图片", "互动-评论类-文本/图片"]),
    ]),
    ("其他作业", [
        ("--", ["专属", "直播"]),
    ]),
    ("日常类", [
        ("--", ["每日签到"]),
    ]),
    ("人工干预调账", [
        ("--", ["后台手动增减分"]),
    ])
]

html_template = """
    <tr class="{row_class}">
        {type_td}
        {platform_td}
        <td class="px-6 py-3 whitespace-nowrap text-sm text-gray-500">{subtype}</td>
        <td class="px-6 py-3 whitespace-nowrap">
            {xp_input}
        </td>
        <td class="px-6 py-3 whitespace-nowrap">
            {toggle}
        </td>
        <td class="px-6 py-3 whitespace-nowrap">
            {limit_config}
        </td>
    </tr>
"""

html_output = []
toggle_counter = 1

for type_name, platforms in data:
    type_rowspan = sum(len(subtypes) for p, subtypes in platforms)
    is_first_in_type = True
    
    for platform_name, subtypes in platforms:
        platform_rowspan = len(subtypes)
        is_first_in_platform = True
        
        for subtype in subtypes:
            if is_first_in_type:
                type_td = f'<td class="px-6 py-3 whitespace-nowrap text-sm font-bold text-gray-900 border-t-2 border-gray-200 bg-gray-50 align-top" rowspan="{type_rowspan}">{type_name}</td>'
                row_class = "border-t-2 border-gray-200 hover:bg-blue-50"
            else:
                type_td = ''
                row_class = "hover:bg-blue-50"
                
            if is_first_in_platform:
                if not is_first_in_type:
                    row_class = "border-t border-gray-100 hover:bg-blue-50"
                platform_td = f'<td class="px-6 py-3 whitespace-nowrap text-sm font-medium text-gray-700 bg-white align-top" rowspan="{platform_rowspan}">{platform_name}</td>'
            else:
                platform_td = ''
                
            is_first_in_type = False
            is_first_in_platform = False
            
            if type_name == "日常类":
                xp_input = '<input type="number" value="2" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">'
                toggle = '<span class="text-sm text-gray-500">--</span>'
                limit_config = """
                    <div class="flex items-center gap-2 limit-config-group">
                        <span class="text-sm font-medium text-gray-700 w-20 text-right">每日最高</span>
                        <input type="number" value="2" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">
                        <span class="text-sm text-gray-500">XP</span>
                    </div>
                """
            elif type_name == "人工干预调账":
                xp_input = '<span class="text-sm text-gray-400">无固定值</span>'
                toggle = '<div class="relative inline-block w-10 align-middle select-none opacity-50"><input type="checkbox" disabled class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none" /><label class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300"></label></div>'
                limit_config = '<span class="text-sm text-gray-400">无上限，需记录操作备注日志</span>'
            else:
                # Default values depending on type to make it look realistic
                default_xp = "10"
                if type_name == "原创": default_xp = "100"
                elif type_name == "转发": default_xp = "20"
                elif type_name == "素材分发作业": default_xp = "30"
                elif type_name == "互动": default_xp = "5"
                
                xp_input = f'<input type="number" value="{default_xp}" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none">'
                toggle = f"""
                    <div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in">
                        <input type="checkbox" id="toggle-{toggle_counter}" checked
                            class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer" />
                        <label for="toggle-{toggle_counter}"
                            class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-300 cursor-pointer"></label>
                    </div>
                """
                limit_config = """
                    <div class="flex items-center gap-2 limit-config-group">
                        <select class="border border-gray-300 rounded-md shadow-sm text-sm p-1.5 focus:border-dfred outline-none bg-white w-28">
                            <option>每日最高</option>
                            <option selected>每月最高</option>
                        </select>
                        <input type="number" value="200" class="w-20 border-gray-300 rounded-md shadow-sm text-sm p-1.5 border focus:border-dfred outline-none disabled:bg-gray-100 disabled:text-gray-400">
                        <span class="text-sm text-gray-500">XP</span>
                    </div>
                """
                toggle_counter += 1
                
            html_output.append(html_template.format(
                row_class=row_class,
                type_td=type_td,
                platform_td=platform_td,
                subtype=subtype,
                xp_input=xp_input,
                toggle=toggle,
                limit_config=limit_config
            ))

tbody_content = "".join(html_output)

# Read file
file_path = "B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Also replace table headers
old_thead = r'<thead class="bg-gray-50">.*?</thead>'
new_thead = """<thead class="bg-gray-50">
                                <tr>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 border-b-2 border-gray-200">作业大类</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 border-b-2 border-gray-200">作业平台</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-48 border-b-2 border-gray-200">作业小类 (系统枚举)</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 border-b-2 border-gray-200">单次发放 XP</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider w-32 border-b-2 border-gray-200">封顶限制开关</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider border-b-2 border-gray-200">限制规则与阀值配置</th>
                                </tr>
                            </thead>"""

html = re.sub(old_thead, new_thead, html, flags=re.DOTALL)

# Replace tbody
old_tbody = r'<tbody class="bg-white divide-y divide-gray-200">.*?</tbody>'
new_tbody = f'<tbody class="bg-white divide-y divide-gray-100">{tbody_content}</tbody>'

html = re.sub(old_tbody, new_tbody, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {toggle_counter - 1} toggles and replaced table body.")
