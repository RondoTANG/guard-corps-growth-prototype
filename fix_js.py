import re

file_path = "B端_等级规则与XP配置页.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

robust_js = """        // Toggle Event Listener for Limits
        document.addEventListener('DOMContentLoaded', () => {
            const toggles = document.querySelectorAll('.toggle-checkbox');
            toggles.forEach(toggle => {
                toggle.addEventListener('change', (e) => {
                    const tr = e.target.closest('tr');
                    if (!tr) return;
                    const container = tr.querySelector('.limit-config-group');
                    if (!container) return;

                    const inputs = container.querySelectorAll('select, input[type="number"]');
                    if (e.target.checked) {
                        container.classList.remove('opacity-50', 'pointer-events-none', 'grayscale');
                        inputs.forEach(el => el.disabled = false);
                    } else {
                        container.classList.add('opacity-50', 'pointer-events-none', 'grayscale');
                        inputs.forEach(el => el.disabled = true);
                    }
                });
                
                // Initialize
                const evt = new Event('change');
                toggle.dispatchEvent(evt);
            });
        });"""

html = re.sub(r'// Toggle Event Listener for Limits.*?}\);(?=\s*</script>)', robust_js, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
