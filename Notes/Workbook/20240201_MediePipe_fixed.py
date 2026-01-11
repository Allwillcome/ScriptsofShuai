from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    # 循环可视化姿势
    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        # 绘制姿势标记点
        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
            annotated_image, 
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style()
        )
    return annotated_image

# 加载并显示原始图像
img_path = "/Users/wangshuaibo/Downloads/girl-4051811_960_720.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"无法加载图像: {img_path}")
    print("请确保图像文件存在，或者使用其他图像文件")
    # 使用一个示例图像路径
    img_path = input("请输入图像文件的完整路径: ")
    img = cv2.imread(img_path)

if img is not None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将BGR图像转换为RGB图像

    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("原始图像")
    plt.axis("off")

    # 检查模型文件是否存在
    model_path = '/Users/wangshuaibo/Downloads/pose_landmarker_full.task'
    import os
    if not os.path.exists(model_path):
        print(f"模型文件不存在: {model_path}")
        print("请从 https://developers.google.com/mediapipe/solutions/vision/pose_landmarker 下载模型文件")
    else:
        try:
            # 创建姿势点识别
            base_options = python.BaseOptions(model_asset_path=model_path)
            options = vision.PoseLandmarkerOptions(
                base_options=base_options
            )
            detector = vision.PoseLandmarker.create_from_options(options)

            # 加载输入的图像 - 使用 RGB 格式
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

            # 进行图像识别
            detection_result = detector.detect(image)

            # 处理图像识别结果，此处为可视化
            annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
            
            plt.subplot(1, 2, 2)
            plt.imshow(annotated_image)
            plt.title("姿态检测结果")
            plt.axis('off')
            
            print(f"检测到 {len(detection_result.pose_landmarks)} 个人体姿态")
            
        except Exception as e:
            print(f"姿态检测过程中出现错误: {e}")
            print("请确保已正确安装 mediapipe 库")

    plt.tight_layout()
    plt.show()
else:
    print("无法加载图像文件")