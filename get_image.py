import pyrealsense2 as rs
import numpy as np
import cv2
import os
import time

f_drive_path = "F:"

# 创建保存图像的文件夹
output_folder = os.path.join(f_drive_path, 'get_image', 'image_output')
os.makedirs(output_folder, exist_ok=True)

# 配置彩色视频流
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

# 启动视频流
pipeline.start(config)

# # 计时开始时间
# start_time = time.time()
imageName = 1

try:
    # while time.time() - start_time < 10:
    while True:
        # Wait for frames: color
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        
        # 转为numpy数组形式
        color_image = np.asanyarray(color_frame.get_data())

        # 展示图像
        cv2.imshow('Color Image', color_image)

        

        # 保存图像
        if cv2.waitKey(1) & 0xFF == ord('s'):
            color_image_path = os.path.join(output_folder, f'{imageName}.png')
            cv2.imwrite(color_image_path, color_image)
            if os.path.exists(color_image_path):
                print(f'Image {color_image_path} saved successfully.')
                imageName += 1
            else:
                print(f'Failed to save image {color_image_path}.')
        
        
        


        # 按q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # 停止视频流
    pipeline.stop()
    cv2.destroyAllWindows()
