import os
import glob
import re

directory = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型"

files = glob.glob(os.path.join(directory, "C端_*.html"))

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace "个人中心 (入口)" -> "个人中心"
    content = content.replace("个人中心 (入口)</a>", "个人中心</a>")
    content = content.replace("个人中心 (入口)\n", "个人中心\n")
    
    # Replace "成长中心大盘" -> "成长中心" in the menu context
    content = content.replace("成长中心大盘</a>", "成长中心</a>")
    content = content.replace("成长中心大盘\n", "成长中心\n")
    
    # Replace "作业大厅" -> "护卫军首页" in the menu context
    content = content.replace("作业大厅</a>", "护卫军首页</a>")
    content = content.replace("作业大厅\n", "护卫军首页\n")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated menus in {len(files)} files.")
