# 训练评语生成逻辑

## 概述

基于各子肌群训练容量数据，生成用户训练回顾评语。

## 输入 → 输出流程

```
输入：各子肌群训练容量（如上胸 10组、中下胸 8组、背部 0组）
  ↓
合并规则：
  - 上胸 + 中下胸 → 胸部
  - 上背 + 下背 → 背部
  - 上臀 + 下臀 → 臀部
  - 股四头肌 + 腘绳肌 → 腿部
  - 其他小肌群单独使用（腹部、小腿、肩部、斜方、手臂）
  ↓
输出：
  - 肯定：「近期主要训练了胸部、腿部」
  - 提醒：「背部、腹部还没有训练」
```

## 肌群合并映射

| 合并后肌群 | 子肌群 |
|------------|--------|
| 胸部 | 上胸、中下胸 |
| 背部 | 上背、下背 |
| 臀部 | 上臀、下臀 |
| 腿部 | 股四头肌、腘绳肌 |
| 腹部 | 腹部（单独） |
| 小腿 | 小腿（单独） |
| 肩部 | 肩部（单独） |
| 斜方 | 斜方（单独） |
| 手臂 | 手臂（单独） |

## 评语模板

### 正面评语（训练容量 > 0）

| 合并后肌群 | 评语 |
|------------|------|
| 胸部 | "近期主要训练了胸部" |
| 背部 | "近期主要训练了背部" |
| 臀部 | "近期主要训练了臀部" |
| 腿部 | "近期主要训练了腿部" |
| 腹部 | "近期主要训练了腹部" |
| 小腿 | "近期主要训练了小腿" |
| 肩部 | "近期主要训练了肩部" |
| 斜方 | "近期主要训练了斜方肌" |
| 手臂 | "近期主要训练了手臂" |

### 提醒评语（训练容量 = 0 或过低）

| 合并后肌群 | 评语 |
|------------|------|
| 胸部 | "胸部还没有训练" |
| 背部 | "背部还没有训练" |
| 臀部 | "臀部还没有训练" |
| 腿部 | "腿部还没有训练" |
| 腹部 | "腹部还没有训练" |
| 小腿 | "小腿还没有训练" |
| 肩部 | "肩部还没有训练" |
| 斜方 | "斜方肌还没有训练" |
| 手臂 | "手臂还没有训练" |

## Python 实现示例

```python
# 肌群合并映射
MUSCLE_GROUP_MAPPING = {
    "胸部": ["上胸", "中下胸"],
    "背部": ["上背", "下背"],
    "臀部": ["上臀", "下臀"],
    "腿部": ["股四头肌", "腘绳肌"],
}

# 独立肌群（不需要合并）
INDEPENDENT_MUSCLES = ["腹部", "小腿", "肩部", "斜方", "手臂"]

# 评语模板
POSITIVE_COMMENTS = {
    "胸部": "近期主要训练了胸部",
    "背部": "近期主要训练了背部",
    "臀部": "近期主要训练了臀部",
    "腿部": "近期主要训练了腿部",
    "腹部": "近期主要训练了腹部",
    "小腿": "近期主要训练了小腿",
    "肩部": "近期主要训练了肩部",
    "斜方": "近期主要训练了斜方肌",
    "手臂": "近期主要训练了手臂",
}

REMINDER_COMMENTS = {
    "胸部": "胸部还没有训练",
    "背部": "背部还没有训练",
    "臀部": "臀部还没有训练",
    "腿部": "腿部还没有训练",
    "腹部": "腹部还没有训练",
    "小腿": "小腿还没有训练",
    "肩部": "肩部还没有训练",
    "斜方": "斜方肌还没有训练",
    "手臂": "手臂还没有训练",
}


def merge_muscle_groups(volume_data: dict[str, int]) -> dict[str, int]:
    """合并子肌群容量到主肌群"""
    merged = {}

    # 处理需要合并的肌群
    for main_group, sub_groups in MUSCLE_GROUP_MAPPING.items():
        total = sum(volume_data.get(sub, 0) for sub in sub_groups)
        merged[main_group] = total

    # 处理独立肌群
    for muscle in INDEPENDENT_MUSCLES:
        merged[muscle] = volume_data.get(muscle, 0)

    return merged


def generate_comments(volume_data: dict[str, int]) -> list[str]:
    """生成训练评语"""
    merged = merge_muscle_groups(volume_data)

    positive = []
    reminders = []

    for muscle, volume in merged.items():
        if volume > 0:
            positive.append(POSITIVE_COMMENTS[muscle])
        else:
            reminders.append(REMINDER_COMMENTS[muscle])

    return positive, reminders


def format_output(positive: list[str], reminders: list[str]) -> str:
    """格式化输出"""
    parts = []
    if positive:
        parts.append("、".join(positive[:-1]) + "，" + positive[-1] if len(positive) > 1 else positive[0])
    if reminders:
        parts.append("、".join(reminders[:-1]) + "，" + reminders[-1] if len(reminders) > 1 else reminders[0])

    return "".join(parts)
```

## 使用示例

```python
# 输入：各子肌群训练容量
input_data = {
    "上胸": 10,
    "中下胸": 8,
    "上背": 0,
    "下背": 0,
    "上臀": 5,
    "下臀": 3,
    "股四头肌": 6,
    "腘绳肌": 4,
    "腹部": 0,
    "小腿": 0,
    "肩部": 3,
    "斜方": 0,
    "手臂": 2,
}

positive, reminders = generate_comments(input_data)
output = format_output(positive, reminders)
# 输出: "近期主要训练了胸部、臀部、腿部、肩部、手臂，背部、腹部、小腿、斜方肌还没有训练"
```

## 输出格式

最终输出为一句完整的评语，例如：
- 「近期主要训练了胸部、腿部，腹部、背部还没有训练」
- 「近期主要训练了肩部、手臂」
- 「胸部、背部、腹部、小腿、肩部、斜方肌、手臂都还没有训练」
