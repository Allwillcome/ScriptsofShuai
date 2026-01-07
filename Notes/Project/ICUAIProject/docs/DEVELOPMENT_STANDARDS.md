# Chrome 扩展开发规范

本文档定义了 Intervals.icu AI Coach 扩展的开发、审核和发布标准。所有代码提交前必须遵循本规范。

---

## 一、图标规范

### 1.1 必需的图标尺寸

根据 [Chrome 官方文档](https://developer.chrome.com/docs/extensions/develop/ui/configure-icons)，扩展必须提供以下四个尺寸的图标：

| 尺寸 | 用途 | 是否必需 |
|------|------|----------|
| 16×16 | 网站图标 (favicon) 和上下文菜单图标 | 推荐 |
| 32×32 | Windows 计算机显示 | 推荐 |
| 48×48 | 扩展管理页面 (chrome://extensions) | 推荐 |
| 128×128 | Chrome Web Store 和安装时显示 | **必需** ✅ |

### 1.2 图标格式要求

**推荐格式：** PNG（对透明度支持最好）

**支持的格式：** BMP、GIF、ICO、JPEG、PNG

**不支持的格式：** ❌ SVG、❌ WebP

**参考：** [Manifest Icons Documentation](https://developer.chrome.com/docs/extensions/reference/manifest/icons)

### 1.3 设计要求

- ✅ **必须是正方形**：否则会被扭曲变形
- ✅ **推荐使用透明背景**：PNG 格式提供最佳透明度支持
- ✅ **保持设计一致性**：所有尺寸应保持视觉一致
- ✅ **清晰可辨认**：在小尺寸（16×16）下仍需清晰

### 1.4 Manifest.json 配置

```json
{
  "icons": {
    "16": "icons/icon-16.png",
    "32": "icons/icon-32.png",
    "48": "icons/icon-48.png",
    "128": "icons/icon-128.png"
  }
}
```

### 1.5 生成图标命令

使用 macOS 内置的 `sips` 工具从原始大图生成各尺寸图标：

```bash
# 假设原始图标为 icon-original.png (建议 512×512 或更大)
sips -z 16 16 icon-original.png --out icons/icon-16.png
sips -z 32 32 icon-original.png --out icons/icon-32.png
sips -z 48 48 icon-original.png --out icons/icon-48.png
sips -z 128 128 icon-original.png --out icons/icon-128.png
```

**注意：** 生成后必须检查所有尺寸的图标是否清晰、无失真。

---

## 二、Manifest.json 规范

### 2.1 版本号规范

遵循语义化版本 (Semantic Versioning)：

- **主版本号 (MAJOR)**：不兼容的 API 修改
- **次版本号 (MINOR)**：向后兼容的功能新增
- **修订号 (PATCH)**：向后兼容的问题修复

示例：`"version": "1.2.3"`

### 2.2 权限声明规范

**原则：** 最小权限原则，只申请必需的权限。

#### 2.2.1 Host Permissions

❌ **禁止使用通配符：**
```json
"host_permissions": [
  "*://*/*"  // ❌ 审核会被拒
]
```

✅ **只声明必需的域名：**
```json
"host_permissions": [
  "https://intervals.icu/*",
  "https://api.openai.com/*",
  "https://api.deepseek.com/*",
  "https://openai.api2d.net/*",
  "https://api.anthropic.com/*"
]
```

**说明：**
- 只包含扩展实际访问的域名
- AI API 域名根据实际支持的服务添加
- 审核时需在隐私表单中详细说明每个域名的用途

#### 2.2.2 Permissions

```json
"permissions": [
  "activeTab",    // 读取当前标签页内容
  "scripting",    // 注入脚本
  "storage"       // 存储配置
]
```

**说明：**
- `activeTab`：读取 Intervals.icu 页面的训练数据
- `scripting`：在页面注入 AI Coach 小部件
- `storage`：本地存储 API 密钥等配置

### 2.3 Content Security Policy

遵循 Manifest V3 的默认 CSP，避免不安全的代码执行。

❌ **禁止：**
- 使用 `eval()`
- 内联脚本
- 从远程加载代码

---

## 三、代码开发规范

### 3.1 文件结构

```
intervals-icu-ai-coach/          # 插件根目录（用于打包）
├── manifest.json                # 扩展清单
├── background.js                # 后台脚本
├── content.js                   # 内容脚本
├── options.html                 # 设置页面
├── options.js                   # 设置逻辑
├── styles.css                   # 样式文件
├── prompt.txt                   # AI 提示词模板
└── icons/                       # 图标目录
    ├── icon-16.png
    ├── icon-32.png
    ├── icon-48.png
    └── icon-128.png
```

### 3.2 代码质量要求

- ✅ 无 `console.log` 调试代码（可使用但需在发布前移除）
- ✅ 无硬编码的 API 密钥或敏感信息
- ✅ 错误处理完善，用户友好的错误提示
- ✅ 代码注释清晰，关键逻辑有说明

### 3.3 安全规范

- ✅ 用户输入必须验证和清理
- ✅ API 调用必须使用 HTTPS
- ✅ 敏感数据（API 密钥）存储在 `chrome.storage.sync`
- ✅ 不收集、存储或传输用户数据到开发者服务器

---

## 四、Chrome Web Store 提交规范

### 4.1 提交前检查清单

#### 图标检查
- [ ] 已生成 16×16、32×32、48×48、128×128 四个尺寸
- [ ] 所有图标为 PNG 格式
- [ ] 所有图标为正方形
- [ ] 128×128 图标清晰、无失真
- [ ] manifest.json 中图标路径正确

#### Manifest 检查
- [ ] 版本号符合语义化版本规范
- [ ] `host_permissions` 只包含必需域名（无通配符）
- [ ] `permissions` 说明清晰，符合最小权限原则
- [ ] 扩展名称、描述准确

#### 代码检查
- [ ] 移除所有调试代码（console.log 等）
- [ ] 无硬编码的敏感信息
- [ ] 错误处理完善
- [ ] 在 Intervals.icu 实际测试通过

#### 文档检查
- [ ] README.md 完整
- [ ] CHANGELOG.md 记录版本变更
- [ ] 隐私政策准备就绪（如需要）
- [ ] 商店描述文案准备完毕

### 4.2 打包规范

**打包命令：**
```bash
cd /path/to/ICUAIProject
zip -r intervals-icu-ai-coach.zip intervals-icu-ai-coach/ -x "*.DS_Store" -x "__MACOSX"
```

**检查压缩包：**
```bash
unzip -l intervals-icu-ai-coach.zip
```

确保：
- ✅ 只包含插件文件，无文档、笔记等无关文件
- ✅ 无 `.DS_Store`、`__MACOSX` 等系统文件
- ✅ 文件结构正确，manifest.json 在根目录

### 4.3 隐私表单填写

参考 `docs/chrome-store-submission.md` 中的详细说明。

**关键点：**
- **单一用途**：明确说明扩展只做训练分析
- **权限理由**：每个权限都需详细说明用途
- **数据使用**：明确说明不收集用户数据
- **远程代码**：声明不使用远程代码

---

## 五、版本发布流程

### 5.1 发布前审核

1. **自我审核**：按照本文档 4.1 检查清单逐项检查
2. **本地测试**：在 Chrome 中加载未打包的扩展，完整测试所有功能
3. **隐私审核**：确认不收集、不传输用户数据
4. **文档同步**：更新 CHANGELOG.md 和 version.json

### 5.2 版本号更新

在 `manifest.json` 和 `version.json` 中同步更新版本号。

### 5.3 Git 提交规范

```bash
git add .
git commit -m "chore: release v1.2.3

- 更新图标为标准尺寸（16/32/48/128）
- 修复权限声明
- 优化目录结构
"
git tag v1.2.3
git push origin master --tags
```

---

## 六、审核失败处理流程

### 6.1 常见拒审原因

1. **图标问题**
   - 图标损坏或格式不支持
   - 尺寸不符合要求
   - 图标在小尺寸下不清晰

2. **权限问题**
   - 使用通配符 `*://*/*`
   - 申请了不必要的权限
   - 权限理由说明不清

3. **功能问题**
   - 承诺的功能无法使用
   - 存在 bug 或错误
   - 在测试环境下无法运行

4. **隐私问题**
   - 未披露数据收集行为
   - 隐私政策缺失或不完整

### 6.2 拒审后操作流程

1. **仔细阅读拒审邮件**：记录违规行为参考 ID 和具体原因
2. **本地复现问题**：按照审核团队的描述复现问题
3. **修复问题**：根据本规范和官方文档修复
4. **完整测试**：确保修复后功能正常
5. **更新版本号**：修复后递增 PATCH 版本号
6. **重新提交**：在 Chrome Web Store 后台重新提交

---

## 七、参考资源

### 官方文档
- [Chrome Extensions Documentation](https://developer.chrome.com/docs/extensions)
- [Manifest Icons](https://developer.chrome.com/docs/extensions/reference/manifest/icons)
- [Configure Extension Icons](https://developer.chrome.com/docs/extensions/develop/ui/configure-icons)
- [Manifest V3 Migration](https://developer.chrome.com/docs/extensions/develop/migrate)
- [Developer Program Policies](https://developer.chrome.com/docs/webstore/program-policies)

### 工具
- [Extension Icon Generator](https://www.iconfinder.com/)
- [TinyPNG](https://tinypng.com/) - PNG 压缩工具
- [Chrome Extension Manifest Validator](https://developer.chrome.com/docs/extensions/tools)

---

## 八、更新日志

| 日期 | 版本 | 更新内容 |
|------|------|----------|
| 2025-01-07 | 1.0 | 初始版本，定义图标、manifest、代码开发规范 |

---

**文档维护者：** 王帅波
**最后更新：** 2025-01-07
**文档版本：** 1.0
