---
name: decision-log
description: Extract and document decision-making patterns from conversations. Use when the user discusses a product decision, trade-off analysis, or problem-solving process and wants to capture the reasoning for future reference. Triggers on phrases like "帮我总结这个决策", "记录一下这个决定", "抽象一下这个问题", or requests to document decision rationale.
allowed-tools: Read Write
metadata:
  author: wangshuaibo
  version: "1.0.0"
  domain: project
---

# DecisionLog Skill

Extract decision-making insights from conversation context and save as structured Markdown files.

## When to Use This Skill

Use this skill when the user:
- Makes a product or design decision and wants to document it
- Discusses trade-offs between different approaches
- Wants to capture reasoning for future reference
- Says phrases like "帮我总结这个决策", "记录一下这个决定", "抽象一下这个问题"

## Workflow

When invoked, follow these steps:

1. **Identify the decision point** from the conversation context
2. **Extract key elements:**
   - Problem type and background
   - Core tension or trade-off
   - Options considered (with pros/cons)
   - Final decision and reasoning
   - Concerns at decision time
   - Underlying principle
3. **Generate Markdown** in the specified format below
4. **Save to file** at `claude-workspace/decisions/YYYY-MM-DD-{short-title}.md`

## Output Format

```markdown
# {Case Title}

## 背景
{Describe the context and what triggered the decision}

## 冲突点
{The core tension or trade-off}

## 具体例子
{A concrete scenario illustrating the problem}

- 方案 A（{label}）：{description} → {consequence}
- 方案 B（{label}）：{description} → {consequence}
- 方案 C（{label}）：{description} → {consequence}

## 我的决策
{What was decided and the reasoning}

## 决策时的担忧
{Concerns at decision time, to revisit later}

## 决策原则提炼
> **{One-sentence principle extracted from this decision}**
```

## Writing Guidelines

- **Write in first person (第一人称)** — this is the user's decision log
- **Keep it concise** — no filler, just the essential reasoning
- **Make principles actionable** — they should be reusable in future decisions
- **Title captures the problem** — not the solution (e.g., "权限设计：功能完整性 vs 用户体验简洁性")
- **Mark unvalidated concerns** — use "待验证" if the concern hasn't been tested yet
- **Include concrete examples** — abstract principles without context are less useful

## Example Trigger Phrases

The user might say:
- "帮我总结一下这个决策"
- "把这个问题抽象一下"
- "记录下我的思考过程"
- "形成决策案例"
- "这个决定值得存档"

## File Management

- **File path:** `claude-workspace/decisions/YYYY-MM-DD-{short-title}.md`
- **Naming pattern:** Use kebab-case for the title (e.g., `2026-01-05-feature-vs-simplicity.md`)
- **Date format:** YYYY-MM-DD (ISO 8601)

## Example Output

See `claude-workspace/decisions/` for accumulated decision logs.

---

## Implementation Notes

When implementing this skill:
1. Read the full conversation context to understand the decision
2. Ask clarifying questions if the decision is ambiguous
3. Use the Write tool to save the file
4. Confirm the file path to the user after saving
