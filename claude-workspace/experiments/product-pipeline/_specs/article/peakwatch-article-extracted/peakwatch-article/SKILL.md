---
name: peakwatch-article
description: >
  Writing guide for PeakWatch in-app health science articles. Use this skill whenever
  writing, drafting, reviewing, or editing any PeakWatch科普文章 (health science article),
  including when asked to write about fitness metrics (HRV, VO2max, RHR, sleep, training
  load, heart rate zones, etc.), when generating article outlines, when checking article
  quality, or when assigning a URL slug to a new article. Also use when the user says
  "按PeakWatch风格写" or "写一篇PeakWatch科普".
---

# PeakWatch 科普文章写作规范

读完本文件后即可开始写作，无需再确认风格问题。如需参考示例文章结构，见 `references/examples.md`。

---

## 零、撰写前确认

> ⚠️ **每次撰写文章前必须确认**

**必须先问用户：本次是「新增文章」还是「修改已有文章」？**

- **新增文章**：从零开始撰写，考虑新功能的完整性
- **修改已有文章**：需考虑老用户兼容性，确保升级平滑过渡

> 原因：修改已有文章时，某些内容（如 PRD 细节）可能已经存在于旧版本中，需要评估是否需要保留或更新。

---

## 一、定位

| 维度 | 说明 |
|------|------|
| **发布平台** | PeakWatch 应用内科普文章 |
| **目标读者** | 有一定健身基础的运动爱好者；使用 Apple Watch；了解心率区间、有氧/无氧等基础概念，但对生理机制尚不深入 |
| **文章目的** | 解释 PeakWatch 某一指标或功能的科学原理，帮助用户将数据与运动实践结合，强化用户对产品数据的信任 |

---

## 二、语气与风格

**基调：专业克制**——介于「学术科普」与「专业工具说明」之间。有数据支撑但不疲惫，有观点但不说教，实用但不鸡汤。

### 五条核心原则

**1. 直接，不铺垫**
开门见山讲核心概念。读者有基础，不需要从「运动对现代人很重要」开始。

**2. 克制，不煽情**
禁止使用「神奇」「颠覆认知」「你必须知道」等营销化语言。用「通常」「研究表明」而非「一定」「绝对」。

**3. 类比点到即止**
类比可以用，但 1–2 句话为限，不要让类比喧宾夺主。
> ✓ 示例：最大摄氧量是「引擎排量」，本次运动峰值摄氧量是「当前转速」。

**4. 不过度免责**
末尾保留标准免责声明即可，正文中不要反复提示「请咨询医生」。

**5. 过滤 PRD 研发细节**
面向用户的内容只讲「是什么」「有什么用」。以下类型的 PRD 细节不写入科普文章：
- 计算公式、精度处理（如四舍五入保留整数）
- 内部实现逻辑、数据结构
- 仅研发关心的技术细节

判断标准：普通用户看这篇需要知道这个吗？不需要的就不写。

---

## 三、文章结构

标准结构（各模块可根据话题灵活取舍）：

```
1. 定义 / 是什么      →  1–2 段，搭配 1 个类比（可选）
2. 原理 / 为什么重要  →  可拆分 2–3 个 H2 子标题
3. 影响因素 / 如何变化 →  哪些因素影响该指标，为什么波动
4. 实践建议（可选）   →  如何通过训练/生活习惯改善
5. PeakWatch 关联     →  该指标在 PeakWatch 中如何呈现和使用
6. 参考文献           →  APA 格式，见第五节
7. 免责声明           →  固定格式，见第六节
```

### 字数

- **常规文章**：500–800 字（正文，不含参考文献和免责声明）
- **复杂话题**：可延伸至 1000–1500 字，但需用子标题拆分
- 宁可短而精准，不要长而空洞

---

## 四、标题命名

### 文章显示标题（中文）

参照以下命名模式：

| 模式 | 示例 |
|------|------|
| 什么是 X？ | 什么是 HRV？ / 什么是手腕温度？ |
| 关于 X | 关于心率与心率区间 / 关于 METs |
| 了解更多关于 X | 了解更多关于睡眠 |
| X 与 Y | 有氧表现与有氧适能 |
| 描述性短语 | 长期、短期训练负荷与训练疲劳度 |

### URL Slug（英文）

Slug 作为文章 URL 的组成部分，需与中文标题语义对应。规则如下：

**格式规则**
- 全小写英文，单词之间用连字符 `-` 连接
- 不使用下划线、空格、大写字母
- 简洁优先，通常 2–5 个单词
- 使用领域通用英文术语（与 Apple Health / Garmin 等平台保持一致）

**常用术语对照**

| 中文概念 | Slug 用词 |
|----------|-----------|
| 心率变异性 | `hrv` |
| 静息心率 | `resting-heart-rate` 或 `rhr` |
| 最大摄氧量 / 有氧适能 | `vo2max` |
| 心率区间 | `heart-rate-zones` |
| 训练负荷 | `training-load` |
| 训练准备度 / 恢复 | `recovery` |
| 体能输出 | `exertion` |
| 身体电能 | `body-energy` |
| 睡眠 | `sleep` |
| 血氧饱和度 | `spo2` |
| 呼吸节律 | `respiratory-rate` |
| 手腕温度 | `wrist-temperature` |
| 心率恢复 | `heart-rate-recovery` |
| METs / 训练强度 | `mets` |
| 运动后 HRV | `post-workout-hrv` |
| 有氧表现 | `cardio-performance` |
| 能量摄入 | `energy-consumption` |
| 长短期训练负荷比 | `training-load-ratio` |
| 房颤 | `afib` |
| 自觉耗能 | `rpe` |

**命名示例**

| 中文标题 | URL Slug |
|----------|----------|
| 什么是 HRV？ | `hrv` |
| 关于心率与心率区间 | `heart-rate-zones` |
| 训练准备度 | `recovery` |
| 有氧表现与有氧适能 | `vo2max` |
| 了解更多关于睡眠 | `sleep` |
| 长期、短期训练负荷与训练疲劳度 | `training-load-ratio` |
| 运动后心率变异性 | `post-workout-hrv` |

**判断流程**
1. 是否已有领域标准缩写（HRV、VO2max、SpO2、METs）？→ 直接使用
2. 否则，取中文标题最核心的 1–2 个英文词
3. 有同义词时，优先与 Apple Health 的字段名保持一致

### 文件命名

文件名直接使用 URL slug + 语言代码：
- 中文版：`{slug}_cn.md`（如 `rpe_cn.md`）
- 英文版：`{slug}_en.md`（如 `rpe_en.md`）

> ⚠️ 文章内不要显示 `**URL Slug**: xxx`，slug 仅用于文件名和 URL 路径

---

## 五、参考文献规范

### 何时引用

每篇文章至少引用 1 篇相关英文论文。以下情况必须引用：
- 提出具体数值或效果大小
- 引用特定研究发现或权威指南（ACSM、AHA 等）
- 声明某指标是「金标准」或「独立预测因子」

### 论文选择

- 与话题直接相关，发表于同行评审期刊
- 优先：运动科学、心脏病学、应用生理学类期刊
- 近 15 年研究为主；经典文献可用，但搭配近期研究
- 1–3 篇，不堆砌

### APA 第 7 版格式

**期刊论文：**
```
作者姓, 名. (年份). 文章标题. 期刊名, 卷(期), 页码. https://doi.org/xxxxx
```

**示例：**
```
Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics
and norms. Frontiers in Public Health, 5, 258. https://doi.org/10.3389/fpubh.2017.00258

Joyner, M. J., & Coyle, E. F. (2008). Endurance exercise performance: The physiology
of champions. The Journal of Physiology, 586(1), 35–44.
https://doi.org/10.1113/jphysiol.2007.143834
```

> ⚠️ **重要**：AI 辅助写作时，发布前必须逐条人工核查 DOI 真实性，防止幻觉引用。

---

## 六、固定格式元素

### PeakWatch 关联模块标题

统一使用以下标题格式（保持各篇一致）：
- `PeakWatch 如何帮助您监测 X？`
- `X 在 PeakWatch 中的呈现`

### 专业术语首次出现

中文名称后括号标注英文缩写，之后直接使用缩写：
- 心率变异性（HRV）→ 之后写 HRV
- 最大摄氧量（VO₂ Max）→ 之后写 VO₂ Max
- 静息心率（RHR）→ 之后写 RHR
- 自觉耗能（RPE）→ 之后写 RPE

### 免责声明（文章最末，固定不变）

```
本文内容仅用于健康科普，不作为医疗诊断或治疗依据。如有不适，请咨询专业医生。
```

### 涉及权限的功能说明

当文章描述 PeakWatch 读取第三方数据（如苹果健康）时，需提示用户授权：
- 写入方式：「需在苹果健康中授权 PeakWatch 访问该数据」
- 英文对应：「requires authorization in Apple Health settings」

> 示例：PeakWatch 可以读取 Apple Health 中记录的 RPE 数据（**需在苹果健康中授权 PeakWatch 访问该数据**），与苹果生态无缝同步

---

## 七、用词对照

| ✗ 避免 | ✓ 推荐替代 |
|--------|-----------|
| 你一定要了解这个！ | 了解 X，有助于…… |
| 神奇的 / 颠覆认知的 | 研究表明 / 数据显示 |
| 绝对 / 肯定会 | 通常 / 在大多数情况下 |
| 最好的方法就是…… | 目前研究支持的方法包括…… |
| 很多人不知道…… | （直接进入内容，无需铺垫） |
| 每天必须做到…… | 建议结合自身恢复状态灵活调整 |

---

## 八、发布前 Checklist

**内容**
- [ ] 核心概念在开头 1–2 段内清晰定义
- [ ] 数值、效果描述有来源支撑，无过度声明
- [ ] 与 PeakWatch 功能有自然关联，不生硬

**风格**
- [ ] 无营销化语言、无说教语气
- [ ] 术语首次出现已标注中英文对照
- [ ] 字数在目标区间内
- [ ] 无 PRD 研发细节（如计算公式、精度处理）

**结构与格式**
- [ ] 末尾有「参考文献」章节（如有引用）
- [ ] DOI 链接已人工核查，真实有效
- [ ] 末尾有固定免责声明
- [ ] URL slug 已生成，符合命名规范
- [ ] 文件名为 `{slug}_cn.md` / `{slug}_en.md` 格式
- [ ] 文章内无 `**URL Slug**: xxx` 显示
- [ ] 涉及第三方数据读取时有授权说明

---

更多示例文章结构参见 `references/examples.md`。
