# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个专门用于 Claude Code 开发和实验的工作目录，用于快速原型开发、技术学习和临时测试。

## 目录结构

- **experiments/** - 实验性代码和新技术尝试，有价值的实验可以提升为正式项目
- **learning/** - 学习新技术、框架、语言的练习代码
- **sandbox/** - 临时测试和沙盒环境，测试完可以随时清理

## Git 管理

- 此目录被父级 Git 仓库 (`ScriptsofShuai`) 管理
- 敏感信息应添加到 `.gitignore`
- 大文件和数据集建议放在其他位置

## 相关目录

- **../Notes/** - 学习笔记和文档
  - `Notes/Biomechanics/` - 生物力学相关项目
  - `Notes/Project/` - 各类项目代码
  - `Notes/Workbook/` - 工作脚本和分析
- **../opencap-api/** - OpenCap API 项目（Django）

## 工作流程

1. 新的实验项目在 `experiments/` 或 `learning/` 中创建独立文件夹
2. 临时快速测试使用 `sandbox/`
3. 成熟的代码考虑移至 `../Notes/Project/` 作为正式项目

## PeakWatch 产品流水线

`experiments/product-pipeline/` 管理 PeakWatch 所有功能的内容生产，每个功能遵循以下流程：

```
PRD → 产品内文章（article/cn.md）→ 多语言翻译（article/en,de,es,jp,kr,tw.md）
                                  ↘ 结合 PRD → GTM（gtm/xiaohongshu.md 等）
```

**目录结构：**
- `features/{功能名}/PRD.md` — 功能说明
- `features/{功能名}/article/` — 中文原文（cn.md）+ 各语言翻译
- `features/{功能名}/gtm/` — 小红书文案等 GTM 内容
- `campaigns/` — 非功能专属的活动/运营内容
- `_specs/` — 翻译规范、文章撰写规范

当用户提到功能更新、新功能上线、PRD 变更时，主动检查对应 `features/` 文件夹，提醒用户同步以下内容（如缺失则点名）：

**⚠️ 内容同步提醒规则：**
当用户提到功能更新、新功能上线、PRD 变更时，主动检查对应 `features/` 文件夹，提醒用户同步以下内容（如缺失则点名）：
1. 是否有 `article/cn.md`（中文原文）
2. 是否完成多语言翻译
3. 是否有 `gtm/` 内容（小红书文案等）

