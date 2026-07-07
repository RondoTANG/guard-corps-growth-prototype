import re

css_file = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/assets/css/common.css"
with open(css_file, "r") as f:
    content = f.read()

content = content.replace(
    ".toggle-checkbox { right: 0; z-index: 1; border-color: #e5e7eb; transition: all 0.3s; }",
    ".toggle-checkbox { left: 0; z-index: 1; border-color: #e5e7eb; transition: all 0.3s; }\n.toggle-checkbox:checked { left: calc(100% - 1.25rem); border-color: #E01E2E; }"
)

with open(css_file, "w") as f:
    f.write(content)
