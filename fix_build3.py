import re

with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add to template
content = content.replace("{MODALS_USERS}", "{MODALS_USERS}\\n        {MODALS_LEDGER}")

# Add to replacement logic
content = content.replace("final_html.replace('{MODALS_USERS}', modals['users'])", "final_html.replace('{MODALS_USERS}', modals['users'])\\n    final_html = final_html.replace('{MODALS_LEDGER}', modals['ledger'])")

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
