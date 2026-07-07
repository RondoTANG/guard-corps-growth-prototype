import re

with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add extraction rule for privilege-drawer and toast-container
new_extraction = """        
    drawer_start_priv = html.find('<div id="privilege-drawer-overlay"')
    if drawer_start_priv != -1:
        end_idx = html.find('<script>', drawer_start_priv)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start_priv)
        modals.append(html[drawer_start_priv:end_idx])

    toast_container_start = html.find('<div id="toast-container"')
    if toast_container_start != -1:
        end_idx = html.find('</div>', toast_container_start) + 6
        modals.append(html[toast_container_start:end_idx])

    return "\\n".join(modals)"""

content = content.replace("return \"\\n\".join(modals)", new_extraction)

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
