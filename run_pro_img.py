import cv2
from ultralytics import YOLO

def prediction_yolo(frame, model):
    results = model(frame, show=True, conf=0.1, device='cpu')
    for result in results:
        predicted_classes = result.boxes.data[:, -1].int()
        predicted_classes_list = predicted_classes.tolist()
        print("--------------------------------")
        print(predicted_classes_list)

# Tạo đối tượng YOLO với mô hình đã tải
model = YOLO('./best_40epoch.pt')

# Đọc ảnh đầu vào
image_path = 'apple_1.jpg'
frame = cv2.imread(image_path)

# Kiểm tra xem ảnh có được đọc thành công không
if frame is None:
    print("Error: Unable to load image.")
else:
    print("--------------------------------")
    # Nhận diện đối tượng bằng YOLO
    prediction_yolo(frame, model)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
