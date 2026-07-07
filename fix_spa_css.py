import re

file_path = "build_bend_spa.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

if "assets/css/common.css" not in content:
    content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '<script src="https://cdn.tailwindcss.com"></script>\n    <link href="assets/css/common.css" rel="stylesheet">')
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        print("common.css added to build_bend_spa.py")
