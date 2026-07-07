import re

with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken template
content = content.replace("{MODALS_USERS}\\n        {MODALS_LEDGER}", "{MODALS_USERS}\\n        {MODALS_LEDGER}")

# Fix the broken python code
broken_code = "final_html = final_html.replace('{MODALS_USERS}\\n        {MODALS_LEDGER}', modals['users'])"
fixed_code = "final_html = final_html.replace('{MODALS_USERS}', modals['users'])\\n    final_html = final_html.replace('{MODALS_LEDGER}', modals['ledger'])"

content = content.replace(broken_code, fixed_code)

# Clean up literal \n if it happened
content = content.replace("{MODALS_USERS}\\\\n        {MODALS_LEDGER}", "{MODALS_USERS}\\n        {MODALS_LEDGER}")

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
