# Claude Code 学习记录

> 记录学习 Claude Code 的进展、收获和待探索的内容

## 目录

- [待探索](#待探索)
- [进行中](#进行中)
- [已完成](#已完成)
- [技术笔记](#技术笔记)

---

## 待探索

### Skills 系统
- [ ] 创建自定义技能
- [ ] 理解技能的懒加载机制
- [ ] 技能触发条件配置

### Hooks 配置
- [ ] 自动化工作流
- [ ] PermissionRequest hook
- [ ] 通知钩子

### Git worktree
- [ ] 隔离开发环境
- [ ] Worktree 管理最佳实践

### 并行 Agent 调度
- [ ] 多任务并行处理
- [ ] Agent 通信机制

### MCP 开发实践
- [ ] 复刻一个简单的 MCP 服务器
- [ ] 理解完整的 MCP SDK 用法

---

## 进行中

### Claude Code 深度使用
- 正在探索 MCP 工具描述和 token 占用
- 研究智谱内置 MCP vs 自建 MCP 的区别
- 学习 Context Window 管理和对话历史压缩

---

## 已完成

### 2026-04-05 | MCP 工具描述与 Context Window

**收获：**
- 理解 MCP 工具描述的格式和 token 占用
- 一个 MCP 服务器约 50-200 tokens 的工具描述
- Skill 采用懒加载机制，不占用常驻 context
- GLM-4.5 Context Window 为 128K tokens

**关键认知：**
> MCP 工具描述会随每次请求发送给模型，所以不能配置太多。建议常驻 5-10 个核心 MCP，项目特定 MCP 放 `.mcp.json`。

---

### 2026-04-04 | Zotero CLI 集成 ✅

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

---

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

## 技术笔记

### MCP 工具描述格式示例

```json
{
  "name": "mcp__flomo__write_note",
  "description": "Write note to flomo",
  "inputSchema": {
    "type": "object",
    "properties": {
      "content": {
        "type": "string",
        "description": "Text content of the note with markdown format"
      }
    },
    "required": ["content"]
  }
}
```

### Context Window 构成

```
128K tokens 总池
├── 输入部分（约 80-100K）
│   ├── 系统提示词：~2K
│   ├── MCP 工具描述：~1-5K
│   ├── 历史对话：~50-80K
│   └── 当前用户消息：~1K
│
└── 输出部分（剩余 28-48K）
    └── 模型单次回复
```

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
