import cv2
from ultralytics import YOLO
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image



def prediction_yolo(frame, model):
    results = model(frame, show = True ,conf = 0.3, device = 'cpu')
    # Giả sử `results` là danh sách các đối tượng Results
    for result in results:
        # Lấy thông tin về lớp dự đoán
        predicted_classes = result.boxes.data[:, -1].int()

        # Chuyển đổi tensor thành danh sách Python và in ra
        predicted_classes_list = predicted_classes.tolist()
        print("--------------------------------")
        print(predicted_classes_list)
# Tạo đối tượng YOLO với mô hình đã tải
model = YOLO('./best_40epoch.pt')

# Mở video từ webcam hoặc tệp video
cap = cv2.VideoCapture(0)

while True:
    start_time = time.time()
    ret, frame = cap.read()

    if not ret:
        break
    print("--------------------------------")
    # Nhận diện đối tượng bằng YOLO
    prediction_yolo(frame)
    end_time = time.time()
    print("FPS: ", 1/(end_time-start_time))
    start_time = end_time
    # Thoát khỏi vòng lặp khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ video khi kết thúc
cap.release()
cv2.destroyAllWindows()
