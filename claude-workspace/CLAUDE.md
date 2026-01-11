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
