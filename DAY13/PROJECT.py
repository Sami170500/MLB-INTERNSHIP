from ultralytics import YOLO
model=YOLO('yolov8s.pt')
results = model.predict(
    source="DATASET HELMETS/images",
    conf=0.5,
    save=True,
    show=True
)
