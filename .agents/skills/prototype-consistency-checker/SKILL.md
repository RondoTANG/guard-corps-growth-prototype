---
name: prototype-consistency-checker
description: 东风护卫军 B 端后台原型 UI 一致性检查与自动修复器。当完成 B 端 HTML 原型修改或新增后，必须调用该技能执行侧边栏菜单、高亮状态的一致性校验。
---

# Prototype Consistency Checker (UI 一致性检查器)

## 技能说明
这是一个针对当前项目的专属 QA 检查技能。由于我们在制作 B 端后台原型时，左侧菜单的 HTML 是完全一样的结构，AI 在复制模板时极易漏掉“高亮选中状态（active-menu）”的切换，导致菜单逻辑错乱。本技能用于在发版前进行全局扫描和自动修复。

## 使用方法
当用户要求检查页面菜单，或者在进行大范围的 HTML 页面复制/修改后，你应该运行以下 Python 脚本：

```bash
python3 scripts/check_and_fix_sidebar.py --fix
```

## 执行逻辑
该脚本会：
1. 扫描当前原型目录下的所有 `B端_*.html` 文件。
2. 提取文件中的 `<aside>` 左侧菜单模块。
3. 自动剥离所有错误残留的高亮背景样式。
4. 根据预设的文件名映射规则（如 `B端_系统设置_文章管理页.html` -> `文章管理`），精准注入 `active-menu` 样式。
5. 自动保存并输出修复报告。
