#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE_DIR="$(dirname "$SCRIPT_DIR")"
FEATURE_NAME="$(basename "$FEATURE_DIR")"

cd "$SCRIPT_DIR"
OUTPUT="${FEATURE_DIR}/${FEATURE_NAME}.zip"

# 删除旧文件
[ -f "$OUTPUT" ] && rm "$OUTPUT"

zip -j "$OUTPUT" *.md
echo "✅ 已生成：${FEATURE_NAME}.zip"
read -p "按回车关闭..."
