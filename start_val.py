from ultralytics import YOLO

model = YOLO("./runs/detect/train/weights/best.pt")

# It'll use the data yaml file in model.pt if you don't set data.
model.val(conf=0.5)
# or you can set the data you want to val
model.val(data="./datasets/boat.yaml", conf=0.5)