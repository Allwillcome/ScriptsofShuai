---
name: garmin-connect
description: "Garmin Connect integration for Claude Code: sync fitness data (steps, HR, calories, workouts, sleep, Body Battery, HRV, VO2 Max) from international Garmin accounts."
---

# Garmin Connect Skill

同步你的佳明手表数据到 Claude Code，支持全球账号（garmin.com）。

## 🚀 快速开始

### 1. 安装依赖

```bash
cd learning/garmin-connect-skill
pip install -r requirements.txt
```

### 2. 认证（一次性）

```bash
python3 scripts/garmin-auth.py your-email@gmail.com password
```

认证成功后，凭证会加密保存到 `~/.garth/session.json`。

### 3. 同步数据

```bash
# 同步今日数据到缓存文件
python3 scripts/garmin-sync.py ~/.garmin-data.json

# 或使用默认路径 ~/.clawdbot/.garmin-cache.json
python3 scripts/garmin-sync.py
```

### 4. 读取数据

在 Python 中使用 `garmin_db_reader.py` 读取缓存数据：

```python
import sys
sys.path.insert(0, 'learning/garmin-connect-skill/scripts')
from garmin_db_reader import GarminDataReader

# 直接从 API 获取最新数据
from garmin_sync import get_garmin_client, get_daily_summary

client = get_garmin_client()
today_data = get_daily_summary(client, '2026-04-04')
print(f"步数: {today_data['steps']}")
print(f"卡路里: {today_data['calories']}")
```

## 📊 支持的数据

### 基础健康指标
- 步数、卡路里（总/活动/BMR）
- 距离（公里）、爬楼层数
- 活动时长、中等/剧烈运动时长

### 心率数据
- 静息心率、最低/最高心率

### 身体电量（Body Battery）
- 当前电量、最高/最低电量
- 充电值、消耗值

### 压力水平
- 平均压力、最高压力

### 高级指标
- HRV（心率变异性）
- VO2 Max（最大摄氧量）
- 健身年龄
- 呼吸率

### 睡眠数据
- 睡眠时长、睡眠分数
- 深/REM/浅睡时长
- 清醒时间、午睡记录

### 运动记录
- 最近20次运动
- 距离、时长、卡路里、心率

## 🔧 故障排除

### 认证失败
- 检查邮箱密码是否正确
- 确认使用的是全球账号（garmin.com）
- 关闭双因素认证或使用应用专用密码

### 数据为空
- 检查佳明服务器是否有新数据
- 确认手表已同步到 Garmin Connect

### 依赖安装失败
```bash
pip install --upgrade pip
pip install garminconnect garth requests python-dateutil
```

## 📝 脚本说明

- `garmin-auth.py` - 一次性认证脚本
- `garmin-sync.py` - 数据同步脚本（支持所有数据类型）
- `garmin_db_reader.py` - 数据库读取器（兼容接口）

## 🌍 区域支持

此技能默认使用全球账号（garmin.com）。如需使用中国账号，请修改认证脚本添加 `--cn` 参数。
