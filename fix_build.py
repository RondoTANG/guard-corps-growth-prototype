with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("'<div id=\"xpDrawer\"'", "'<div id=\"xp-drawer-overlay\"'")

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
