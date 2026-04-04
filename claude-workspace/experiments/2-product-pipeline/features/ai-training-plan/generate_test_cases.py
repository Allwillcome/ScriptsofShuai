#!/usr/bin/env python3
"""
AI 训练计划测试用例生成器
根据表格用例生成对应的 JSON 文件
"""

import json
import os

# 字段映射配置
GENDER_MAP = {"男": "MALE", "女": "FEMALE"}
FITNESS_LEVEL_MAP = {"初级": "BEGINNER", "中级": "INTERMEDIATE", "高级": "ADVANCED"}
TRAINING_TYPE_MAP = {
    "力量训练": "STRENGTH_TRAINING",
    "有氧训练": "CARDIO",
    "有氧训练/HIIT": "CARDIO",
    "拉伸/柔韧性": "FLEXIBILITY",
    "跑步": "RUNNING",
    "Hybrid混合": "HYBRID",
    "功能性训练": "FUNCTIONAL_TRAINING",
}
DIFFICULTY_MAP = {"简单": "EASY", "适中": "MODERATE", "难": "HARD"}
VENUE_MAP = {"居家": "HOME", "健身房": "GYM", "户外": "OUTDOOR"}

# 测试用例数据（来自用户提供的表格）
TEST_CASES = [
    {
        "id": "LC-01",
        "type": "训练课程",
        "age": 28,
        "gender": "男",
        "heightCm": 175,
        "weightKg": 72,
        "fitnessLevel": "初级",
        "courseTheme": "练胸 - 增肌训练，专注胸部肌肉发展",
        "trainingType": "力量训练",
        "durationMinutes": 30,
        "difficulty": "适中",
        "trainingVenue": "居家",
        "availableEquipment": ["哑铃"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "65 bpm",
        "notes": "典型新手用户"
    },
    {
        "id": "LC-02",
        "type": "训练课程",
        "age": 35,
        "gender": "女",
        "heightCm": 162,
        "weightKg": 58,
        "fitnessLevel": "中级",
        "courseTheme": "翘臀 - 臀腿增肌训练，塑造臀部线条",
        "trainingType": "力量训练",
        "durationMinutes": 45,
        "difficulty": "难",
        "trainingVenue": "健身房",
        "availableEquipment": ["哑铃", "壶铃"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "62 bpm",
        "notes": "进阶女性用户"
    },
    {
        "id": "LC-03",
        "type": "训练课程",
        "age": 42,
        "gender": "男",
        "heightCm": 180,
        "weightKg": 85,
        "fitnessLevel": "中级",
        "courseTheme": "减脂 - 有氧减脂训练，目标减重5kg",
        "trainingType": "有氧训练/HIIT",
        "durationMinutes": 30,
        "difficulty": "难",
        "trainingVenue": "居家",
        "availableEquipment": [],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": ["波比跳"],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "70 bpm",
        "notes": "中年男性减脂"
    },
    {
        "id": "LC-04",
        "type": "训练课程",
        "age": 25,
        "gender": "女",
        "heightCm": 165,
        "weightKg": 52,
        "fitnessLevel": "初级",
        "courseTheme": "拉伸 - 腰背柔韧性提升，缓解腰肌劳损",
        "trainingType": "拉伸/柔韧性",
        "durationMinutes": 20,
        "difficulty": "简单",
        "trainingVenue": "居家",
        "availableEquipment": [],
        "injuryNotes": "腰部",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "一般",
        "sleepQuality": "睡眠一般",
        "hrv": "偏低",
        "restingHeartRate": "68 bpm",
        "notes": "腰肌劳损用户"
    },
    {
        "id": "LC-05",
        "type": "训练课程",
        "age": 30,
        "gender": "男",
        "heightCm": 178,
        "weightKg": 75,
        "fitnessLevel": "高级",
        "courseTheme": "5公里跑 - 跑步速度训练，当前30min→目标25min",
        "trainingType": "跑步",
        "durationMinutes": 40,
        "difficulty": "难",
        "trainingVenue": "户外",
        "availableEquipment": [],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "55 bpm",
        "notes": "跑步进阶用户"
    },
    {
        "id": "LC-06",
        "type": "训练课程",
        "age": 45,
        "gender": "女",
        "heightCm": 160,
        "weightKg": 65,
        "fitnessLevel": "初级",
        "courseTheme": "慢跑 - 5公里跑步训练，心肺能力提升，膝关节有旧伤需注意",
        "trainingType": "跑步",
        "durationMinutes": 25,
        "difficulty": "简单",
        "trainingVenue": "居家",
        "availableEquipment": ["跑步机"],
        "injuryNotes": "膝关节",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "一般",
        "sleepQuality": "睡眠一般",
        "hrv": "正常",
        "restingHeartRate": "72 bpm",
        "notes": "膝关节有旧伤"
    },
    {
        "id": "LC-07",
        "type": "训练课程",
        "age": 33,
        "gender": "男",
        "heightCm": 172,
        "weightKg": 70,
        "fitnessLevel": "中级",
        "courseTheme": "核心强化 - 核心肌群力量训练",
        "trainingType": "力量训练",
        "durationMinutes": 30,
        "difficulty": "适中",
        "trainingVenue": "居家",
        "availableEquipment": ["哑铃"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": ["平板支撑"],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "60 bpm",
        "notes": "核心强化需求"
    },
    {
        "id": "LC-08",
        "type": "训练课程",
        "age": 29,
        "gender": "女",
        "heightCm": 168,
        "weightKg": 56,
        "fitnessLevel": "初级",
        "courseTheme": "全身循环 - 综合体能提升，混合训练",
        "trainingType": "Hybrid混合",
        "durationMinutes": 35,
        "difficulty": "适中",
        "trainingVenue": "居家",
        "availableEquipment": [],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": ["HIIT"],
        "avoidedMovements": ["波比跳"],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "63 bpm",
        "notes": "入门Hybrid"
    },
    {
        "id": "LC-09",
        "type": "训练课程",
        "age": 38,
        "gender": "男",
        "heightCm": 175,
        "weightKg": 78,
        "fitnessLevel": "中级",
        "courseTheme": "背部训练 - 背部肌肉增肌，手肘有网球肘需注意",
        "trainingType": "力量训练",
        "durationMinutes": 50,
        "difficulty": "难",
        "trainingVenue": "健身房",
        "availableEquipment": ["哑铃", "杠铃"],
        "injuryNotes": "手肘",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "58 bpm",
        "notes": "手肘有网球肘"
    },
    {
        "id": "LC-10",
        "type": "训练课程",
        "age": 50,
        "gender": "女",
        "heightCm": 158,
        "weightKg": 62,
        "fitnessLevel": "初级",
        "courseTheme": "体态矫正 - 改善圆肩驼背，适合久坐上班族",
        "trainingType": "功能性训练",
        "durationMinutes": 25,
        "difficulty": "简单",
        "trainingVenue": "居家",
        "availableEquipment": [],
        "injuryNotes": "肩关节,腰部",
        "avoidedTrainingTypes": [],
        "avoidedMovements": ["俯卧撑"],
        "trainingReadiness": "一般",
        "sleepQuality": "睡眠一般",
        "hrv": "偏低",
        "restingHeartRate": "68 bpm",
        "notes": "久坐上班族"
    },
    {
        "id": "LC-11",
        "type": "训练课程",
        "age": 27,
        "gender": "男",
        "heightCm": 182,
        "weightKg": 82,
        "fitnessLevel": "高级",
        "courseTheme": "硬拉训练 - 下肢力量提升，力量举专项",
        "trainingType": "力量训练",
        "durationMinutes": 60,
        "difficulty": "难",
        "trainingVenue": "健身房",
        "availableEquipment": ["杠铃", "史密斯机"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "52 bpm",
        "notes": "力量举用户"
    },
    {
        "id": "LC-12",
        "type": "训练课程",
        "age": 40,
        "gender": "女",
        "heightCm": 163,
        "weightKg": 60,
        "fitnessLevel": "中级",
        "courseTheme": "瑜伽拉伸 - 全身柔韧性提升",
        "trainingType": "拉伸/柔韧性",
        "durationMinutes": 40,
        "difficulty": "简单",
        "trainingVenue": "居家",
        "availableEquipment": [],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "64 bpm",
        "notes": "柔韧性提升"
    },
    {
        "id": "LC-13",
        "type": "训练课程",
        "age": 32,
        "gender": "男",
        "heightCm": 176,
        "weightKg": 74,
        "fitnessLevel": "初级",
        "courseTheme": "椭圆机有氧 - 心肺能力提升，椭圆机入门训练",
        "trainingType": "有氧训练",
        "durationMinutes": 30,
        "difficulty": "简单",
        "trainingVenue": "健身房",
        "availableEquipment": ["椭圆机"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "66 bpm",
        "notes": "有氧器械入门"
    },
    {
        "id": "LC-14",
        "type": "训练课程",
        "age": 23,
        "gender": "女",
        "heightCm": 170,
        "weightKg": 55,
        "fitnessLevel": "中级",
        "courseTheme": "划船机训练 - 心肺能力提升，划船机进阶训练",
        "trainingType": "有氧训练",
        "durationMinutes": 40,
        "difficulty": "适中",
        "trainingVenue": "健身房",
        "availableEquipment": ["划船机"],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "61 bpm",
        "notes": "划船机进阶"
    },
    {
        "id": "LC-15",
        "type": "训练课程",
        "age": 36,
        "gender": "男",
        "heightCm": 174,
        "weightKg": 76,
        "fitnessLevel": "高级",
        "courseTheme": "半马训练 - 半程马拉松备赛，目标2:00完赛",
        "trainingType": "跑步",
        "durationMinutes": 90,
        "difficulty": "难",
        "trainingVenue": "户外",
        "availableEquipment": [],
        "injuryNotes": "无伤病",
        "avoidedTrainingTypes": [],
        "avoidedMovements": [],
        "trainingReadiness": "良好",
        "sleepQuality": "睡眠良好",
        "hrv": "正常",
        "restingHeartRate": "50 bpm",
        "notes": "半马备赛用户"
    },
]


def convert_to_json_format(test_case):
    """将测试用例转换为 JSON 格式"""
    return {
        "title": f'{test_case["id"]} {test_case["courseTheme"].split(" - ")[0]}',
        "age": test_case["age"],
        "gender": GENDER_MAP[test_case["gender"]],
        "heightCm": test_case["heightCm"],
        "weightKg": test_case["weightKg"],
        "fitnessLevel": FITNESS_LEVEL_MAP[test_case["fitnessLevel"]],
        "courseTheme": test_case["courseTheme"],
        "trainingType": TRAINING_TYPE_MAP.get(
            test_case["trainingType"], "STRENGTH_TRAINING"
        ),
        "durationMinutes": test_case["durationMinutes"],
        "difficulty": DIFFICULTY_MAP[test_case["difficulty"]],
        "trainingVenue": VENUE_MAP[test_case["trainingVenue"]],
        "availableEquipment": test_case["availableEquipment"],
        "injuryNotes": (
            "无" if test_case["injuryNotes"] == "无伤病" else test_case["injuryNotes"]
        ),
        "avoidedTrainingTypes": test_case["avoidedTrainingTypes"],
        "avoidedMovements": test_case["avoidedMovements"],
        "trainingReadiness": test_case["trainingReadiness"],
        "sleepQuality": test_case["sleepQuality"],
        "hrv": test_case["hrv"],
        "restingHeartRate": test_case["restingHeartRate"],
    }


def generate_test_cases(output_dir="test_cases"):
    """生成所有测试用例 JSON 文件"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    generated_files = []
    for test_case in TEST_CASES:
        json_data = convert_to_json_format(test_case)
        filename = f'{test_case["id"]}_{json_data["title"]}.json'
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        generated_files.append(filepath)
        print(f"Generated: {filename}")

    print(f"\n✓ 共生成 {len(generated_files)} 个测试用例文件")
    print(f"  输出目录: {output_dir}/")

    return generated_files


if __name__ == "__main__":
    generate_test_cases()
