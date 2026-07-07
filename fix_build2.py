import re

with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add extraction rule for evidence-modal
new_extraction = """        
    drawer_start_ev = html.find('<div id="evidence-modal-overlay"')
    if drawer_start_ev != -1:
        end_idx = html.find('<script>', drawer_start_ev)
        if end_idx == -1: end_idx = html.find('</body>', drawer_start_ev)
        modals.append(html[drawer_start_ev:end_idx])
        
    return "\\n".join(modals)"""

content = content.replace("return \"\\n\".join(modals)", new_extraction)

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
