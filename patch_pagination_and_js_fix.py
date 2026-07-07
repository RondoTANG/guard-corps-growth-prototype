import re

filepath = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_成长数据健康度大盘.html"
with open(filepath, "r") as f:
    content = f.read()

# Fix Pagination: it should be outside overflow-x-auto
# Let's find the pagination div
pag_idx = content.find('<div class="px-6 py-4 border-t border-gray-200 flex items-center justify-between">')
if pag_idx != -1:
    # Find the end of this div
    # It ends with '</div>' (actually it has some nested divs)
    # Let's use regex or string manipulation
    end_pag_idx = content.find('</div>\n</div>\n</div>', pag_idx)
    # Wait, the structure is:
    # <div class="bg-white border border-gray-200 rounded-md shadow-sm overflow-x-auto mb-6">
    #   <table ...> ... </table>
    #   <div class="px-6 py-4 border-t... pagination ...</div>
    # </div>
    pass

