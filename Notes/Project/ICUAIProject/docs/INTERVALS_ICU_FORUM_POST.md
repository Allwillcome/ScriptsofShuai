# Intervals.icu 论坛推广文案

**目标平台**: https://forum.intervals.icu/
**发布板块**: General Discussion 或 Feature Requests
**发布时机**: v0.2.1发布后

---

## 标题选项

### 选项1 (推荐):
**"I built an AI Coach Chrome extension for Intervals.icu - Get instant workout analysis and personalized training plans"**

### 选项2:
**"Introducing Intervals.icu AI Coach - Your Personal Training Assistant Powered by AI"**

### 选项3:
**"[Chrome Extension] AI-powered workout analysis + auto-generated training plans for Intervals.icu"**

---

## 正文 (英文版)

```markdown
# Introducing Intervals.icu AI Coach 🚀

Hey everyone! 👋

I'm a self-coached cyclist/runner and a long-time Intervals.icu user. Like many of you, I love analyzing my training data, but I often found myself staring at charts wondering:

- "Was that interval session too hard?"
- "Why did my heart rate drift in the tempo section?"
- "What should my next workout be to build on this progress?"

As a developer, I thought: **What if AI could help interpret this data and provide instant coaching feedback?**

So I built **Intervals.icu AI Coach** - a Chrome extension that brings AI-powered analysis directly to your Intervals.icu activity pages.

---

## What It Does

### 🎯 1. Instant Workout Analysis
Click "Analyze" on any activity page, and within 10-30 seconds, get:
- Data-driven insights about your performance
- Explanations for unusual patterns (HR drift, power drops, pacing issues)
- Actionable recommendations for improvement

### 📝 2. Personalized Training Plans
Based on your current workout, the AI suggests your next session in **Intervals.icu's native plain text format**:

```intervals
Warmup
- 10m @ 60%

Main Set
- 3 x 8m @ 88-92% with 4m recovery

Cooldown
- 10m easy
```

**One-click copy to clipboard** → paste directly into Intervals.icu 🎉

### ✅ 3. Format Validation (NEW in v0.2.1)
The extension now uses an **AI agent architecture** that:
- Validates generated workouts against Intervals.icu format rules
- Auto-corrects format errors (up to 3 attempts)
- Ensures every workout is ready to import

### 📊 4. Real-time Progress Feedback
See exactly what's happening:
- Step 1: Scraping workout data
- Step 2: Preparing AI request
- Step 3: Generating analysis (shows attempt number if corrections needed)
- Step 4: Validating workout format
- Step 5: Rendering results

---

## Why I Built This

As someone who can't afford a personal coach but wants data-driven training, I needed a way to get quick insights from my workouts. I tried:

❌ **Manual analysis**: Time-consuming, inconsistent
❌ **ChatGPT copy-paste**: Tedious, loses context
❌ **Generic training plans**: Don't adapt to my current fitness

✅ **Intervals.icu AI Coach**: Instant, personalized, integrated

---

## Key Features

- 🤖 **Multi-AI Support**: Works with 13+ AI providers (OpenAI, Claude, DeepSeek, Gemini, etc.)
- 🔒 **Privacy-First**: No data sent to my servers - everything stays between you and your chosen AI service
- ⚡ **Fast**: Analysis in 10-30 seconds
- 🎨 **Clean UI**: Non-intrusive floating widget that blends with Intervals.icu
- 🆓 **Free & Open Source**: MIT License

---

## Example Use Cases

### 🏃 After a Threshold Run:
**AI Analysis**:
> "Your average HR of 168 bpm (92% max) is well-aligned with your lactate threshold pace. The slight HR drift in the final 2km (+5 bpm) suggests you were near your limit - excellent execution of a threshold session.
>
> **Recommended next workout**: A recovery run tomorrow (50-60 minutes @ 65-70% max HR) followed by an interval session in 3-4 days."

### 🚴 After a Sweet Spot Ride:
**AI-Generated Workout**:
```intervals
Warmup
- 15m building from 50% to 70%

Main Set
- 3 x 12m @ 88-92% with 5m @ 65%

Cooldown
- 10m @ 55%
```

---

## How to Use

1. **Install** the extension from Chrome Web Store (link below)
2. **Configure** your AI provider and API key in settings
3. **Navigate** to any Intervals.icu activity page
4. **Click** the "Analyze" button in the floating widget
5. **Get** instant feedback and personalized training plans!

---

## Technical Details (for the curious)

- Built with **Chrome Extension Manifest V3**
- **Agent architecture** with automatic format validation and self-correction
- Comprehensive **workout format validator** (validates time, intensity, structure)
- **Operation logging** for debugging
- Markdown rendering with **one-click copy** for code blocks

The extension extracts your activity data (title, description, summary stats), sends it to your configured AI service, and renders the response. Your API key is stored securely in Chrome's sync storage.

---

## What's Next

I'm actively developing this based on user feedback. Planned features:

- [ ] Training load analysis (multi-day trends)
- [ ] Custom prompt templates
- [ ] Workout library (save and reuse plans)
- [ ] True streaming output (see analysis appear in real-time)

---

## Download & Source Code

- **Chrome Web Store**: [Link will be added after publishing]
- **GitHub**: [Link will be added - star if you find it useful!]
- **Documentation**: Includes format guide, development standards, PRD

---

## I'd Love Your Feedback!

As an Intervals.icu power user, I built this for users like me. I'd really appreciate:

- 🐛 **Bug reports**: What's not working?
- 💡 **Feature ideas**: What would make this more useful?
- ⭐ **General feedback**: Is this solving a real problem for you?

Drop a comment below or open a GitHub issue!

---

## FAQ

**Q: Does this cost money?**
A: The extension is free, but you need your own API key from an AI provider (OpenAI, Claude, etc.). Costs are typically $0.001-0.01 per analysis.

**Q: Is my data secure?**
A: Yes! Nothing is sent to my servers. Data goes directly from the extension to your chosen AI provider using your API key.

**Q: Which AI provider is best?**
A: I recommend:
- **GPT-4o-mini** (OpenAI): Best value, fast, accurate ($0.001/analysis)
- **Claude 3.5 Sonnet** (Anthropic): Most detailed feedback ($0.012/analysis)
- **DeepSeek** (China): Ultra-cheap ($0.0001/analysis)

**Q: Can I customize the analysis prompt?**
A: Yes! You can edit the system prompt in settings to focus on specific aspects (power analysis, HR zones, pacing strategy, etc.)

**Q: Does this work for all sports?**
A: Yes! It works for any activity on Intervals.icu - running, cycling, swimming, triathlon, etc.

---

Hope this helps some of you get more value from your Intervals.icu data! 💪

Happy training! 🚴‍♂️🏃‍♀️

[Your Name]
```

---

## 正文 (中文版 - 备选)

如果目标受众有中文用户，也可准备中文版发布到中文论坛或社区：

```markdown
# 给 Intervals.icu 做了个 AI 教练插件 🚀

大家好！👋

我是一名自我训练的骑行/跑步爱好者，也是 Intervals.icu 的长期用户。和很多人一样，我喜欢分析训练数据，但经常盯着图表发呆：

- "这个间歇训练是不是太猛了？"
- "为什么节奏段心率会飘？"
- "下次该练什么才能更进一步？"

作为开发者，我想：**要是 AI 能帮忙解读数据，提供即时反馈就好了。**

所以我做了 **Intervals.icu AI Coach** - 一个 Chrome 插件，直接在你的 Intervals.icu 活动页面提供 AI 分析。

---

## 它能做什么

### 🎯 1. 即时训练分析
在任何活动页面点"分析"，10-30 秒内得到：
- 基于数据的表现洞察
- 异常模式解释（心率飘移、功率掉速、配速问题）
- 可执行的改进建议

### 📝 2. 个性化训练计划
基于当前训练，AI 会建议你的下一次课表，直接生成 **Intervals.icu 原生格式**：

```intervals
热身
- 10分钟 @ 60%

主课
- 3 组 8分钟 @ 88-92%，组间 4分钟恢复

放松
- 10分钟轻松
```

**一键复制** → 直接粘贴到 Intervals.icu 🎉

### ✅ 3. 格式校验（v0.2.1 新增）
插件现在使用 **AI Agent 架构**：
- 自动验证生成的训练计划格式
- 自动修正格式错误（最多 3 次尝试）
- 确保每个计划都能直接导入

### 📊 4. 实时进度反馈
清楚看到发生了什么：
- 步骤 1：抓取训练数据
- 步骤 2：准备 AI 请求
- 步骤 3：生成分析（如需修正会显示尝试次数）
- 步骤 4：验证训练计划格式
- 步骤 5：渲染结果

---

## 为什么做这个

作为请不起私教但想要数据驱动训练的人，我需要从训练中快速获得洞察。我试过：

❌ **手动分析**：耗时，不一致
❌ **ChatGPT 复制粘贴**：繁琐，丢失上下文
❌ **通用训练计划**：不适应当前状态

✅ **Intervals.icu AI Coach**：即时、个性化、集成

---

[其余内容同英文版...]
```

---

## 发布策略

### 发布时机
1. **Chrome Web Store审核通过后**
2. **自己测试1-2周，确保稳定后**
3. **准备好回复常见问题**

### 互动策略
1. **快速回复**: 24小时内回复所有评论
2. **征集反馈**: 主动问"你们希望看到什么功能？"
3. **展示更新**: 定期发布"Updated to v0.x.x"跟帖
4. **用户案例**: 收集真实用户的使用体验

### 配套资源
- [ ] 录制 2 分钟演示视频
- [ ] 准备 3-5 张功能截图
- [ ] 写一个详细的 API Key 配置教程（图文）

---

## 注意事项

### ✅ 要做的：
- 强调"privacy-first"（不收集数据）
- 说明成本透明（每次分析约$0.001-0.01）
- 提供详细的使用文档
- 积极回应反馈

### ❌ 不要做：
- 过度承诺功能
- 批评竞品或其他工具
- 忽略负面反馈
- 发广告味太重的内容

---

## 预期效果

**乐观估计**:
- 50-100 次点击
- 10-20 次安装
- 3-5 条有价值的反馈

**现实估计**:
- 20-50 次点击
- 5-10 次安装
- 1-2 条反馈

**关键指标**:
- ⭐ 评论互动质量 > 点击量
- ⭐ 有人主动分享体验
- ⭐ 得到核心用户认可

---

**祝发布顺利！🚀**
