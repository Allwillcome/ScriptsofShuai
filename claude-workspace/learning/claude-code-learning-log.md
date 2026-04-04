# Claude Code 学习记录

> 记录学习 Claude Code 的进展、收获和待探索的内容

---

## 已完成

### 2026-04-04 | MCP (Model Context Protocol) 配置

**收获：**
- 学会了配置 MCP 服务器
- 理解了 MCP 工作原理：通过 stdio 通信，启动时声明工具列表，AI 根据语义自动调用
- 核心就是三部分：声明工具（ListToolsRequestSchema）、处理调用（CallToolRequestSchema）、业务逻辑（如发 HTTP 请求）

**已配置的 MCP：**
- `flomo-mcp` - 写笔记到 flomo

**关键认知：**
> 学会在干中学、在冒险中学，而不是按部就班

**参考资源：**
- flomo-mcp 源码：`@chatmcp/mcp-server-flomo`
- 配置文件：`.mcp.json`

---

## 进行中

- [ ] MCP 开发实践
  - [ ] 复刻一个简单的 MCP 服务器
  - [ ] 理解完整的 MCP SDK 用法

---

## 待探索

### Zotero CLI 集成 ✅ 已配置

**已选方案：** `cookjohn/zotero-mcp` (580⭐)

**配置方式：** HTTP 传输（本地 Zotero 插件）
```bash
claude mcp add --transport http zotero-mcp http://127.0.0.1:23120/mcp
```

**功能（已可用）：**
- [x] 保存书籍/文献到 Zotero
- [x] 直接打开一本书的内容
- [x] 搜索 Zotero 中的内容
- [x] 智能问答、全文分析

**配置日期：** 2026-04-04

---

### 其他 Claude Code 技能

- [ ] Skills 系统 - 创建自定义技能
- [ ] Hooks 配置 - 自动化工作流
- [ ] Git worktree 隔离开发
- [ ] 并行 Agent 调度

---

## 笔记

### MCP 工作原理简述

```
启动流程：
MCP Server → stdio → Claude 声明工具列表 → 加入系统提示

调用流程：
用户输入 → Claude 理解语义 → 自动匹配工具 → 调用 MCP Server → 返回结果
```

### 配置模板

```json
// .mcp.json
{
  "mcpServers": {
    "服务名": {
      "command": "npx",
      "args": ["-y", "包名"],
      "env": {
        "环境变量": "值"
      }
    }
  }
}
```
