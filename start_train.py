from ultralytics import YOLO


model = YOLO('yolov8s.pt')


# Training
results = model.train(
   data='data/data_imgs.yaml',
   imgsz=640,
   epochs=1,
   batch=8,
   save=True,
   device = 'cpu',
   pretrained = True,
   name='yolov8n_custom',
   plots=True
   )     