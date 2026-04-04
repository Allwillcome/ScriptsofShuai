#!/bin/bash
# Garmin 速率限制解除后测试脚本

echo "🧪 Testing Garmin connection..."
echo ""

cd /Users/wangshuaibo/Documents/ScriptsofShuai/claude-workspace/learning/garmin-connect-skill/scripts

# Test 1: 尝试重新认证
echo "📋 Test 1: Re-authentication..."
python3 garmin-auth-final.py 2019240860@bsu.edu.cn Garmin2024
AUTH_RESULT=$?

echo ""
echo "---"
echo ""

# Test 2: 尝试同步数据
echo "📋 Test 2: Sync data..."
python3 garmin-sync.py
SYNC_RESULT=$?

echo ""
echo "======================================="
echo "结果汇总:"
echo "======================================="

if [ $AUTH_RESULT -eq 0 ]; then
    echo "✅ 认证成功"
else
    echo "❌ 认证失败 (速率限制可能仍在)"
fi

if [ $SYNC_RESULT -eq 0 ]; then
    echo "✅ 数据同步成功"
else
    echo "❌ 数据同步失败"
fi

echo "======================================="

# 显示缓存文件
if [ -f "$HOME/.clawdbot/.garmin-cache.json" ]; then
    echo ""
    echo "📦 缓存文件内容预览:"
    head -30 "$HOME/.clawdbot/.garmin-cache.json"
fi
