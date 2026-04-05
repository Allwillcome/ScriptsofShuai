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

### Hooks 进阶
- [ ] 学习评级系统（1-5 级）
- [ ] PermissionRequest hook
- [ ] PostToolUse 自动化

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

- (暂无)

---

## 已完成

### 2026-04-05 | 学习追踪 Hooks 系统

**收获：**
- 实现了 SessionStart hook，每次会话开始时自动展示学习进度
- 编写了 Python 脚本解析学习日志 Markdown 文件
- 配置了 Shell 包装脚本处理错误和日志
- 理解了 hooks 配置格式和触发时机

**已配置：**
- `~/.claude/scripts/learning-tracker.py` - Python 解析脚本
- `~/.claude/scripts/learning-tracker.sh` - Hook 包装脚本
- `~/.claude/settings.json` - SessionStart hook 配置

**关键认知：**
> **settings.json 是注册表，不是目录结构**
> - 定义"什么时候运行什么"，而不是 Windows 注册表那种复杂的目录结构
> - Hooks 是 Claude Code 主动调用脚本，而不是脚本检测事件
> - 脚本无法"监听"会话开始，必须通过 settings.json 注册
>
> **为什么用 .sh 包装 Python？**
> - 错误隔离：确保脚本失败不阻塞会话
> - 环境管理：设置变量、切换目录
> - 日志记录：统一记录到 ~/.claude/
> - 最佳实践：符合 hooks 生态规范

---

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

---

## 洞见与思考

### 显性知识 vs 隐性知识（2026-04-05）

用户原话：

```
这个 Slash 是一个隐式专家召唤。这点就让我想到了认知科学把知识分为两类：
一类是显性的知识，比如描述性知识，就是我们死记硬背的；
一类是隐性的知识，也就是程序性知识，比如厨师背不下来菜谱，但是能做出好菜。
这个隐性的知识才是专家知识，程序性的知识这块东西可能永远也没有办法完全由 AI 替代，
只能无限的接近专家的思维。
```

**对应关系：**

| 知识类型 | 认知科学 | Claude Code |
|---------|---------|-------------|
| **显性知识** | 描述性知识（死记硬背） | 斜杠命令（明确输入） |
| **隐性知识** | 程序性知识（专家直觉） | Skill（语义匹配） |

**关键洞察：**
> 隐性知识（专家知识）可能永远无法完全被 AI 替代，只能无限接近专家的思维过程。
>
> Skill 系统正是对这种"隐性知识"的工程化尝试——通过意图匹配和领域专家封装，让 AI 逼近人类专家的自然思维模式。

---

### 知识应用路径的里程碑（2026-04-05）

用户原话：

```
现在我能够看到优秀产品中蕴含的科学知识了，下一步就是把科学知识应用到产品、生活中。
我其实已经能够很好的把运动科学知识运用到产品中（PeakWatch），
也能够把认知科学应用到生活中，
现在还需要像 Claude 创始人及其团队一样，把认知科学、生物学运用到 AI 产品的使用当中。
这点是个挺里程碑的时刻。
```

**知识应用地图：**

| 领域 | 科学知识 | 应用场景 | 状态 |
|------|---------|---------|------|
| **运动科学** | 生物力学、训练科学 | PeakWatch 产品设计 | ✅ 已实现 |
| **认知科学** | 行为设计、习惯养成 | 个人生活管理 | ✅ 已实现 |
| **AI 产品使用** | 认知科学、生物学 | Claude Code 工作流 | 🎯 **下一步** |

**学习目标：**
> 像 Anthropic 团队一样，将认知科学和生物学的深层原理应用到 AI 产品的使用方式中，创造更符合人类自然认知的交互模式。
