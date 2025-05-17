import cv2
import numpy as np

def simulate_sensor_data():
    camera = np.zeros((200, 400, 3), dtype=np.uint8)
    lidar = np.random.randint(0, 255, (200, 400), dtype=np.uint8)
    cv2.rectangle(camera, (150, 100), (250, 180), (0, 0, 255), -1)
    return camera, lidar

def fuse_sensors(camera, lidar):
    fused = cv2.addWeighted(camera, 0.7, cv2.cvtColor(lidar, cv2.COLOR_GRAY2BGR), 0.3, 0)
    return fused

camera_img, lidar_img = simulate_sensor_data()
fused_output = fuse_sensors(camera_img, lidar_img)

cv2.imshow("Fused Sensor View", fused_output)
cv2.waitKey(0)
cv2.destroyAllWindows()