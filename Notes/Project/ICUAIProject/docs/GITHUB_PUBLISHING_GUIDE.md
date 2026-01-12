# GitHub 发布指南

**目标**: 将Intervals.icu AI Coach发布到GitHub，并进行推广

**前提**: 你已有GitHub账号

---

## 📋 准备清单

### ✅ 必需文件（已完成）
- [x] README.md - 项目介绍
- [x] LICENSE - MIT许可证
- [x] CHANGELOG.md - 版本历史
- [x] .gitignore - Git忽略规则
- [x] intervals-icu-ai-coach/ - 扩展源代码
- [x] docs/ - 文档目录

### ⭐ 可选但推荐
- [ ] screenshots/ - 功能截图（强烈推荐）
- [ ] demo.gif - 演示动图
- [ ] CONTRIBUTING.md - 贡献指南
- [ ] CODE_OF_CONDUCT.md - 行为准则

---

## 🚀 发布步骤

### 步骤1: 创建GitHub仓库

#### 方式A: 通过GitHub网站（推荐新手）

1. 访问 [github.com/new](https://github.com/new)

2. 填写仓库信息:
   - **Repository name**: `intervals-icu-ai-coach`
   - **Description**: `AI-powered workout analysis and personalized training plans for Intervals.icu`
   - **Public** (公开仓库)
   - ❌ **不勾选** "Add a README file" (我们已有README)
   - ❌ **不勾选** ".gitignore" (已有)
   - ✅ **选择** "MIT License"

3. 点击 "Create repository"

4. 复制仓库URL（会在下一步使用）:
   ```
   https://github.com/你的用户名/intervals-icu-ai-coach.git
   ```

#### 方式B: 通过命令行

```bash
# 需要先安装 GitHub CLI (gh)
# macOS: brew install gh
# 然后登录: gh auth login

gh repo create intervals-icu-ai-coach \
  --public \
  --description "AI-powered workout analysis and personalized training plans for Intervals.icu" \
  --license mit
```

---

### 步骤2: 准备本地仓库

打开终端，进入项目目录：

```bash
cd /Users/wangshuaibo/Documents/ScriptsofShuai/Notes/Project/ICUAIProject
```

检查Git状态：

```bash
git status
```

---

### 步骤3: 更新README中的链接

在README.md中，将所有 `yourusername` 替换为你的GitHub用户名。

假设你的用户名是 `wangshuaibo`，运行：

```bash
# 方式A: 手动编辑README.md，替换以下内容
# https://github.com/yourusername → https://github.com/wangshuaibo

# 方式B: 用命令替换（macOS/Linux）
sed -i '' 's/yourusername/wangshuaibo/g' README.md
```

提交更改：

```bash
git add README.md
git commit -m "docs: update GitHub username in README"
```

---

### 步骤4: 推送到GitHub

#### 首次推送

如果这是首次推送到GitHub：

```bash
# 添加远程仓库（替换为你的用户名）
git remote add origin https://github.com/wangshuaibo/intervals-icu-ai-coach.git

# 推送到main分支（或master，取决于你的默认分支名）
git branch -M main
git push -u origin main
```

#### 已有远程仓库

如果已经配置过remote：

```bash
# 直接推送
git push
```

---

### 步骤5: 验证发布成功

1. 访问 `https://github.com/你的用户名/intervals-icu-ai-coach`

2. 检查以下内容是否正确显示：
   - ✅ README.md渲染正确
   - ✅ 徽章显示（Version, License等）
   - ✅ 文件结构清晰
   - ✅ LICENSE文件存在

---

### 步骤6: 创建第一个Release

Release可以让用户更方便地下载特定版本。

#### 通过GitHub网站：

1. 进入你的仓库页面

2. 点击右侧 "Releases" → "Create a new release"

3. 填写信息：
   - **Tag**: `v0.2.1`
   - **Release title**: `v0.2.1 - Agent Architecture with Auto Format Validation`
   - **Description**: 从CHANGELOG.md复制v0.2.1的更新内容

   ```markdown
   ## ✨ New Features

   - **Agent-style analysis architecture** with automatic format validation
   - **AI self-correction mechanism** (up to 3 attempts if format errors detected)
   - **Intervals.icu format validator** module
   - **Operation logging system** for debugging

   ## 🎨 Improvements

   - Enhanced progress feedback (4 steps → 5 steps)
   - Real-time progress updates from background script
   - Shows validation status and correction attempts

   ## 📚 Documentation

   - Added testing guide (TESTING_v0.2.1.md)
   - Updated PRD with roadmap

   ## 📦 Installation

   Download `intervals-icu-ai-coach-v0.2.1.zip` below and load it as an unpacked extension in Chrome.

   See [README.md](https://github.com/wangshuaibo/intervals-icu-ai-coach) for detailed installation instructions.
   ```

4. 上传打包文件：

   先在本地打包：
   ```bash
   cd intervals-icu-ai-coach
   zip -r intervals-icu-ai-coach-v0.2.1.zip . -x "*.DS_Store"
   ```

   然后拖拽zip文件到"Attach binaries"区域

5. 点击 "Publish release"

#### 通过命令行：

```bash
# 创建并推送tag
git tag -a v0.2.1 -m "v0.2.1 - Agent Architecture with Auto Format Validation"
git push origin v0.2.1

# 使用GitHub CLI创建release
gh release create v0.2.1 \
  --title "v0.2.1 - Agent Architecture with Auto Format Validation" \
  --notes-file CHANGELOG.md \
  intervals-icu-ai-coach-v0.2.1.zip
```

---

## 📸 准备截图（强烈推荐）

好的截图能大幅提升Star数和安装量。

### 需要的截图

1. **主界面** - intervals-icu-ai-coach widget
2. **分析进度** - 5步进度显示
3. **分析结果** - AI反馈 + 训练计划
4. **设置页面** - API配置界面

### 如何制作

#### 工具推荐
- macOS: 自带截图 (Cmd+Shift+4)
- Chrome: 开发者工具 → 右键元素 → Capture node screenshot
- 编辑工具: macOS Preview / Figma / Canva

#### 最佳实践
- 尺寸: 1280x720 或 1920x1080
- 格式: PNG (高质量) 或 WebP (小体积)
- 内容: 模糊敏感数据（API Key等）
- 命名: `screenshot-main.png`, `screenshot-progress.png`

#### 存放位置
```bash
mkdir -p docs/images
# 将截图放到 docs/images/
```

#### 更新README
在README.md中添加截图区域：

```markdown
## 📸 Screenshots

### Main Interface
![Main Widget](docs/images/screenshot-main.png)

### Analysis Progress
![Progress Feedback](docs/images/screenshot-progress.png)

### Generated Workout Plan
![Workout Plan](docs/images/screenshot-workout.png)

### Settings Page
![Settings](docs/images/screenshot-settings.png)
```

---

## 🎬 制作演示GIF（可选但效果好）

### 工具推荐
- macOS: Kap (免费, https://getkap.co/)
- Windows: ScreenToGif
- 在线: Gifcap

### 录制内容（30秒以内）
1. 打开Intervals.icu活动页面
2. 点击AI Coach widget展开
3. 点击"Analyze"按钮
4. 显示进度条
5. 显示分析结果
6. 点击"Copy"按钮复制训练计划

### 优化GIF
- 压缩: 使用 ezgif.com
- 尺寸: 800px宽度足够
- 帧率: 10-15 fps
- 循环: 设置为循环播放

### 添加到README
```markdown
## 🎬 Demo

![Demo](docs/images/demo.gif)
```

---

## 🏷️ 设置GitHub Topics

Topics可以提高项目可发现性。

1. 进入仓库页面

2. 点击"About"右侧的齿轮图标

3. 添加Topics:
   ```
   chrome-extension
   intervals-icu
   ai-coaching
   workout-analysis
   training-plan
   openai
   claude
   cycling
   running
   triathlon
   endurance-sports
   sports-analytics
   ```

4. 保存

---

## 📢 推广策略

### GitHub内推广

1. **GitHub Trending**
   - 让朋友Star你的项目（前几个Star很重要）
   - 活跃开发（频繁commit）
   - 完善README和文档

2. **GitHub Topics**
   - 关注相关Topic下的项目
   - 参与讨论
   - 在issue中帮助别人

### 社区推广

#### Intervals.icu论坛（主战场）
- 发布时机: Chrome审核通过后
- 发布内容: 使用 `docs/INTERVALS_ICU_FORUM_POST.md`
- 持续互动: 每天查看回复，快速响应

#### Reddit
- [r/intervals_icu](https://reddit.com/r/intervals_icu)
- [r/chrome_extensions](https://reddit.com/r/chrome_extensions)
- 标题: "I built an AI Coach extension for Intervals.icu"

#### Hacker News
- 时机: 等Star数>50时
- 标题: "Show HN: AI Coach for Intervals.icu (Chrome Extension)"
- 要点: 强调技术亮点（Agent架构, 自我修正等）

#### Twitter/X
- Hashtags: #intervalsicu #cycling #running #aicoach
- @intervals_icu (官方账号可能转发)

### 技术社区

- **Product Hunt** (等功能更完善)
- **Dev.to** (写技术文章介绍实现过程)
- **Medium** (写故事性文章)

---

## 📊 监控指标

跟踪以下数据以评估效果：

| 指标 | 目标(首月) | 跟踪方式 |
|------|-----------|---------|
| GitHub Stars | 20+ | GitHub Insights |
| GitHub Forks | 3+ | GitHub Insights |
| Chrome安装量 | 50+ | Chrome Web Store Dashboard |
| 论坛讨论回复 | 10+ | 手动统计 |
| Issues提交 | 3+ | GitHub Issues |

---

## ⚠️ 注意事项

### 不要做
- ❌ 买Stars或Forks（会被封号）
- ❌ 在无关仓库发spam
- ❌ 发布未经测试的代码
- ❌ 忽略用户反馈

### 要做
- ✅ 快速响应Issues（24小时内）
- ✅ 接受合理的PR
- ✅ 定期更新文档
- ✅ 保持代码质量

---

## 🔄 后续维护

### 每周
- 检查GitHub Issues
- 回复论坛讨论
- 更新CHANGELOG

### 每月
- 发布新版本（如有重要功能）
- 分析用户反馈
- 优化README

### 每季度
- 重大功能更新
- 写技术博客
- 参与社区活动

---

## 📝 需要你提供的信息

为了完成发布，我需要你提供：

### 必需信息
1. **GitHub用户名**: `wangshuaibo` (你已提供)
2. **邮箱** (可选，用于GitHub commits): `your.email@example.com`
3. **个人网站/社交链接** (可选):
   - Twitter: @yourhandle
   - LinkedIn: linkedin.com/in/yourprofile

### 可选信息
- **项目背景故事**: 为什么做这个项目？
- **真实使用案例**: 有没有用这个工具提升训练的经历？
- **未来计划**: 接下来想做什么功能？

---

## 🎯 快速命令参考

所有命令汇总（复制即用）：

```bash
# 1. 进入项目目录
cd /Users/wangshuaibo/Documents/ScriptsofShuai/Notes/Project/ICUAIProject

# 2. 检查状态
git status

# 3. 更新README中的用户名（替换wangshuaibo为你的实际用户名）
sed -i '' 's/yourusername/wangshuaibo/g' README.md
git add README.md
git commit -m "docs: update GitHub username in README"

# 4. 添加远程仓库（首次）
git remote add origin https://github.com/wangshuaibo/intervals-icu-ai-coach.git

# 5. 推送到GitHub
git branch -M main
git push -u origin main

# 6. 打包扩展
cd intervals-icu-ai-coach
zip -r intervals-icu-ai-coach-v0.2.1.zip . -x "*.DS_Store"
cd ..

# 7. 创建Release tag
git tag -a v0.2.1 -m "v0.2.1 - Agent Architecture with Auto Format Validation"
git push origin v0.2.1
```

---

## 🆘 常见问题

### Q: git push失败，提示authentication failed
A: 需要配置GitHub个人访问令牌（Personal Access Token）:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token → 勾选 `repo` 权限
3. 复制token
4. 推送时用token替代密码

### Q: README中的图片不显示
A: 检查图片路径是否正确，GitHub使用相对路径:
```markdown
✅ ![Screenshot](docs/images/screenshot.png)
❌ ![Screenshot](/Users/wangshuaibo/...)
```

### Q: 想修改已发布的Release
A:
- 进入Releases页面
- 点击Release旁的Edit按钮
- 修改后Save

### Q: 想删除并重新创建仓库
A:
```bash
# 删除本地remote
git remote remove origin

# GitHub网站删除仓库，然后重新创建
# 再次添加remote
git remote add origin https://github.com/wangshuaibo/new-repo.git
git push -u origin main
```

---

**准备好了就开始发布吧！🚀**

有任何问题随时问我！
