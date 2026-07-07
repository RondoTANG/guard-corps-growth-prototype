import re

file_path = "/Users/RondoT/Documents/护卫军相关/04_成长与激励体系/04_成长体系UI原型/B端_XP资产流水明细表.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Filter Bar
filter_old = """                <div>
                    <label class="block text-xs font-medium text-gray-500 mb-1">变动类型</label>
                    <select class="border border-gray-300 rounded p-1.5 text-sm w-40 focus:border-blue-500 outline-none bg-white">
                        <option>全部类型</option>
                        <optgroup label="增加">
                            <option>作业通过奖励</option>
                            <option>人工干预 (加额)</option>
                        </optgroup>
                        <optgroup label="减少">
                            <option>过期核销扣减</option>
                            <option>人工干预 (扣罚)</option>
                        </optgroup>
                    </select>
                </div>"""

filter_new = """                <div>
                    <label class="block text-xs font-medium text-gray-500 mb-1">变动类型</label>
                    <select class="border border-gray-300 rounded p-1.5 text-sm w-40 focus:border-blue-500 outline-none bg-white">
                        <option>全部类型</option>
                        <optgroup label="增加">
                            <option>作业通过奖励</option>
                            <option>人工干预 (加额)</option>
                        </optgroup>
                        <optgroup label="减少">
                            <option>过期核销扣减</option>
                            <option>人工干预 (扣罚)</option>
                        </optgroup>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-500 mb-1">段位</label>
                    <select class="border border-gray-300 rounded p-1.5 text-sm w-32 focus:border-blue-500 outline-none bg-white">
                        <option>全部段位</option>
                        <option>Level 1 (新秀)</option>
                        <option>Level 2 (熟练)</option>
                        <option>Level 3 (专家)</option>
                        <option>Level 4 (大师)</option>
                    </select>
                </div>"""

html = html.replace(filter_old, filter_new)

# 2. Update Table Header
thead_old = """                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">目标用户</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">变动类型</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">XP 变动额</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">期后 XP 余额</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">关联作业/原因</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">操作人</th>"""

thead_new = """                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">目标用户</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">当前段位</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">变动类型</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">XP 变动额</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">期后 XP 余额</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">关联作业/原因</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">操作凭证</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">操作人</th>"""

html = html.replace(thead_old, list(set([thead_new]))[0] if html.count(thead_old) else thead_old)
if html.count(thead_old): html = html.replace(thead_old, thead_new)

# Row 1 update (Add Tier, add Evidence)
row1_old = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xs mr-3">张三</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">张三 (UID: 10045)</div>
                                        <div class="text-xs text-gray-500">Level 4 (大师)</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">作业通过奖励</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-bold">+150 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">12,450 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <div><a href="#" class="text-blue-600 hover:underline">TASK-20260703-9982</a></div>
                                <div class="text-xs text-gray-400">视频号互动作业</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">系统自动</td>"""

row1_new = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xs mr-3">张三</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">张三</div>
                                        <div class="text-xs text-gray-500">10045 | 138****0001</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800 border border-yellow-200"><i class="fas fa-crown mr-1 mt-0.5"></i> Level 4 (大师)</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">作业通过奖励</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-bold">+150 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">12,450 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <div><a href="#" class="text-blue-600 hover:underline">TASK-20260703-9982</a></div>
                                <div class="text-xs text-gray-400">视频号互动作业</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">-</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">系统自动</td>"""

html = html.replace(row1_old, row1_new)

# Row 2 update (Manual intervention with Evidence)
row2_old = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 font-bold text-xs mr-3">李四</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">李四 (UID: 10088)</div>
                                        <div class="text-xs text-gray-500">Level 2 (熟练)</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800">人工干预 (加额)</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-bold">+500 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">1,450 XP</td>
                            <td class="px-6 py-4 text-sm text-gray-500">
                                <div class="truncate w-48" title="活动额外激励发放">活动额外激励发放</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Admin_Li</td>"""

row2_new = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 font-bold text-xs mr-3">李四</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">李四</div>
                                        <div class="text-xs text-gray-500">10088 | 139****0002</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800 border border-blue-200">Level 2 (熟练)</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800">人工干预 (加额)</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-bold">+500 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">1,450 XP</td>
                            <td class="px-6 py-4 text-sm text-gray-500">
                                <div class="truncate w-48" title="活动额外激励发放">活动额外激励发放</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <button onclick="openEvidenceModal()" class="text-blue-600 hover:text-blue-800 flex items-center gap-1"><i class="fas fa-image"></i> 查看凭证</button>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Admin_Li</td>"""

html = html.replace(row2_old, row2_new)

# Row 3 update
row3_old = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-bold text-xs mr-3">王五</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">王五 (UID: 10201)</div>
                                        <div class="text-xs text-gray-500">Level 1 (新秀)</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">过期核销扣减</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-red-600 font-bold">-200 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">120 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <div>年底 XP 滚动清零</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">系统自动</td>"""

row3_new = """                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                    <div class="h-8 w-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-bold text-xs mr-3">王五</div>
                                    <div>
                                        <div class="text-sm font-medium text-gray-900">王五</div>
                                        <div class="text-xs text-gray-500">10201 | 137****0003</div>
                                    </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800 border border-gray-200">Level 1 (新秀)</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">过期核销扣减</span>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-red-600 font-bold">-200 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">120 XP</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <div>年底 XP 滚动清零</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">-</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">系统自动</td>"""

html = html.replace(row3_old, row3_new)

# Add Evidence Modal HTML and JS at the end
modal_html = """
    <!-- Evidence Modal -->
    <div id="evidence-modal-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-[300] hidden items-center justify-center opacity-0 transition-opacity duration-300">
        <div id="evidence-modal" class="bg-white rounded-lg shadow-xl w-[600px] transform scale-95 opacity-0 transition-all duration-300 flex flex-col max-h-[90vh]">
            <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
                <h3 class="text-lg font-medium text-gray-900">操作凭证详情</h3>
                <button onclick="closeEvidenceModal()" class="text-gray-400 hover:text-gray-500 focus:outline-none">
                    <i class="fas fa-times text-xl"></i>
                </button>
            </div>
            <div class="p-6 overflow-y-auto custom-scrollbar">
                <div class="mb-4">
                    <label class="block text-sm font-medium text-gray-700 mb-2">干预说明</label>
                    <div class="text-sm text-gray-600 bg-gray-50 p-3 rounded border border-gray-200">
                        由于系统故障，导致该用户参与“视频号互动任务”时XP未正常发放。经运营核实，予以手动补发 500 XP。
                    </div>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">附件凭证</label>
                    <div class="border border-gray-200 rounded p-2 bg-gray-50">
                        <img src="https://via.placeholder.com/500x300.png?text=Evidence+Screenshot+1" alt="凭证截图" class="w-full rounded border border-gray-200 shadow-sm cursor-zoom-in">
                    </div>
                </div>
            </div>
            <div class="px-6 py-4 bg-gray-50 text-right border-t border-gray-200 rounded-b-lg">
                <button onclick="closeEvidenceModal()" class="px-4 py-2 bg-white border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none">关闭</button>
            </div>
        </div>
    </div>

    <script>
        function openEvidenceModal() {
            const overlay = document.getElementById('evidence-modal-overlay');
            const modal = document.getElementById('evidence-modal');
            
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
            void overlay.offsetWidth; // reflow
            overlay.classList.remove('opacity-0');
            modal.classList.remove('scale-95', 'opacity-0');
        }

        function closeEvidenceModal() {
            const overlay = document.getElementById('evidence-modal-overlay');
            const modal = document.getElementById('evidence-modal');
            
            overlay.classList.add('opacity-0');
            modal.classList.add('scale-95', 'opacity-0');
            
            setTimeout(() => {
                overlay.classList.add('hidden');
                overlay.classList.remove('flex');
            }, 300);
        }
    </script>
</body>"""

html = html.replace("</body>", modal_html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
