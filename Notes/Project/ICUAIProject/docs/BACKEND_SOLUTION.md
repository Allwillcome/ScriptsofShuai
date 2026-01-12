# 后端服务技术方案 (未来扩展)

**文档状态**: 调研完成，暂不实施
**创建日期**: 2025-01-12
**目的**: 提供免费额度，降低用户使用门槛

---

## 需求背景

当前v0.2.1要求用户自行配置API Key，存在以下问题：

1. **使用门槛高**: 用户需要注册AI服务、获取API Key、配置到扩展
2. **流失率高**: 很多潜在用户在配置环节放弃
3. **开发者自用不便**: 需要频繁切换API Key

**解决方案**: 提供免费额度（如5次），超出后引导用户配置API Key

---

## 架构设计

### 当前架构 (v0.2.1)
```
Chrome扩展 → 用户的API Key → OpenAI/Claude/DeepSeek
```

### 目标架构
```
Chrome扩展 → 后端代理服务 → AI服务 (用开发者的API Key)
             ↓
          额度管理系统
          使用统计
          权限控制
```

---

## 技术方案

### 方案A: Render + SQLite (推荐)

#### 架构组件
1. **后端服务**: Python FastAPI
2. **数据库**: SQLite (持久化到Render磁盘)
3. **部署**: Render.com (免费层)
4. **防休眠**: UptimeRobot (每14分钟ping)

#### 数据库设计
```sql
-- 用户表
CREATE TABLE users (
    extension_id TEXT PRIMARY KEY,     -- Chrome扩展唯一ID
    quota_used INTEGER DEFAULT 0,      -- 已用次数
    quota_total INTEGER DEFAULT 5,     -- 总额度
    role TEXT DEFAULT 'user',          -- user/admin
    created_at TIMESTAMP,
    last_used_at TIMESTAMP
);

-- 使用日志
CREATE TABLE usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    extension_id TEXT,
    timestamp TIMESTAMP,
    model TEXT,                         -- gpt-4o-mini, claude-3.5-sonnet
    tokens_input INTEGER,
    tokens_output INTEGER,
    success BOOLEAN,
    error_message TEXT,
    FOREIGN KEY (extension_id) REFERENCES users(extension_id)
);
```

#### API设计
```
POST /api/analyze
- 参数: { extension_id, activity_data, lang }
- 返回: { success, result, quota_remaining }
- 逻辑:
  1. 检查额度
  2. 调用AI API
  3. 扣减额度
  4. 记录日志

GET /api/quota
- 参数: { extension_id }
- 返回: { quota_used, quota_total, quota_remaining }

POST /admin/users/{extension_id}/quota
- 参数: { quota_total }
- 返回: { success }
- 权限: 仅管理员
```

#### 成本估算

**API调用成本** (GPT-4o-mini):
| 用户数 | 每人额度 | 总调用 | 月成本 |
|--------|---------|---------|--------|
| 50 | 5次 | 250 | $0.25 |
| 200 | 5次 | 1000 | $1.00 |
| 500 | 5次 | 2500 | $2.50 |
| 1000 | 5次 | 5000 | $5.00 |

**服务器成本**: $0 (Render免费层)

**总成本**: $0.25 - $5.00/月

---

### 方案B: Cloudflare Workers + KV

#### 优点
- ✅ 100K请求/天 (远超需求)
- ✅ 全球CDN，零延迟
- ✅ 无休眠问题
- ✅ 完全免费

#### 缺点
- ❌ 学习曲线 (Workers语法)
- ❌ KV数据库不如SQL方便
- ❌ 调试相对复杂

#### 适用场景
- 用户数 > 1000
- 需要全球低延迟
- 长期运营

---

### 方案C: Vercel Serverless

#### 优点
- ✅ 部署简单
- ✅ 无休眠
- ✅ 100GB带宽

#### 缺点
- ❌ 10秒函数超时 (AI调用可能超时)
- ❌ 不适合长时间API调用

#### 结论
**不推荐**，AI响应时间15-30秒会超时

---

## Render免费层限制

| 指标 | 免费额度 | 预估消耗(200用户) | 够用？ |
|------|---------|------------------|-------|
| 运行时间 | 750小时/月 | ~10小时/月 | ✅ |
| RAM | 512MB | ~100MB | ✅ |
| 磁盘 | 1GB | ~50MB | ✅ |
| 带宽 | 100GB/月 | ~1GB/月 | ✅ |
| 请求数 | 无限 | ~1000/月 | ✅ |

**结论**: 完全够用，0-500用户无压力

---

## Chrome扩展改造

### 双模式设计
```javascript
// background.js

async function handleAnalysis(activityData, lang) {
  const config = await chrome.storage.sync.get(['useOwnApiKey', 'apiKey']);

  if (config.useOwnApiKey && config.apiKey) {
    // 模式1: 用户自己的API Key
    return await callAIDirectly(activityData, lang, config);
  } else {
    // 模式2: 免费额度 (调用后端代理)
    return await callBackendProxy(activityData, lang);
  }
}

async function callBackendProxy(activityData, lang) {
  const extensionId = chrome.runtime.id;

  // 1. 检查额度
  const quotaResponse = await fetch('https://your-backend.onrender.com/api/quota', {
    method: 'GET',
    headers: { 'X-Extension-ID': extensionId }
  });

  const quota = await quotaResponse.json();

  if (quota.quota_remaining <= 0) {
    throw new Error('Free quota exceeded. Please configure your own API Key.');
  }

  // 2. 调用分析
  const response = await fetch('https://your-backend.onrender.com/api/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Extension-ID': extensionId
    },
    body: JSON.stringify({ activity_data: activityData, lang })
  });

  const result = await response.json();

  // 3. 显示剩余额度
  console.log(`Quota remaining: ${result.quota_remaining}/5`);

  return result.result;
}
```

### 设置页面改造
```html
<!-- options.html -->
<div class="mode-selector">
  <h3>Usage Mode</h3>

  <label>
    <input type="radio" name="mode" value="free" checked>
    Free Mode (5 analyses/month)
    <span id="quota-display">Remaining: 5/5</span>
  </label>

  <label>
    <input type="radio" name="mode" value="own-key">
    Use My Own API Key (Unlimited)
  </label>
</div>

<div id="api-key-config" style="display:none;">
  <!-- 原有的API Key配置界面 -->
</div>
```

---

## 管理后台设计

### 功能列表
1. **用户管理**
   - 查看所有用户列表
   - 搜索用户 (by extension_id)
   - 修改用户额度
   - 设置用户角色

2. **统计数据**
   - 总用户数
   - 总调用次数
   - 成功率
   - 成本统计

3. **使用日志**
   - 查看最近100条调用
   - 按时间/用户筛选
   - 错误日志查看

### 技术实现
- **框架**: React Admin / Streamlit (Python)
- **认证**: 简单密码 (仅管理员使用)
- **部署**: 同后端服务

---

## 实施计划

### 阶段1: MVP (3-4天)
- [ ] FastAPI后端服务
- [ ] SQLite数据库
- [ ] 基础API (analyze, quota)
- [ ] 部署到Render
- [ ] 配置UptimeRobot

### 阶段2: Chrome扩展集成 (1天)
- [ ] 双模式切换逻辑
- [ ] 额度检查和显示
- [ ] 错误处理和引导

### 阶段3: 管理后台 (1天)
- [ ] 用户列表
- [ ] 额度管理
- [ ] 统计数据

### 阶段4: 测试和发布 (1天)
- [ ] 功能测试
- [ ] 压力测试
- [ ] 监控配置

**总工作量**: 6-7天

---

## 风险和缓解

### 风险1: 用户滥用免费额度
**表现**: 卸载重装骗取额度

**缓解方案**:
1. 用设备指纹 (IP + User Agent) 辅助识别
2. 限制单IP每日注册次数
3. 人工审核异常账户

### 风险2: API成本失控
**表现**: 用户数暴增，成本超预算

**缓解方案**:
1. 设置总额度上限 (如1000次/月)
2. 监控日消耗，超阈值暂停新用户
3. 优先使用DeepSeek (成本低10倍)

### 风险3: 后端服务宕机
**表现**: Render休眠或故障

**缓解方案**:
1. UptimeRobot保持唤醒
2. 添加健康检查 (/health)
3. 自动降级到用户API Key模式

---

## 何时实施

### 触发条件（满足任一）:
1. ✅ Chrome商店安装量 > 100
2. ✅ 用户反馈"配置API Key太复杂"超过10次
3. ✅ 自己需要频繁使用且不想配置API Key

### 建议时机:
- **现在**: ❌ 先验证v0.2.1核心功能
- **发布后2-4周**: ✅ 收集用户反馈后决定
- **安装量>100**: ✅ 证明产品价值后投入

---

## 替代方案

### 方案1: 详细的API Key配置教程
**投入**: 1天编写图文教程
**成本**: $0
**效果**: 可能降低30%的配置难度

### 方案2: 一键配置脚本
**投入**: 半天开发
**成本**: $0
**效果**: 自动打开OpenAI、DeepSeek注册页，引导用户

### 方案3: 视频教程
**投入**: 1天录制和剪辑
**成本**: $0
**效果**: 显著降低配置门槛

**建议**: 先尝试方案1和3，如果仍有大量用户卡住，再实施后端服务

---

## 参考资源

### 部署平台对比
- [Render官方文档](https://render.com/docs)
- [Cloudflare Workers文档](https://developers.cloudflare.com/workers/)
- [Vercel定价](https://vercel.com/pricing)

### 技术栈
- [FastAPI官方文档](https://fastapi.tiangolo.com/)
- [SQLite Python API](https://docs.python.org/3/library/sqlite3.html)
- [UptimeRobot](https://uptimerobot.com/)

### 额度管理参考
- [Stripe Metering](https://stripe.com/docs/billing/subscriptions/usage-based)
- [Supabase Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)

---

## 总结

**技术可行性**: ✅ 高
**经济可行性**: ✅ 高 ($0-5/月)
**优先级**: ⭐⭐⭐ (中等，非紧急)

**当前决策**: 暂不实施，先验证v0.2.1

**未来触发条件**:
- 安装量 > 100
- 用户反馈API Key配置困难

---

**文档维护**:
- 下次更新: 2025-02 (v0.2.1发布后评估)
- 责任人: Shuaibo Wang
