import re
import requests
import sys
import os
from datetime import datetime, timedelta

def get_song_id(url: str) -> str:
    """从网易云歌曲链接中提取歌曲ID"""
    match = re.search(r'id=(\d+)', url)
    if not match:
        raise ValueError("链接中没有找到歌曲ID")
    return match.group(1)

def get_lyrics(song_id: str) -> str:
    """通过网易云API获取歌词"""
    api_url = f"https://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://music.163.com/"
    }
    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    if "lrc" in data and "lyric" in data["lrc"]:
        return data["lrc"]["lyric"]
    else:
        return "未找到歌词"

def lrc_to_srt(lrc_content: str) -> str:
    """将LRC格式歌词转换为SRT格式"""
    if not lrc_content or lrc_content == "未找到歌词":
        return ""
    
    # 解析LRC格式的时间戳和歌词
    lines = lrc_content.strip().split('\n')
    srt_lines = []
    subtitle_index = 1
    
    for line in lines:
        # 匹配LRC时间戳格式 [mm:ss.xxx]
        match = re.match(r'\[(\d{2}):(\d{2})\.(\d{2,3})\](.*)', line)
        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            milliseconds = int(match.group(3).ljust(3, '0')[:3])  # 确保是3位毫秒
            text = match.group(4).strip()
            
            # 跳过空行和制作信息
            if not text or text.startswith('作词') or text.startswith('作曲') or text.startswith('编曲') or text.startswith('制作'):
                continue
            
            # 计算开始时间
            start_time = timedelta(minutes=minutes, seconds=seconds, milliseconds=milliseconds)
            
            # 设置结束时间（默认显示3秒，如果有下一句则到下一句开始）
            end_time = start_time + timedelta(seconds=3)
            
            # SRT时间格式：HH:MM:SS,mmm
            start_str = str(start_time).split('.')[0] + ',' + str(start_time.microseconds // 1000).zfill(3)
            end_str = str(end_time).split('.')[0] + ',' + str(end_time.microseconds // 1000).zfill(3)
            
            # 添加小时部分（如果需要）
            if ':' not in start_str[:2]:
                start_str = '00:' + start_str
            if ':' not in end_str[:2]:
                end_str = '00:' + end_str
                
            srt_lines.append(f"{subtitle_index}")
            srt_lines.append(f"{start_str} --> {end_str}")
            srt_lines.append(text)
            srt_lines.append("")  # 空行分隔
            
            subtitle_index += 1
    
    return '\n'.join(srt_lines)

def get_song_info(song_id: str) -> dict:
    """获取歌曲信息"""
    api_url = f"https://music.163.com/api/song/detail/?id={song_id}&ids=[{song_id}]"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://music.163.com/"
    }
    try:
        resp = requests.get(api_url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        if "songs" in data and len(data["songs"]) > 0:
            song = data["songs"][0]
            return {
                "name": song.get("name", "未知歌曲"),
                "artist": song["artists"][0]["name"] if song.get("artists") else "未知歌手"
            }
    except:
        pass
    return {"name": "未知歌曲", "artist": "未知歌手"}

def main():
    if len(sys.argv) < 2:
        print("用法: python get_lyrics.py <网易云歌曲链接>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        song_id = get_song_id(url)
        
        # 获取歌曲信息
        song_info = get_song_info(song_id)
        print(f"正在获取歌曲: {song_info['name']} - {song_info['artist']}")
        
        # 获取歌词
        lyrics = get_lyrics(song_id)
        
        if lyrics == "未找到歌词":
            print("未找到歌词")
            return
            
        print("歌词内容：\n")
        print(lyrics)
        
        # 转换为SRT格式
        srt_content = lrc_to_srt(lyrics)
        
        if srt_content:
            # 生成文件名（去除特殊字符）
            safe_name = re.sub(r'[<>:"/\\|?*]', '_', f"{song_info['name']}_{song_info['artist']}")
            filename = f"{safe_name}.srt"
            
            # 保存SRT文件
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(srt_content)
            
            print(f"\n✅ SRT字幕文件已保存为: {filename}")
            print("可以直接导入到剪映中使用！")
        else:
            print("\n❌ 转换SRT格式失败")
            
    except Exception as e:
        print("出错了：", e)

if __name__ == "__main__":
    main()