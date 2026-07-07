with open("build_bend_spa.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("build_bend_spa.py", "w", encoding="utf-8") as f:
    for line in lines:
        if "{MODALS_USERS}\\n        {MODALS_LEDGER}" in line:
            f.write("        {MODALS_USERS}\n        {MODALS_LEDGER}\n")
            continue
        if "final_html = final_html.replace('{MODALS_USERS}', modals['users'])\\n    final_html = final_html.replace('{MODALS_LEDGER}', modals['ledger'])" in line:
            f.write("    final_html = final_html.replace('{MODALS_USERS}', modals['users'])\n")
            f.write("    final_html = final_html.replace('{MODALS_LEDGER}', modals['ledger'])\n")
            continue
        f.write(line)

